'''
Had to search the internet for reading file in python, running loop in python, spliting a string, converting 
string to numeric value, getting absolute value, using the enumerate funtion properly 
'''

leftList=[]
rightList=[]
totalDistance=0

# Read the file, 
with open('../puzzle_input/one.txt', 'r') as file:
    for line in file:
        # Print each line
        currentPair= line.split()
        leftList.append(int(currentPair[0]))
        rightList.append(int(currentPair[1]))

leftList.sort()
rightList.sort()

for index,item in enumerate(leftList):
    diff=abs(leftList[index]-rightList[index])
    totalDistance+=diff
print("total Distance",totalDistance)
