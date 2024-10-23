s = "hello"
li = list(s)
new =[]

for s in li:
    last_char = li.pop()
    li.insert(0,last_char)
    ab = "".join(li)
    new.append(ab)
print(new)
