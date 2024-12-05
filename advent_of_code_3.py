import re

# Open the file and read its content
with open('example.txt', 'r') as file:
    content = file.read()

# Define a regex pattern to match 'mul(x, y)' where x and y can be numbers
pattern = r'mul\((\d+),(\d+)\)'  # Capture x and y as groups

# Find all matches in the file
matches = re.findall(pattern, content)

# Calculate the multiplications and store in a list
results = [int(x) * int(y) for x, y in matches]

# Print the list of results
print("Individual multiplications:", results)

# Calculate the total sum of the multiplications
total_sum = sum(results)
print("Total sum:", total_sum)
