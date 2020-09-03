def contar(cadena):
    arr=""
    correcto=True
    for char in cadena:
        if char == '(':
            arr=arr+'('
        elif char == ')':
            tam=len(arr)
            if tam-1<0:
                correcto=False
                break
            if arr[tam-1] == '(':
                tama=tam-1;
                arr=arr[0:tama]
            else:
                correcto=False
                break
        elif char == '[':
            arr=arr+'['
        elif char == ']':
            tam=len(arr)
            if tam-1<0:
                correcto=False
                break
            if arr[tam-1] == '[':
                tama=tam-1;
                arr=arr[0:tama]
            else:
                correcto=False
                break

    if len(arr)==0 and correcto==True:
        print("SI")
    else:
        print("NO")
print("ingresa cade")
cadena=raw_input()
contar(cadena)
