deneme = "acabdkaca"


def isPalindrome(s:str):
    count = 0
    loop = round(len(s)/2)
    while(loop != count):
        if(s[0] == s[len(s)-1]):
            s = s[1:len(s)-1]
            count += 1
        else:
            return "number is not palindrome"
    return "number is palindrome"

result = isPalindrome(deneme)
print(result)