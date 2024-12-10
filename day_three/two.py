import re

# Initialize total sum and matches list
total_sum = 0
valid_matches = []

# Specify the path to your text file
file_path = 'input2.txt'

# Read the file content and normalize it by removing newlines
with open(file_path, 'r') as file:
    file_content = file.read().replace('\n', '')

# Split the content into chunks based on "don't()"
chunks = file_content.split("don't()")

# Define the pattern to extract `mul(x,y)` directly
pattern = r"mul\((\d+),(\d+)\)"

# Loop through the chunks and process them
for i, chunk in enumerate(chunks):
    if i == 0:  # First chunk is always valid
        matches = re.findall(pattern, chunk)
        # print("First chunk matches:", matches)
        valid_matches.extend(matches)
    else:
        # Process only if 'do()' exists in the chunk
        if 'do()' in chunk:
            # Extract the portion after the first 'do()'
            result_after_do = chunk.split('do()', 1)[1]
            matches = re.findall(pattern, result_after_do)
            print(f"Do chunk {i} matches:", matches)
            valid_matches.extend(matches)

# Compute the total sum of products
for x, y in valid_matches:
    product = int(x) * int(y)
    print("Extracted numbers:", x, y, "Product:", product)
    total_sum += product

# Print the result
print("Total Sum:", total_sum)
