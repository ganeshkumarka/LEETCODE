import pandas as pd

def create_student_dataframe(student_data):
    # Create DataFrame from the 2D list
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

# Example input: 2D list with student data
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

# Create DataFrame and display the result
student_df = create_student_dataframe(student_data)
print(student_df)
