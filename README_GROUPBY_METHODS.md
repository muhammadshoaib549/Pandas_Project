# 📂 Pandas GroupBy & DataFrame Methods: Comprehensive Reference Guide

Welcome to the **Pandas GroupBy & Advanced DataFrame Methods Master Reference Guide**! This comprehensive documentation acts as an interactive reference for modern Pandas operations mapped in your interactive notebook **[groupby.ipynb](file:///home/shoaib/Desktop/Pandas_Project/groupby.ipynb)**.

> [!NOTE]
> This guide features a premium, self-contained 3-column lookup layout: **Concept Name**, **Code**, and **Detailed Explanation**. All existing READMEs are preserved completely untouched!

---

## 🏗️ 1. Advanced Frequency Analysis & Multi-Column Sorting

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Simple Value Frequencies (`value_counts()`)** | ```python\na = pd.Series([1, 1, 1, 2, 2, 3])\na.value_counts()\n``` | Tallies occurrences of unique values inside a Series, returning a frequency distribution sorted in descending order. |
| **Row-wise Unique Combinations** | ```python\nmarks.value_counts()\n``` | Examines raw combinations of values across all columns of a DataFrame, computing the frequency of exact duplicate rows. |
| **Vectorized Text Filtering Frequencies** | ```python\nipl[\n  ~ipl['MatchNumber'].str.isdigit()\n]['Player_of_Match'].value_counts()\n``` | Uses string negation (`~` and `.str.isdigit()`) to select play-off/final matches, then aggregates Player of the Match awards for those games. |
| **Visualizing Distributions** | ```python\nipl['TossDecision'].value_counts().plot(kind='pie')\n``` | Aggregates choices made after winning the toss (Field vs Bat) and renders them instantly as an illustrative pie chart. |
| **Summing Disjoint Series Combinations** | ```python\n(\n  ipl['Team2'].value_counts() + \n  ipl['Team1'].value_counts()\n).sort_values(ascending=False)\n``` | Adds two Series together by matching index labels (team names) to compute total matches played, then sorts the results descending. |
| **Sorting Values Descending** | ```python\nx = pd.Series([12, 14, 1, 56, 89])\nx.sort_values(ascending=False)\n``` | Sorts values. Specifying `ascending=False` orders the data from highest to lowest. |
| **Sorting DataFrame Alphabetically** | ```python\nmovies.sort_values('title_x', ascending=False)\n``` | Aligns the entire DataFrame by sorting values in the `'title_x'` column alphabetically in reverse. |
| **Null Positioning in Sorting** | ```python\nstudents.sort_values(\n  'name', \n  na_position='first', \n  ascending=False, \n  inplace=True\n)\n``` | Orders rows. Setting `na_position='first'` positions missing elements (`NaN`) at the top of the sorted index in-place. |
| **Hierarchical Multi-Key Sorting** | ```python\nmovies.sort_values(\n  ['year_of_release', 'title_x'], \n  ascending=[True, False]\n)\n``` | Sorts data by year of release in ascending order, and resolves ties by sorting movie titles in descending order. |

---

## 📈 2. Numerical Ranking & Index Transformations

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Numerical Value Ranking (`.rank()`)** | ```python\nbatsman['batting_rank'] = (\n  batsman['batsman_run'].rank(ascending=False)\n)\nbatsman.sort_values('batting_rank')\n``` | Assigns ranks to rows. Handled using ascending or descending orders, resolving tie-breaks automatically with average values. |
| **Sorting Index Labels** | ```python\nmarks_series.sort_index(ascending=False)\nmovies.sort_index(ascending=False)\n``` | Sorts Series or DataFrame indices rather than sorting their cell value arrays. |
| **Assigning Row Index Label** | ```python\nbatsman.set_index('batter', inplace=True)\n``` | Replaces default integer row coordinates with a column (e.g., `'batter'`), enabling fast string key-based lookups. |
| **Restoring Range Index** | ```python\nbatsman.reset_index(inplace=True)\n``` | Restores row indexes to the standard RangeIndex `[0, 1, 2...]` without discarding historical indexing columns. |
| **Non-Destructive Index Replacement** | ```python\nbatsman.reset_index().set_index('batting_rank')\n``` | Moves the active index back into the DataFrame as a normal column before setting a brand-new custom index. |
| **Series-to-DataFrame Re-shaping** | ```python\nmarks_series.reset_index()\n``` | Un-pivots a 1D Pandas Series, outputting a 2-Column DataFrame mapping old index labels to values. |
| **Selective Label Renaming** | ```python\nmovies.set_index('title_x', inplace=True)\nmovies.rename(\n  columns={'imdb_id':'imdb', 'poster_path':'link'},\n  inplace=True\n)\nmovies.rename(index={\n  'Uri: The Surgical Strike':'Uri',\n  'Battalion 609':'Battalion'\n})\n``` | Renames column headers and specific index rows using python dictionaries. |

---

## 🔍 3. Uniqueness, Null Value Auditing & Deduplication

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Unique Elements Array (`.unique()`)** | ```python\ntemp.unique()\nlen(temp.unique())\n``` | Returns a raw NumPy ndarray of unique values present in the Series (including `NaN` as a unique representation). |
| **Count Unique Items (`.nunique()`)** | ```python\ntemp.nunique()\nipl['Season'].nunique()\n``` | Calculates the total count of unique categories in the dataset, **automatically excluding NaNs** from the final count. |
| **Locating Empty Cells (`.isnull()`)** | ```python\nstudents['name'][students['name'].isnull()]\n``` | Generates a boolean mask identifying empty (`NaN`) fields, filtering and displaying only rows with missing values. |
| **Locating Valid Fields (`.notnull()`)** | ```python\nstudents['name'][students['name'].notnull()]\n``` | Generates a boolean mask identifying valid cells, filtering out all missing values. |
| **Null Existence Flag (`.hasnans`)** | ```python\nstudents['name'].hasnans\n``` | Returns a fast boolean check (`True`/`False`) indicating if a Series contains one or more null elements. |
| **Row-wise Null Maps** | ```python\nstudents.isnull()\nstudents.notnull()\n``` | Generates a boolean representation mapping the presence of null values for every coordinate in the dataset. |
| **Dropping Rows with Missing Data** | ```python\nstudents.dropna(how='any')\nstudents.dropna(how='all')\n``` | Drops rows based on nulls. `how='any'` drops rows if any value is missing; `how='all'` drops rows only if every single column is null. |
| **Targeted Row Dropping** | ```python\nstudents.dropna(subset=['name'])\nstudents.dropna(subset=['name', 'college'])\n``` | Limits missing-value analysis to selected columns, keeping rows that have valid data in those critical columns. |
| **Null Substitution (`fillna`)** | ```python\nstudents['name'].fillna('unknown')\nstudents['package'].fillna(\n  students['package'].mean()\n)\n``` | Fills missing cells with fallback scalars or derived averages to keep dataset sizes consistent. |
| **Backward Imputation** | ```python\nstudents['name'].fillna(method='bfill')\n``` | Fills nulls by copying down values from the next adjacent valid cell below. |
| **Dropping Duplicate Records** | ```python\ntemp.drop_duplicates()\nmarks.drop_duplicates(keep='last')\nstudents.drop_duplicates()\n``` | Removes duplicate rows. `keep='last'` retains only the final occurrence, while `keep='first'` keeps the first. |
| **Filtering Duplicates using Masks** | ```python\nipl['all_players'] = (\n  ipl['Team1Players'] + ipl['Team2Players']\n)\nipl['did_kohli_play'] = (\n  ipl['all_players'].apply(\n    lambda x: 'V Kohli' in x\n  )\n)\nipl[\n  (ipl['City'] == 'Delhi') &\n  (ipl['did_kohli_play'] == True)\n].drop_duplicates(\n  subset=['City', 'did_kohli_play'],\n  keep='first'\n)\n``` | Merges team lists, creates logical masks, filters by city and player, and drop duplicate location entries. |

---

## 🗑️ 4. Selective Dropping & Custom Vectorized Transforms

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Dropping Series Coordinates** | ```python\ntemp.drop(index=[0,6])\n``` | Removes elements at specified index positions, leaving other values untouched. |
| **Dropping DataFrame Columns** | ```python\nstudents.drop(\n  columns=['branch', 'cgpa'],\n  inplace=True\n)\n``` | Drops selected columns from the DataFrame. |
| **Dropping Rows by Index Label** | ```python\nstudents.set_index('name').drop(\n  index=['nitish', 'aditya']\n)\n``` | Drops specified student rows by their name labels. |
| **Custom Vectorized Maps (`apply`)** | ```python\ndef sigmoid(value):\n  return 1 / (1 + np.exp(-value))\ntemp.apply(sigmoid)\n``` | Applies custom mathematical operations to each individual element of a Series. |
| **Row-wise DataFrame Maps (`axis=1`)** | ```python\ndef euclidean(row):\n  pt_A = row['1st point']\n  pt_B = row['2nd point']\n  return (\n    (pt_A[0] - pt_B[0])**2 + \n    (pt_A[1] - pt_B[1])**2\n  )**0.5\npoints_df['distance'] = (\n  points_df.apply(euclidean, axis=1)\n)\n``` | Computes metrics horizontally across columns for each row (`axis=1`) by passing the entire row as a Series. |

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
> Use these layouts to speed up your data transformations inside **[groupby.ipynb](file:///home/shoaib/Desktop/Pandas_Project/groupby.ipynb)**!
