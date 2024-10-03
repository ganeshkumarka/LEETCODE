import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # Use .shape to get the number of rows and columns
    rows, columns = players.shape
    # Return the result as a list
    return [rows, columns]

# Example DataFrame
data = {
    'player_id': [846, 749, 155, 583, 388, 883, 355, 247, 761, 642],
    'name': ['Mason', 'Riley', 'Bob', 'Isabella', 'Zachary', 'Ava', 'Violet', 'Thomas', 'Jack', 'Charlie'],
    'age': [21, 30, 28, 32, 24, 23, 18, 27, 33, 36],
    'position': ['Forward', 'Winger', 'Striker', 'Goalkeeper', 'Midfielder', 'Defender', 'Striker', 'Striker', 'Midfielder', 'Center-back'],
    'team': ['RealMadrid', 'Barcelona', 'ManchesterUnited', 'Liverpool', 'BayernMunich', 'Chelsea', 'Juventus', 'ParisSaint-Germain', 'ManchesterCity', 'Arsenal']
}

players = pd.DataFrame(data)

# Get the size of the DataFrame
result = getDataframeSize(players)

# Output the result
print(result)
