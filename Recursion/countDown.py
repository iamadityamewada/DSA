def countDown(num:int):
    if num <= 0:
        print(0)
    else:
        print(num)
        countDown(num-1)     

countDown(10)


