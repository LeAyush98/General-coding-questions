def pattern1():
    for i in range(5):
        for j in range(i+1):
            print("*", end= " ")
        print("\n") 

# pattern1()        

def pattern2():
    for i in range(5):
        print(f"{(i*2) * ' ' }", end="")
        for j in range(5,i,-1):
            print("*", end= " ")
        print("\n") 


# pattern2()

def pattern3():
    for i in range(5):
        for j in range(i+1):
            print(j+1, end= " ")
        print("\n") 

# pattern3()        

def pattern4():
    for i in range(5):
        # print(f"{(i*2) * ' ' }", end="")
        for j in range(5,i,-1):
            print("*", end= " ")
        print("\n") 

# pattern4()

def pattern5():
    k = 5
    for i in range(5):
        print(f"{(k-1) * ' '}", end="")
        for j in range(2*i+1):
            print("*", end= "")
        print("\n") 
        k -=1

# pattern5()        

def pattern6():
    for i in range(5):
        # print(f"{(i*2) * ' ' }", end="")
        for j in range(1,5+1-i,1):
            print(j, end= " ")
        print("\n") 

# pattern6()


def pattern7():
    k = 5
    for i in range(5):
        print(f"{(k-1)* ' '}", end="")
        for j in range(i+1):
            print("*", end="")
        print("\n")
        k -=1

# pattern7()

def pattern8():
    k = 0
    for i in range(5):
        print(f"{k* ' '}", end="")
        for j in range(2*(5 - i), 1, -1):
            print("*", end="")
        print("\n")
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

pattern9()