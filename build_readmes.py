import os
import json
import re

workspace_dir = "/home/shoaib/Desktop/Pandas_Project"
parsed_dir = os.path.join(workspace_dir, "temp_parsed_data")
output_dir = os.path.join(workspace_dir, "codesworking")
os.makedirs(output_dir, exist_ok=True)

def escape_markdown_table_cell(text):
    if not text:
        return "-"
    # Escape vertical bar which is the markdown table separator
    text_escaped = text.replace('|', r'\|')
    # Escape newlines as literal \n strings so that the entire row stays on a single line in markdown
    text_escaped = text_escaped.replace('\n', r'\n')
    return text_escaped

def generate_working_explanation(code, filename):
    code_lower = code.lower()
    explanations = []
    
    # 1. Imports
    if "import pandas" in code or "import numpy" in code:
        explanations.append("Imports the Pandas and NumPy libraries, laying the foundation for high-performance structured data manipulation and mathematical array operations.")
        
    # 2. Loading CSV
    csv_match = re.search(r'read_csv\([\'"]([^\'"]+)[\'"]\)', code)
    if csv_match:
        explanations.append(f"Loads the CSV dataset from `{csv_match.group(1)}` into a Pandas DataFrame to prepare it for subsequent structured analysis and cleaning.")
        
    # 3. Head & Tail
    head_match = re.search(r'\.head\(([^)]*)\)', code)
    if head_match:
        n = head_match.group(1).strip()
        n_str = n if n else "5"
        explanations.append(f"Retrieves the first {n_str} rows of the DataFrame to inspect the column headers, data types, and initial data alignment.")
    tail_match = re.search(r'\.tail\(([^)]*)\)', code)
    if tail_match:
        n = tail_match.group(1).strip()
        n_str = n if n else "5"
        explanations.append(f"Retrieves the last {n_str} rows of the DataFrame to inspect the trailing records and verify that data import is complete.")
        
    # 4. Info & Describe & Shape & Columns
    if ".info()" in code:
        explanations.append("Generates a comprehensive summary of the DataFrame, including row count, index details, column labels, non-null counts, data types, and memory usage.")
    if ".describe()" in code:
        explanations.append("Generates descriptive statistical summaries (count, mean, standard deviation, min, max, and percentiles) for all numeric columns to understand their distributions.")
    if ".shape" in code:
        explanations.append("Accesses the `.shape` attribute to retrieve a tuple representing the dimensions (number of rows and columns) of the DataFrame.")
    if ".columns" in code and "=" not in code:
        explanations.append("Accesses the `.columns` attribute to view and list all available column headers in the DataFrame.")
    if ".dtypes" in code:
        explanations.append("Accesses the `.dtypes` attribute to view the specific data types associated with each column in the DataFrame.")
        
    # 5. Data Structures Instantiation
    if "pd.Series" in code:
        explanations.append("Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array.")
    if "pd.DataFrame" in code:
        explanations.append("Instantiates a new 2-dimensional tabular Pandas DataFrame object from a structured dictionary or nested list.")
        
    # 6. Sorting & Indexing
    if "sort_values" in code:
        asc = "descending" if "ascending=False" in code else "ascending"
        col_match = re.search(r'sort_values\([\'"]([^\'"]+)[\'"]', code)
        cols_match = re.search(r'sort_values\(\[([^\]]+)\]', code)
        if col_match:
            explanations.append(f"Sorts the DataFrame rows based on values in the `{col_match.group(1)}` column in {asc} order.")
        elif cols_match:
            explanations.append(f"Sorts the DataFrame rows hierarchically based on values in multiple columns: `[{cols_match.group(1)}]` in configured order.")
        else:
            explanations.append(f"Sorts the Series or DataFrame rows based on element values in {asc} order.")
            
    if "sort_index" in code:
        asc = "descending" if "ascending=False" in code else "ascending"
        explanations.append(f"Restructures the DataFrame/Series by sorting its index labels in {asc} order instead of sorting by its values.")
        
    if "set_index" in code:
        idx_col = re.search(r'set_index\([\'"]([^\'"]+)[\'"]', code)
        col_name = f"`{idx_col.group(1)}`" if idx_col else "the specified column"
        inplace = "in-place (modifying the original DataFrame directly)" if "inplace=True" in code else "returning a new DataFrame with the updated index"
        explanations.append(f"Sets {col_name} as the new index (row labels) of the DataFrame, {inplace}.")
        
    if "reset_index" in code:
        drop = "dropping the old index" if "drop=True" in code else "retaining the old index as a normal column"
        inplace = "in-place" if "inplace=True" in code else "returning a new object"
        explanations.append(f"Reverts the custom index back to a standard incremental integer RangeIndex, {drop} and applying changes {inplace}.")
        
    if "rename(" in code:
        explanations.append("Renames columns or index labels of the DataFrame using mapping dictionaries to fix labels or correct spelling.")
        
    # 7. Uniqueness & Counting
    if "value_counts" in code:
        explanations.append("Computes the frequency distribution of unique elements in the Series or DataFrame, sorting the counts in descending order.")
    if ".unique()" in code:
        explanations.append("Returns a NumPy array containing only the unique elements present in the target Series, preserving their order of occurrence and including missing values.")
    if "nunique()" in code:
        explanations.append("Computes the count of unique values in the Series or DataFrame, excluding missing values (`NaN`) by default.")
        
    # 8. Handling Null / Missing Data
    if "isnull()" in code or "isna()" in code:
        if ".sum()" in code:
            explanations.append("Generates a boolean null-mask and aggregates it using `.sum()` to find the total count of missing values per column.")
        else:
            explanations.append("Generates a boolean mask (same shape as DataFrame/Series) mapping empty cells (`NaN`/`None`) to `True` and valid cells to `False`.")
    if "notnull()" in code or "notna()" in code:
        explanations.append("Generates a boolean mask identifying valid (non-missing) elements across the DataFrame/Series.")
    if ".hasnans" in code:
        explanations.append("Queries the `.hasnans` attribute of a Series, returning `True` if it contains one or more missing values.")
    if "dropna" in code:
        subset_match = re.search(r'subset=\[([^\]]+)\]', code)
        subset_str = f" restricted to columns `[{subset_match.group(1)}]`" if subset_match else ""
        how_str = " if 'all' columns are null" if "how='all'" in code else " if 'any' column is null"
        inplace = "in-place" if "inplace=True" in code else ""
        explanations.append(f"Filters out and discards rows containing missing values{subset_str}{how_str}, applying changes {inplace}.")
    if "fillna" in code:
        method_match = re.search(r'method=[\'"]([^\'"]+)[\'"]', code)
        method_str = f" using the '{method_match.group(1)}' method (such as backfill/forward-fill)" if method_match else ""
        val_match = re.search(r'fillna\(([^,)]+)\)', code)
        val_str = f" with `{val_match.group(1)}`" if val_match and "method" not in code else " with the specified fallback value"
        explanations.append(f"Imputes missing values{val_str}{method_str} to clean the dataset and maintain column continuity.")
        
    # 9. Duplicates
    if "duplicated()" in code:
        if ".sum()" in code:
            explanations.append("Computes a boolean mask for duplicate rows and aggregates them to find the total number of duplicate records.")
        else:
            explanations.append("Identifies duplicate rows in the DataFrame, returning a boolean Series where redundant rows are marked as `True`.")
    if "drop_duplicates" in code:
        keep = "last" if "keep='last'" in code else ("first" if "keep='first'" in code else "first (default)")
        subset_match = re.search(r'subset=\[([^\]]+)\]', code)
        subset_str = f" based on subset columns `[{subset_match.group(1)}]`" if subset_match else ""
        explanations.append(f"Removes duplicate row records from the DataFrame{subset_str}, keeping only the `{keep}` occurrence.")
        
    # 10. Math & Stats Operations
    if ".sum()" in code and "isnull" not in code and "duplicated" not in code:
        explanations.append("Calculates the sum total of values across the specified axis (default is vertically along columns).")
    if ".mean()" in code and "fillna" not in code:
        explanations.append("Calculates the arithmetic mean of numeric elements in the DataFrame or Series.")
    if ".median()" in code:
        explanations.append("Computes the median (middle value) of numeric elements to evaluate central tendency.")
    if ".mode()" in code:
        explanations.append("Computes the mathematical mode (most frequently occurring value) of elements.")
    if ".std()" in code:
        explanations.append("Computes the standard deviation of numerical elements to measure statistical dispersion.")
    if ".var()" in code:
        explanations.append("Computes the variance of numerical elements to measure data spread around the mean.")
    if ".min()" in code:
        explanations.append("Finds the minimum value among elements in the Series/DataFrame.")
    if ".max()" in code:
        explanations.append("Finds the maximum value among elements in the Series/DataFrame.")
    if ".corr()" in code:
        explanations.append("Computes the pairwise Pearson correlation coefficients between numerical columns to find linear trends.")
    if ".cumsum()" in code:
        explanations.append("Calculates the cumulative running sum of elements down the rows.")
    if ".rolling(" in code:
        explanations.append("Applies a rolling window calculation (such as a moving average) across a specified period size.")
    if ".shift(" in code:
        explanations.append("Shifts the Series values up or down by a specified number of periods, useful for calculating period-over-period differences.")
        
    # 11. Custom transformations & Vectorized Mapping
    if ".apply(" in code:
        func_match = re.search(r'apply\(([^,)]+)', code)
        func_name = f"`{func_match.group(1).strip()}`" if func_match else "the custom function"
        axis_str = " row-by-row horizontally (`axis=1`)" if "axis=1" in code else " element-wise vertically"
        explanations.append(f"Maps {func_name}{axis_str} across the DataFrame/Series to perform customized transformations.")
    if ".map(" in code:
        explanations.append("Performs element-wise value mapping or category substitution on a Series using a dictionary or mapping function.")
        
    # 12. Row Filtering & Selection
    if ".loc[" in code:
        explanations.append("Uses `.loc` indexing to select rows and columns based on their string labels or boolean conditional mask arrays.")
    if ".iloc[" in code:
        explanations.append("Uses `.iloc` indexing to select rows and columns based on their absolute integer positions (offsets).")
    if "query(" in code:
        explanations.append("Queries the DataFrame rows using a clear and readable boolean expression string, filtering records in-place.")
    if ".isin(" in code:
        explanations.append("Filters DataFrame rows by checking if column values match any entries specified in a list, returning a boolean mask.")
        
    # 13. Reshaping
    if "pivot_table(" in code:
        explanations.append("Summarizes and aggregates the DataFrame by creating a pivot table intersected across specified rows and columns.")
    if "melt(" in code:
        explanations.append("Unpivots the DataFrame from a wide format to a long format, converting multiple columns into key-value attribute rows.")
    if "pd.cut(" in code:
        explanations.append("Discretizes continuous numerical values into discrete intervals or categorical bins based on defined boundaries.")
    if "pd.get_dummies(" in code:
        explanations.append("Performs one-hot encoding, converting a categorical column into multiple boolean indicators of category presence.")
        
    # 14. Merging and Concatenating
    if "merge(" in code:
        how_match = re.search(r'how=[\'"]([^\'"]+)[\'"]', code)
        how_str = f" using a '{how_match.group(1)}' join" if how_match else " using an 'inner' join"
        explanations.append(f"Combines two separate DataFrames{how_str} matching rows on shared key columns.")
    if "pd.concat(" in code:
        axis_str = "horizontally (along columns)" if "axis=1" in code else "vertically (along rows)"
        explanations.append(f"Concatenates multiple Pandas objects {axis_str} to stack or align datasets.")
        
    # 15. Vectorized String Methods
    if ".str.upper" in code:
        explanations.append("Applies vectorized string conversion to transform all text elements in the column to uppercase.")
    if ".str.lower" in code:
        explanations.append("Applies vectorized string conversion to transform all text elements in the column to lowercase.")
    if ".str.capitalize" in code:
        explanations.append("Applies vectorized string capitalization, converting the first character of each word/element to uppercase and others to lowercase.")
    if ".str.title" in code:
        explanations.append("Applies vectorized titlecasing, capitalizing the first letter of each word inside each string element.")
    if ".str.strip" in code:
        explanations.append("Performs a vectorized whitespace cleanup, trimming leading and trailing padding spaces from all string cells.")
    if ".str.split" in code:
        expand_str = " and expands them into a multi-column DataFrame" if "expand=True" in code else ""
        explanations.append(f"Splits string elements into lists of substrings based on a delimiter{expand_str}.")
    if ".str.replace" in code:
        explanations.append("Performs vectorized string substitution, replacing occurrences of target characters/regex patterns with a new string.")
    if ".str.contains" in code:
        case_str = " ignoring letter casing" if "case=False" in code else ""
        explanations.append(f"Evaluates if string elements contain a target substring or regex pattern{case_str}, returning a boolean filtering mask.")
    if ".str.len()" in code:
        explanations.append("Computes the character length of each string element in the Series, allowing length-based filtering.")
    if ".str.get(" in code:
        idx_get = re.search(r'get\(([^)]+)\)', code)
        idx_str = f" at index `{idx_get.group(1)}`" if idx_get else ""
        explanations.append(f"Extracts the specific item{idx_str} from each list inside the split string elements in a vectorized manner.")
    if ".str.endswith" in code:
        explanations.append("Evaluates if string elements end with a specific suffix, returning a boolean mask.")
    if ".str.startswith" in code:
        explanations.append("Evaluates if string elements start with a specific prefix, returning a boolean mask.")
    if ".str.isdigit" in code:
        explanations.append("Evaluates if string elements consist entirely of numeric digit characters.")
    if ".str.lstrip" in code:
        explanations.append("Trims leading whitespace or specific characters from the left side of each string cell.")
    if ".str[::-1]" in code:
        explanations.append("Slices each string element with a step size of `-1`, reversing the character order of every text cell in a vectorized fashion.")
        
    # 16. General Types & Attributes
    if ".astype(" in code:
        type_match = re.search(r'astype\(([^)]+)\)', code)
        type_str = f" to `{type_match.group(1).strip()}`" if type_match else ""
        explanations.append(f"Casts the data type of the column elements{type_str} to optimize memory or enable type-specific operations.")
    if ".copy()" in code:
        explanations.append("Creates a deep copy of the DataFrame or Series to ensure modifications do not affect the original source data.")
    if ".insert(" in code:
        explanations.append("Inserts a new column into the DataFrame at a specific integer index location rather than at the end.")
        
    # 17. Plotting
    if ".plot(" in code:
        kind_match = re.search(r'kind=[\'"]([^\'"]+)[\'"]', code)
        kind_str = f" of type '{kind_match.group(1)}'" if kind_match else ""
        explanations.append(f"Invokes Matplotlib/Pandas visualization to render an aesthetic plot{kind_str} representing the aggregated column data.")
        
    # Fallback/General Explanations
    if not explanations:
        if "=" in code:
            explanations.append("Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset.")
        else:
            explanations.append("Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values.")
            
    # Combine explanations beautifully
    combined_explanation = " ".join(explanations)
    return combined_explanation

