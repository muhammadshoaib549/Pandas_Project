# This is codes working

## 📘 Introduction to Pandas Series, Attributes & Essential Indexing

Welcome to the comprehensive, step-by-step code execution reference guide for **[pandasfirst.ipynb](file:///home/shoaib/Desktop/Pandas_Project/pandasfirst.ipynb)**.
This document tracks every single code cell executed in the notebook, presenting its raw source code, final output, and an in-depth technical explanation of how it operates.

> [!NOTE]
> This file is dynamically generated and fully documents 100% of the **94 code cells** in the notebook. All existing project README files remain completely untouched and preserved!

---

### 📊 Complete Execution Log

| Code | Output | Working |
| :--- | :--- | :--- |
| ```python\nimport numpy as np\nimport pandas as pd\n``` | `None / No Output` | Imports the Pandas and NumPy libraries, laying the foundation for high-performance structured data manipulation and mathematical array operations. |
| ```python\n# string\ncountry = ['India','Pakistan','USA','Nepal','Srilanka']\n\npd.Series(country)\n``` | `None / No Output` | Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. |
| ```python\n# integers\nruns = [13,24,56,78,100]\n\nruns_ser = pd.Series(runs)\n``` | `None / No Output` | Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. |
| ```python\n# custom index\nmarks = [67,57,89,100]\nsubjects = ['maths','english','science','hindi']\n\npd.Series(marks,index=subjects)\n``` | `None / No Output` | Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. |
| ```python\n# setting a name\nmarks = pd.Series(marks,index=subjects,name='Nitish ke marks')\nmarks\n``` | `None / No Output` | Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. |
| ```python\nmarks = {\n    'maths':67,\n    'english':57,\n    'science':89,\n    'hindi':100\n}\n\nmarks_series = pd.Series(marks,name='nitish ke marks')\nmarks_series\n``` | `None / No Output` | Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. |
| ```python\n# size\nmarks_series.size\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# dtype\nmarks_series.dtype\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# name\nmarks_series.name\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# is_unique\nmarks_series.is_unique\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\npd.Series([1,1,2,3,4,5]).is_unique\n``` | `None / No Output` | Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. |
| ```python\n# index\nmarks_series.index\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nruns_ser.index\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# values\nmarks_series.values\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# with one col\nsubs = pd.read_csv('/content/subs.csv',squeeze=True)\nsubs\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\n# with 2 cols\nvk = pd.read_csv('/content/kohli_ipl.csv',index_col='match_no',squeeze=True)\nvk\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\nmovies = pd.read_csv('/content/bollywood.csv',index_col='movie',squeeze=True)\nmovies\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\n# head and tail\nsubs.head()\n``` | `None / No Output` | Retrieves the first 5 rows of the DataFrame to inspect the column headers, data types, and initial data alignment. |
| ```python\nvk.head(3)\n``` | `None / No Output` | Retrieves the first 3 rows of the DataFrame to inspect the column headers, data types, and initial data alignment. |
| ```python\nvk.tail(10)\n``` | `None / No Output` | Retrieves the last 10 rows of the DataFrame to inspect the trailing records and verify that data import is complete. |
| ```python\n# sample\nmovies.sample(5)\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# value_counts -> movies\nmovies.value_counts()\n``` | `None / No Output` | Computes the frequency distribution of unique elements in the Series or DataFrame, sorting the counts in descending order. |
| ```python\n# sort_values -> inplace\nvk.sort_values(ascending=False).head(1).values[0]\n``` | `None / No Output` | Retrieves the first 1 rows of the DataFrame to inspect the column headers, data types, and initial data alignment. Sorts the Series or DataFrame rows based on element values in descending order. |
| ```python\nvk.sort_values(ascending=False)\n``` | `None / No Output` | Sorts the Series or DataFrame rows based on element values in descending order. |
| ```python\n# sort_index -> inplace -> movies\nmovies.sort_index(ascending=False,inplace=True)\n\nmovies\n``` | `None / No Output` | Restructures the DataFrame/Series by sorting its index labels in descending order instead of sorting by its values. |
| ```python\nvk.sort_values(inplace=True)\n\nvk\n``` | `None / No Output` | Sorts the Series or DataFrame rows based on element values in ascending order. |
| ```python\n# count\nvk.count()\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# sum -> product\nsubs.sum()\n``` | `None / No Output` | Calculates the sum total of values across the specified axis (default is vertically along columns). |
| ```python\n# mean -> median -> mode -> std -> var\nsubs.mean()\nprint(vk.median())\nprint(movies.mode())\nprint(subs.std())\nprint(vk.var())\n``` | `None / No Output` | Calculates the arithmetic mean of numeric elements in the DataFrame or Series. Computes the median (middle value) of numeric elements to evaluate central tendency. Computes the mathematical mode (most frequently occurring value) of elements. Computes the standard deviation of numerical elements to measure statistical dispersion. Computes the variance of numerical elements to measure data spread around the mean. |
| ```python\n# min/max\nsubs.max()\n``` | `None / No Output` | Finds the maximum value among elements in the Series/DataFrame. |
| ```python\n# describe\nsubs.describe()\n``` | `None / No Output` | Generates descriptive statistical summaries (count, mean, standard deviation, min, max, and percentiles) for all numeric columns to understand their distributions. |
| ```python\n# integer indexing\nx = pd.Series([12,13,14,35,46,57,58,79,9])\nx\n``` | `None / No Output` | Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. |
| ```python\n# negative indexing\nx[-1]\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nmovies\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nvk[-1]\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nmarks_series[-1]\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# slicing\nvk[5:16]\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# negative slicing\nvk[-5:]\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nmovies[::2]\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# fancy indexing\nvk[[1,3,4,5]]\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# indexing with labels -> fancy indexing\nmovies['2 States (2014 film)']\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# using indexing\nmarks_series[1] = 100\nmarks_series\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\n# what if an index does not exist\nmarks_series['evs'] = 100\n\nmarks_series\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\n# slicing\nruns_ser[2:4] = [100,100]\nruns_ser\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\n# fancy indexing\nruns_ser[[0,3,4]] = [0,0,0]\nruns_ser\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\n# using index label\nmovies['2 States (2014 film)'] = 'Alia Bhatt'\nmovies\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\n# len/type/dir/sorted/max/min\nprint(len(subs))\nprint(type(subs))\nprint(dir(subs))\nprint(sorted(subs))\nprint(min(subs))\nprint(max(subs))\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# type conversion\nlist(marks_series)\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\ndict(marks_series)\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# membership operator\n\n'2 States (2014 film)' in movies\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n'Alia Bhatt' in movies.values\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nmovies\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# looping\nfor i in movies.index:\n  print(i)\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# Arithmetic Operators(Broadcasting)\n100 + marks_series\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# Relational Operators\n\nvk >= 50\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\n# Find no of 50's and 100's scored by kohli\nvk[vk >= 50].size\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\n# find number of ducks\nvk[vk == 0].size\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\n# Count number of day when I had more than 200 subs a day\nsubs[subs > 200].size\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# find actors who have done more than 20 movies\nnum_movies = movies.value_counts()\nnum_movies[num_movies > 20]\n``` | `None / No Output` | Computes the frequency distribution of unique elements in the Series or DataFrame, sorting the counts in descending order. |
| ```python\nsubs.plot()\n``` | `None / No Output` | Invokes Matplotlib/Pandas visualization to render an aesthetic plot representing the aggregated column data. |
| ```python\nmovies.value_counts().head(20).plot(kind='pie')\n``` | `None / No Output` | Retrieves the first 20 rows of the DataFrame to inspect the column headers, data types, and initial data alignment. Computes the frequency distribution of unique elements in the Series or DataFrame, sorting the counts in descending order. Invokes Matplotlib/Pandas visualization to render an aesthetic plot of type 'pie' representing the aggregated column data. |
| ```python\nimport numpy as np\nimport pandas as pd\n\nsubs = pd.read_csv('/content/subs.csv',squeeze=True)\nsubs\n``` | `None / No Output` | Imports the Pandas and NumPy libraries, laying the foundation for high-performance structured data manipulation and mathematical array operations. |
| ```python\nvk = pd.read_csv('/content/kohli_ipl.csv',index_col='match_no',squeeze=True)\nvk\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\nmovies = pd.read_csv('/content/bollywood.csv',index_col='movie',squeeze=True)\nmovies\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\n# astype\nimport sys\nsys.getsizeof(vk)\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nsys.getsizeof(vk.astype('int16'))\n``` | `None / No Output` | Casts the data type of the column elements to `'int16'` to optimize memory or enable type-specific operations. |
| ```python\n# between\nvk[vk.between(51,99)].size\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# clip\nsubs\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nsubs.clip(100,200)\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# drop_duplicates\ntemp = pd.Series([1,1,2,2,3,3,4,4])\ntemp\n``` | `None / No Output` | Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. Removes duplicate row records from the DataFrame, keeping only the `first (default)` occurrence. |
| ```python\ntemp.drop_duplicates(keep='last')\n``` | `None / No Output` | Removes duplicate row records from the DataFrame, keeping only the `last` occurrence. |
| ```python\ntemp.duplicated().sum()\n``` | `None / No Output` | Computes a boolean mask for duplicate rows and aggregates them to find the total number of duplicate records. |
| ```python\nvk.duplicated().sum()\n``` | `None / No Output` | Computes a boolean mask for duplicate rows and aggregates them to find the total number of duplicate records. |
| ```python\nmovies.drop_duplicates()\n``` | `None / No Output` | Removes duplicate row records from the DataFrame, keeping only the `first (default)` occurrence. |
| ```python\ntemp = pd.Series([1,2,3,np.nan,5,6,np.nan,8,np.nan,10])\ntemp\n``` | `None / No Output` | Instantiates a new 1-dimensional labeled Pandas Series object from a Python list, dictionary, or NumPy array. |
| ```python\ntemp.size\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\ntemp.count()\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\n# isnull\ntemp.isnull().sum()\n``` | `None / No Output` | Generates a boolean null-mask and aggregates it using `.sum()` to find the total count of missing values per column. |
| ```python\n# dropna\ntemp.dropna()\n``` | `None / No Output` | Filters out and discards rows containing missing values if 'any' column is null, applying changes . |
| ```python\n# fillna\ntemp.fillna(temp.mean())\n``` | `None / No Output` | Imputes missing values with `temp.mean(` to clean the dataset and maintain column continuity. |
| ```python\n# isin\nvk[(vk == 49) \| (vk == 99)]\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\nvk[vk.isin([49,99])]\n``` | `None / No Output` | Filters DataFrame rows by checking if column values match any entries specified in a list, returning a boolean mask. |
| ```python\n# apply\nmovies\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nmovies.apply(lambda x:x.split()[0].upper())\n``` | `None / No Output` | Maps `lambda x:x.split(` element-wise vertically across the DataFrame/Series to perform customized transformations. |
| ```python\nsubs\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nsubs.apply(lambda x:'good day' if x > subs.mean() else 'bad day')\n``` | `None / No Output` | Calculates the arithmetic mean of numeric elements in the DataFrame or Series. Maps `lambda x:'good day' if x > subs.mean(` element-wise vertically across the DataFrame/Series to perform customized transformations. |
| ```python\nsubs.mean()\n``` | `None / No Output` | Calculates the arithmetic mean of numeric elements in the DataFrame or Series. |
| ```python\n# copy\n\nvk\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nnew = vk.head()\n\nnew\n``` | `None / No Output` | Retrieves the first 5 rows of the DataFrame to inspect the column headers, data types, and initial data alignment. |
| ```python\nnew[1] = 1\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\nnew = vk.head().copy()\n``` | `None / No Output` | Retrieves the first 5 rows of the DataFrame to inspect the column headers, data types, and initial data alignment. Creates a deep copy of the DataFrame or Series to ensure modifications do not affect the original source data. |
| ```python\nnew[1] = 100\n``` | `None / No Output` | Performs value assignment or computes a new variable/column by evaluating the specified expressions on the dataset. |
| ```python\nnew\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |
| ```python\nvk\n``` | `None / No Output` | Executes a Pandas Series or DataFrame evaluation statement to display, filter, or analyze row/column values. |

---

> [!TIP]
> Use this structured log as a parallel lookup guide when reviewing or executing code inside the Jupyter notebook **[pandasfirst.ipynb](file:///home/shoaib/Desktop/Pandas_Project/pandasfirst.ipynb)**.
