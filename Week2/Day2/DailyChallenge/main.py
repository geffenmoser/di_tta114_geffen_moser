matrix_list_strings = [ "7ii", "Tsx", "h%?", "i #","sM ", "$a ","#t%","^r!"]
matrix_new_string_0 = ""
matrix_new_string_1= ""
matrix_new_string_2= ""
for k in matrix_list_strings:
    if k[0].isalpha() == True:
        matrix_new_string_0 += k[0]
    else:
        matrix_new_string_0 += " "
    if k[1].isalpha() == True:
        matrix_new_string_1 += k[1]
    else:
        matrix_new_string_1 += " "
    if k[2].isalpha() == True:
        matrix_new_string_2 += k[2]
    else:
        matrix_new_string_2 += " "
new_string = matrix_new_string_0 + matrix_new_string_1 + matrix_new_string_2
print(new_string)