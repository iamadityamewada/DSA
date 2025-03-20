class Number10Error(Exception):
    def __init__(self,msg,error_code):
        # self.msg = msg 
        super().__init__(f"{msg} - {error_code}")

num = int(input("Enter a number : "))

if num == 10:
    raise Number10Error("you can't enter number 10",501)