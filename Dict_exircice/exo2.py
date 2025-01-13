dictionnaire ={}
key = input("entre le nom :")
value = input("Entre le valure:")
continue_adding=True
while continue_adding:
    if key in dictionnaire:
        dictionnaire[key] = dictionnaire[key]+","+value
    else:
        dictionnaire[key]=value
add_more = input(print("Do u want to add more"))
if add_more == 1 :
    continue_adding=False
else:
    continue_adding=True

print(dictionnaire)