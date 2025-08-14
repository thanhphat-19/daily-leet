
# input string interger
# output largest 3-same-digit
# Example: 
# Input: "5777897333"
# Output: "777"
# That we take a pointer to loop
# then, we check if the i == i+1 == i+2 is the same 
# if true, store it in a list 
# finally we take the max result 

def find_largest_3_same_digit(num: str) -> str:
    if int(num) < 100: 
        return ""
    results = []
    for i in  range (len(num)- 2) :
        if num[i] == num[i + 1] == num[i + 2]:
            results.append(num[i]*3)
    if not results:
        return ""

    largest_3_same_digit = max(results)
    return largest_3_same_digit
    
num = "2300019"
largest_3_same_digit = find_largest_3_same_digit(num)
print(largest_3_same_digit)



