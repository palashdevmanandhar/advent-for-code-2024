
import re
total_sum=0

# Specify the path to your text file
file_path = 'input.txt'

# Open the file and read its content as a string
with open(file_path, 'r') as file:
    file_content = file.read()


# Define the pattern for mul(x,y) where x and y are integers
pattern = r"mul\(\d+,\d+\)"

# Use re.findall to extract all matches
matches = re.findall(pattern, file_content)

print("matches check",matches)

for pair in matches:
    pattern_one = r"\(([^,]+),"
    pattern_two= r",([^)]+)\)"
    match_one = re.search(pattern_one, pair)
    match_two = re.search(pattern_two,pair)
    result_one = int(match_one.group(1))
    result_two = int(match_two.group(1))
    
    product=result_one*result_two
    print("Extracted string:", result_one,result_two,product)
    total_sum= total_sum + product
    

# Print the results
print("Extracted patterns:", total_sum)