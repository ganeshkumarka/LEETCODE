import pandas as pd

def select_student(students: pd.DataFrame) -> pd.DataFrame:
    # Use the .query() method to filter the DataFrame
    result = students.query('student_id == 101')[['name', 'age']]
    return result

# Example DataFrame
data = {
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
}

students = pd.DataFrame(data)

# Select the student with student_id = 101
result = select_student(students)
print(result)
