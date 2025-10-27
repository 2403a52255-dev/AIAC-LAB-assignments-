def generate_power_bill():
    try:
        units = float(input("Enter the number of units consumed: "))
        if units < 0:
            print("Units consumed cannot be negative.")
            return

        # Example slab rates (can be adjusted as needed)
        if units <= 100:
            rate = 1.5
            bill = units * rate
        elif units <= 300:
            bill = 100 * 1.5 + (units - 100) * 2.5
        else:
            bill = 100 * 1.5 + 200 * 2.5 + (units - 300) * 4.0

        fixed_charge = 50  # Example fixed charge
        total_bill = bill + fixed_charge

        print(f"Units Consumed: {units}")
        print(f"Energy Charge: ₹{bill:.2f}")
        print(f"Fixed Charge: ₹{fixed_charge:.2f}")
        print(f"Total Power Bill: ₹{total_bill:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number for units consumed.")

generate_power_bill()
