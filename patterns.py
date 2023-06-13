def pattern1():
    for i in range(5):
        for j in range(i+1):
            print("*", end= " ")
        print() 

# pattern1()        

def pattern2():
    for i in range(5):
        print(f"{(i*2) * ' ' }", end="")
        for j in range(5,i,-1):
            print("*", end= " ")
        print() 


# pattern2()

def pattern3():
    for i in range(5):
        for j in range(i+1):
            print(j+1, end= " ")
        print() 

# pattern3()        

def pattern4():
    for i in range(5):
        # print(f"{(i*2) * ' ' }", end="")
        for j in range(5,i,-1):
            print("*", end= " ")
        print() 

# pattern4()

def pattern5():
    k = 5
    for i in range(5):
        print(f"{(k-1) * ' '}", end="")
        for j in range(2*i+1):
            print("*", end= "")
        print() 
        k -=1

# pattern5()        

def pattern6():
    for i in range(5):
        # print(f"{(i*2) * ' ' }", end="")
        for j in range(1,5+1-i,1):
            print(j, end= " ")
        print() 

# pattern6()


def pattern7():
    k = 5
    for i in range(5):
        print(f"{(k-1)* ' '}", end="")
        for j in range(i+1):
            print("*", end="")
        print()
        k -=1

# pattern7()

def pattern8():
    k = 0
    for i in range(5):
        print(f"{k* ' '}", end="")
        for j in range(2*(5 - i), 1, -1):
            print("*", end="")
        print()
        k +=1

# pattern8()            

def pattern9():
    k = 5
    for i in range(5):
        m = 1
        c = 0
        print(f"{k* ' '}", end="")
        for j in range(i+(i+1)):
            
            if j <= i:
                print(j+1+i, end="")
                pass
            else:
                print(j+i-m-c, end="")  
                m = m+1
                c = c+1
        print("\n\n")
        k -= 1

# pattern9()

def pattern10():
    k = 1
    for i in range(2*5):
        if i < 5:
            for j in range(i+1):
                print("*", end=" ")
        else:
            for j in range(5-k):
                print("*", end=" ")    
            k+=1    
        print()    

# pattern10()

def pattern11():
    k = 1
    space = 5
    for i in range(2*5):
        if i < 5:
            print(f"{(space-1)*' '}", end="")
            for j in range(i+1):
                print("*", end="")
            space-=1
        else:
            print(f"{(space+1)*' '}", end="")
            for j in range(5-k):
                print("*", end="")    
            space+=1
            k+=1    
        print() 
          
# pattern11()


def pattern13():
    rows = [[] for k in range(6)]
    for i in range(6):
        for j in range(i+1):
            if j == i or j == 0:
                print(1, end=" ")
                var = 1
            else:
                print(rows[i-1][j-1] + rows[i-1][j], end=" ")
                var = rows[i-1][j-1] + rows[i-1][j]
            rows[i].append(var)    
          
        print()
    return rows

# pattern13()

def pattern14():
    var = 0
    for i in range(5):
        for j in range(i+1):
            var += 1    
            print(var, end=" ")
        print()

# pattern14()

def pattern15():
    k = 5
    for i in range(5):
        print(f"{k*' '}" , end="")
        for j in range(5):
            print("x", end="")
        k-=1
        print()

# pattern15()

def pattern16():
    k = 0
    for i in range(5):
        print(f"{k*' '}" , end="")
        for j in range(5):
            print("x", end="")
        k+=1
        print()

# pattern16()

def pattern17():
    for i in range(3):
        for j in range(4):
            print("*", end=" ")
        print()

# pattern17()

def pattern18():
    n = 6
    b = 10
    for i in range(n):
        for j in range(b):
            if i == 0 or i == n-1:
                print("*", end=" ")
            else:
                if j == 0 or j == b-1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")    

        print()

# pattern18()

def pattern19():
    k = 5
    n = 5
    space = 1
    count = 1
    for i in range(2*n):
        if i < n:
            print(f"{k*' '}", end="")
            for j in range(i+1):
                if i % 2 == 0:
                    print("*", end="")
                else:
                    print("-", end="")
            k -= 1        
        else:
            print(f"{(space+1)*' '}", end="")
            for j in range(n-count):
                if i % 2 == 0:
                    print("*", end="")
                else:
                    print("-", end="")
            space+=1        
            count +=1        
        print()

pattern19()



def pattern20():
    k = 5
    for i in range(5):
        print(f"{k*' '}", end="")
        for j in range(2*i+1):
            if j == 0 or j == 2*i:
                print("*", end="")
            else:
                print("_", end="")    
        k=k-1    
        print()

# pattern20()
