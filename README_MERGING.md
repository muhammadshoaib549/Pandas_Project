# 🤝 Pandas Concatenation & Merging: Master Reference Guide

Welcome to the **Pandas Concatenation & Merging Master Reference Guide**! This comprehensive document maps all the advanced multi-table data alignment, unioning, joining, and business-intelligence case study operations from your interactive notebook **[season20.ipynb](file:///home/shoaib/Desktop/Pandas_Project/season20.ipynb)**.

> [!NOTE]
> This guide is structured in a clean, professional three-column table format: **Concept Name**, **Code**, and **Detailed Explanation**. All existing README files are left completely untouched.

---

## 🏗️ 1. Concatenation & Appending (Unions)

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Standard Vertical Concatenation** | ```python\nregs = pd.concat([nov, dec], ignore_index=True)\nregs\n``` | Row-wise appends two DataFrames. Setting `ignore_index=True` resets the row labels into a continuous sequential range index. |
| **Vertical Appending** | ```python\nnov.append(dec, ignore_index=True)\n``` | Appends DataFrame rows vertically. *Warning: `.append` is deprecated in newer Pandas versions; always prefer `pd.concat`.* |
| **Hierarchical MultiIndex Keys** | ```python\nmulti = pd.concat([nov, dec], keys=['Nov', 'Dec'])\nmulti.loc[('Dec', 4)]\n``` | Concatenates while preserving the source identity of rows by creating a MultiIndex index. Rows can be queried using nested key tuples. |
| **Horizontal Concatenation** | ```python\npd.concat([nov, dec], axis=1)\n``` | Combines DataFrames side-by-side along column indices (`axis=1`). Aligns rows by matching index numbers. |

---

## 🔗 2. Joining Data (Merge Joins)

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Inner Join Merge** | ```python\nstudents.merge(regs, how='inner', on='student_id')\n``` | Finds and returns rows where keys match in **both** DataFrames. Rows with unmatched `student_id` are excluded. |
| **Left Outer Join Merge** | ```python\ncourses.merge(regs, how='left', on='course_id')\n``` | Keeps all records from the left DataFrame (`courses`), appending matching data from the right. Unmatched keys get filled with `NaN`. |
| **Right Outer Join Merge** | ```python\nstudents.merge(regs, how='right', on='student_id')\n``` | Keeps all records from the right DataFrame (`regs`), appending matching data from the left. Unmatched keys are filled with `NaN`. |
| **Full Outer Join Merge** | ```python\nstudents.merge(regs, how='outer', on='student_id').tail(10)\n``` | Returns **all records** from both DataFrames, aligning matching keys and filling missing mappings with `NaN`. |
| **Alternative Merge Syntax** | ```python\npd.merge(students, regs, how='inner', on='student_id')\n``` | Functional syntax alternative. Equivalent to calling the `.merge()` method on individual DataFrame objects. |

---

## 📊 3. Analytical Cases & Set Operations

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **1. Total Revenue** | ```python\nregs.merge(courses, how='inner', on='course_id')['price'].sum()\n``` | Merges registrations and courses, then sums the price column to find total sales revenue. |
| **2. Monthly Revenue** | ```python\ntemp_df = pd.concat([nov, dec], keys=['Nov', 'Dec']).reset_index()\ntemp_df.merge(courses, on='course_id').groupby('level_0')['price'].sum()\n``` | Groups rows by the MultiIndex source label (`'level_0'`) and aggregates prices to show monthly sales trends. |
| **3. Registration Lookup** | ```python\nregs.merge(students, on='student_id').merge(courses, on='course_id')[['name', 'course_name', 'price']]\n``` | Chains multiple merge operations to map student names, enrolled course names, and prices into a single list. |
| **4. Revenue Bar Chart** | ```python\nregs.merge(courses, on='course_id').groupby('course_name')['price'].sum().plot(kind='bar')\n``` | Groups total revenue by course name and generates an illustrative bar chart representing sales performance. |
| **5. Intersection (Both Months)** | ```python\ncommon_student_id = np.intersect1d(nov['student_id'], dec['student_id'])\nstudents[students['student_id'].isin(common_student_id)]\n``` | Uses NumPy's `np.intersect1d` to find student IDs that appear in both datasets, then filters the student directory. |
| **6. Set Difference (No Enrolls)** | ```python\ncourse_id_list = np.setdiff1d(courses['course_id'], regs['course_id'])\ncourses[courses['course_id'].isin(course_id_list)]\n``` | Uses `np.setdiff1d` to isolate course IDs that have zero active registrations in the enrollment database. |
| **7. Total Non-Enrolled Students** | ```python\nstudent_id_list = np.setdiff1d(students['student_id'], regs['student_id'])\nstudents[students['student_id'].isin(student_id_list)].shape[0]\n``` | Isolates and counts student directory records that do not map to any enrollment records. |
| **8. Self-Join Relationships** | ```python\nstudents.merge(students, how='inner', left_on='partner', right_on='student_id')[['name_x', 'name_y']]\n``` | Merges a DataFrame with itself to map relationships. Here, it maps students (`name_x`) to their learning partners (`name_y`). |
| **9. Most Active Students** | ```python\nregs.merge(students, on='student_id').groupby(['student_id', 'name'])['name'].count().sort_values(ascending=False).head(3)\n``` | Groups registrations by student details, counts course sign-ups, and returns the top 3 most active students. |
| **10. Top Spending Students** | ```python\nregs.merge(students, on='student_id').merge(courses, on='course_id').groupby(['student_id', 'name'])['price'].sum().sort_values(ascending=False).head(3)\n``` | Chains merges, groups by student details, and sums prices to identify the top 3 highest-spending customers. |

---

## 🏏 4. IPL Advanced Metrics Case Study

| Concept Name | Code | Explanation |
| :--- | :--- | :--- |
| **Cross-Table Match Join** | ```python\ntemp_df = delivery.merge(matches, left_on='match_id', right_on='id')\n``` | Joins the ball-by-ball delivery log with the match info table, mapping match properties (season, city, venue) to individual deliveries. |
| **Stadium Sixes Ratio** | ```python\nsix_df = temp_df[temp_df['batsman_runs'] == 6]\nnum_sixes = six_df.groupby('venue')['venue'].count()\nnum_matches = matches['venue'].value_counts()\n(num_sixes / num_matches).sort_values(ascending=False).head(10)\n``` | Filters sixes, counts total sixes hit at each venue, divides by total matches played at each stadium, and sorts to find high-ratio grounds. |
| **Orange Cap Winners by Season** | ```python\ntemp_df.groupby(['season', 'batsman'])['batsman_runs'].sum().reset_index().sort_values('batsman_runs', ascending=False).drop_duplicates(subset=['season'], keep='first').sort_values('season')\n``` | Sums runs scored by each batter per season, sorts descending, drops duplicates keeping the highest scorer per season, and orders by year. |

---

> [!TIP]
> Keep this lookup guide open when working on your database manipulation assignments inside **[season20.ipynb](file:///home/shoaib/Desktop/Pandas_Project/season20.ipynb)**!
