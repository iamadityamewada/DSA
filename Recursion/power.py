num = 6
pow = 2

def power_fun(num,p):
    if p == 0:
        return 1
    return num * power_fun(num,p-1)

print("Power :", power_fun(num,pow))