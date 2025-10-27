def generate_power_bill():
    try:
        units = float(input("Enter the number of units consumed: "))
        if units < 0:
            print("Units consumed cannot be negative.")
            return
        charge_per_unit = float(input("Enter the charge per unit: "))
        if charge_per_unit < 0:
            print("Charge per unit cannot be negative.")
            return
        user_type = input("Enter user type (domestic/commercial): ").strip().lower()
        if user_type not in ['domestic', 'commercial']:
            print("Invalid user type. Please enter 'domestic' or 'commercial'.")
            return

        if user_type == 'domestic':
            fixed_charge = 50
        else:  # commercial
            fixed_charge = 100

        bill = units * charge_per_unit
        total_bill = bill + fixed_charge

        print(f"User Type: {user_type.capitalize()}")
        print(f"Units Consumed: {units}")
        print(f"Charge per Unit: ₹{charge_per_unit:.2f}")
        print(f"Energy Charge: ₹{bill:.2f}")
        print(f"Fixed Charge: ₹{fixed_charge:.2f}")
        print(f"Total Power Bill: ₹{total_bill:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numbers for units and charge per unit.")

generate_power_bill()
