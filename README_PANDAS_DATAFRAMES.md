# 📊 Pandas DataFrames: Master Reference Guide

Welcome to the **Pandas DataFrames Master Reference Guide**! This comprehensive document acts as an interactive cheat-sheet and textbook reference for Pandas **DataFrames**—the primary 2-Dimensional, size-mutable tabular data structure used in modern Python data science workflows.

> [!NOTE]
> This guide is dynamically generated from your session-17 learning materials. It maps all operations from the provided Jupyter Notebook, formatted as a highly accessible 3-column reference grid: **Concept Name**, **Code**, and **Detailed Explanation**.

---

## 🏗️ 1. DataFrame Initialization & Creation

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **DataFrame from List of Lists** | ```python\nstudent_data = [\n    [100,80,10],\n    [90,70,7],\n    [120,100,14],\n    [80,50,2]\n]\npd.DataFrame(\n    student_data, \n    columns=['iq','marks','package']\n)\n``` | Converts a nested Python list (representing rows of data) into a tabular DataFrame. The `columns` parameter explicitly assigns header labels to each column position. |
| **DataFrame from Dictionary** | ```python\nstudent_dict = {\n    'name':['nitish','ankit','rupesh','rishabh','amit','ankita'],\n    'iq':[100,90,120,80,0,0],\n    'marks':[80,70,100,50,0,0],\n    'package':[10,7,14,2,0,0]\n}\nstudents = pd.DataFrame(student_dict)\nstudents.set_index('name', inplace=True)\nstudents\n``` | Converts a Python dict (keys become column names, lists become column data) to a DataFrame. `.set_index('name', inplace=True)` sets the 'name' column as the custom row-index in-place. |
| **CSV Tabular Import** | ```python\nmovies = pd.read_csv('movies.csv')\nipl = pd.read_csv('ipl-matches.csv')\n``` | Standard high-performance utility to read structured tabular values from comma-separated value (CSV) files straight into fully populated DataFrames. |

---

## 🔍 2. DataFrame Structural Attributes & Inspection

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Grid Dimension Shape (`.shape`)** | ```python\nmovies.shape\nipl.shape\n``` | Returns a 2-element tuple indicating dimensions: `(total_rows, total_columns)`. This attribute is read-only and does not calculate values. |
| **Column Data Types (`.dtypes`)** | ```python\nmovies.dtypes\nipl.dtypes\n``` | Displays the data types of all columns. Standard types include `int64`, `float64`, `object` (text/mixed), and specialized types like `category`. |
| **Row Indices (`.index`)** | ```python\nmovies.index\nipl.index\n``` | Returns the active Index object of the rows. This could be standard RangeIndex `[0, 1, 2...]` or label-based custom indices. |
| **Column Labels (`.columns`)** | ```python\nmovies.columns\nipl.columns\nstudents.columns\n``` | Accesses the array containing all active column headers. Very useful for iterating or selecting features dynamically. |
| **NumPy Extraction (`.values`)** | ```python\nstudents.values\nipl.values\n``` | Extracts the underlying tabular data as a raw **2D NumPy ndarray**, stripping all column headers and row labels. |
| **Inspecting Rows (`.head()` / `.tail()`)** | ```python\nmovies.head(2)\nipl.tail(2)\n``` | Head retrieves the first `n` records; Tail displays the last `n` records. Useful for testing transformations or doing sanity checks on imports. |
| **Random Sampling (`.sample()`)** | ```python\nipl.sample(5)\n``` | Generates a randomized selection of `n` rows. Excellent for debugging data structures or retrieving random samples. |
| **DataFrame Information Summary (`.info()`)** | ```python\nmovies.info()\nipl.info()\n``` | Generates a structured summary of row/column count, column data types, missing/null value counts, and total system memory footprint. |
| **Descriptive Statistics Summary (`.describe()`)** | ```python\nmovies.describe()\nipl.describe()\n``` | Automatically calculates statistical summaries (mean, standard deviation, min, max, percentiles) for all numeric columns. |
| **Missing Values Detection (`.isnull()`)** | ```python\nmovies.isnull().sum()\n``` | Identifies missing values (`NaN`/`None`). Chaining `.sum()` tallies the count of missing records per column, helping with data cleaning. |
| **Duplicate Row Check (`.duplicated()`)** | ```python\nmovies.duplicated().sum()\nstudents.duplicated().sum()\n``` | Evaluates if rows are identical duplicates of previously seen rows. Summing the mask yields the total duplicated count. |
| **Renaming Columns (`.rename()`)** | ```python\nstudents.rename(\n    columns={'marks':'percent', 'package':'lpa'},\n    inplace=True\n)\n``` | Modifies specific column names using a key-value dictionary map. Setting `inplace=True` directly alters the target DataFrame. |

