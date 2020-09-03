#Manuel Eduardo Alvarez Sanchez
#manuel.alvarez.sanchez@ucsp.edu.pe
def gerundio(cadena):
    tam=len(cadena)
    res1 = cadena.find(' ')
    res2 = res1+1
    primera_cadena=cadena[0:res1]
    segunda_cadena=cadena[res2:tam]
    tamm=len(primera_cadena)
    c1="ando"
    c2="iendo"
    c3="endo"
    c4="yendo"
    if primera_cadena=="reir":
        if segunda_cadena=="riendo":
            print("SI")
        else:
            print("NO")
    else:
        if primera_cadena[tamm-2] == 'a':
            tama=tamm-2
            primera_cadena=primera_cadena[0:tama]
            primera_cadena=primera_cadena+c1
            if primera_cadena==segunda_cadena:
                print("SI")
            else:
                print("NO")
        elif primera_cadena[tamm-2] == 'e':
            if (primera_cadena[tamm-3]=='a') or (primera_cadena[tamm-3]=='e') or (primera_cadena[tamm-3]=='i') or (primera_cadena[tamm-3]=='o') or (primera_cadena[tamm-3]=='u'):
                tama=tamm-2
                primera_cadena=primera_cadena[0:tama]
                primera_cadena=primera_cadena+c4
                if primera_cadena==segunda_cadena:
                    print("SI")
                else:
                    print("NO")
            else:
                tama=tamm-2;
                primera_cadena=primera_cadena[0:tama]
                primera_cadena=primera_cadena+c2
                if primera_cadena==segunda_cadena:
                    print("SI")
                else:
                    print("NO")
        elif primera_cadena[tamm-2] == 'i':
            if (primera_cadena[tamm-3]=='a') or (primera_cadena[tamm-3]=='e') or (primera_cadena[tamm-3]=='i') or (primera_cadena[tamm-3]=='o') or (primera_cadena[tamm-3]=='u'):
                tama=tamm-2
                primera_cadena=primera_cadena[0:tama]
                primera_cadena=primera_cadena+c4
                if primera_cadena==segunda_cadena:
                    print("SI")
                else:
                    print("NO")
            else:
                tama=tamm-1;
                primera_cadena=primera_cadena[0:tama]
                primera_cadena=primera_cadena+c3
                if primera_cadena==segunda_cadena:
                    print("SI")
                else:
                    print("NO")
    
print("ingresa cadena")
cadena=raw_input()
gerundio(cadena)

