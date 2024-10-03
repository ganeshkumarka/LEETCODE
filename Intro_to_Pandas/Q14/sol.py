import pandas as pd

data = {
    'product': ['Umbrella', 'SleepingBag'],
    'quarter_1': [417, 800],
    'quarter_2': [224, 936],
    'quarter_3': [379, 93],
    'quarter_4': [611, 875]
}

report = pd.DataFrame(data)

reshaped_report = pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')

print(reshaped_report)
