inputData=[]

with open('./day_two_input.txt','r') as file:
    for line in file:
        inputData.append(list(map(int, line.strip().split())))

def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    return set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}

safe_count = sum(is_safe(row) for row in inputData)
print(safe_count)

safe_count = sum(
    any(is_safe(row[:i] + row[i + 1:]) for i in range(len(row))) for row in inputData
)
print(safe_count)
