import os
import json
import re

workspace_dir = "/home/shoaib/Desktop/Pandas_Project"
scratch_dir = os.path.join(workspace_dir, "temp_parsed_data")
os.makedirs(scratch_dir, exist_ok=True)

# Regex to strip ANSI escape codes
ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

def clean_ansi(text):
    return ansi_escape.sub('', text)

def parse_notebook(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # In-memory fix for dataframes.ipynb malformed JSON
    if "dataframes.ipynb" in filepath:
        # Replace the missing bracket block
        bad_block = '"source": [\n    "### set_index(dataframe) -> inplace"\n  },'
        good_block = '"source": [\n    "### set_index(dataframe) -> inplace"\n   ]\n  },'
        if bad_block in content:
            content = content.replace(bad_block, good_block)
        else:
            # Try with different whitespace just in case
            content = re.sub(
                r'"source":\s*\[\s*"### set_index\(dataframe\) -> inplace"\s*\},',
                r'"source": [\n    "### set_index(dataframe) -> inplace"\n   ]\n  },',
                content
            )
            
    try:
        nb = json.loads(content)
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return None
    
    parsed_cells = []
    cells = nb.get('cells', [])
    code_index = 1
    for cell in cells:
        if cell.get('cell_type') == 'code':
            # Extract source code
            source = "".join(cell.get('source', []))
            if not source.strip():
                # Skip empty code cells
                continue
            
            # Extract and format outputs
            formatted_outputs = []
            outputs = cell.get('outputs', [])
            for out in outputs:
                out_type = out.get('output_type')
                if out_type == 'stream':
                    text = "".join(out.get('text', []))
                    formatted_outputs.append(clean_ansi(text))
                elif out_type in ['execute_result', 'display_data']:
                    data = out.get('data', {})
                    if 'text/plain' in data:
                        text = "".join(data['text/plain'])
                        formatted_outputs.append(clean_ansi(text))
                elif out_type == 'error':
                    ename = out.get('ename', 'Error')
                    evalue = out.get('evalue', '')
                    tb = "".join(out.get('traceback', []))
                    formatted_outputs.append(clean_ansi(f"{ename}: {evalue}\n{tb}"))
            
            combined_output = "\n".join(formatted_outputs).strip()
            
            parsed_cells.append({
                "cell_index": code_index,
                "code": source.strip(),
                "output": combined_output
            })
            code_index += 1
            
    return parsed_cells

def main():
    ipynb_files = []
    for root, dirs, files in os.walk(workspace_dir):
        # Exclude hidden directories like .git
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'temp_parsed_data' and d != 'codesworking']
        for file in files:
            if file.endswith('.ipynb'):
                ipynb_files.append(os.path.join(root, file))
                
    print(f"Found {len(ipynb_files)} ipynb files:")
    for f in ipynb_files:
        print(f" - {f}")
        
    for filepath in ipynb_files:
        relative_path = os.path.relpath(filepath, workspace_dir)
        cells = parse_notebook(filepath)
        if cells is not None:
            # We will save the parsed content into a json file in the scratch directory
            # replacing directory separators and extension
            safe_name = relative_path.replace(os.sep, "__").replace(".ipynb", ".json")
            out_path = os.path.join(scratch_dir, safe_name)
            with open(out_path, 'w', encoding='utf-8') as out_f:
                json.dump({
                    "file_path": filepath,
                    "relative_path": relative_path,
                    "cells": cells
                }, out_f, indent=2)
            print(f"Saved parsed notebook data to {out_path} (cells: {len(cells)})")

if __name__ == "__main__":
    main()
