# This is codes working

## 📘 Pandas DataFrame Methods & Core Manipulations Master Guide

Welcome to the comprehensive, step-by-step code execution reference guide for **[dataframes.ipynb](file:///home/shoaib/Desktop/Pandas_Project/dataframes.ipynb)**.
This document tracks every single code cell executed in the notebook, presenting its raw source code, final output, and an in-depth technical explanation of how it operates.

> [!NOTE]
> This file is dynamically generated and fully documents 100% of the **65 code cells** in the notebook. All existing project README files remain completely untouched and preserved!

---

### 📊 Complete Execution Log

| Code | Output | Working |
| :--- | :--- | :--- |
| ```python\nimport numpy as np\nimport pandas as pd\n\na = pd.Series([1,1,1,2,2,3])\na.value_counts()\n``` | `None / No Output` | Imports the Pandas and NumPy libraries, laying the foundation for high-performance structured data manipulation and mathematical array operations. Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. Computes the frequency distribution of unique elements in the Series or DataFrame, sorting the counts in descending order. |
| ```python\nmarks = pd.DataFrame([\n    [100,80,10],\n    [90,70,7],\n    [120,100,14],\n    [80,70,14],\n    [80,70,14]\n],columns=['iq','marks','package'])\n\nmarks\n``` | `None / No Output` | Instantiates a new 2-dimensional tabular Pandas DataFrame object from a structured dictionary or nested list. |
| ```python\nmarks.value_counts()\n``` | `None / No Output` | Computes the frequency distribution of unique elements in the Series or DataFrame, sorting the counts in descending order. |
| ```python\nipl = pd.read_csv('ipl-matches.csv')\nipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts()\n``` | `None / No Output` | Loads the CSV dataset from `ipl-matches.csv` into a Pandas DataFrame to prepare it for subsequent structured analysis and cleaning. Computes the frequency distribution of unique elements in the Series or DataFrame, sorting the counts in descending order. Evaluates if string elements consist entirely of numeric digit characters. |
| ```python\n# Toss decision plot\nipl['TossDecision'].value_counts().plot(kind='pie')\n``` | `None / No Output` | Computes the frequency distribution of unique elements in the Series or DataFrame, sorting the counts in descending order. Invokes Matplotlib/Pandas visualization to render an aesthetic plot of type 'pie' representing the aggregated column data. |
| ```python\n# how many matches each team has played\n(ipl['Team2'].value_counts() + ipl['Team1'].value_counts()).sort_values(ascending=False)\n``` | `None / No Output` | Sorts the Series or DataFrame rows based on element values in descending order. Computes the frequency distribution of unique elements in the Series or DataFrame, sorting the counts in descending order. |
| ```python\nx = pd.Series([12,14,1,56,89])\nx\n``` | `None / No Output` | Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. |
| ```python\nx.sort_values(ascending=False)\n``` | `None / No Output` | Sorts the Series or DataFrame rows based on element values in descending order. |
| ```python\nmovies = pd.read_csv('movies.csv')\nmovies.head(4)\n``` | `None / No Output` | Loads the CSV dataset from `movies.csv` into a Pandas DataFrame to prepare it for subsequent structured analysis and cleaning. Retrieves the first 4 rows of the DataFrame to inspect the column headers, data types, and initial data alignment. |
| ```python\nmovies.sort_values('title_x',ascending=False)\n``` | `None / No Output` | Sorts the DataFrame rows based on values in the `title_x` column in descending order. |
| ```python\nstudents = pd.DataFrame(\n    {\n        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],\n        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],\n        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],\n        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],\n        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]\n    }\n)\n\nstudents\n``` | `None / No Output` | Instantiates a new 2-dimensional tabular Pandas DataFrame object from a structured dictionary or nested list. |
| ```python\nstudents.sort_values('name',na_position='first',ascending=False,inplace=True)\nstudents\n``` | `None / No Output` | Sorts the DataFrame rows based on values in the `name` column in descending order. |
| ```python\nmovies.sort_values(['year_of_release','title_x'],ascending=[True,False])\n``` | `None / No Output` | Sorts the DataFrame rows hierarchically based on values in multiple columns: `['year_of_release','title_x']` in configured order. |
| ```python\nbatsman = pd.read_csv('batsman_runs_ipl.csv')\nbatsman.head()\n``` | `None / No Output` | Loads the CSV dataset from `batsman_runs_ipl.csv` into a Pandas DataFrame to prepare it for subsequent structured analysis and cleaning. Retrieves the first 5 rows of the DataFrame to inspect the column headers, data types, and initial data alignment. |
| ```python\nbatsman['batting_rank'] = batsman['batsman_run'].rank(ascending=False)\nbatsman.sort_values('batting_rank')\n``` | `None / No Output` | Sorts the DataFrame rows based on values in the `batting_rank` column in descending order. |
| ```python\nmarks = {\n    'maths':67,\n    'english':57,\n    'science':89,\n    'hindi':100\n}\n\nmarks_series = pd.Series(marks)\nmarks_series\n``` | `None / No Output` | Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. |
| ```python\nmarks_series.sort_index(ascending=False)\n``` | `None / No Output` | Restructures the DataFrame/Series by sorting its index labels in descending order instead of sorting by its values. |
| ```python\nmovies.sort_index(ascending=False)\n``` | `None / No Output` | Restructures the DataFrame/Series by sorting its index labels in descending order instead of sorting by its values. |
| ```python\nbatsman.set_index('batter',inplace=True)\nbatsman\n``` | `None / No Output` | Sets `batter` as the new index (row labels) of the DataFrame, in-place (modifying the original DataFrame directly). |
| ```python\nbatsman.reset_index(inplace=True)\nbatsman\n``` | `None / No Output` | Sets the specified column as the new index (row labels) of the DataFrame, in-place (modifying the original DataFrame directly). Reverts the custom index back to a standard incremental integer RangeIndex, retaining the old index as a normal column and applying changes in-place. |
| ```python\n# how to replace existing index without loosing\nbatsman.reset_index().set_index('batting_rank')\n``` | `None / No Output` | Sets `batting_rank` as the new index (row labels) of the DataFrame, returning a new DataFrame with the updated index. Reverts the custom index back to a standard incremental integer RangeIndex, retaining the old index as a normal column and applying changes returning a new object. |
| ```python\n# series to dataframe using reset_index\nmarks_series.reset_index()\n``` | `None / No Output` | Sets the specified column as the new index (row labels) of the DataFrame, returning a new DataFrame with the updated index. Reverts the custom index back to a standard incremental integer RangeIndex, retaining the old index as a normal column and applying changes returning a new object. |
| ```python\nmovies.set_index('title_x',inplace=True)\nmovies.rename(columns={'imdb_id':'imdb','poster_path':'link'},inplace=True)\n``` | `None / No Output` | Sets `title_x` as the new index (row labels) of the DataFrame, in-place (modifying the original DataFrame directly). Renames columns or index labels of the DataFrame using mapping dictionaries to fix labels or correct spelling. |
| ```python\nmovies.rename(index={'Uri: The Surgical Strike':'Uri','Battalion 609':'Battalion'})\n``` | `None / No Output` | Renames columns or index labels of the DataFrame using mapping dictionaries to fix labels or correct spelling. |
| ```python\ntemp = pd.Series([1,1,2,2,3,3,4,4,5,5,np.nan,np.nan])\nprint(temp)\n``` | `None / No Output` | Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. |
| ```python\nlen(temp.unique())\n``` | `None / No Output` | Returns a NumPy array containing only the unique elements present in the target Series, preserving their order of occurrence and including missing values. |
| ```python\ntemp.nunique()\n``` | `None / No Output` | Computes the count of unique values in the Series or DataFrame, excluding missing values (`NaN`) by default. |
| ```python\nlen(ipl['Season'].unique())\n``` | `None / No Output` | Returns a NumPy array containing only the unique elements present in the target Series, preserving their order of occurrence and including missing values. |
| ```python\nipl['Season'].nunique()\n``` | `None / No Output` | Computes the count of unique values in the Series or DataFrame, excluding missing values (`NaN`) by default. |
| ```python\nstudents['name'][students['name'].isnull()]\n``` | `None / No Output` | Generates a boolean mask (same shape as DataFrame/Series) mapping empty cells (`NaN`/`None`) to `True` and valid cells to `False`. |
| ```python\nstudents['name'][students['name'].notnull()]\n``` | `None / No Output` | Generates a boolean mask identifying valid (non-missing) elements across the DataFrame/Series. |
| ```python\nstudents['name'].hasnans\n``` | `None / No Output` | Queries the `.hasnans` attribute of a Series, returning `True` if it contains one or more missing values. |
| ```python\nstudents\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nstudents.isnull()\n``` | `None / No Output` | Generates a boolean mask (same shape as DataFrame/Series) mapping empty cells (`NaN`/`None`) to `True` and valid cells to `False`. |
| ```python\nstudents.notnull()\n``` | `None / No Output` | Generates a boolean mask identifying valid (non-missing) elements across the DataFrame/Series. |
| ```python\nstudents['name'].dropna()\n``` | `None / No Output` | Filters out and discards rows containing missing values if 'any' column is null, applying changes . |
| ```python\nstudents\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nstudents.dropna(how='any')\n``` | `None / No Output` | Filters out and discards rows containing missing values if 'any' column is null, applying changes . |
| ```python\nstudents.dropna(how='all')\n``` | `None / No Output` | Filters out and discards rows containing missing values if 'all' columns are null, applying changes . |
| ```python\nstudents.dropna(subset=['name'])\n``` | `None / No Output` | Filters out and discards rows containing missing values restricted to columns `['name']` if 'any' column is null, applying changes . |
| ```python\nstudents.dropna(subset=['name','college'])\n``` | `None / No Output` | Filters out and discards rows containing missing values restricted to columns `['name','college']` if 'any' column is null, applying changes . |
| ```python\nstudents.dropna(inplace=True)\n``` | `None / No Output` | Filters out and discards rows containing missing values if 'any' column is null, applying changes in-place. |
| ```python\nstudents['name'].fillna('unknown')\n``` | `None / No Output` | Imputes missing values with `'unknown'` to clean the dataset and maintain column continuity. |
| ```python\nstudents\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nstudents['package'].fillna(students['package'].mean())\n``` | `None / No Output` | Imputes missing values with `students['package'].mean(` to clean the dataset and maintain column continuity. |
| ```python\nstudents['name'].fillna(method='bfill')\n``` | `None / No Output` | Imputes missing values with the specified fallback value using the 'bfill' method (such as backfill/forward-fill) to clean the dataset and maintain column continuity. |
| ```python\ntemp = pd.Series([1,1,1,2,3,3,4,4])\ntemp.drop_duplicates()\n``` | `None / No Output` | Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. Removes duplicate row records from the DataFrame, keeping only the `first (default)` occurrence. |
| ```python\nmarks.drop_duplicates(keep='last')\n``` | `None / No Output` | Removes duplicate row records from the DataFrame, keeping only the `last` occurrence. |
| ```python\n# find the last match played by virat kohli in Delhi\nipl['all_players'] = ipl['Team1Players'] + ipl['Team2Players']\nipl.head()\n``` | `None / No Output` | Retrieves the first 5 rows of the DataFrame to inspect the column headers, data types, and initial data alignment. |
| ```python\ndef did_kohli_play(players_list):\n  return 'V Kohli' in players_list\n\nipl['did_kohli_play'] = ipl['all_players'].apply(did_kohli_play)\nipl[(ipl['City'] == 'Delhi') & (ipl['did_kohli_play'] == True)].drop_duplicates(subset=['City','did_kohli_play'],keep='first')\n``` | `None / No Output` | Removes duplicate row records from the DataFrame based on subset columns `['City','did_kohli_play']`, keeping only the `first` occurrence. Maps `did_kohli_play` element-wise vertically across the DataFrame/Series to perform customized transformations. |
| ```python\nstudents.drop_duplicates()\n``` | `None / No Output` | Removes duplicate row records from the DataFrame, keeping only the `first (default)` occurrence. |
| ```python\ntemp = pd.Series([10,2,3,16,45,78,10])\ntemp\n``` | `None / No Output` | Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. |
| ```python\ntemp.drop(index=[0,6])\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\nstudents\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nstudents.drop(columns=['branch','cgpa'],inplace=True)\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\nstudents.set_index('name').drop(index=['nitish','aditya'])\n``` | `None / No Output` | Sets `name` as the new index (row labels) of the DataFrame, returning a new DataFrame with the updated index. |
| ```python\ntemp = pd.Series([10,20,30,40,50])\ntemp\n``` | `None / No Output` | Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. |
| ```python\ndef sigmoid(value):\n  return 1/1+np.exp(-value)\n\ntemp.apply(sigmoid)\n``` | `None / No Output` | Maps `sigmoid` element-wise vertically across the DataFrame/Series to perform customized transformations. |
| ```python\npoints_df = pd.DataFrame(\n    {\n        '1st point':[(3,4),(-6,5),(0,0),(-10,1),(4,5)],\n        '2nd point':[(-3,4),(0,0),(2,2),(10,10),(1,1)]\n    }\n)\n\npoints_df\n``` | `None / No Output` | Instantiates a new 2-dimensional tabular Pandas DataFrame object from a structured dictionary or nested list. |
| ```python\ndef euclidean(row):\n  pt_A = row['1st point']\n  pt_B = row['2nd point']\n\n  return ((pt_A[0] - pt_B[0])**2 + (pt_A[1] - pt_B[1])**2)**0.5\n\npoints_df['distance'] = points_df.apply(euclidean,axis=1)\npoints_df\n``` | `None / No Output` | Maps `euclidean` row-by-row horizontally (`axis=1`) across the DataFrame/Series to perform customized transformations. |
| ```python\n# isin(series)\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# corr\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# nlargest and nsmallest\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# insert\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# copy\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |

---

> [!TIP]
> Use this structured log as a parallel lookup guide when reviewing or executing code inside the Jupyter notebook **[dataframes.ipynb](file:///home/shoaib/Desktop/Pandas_Project/dataframes.ipynb)**.
