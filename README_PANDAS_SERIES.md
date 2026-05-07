# 🐼 Pandas Series: Master Reference Guide

Welcome to the **Pandas Series Master Reference Guide**! This document serves as a complete, self-contained educational resource detailing the 1-Dimensional array structure of Pandas—the **Series**. 

> [!NOTE]
> This guide is dynamically generated from the codebase and maps every core concept, function, and attribute covered in the learning session. It provides a complete three-column layout: **Concept Name**, **Code**, and **Explanation**.

---

## 🚀 1. Library Initialization & Basics

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **What is Pandas?** | *Conceptual* | **Pandas** is a fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation tool built on top of the Python programming language. |
| **What is a Pandas Series?** | *Conceptual* | A **Series** is a 1-Dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.). It behaves like a single column in a table. |
| **Importing Libraries** | ```python\nimport numpy as np\nimport pandas as pd\n``` | Imports **NumPy** (for underlying numerical array computations) and **Pandas** (for high-level data structures and manipulation). |

---

## 🛠️ 2. Series Creation

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Series from List (String Data)** | ```python\ncountry = ['India', 'Pakistan', 'USA', 'Nepal', 'Srilanka']\npd.Series(country)\n``` | Converts a Python list of strings into a Series. Since no index is specified, Pandas automatically assigns standard integer indices starting from `0`. |
| **Series from List (Integer Data)** | ```python\nruns = [13, 24, 56, 78, 100]\nruns_ser = pd.Series(runs)\n``` | Converts a list of integers into a Series. It creates an 1D array of integers (`int64` data type) with default indexing. |
| **Custom Label Indexing** | ```python\nmarks = [67, 57, 89, 100]\nsubjects = ['maths', 'english', 'science', 'hindi']\npd.Series(marks, index=subjects)\n``` | Customizes the index labels of the Series. Instead of standard integers, elements are now indexed by subject names, which acts as a key-value lookup. |
| **Naming a Series** | ```python\nmarks = pd.Series(marks, index=subjects, name='Nitish ke marks')\nmarks\n``` | Assigns a descriptive `name` to the Series. This name acts as the column identifier when the Series is integrated into a multi-column DataFrame. |
| **Series from Dictionary** | ```python\nmarks = {\n    'maths': 67,\n    'english': 57,\n    'science': 89,\n    'hindi': 100\n}\nmarks_series = pd.Series(marks, name='nitish ke marks')\nmarks_series\n``` | Direct conversion of a Python dictionary. The dictionary **keys** automatically map to the **Series Index** and the dictionary **values** map to the **Series values**. |

---

## 🔍 3. Series Attributes

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Size Attribute (`.size`)** | ```python\nmarks_series.size\n``` | Returns the total count of elements (including any missing/NaN values) stored in the Series. |
| **Data Type Attribute (`.dtype`)** | ```python\nmarks_series.dtype\n``` | Displays the data type of the stored values. Homogeneous arrays will report types like `int64`, `float64`, or `object` (for strings/mixed types). |
| **Name Attribute (`.name`)** | ```python\nmarks_series.name\n``` | Retrieves the current name string assigned to the Series. |
| **Uniqueness Check (`.is_unique`)** | ```python\nmarks_series.is_unique\npd.Series([1,1,2,3,4,5]).is_unique\n``` | Returns `True` if every single value in the Series is unique (no duplicate values exist). Otherwise, returns `False`. |
| **Index Retrieval (`.index`)** | ```python\nmarks_series.index\nruns_ser.index\n``` | Accesses the Index object containing all lookup labels associated with the Series. |
| **Values Retrieval (`.values`)** | ```python\nmarks_series.values\n``` | Extracts the underlying raw data of the Series, returning it as a standard **NumPy ndarray**. |

---

## 💾 4. Loading External Datasets via CSV

> [!IMPORTANT]
> The `squeeze=True` parameter was historically used to automatically convert single-column DataFrames into 1-Dimensional Series upon import. In newer Pandas versions, this is achieved using `.squeeze()`.

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Read Single-Column CSV as Series** | ```python\nsubs = pd.read_csv('/content/subs.csv', squeeze=True)\nsubs\n``` | Imports a single-column CSV dataset (`subs.csv`) and coerces it into a 1D Pandas Series. |
| **Read Multi-Column CSV with Index** | ```python\nvk = pd.read_csv('/content/kohli_ipl.csv', index_col='match_no', squeeze=True)\nvk\n``` | Loads `kohli_ipl.csv`, sets the `match_no` column as the index (row labels), and squeezes the remaining column into a Series representing Kohli's match runs. |
| **Read Text-indexed CSV** | ```python\nmovies = pd.read_csv('/content/bollywood.csv', index_col='movie', squeeze=True)\nmovies\n``` | Loads a dataset of movies and lead actors. It registers the movie title as the primary index and the actor as the Series values. |

---

