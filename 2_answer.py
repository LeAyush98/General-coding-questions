list_main = []
list_average = []
average1 = 0
average2 = 0
average3 = 0
count = 0

ELEMENT_COUNT = 9
SUM_COUNT = 3


for oxygen in range(ELEMENT_COUNT):
    list_main.append(int(input()))
    if list_main[oxygen] not in range(0,100):
        print("INVAID INPUT")
        break

for index in range(SUM_COUNT):
    if index == 0:
        average1 = round((sum(list_main[index: -1: SUM_COUNT])/SUM_COUNT))
        list_average.append(average1)
    if index == 1:
        average2 = round((sum(list_main[index: -1: SUM_COUNT])/SUM_COUNT))    
        list_average.append(average2)
    if index == 2:
        average3 = round(((sum(list_main[index: -1: SUM_COUNT]) + list_main[-1])/SUM_COUNT))    
        list_average.append(average3)
        
for average in list_average:
    if average < 70:
        count +=1

max = list_average.index(max(list_average))

if count == 3:
    print("All trainees are unfit")
else:
    print(f"Trainee Number: {max+1}")
    for position, average in enumerate(list_average):
        if max != position: 
            if average == list_average[max]:
                print(f"Trainee Number: {position+1}")

    

