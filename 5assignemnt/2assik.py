import json

def manage_student_grades():
    # [cite_start]1. Create a students.json file [cite: 20]
    data = [
        {"name": "Alice", "age": 20, "grades": [85, 90, 92]},
        {"name": "Bob", "age": 22, "grades": [78, 81, 85]},
        {"name": "Charlie", "age": 21, "grades": [90, 95, 100]}
    ]
    
    with open('students.json', 'w') as f:
        json.dump(data, f, indent=4)

    # [cite_start]2. Read, calculate average, write to new file [cite: 24-27]
    try:
        with open('students.json', 'r') as f:
            students = json.load(f)
        
        updated_students = []
        for student in students:
            grades = student['grades']
            avg_grade = sum(grades) / len(grades) if grades else 0
            
            student_copy = student.copy()
            student_copy['average_grade'] = round(avg_grade, 2)
            updated_students.append(student_copy)
            
        # [cite_start]Writes the updated data back to a new JSON file [cite: 27]
        with open('students_updated.json', 'w') as f:
            json.dump(updated_students, f, indent=4)
            
        print("Processed data saved to students_updated.json")

    except FileNotFoundError:
        print("students.json not found")

if __name__ == "__main__":
    manage_student_grades()