import re

# Initialize total_sum and matches list
total_sum = 0
valid_matches = []

# Specify the path to your text file
file_path = 'test.txt'

# Open the file and read its content as a string
with open(file_path, 'r') as file:
    file_content = file.read()

# Split the content into chunks based on 'don't()' occurrences
chunks = file_content.split("don't()")

# Define the pattern for mul(x,y) where x and y are integers
pattern = r"mul\(\d+,\d+\)"


# Loop trough the chunks and consider valid pairs 
for i,chunk in enumerate(chunks):
    # If 'do()' appears in the chunk, process it; otherwise skip
    if i == 0:
        first_chuck_matches = re.findall(pattern, chunk)
        print("first chuck match",first_chuck_matches)
        valid_matches+=first_chuck_matches
    else:
        print("chunk",i,":",chunk)    

        if 'do()' in chunk:
            # Consider only the part of the chunk after the first 'do()' occurance
            match = re.search(r'do\(\)(.*)', chunk)
            result_after_fist_do = match.group(1) 
            
            print("do chunk",i,":",result_after_fist_do)
        
            # Find all matches in the current chunk
            found_matches = re.findall(pattern, result_after_fist_do)
            valid_matches+=found_matches
            print("do chunk matches",i,":",found_matches)


# Loop though the valid pairs, calculate the product and add to totalsum
for pair in valid_matches:
    pattern_one = r"\(([^,]+),"
    pattern_two= r",([^)]+)\)"
    match_one = re.search(pattern_one, pair)
    match_two = re.search(pattern_two,pair)
    result_one = int(match_one.group(1))
    result_two = int(match_two.group(1))
    
    product=result_one*result_two
    # print("Extracted string:", result_one,result_two,product)
    total_sum= total_sum + product

# # Print the result
print("Matches:", valid_matches)
print("Total Sum:", total_sum)
