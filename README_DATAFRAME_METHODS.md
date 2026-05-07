# 🗂️ Pandas DataFrame Methods: Advanced Reference Guide

Welcome to the **Pandas DataFrame Methods Master Reference Guide**! This comprehensive document represents a complete, self-contained educational resource mapping the most powerful methods and utilities of Pandas **Series** and **DataFrames** covered in **[dataframes.ipynb](file:///home/shoaib/Desktop/Pandas_Project/dataframes.ipynb)**.

> [!NOTE]
> This guide provides a premium 3-column reference layout: **Concept Name**, **Code**, and **Detailed Explanation**. Use it to look up operations, understand parameters, and optimize your data science workflow.

---

## 🚀 1. Aggregation, Frequency & Sorting

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Element Frequency counts (`value_counts()`)** | ```python\na = pd.Series([1,1,1,2,2,3])\na.value_counts()\n``` | Counts the occurrences of each unique element. Returns a new Series indexed by the unique values, sorted in descending order of frequency. |
| **DataFrame-wide Value Frequency** | ```python\nmarks.value_counts()\n``` | Counts combinations of unique rows in a DataFrame, displaying the frequency of duplicate records across selected columns. |
| **Filtered Row Frequency Counts** | ```python\nipl[\n  ~ipl['MatchNumber'].str.isdigit()\n]['Player_of_Match'].value_counts()\n``` | Extracts non-digit match records (such as play-off/final matches) using string-not-digit negation (`~`), and aggregates POTM frequency. |
| **Pie Chart Visual Output** | ```python\nipl['TossDecision'].value_counts().plot(kind='pie')\n``` | Aggregates the unique values of a column (Toss Decisions) and directly renders a visual pie representation. |
| **Cross-Column Summation & Sorting** | ```python\n(\n  ipl['Team2'].value_counts() + \n  ipl['Team1'].value_counts()\n).sort_values(ascending=False)\n``` | Adds value frequencies across different columns to find the total matches played per team, then sorts the results high-to-low. |
| **Series Sorting (`sort_values()`)** | ```python\nx = pd.Series([12, 14, 1, 56, 89])\nx.sort_values(ascending=False)\n``` | Sorts values of the Series. Setting `ascending=False` sorts the values in descending order. |
| **DataFrame Sorting by Column** | ```python\nmovies.sort_values('title_x', ascending=False)\n``` | Re-arranges the DataFrame rows by sorting alphabetical strings in the specified `'title_x'` column. |
| **Handling Nulls in Sorting** | ```python\nstudents.sort_values(\n  'name', \n  na_position='first', \n  ascending=False, \n  inplace=True\n)\n``` | Sorts rows by `'name'`. Specifying `na_position='first'` places missing (`NaN`) values at the top of the sorted DataFrame. |
| **Multi-Column Key Sorting** | ```python\nmovies.sort_values(\n  ['year_of_release', 'title_x'], \n  ascending=[True, False]\n)\n``` | Sorts rows hierarchically: first by year of release in ascending order, then by title in descending order for ties. |

---

## 📈 2. Ranking & Index Management

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Value Ranking (`.rank()`)** | ```python\nbatsman['batting_rank'] = (\n  batsman['batsman_run'].rank(ascending=False)\n)\nbatsman.sort_values('batting_rank')\n``` | Assigns mathematical ranks to values. If elements are identical, rank resolves ties (by default, taking the average of the rank indices). |
| **Sorting by Index Labels** | ```python\nmarks_series.sort_index(ascending=False)\nmovies.sort_index(ascending=False)\n``` | Restructures the Series/DataFrame by sorting the index labels alphabetically or numerically instead of values. |
| **Assigning Row Index (`set_index`)** | ```python\nbatsman.set_index('batter', inplace=True)\n``` | Overwrites the default integer range index with a specified column (e.g., `'batter'`), enabling fast string-label index lookups. |
| **Resetting Index (`reset_index`)** | ```python\nbatsman.reset_index(inplace=True)\n``` | Reverts the index back to a standard sequential integer RangeIndex `[0, 1, 2...]`. If `drop=True` (not specified here), the previous index column is discarded. |
| **Index Swapping Without Loss** | ```python\nbatsman.reset_index().set_index('batting_rank')\n``` | Resets the current index to a normal column before setting a brand-new column as index, ensuring no lookup data is deleted. |
| **Series-to-DataFrame Cast** | ```python\nmarks_series.reset_index()\n``` | Converts a Series into a 2-Column DataFrame where column 1 is the previous index and column 2 is the actual values. |
| **Renaming Index & Columns** | ```python\nmovies.set_index('title_x', inplace=True)\nmovies.rename(\n  columns={'imdb_id':'imdb', 'poster_path':'link'},\n  inplace=True\n)\nmovies.rename(index={\n  'Uri: The Surgical Strike':'Uri',\n  'Battalion 609':'Battalion'\n})\n``` | Renames column headers and row labels using mapper dictionaries. Supports index label corrections directly in-place. |

---

## 🔍 3. Uniqueness, Missing Values & Duplicates

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Unique Elements Array (`.unique()`)** | ```python\ntemp.unique()\nlen(temp.unique())\n``` | Returns a NumPy array containing only unique elements from the Series (including any missing `NaN` values as a unique item). |
| **Unique Elements Count (`.nunique()`)** | ```python\ntemp.nunique()\nipl['Season'].nunique()\n``` | Computes the count of unique elements in the Series/DataFrame. By default, **does not count missing/null values** as unique. |
| **Filtering Missing Values (`.isnull()`)** | ```python\nstudents['name'][students['name'].isnull()]\n``` | Generates a boolean mask mapping cells that are empty (`NaN`). Used here to filter and display only missing rows. |
| **Filtering Non-Null Values (`.notnull()`)** | ```python\nstudents['name'][students['name'].notnull()]\n``` | Generates a boolean mask identifying valid cells, filtering out all missing values. |
| **Exhaustive Null Check (`.hasnans`)** | ```python\nstudents['name'].hasnans\n``` | Returns a quick boolean `True` if the target Series contains one or more missing (`NaN`) values. |
| **Row-wise Null Evaluation** | ```python\nstudents.isnull()\nstudents.notnull()\n``` | Generates a boolean representation of the DataFrame, mapping every element position to `True`/`False` based on null status. |
| **Dropping Null Rows (`dropna`)** | ```python\nstudents.dropna(how='any')\nstudents.dropna(how='all')\n``` | Drops row records. `how='any'` drops rows if any value is missing; `how='all'` drops rows only if every column value is null. |
| **Subset-targeted Null Dropping** | ```python\nstudents.dropna(subset=['name'])\nstudents.dropna(subset=['name', 'college'])\n``` | Restricts the null analysis to a specific list of columns. It drops rows only if missing inputs appear in those targeted columns. |
| **Null Value Imputation (`fillna`)** | ```python\nstudents['name'].fillna('unknown')\nstudents['package'].fillna(\n  students['package'].mean()\n)\n``` | Substitutes missing values with specified fallbacks (e.g., constant strings or summary statistics like the column average). |
| **Backfill Imputation (`bfill`)** | ```python\nstudents['name'].fillna(method='bfill')\n``` | Imputes missing inputs by copying the next consecutive valid element upwards (backward filling). |
| **Dropping Duplicate Rows** | ```python\ntemp.drop_duplicates()\nmarks.drop_duplicates(keep='last')\nstudents.drop_duplicates()\n``` | Removes duplicates. `keep='last'` retains only the final occurrence, while `keep='first'` (default) keeps the first. |
| **Complex Duplication Sieve** | ```python\nipl['all_players'] = (\n  ipl['Team1Players'] + ipl['Team2Players']\n)\nipl['did_kohli_play'] = (\n  ipl['all_players'].apply(\n    lambda x: 'V Kohli' in x\n  )\n)\nipl[\n  (ipl['City'] == 'Delhi') &\n  (ipl['did_kohli_play'] == True)\n].drop_duplicates(\n  subset=['City', 'did_kohli_play'],\n  keep='first'\n)\n``` | Combines player rosters, applies membership flags, filters matching locations, and sifts unique location combinations. |

---

## 🗑️ 4. Dropping & Vectorized Mapping

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Dropping Series Indices** | ```python\ntemp.drop(index=[0,6])\n``` | Removes elements at specified index positions, leaving other values untouched. |
| **Dropping DataFrame Columns** | ```python\nstudents.drop(\n  columns=['branch', 'cgpa'],\n  inplace=True\n)\n``` | Drops specific columns from the DataFrame. |
| **Dropping Rows by Name Label** | ```python\nstudents.set_index('name').drop(\n  index=['nitish', 'aditya']\n)\n``` | Swaps row indices to labels and drops corresponding student rows. |
| **Element-wise Series Map (`apply`)** | ```python\ndef sigmoid(value):\n  return 1 / (1 + np.exp(-value))\ntemp.apply(sigmoid)\n``` | Maps custom Python mathematical operations across each element of the Series in vectorized speed. |
| **Row-wise DataFrame Map (`axis=1`)** | ```python\ndef euclidean(row):\n  pt_A = row['1st point']\n  pt_B = row['2nd point']\n  return (\n    (pt_A[0] - pt_B[0])**2 + \n    (pt_A[1] - pt_B[1])**2\n  )**0.5\npoints_df['distance'] = (\n  points_df.apply(euclidean, axis=1)\n)\n``` | Applies functions horizontally across rows (`axis=1`). Passes each row as a Series to compute custom metrics (e.g., Euclidean distance). |

---

## 💎 5. Essential Advanced Methods (Reference Templates)

The following core utilities are placeholders in your notebook—here is how you can use them:

* **`.isin()`**
  * **Code**: `df[df['col'].isin(['A', 'B', 'C'])]`
  * **Explanation**: Returns a boolean mask identifying if column values match entries in a list. Ideal for quick, optimized filtering.
* **`.corr()`**
  * **Code**: `df.corr(numeric_only=True)`
  * **Explanation**: Computes pairwise Pearson correlation coefficients between numerical variables to evaluate linear trends.
* **`.nlargest()` & `.nsmallest()`**
  * **Code**: `df.nlargest(5, 'col')`
  * **Explanation**: Retrieves the top (or bottom) `n` records sorted by a target column, executing faster than standard `sort_values().head()`.
* **`.insert()`**
  * **Code**: `df.insert(index_loc, 'new_col_name', values)`
  * **Explanation**: Inserts a new column at a specific position index rather than appending it to the end of the DataFrame.
* **`.copy()`**
  * **Code**: `cloned_df = df.copy()`
  * **Explanation**: Clones the DataFrame. This prevents changes made to the duplicate from updating the original source (avoids SettingWithCopy warnings).

---

> [!TIP]
> Use these layouts to speed up your data transformations inside **[dataframes.ipynb](file:///home/shoaib/Desktop/Pandas_Project/dataframes.ipynb)**!
