# import pandas as pd

# def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
  
#     result = animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]

import pandas as pd

data = {
    'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
    'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
    'age': [98, 50, 6, 45, 100, 26],
    'weight': [464, 41, 328, 463, 50, 349]
}

animals = pd.DataFrame(data)

filtered_animals = animals[animals['weight'] > 100]

sorted_animals = filtered_animals.sort_values(by='weight', ascending=False)

result = sorted_animals[['name']]

print(result)
