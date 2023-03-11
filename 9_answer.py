from jovian.pythondsa import evaluate_test_cases

def binary_search(array :list, key: int) -> int:
    low = 0
    high = len(array)
    while low <= high:
        mid = (low+high)//2
        if array[mid] == key:
            return array.index(array[mid]) 
        elif array[mid] > key:
            high = mid - 1
        elif array[mid] < key:
            low = mid + 1
    return -1
array = [23,45,67,89,143,234]

test_case = [{
    "input" : {
        "array" : array,
        "key" : 143
    } ,

    "output" : 4
},
{
    "input" : {
        "array" : array,
        "key" : 9    
    } ,

    "output": -1
}    
]

evaluate_test_cases(binary_search, test_case)

#print(test_case["output"] == binary_search(low =0, high =len(array), array=test_case["input"]["array"]))
