
import pandas as pd

input_data = {'ts': [1, 2, 3, 4, 5],
              'items purchased': ['bread, milk', 'books, pen', 'bat, ball', 'bread, butter', 'bread, milk']}

row_data = pd.DataFrame(input_data)
print(row_data)
# Rest of the code to transform the row data to columnar data
item_counts = {}

for i, row in row_data.iterrows():
    for item in row['items purchased'].split(','):
        item = item.strip()
        if item not in item_counts:
            item_counts[item] = [0] * len(row_data)
        item_counts[item][i] += 1

columnar_data = pd.DataFrame(item_counts)
columnar_data.insert(0, 'ts', row_data['ts'])

# Save to a CSV file
columnar_data.to_csv('output.csv', index=False)

print(columnar_data)
