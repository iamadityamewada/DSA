# type of error - compile time error and run time error 

charac = input("enter a value a: ")


try:
    print(a)
    print(int(charac))
    print(6 + charac)
   
except ValueError as e:
    print(e,": Some thing went wrong")
except TypeError as e:
    print(e,": value are not of int type")
# except NameError as e:
#     print(e)    
except:
    print("Some thing went wrong")    