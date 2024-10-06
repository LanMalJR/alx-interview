def pascal_triangle(n):
    
    """Returns a list of lists representing Pascal's Triangle up to level n."""
    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize the first row of the triangle
    
    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        row = [1]  # Start the new row with a 1
        
        # Calculate the intermediate values of the row
        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])
        
        row.append(1)  # End the row with a 1
        triangle.append(row)  # Add the row to the triangle
    
    return triangle
