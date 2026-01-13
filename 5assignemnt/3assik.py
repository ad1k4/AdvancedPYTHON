# Task 3. OOP Principles & Custom Classes

# 1. Create a base class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Encapsulation (protected attribute)

    def introduce(self):
        return f"I am {self.name} and I am {self._age} years old."

# 2. Create a child class Student
class Student(Person):  # Inheritance
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    # 3. Polymorphism: Overriding a method
    def introduce(self):
        return f"Student: {self.name}, ID: {self.student_id}"

# Demonstration
if __name__ == "__main__":
    p = Person("John", 40)
    s = Student("Jane", 20, "S123")
    
    print(p.introduce())
    print(s.introduce())