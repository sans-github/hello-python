import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timedelta


def generate_transactions_dataset(n_rows=1000, output_path="data/data_matplotlib.csv"):
    """
    Generate a synthetic transactions dataset optimized for learning matplotlib.
    Includes multiple data types and relationships to support all learning objectives.
    """
    np.random.seed(42)

    # Date range for temporal analysis
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(n_rows)]

    # Categories for grouping and comparison
    categories = ["Electronics", "Clothing", "Food", "Books", "Home"]
    regions = ["North", "South", "East", "West"]
    payment_methods = ["Credit Card", "Debit Card", "Cash", "PayPal"]

    # Generate correlated data for meaningful visualizations
    data = {
        "date": dates,
        "transaction_id": [f"TXN{str(i).zfill(6)}" for i in range(1, n_rows + 1)],
        # Numeric columns with different distributions
        "amount": np.random.lognormal(4, 1, n_rows).round(2),  # Right-skewed
        "quantity": np.random.poisson(3, n_rows),  # Count data
        "discount_percent": np.random.beta(2, 5, n_rows) * 100,  # 0-100 range
        # Categorical columns for grouping
        "category": np.random.choice(categories, n_rows, p=[0.3, 0.25, 0.2, 0.15, 0.1]),
        "region": np.random.choice(regions, n_rows),
        "payment_method": np.random.choice(payment_methods, n_rows),
        # Binary/boolean for filtering
        "is_member": np.random.choice([True, False], n_rows, p=[0.6, 0.4]),
        "is_online": np.random.choice([True, False], n_rows, p=[0.7, 0.3]),
    }

    df = pd.DataFrame(data)

    # Add derived columns
    df["revenue"] = (
        df["amount"] * df["quantity"] * (1 - df["discount_percent"] / 100)
    ).round(2)
    df["month"] = pd.to_datetime(df["date"]).dt.to_period("M").astype(str)
    df["day_of_week"] = pd.to_datetime(df["date"]).dt.day_name()
    df["quarter"] = pd.to_datetime(df["date"]).dt.quarter

    # Add some seasonal patterns
    df["season_factor"] = df["date"].apply(
        lambda x: 1.3 if x.month in [11, 12] else 1.0
    )
    df["revenue"] = (df["revenue"] * df["season_factor"]).round(2)
    df = df.drop("season_factor", axis=1)

    # Add ratings for scatter plots
    df["customer_rating"] = np.random.normal(4.0, 0.8, n_rows).clip(1, 5).round(1)

    # Add some correlation between amount and rating
    df.loc[df["amount"] > df["amount"].quantile(0.75), "customer_rating"] += 0.3
    df["customer_rating"] = df["customer_rating"].clip(1, 5).round(1)

    # Ensure output directory exists
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Save to CSV
    df.to_csv(output_file, index=False)

    print(f"Dataset generated: {n_rows} rows")
    print(f"Saved to: {output_file.absolute()}")
    print(f"\nColumns: {', '.join(df.columns)}")
    print("\nFirst few rows:")
    print(df.head())
    print("\nData types:")
    print(df.dtypes)
    print("\nBasic stats:")
    print(df.describe())

    return df


def generate_learning_notes():
    """
    Generate a text file explaining what each column is good for learning.
    """
    notes = """
MATPLOTLIB LEARNING DATASET - COLUMN GUIDE
==========================================

This dataset is designed to teach matplotlib progressively. Here's what each column enables:

TEMPORAL ANALYSIS:
- date: Line plots over time, time series
- month: Grouped bar charts by month
- quarter: Seasonal comparisons
- day_of_week: Weekly patterns

NUMERIC DISTRIBUTIONS:
- amount: Histograms, distribution plots
- quantity: Count-based plots
- discount_percent: Percentage-based visualizations
- revenue: Primary metric for most plots
- customer_rating: Scatter plot correlations

CATEGORICAL GROUPING:
- category: Group by product type (5 categories)
- region: Geographic comparisons (4 regions)
- payment_method: Payment type analysis (4 methods)

BINARY FILTERS:
- is_member: Compare member vs non-member
- is_online: Online vs offline transactions

LEARNING PATH MAPPING:
======================

1. SINGLE PLOT, SINGLE VARIABLE:
   - Line: revenue over date
   - Bar: total revenue by category
   - Histogram: distribution of amount

2. BASIC CUSTOMIZATION:
   - Use any of the above with titles, labels, colors

3. MULTIPLE ELEMENTS, SAME PLOT:
   - Multiple lines: revenue by region over time
   - Multiple bars: revenue by category for each quarter
   - Overlayed histograms: amount distribution by is_member

4. DIFFERENT PLOT TYPES:
   - Combine line (revenue over time) + bar (by category) + scatter (amount vs rating)

5. GROUPED CATEGORICAL:
   - One line per region showing revenue over time
   - Grouped bars: category revenue by payment_method
   - Stacked bars: category breakdown by region

6. SUBPLOTS:
   - Grid of plots: one per region or category
   - Shared axes: compare regions with aligned scales

7. STYLING:
   - Add legends for multiple lines/bars
   - Rotate x-axis labels for date/category
   - Annotate maximum values

8. FIGURE CONTROL:
   - Multiple axes: main revenue + quantity subplot
   - Twin axes: revenue and customer_rating on same plot

9. OUTPUT:
   - Save any plot to PNG
"""

    notes_path = Path("data/LEARNING_GUIDE.txt")
    notes_path.parent.mkdir(parents=True, exist_ok=True)

    with open(notes_path, "w") as f:
        f.write(notes)

    print(f"\nLearning guide saved to: {notes_path.absolute()}")


if __name__ == "__main__":
    # Generate the dataset
    df = generate_transactions_dataset(
        n_rows=1000, output_path="data/data_matplotlib.csv"
    )

    # Generate learning notes
    generate_learning_notes()

    print("\n✓ Dataset generation complete!")
    print(
        "✓ You can now use data/data_matplotlib.csv in your matplotlib learning script"
    )
