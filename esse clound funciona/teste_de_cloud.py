import os
import sys
import urllib.request

#Cores para deixar bonitinho
vermelho = '\033[31m' 
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
branco = '\033[37m'
vermelho_claro = '\033[91m'
verde_claro = '\033[92m'

def deletandp_arq_logs():
    try:
        os.remove("logs.txt")
        print(ciano+"Logs antigos deletados")
    except:
        print(vermelho_claro+"Erro em deletar os logs antigos...")
def criar_arq_logs():
    print(ciano+"Criando arquivo de logs...")
    arq  = open("logs.txt", "x")
    arq.close()
    print(verde_claro+"Arquivo de logs criado com sucesso!")
   
def testes():

    links_de_teste = [
"https://cdn-101.anonfiles.com/Y1Va80Q7y2/b57cc7d8-1673109868/teste.txt",
"https://cdn-130.filechan.org/Z8AdAdQ5y5/98976dc0-1673132668/teste.txt",
"https://cdn-117.letsupload.cc/NaC5A8Q6y6/22f494d9-1673132710/teste.txt",
"https://cdn-107.share-online.is/3aF0AfQ6y2/e2a7a439-1673132905/teste.txt",
"https://cdn-107.myfile.is/ydo8BdQcy6/54064a06-1673132925/teste.txt",
"https://cdn-130.megaupload.nz/Y7p3BcQcy7/4de96475-1673133479/teste.txt"
]

    for x in links_de_teste:
        print(ciano+"\n Testando:"+branco+x+"\n")
        
        try:
            urllib.request.urlretrieve(x, "teste_1.txt")#nome e extenção 
            os.remove("teste_1.txt")
            resultados = x+" OK! \n"
            print(branco+x+verde+" OK!")
            salvando_logs(resultados)
        except:
            erro = sys.exc_info()
            print(vermelho+ "ERROR!!! \n"+ vermelho_claro+str(erro)+branco)
            resultados = x+"   ERROR!!!\n"
            salvando_logs(resultados)
            try:
                os.remove("teste_1.txt")
            except:
                continue

 

def salvando_logs(resultados):
    arq = open("logs.txt", "a")
    arq.write(resultados)
    arq.close()



deletandp_arq_logs()
criar_arq_logs()
testes()