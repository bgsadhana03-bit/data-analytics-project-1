print("DecodeLabs Data Analytics Project 1")
print("Project: Data Cleaning and Preparation")
print("Learning Python step by step")
import pandas as pd
print("Pandas is ready!")
df = pd.read_excel("../Dataset for Data Analytics.xlsx")

print(df.head())
print("Dataset shape:", df.shape)
print("Column names:", df.columns.tolist())
print("Missing values in each column:")
print(df.isnull().sum())
print(df["CouponCode"].value_counts(dropna=False))
print("Duplicate OrderIDs:", df["OrderID"].duplicated().sum())
print("Unique OrderIDs:", df["OrderID"].nunique())
print("Date data type:", df["Date"].dtype)
print(df["Date"].head(10))
dates = pd.to_datetime(df["Date"], errors="coerce")

print("Missing or invalid dates:", dates.isna().sum())
print("Earliest date:", dates.min())
print("Latest date:", dates.max())
print("Completely duplicated rows:", df.duplicated().sum())
print("Total rows:", len(df))
print(df.dtypes)
print("Numeric columns summary:")
print(df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].describe())
expected_total = df["Quantity"] * df["UnitPrice"]

difference = (df["TotalPrice"] - expected_total).abs()

print("Rows with incorrect TotalPrice:", (difference > 0.01).sum())
print("Payment methods:")
print(df["PaymentMethod"].value_counts(dropna=False))

print("\nOrder statuses:")
print(df["OrderStatus"].value_counts(dropna=False))
text_columns = df.select_dtypes(include=["str"]).columns

for column in text_columns:
    non_missing = df[column].dropna()
    has_spaces = non_missing.ne(non_missing.str.strip())
    print(f"{column}: {has_spaces.sum()} values with extra spaces")
cleaned_df = df.copy()

print("Original rows:", len(df))
print("Cleaned copy rows:", len(cleaned_df))
cleaned_df = cleaned_df.drop_duplicates()

print("Rows after removing duplicates:", len(cleaned_df))
print("Duplicate rows remaining:", cleaned_df.duplicated().sum())

print("Missing values in cleaned copy:")
print(cleaned_df.isnull().sum())

print("Date data type in cleaned copy:", cleaned_df["Date"].dtype)

cleaned_dates = pd.to_datetime(cleaned_df["Date"], errors="coerce")

print("Missing or invalid dates in cleaned copy:", cleaned_dates.isna().sum())

text_columns = cleaned_df.select_dtypes(include=["str"]).columns

for column in text_columns:
    cleaned_df[column] = cleaned_df[column].str.strip()

print("Text columns checked and trimmed:")
print(text_columns.tolist())

print("Checking for extra spaces after cleaning:")

for column in text_columns:
    has_extra_spaces = cleaned_df[column].dropna().ne(
        cleaned_df[column].dropna().str.strip()
    )
    print(f"{column}: {has_extra_spaces.sum()} values with extra spaces")
    
output_file = "C:/Users/SADHANA/Downloads/data-analytics-project-1/Cleaned_Data_Analytics.xlsx"

cleaned_df.to_excel(output_file, index=False)

print("Cleaned dataset saved to:", output_file)

check_df = pd.read_excel(output_file)

print("Saved file shape:", check_df.shape)
print("Duplicate OrderIDs:", check_df["OrderID"].duplicated().sum())

check_dates = pd.to_datetime(check_df["Date"], errors="coerce")
print("Missing or invalid dates:", check_dates.isna().sum())

print("Missing values in saved file:")
print(check_df.isnull().sum())

