class Student:
    """
    Represents a student with a name, age, and a list of marks.
    Provides methods to display details and calculate total marks.
    """
    def __init__(self, name, age, mark1, mark2, mark3):
        """
        Initialize a Student instance.

        Args:
            name (str): The student's name.
            age (int): The student's age.
            mark1 (int or float): First mark.
            mark2 (int or float): Second mark.
            mark3 (int or float): Third mark.
        """
        self.name = name
        self.age = age
        self.marks = [mark1, mark2, mark3]

    def details(self):
        """
        Prints the student's name and age in a readable format.
        """
        print(f"Name: {self.name}\nAge: {self.age}")

    def total(self):
        """
        Returns the total of the student's marks.

        Returns:
            int or float: The sum of all marks.
        """
        return sum(self.marks)

# Example usage and output display
if __name__ == "__main__":
    student = Student("Alice", 20, 85, 90, 88)
    print("Student Details:")
    student.details()
    print(f"Total Marks: {student.total()}")
