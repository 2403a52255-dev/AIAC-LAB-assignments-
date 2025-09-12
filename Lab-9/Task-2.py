class SRU_Student:
    def __init__(self, name, roll_no, hostel_status, fee_paid=0):
        # Initialize student details
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status   # Yes/No or True/False
        self.fee_paid = fee_paid

    # Method to update fee
    def fee_update(self, amount):
        self.fee_paid += amount  # Add the amount to fee_paid
        print(f"₹{amount} added. Total fee paid: ₹{self.fee_paid}")

    # Method to display student details
    def display(self):
        print(f"Name: {self.name}")  # Print student's name
        print(f"Roll No: {self.roll_no}")  # Print roll number
        print(f"Hostel Status: {self.hostel_status}")  # Print hostel status
        print(f"Fee Paid: ₹{self.fee_paid}")  # Print fee paid

# Example usage
if __name__ == "__main__":
    student1 = SRU_Student("Namitha", "SRU123", "Yes")  # Create a student object
    student1.display()  # Display initial details
    student1.fee_update(5000)  # Update fee by 5000
    student1.display()  # Display updated details