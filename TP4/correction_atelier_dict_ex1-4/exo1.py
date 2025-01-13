def sorted_dict(Dict,reverse = False):
    D = Dict.copy()
    Temp_Dict = {}
    while D:
        temp_value = list(D.values())[0]
        temp_key = list(D.keys())[0]
        for key in D.keys():
            if reverse: #ordre décroissant
                expression = temp_value < D[key]
            else: # ordre croissant
                expression = temp_value > D[key]
            if expression:
                temp_value = D[key]
                temp_key = key
        Temp_Dict[temp_key] = temp_value
        del D[temp_key]

    return Temp_Dict
print({1 : 2, 3 : 4, 4 : 3, 2 : 1, 0 : 0})
print(sorted_dict({1 : 2, 3 : 4, 4 : 3, 2 : 1, 0 : 0},reverse=True))


