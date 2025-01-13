Students = {
'Ahmed Ali': (1.72, 70),
'Adam Alami': (1.69, 65),
'Karim Tazi': (1.82, 68),
'Fatima Tabit': (1.65, 66)
}
t = 1.70
p = 65
Students2 ={item for item in Students.items() if item[1][0] >t and \
            item[1][1] >p}

print(dict(Students2))

