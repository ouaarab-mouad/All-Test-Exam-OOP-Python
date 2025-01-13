def sorted_dict(Dict):
    D = Dict.copy()
    temp_dict ={}
    while D :
        temp_value = D.values()[0]
        temp_key = D.keys()[0]
        for key in D.keys():
            if reversed:
                expression = temp_value < D[key]
            else:
                expression = temp_value > D[key]    
            
            
        temp.Dict[temp_key] = temp_value
        del D[temp_key]
    return temp_dict
print(sorted_dict(liste={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}))