import pandas as pd

# Read the input from a CSV file
row_data = pd.read_csv('input.csv')

# Create an empty dictionary to store the count of each item
item_counts = {}

# Loop through each row in the input DataFrame
for i, row in row_data.iterrows():
    # Split the items purchased string by comma and iterate through the resulting list of items
    for item in row['items purchased'].split(','):
        item = item.strip()  # Remove any whitespace around the item
        if item not in item_counts:
            item_counts[item] = [0] * len(row_data)  # Initialize the count for the new item to zeros
        # For each item, increment its count in the dictionary for the corresponding timestamp
        item_counts[item][i] += 1

# Convert the dictionary to a DataFrame
columnar_data = pd.DataFrame(item_counts)
columnar_data.insert(0, 'ts', row_data['ts'])

print(columnar_data)
