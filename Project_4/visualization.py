import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")

# 1. Load Data
df = pd.read_csv('dataset.csv')
df = df.dropna()

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# ---------------------------------------------------------
# CHART 1: Bar Chart - Top Products by Total Revenue
# ---------------------------------------------------------
plt.figure(figsize=(9, 5))
product_sales = (
    df.groupby('Product')['TotalPrice']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

sns.barplot(
    data=product_sales,
    x='Product',
    y='TotalPrice',
    palette='Blues_d',
    legend=False,
)
plt.title(
    'Total Revenue by Product Category', fontsize=13, fontweight='bold', pad=12
)
plt.xlabel('Product', fontsize=11)
plt.ylabel('Total Revenue ($)', fontsize=11)
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig('1_product_sales_bar.png', dpi=300)
plt.show()

# ---------------------------------------------------------
# CHART 2: Pie Chart - Revenue Share by Referral Source
# ---------------------------------------------------------
plt.figure(figsize=(6.5, 6.5))
referral_sales = df.groupby('ReferralSource')['TotalPrice'].sum()

plt.pie(
    referral_sales,
    labels=referral_sales.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette('pastel'),
    textprops={'fontsize': 10, 'fontweight': 'bold'},
)

plt.title(
    'Revenue Distribution by Referral Source',
    fontsize=13,
    fontweight='bold',
    pad=12,
)

plt.tight_layout()
plt.savefig('2_referral_share_pie.png', dpi=300)
plt.show()

# ---------------------------------------------------------
# CHART 3: Line Chart - Monthly Sales Trend
# ---------------------------------------------------------
plt.figure(figsize=(10, 5))

# Group by Year-Month
df['YearMonth'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('YearMonth')['TotalPrice'].sum().reset_index()
monthly_sales['YearMonth'] = monthly_sales['YearMonth'].astype(str)

plt.plot(
    monthly_sales['YearMonth'],
    monthly_sales['TotalPrice'],
    marker='o',
    color='#2b5c8f',
    linewidth=2,
)

plt.title('Monthly Sales Trend Over Time', fontsize=13, fontweight='bold', pad=12)
plt.xlabel('Month', fontsize=11)
plt.ylabel('Total Sales ($)', fontsize=11)
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('3_monthly_trend_line.png', dpi=300)
plt.show()

print('✅ Project complete! Charts saved to your project folder.')