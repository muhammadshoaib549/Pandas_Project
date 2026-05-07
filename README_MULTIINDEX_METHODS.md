# 🗂️ Pandas MultiIndexing, Reshaping & Pivoting: Master Reference Guide

Welcome to the **Pandas MultiIndexing, Reshaping & Pivoting Master Reference Guide**! This comprehensive document maps all the concepts from your interactive notebook **[season21t.ipynb](file:///home/shoaib/Desktop/Pandas_Project/season21t.ipynb)** into an educational, premium reference tool.

> [!NOTE]
> This guide is structured in your preferred three-column table format: **Concept Name**, **Code**, and **Detailed Explanation**. All existing README files are left completely untouched!

---

## 🗺️ 1. MultiIndex Creation & Structural Setup

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Hierarchical Indexing from Tuples** | ```python\nindex_val = [('cse', 2019), ('cse', 2020), ...]\nmultiindex = pd.MultiIndex.from_tuples(index_val)\n``` | Generates a multi-layered structure of unique indexes from a list of tuple pairs, creating parent-child relationships. |
| **MultiIndex Cartesian Product** | ```python\npd.MultiIndex.from_product([\n  ['cse', 'ece'], \n  [2019, 2020, 2021, 2022]\n])\n``` | Automatically generates a MultiIndex mapping every combination of elements from list inputs using Cartesian products. |
| **Extracting MultiIndex Levels** | ```python\nmultiindex.levels[1]\n``` | Accesses and returns a list of unique labels present inside a specific coordinate level of the MultiIndex. |
| **MultiIndex Series Definition** | ```python\ns = pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=multiindex)\n``` | Attaches the multi-layered index structure to a Series, establishing multi-layered row coordinates. |
| **Slicing MultiIndex Series** | ```python\ns['cse']\n``` | Extracts and returns all data points belonging to the specified outer-level index label as a sub-Series. |

---

## 🔄 2. Stacking, Unstacking & MultiIndex DataFrames

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Unstacking Series (`.unstack()`)** | ```python\ntemp = s.unstack()\n``` | Transforms a 1D MultiIndex Series into a 2D DataFrame by converting the inner index level into column headers. |
| **Stacking DataFrames (`.stack()`)** | ```python\ntemp.stack()\n``` | Compresses column headers into an inner row index level, converting a 2D DataFrame back into a 1D MultiIndex Series. |
| **MultiIndex DataFrame (Rows)** | ```python\nbranch_df1 = pd.DataFrame(\n  [[1, 2], [3, 4], ...], \n  index=multiindex, \n  columns=['avg_package', 'students']\n)\n``` | Constructs a DataFrame containing multi-layered indexing labels across its rows while columns remain simple. |
| **MultiIndex DataFrame (Columns)** | ```python\nbranch_df2 = pd.DataFrame(\n  [[1, 2, 0, 0], ...], \n  index=[2019, 2020, 2021, 2022], \n  columns=pd.MultiIndex.from_product([\n    ['delhi', 'mumbai'], \n    ['avg_package', 'students']\n  ])\n)\n``` | Constructs a DataFrame where rows have a simple flat index, but column coordinates are multi-layered (e.g. Cities -> Metrics). |
| **Fully Hierarchical DataFrame** | ```python\nbranch_df3 = pd.DataFrame(\n  [[1, 2, 0, 0], ...], \n  index=multiindex, \n  columns=pd.MultiIndex.from_product([\n    ['delhi', 'mumbai'], \n    ['avg_package', 'students']\n  ])\n)\n``` | Constructs a complex DataFrame containing multi-layered dimensions across both index levels and column labels. |
| **Double Stacking** | ```python\nbranch_df3.stack().stack()\n``` | Stacks both levels of columns sequentially into the row index, condensing a 2D DataFrame into a single multi-layered Series. |

---

## 🔎 3. MultiIndex Navigation, Slicing & Axis Operations

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Extracting Single MultiIndex Row** | ```python\nbranch_df3.loc[('cse', 2022)]\n``` | Locates and extracts columns for a specific row using a coordinate tuple mapping `(outer_row, inner_row)`. |
| **Slicing Multiple Rows** | ```python\nbranch_df3.loc[('cse', 2019):('ece', 2020):2]\n``` | Slices rows step-wise from one specific multi-index tuple coordinate to another, matching step bounds. |
| **Positional DataFrame Slicing** | ```python\nbranch_df3.iloc[0:5:2]\n``` | Selects rows positionally, ignoring index names to extract rows between index integer offsets. |
| **Accessing Nested Columns** | ```python\nbranch_df3['delhi']['students']\n``` | Traverses multi-level columns by indexing outer labels first, followed by inner column coordinates. |
| **Positional Column Extraction** | ```python\nbranch_df3.iloc[:, 1:3]\n``` | Slices columns positionally, retrieving all rows for column integer indexes 1 and 2. |
| **Cross-Section Selection** | ```python\nbranch_df3.iloc[[0, 4], [1, 2]]\n``` | Extracts specific row-column intersections positionally. |
| **Multi-Level Index Sorting** | ```python\nbranch_df3.sort_index(ascending=False)\nbranch_df3.sort_index(ascending=[False, True])\n``` | Sorts index levels. Can sort all descending, or specify different sorting orders for each level using lists. |
| **Targeted Level Sorting** | ```python\nbranch_df3.sort_index(level=0, ascending=False)\n``` | Sorts row indices based on a single target level (e.g., Level `0`), leaving other index levels unsorted. |
| **DataFrame Transposition** | ```python\nbranch_df3.transpose()\n``` | Rotates the DataFrame axis, swapping row indexes with column headers. |
| **Index Level Swapping** | ```python\nbranch_df3.swaplevel(axis=1)\n``` | Interchanges the positions of inner and outer levels in a multi-index along a specified axis. |

---

## 🧼 4. Wide-to-Long Reshaping (`.melt()`)

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Simple Wide-to-Long Melts** | ```python\npd.DataFrame({'cse': [120]}).melt()\n``` | Melts a wide DataFrame into long-format containing two flat columns: `variable` and `value`. |
| **Melting with Named Columns** | ```python\ndf.melt(\n  var_name='branch', \n  value_name='num_students'\n)\n``` | Unpivots columns into custom-named `var_name` and `value_name` category columns. |
| **Multi-Identifier Melting** | ```python\ndf.melt(\n  id_vars=['branch'], \n  var_name='year', \n  value_name='students'\n)\n``` | Unpivots multiple column fields while preserving selected identifier columns (`id_vars`) as repeated row descriptors. |
| **COVID-19 Sifting & Merging** | ```python\ndeath = death.melt(\n  id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], \n  var_name='date', \n  value_name='num_deaths'\n)\n``` | Melts wide daily logs into tidy, vertical time-series tables, allowing DataFrames to be merged on composite keys. |

---

## 📈 5. Pivot Tables & Visualization

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Groupby Un-pivoting Alternative** | ```python\ndf.groupby(['sex', 'smoker'])[['total_bill']].mean().unstack()\n``` | Groups data by multiple columns and unstacks the inner index, generating a multi-dimensional table manually. |
| **Standard Pivot Table** | ```python\ndf.pivot_table(\n  index='sex', \n  columns='smoker', \n  values='total_bill'\n)\n``` | Dynamically aggregates a target column across two categoric axes, defaulting to mean values. |
| **Pivot with Custom Functions** | ```python\ndf.pivot_table(\n  index='sex', \n  columns='smoker', \n  values='total_bill', \n  aggfunc='std'\n)\n``` | Computes custom statistics (e.g., standard deviation `std`, `sum`, `max`) across the pivoted groups. |
| **Multi-Aggregation Pivoting** | ```python\ndf.pivot_table(\n  index=['sex', 'smoker'], \n  columns=['day', 'time'], \n  aggfunc={\n    'size': 'mean', \n    'tip': 'max', \n    'total_bill': 'sum'\n  }, \n  margins=True\n)\n``` | Performs different aggregation functions across multiple hierarchical row and column indices. |
| **Pivot Table Margins** | ```python\ndf.pivot_table(\n  index='sex', \n  columns='smoker', \n  values='total_bill', \n  aggfunc='sum', \n  margins=True\n)\n``` | Calculates row and column sub-totals and grand totals, returning them in a `'All'` margins row/column. |
| **Pivoted Expense Visualizations** | ```python\ndf.pivot_table(\n  index='month', \n  columns='Category', \n  values='INR', \n  aggfunc='sum', \n  fill_value=0\n).plot()\n``` | Pivots expense records, fills empty fields with 0, and plots a multi-series line chart of monthly expense categories. |

---

> [!TIP]
> Keep this lookup guide open when working on your database navigation assignments inside **[season21t.ipynb](file:///home/shoaib/Desktop/Pandas_Project/season21t.ipynb)**!
