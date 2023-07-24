def pool(arr, capacity, rows, cols):
    res = 0
    for i in range(rows):
        for j in range(cols):
            res = arr[0][0] + arr[1][0]
            if res == capacity:
                return True
    return False

rows = int(input())
cols = int(input())
arr = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    arr.append(row)
capacity = int(input())
res = pool(arr, capacity, rows, cols)
print(res)
