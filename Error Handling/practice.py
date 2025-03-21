age = int(input("Enter Your age : "))

# if age < 0:
#     raise ValueError("age can not be nagative")

try:
    if age < 0 :
        raise ValueError("age can not be nagative")        
except:
    print("Invalid age! Please enter a valid age")



class InvalidMarksError(Exception):
    pass

marks = int(input("Enter your marks : "))

try:
    if marks<0 or marks>100:
        raise InvalidMarksError("Invalid Marks")
except:
    print("Marks should be between in 1 to 100")    