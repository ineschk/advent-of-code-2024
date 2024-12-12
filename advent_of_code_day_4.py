def part_1(file_path):
    with open(file_path,'r') as file :
        grid = [] 
        # reading the grid of str from a file input 
        for line in file:
            grid.append(line.strip())
        word = 'XMAS'
        
        def count_word_in_grid(grid, word):
            rows = len(grid)
            cols = len(grid[0])
            word_lenght = len(word)
            directions = [
                (0,1 ),     #Right
                (0,-1),     #Left
                (1, 0),     #Down
                (-1,0),     #Up
                (1, 1),     #Down-Right
                (-1,1),     #Up-Right
                (1,-1),     #Down-Left
                (-1,-1),    #Up-Left
            
            ]
            count = 0
            def check_word(x,y,dx,dy):
                for i in range(word_lenght):
                    nx, ny = x + i * dx , y +i * dy
                    if not( 0 <= nx < rows and 0 <= ny < cols )or grid[nx][ny] != word[i]:
                        return False
                return True
            for x in range(rows):
                for y in range(cols):
                    for dx, dy in directions:
                        if check_word(x,y,dx,dy):
                            count += 1
            return count
        
    count = count_word_in_grid(grid , word)
    print("le resulat est : ",count)   

def part_2(file_path):
    with open(file_path,'r') as file :
        grid = []
        # reading the grid of str from a file input
        for line in file:
            grid.append(line.strip())

        def count_xmas_patterns(grid):
            """
            Count the number of X-MAS patterns in a 2D grid.
            
            Args:
            - grid (list of list of str): 2D grid of letters.
            
            Returns:
            - int: The total number of X-MAS patterns found.
            """
            rows = len(grid)
            cols = len(grid[0])
            count = 0

            # Helper function to check the X-MAS pattern
            def is_xmas_pattern(x, y):
                """
                Check if an X-MAS pattern exists with (x, y) as the center.
                
                Returns:
                - bool: True if a valid X-MAS pattern is found, False otherwise.
                """
                if not (0 <= x - 1 < rows and 0 <= x + 1 < rows and 0 <= y - 1 < cols and 0 <= y + 1 < cols):
                    return False

                # Diagonal elements
                top_left = grid[x - 1][y - 1]
                bottom_right = grid[x + 1][y + 1]
                top_right = grid[x - 1][y + 1]
                bottom_left = grid[x + 1][y - 1]
                
                # Middle element
                middle = grid[x][y]

                # Check for the X-MAS pattern
                return (
                    (top_left + middle + bottom_right in ["MAS", "SAM"] and
                    top_right + middle + bottom_left in ["MAS", "SAM"])
                )

            # Iterate over each cell in the grid
            for x in range(rows):
                for y in range(cols):
                    if is_xmas_pattern(x, y):
                        count += 1

            return count
        count =  count_xmas_patterns(grid)
        print('le veritable resultat est ',count)



file_path = 'input_file_day_4.txt'
part_1(file_path) 
part_2(file_path)