import requests
import os


if not os.path.exists("../sales_analysis"):
    os.makedirs("../sales_analysis")

if not os.path.exists("../sales_analysis/data"):
    os.makedirs("../sales_analysis/data")

if not os.path.exists("../sales_analysis/data/sales.csv"):
    os.makedirs("../sales_analysis/data/sales.csv")

if not os.path.exists("../sales_analysis/output"):
    os.makedirs("../sales_analysis/output")


# Preferred approach using a for loop

for folder in {
    "../sales_analysis",
    "../sales_analysis/data",
    "../sales_analysis/output"
}:
    os.makedirs(folder, exist_ok=True)


#Download a web page
response = requests.get('https://api.github.com')
print(response.status_code)
