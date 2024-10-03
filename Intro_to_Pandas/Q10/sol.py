import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

data = {'student_id': [32, 217, 779, 849],
        'name': ['Piper', 'Georgia', 'Willow', 'Henry'],
        'grade': ['A', 'B', 'C', 'D']}
students = pd.DataFrame(data)