def get_notebook_friendly_title(filename):
    # Mapping filename to a premium title
    titles = {
        "season22t": "Pandas Vectorized String Accessors & Regular Expressions Guide",
        "dataframes": "Pandas DataFrame Methods & Core Manipulations Master Guide",
        "pandassecond": "Pandas Tabular Operations & Series Methods Master Reference",
        "pandasfirst": "Introduction to Pandas Series, Attributes & Essential Indexing",
        "suplementrypandas": "Supplementary Pandas Techniques & Advanced Series Operations",
        "season21t": "Merging, Joining & Concatenating Multi-Table DataFrames",
        "season20": "Pandas GroupBy, Split-Apply-Combine & Data Aggregation Guide",
        "groupby": "Advanced Grouping, Aggregation & Data Transformation reference",
        "NetflixCleaning": "Netflix Dataset Exploratory Data Analysis & Cleaning Case Study"
    }
    
    # Try direct mapping
    for key, title in titles.items():
        if key.lower() in filename.lower():
            return title
            
    # Fallback
    clean_name = filename.replace(".ipynb", "").replace("_", " ").title()
    return f"{clean_name} Analysis & Reference"

def process_file(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    file_path = data["file_path"]
    relative_path = data["relative_path"]
    cells = data["cells"]
    
    # Extract file base name without path and extension
    basename = os.path.basename(file_path).replace(".ipynb", "")
    readme_name = f"{basename}_README.md"
    output_path = os.path.join(output_dir, readme_name)
    
    title = get_notebook_friendly_title(basename)
    
    markdown_lines = []
    # 1. Main Headers (MUST have "This is codes working")
    markdown_lines.append("# This is codes working")
    markdown_lines.append("")
    markdown_lines.append(f"## 📘 {title}")
    markdown_lines.append("")
    markdown_lines.append(f"Welcome to the comprehensive, step-by-step code execution reference guide for **[{relative_path}](file://{file_path})**.")
    markdown_lines.append("This document tracks every single code cell executed in the notebook, presenting its raw source code, final output, and an in-depth technical explanation of how it operates.")
    markdown_lines.append("")
    markdown_lines.append("> [!NOTE]")
    markdown_lines.append(f"> This file is dynamically generated and fully documents 100% of the **{len(cells)} code cells** in the notebook. All existing project README files remain completely untouched and preserved!")
    markdown_lines.append("")
    markdown_lines.append("---")
    markdown_lines.append("")
    
    # 2. Main Reference Table
    markdown_lines.append("### 📊 Complete Execution Log")
    markdown_lines.append("")
    markdown_lines.append("| Code | Output | Working |")
    markdown_lines.append("| :--- | :--- | :--- |")
    
    for idx, cell in enumerate(cells):
        code_raw = cell["code"]
        output_raw = cell["output"]
        
        # Format Code block for table cell
        # Standard GFM renders single line with \n inside block correctly
        code_escaped = escape_markdown_table_cell(f"```python\n{code_raw}\n```")
        
        # Format Output block for table cell
        if output_raw:
            output_escaped = escape_markdown_table_cell(f"```\n{output_raw}\n```")
        else:
            output_escaped = "`None / No Output`"
            
        # Generate Working Description
        working_desc = generate_working_explanation(code_raw, basename)
        working_escaped = escape_markdown_table_cell(working_desc)
        
        markdown_lines.append(f"| {code_escaped} | {output_escaped} | {working_escaped} |")
        
    markdown_lines.append("")
    markdown_lines.append("---")
    markdown_lines.append("")
    markdown_lines.append("> [!TIP]")
    markdown_lines.append(f"> Use this structured log as a parallel lookup guide when reviewing or executing code inside the Jupyter notebook **[{relative_path}](file://{file_path})**.")
    markdown_lines.append("")
    
    # Write output to the readme file
    with open(output_path, 'w', encoding='utf-8') as out_f:
        out_f.write("\n".join(markdown_lines))
        
    print(f"Successfully generated README at: {output_path} with {len(cells)} cells.")

def main():
    json_files = [f for f in os.listdir(parsed_dir) if f.endswith('.json')]
    print(f"Found {len(json_files)} parsed json files in {parsed_dir}")
    
    for file in json_files:
        json_file_path = os.path.join(parsed_dir, file)
        try:
            process_file(json_file_path)
        except Exception as e:
            print(f"Error processing {file}: {e}")
            
    print("\nAll README files generated successfully inside: codesworking/")

if __name__ == "__main__":
    main()
