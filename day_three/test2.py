import re
file_path = 'test.txt'

# Open the file and read its content as a string
with open(file_path, 'r') as file:
    file_content = file.read()


match = re.search(r'do\(\)(.*)', file_content)
result = match.group(1)  # Extract everything after 'do()'
print(result)


# do_chunk = file_content.split('do()')[-1]
# print("do chunk",do_chunk)