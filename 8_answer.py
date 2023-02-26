N = int(input())
B = []
index = 0
unique = []

for _ in range(N):
    B.append(input().casefold())

while index < N:
    if B[index] not in unique:
        unique.append(B[index])
    else:
        pass
    index = index + 1

for _ in unique:
    if B.count(_) % 2 != 0:
        print(_)
        break
    else:
        if _ == (len(unique)-1):
            print("All are even")
