import os
import pandas as pd
print(pd)
import sys
from helpers import calculate_total, format_currency
# print(sys.path)
# Add a folder to Python's search path
# sys.path.append("/path/to/my/folder")

os.chdir("../sales_analysis") # Change working directory

print("Check Directory: ", os.getcwd()) # Check current working directory


data_path = "data/sales.csv"

if os.path.exists(data_path): # Checking if the path exists in the working directory
    print(f"✅ Found {data_path}")
else:
    print(f"""❌ {data_path} not found.
    Make sure you are running from the sales_analysis folder""")



data = "data/sales.csv"

with open("data/sales.csv", "r") as file:
    content = file.read()

print(content)


df = pd.read_csv("data/sales.csv")

df["total"] = df["quantity"] * df["price"]

df

total = df.groupby("product")[["total"]].sum().sort_values(by="total", ascending=False).reset_index()

avg = df.groupby("product")[["total"]].mean().sort_values(by="total", ascending=False).reset_index()


df.to_json("output/sales.json", orient="records", indent=4)
total.to_json("output/total.json", orient="records", indent=4)
avg.to_json("output/avg.json", orient="records", indent=4)
df.to_excel("output/sales.xlsx", index=False)
total.to_excel("output/total.xlsx", index=False)


with open("../useful_commands.txt", "r") as file:
    requirements = file.read()

print(requirements)



df = pd.read_csv("data/sales.csv")

totals = []
prices = []

for index, row in df.iterrows():
    total = calculate_total(row["quantity"], row["price"])
    price = row["price"]
    total = format_currency(total)
    price = format_currency(price)
    totals.append(total)
    prices.append(price)


df["total"] = total
df["price"] = price

df


for index, row in df.iterrows():
    totals.append(
        format_currency(
            calculate_total(row["quantity"], row["price"])
        )
    )

df["total"] = totals

df

#------------------------------------------------------------
try:
    for index, row in df.iterrows():
        totals.append(
            calculate_total(row["quantity"], row["price"])
        )

except:
    df["total"] = totals

df



