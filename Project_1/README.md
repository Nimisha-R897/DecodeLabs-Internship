# Data Cleaning & Preprocessing Pipeline
A Python-based automated data cleaning pipeline using **Pandas** and **NumPy**. This script processes raw e-commerce order datasets, handles missing values, removes duplicates, standardizes string formats, and exports clean, ready-to-analyze data.
## 📌 Features
 **Data Inspection:** Logs original dataset dimensions, structure, and missing value counts.
 **Duplicate Removal:** Identifies and drops redundant records.
 **Smart Missing Value Imputation:**
  * **Numerical Columns:** Fills missing values with the column **mean**.
  * **Categorical Columns:** Imputes missing text values using the column **mode**.
* **Text Formatting:** Strips unwanted leading and trailing whitespace across text fields.
* **Automated Export:** Saves the processed data directly into a clean CSV format (`cleaned_dataset.csv`).
## 🛠️ Requirements & Installation
Ensure you have Python installed, then install the necessary dependencies via terminal:
```bash
pip install pandas numpy

## How to Run
place the row dataset named dataset.csv in the project directory
run the code
locate the output file : cleaned_dataset.csv

## Project Structure
Data-Cleaning-Project1/
│
├── dataset.csv            # Raw input dataset
├── cleaned_dataset.csv    # Processed output dataset (generated after script execution)
├── data_cleaning.py       # Main Python cleaning script
└── README.md              # Project documentation

## Sample Output

Missing Values Before Cleaning:
Quantity          12
UnitPrice          8
ShippingAddress    5
...

Missing Values After Cleaning:
Quantity          0
UnitPrice          0
ShippingAddress    0
...

Data cleaning complete! Saved to 'cleaned_dataset.csv'.