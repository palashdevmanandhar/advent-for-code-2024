# Initialize a counter for safe reports and the dictionary to store files
inputData = []
safeReports = 0
valid_sorted_list = []

# Read input data from file and store the data into dictionary
# Use line.strip().split() to remove any trailing spaces or newline characters and split the line into individual strings.
# Use map(int, ...) to convert the strings into integers.

with open("./input.txt", "r") as file:
    for line in file:
        inputData.append(list(map(int, line.strip().split())))


def is_valid_with_removal(lst):
    # Check if the list is strictly sorted
    def is_strictly_sorted(lst):
        if all(lst[i] < lst[i + 1] for i in range(len(lst) - 1)):
            return True
        if all(lst[i] > lst[i + 1] for i in range(len(lst) - 1)):
            return True
        return False

    # Check if the list delta is between 1 and 3
    def is_strictly_valid(arr):
        for i in range(len(arr) - 1):
            diff = abs(arr[i] - arr[i + 1])
            if diff == 0 or diff > 3:
                return False
        return True

    if is_strictly_sorted(lst) and is_strictly_valid(lst):
        return True

    # try removing each element and check if the list becomes valid
    for i in range(len(lst)):
        temp_list = lst[:i] + lst[i + 1 :]  # Remove the element at index i
        if is_strictly_sorted(temp_list) and is_strictly_valid(temp_list):
            return True

    return False


for list in inputData:
    correct_difference_list = is_valid_with_removal(list)
    if correct_difference_list == True:
        safeReports += 1


print("all line", safeReports)