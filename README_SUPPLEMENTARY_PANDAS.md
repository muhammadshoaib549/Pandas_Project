# 📒 Supplementary Pandas Series: Complete Lookup Guide

Welcome to the **Supplementary Pandas Series Lookup Guide**! This document serves as your structured companion manual for the interactive notebook **[suplementrypandas.ipynb](file:///home/shoaib/Desktop/Pandas_Project/suplementrypandas.ipynb)**. It features a complete educational breakdown of the Pandas **Series** object—from initialization to powerful advanced methods.

> [!NOTE]
> This guide is kept separately from your other materials to ensure modular learning. It provides a complete three-column layout mapping: **Concept Name**, **Code**, and **Detailed Explanation** for every single instruction in the notebook.

---

## ⚡ 1. Introduction & Core Creation

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **What is Pandas?** | *Conceptual* | **Pandas** is a robust, open-source data analysis and manipulation engine built on Python. It provides high-performance data structures for dealing with tabular inputs. |
| **What is a Pandas Series?** | *Conceptual* | A **Series** is a 1-Dimensional array holding data of any homogeneous type. It features a parallel array of index labels, providing hashmap-like constant-time lookups. |
| **Importing Libraries** | ```python\nimport numpy as np\nimport pandas as pd\n``` | Loads **NumPy** for vector math and **Pandas** for structural objects. |
| **Series from List (Strings)** | ```python\ncountry = ['India', 'Pakistan', 'USA', 'Nepal', 'Srilanka']\npd.Series(country)\n``` | Converts an array of string elements into a Series with a default integer range index `[0, 1, 2...]`. |
| **Series from List (Integers)** | ```python\nruns = [13, 24, 56, 78, 100]\nruns_ser = pd.Series(runs)\n``` | Converts integer inputs into a `Series` (creates a highly optimized numerical 1D array of type `int64`). |
| **Custom Subject Indexing** | ```python\nmarks = [67, 57, 89, 100]\nsubjects = ['maths', 'english', 'science', 'hindi']\npd.Series(marks, index=subjects)\n``` | Creates an index with custom subject label keys rather than default sequential integer coordinates. |
| **Naming the Series** | ```python\nmarks = pd.Series(marks, index=subjects, name='Nitish ke marks')\nmarks\n``` | Sets a descriptive `name` metadata attribute on the Series. Useful when integrating columns or making DataFrame columns. |
| **Series from Dictionary** | ```python\nmarks = {\n    'maths': 67,\n    'english': 57,\n    'science': 89,\n    'hindi': 100\n}\nmarks_series = pd.Series(marks, name='nitish ke marks')\nmarks_series\n``` | Automatically parses dictionary keys to become Series index labels, and dictionary values to populate the series. |

---

## 💎 2. Series Attributes

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Total Size (`.size`)** | ```python\nmarks_series.size\n``` | Returns the absolute count of elements stored in the Series (nulls included). |
| **Data Type Check (`.dtype`)** | ```python\nmarks_series.dtype\n``` | Displays the data type of the underlying array (e.g., `int64`, `float64`, `object`). |
| **Metadata Name Check (`.name`)** | ```python\nmarks_series.name\n``` | Accesses or updates the string representation assigned to the series. |
| **Unique Checker (`.is_unique`)** | ```python\nmarks_series.is_unique\npd.Series([1,1,2,3,4,5]).is_unique\n``` | Returns a boolean `True` if all series values are completely unique; returns `False` if duplicates exist. |
| **Index Representation (`.index`)** | ```python\nmarks_series.index\nruns_ser.index\n``` | Retrieves the Index object detailing row labels. |
| **Underlying NumPy Array (`.values`)** | ```python\nmarks_series.values\n``` | Extracts and exposes raw numerical elements as an unlabelled **1D NumPy ndarray**. |

---

## 💾 3. File Imports & Squeezing

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Single Column CSV Squeezing** | ```python\nsubs = pd.read_csv('/content/subs.csv', squeeze=True)\nsubs\n``` | Reads a single-column CSV. Setting `squeeze=True` forces Pandas to load the dataset directly as a 1-Dimensional Series. |
| **Multi-Column Text CSV Squeezing** | ```python\nvk = pd.read_csv('/content/kohli_ipl.csv', index_col='match_no', squeeze=True)\nvk\n``` | Loads a 2-column IPL match file, setting the `match_no` column as the index labels, squeezing the remaining column into a Series. |
| **Text-indexed Movie Squeezing** | ```python\nmovies = pd.read_csv('/content/bollywood.csv', index_col='movie', squeeze=True)\nmovies\n``` | Creates an actor lookup Series where movie titles represent index labels and actor names are the Series values. |

---

## 🔍 4. Inspection, value_counts & Sorting

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Display Extremities (`.head()` / `.tail()`)** | ```python\nsubs.head()\nvk.head(3)\nvk.tail(10)\n``` | Head views the first `n` records; Tail views the last `n` records from the ends of the Series. |
| **Random Sampling (`.sample()`)** | ```python\nmovies.sample(5)\n``` | Extracts `n` random samples, helping check the dataset without directional bias. |
| **Value Frequency Counts (`.value_counts()`)** | ```python\nmovies.value_counts()\n``` | Tallies occurrences of unique categories in the Series, sorting values high-to-low by default. |
| **Sorting Values** | ```python\nvk.sort_values(ascending=False).head(1).values[0]\nvk.sort_values(ascending=False)\nvk.sort_values(inplace=True)\n``` | Sorts values. `ascending=False` sorts descending. `inplace=True` writes the sorted representation in-place. |
| **Sorting Row Labels** | ```python\nmovies.sort_index(ascending=False, inplace=True)\nmovies\n``` | Re-arranges the Series alphabetically or numerically based on the **index labels** instead of values. |

---

## 🧮 5. Statistical Computations

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Count Valid Elements (`.count()`)** | ```python\nvk.count()\n``` | Tally only the non-null elements in the Series. (Excludes missing values/NaNs). |
| **Summation (`.sum()`)** | ```python\nsubs.sum()\n``` | Returns the sum total of all numerical elements. |
| **Summary Statistics** | ```python\nsubs.mean()\nprint(vk.median())\nprint(movies.mode())\nprint(subs.std())\nprint(vk.var())\n``` | Computes essential descriptive math properties: mean (average), median (mid-point), mode (most frequent), standard deviation, and variance. |
| **Maximum Value Selection (`.max()`)** | ```python\nsubs.max()\n``` | Finds and returns the maximum element in the dataset. |
| **Descriptive Summary Table (`.describe()`)** | ```python\nsubs.describe()\n``` | Outputs a quick overview of count, mean, std, min, 25%, 50%, 75% percentiles, and max. |

---

## 🎯 6. Slicing, Slicing Constraints & Fancy Indexing

> [!WARNING]
> Accessing positional indices using negative values (`-1`) raises errors in Series that use default integer indices (`0, 1, 2...`) because Pandas can confuse it with a potential label of `-1`. It works perfectly if the index consists of non-integer labels (like string keys).

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Positional Integer Indexing** | ```python\nx = pd.Series([12, 13, 14, 35, 46, 57, 58, 79, 9])\nx\n``` | Standard zero-indexed item query. |
| **Negative Index Lookup** | ```python\nx[-1]          # Raises error (IntIndex)\nvk[-1]         # Raises error (IntIndex)\nmarks_series[-1] # Works perfectly (LabelIndex)\n``` | Demonstrates positional tail lookup constraints. Labeled indices allow negative indexing, while standard range integer indexes throw exceptions. |
| **Continuous Slice Range** | ```python\nvk[5:16]\nvk[-5:]\nmovies[::2]\n``` | Extracts elements in a range. Slicing using positions is non-inclusive of the upper boundary value. |
| **Fancy Index Lists** | ```python\nvk[[1, 3, 4, 5]]\n``` | Queries disjoint items by passing a nested Python list of labels/positions. |
| **Key Lookup** | ```python\nmovies['2 States (2014 film)']\n``` | Directly fetches the value mapped to a specific text label index in constant time. |

---

## ✏️ 7. Overwriting & Dynamic Appending

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Overwriting Value** | ```python\nmarks_series[1] = 100\nmarks_series\n``` | Modifies the element at position index `1` in-place. |
| **Inserting Missing Label** | ```python\nmarks_series['evs'] = 100\nmarks_series\n``` | Assigning a value to an index key that doesn't exist automatically creates the label and appends the value. |
| **Updating Continuous Slices** | ```python\nruns_ser[2:4] = [100, 100]\nruns_ser\n``` | Replaces multiple consecutive values using slice notation assignments. |
| **Updating Disjoint Indices** | ```python\nruns_ser[[0, 3, 4]] = [0, 0, 0]\nruns_ser\n``` | Uses fancy index lists to modify scattered positions simultaneously. |
| **Label-based Modification** | ```python\nmovies['2 States (2014 film)'] = 'Alia Bhatt'\nmovies\n``` | Targets and updates a value using its custom string key. |

---

## 🐍 8. Primitives Compatibility & Set Operations

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Python Built-in Primitives** | ```python\nprint(len(subs))\nprint(type(subs))\nprint(dir(subs))\nprint(sorted(subs))\nprint(min(subs))\nprint(max(subs))\n``` | Demonstrates compatibility with built-ins like `len()`, `type()`, `sorted()`, list methods mapping (`dir()`), `min()`, and `max()`. |
| **Type Conversions** | ```python\nlist(marks_series)\ndict(marks_series)\n``` | Conversions to native Python structures like lists or standard dictionaries. |
| **Membership Check (`in`)** | ```python\n'2 States (2014 film)' in movies\n'Alia Bhatt' in movies.values\n``` | Checking `key in series` checks the index labels. To test inside elements, check on `.values`. |
| **Iteration Loop** | ```python\nfor i in movies.index:\n  print(i)\n``` | Iterates over elements. Loops on `.index` return label keys, while loops on the Series yield values. |

---

## ⚡ 9. Vectorized Operators & Boolean Subsetting

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Arithmetic Broadcasting** | ```python\n100 + marks_series\n``` | Modifies elements in vectorized speed without explicit Python `for` loops. |
| **Relational Boolean Masks** | ```python\nvk >= 50\n``` | Compares elements, returning a boolean series indicating elements satisfying the constraint. |
| **Boolean Index Filtering** | ```python\nvk[vk >= 50].size\nvk[vk == 0].size\nsubs[subs > 200].size\n``` | Filters the Series, keeping only rows that align with `True` values in the boolean mask. |
| **Frequency Mask Subsetting** | ```python\nnum_movies = movies.value_counts()\nnum_movies[num_movies > 20]\n``` | Computes counts first, then applies boolean filtering on category sizes. |

---

## 📈 10. Visualization Plots

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Integrated Line Plot** | ```python\nsubs.plot()\n``` | Automatically generates a line plot mapping sequential indices over Series values. |
| **Integrated Pie Distribution** | ```python\nmovies.value_counts().head(20).plot(kind='pie')\n``` | Creates an illustrative pie chart showing value distributions of the top 20 categories. |

---

## 💎 11. Core Advanced Methods

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Memory Saving Cast (`.astype()`)** | ```python\nimport sys\nsys.getsizeof(vk)\nsys.getsizeof(vk.astype('int16'))\n``` | Casts storage structures (e.g., `int64` to `int16`) to optimize memory footprint. |
| **Interval Matching (`.between()`)** | ```python\nvk[vk.between(51, 99)].size\n``` | Returns a boolean mask checking if elements fall inside the inclusive numeric boundaries `[start, end]`. |
| **Boundary Clamping (`.clip()`)** | ```python\nsubs.clip(100, 200)\n``` | Outlier clamping. Lower values are set to `100`; values above are capped at `200`. |
| **Drop Duplicated Items (`.drop_duplicates()`)** | ```python\ntemp = pd.Series([1, 1, 2, 2, 3, 3, 4, 4])\ntemp.drop_duplicates(keep='last')\nmovies.drop_duplicates()\n``` | Keeps unique elements. Setting `keep='last'` retains the last occurrence of duplicates; `keep='first'` keeps the first. |
| **Duplicate Checking (`.duplicated()`)** | ```python\ntemp.duplicated().sum()\nvk.duplicated().sum()\n``` | Identifies duplicates with a boolean Series. Summing it returns the total duplicates count. |
| **Null Value Audit (`.isnull()`)** | ```python\ntemp = pd.Series([1, 2, 3, np.nan, 5, 6, np.nan, 8, np.nan, 10])\ntemp.isnull().sum()\n``` | Finds missing (`NaN`) entries. Summing the mask yields total null counts. |
| **Exclude Null Entries (`.dropna()`)** | ```python\ntemp.dropna()\n``` | Filters out rows that contain missing or null (`NaN`) inputs. |
| **Substitute Missing Inputs (`.fillna()`)** | ```python\ntemp.fillna(temp.mean())\n``` | Substitutes missing values with a designated fallback value (such as the Series average). |
| **List Membership Lookup (`.isin()`)** | ```python\nvk[(vk == 49) | (vk == 99)]\nvk[vk.isin([49, 99])]\n``` | Tests if elements match list values. Much cleaner and faster than multiple chained logical OR (`\|`) statements. |
| **Element-wise Apply (`.apply()`)** | ```python\nmovies.apply(lambda x: x.split()[0].upper())\nsubs.apply(lambda x: 'good day' if x > subs.mean() else 'bad day')\n``` | Applies custom functions or lambdas element-wise across all rows in the Series. |
| **Views vs Safe Copying (`.copy()`)** | ```python\nnew = vk.head()\nnew[1] = 1 # Edits parent vk!\nnew = vk.head().copy()\nnew[1] = 100 # Safe\n``` | Slicing creates reference views. Modifying views updates the original Series. Create safe independent clones with `.copy()`. |

---

> [!TIP]
> Keep this lookup cheat-sheet open when working on your assignments inside **[suplementrypandas.ipynb](file:///home/shoaib/Desktop/Pandas_Project/suplementrypandas.ipynb)** to speed up your development workflows!
