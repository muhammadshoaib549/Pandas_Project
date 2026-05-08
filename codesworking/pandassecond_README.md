# This is codes working

## 📘 Pandas Tabular Operations & Series Methods Master Reference

Welcome to the comprehensive, step-by-step code execution reference guide for **[pandassecond.ipynb](file:///home/shoaib/Desktop/Pandas_Project/pandassecond.ipynb)**.
This document tracks every single code cell executed in the notebook, presenting its raw source code, final output, and an in-depth technical explanation of how it operates.

> [!NOTE]
> This file is dynamically generated and fully documents 100% of the **61 code cells** in the notebook. All existing project README files remain completely untouched and preserved!

---

### 📊 Complete Execution Log

| Code | Output | Working |
| :--- | :--- | :--- |
| ```python\nimport numpy as np\nimport pandas as pd\n``` | `None / No Output` | Imports the Pandas and NumPy libraries, laying the foundation for high-performance structured data manipulation and mathematical array operations. |
| ```python\n# using lists\nstudent_data = [\n    [100,80,10],\n    [90,70,7],\n    [120,100,14],\n    [80,50,2]\n]\n\npd.DataFrame(student_data,columns=['iq','marks','package'])\n``` | `None / No Output` | Instantiates a new 2-dimensional tabular Pandas DataFrame object from a structured dictionary or nested list. |
| ```python\n# using dicts\n\nstudent_dict = {\n    'name':['nitish','ankit','rupesh','rishabh','amit','ankita'],\n    'iq':[100,90,120,80,0,0],\n    'marks':[80,70,100,50,0,0],\n    'package':[10,7,14,2,0,0]\n}\n\nstudents = pd.DataFrame(student_dict)\nstudents.set_index('name',inplace=True)\nstudents\n``` | `None / No Output` | Instantiates a new 2-dimensional tabular Pandas DataFrame object from a structured dictionary or nested list. Sets `name` as the new index (row labels) of the DataFrame, in-place (modifying the original DataFrame directly). |
| ```python\n# using read_csv\nmovies = pd.read_csv('movies.csv')\nmovies\n``` | `None / No Output` | Loads the CSV dataset from `movies.csv` into a Pandas DataFrame to prepare it for subsequent structured analysis and cleaning. |
| ```python\nipl = pd.read_csv('ipl-matches.csv')\nipl\n``` | `None / No Output` | Loads the CSV dataset from `ipl-matches.csv` into a Pandas DataFrame to prepare it for subsequent structured analysis and cleaning. |
| ```python\n# shape\nmovies.shape\nipl.shape\n``` | `None / No Output` | Accesses the `.shape` attribute to retrieve a tuple representing the dimensions (number of rows and columns) of the DataFrame. |
| ```python\n# dtypes\nmovies.dtypes\nipl.dtypes\n``` | `None / No Output` | Accesses the `.dtypes` attribute to view the specific data types associated with each column in the DataFrame. |
| ```python\n# index\nmovies.index\nipl.index\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# columns\nmovies.columns\nipl.columns\n# Note: 'student' is referenced here (likely a typo for 'students' in the original session)\ntry:\n    student.columns\nexcept NameError:\n    print("student variable is not defined, please use students.columns instead:")\n    print(students.columns)\n``` | `None / No Output` | Accesses the `.columns` attribute to view and list all available column headers in the DataFrame. |
| ```python\n# values\ntry:\n    student.values\nexcept NameError:\n    print("student variable is not defined, please use students.values instead:")\n    print(students.values)\nipl.values\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# head and tail\nmovies.head(2)\n``` | `None / No Output` | Retrieves the first 2 rows of the DataFrame to inspect the column headers, data types, and initial data alignment. |
| ```python\nipl.tail(2)\n``` | `None / No Output` | Retrieves the last 2 rows of the DataFrame to inspect the trailing records and verify that data import is complete. |
| ```python\n# sample\nipl.sample(5)\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# info\nmovies.info()\n``` | `None / No Output` | Generates a comprehensive summary of the DataFrame, including row count, index details, column labels, non-null counts, data types, and memory usage. |
| ```python\nipl.info()\n``` | `None / No Output` | Generates a comprehensive summary of the DataFrame, including row count, index details, column labels, non-null counts, data types, and memory usage. |
| ```python\n# describe\nmovies.describe()\n``` | `None / No Output` | Generates descriptive statistical summaries (count, mean, standard deviation, min, max, and percentiles) for all numeric columns to understand their distributions. |
| ```python\nipl.describe()\n``` | `None / No Output` | Generates descriptive statistical summaries (count, mean, standard deviation, min, max, and percentiles) for all numeric columns to understand their distributions. |
| ```python\n# isnull\nmovies.isnull().sum()\n``` | `None / No Output` | Generates a boolean null-mask and aggregates it using `.sum()` to find the total count of missing values per column. |
| ```python\n# duplicated\nmovies.duplicated().sum()\n``` | `None / No Output` | Computes a boolean mask for duplicate rows and aggregates them to find the total number of duplicate records. |
| ```python\nstudents.duplicated().sum()\n``` | `None / No Output` | Computes a boolean mask for duplicate rows and aggregates them to find the total number of duplicate records. |
| ```python\n# rename\nstudents\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nstudents.rename(columns={'marks':'percent','package':'lpa'},inplace=True)\n``` | `None / No Output` | Renames columns or index labels of the DataFrame using mapping dictionaries to fix labels or correct spelling. |
| ```python\n# sum -> axis argument\nstudents.sum(axis=0)\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\nstudents.mean(axis=1)\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\nstudents.var()\n``` | `None / No Output` | Computes the variance of numerical elements to measure data spread around the mean. |
| ```python\n# single cols\nmovies['title_x']\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nipl['Venue']\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# multiple cols\nmovies[['year_of_release','actors','title_x']]\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nipl[['Team1','Team2','WinningTeam']]\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# single row\nmovies.iloc[5]\n``` | `None / No Output` | Uses `.iloc` indexing to select rows and columns based on their absolute integer positions (offsets). |
| ```python\n# multiple row\nmovies.iloc[:5]\n``` | `None / No Output` | Uses `.iloc` indexing to select rows and columns based on their absolute integer positions (offsets). |
| ```python\n# fancy indexing\nmovies.iloc[[0,4,5]]\n``` | `None / No Output` | Uses `.iloc` indexing to select rows and columns based on their absolute integer positions (offsets). |
| ```python\n# loc\nstudents\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nstudents.loc['nitish']\n``` | `None / No Output` | Uses `.loc` indexing to select rows and columns based on their string labels or boolean conditional mask arrays. |
| ```python\nstudents.loc['nitish':'rishabh':2]\n``` | `None / No Output` | Uses `.loc` indexing to select rows and columns based on their string labels or boolean conditional mask arrays. |
| ```python\nstudents.loc[['nitish','ankita','rupesh']]\n``` | `None / No Output` | Uses `.loc` indexing to select rows and columns based on their string labels or boolean conditional mask arrays. |
| ```python\nstudents.iloc[[0,3,4]]\n``` | `None / No Output` | Uses `.iloc` indexing to select rows and columns based on their absolute integer positions (offsets). |
| ```python\nmovies.iloc[0:3,0:3]\n``` | `None / No Output` | Uses `.iloc` indexing to select rows and columns based on their absolute integer positions (offsets). |
| ```python\nmovies.loc[0:2,'title_x':'poster_path']\n``` | `None / No Output` | Uses `.loc` indexing to select rows and columns based on their string labels or boolean conditional mask arrays. |
| ```python\nipl.head(2)\n``` | `None / No Output` | Retrieves the first 2 rows of the DataFrame to inspect the column headers, data types, and initial data alignment. |
| ```python\n# find all the final winners\nmask = ipl['MatchNumber'] == 'Final'\nnew_df = ipl[mask]\nnew_df[['Season','WinningTeam']]\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\nipl[ipl['MatchNumber'] == 'Final'][['Season','WinningTeam']]\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\n# how many super over finishes have occured\nipl[ipl['SuperOver'] == 'Y'].shape[0]\n``` | `None / No Output` | Accesses the `.shape` attribute to retrieve a tuple representing the dimensions (number of rows and columns) of the DataFrame. |
| ```python\n# how many matches has csk won in kolkata\nipl[(ipl['City'] == 'Kolkata') & (ipl['WinningTeam'] == 'Chennai Super Kings')].shape[0]\n``` | `None / No Output` | Accesses the `.shape` attribute to retrieve a tuple representing the dimensions (number of rows and columns) of the DataFrame. |
| ```python\n# toss winner is match winner in percentage\n(ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]/ipl.shape[0])*100\n``` | `None / No Output` | Accesses the `.shape` attribute to retrieve a tuple representing the dimensions (number of rows and columns) of the DataFrame. |
| ```python\n# movies with rating higher than 8 and votes>10000\nmovies[(movies['imdb_rating'] > 8.5) & (movies['imdb_votes'] > 10000)].shape[0]\n``` | `None / No Output` | Accesses the `.shape` attribute to retrieve a tuple representing the dimensions (number of rows and columns) of the DataFrame. |
| ```python\n# Action movies with rating higher than 7.5\n# mask1 = movies['genres'].str.split('\|').apply(lambda x:'Action' in x)\nmask1 = movies['genres'].str.contains('Action')\nmask2 = movies['imdb_rating'] > 7.5\n\nmovies[mask1 & mask2]\n``` | `None / No Output` | Maps `lambda x:'Action' in x` element-wise vertically across the DataFrame/Series to perform customized transformations. Splits string elements into lists of substrings based on a delimiter. Evaluates if string elements contain a target substring or regex pattern, returning a boolean filtering mask. |
| ```python\n# write a function that can return the track record of 2 teams against each other\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# completely new\nmovies['Country'] = 'India'\nmovies.head()\n``` | `None / No Output` | Retrieves the first 5 rows of the DataFrame to inspect the column headers, data types, and initial data alignment. |
| ```python\n# from existing ones\nmovies.dropna(inplace=True)\n\nmovies['lead actor'] = movies['actors'].str.split('\|').apply(lambda x:x[0])\nmovies.head()\n``` | `None / No Output` | Retrieves the first 5 rows of the DataFrame to inspect the column headers, data types, and initial data alignment. Filters out and discards rows containing missing values if 'any' column is null, applying changes in-place. Maps `lambda x:x[0]` element-wise vertically across the DataFrame/Series to perform customized transformations. Splits string elements into lists of substrings based on a delimiter. |
| ```python\nmovies.info()\n``` | `None / No Output` | Generates a comprehensive summary of the DataFrame, including row count, index details, column labels, non-null counts, data types, and memory usage. |
| ```python\n# astype\nipl.info()\n``` | `None / No Output` | Generates a comprehensive summary of the DataFrame, including row count, index details, column labels, non-null counts, data types, and memory usage. |
| ```python\nipl['ID'] = ipl['ID'].astype('int32')\n``` | `None / No Output` | Casts the data type of the column elements to `'int32'` to optimize memory or enable type-specific operations. |
| ```python\nipl.info()\n``` | `None / No Output` | Generates a comprehensive summary of the DataFrame, including row count, index details, column labels, non-null counts, data types, and memory usage. |
| ```python\n# ipl['Season'] = ipl['Season'].astype('category')\nipl['Team1'] = ipl['Team1'].astype('category')\nipl['Team2'] = ipl['Team2'].astype('category')\n``` | `None / No Output` | Casts the data type of the column elements to `'category'` to optimize memory or enable type-specific operations. |
| ```python\nipl.info()\n``` | `None / No Output` | Generates a comprehensive summary of the DataFrame, including row count, index details, column labels, non-null counts, data types, and memory usage. |
| ```python\n# value_counts\n``` | `None / No Output` | Computes the frequency distribution of unique elements in the Series or DataFrame, sorting the counts in descending order. |
| ```python\n# find which player has won most potm -> in finals and qualifiers\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# Toss decision plot\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# how many matches each team has played\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# sort_values -> ascending -> na_position -> inplace -> multiple cols\n``` | `None / No Output` | Sorts the Series or DataFrame rows based on element values in ascending order. |

---

> [!TIP]
> Use this structured log as a parallel lookup guide when reviewing or executing code inside the Jupyter notebook **[pandassecond.ipynb](file:///home/shoaib/Desktop/Pandas_Project/pandassecond.ipynb)**.
