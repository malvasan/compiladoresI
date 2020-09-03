def contar(cadena):
    cont_parentesis_abre=0
    cont_parentesis_cierra=0
    cont_laves_abre=0
    cont_llaves_cierra=0
    for char in cadena:
        if char == '(':
            cont_parentesis_abre=cont_parentesis_abre+1
        elif char == ')':
            cont_parentesis_cierra=cont_parentesis_cierra+1
        elif char == '[':
            cont_laves_abre=cont_laves_abre+1
        elif char == ']':
            cont_llaves_cierra=cont_llaves_cierra+1
    
    if (cont_parentesis_abre==cont_parentesis_cierra) and (cont_laves_abre==cont_llaves_cierra):
        print("SI")
    else:
        print("NO")
print("ingresa cade")
cadena=raw_input()
contar(cadena)