## 🔍 5. Inspecting & Ordering Data

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Inspect Top & Bottom (`.head()` / `.tail()`)** | ```python\nsubs.head()\nvk.head(3)\nvk.tail(10)\n``` | `.head(n)` retrieves the first `n` elements (defaults to 5) and `.tail(n)` retrieves the last `n` elements. Excellent for quick data verification. |
| **Random Sampling (`.sample()`)** | ```python\nmovies.sample(5)\n``` | Generates a randomized sample of `n` rows. Extremely helpful for getting unbiased previews of data distributions. |
| **Frequency Counts (`.value_counts()`)** | ```python\nmovies.value_counts()\n``` | Aggregates data by unique values, returning a new Series containing unique items and their respective frequency counts sorted in descending order. |
| **Sorting by Values** | ```python\nvk.sort_values(ascending=False).head(1).values[0]\nvk.sort_values(ascending=False)\nvk.sort_values(inplace=True)\n``` | Sorts values. `ascending=False` sorts high-to-low. Chaining `.head(1).values[0]` returns the single maximum value. `inplace=True` modifies the source Series. |
| **Sorting by Index** | ```python\nmovies.sort_index(ascending=False, inplace=True)\nmovies\n``` | Re-orders the dataset alphabetically/numerically based on its **index labels** (e.g., sorting movies from Z to A in-place). |

---

## 📊 6. Summary Statistics & Maths

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Count Non-Null Elements (`.count()`)** | ```python\nvk.count()\n``` | Calculates and returns the number of non-missing (non-NaN) records. Size counts everything; count ignores null values. |
| **Summation (`.sum()`)** | ```python\nsubs.sum()\n``` | Computes the mathematical sum of all numeric values across the Series. |
| **Statistical Metrics** | ```python\nsubs.mean()\nprint(vk.median())\nprint(movies.mode())\nprint(subs.std())\nprint(vk.var())\n``` | Computes essential mathematical markers: **mean** (average), **median** (mid-point), **mode** (most frequent values), **standard deviation** (dispersion), and **variance**. |
| **Extrema Values (`.min()` / `.max()`)** | ```python\nsubs.max()\n``` | Extracts the lowest or highest value stored inside the Series. |
| **Descriptive Summary (`.describe()`)** | ```python\nsubs.describe()\n``` | Returns a consolidated summary of standard statistical metrics (count, mean, std, min, max, 25%, 50%, and 75% percentiles). |

---

## 🎯 7. Advanced Indexing & Slicing

> [!WARNING]
> Integer-indexed Series do **not** support negative indexing (`-1`) directly through standard brackets because it causes ambiguity with potential labels. Labeled index Series, however, support negative indexing natively.

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Integer-based Index Access** | ```python\nx = pd.Series([12, 13, 14, 35, 46, 57, 58, 79, 9])\nx\n``` | Allocates values to standard integer index positions. |
| **Negative Indexing** | ```python\nx[-1]          # Error (IntIndex)\nvk[-1]         # Error (IntIndex)\nmarks_series[-1] # Works (LabelIndex)\n``` | Demonstrates positional boundary lookup behavior. Labeled indices allow negative indexing to lookup from the tail, while integer indices raise key errors. |
| **Positional Slicing** | ```python\nvk[5:16]\nvk[-5:]\nmovies[::2]\n``` | Extracts a range of values using `[start:stop:step]` positional coordinates. Slicing with numbers is non-inclusive of the end boundary. |
| **Fancy Indexing** | ```python\nvk[[1, 3, 4, 5]]\n``` | Extracts multiple disjoint index keys or coordinate values simultaneously by wrapping them in a nested Python list. |
| **Label-based Lookup** | ```python\nmovies['2 States (2014 film)']\n``` | Directly queries and fetches the values corresponding to a custom string or datetime index key (acts like a constant-time hash map lookup). |

---

## ✏️ 8. Modifying & Editing Series

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **In-place Value Update** | ```python\nmarks_series[1] = 100\nmarks_series\n``` | Overwrites the value at a specific index location. |
| **Dynamic Index Appending** | ```python\nmarks_series['evs'] = 100\nmarks_series\n``` | Assigning a value to an index label that does not exist in the Series automatically appends that key-value pair to the end. |
| **Bulk Slice Modification** | ```python\nruns_ser[2:4] = [100, 100]\nruns_ser\n``` | Updates a continuous range of elements using slicing techniques. |
| **Fancy Index Modification** | ```python\nruns_ser[[0, 3, 4]] = [0, 0, 0]\nruns_ser\n``` | Replaces several scattered indices with a corresponding set of new values in a single line. |
| **Label-based Modification** | ```python\nmovies['2 States (2014 film)'] = 'Alia Bhatt'\nmovies\n``` | Identifies the record with the matching text index and alters its value directly. |

---

## 🐍 9. Python Integration & Built-in Interoperability

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Standard Python Built-ins** | ```python\nprint(len(subs))\nprint(type(subs))\nprint(dir(subs))\nprint(sorted(subs))\nprint(min(subs))\nprint(max(subs))\n``` | Proves seamless interoperability with standard Python primitives: `len()` for length, `type()` for structure verification, `dir()` for attribute maps, `sorted()` for custom lists, and `min`/`max`. |
| **Type Coercion** | ```python\nlist(marks_series)\ndict(marks_series)\n``` | Casts a Pandas Series directly into standard Python **lists** or nested **dictionaries** for downstream processing. |
| **Membership Testing (`in` operator)** | ```python\n'2 States (2014 film)' in movies\n'Alia Bhatt' in movies.values\n``` | Testing `key in Series` checks the **Index**. To test if a value is contained within the Series elements, perform the check on `.values`. |
| **Looping & Iterating** | ```python\nfor i in movies.index:\n  print(i)\n``` | Custom iteration. Iterating over `.index` loops through keys, while iterating directly over the Series yields values. |

