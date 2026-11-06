# Data Visualization with Seaborn in Python

## Overview

Seaborn is a Python data visualization library built on top of Matplotlib that provides a high-level interface for creating attractive, informative statistical graphics. It integrates well with Pandas DataFrames and simplifies complex visualizations.

---

## Installation & Setup

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Optional: Set style and context
sns.set_style("darkgrid")  # or "whitegrid", "dark", "white", "ticks"
sns.set_context("notebook")  # or "paper", "talk", "poster"
```

---

## Core Concepts

### Aesthetics
- **Hue**: Color encoding (typically categorical)
- **Size**: Marker size encoding (typically continuous)
- **Style**: Marker style or line style
- **Palette**: Color scheme (categorical, sequential, diverging)

### Figure-level vs Axes-level
- **Axes-level**: Draw on a single matplotlib axis (faster, simpler)
- **Figure-level**: Manage figure creation and subplot arrangement (more flexible for multi-plot grids)

---

## Essential Plot Types

### 1. **Scatter Plot** (Axes-level)
```python
sns.scatterplot(data=df, x='column1', y='column2', hue='category', size='value', palette='Set2')
plt.show()
```
- Best for: Bivariate relationships
- Parameters: `x`, `y`, `hue`, `size`, `style`, `data`, `palette`

### 2. **Line Plot** (Axes-level)
```python
sns.lineplot(data=df, x='time', y='value', hue='group', style='type')
plt.show()
```
- Best for: Trends over time or continuous variables
- Automatically aggregates multiple observations

### 3. **Distribution Plot** (Figure-level)
```python
sns.displot(data=df, x='column', kde=True, bins=30, hue='category')
plt.show()
```
- Best for: Single variable distribution
- Combines histogram and KDE (kernel density estimate)

### 4. **Histogram** (Axes-level)
```python
sns.histplot(data=df, x='column', bins=25, kde=True, hue='category')
plt.show()
```
- Best for: Frequency distribution
- Faster for large datasets than displot

### 5. **Box Plot**
```python
sns.boxplot(data=df, x='category', y='value', hue='group', palette='Set2')
plt.show()
```
- Best for: Comparing distributions across categories
- Shows median, quartiles, and outliers

### 6. **Violin Plot**
```python
sns.violinplot(data=df, x='category', y='value', hue='group', split=True)
plt.show()
```
- Best for: Distribution shape across categories
- Combines box plot and KDE

### 7. **Bar Plot**
```python
sns.barplot(data=df, x='category', y='value', hue='group', palette='husl', ci=95)
plt.show()
```
- Best for: Categorical comparisons with confidence intervals
- Default aggregation: mean

### 8. **Count Plot**
```python
sns.countplot(data=df, x='category', hue='subcategory', palette='Set3')
plt.show()
```
- Best for: Categorical frequencies
- Automatically counts occurrences

### 9. **Heat Map**
```python
# Correlation matrix
corr = df.corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', cbar_kws={'label': 'Correlation'})
plt.show()
```
- Best for: 2D matrix data, correlations
- Parameters: `annot` (show values), `fmt` (number format), `cmap` (colormap)

### 10. **Pair Plot** (Figure-level)
```python
sns.pairplot(data=df, hue='category', diag_kind='kde', plot_kws={'alpha': 0.6})
plt.show()
```
- Best for: Exploring relationships between all variables
- Creates a matrix of plots

### 11. **Joint Plot** (Figure-level)
```python
sns.jointplot(data=df, x='column1', y='column2', kind='hex', height=6)
plt.show()
```
- Best for: Bivariate + marginal distributions
- Kinds: `scatter`, `kde`, `hist`, `hex`, `reg`, `resid`

### 12. **Regression Plot**
```python
sns.regplot(data=df, x='x', y='y')  # Axes-level
sns.lmplot(data=df, x='x', y='y', hue='group')  # Figure-level with groups
plt.show()
```
- Best for: Showing linear regression with confidence interval

### 13. **Categorical Plot** (Figure-level)
```python
sns.catplot(data=df, x='category', y='value', kind='box', hue='group', col='facet_var', height=4)
plt.show()
```
- Wrapper for multiple categorical plot types
- Supports faceting with `col` and `row`

---

## Customization & Styling

### Color Palettes
```python
# View available palettes
sns.color_palette()
sns.color_palette("husl", 8)

