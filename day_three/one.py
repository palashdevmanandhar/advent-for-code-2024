import re

# Initialize the total sum
total_sum = 0

# Specify the path to your text file
file_path = 'input.txt'

# Read the file content
with open(file_path, 'r') as file:
    file_content = file.read()

# Define a regex pattern to capture both numbers in mul(x,y)
pattern = r"mul\((\d+),(\d+)\)"

# Find all matches and extract the numbers as tuples of strings
matches = re.findall(pattern, file_content)
# print("matches",matches)

# Calculate the product for each pair and update the total sum
for x, y in matches:
    product = int(x) * int(y)
    # print("Extracted numbers:", x, y, "Product:", product)
    total_sum += product

# Output the final total sum
print("Total Sum:", total_sum)

# 191183308 for input.txt