from turtledemo.sorting_animate import instructions1

#---- DESENVOLVA UM PROGRAMA QUE COLETE DADOS DA ALTURA E GENERO DE 15 PESSOAS ----#



valores = []
for dados in range(15):
    altura = float(input(f"\nQual a altura da {dados+1}° pessoas (em metros): "))/100
    genero = input("Digite o seu genero (M/F)? : ").upper()

    valores.append((altura , genero))

     ##################################################################

    #----- A MAIOR E MENOR ALTURA DO GRUPO -----#
    alturas = [t[0] for t in valores]
    maior_altura = max(alturas)
    menor_altura = min(alturas)

    #print(f"\nMaior altura: {maior_altura:.2f} m")
    #print(f"\nMenor altura: {menor_altura:.2f} m")

    #----- A MEDIA DE ALTURA DAS PESSOAS DO GENERO MASCULINO -----#

contador = 0

soma = 0
for pessoa in valores:
    if pessoa[1] == "M":
        soma += pessoa[0]
        contador += 1


media = 0
if contador > 0:
    media = soma/contador


    #----- O NUMERO DE PESSOAS O GENERO FEMENINO #

sexo_femenino = 0
for pessoa in valores:
    if pessoa[1] == "F":
        sexo_femenino += 1





    #---- CIANDO ARQUIVO .TXT ------#
with open("resultados.txt", "w") as arquivo:
    arquivo.write("------- MAIOR E MENOR ALTURA DO GRUPO -------\n")
    arquivo.write(f"\nMaior altura: {maior_altura:.2f} m\n")
    arquivo.write(f"Menor altura: {menor_altura:.2f} m\n")

    arquivo.write("\n------- ALTURA MEDIA DOS HOMENS -------\n")
    arquivo.write(f"\nmedia dos homens: {media:.2f} m\n")

    arquivo.write("\n------- QUANTIDADE DE MULHERES -------\n")
    arquivo.write(f"\nTotal de mulheres: {int(sexo_femenino):} \n")


    print("\n---- O RESULTADO ESTA NO ARQUIVO resultados.txt NA PASTA DO PROJETO ----")