# Named palettes: "Set1", "Set2", "Set3", "husl", "coolwarm", "RdBu", "Pastel1", etc.

# Custom palette
custom_palette = ["#FF6B6B", "#4ECDC4", "#45B7D1"]
sns.set_palette(custom_palette)
```

### Figure Styling
```python
# Pre-defined styles
sns.set_style("whitegrid")  # Clean background with grid
sns.set_context("talk")      # Larger elements for presentations

# Context options: "paper" (small), "notebook" (default), "talk" (large), "poster" (largest)
```

### Manual Customization
```python
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='col1', y='col2', ax=ax, s=100, alpha=0.6)
ax.set_title('My Plot', fontsize=16, fontweight='bold')
ax.set_xlabel('X Axis', fontsize=12)
ax.set_ylabel('Y Axis', fontsize=12)
plt.tight_layout()
plt.show()
```

---

## Advanced Techniques

### Faceting with Multiple Subplots
```python
sns.catplot(data=df, x='x', y='y', col='col_facet', row='row_facet', kind='box')
plt.show()
```

### Combining Plots
```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(data=df, x='col1', ax=axes[0], kde=True)
sns.boxplot(data=df, x='col2', ax=axes[1])
plt.tight_layout()
plt.show()
```

### Handling Missing Data
```python
# Seaborn handles NaN values gracefully by default
# Use dropna in catplot to exclude missing values
sns.catplot(data=df.dropna(), x='x', y='y')
```

### Size and Scale
```python
fig, ax = plt.subplots(figsize=(12, 8))
sns.set_context("poster", font_scale=1.2)  # Adjust element sizes
sns.scatterplot(data=df, x='x', y='y', ax=ax, s=200)  # s = marker size
```

---

## Practical Example

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load example dataset
tips = sns.load_dataset("tips")

# Create a comprehensive visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Scatter plot with regression
sns.regplot(data=tips, x='total_bill', y='tip', ax=axes[0, 0])
axes[0, 0].set_title('Bill vs Tip (with Regression)')

# 2. Box plot by day
sns.boxplot(data=tips, x='day', y='total_bill', hue='sex', ax=axes[0, 1], palette='Set2')
axes[0, 1].set_title('Bill by Day and Gender')

# 3. Count plot
sns.countplot(data=tips, x='day', hue='sex', ax=axes[1, 0], palette='husl')
axes[1, 0].set_title('Number of Customers by Day')

# 4. Violin plot
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex', ax=axes[1, 1], split=True)
axes[1, 1].set_title('Bill Distribution by Day and Gender')

plt.tight_layout()
plt.show()
```

---

## Common Parameters Reference

| Parameter | Use | Example |
|-----------|-----|---------|
| `data` | DataFrame source | `data=df` |
| `x`, `y` | Column names for axes | `x='time', y='value'` |
| `hue` | Color by category | `hue='group'` |
| `size` | Marker size by value | `size='importance'` |
| `style` | Marker/line style | `style='type'` |
| `palette` | Color scheme | `palette='Set1'` |
| `ax` | Matplotlib axis | `ax=axes[0]` |
| `figsize` | Figure dimensions | `figsize=(10, 6)` |
| `kde` | Add density curve | `kde=True` |
| `ci` | Confidence interval | `ci=95` |
| `hue_order` | Category order | `hue_order=['A', 'B', 'C']` |

---

## Tips & Best Practices

1. **Always inspect data first** — Use `df.head()`, `df.info()`, `df.describe()`
2. **Choose appropriate plot types** — Match visualization to data type and question
3. **Use meaningful titles and labels** — Make plots self-explanatory
4. **Consider color-blind friendly palettes** — "Set2", "husl", or "colorblind"
5. **Avoid over-plotting** — Use transparency (`alpha`), faceting, or aggregation
6. **Save figures properly** — `plt.savefig('plot.png', dpi=300, bbox_inches='tight')`
7. **Clean data before plotting** — Handle missing values and outliers appropriately

---

This should give you a solid foundation for data visualization with Seaborn!