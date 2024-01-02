# Attempt to load the CSV file into a pandas DataFrame again
import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
file_path = 'HKG_clean_mathMean.csv'
try:
    # Attempt to read the file with pandas
    df = pd.read_csv(file_path)
    # Display the first few rows to confirm it's loaded correctly
    print(df.head())
except Exception as e:
    print(f"An error occurred: {e}")
# Replace '$null$' with NaN (Not a Number)
df.replace("$null$", pd.NA, inplace=True)

# Remove rows with NaN values
df.dropna(inplace=True)

# Convert the Math_mean and ST296Q01JA columns to numeric
df["Math_mean"] = pd.to_numeric(df["Math_mean"])
df["ST296Q01JA"] = pd.to_numeric(df["ST296Q01JA"])

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(df["ST296Q01JA"], df["Math_mean"], color='blue')
plt.title('Scatter Plot of Math_mean vs ST296Q01JA')
plt.xlabel('Time spent on mathematics homework (ST296Q01JA)')
plt.ylabel('Math_mean score')
plt.grid(True)
plt.show()