# part one
'''
def total_distance_from_file(file_path):
# Initialize lists for the two columns
    column1 = []
    column2 = []

    # Read the file and parse into two lists
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into two numbers and convert to integers
            num1, num2 = map(int, line.split())
            column1.append(num1)
            column2.append(num2)

    # Sort the lists
    sorted_col1 = sorted(column1)
    sorted_col2 = sorted(column2)

    # Calculate the total distance
    total_distance = sum(abs(a - b) for a, b in zip(sorted_col1, sorted_col2))
    return total_distance
# Example usage
file_path = 'lists.txt'  # Replace with your file path
result = total_distance_from_file(file_path)
print(f"Total distance: {result}")

'''
# part 2 : 

def occurancy_in_list(file_path):
    with open(file_path, 'r') as file:
        
        column2 = []
        column1 = []
        for line in file:
            num1, num2 = list(map(int, line.split()))
            column1.append(num1)
            column2.append(num2)
        similarity = 0
        for num in column1:
            count_in_right = column2.count(num)  # Count how often num appears in the right list
            similarity += num * count_in_right 
        
    return similarity

# exemple : 
file_path = 'lists.txt'
result = occurancy_in_list(file_path)
print(f"Sum of the product of each number and its count: {result}")