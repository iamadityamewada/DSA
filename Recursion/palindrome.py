string = "mom"
# string = "Aditya"

def check_palindrome(string):
    rev_str = []
    def rev_string(string,index):
        if index < 0:
            return
        rev_str.append(string[index])
        rev_string(string,index-1)
    string = list(string)
    print(string)
    index = len(string) - 1
    rev_string(string,index)
    if string == rev_str:
        print("String is Palindrome")
    else:
        print("String is not palindrome")

check_palindrome(string)        

