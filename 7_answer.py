T = int(input())
E = []
L = []
guests_present = []
index = 0

for _ in range(T):
    E.append(int(input()))
for _ in range(T):
    L.append(int(input()))

while index < T:
   guests_present.append(E[index] - L[index]) 
   try:
       E[index+1] += guests_present[index]
   except IndexError:
       pass    
   index +=1

print(max(guests_present))
    