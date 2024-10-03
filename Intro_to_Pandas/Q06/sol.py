import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers_cleaned = customers.drop_duplicates(subset='email', keep='first')
    return customers_cleaned

# Sample input data
data = {'customer_id': [1, 2, 3, 4, 5, 6],
        'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
        'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 
                  'john@example.com', 'john@example.com', 'alice@example.com']}

customers = pd.DataFrame(data)

result = dropDuplicateEmails(customers)
print(result)
