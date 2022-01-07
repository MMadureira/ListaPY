inventario = []
resposta = "S"
while resposta == "S":
    equipamento=[input("\nEquipamento: "),
                 float(input("Valor: ")),
                 int(input("Número Serial: ")),
                 input("Departamento: ")]
    inventario.append(equipamento)
    resposta = input("\nDigite \"S\" para continuar ou \"N\" para sair: ").upper()

for elemento in inventario:
    print("\nNome...........: ", elemento[0])
    print("Valor..........: ", elemento[1])
    print("Serial.........: ", elemento[2])
    print("Departamento...: ", elemento[3])

busca=input("\nDigite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca == elemento[0]:
        print("\nValor.........: ", elemento[1])
        print("Serial........: ", elemento[2])
        print("Departamento..: ", elemento[3])

deprecicao=input("\nDigite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if deprecicao == elemento[0]:
        print("\nValor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])

serial=int(input("\nDigite o serial do equipamento que será excluído: "))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

for elemento in inventario:
    print("\nEquipamentos que ficaram: ")
    print("Nome...........: ", elemento[0])
    print("Valor..........: ", elemento[1])
    print("Serial.........: ", elemento[2])
    print("Departamento...: ", elemento[3])
