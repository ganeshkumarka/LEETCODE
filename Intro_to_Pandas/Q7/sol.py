import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    valid_rows = []

    for index, row in students.iterrows():
        if pd.notna(row['name']):
            valid_rows.append(row)
    result = pd.DataFrame(valid_rows)
    
    return result

#also {students.dropna(subset=['name'])}

data = {'student_id': [32, 217, 779, 849],
        'name': ['Piper', None, 'Georgia', 'Willow'],
        'age': [5, 19, 20, 14]}

students = pd.DataFrame(data)


result = dropMissingData(students)
print(result)