---

## 🧮 3. Math & Aggregation Methods

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Column-wise Aggregation (Axis 0)** | ```python\nstudents.sum(axis=0)\n``` | Computes summaries downwards across rows for each individual column. `axis=0` is the default behavior in Pandas. |
| **Row-wise Aggregation (Axis 1)** | ```python\nstudents.mean(axis=1)\n``` | Computes values horizontally across columns for each row index (e.g., finding a student's average score across subjects). |
| **Column Variance (`.var()`)** | ```python\nstudents.var()\n``` | Returns the variance of numeric columns, showing how far data points are spread from their mean value. |

---

## 🎯 4. Indexing & Selecting Columns

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Single Column Extraction** | ```python\nmovies['title_x']\nipl['Venue']\n``` | Extracts a single column by name. This returns a 1D Pandas **Series** object sharing the DataFrame's index. |
| **Multi-Column Selection** | ```python\nmovies[['year_of_release', 'actors', 'title_x']]\nipl[['Team1', 'Team2', 'WinningTeam']]\n``` | Extracts a sub-DataFrame containing only the specified list of column names (order is respected). Note the **double square brackets**. |

---

## 📍 5. Indexing & Selecting Rows

> [!IMPORTANT]
> - `iloc` searches exclusively using **integer positional index coordinates** (0-based offsets).
> - `loc` searches exclusively using **row index labels** or strings.

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Positional Selection (`iloc`) - Single Row** | ```python\nmovies.iloc[5]\n``` | Extracts a single row at physical position `5` (the 6th row). Returns a Series with column headers as the index. |
| **Positional Selection (`iloc`) - Slice** | ```python\nmovies.iloc[:5]\n``` | Selects a continuous slice of row positions. Integer position slicing is **non-inclusive** of the end boundary (returns positions 0 to 4). |
| **Positional Selection (`iloc`) - Fancy List** | ```python\nmovies.iloc[[0,4,5]]\n``` | Extracts disjoint rows at custom positional indices passed as a Python list. |
| **Label-based Selection (`loc`) - Single Row** | ```python\nstudents.loc['nitish']\n``` | Finds and retrieves row data matching the custom index label string `'nitish'`. |
| **Label-based Selection (`loc`) - Slice** | ```python\nstudents.loc['nitish':'rishabh':2]\n``` | Slices rows alphabetically/order-wise from label `'nitish'` to `'rishabh'`, skipping every alternate row. Label slicing **is inclusive** of the end label! |
| **Label-based Selection (`loc`) - Fancy List** | ```python\nstudents.loc[['nitish','ankita','rupesh']]\n``` | Extracts disjoint rows corresponding to multiple label values. |
| **Positional Fallback on Labeled Data** | ```python\nstudents.iloc[[0,3,4]]\n``` | Even if a DataFrame uses string/labeled indexes, you can always fallback to `iloc` to query rows by physical coordinates. |

---

## 🧭 6. Multi-Axis Selection (Rows & Columns combined)

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Positional Rows & Columns** | ```python\nmovies.iloc[0:3, 0:3]\n``` | Selects rows from position `0` to `2` and columns from position `0` to `2`. Syntactically structured as `.iloc[row_slice, col_slice]`. |
| **Label-based Rows & Columns** | ```python\nmovies.loc[0:2, 'title_x':'poster_path']\n``` | Selects row labels `0` to `2` and column labels starting at `'title_x'` up to and including `'poster_path'`. |

---

## 🧼 7. Logical Filtering & Boolean Indexing

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Simple Boolean Condition Filter** | ```python\nmask = ipl['MatchNumber'] == 'Final'\nnew_df = ipl[mask]\nnew_df[['Season','WinningTeam']]\n``` | Computes a logical Series (mask) and uses it to subset matching rows. Selecting subset columns returns filtered properties. |
| **Chained Boolean Filter** | ```python\nipl[ipl['MatchNumber'] == 'Final'][['Season','WinningTeam']]\n``` | Identical filter logic as above, but written in a single compact chained expression without declaring a separate mask variable. |
| **Count Matching Matches** | ```python\nipl[ipl['SuperOver'] == 'Y'].shape[0]\n``` | Filters rows matching the condition and accesses the index `0` of the shape tuple to determine total matches. |
| **Bitwise AND Filtering (`&`)** | ```python\nipl[\n  (ipl['City'] == 'Kolkata') &\n  (ipl['WinningTeam'] == 'Chennai Super Kings')\n].shape[0]\n``` | Combines multiple row filter conditions. Each logical condition **must** be wrapped in standard parentheses `()`, using `&` (not `and`). |
| **Percentage Calculations** | ```python\n(\n  ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]\n  / ipl.shape[0]\n) * 100\n``` | Calculates the percentage of matches where the team winning the toss also won the match. |
| **Filtering Numeric Range Intersections** | ```python\nmovies[\n  (movies['imdb_rating'] > 8.5) &\n  (movies['imdb_votes'] > 10000)\n].shape[0]\n``` | Counts the subset of movies having ratings higher than 8.5 AND more than 10,000 votes. |
| **Text Pattern Matching (`.str.contains`)** | ```python\nmask1 = movies['genres'].str.contains('Action')\nmask2 = movies['imdb_rating'] > 7.5\nmovies[mask1 & mask2]\n``` | Uses Pandas vectorized string methods to match substrings. This filters highly-rated action movies. |

---

## ➕ 8. Modifying Structure & Creating Columns

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Constant Value Insertion** | ```python\nmovies['Country'] = 'India'\nmovies.head()\n``` | Creates a new column named `'Country'` and populates every row with the value `'India'` via vector broadcasting. |
| **Vectorized Feature Extraction** | ```python\nmovies.dropna(inplace=True)\nmovies['lead actor'] = (\n    movies['actors'].str.split('|').apply(lambda x: x[0])\n)\nmovies.head()\n``` | First cleans missing data in-place. Then splits actor listings by standard pipes (`\|`), applying a lambda to extract the first actor as the lead. |

---

## 💎 9. Column Type Casting & Memory Saving

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Downcasting Primitives** | ```python\nipl['ID'] = ipl['ID'].astype('int32')\n``` | Changes data representation from `int64` to `int32` to optimize memory usage, which is ideal for large datasets. |
| **Low-Cardinality Categorical Casting** | ```python\nipl['Team1'] = ipl['Team1'].astype('category')\nipl['Team2'] = ipl['Team2'].astype('category')\n``` | Converts text columns with repeated values (teams) into `category` types. This stores strings once internally and references them as integers, saving memory. |

---

## 📝 10. Advanced Exercises & Tasks

These advanced prompts are from the end of your session-17 notebook. You can test your code in your workspace:

* **Task 1: Track Record Function**
  * **Objective**: Write a reusable function that takes two teams as input arguments and returns their head-to-head match records.
* **Task 2: Play-offs Player of the Match**
  * **Objective**: Find the player with the highest "Player of the Match" (POTM) awards in IPL finals and playoff/qualifier matches.
* **Task 3: Toss Decision Plots**
  * **Objective**: Create a visualization chart representing teams' decisions after winning the toss (Field vs Bat).
* **Task 4: Match Distribution**
  * **Objective**: Find how many total matches each team has played in the dataset.
* **Task 5: Multivariable Sorting (`sort_values`)**
  * **Objective**: Sort dataframes by multiple columns, controlling ascending properties, handling nulls with `na_position`, and setting in-place flags.

---

> [!TIP]
> Use these formulas as templates in your Jupyter notebook **[pandassecond.ipynb](file:///home/shoaib/Desktop/Pandas_Project/pandassecond.ipynb)** to fast-track your data manipulation assignments!
