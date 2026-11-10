# 1.) It makes tasks much more simple in comparision to excel. This is because it's more efficient
# and holds a much larger scale of data than excel can hold. However, excel is much more manual and hands on. 
# 2.) I believe something thst can record customer transactions. This is because we can use this to count just how
# much of something we still have in stock for other consumers.
#

import csv
import datetime
from datetime import datetime

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

print("--- Exercise 3 ---")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(row)

print("--- Exercise 4 ---")

total_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader (f)
    next(reader)
    for row in reader:
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        dict_total += total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total Revenue: ${total_revenue:.2f}")

print("--- Exercise 5 ---")

high_value = []
low_value = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        if total > 100:
            high_value.append([product, f"{price:.2f}", quantity, f"total:.2f"])

with open(CLEANED_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    writer.writerows(high_value)

print(f"Original rows: {rows_read}")
print(f"Rows written: {len(high_value)}")


# come back to

print("--- Exercise 6 ---")

dict_total = 0
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantitiy"])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units x ${price:.2f} = ${total:.2f}")

print("--- Exercise 7 ---")

summary = {}
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + total
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

print("--- Exercise 8 ---")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%m:%S")
with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} total revenue: ${total_revenue:.2f}\n")

entries = 0
with open(LOG_FILE, "r") as f:
    for line in f:
        enteries+= 1
        print(line.strip())

print(f"Log enteries so far: {enteries}")