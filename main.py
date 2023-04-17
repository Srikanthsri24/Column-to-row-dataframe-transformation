
import pandas as pd

# Create a sample columnar database
columnar_data = pd.DataFrame({'ts': [1, 2, 3, 4, 5],
                              'bread': [1, 0, 0, 1, 1],
                              'milk': [1, 0, 0, 0, 1],
                              'books': [0, 1, 0, 0, 0],
                              'pen': [0, 1, 0, 0, 0],
                              'bat': [0, 0, 1, 0, 0],
                              'ball': [0, 0, 1, 0, 0],
                              'butter': [0, 0, 0, 1, 0]})
print(columnar_data)
# Transform the columnar database to a row database
row_data = columnar_data.melt(id_vars=['ts'], var_name='item', value_name='count')
row_data = row_data[row_data['count'] == 1]  # Keep only rows with count = 1
row_data = row_data.drop(columns=['count'])

# Combine the items purchased for each timestamp into a single string
row_data = row_data.groupby('ts')['item'].apply(lambda x: ', '.join(x)).reset_index()

# Rename the columns to match the desired output
row_data.columns = ['ts', 'items purchased']

print(row_data)
