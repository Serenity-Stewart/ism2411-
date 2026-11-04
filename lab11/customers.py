# 1.) I believe the general rule of thumb is whether you are certain or uncertain
# of data. you use brackets for when you know the key exists - being very structured data.
# meanwhile, use .get() if you're unsure if theres a key/if the data is entirely uncertain.

# 2.) while I never used excel, I'm aware of the similarities when it comes to rows and colums of informaton.
# however, python is much better at doing very large scare data sets while excel can only do a little.


print("--- Exercise 1 ---")
customer = {
    "name": "Alice",
    "Name": "not-Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])


print("--- Exercise 2 ---")
customer['phone'] = '555-5555'
print(customer)
customer['tier'] = 'platinum'
print(customer)
del customer ['Name']
print(customer)

print(customer.get('ytd_spend',0))

print("--- Exercise 3 ---")
print(customer.get("email", "no email on file"))

try:
    print(customer['email'])
except KeyError as error:
    print("KeyError caught: ", error)

print("--- Exercise 4 ---")

for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(key)

print("--- Exercise 5 ---")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.1,
    "platinum": 0.15
}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")

print("--- Exercise 6 ---")

customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"record")

print("--- Exercise 7 ---")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {name} - only {details['stock']} left")

print("--- Exercise 8 ---")

transactions = [
    {'region': 'South', 'amount': 300},
    {'region': 'North', 'amount': 150},
    {'region': 'South', 'amount': 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")
