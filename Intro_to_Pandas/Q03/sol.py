import pandas as pd

def display_first_three_rows(employees: pd.DataFrame) -> pd.DataFrame:
    # Use .head(3) to get the first 3 rows of the DataFrame
    return employees.head(3)

# Example DataFrame
data = {
    'employee_id': [3, 90, 9, 60, 49, 43],
    'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
    'department': ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources', 'Administration'],
    'salary': [48675, 11096, 33805, 37678, 23793, 40454]
}

employees = pd.DataFrame(data)

# Display the first 3 rows
result = display_first_three_rows(employees)
print(result)
