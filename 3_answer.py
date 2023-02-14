N = int(input())
arr = []
new_arr = []
count = 0
for value in range(N):
    arr.append(int(input()))
   
for value in arr:
    if value != 0:
        new_arr.append(value)
    else:
        count += 1

for append in range(count):
    new_arr.append(0)

print(new_arr)