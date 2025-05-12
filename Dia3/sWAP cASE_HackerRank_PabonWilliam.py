# ####################
# # #### Dia 3  ######
# #####################

def swap_case(s):
    result = ''  
    for char in s: 
        if char.islower():  
            result += char.upper()  
        elif char.isupper():  
            result += char.lower()  
        else:
            result += char 
    return result  


s = input()
result = swap_case(s)
print(result)

# Desarrollado por : William Santiago Pabon Ardila - C.C:1.006.798.412