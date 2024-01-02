import pandas as pd

# Assuming the data is in a file named 'data.xlsx' in the same directory.
# Load the data
file_path = 'clean.xlsx'
data = pd.read_excel(file_path)

# Define the columns for math anxiety and self-efficacy
math_anxiety_columns = ['ST292Q01JA', 'ST292Q02JA', 'ST292Q03JA', 'ST292Q04JA', 'ST292Q05JA', 'ST292Q06JA']
self_efficacy_columns = ['MATHEFF', 'MATHEF21', 'SDLEFF', 'ICTEFFIC']

# Filter rows where exactly one of the math anxiety columns is 97
filtered_data = data[(data[math_anxiety_columns] == 97).sum(axis=1) == 1]

# Filter out rows where any of the self-efficacy columns is 99
filtered_data = filtered_data[~filtered_data[self_efficacy_columns].isin([99]).any(axis=1)]

# Save the cleaned data to a new file
output_file_path = 'clean1.xlsx'
filtered_data.to_excel(output_file_path, index=False)
print(output_file_path)

