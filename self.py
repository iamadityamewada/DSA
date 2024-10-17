# input = "HelloAdityaYouAreCool"
# output = ["Hello", "Aditya","You","Are","Cool"]

#msg = input("Enter a Msg: ")
msg = "HelloAdityaYouAreCool"
word =""
res=[]
for i in msg:
    if i==i.upper() and word!="":
        res.append(word)
        word=""
    word = word + i
res.append(word)    
print(res)
    

