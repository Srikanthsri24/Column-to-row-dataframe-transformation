import pandas as pd

# Read the input from a CSV file
columnar_data = pd.read_csv('input.csv')

# Transform the columnar database to a row database
row_data = columnar_data.melt(id_vars=['ts'], var_name='item', value_name='count')
row_data = row_data[row_data['count'] == 1]  # Keep only rows with count = 1
row_data = row_data.drop(columns=['count'])

# Combine the items purchased for each timestamp into a single string
row_data = row_data.groupby('ts')['item'].apply(lambda x: ', '.join(x)).reset_index()

# Rename the columns to match the desired output
row_data.columns = ['ts', 'items purchased']

print(row_data)