---

## ⚡ 10. Vectorized Math (Broadcasting) & Relational Masks

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Scalar Arithmetic Broadcasting** | ```python\n100 + marks_series\n``` | Applies mathematical operations element-wise to every single element in the Series in a vectorized fashion without needing loops. |
| **Relational Comparison Masks** | ```python\nvk >= 50\n``` | Performs logical comparison on each element, returning a Series of identical shape populated with `True`/`False` boolean answers. |

---

## 🧹 11. Boolean Indexing & Advanced Filtering

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Logical Condition Filtering** | ```python\nvk[vk >= 50].size\nvk[vk == 0].size\nsubs[subs > 200].size\n``` | Passes a boolean comparison mask into the Series brackets `[]`. This filters and retains only the elements that satisfy the logical criteria. |
| **Frequency Threshold Filtering** | ```python\nnum_movies = movies.value_counts()\nnum_movies[num_movies > 20]\n``` | Computes category frequencies and applies boolean indexing on the frequencies to filter categories appearing more than 20 times. |

---

## 📈 12. Integrated Plotting & Visualization

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Line Plots** | ```python\nsubs.plot()\n``` | Generates a standard sequential line chart plotting Series values over the index sequence utilizing Matplotlib. |
| **Pie Charts** | ```python\nmovies.value_counts().head(20).plot(kind='pie')\n``` | Creates an illustrative pie chart mapping value distributions for categorical columns (e.g., top 20 actors and their movie market share). |

---

## 💎 13. Powerful Advanced Methods

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Memory Cast & Optimization (`.astype()`)** | ```python\nimport sys\nsys.getsizeof(vk)\nsys.getsizeof(vk.astype('int16'))\n``` | Downcasts numerical representations (e.g., `int64` to `int16`) to drastically reduce memory footprints. |
| **Range Intersect Filtering (`.between()`)** | ```python\nvk[vk.between(51, 99)].size\n``` | Returns a boolean mask highlighting elements that fall within the closed numerical interval `[min, max]`. |
| **Boundary Clamping (`.clip()`)** | ```python\nsubs.clip(100, 200)\n``` | Caps numerical outliers. Values lower than the lower boundary are set to `100`; values exceeding the upper boundary are set to `200`. |
| **Duplicate Elimination (`.drop_duplicates()`)** | ```python\ntemp = pd.Series([1,1,2,2,3,3,4,4])\ntemp.drop_duplicates(keep='last')\nmovies.drop_duplicates()\n``` | Drops repeated occurrences. `keep='last'` retains the final instance of duplicates; `keep='first'` keeps the initial one. |
| **Duplicate Checking (`.duplicated()`)** | ```python\ntemp.duplicated().sum()\nvk.duplicated().sum()\n``` | Flags repeats with a boolean index. Summing the result counts total duplicate occurrences. |
| **Null Value Identification (`.isnull()`)** | ```python\ntemp = pd.Series([1,2,3,np.nan,5,6,np.nan,8,np.nan,10])\ntemp.isnull().sum()\n``` | Produces a boolean mask detecting missing (`NaN`) values. Chaining `.sum()` tallies the total missing inputs. |
| **Null Row Elimination (`.dropna()`)** | ```python\ntemp.dropna()\n``` | Filters and discards any record containing a missing/null (`NaN`) entry, returning a clean Series. |
| **Null Replacement (`.fillna()`)** | ```python\ntemp.fillna(temp.mean())\n``` | Substitutes missing (`NaN`) entries with a fallback value (such as the overall mathematical mean). |
| **Set Containment Lookup (`.isin()`)** | ```python\nvk[(vk == 49) | (vk == 99)]\nvk[vk.isin([49,99])]\n``` | Tests if elements match entries in a provided list. Provides a cleaner, faster alternative to multiple logical OR operators. |
| **Element-wise Mapping (`.apply()`)** | ```python\nmovies.apply(lambda x: x.split()[0].upper())\nsubs.apply(lambda x: 'good day' if x > subs.mean() else 'bad day')\n``` | Executes custom element-wise transforms. Maps string manipulations or logical conditions across all rows in a highly parallelized manner. |
| **Shallow vs Deep Copy (`.copy()`)** | ```python\nnew = vk.head()\nnew[1] = 1 # Warning: modifies vk!\nnew = vk.head().copy()\nnew[1] = 100 # Safe\n``` | Custom copying. Standard slices return logical views where edits propagate to the original Series. `.copy()` clones a deep independent replica. |

---

> [!TIP]
> Keep this document handy when practicing Pandas. To test any of the methods, execute the corresponding block in your interactive notebook `pandasfirst.ipynb`.
