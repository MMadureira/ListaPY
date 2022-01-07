from Cap3.IdentificacaoDeFuncoes import *

minhaLista = []
print("\n--------Preenchendo--------")
preencherInventario(minhaLista)
print("\n--------Exibindo--------")
exibirInventario(minhaLista)

print("\n\n--------Pesquisando--------")
localizarPorNome(minhaLista)
print("\n--------Alterando--------")
depreciarPorNome(minhaLista, 20)

print("\n\n--------Excluindo--------")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("\n--------Resumindo--------")
resumirValores(minhaLista)