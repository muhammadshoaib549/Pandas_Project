# This is codes working

## 📘 Pandas Vectorized String Accessors & Regular Expressions Guide

Welcome to the comprehensive, step-by-step code execution reference guide for **[season22t.ipynb](file:///home/shoaib/Desktop/Pandas_Project/season22t.ipynb)**.
This document tracks every single code cell executed in the notebook, presenting its raw source code, final output, and an in-depth technical explanation of how it operates.

> [!NOTE]
> This file is dynamically generated and fully documents 100% of the **18 code cells** in the notebook. All existing project README files remain completely untouched and preserved!

---

### 📊 Complete Execution Log

| Code | Output | Working |
| :--- | :--- | :--- |
| ```python\nimport pandas as pd\nimport numpy as np\n``` | `None / No Output` | Imports the Pandas and NumPy libraries, laying the foundation for high-performance structured data manipulation and mathematical array operations. |
| ```python\na = np.array([1,2,3,4])\na * 4\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\ns = ['cat','mat',None,'rat']\ntry:\n    [i.startswith('c') for i in s]\nexcept AttributeError as e:\n    print("AttributeError:", e)\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\ns = pd.Series(['cat','mat',None,'rat'])\n# string accessor\ns.str.startswith('c')\n``` | `None / No Output` | Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. Evaluates if string elements start with a specific prefix, returning a boolean mask. |
| ```python\ndf = pd.read_csv('titanic.csv')\ndf['Name']\n``` | `None / No Output` | Loads the CSV dataset from `titanic.csv` into a Pandas DataFrame to prepare it for subsequent structured analysis and cleaning. |
| ```python\ndf['Name'].str.upper()\ndf['Name'].str.capitalize()\ndf['Name'].str.title()\n``` | `None / No Output` | Applies vectorized string conversion to transform all text elements in the column to uppercase. Applies vectorized string capitalization, converting the first character of each word/element to uppercase and others to lowercase. Applies vectorized titlecasing, capitalizing the first letter of each word inside each string element. |
| ```python\ndf['Name'][df['Name'].str.len() == 82].values[0]\n``` | `None / No Output` | Computes the character length of each string element in the Series, allowing length-based filtering. |
| ```python\n"                   nitish                              ".strip()\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\ndf['Name'].str.strip()\n``` | `None / No Output` | Performs a vectorized whitespace cleanup, trimming leading and trailing padding spaces from all string cells. |
| ```python\ndf['lastname'] = df['Name'].str.split(',').str.get(0)\ndf.head()\n``` | `None / No Output` | Retrieves the first 5 rows of the DataFrame to inspect the column headers, data types, and initial data alignment. Splits string elements into lists of substrings based on a delimiter. Extracts the specific item at index `0` from each list inside the split string elements in a vectorized manner. |
| ```python\ndf[['title','firstname']] = df['Name'].str.split(',').str.get(1).str.strip().str.split(' ', n=1, expand=True)\ndf.head()\n``` | `None / No Output` | Retrieves the first 5 rows of the DataFrame to inspect the column headers, data types, and initial data alignment. Performs a vectorized whitespace cleanup, trimming leading and trailing padding spaces from all string cells. Splits string elements into lists of substrings based on a delimiter and expands them into a multi-column DataFrame. Extracts the specific item at index `1` from each list inside the split string elements in a vectorized manner. |
| ```python\ndf['title'].value_counts()\n``` | `None / No Output` | Computes the frequency distribution of unique elements in the Series or DataFrame, sorting the counts in descending order. |
| ```python\ndf['title'] = df['title'].str.replace('Ms.','Miss.')\ndf['title'] = df['title'].str.replace('Mlle.','Miss.')\ndf['title'].value_counts()\n``` | `None / No Output` | Computes the frequency distribution of unique elements in the Series or DataFrame, sorting the counts in descending order. Performs vectorized string substitution, replacing occurrences of target characters/regex patterns with a new string. |
| ```python\ndf[df['firstname'].str.endswith('A')]\n``` | `None / No Output` | Evaluates if string elements end with a specific suffix, returning a boolean mask. |
| ```python\ndf[df['firstname'].str.isdigit()]\n``` | `None / No Output` | Evaluates if string elements consist entirely of numeric digit characters. |
| ```python\ndf[df['firstname'].str.contains('john',case=False)]\n``` | `None / No Output` | Evaluates if string elements contain a target substring or regex pattern ignoring letter casing, returning a boolean filtering mask. |
| ```python\ndf[df['lastname'].str.contains('^[^aeiouAEIOU].+[^aeiouAEIOU]$')]\n``` | `None / No Output` | Evaluates if string elements contain a target substring or regex pattern, returning a boolean filtering mask. |
| ```python\ndf['Name'].str[::-1]\n``` | `None / No Output` | Slices each string element with a step size of `-1`, reversing the character order of every text cell in a vectorized fashion. |

---

> [!TIP]
> Use this structured log as a parallel lookup guide when reviewing or executing code inside the Jupyter notebook **[season22t.ipynb](file:///home/shoaib/Desktop/Pandas_Project/season22t.ipynb)**.
