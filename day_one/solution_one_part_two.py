'''
Had to search the internet for reading file in python, running loop in python, spliting a string, converting 
string to numeric value, getting absolute value, using the enumerate funtion properly 
'''

leftList=[]
rightList=[]
occuranceSum=0

# Read the file, and create a seperate right and left list
with open('../puzzle_input/one.txt', 'r') as file:
    for line in file:
        # Print each line
        currentPair= line.split()
        leftList.append(int(currentPair[0]))
        rightList.append(int(currentPair[1]))

for index,item in enumerate(leftList):
    occurrenceCount= rightList.count(item)
    occuranceSum+= occurrenceCount*item

print("occuranceSum",occuranceSum)
