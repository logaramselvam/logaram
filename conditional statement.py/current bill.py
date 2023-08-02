customer_id = input("Enter customer ID: ")
customer_name = input("Enter customer name: ")
units_consumed = int(input("Enter units consumed: "))
if units_consumed <= 199:
    charge_per_unit = 1.20
elif 200 <= units_consumed < 400:
    charge_per_unit = 1.50
elif 400 <= units_consumed < 600:
    charge_per_unit = 1.80
else:
    charge_per_unit = 2.00

total_amount = units_consumed * charge_per_unit

# Apply surcharge if the bill exceeds Rs. 400
if total_amount > 400:
    surcharge = total_amount * 0.15
    total_amount += surcharge

# Set the minimum bill amount to Rs. 100
if total_amount < 100:
    total_amount = 100
print("\nElectricity Bill")
print(f"Customer ID: {customer_id}")
print(f"Customer Name: {customer_name}")
print(f"Units Consumed: {units_consumed}")
print(f"Total Amount to be Paid: Rs. {total_amount:.2f}")
