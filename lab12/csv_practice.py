import csv
from datetime import datatime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

# with open(SALES_FILE, "r") as f:
#    reader = csv.reader(f)
#    header = next(reader)
#    for row in reader:

print("--- Exercise 1 ---")
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE}.")


print("--- Exercise 2 ---")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)