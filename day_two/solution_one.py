# Initialize a counter for safe reports and the dictionary to store files
inputData=[]
safeReports=0
valid_sorted_list = []

# Read input data from file and store the data into dictionary
# Use line.strip().split() to remove any trailing spaces or newline characters and split the line into individual strings.
# Use map(int, ...) to convert the strings into integers.

with open('./day_two_input.txt','r') as file:
    for line in file:
        inputData.append(list(map(int, line.strip().split())))
        

# Check if the data are in sorted order, either descending or ascending
def is_sorted(list):
    if list == sorted(list) or list == sorted(list, reverse=True):
        return True
    else:
        return False 

# Check difference between consicutive levels is valid
def check_diff(list):
    print("curr list",list)
    for i in range(len(list) - 1):  # Iterate until the second-to-last element
        diff = abs(list[i] - list[i+1])
        if not (1 <= diff <= 3):  # Check if the difference is outside the range 1 to 3
            print("Invalid difference:", list[i], list[i+1], "with difference:", diff)
            return False
    return True  


# Loop through the list and check if list is sorted
for i,currList in enumerate(inputData):
    sortedList= is_sorted(currList)
    if sortedList == True:
        valid_sorted_list.append(currList)

# Loop through the sorted List and check the difference between consecutive levels validity
for list in valid_sorted_list:
    correct_difference_list=check_diff(list)
    if correct_difference_list == True:
        safeReports+=1


print('all line',safeReports)