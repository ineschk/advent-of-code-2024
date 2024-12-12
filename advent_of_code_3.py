import re
def part_1(file_path):
    # Open the file and read its content
    with open('input_file_day_3.txt', 'r') as file:
        content = file.read()


            # Define a regex pattern to match 'mul(x, y)' where x and y can be numbers
        pattern = r'mul\((\d+),(\d+)\)'  # Capture x and y as groups

            # Find all matches in the file
        matches = re.findall(pattern, content)

            # Calculate the multiplications and store in a list
        results = [int(x) * int(y) for x, y in matches]

            # Print the list of results
        

            # Calculate the total sum of the multiplications
        total_sum = sum(results)
        print("Total sum of the multiplications:", total_sum)
    file.close()
            
            
        
          

   







def part_2(file_path):

    def process_memory_with_conditions(file_path):
        """
        Process the corrupted memory from an input file to calculate the sum of results from enabled `mul` instructions.

        Args:
        - file_path (str): The path to the input file containing the corrupted memory.

        Returns:
        - int: The sum of the results of enabled `mul` instructions.
        """
        # Regex to extract valid mul instructions: mul(X,Y) where X and Y are integers
        mul_regex = r"mul\((\d+),(\d+)\)"
        
        # Regex to detect `do()` and `don't()` instructions
        do_regex = r"do\(\)"
        dont_regex = r"don't\(\)"

        # Initialize variables
        is_enabled = True  # Initially, mul instructions are enabled
        total_sum = 0

        # Read the file content
        with open(file_path, 'r') as file:
            memory = file.read()

        # Split memory into tokens to process sequentially
        tokens = re.split(f"({mul_regex}|{do_regex}|{dont_regex})", memory)
        
        for token in tokens:
            token = str(token).strip()

            # Check if the token is a valid `mul` instruction
            mul_match = re.match(mul_regex, token)
            if mul_match and is_enabled:
                # Extract numbers and calculate the product
                x, y = map(int, mul_match.groups())
                total_sum += x * y

            # Handle `do()` instruction to enable future `mul`
            elif re.match(do_regex, token):
                is_enabled = True

            # Handle `don't()` instruction to disable future `mul`
            elif re.match(dont_regex, token):
                is_enabled = False

        return total_sum

    # Example usage

    # Path to the input file
    input_file = "input_file_day_3.txt"

    # Process the memory and calculate the result
    result = process_memory_with_conditions(input_file)
    print("The sum of just the enabled multiplication is :", result)

# implementation 
if __name__ == "__main__":
    #Path to the input file
    input_file = "input_file_day_3.txt"
    part_1(input_file)
    part_2(input_file)
