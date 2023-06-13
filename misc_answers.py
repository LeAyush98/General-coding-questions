
# # Write a program to reverse an integer in Python.

def reverse(num: int) -> int:
    pass
    num = list(str(num))
    for _ in range(len(num)//2):
        num[_] , num[(len(num) -1) -_] = num[(len(num) -1) -_], num[_]
    return int("".join(num))

# print(reverse(int(input("Please enter the number to reverse"))))

# # Python program to calculate LCM of given two numbers.
# # Python Program to find GCD or HCF of two numbers.
# # Python Program to find GCD of two numbers using recursion.

def lcm(num1, num2, start) -> int:
    answer = None
    found = False
    while not found:
        list1 = [num1*i for i in range(start, start*10)]
        list2 = [num2*i for i in range(start, start*10)]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    answer = list2[j]
                    found = True
                    break
            if found:
                    break    
        start+=10    
    return answer    
                    
#     # print(list1)
#     # print(list2)

# print(lcm(1642,1931,1))    
# print(f"HCF is {(1642*1931)/lcm(1642,1931,1)}")

# Python Program to Convert Decimal Number into Binary.
# Python Program to convert Decimal number to Octal number.

def dec_to_bin(num: int) -> int :
    bin = []
    while num >= 1:
        bin.append(num%2) 
        num = num//2      
    bin.reverse()
    return bin

# print(dec_to_bin(987))

def dec_to_oct(num: int) -> int :
    oct = []
    while num >= 1:
        oct.append(num%8)  
        num = num//8
    oct.reverse()
    return oct

# print(dec_to_oct(8453))

def swap(a,b):
    a = a+b
    b = a-b
    a = a-b
    print(a)
    print(b)

# swap(5,3)


# fibonnaci with recursion 

# 1, 1, 1+1, 3,5,8,13

arr = []

def fibonac(n):
    for i in range(n):
        if len(arr) < 2:
            arr.append(1)  
            continue
        else:
            arr.append(arr[i-1] + arr[i-2])
    return arr

# print(fibonac(10))    
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

def rfibonac(n):
    if n == 1 or n == 2:
        return 1  
    else:
        # arr.append(arr[i-1] + arr[i-2])
        return rfibonac(n-1) + rfibonac(n-2)

# for i in range(1,10+1):    
#     print(rfibonac(i), end=" ")    

# Python Program to calculate factorial using iterative method.
def facto(num):
    result = 1
    for i in range(1, num+1):
        result = result * i
    print(result)   

# facto(5)

# Python Program to calculate factorial using recursion.
def facto(num):
    if num == 0:
        return 1
    else:
        return num * facto(num-1)

# print(facto(5))


# Python Program to find Smallest number among three.
def smallest(a,b,c):
    list1 = [a,b,c]
    for i in range(len(list1) - 1):
        for j in range(len(list1) - 1 - i):
            if list1[j] > list1[j+1]:
                list1[j] , list1[j+1] = list1[j+1] , list1[j]
    print(list1[0])

# smallest(9,8,10)

# Python program to print first n Prime Number with explanation.
arr = []
def primenum(n):
    for i in range(n+1):
        if i == 2:
            arr.append(i)
        elif i > 2:
            count = 0
            for j in range(1, (i//2)+1):
                if i%j == 0:
                    count +=1
            if count < 2:
                print(f"{i} is prime")                

# primenum(100)

# Python Program to print Prime Number in a given range.

arr = []
def primenum(start, n):
    for i in range(start, n+1):
        if i == 2:
            arr.append(i)
        elif i > 2:
            count = 0
            for j in range(1, (i//2)+1):
                if i%j == 0:
                    count +=1
            if count < 2:
                print(f"{i} is prime")                

# primenum(50, 100)

# n = ["a", "b", "c"]
# n.remove("b")
# print(n.count('a'))
# print("".join(n))

# Python Program to check if two Strings are Anagram.
def anagram(a,b):
    count = 0
    a = list(a)
    b = list(b)
    if len(a) == len(b):
        for letter in a:
            if letter in b:
                count+=1
            else:
                return False
        for letter in b:
            if letter in a:
                count+=1
            else:
                return False    
        if count == 2*len(a):
            return True
    else: 
        return False

# print(anagram("fats", "fast"))    


# Palindrome
def adrome(string:str) -> str:
    string = list(string)
    # revers = string
    for _ in range(len(string)//2):
        pass
        string[_] , string[len(string)- 1 - _] = string[len(string)- 1 - _] , string[_]
    return "".join(string)

# string = "hannah"
# print(adrome(string) == string)    

# nam = "avs adds"
# nam = nam.replace(" ", "")
# print(nam)

# Python program to print all non repeating character in string.
def nrc(string:str) -> str:
    nrcl = []
    string = list(string)
    for _ in string:
        if string.count(_) == 1:
            nrcl.append(_)
    return "".join(nrcl)        

# print(nrc("ayush sharma"))


# Python program to concatenate two strings without using join() method.
def conc(a,b):
    a = list(a)
    b = list(b)
    for _ in b:
        a.append(_)
    return "".join(a)

# print(conc("ayush", "sharma"))    

# Python program to remove repeated character from string.
# Python program to calculate sum of integers in string.
def soi(string:str) -> int:
    sum = 0
    string = list(string)
    for _ in string:
        if _.isdigit():
            sum += int(_)
    return sum

# print(soi("ayu.sharma798"))        

# Python program to print the highest frequency character in a String.
def hfc(string:str):
    string = list(string)
    lstring = [string.count(_) for _ in string]
    return string[lstring.index(max(lstring))]
    

# print(hfc("ayush sharma"))    

# Python program to convert lowercase char to uppercase of string.
def ltu(string:str):
    string = list(string)
    beans = []
    # ustring = [_.upper() if _.islower() else _ for _ in string for _ in string]
    for _ in string:
        if _.islower():
            beans.append(_.upper())
        else:
            beans.append(_)       
    return "".join(beans)

# print(ltu("Ayush Sharma"))

# Python program to convert lowercase vowel to uppercase in string.
def lcv(string:str) -> str:
    answer = []
    vowels = ["a","e","i","o","u"]
    string = list(string)
    for _ in string:
        if _ in vowels:
            if _.islower():
                answer.append(_.upper())
            else:
                pass
        else:
            answer.append(_)        
    return "".join(answer)

# print(lcv("Ayush Sharma"))

# reverse string with recursion

def revstr(arr: list, index:int) -> str:
    if index < len(arr) // 2:
        arr[index] , arr[len(arr) - 1 - index] = arr[len(arr) - 1 - index] , arr[index]
        revstr(arr , index+1)
    return arr    

nam = "ayush sharma"
nam = list(nam)
print(revstr(nam, 0))
