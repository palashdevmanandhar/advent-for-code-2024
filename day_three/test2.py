from re import findall

total1 = total2 = 0
enabled = True
# Specify the path to your text file
file_path = 'input2.txt'

# Open the file and read its content as a string
with open(file_path, 'r') as file:
    file_content = file.read()

for a, b, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", file_content):
    if do or dont:
        enabled = bool(do)
    else:
        x = int(a) * int(b)
        if enabled: 
            print("Extracted string:",int(a),int(b),x)
        total1 += x
        total2 += x * enabled

print( total2)