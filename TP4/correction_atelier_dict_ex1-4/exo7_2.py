Students = {
'Ahmed Ali': (1.72, 70),
'Adam Alami': (1.69, 65),
'Karim Tazi': (1.82, 68),
'Fatima Tabit': (1.65, 66)
}
t = 1.70
p = 65
Students2 ={}

for key in Students.keys():
    if Students[key][0] > t and Students[key][1] >p:
        Students2[key] = Students[key]

print(Students2)

