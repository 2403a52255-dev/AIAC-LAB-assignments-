def generate_power_bill():
    try:
        units = float(input("Enter the number of units consumed: "))
        if units < 0:
            print("Units consumed cannot be negative.")
            return

        user_type = input("Enter user type (domestic/commercial): ").strip().lower()
        if user_type not in ['domestic', 'commercial']:
            print("Invalid user type. Please enter 'domestic' or 'commercial'.")
            return

        if user_type == 'domestic':
            # Example slab rates for domestic users
            if units <= 100:
                bill = units * 1.5
            elif units <= 300:
                bill = 100 * 1.5 + (units - 100) * 2.5
            else:
                bill = 100 * 1.5 + 200 * 2.5 + (units - 300) * 4.0
            fixed_charge = 50
        else:  # commercial
            # Example slab rates for commercial users
            if units <= 100:
                bill = units * 2.5
            elif units <= 300:
                bill = 100 * 2.5 + (units - 100) * 4.0
            else:
                bill = 100 * 2.5 + 200 * 4.0 + (units - 300) * 6.0
            fixed_charge = 100

        total_bill = bill + fixed_charge

        print(f"User Type: {user_type.capitalize()}")
        print(f"Units Consumed: {units}")
        print(f"Energy Charge: ₹{bill:.2f}")
        print(f"Fixed Charge: ₹{fixed_charge:.2f}")
        print(f"Total Power Bill: ₹{total_bill:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number for units consumed.")

generate_power_bill()
