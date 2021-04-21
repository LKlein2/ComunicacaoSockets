import sys
import socket
import json
import pickle

def criarJson(method, codigoLivro, tituloLivro, autorLivro, edicaoLivro, anoPublicacaoLivro) :
    livros = {}
    livro = {}

    livros["method"] = method
    livros["livro"] = livro

    if (codigoLivro > 0) : livro["codigoLivro"] = codigoLivro
    if (tituloLivro != "") : livro["tituloLivro"] = tituloLivro
    if (autorLivro != "") : livro["autorLivro"]  = autorLivro
    if (edicaoLivro != "") : livro["edicaoLivro"] = edicaoLivro
    if (anoPublicacaoLivro > 0) : livro["anoPublicacaoLivro"] = anoPublicacaoLivro

    livrosString = json.dumps(livros)

    return livrosString

def comunicarServidor(json_input) :
    soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soquete.connect((ip,porta))
    soquete.send(json_input.encode())

    msg = soquete.recv(1024)

    soquete.close()
    
    return (msg.decode())

def menuPrincipal():
    print('''
            Sistema de consulta de livros - Sockets:

            [1] - Criar livro
            [2] - Consultar livro
            [3] - Consultar por ano e nro de edicao
            [4] - Remover livro
            [5] - Alterar livro
            [6] - Sair
        ''')

def menu1():
    print("Titulo do livro: ")
    tituloLivro = str(input())

    print("Autor do livro: ")
    autorLivro = str(input())

    print("Edicao do livro: ")
    edicaoLivro = str(input())

    print("ano de publicacao do livro: ")
    anoPublicacaoLivro = int(input())
    
    livroString = criarJson("CriarLivro",0,tituloLivro,autorLivro,edicaoLivro,anoPublicacaoLivro)
    
    msg = comunicarServidor(livroString)
    print(msg)

def menu2():
    escolhaMenu2 = 0

    while (escolhaMenu2 != 3):
        print('''
            Sistema de consulta de livros - Sockets:
            
            [Consultar livro]
            [1] - Consultar pelo Autor
            [2] - Consultar pelo Titulo
            [3] - Voltar
        ''')
        escolhaMenu2 = int(input('Escolha uma opção: '))

        if (escolhaMenu2 == 1) :
            print("Autor do livro: ")
            autorLivro = str(input())

            livroString = criarJson("ConsultarLivroAutor",0,"",autorLivro,"",0)

            msg = comunicarServidor(livroString)
            print(msg)

        elif (escolhaMenu2 == 2) :
            print("Titulo do livro: ")
            tituloLivro = str(input())

            livroString = criarJson("ConsultarLivroTitulo",0,tituloLivro,"","",0)

            msg = comunicarServidor(livroString)
            print(msg)

        elif (escolhaMenu2 == 3) :
            return
        elif (escolhaMenu2 > 3) :
            print("Opcao invalida")

def menu3():
    print("Ano do livro: ")
    anoPublicacaoLivro = int(input())

    print("Numero da edicao livro: ")
    edicaoLivro = str(input())

    livroString = criarJson("ConsultarLivroPorAnoEdicao",0,"","",edicaoLivro,anoPublicacaoLivro)

    msg = comunicarServidor(livroString)
    print(msg)

def menu4():
    print("Titulo do livro: ")
    tituloLivro = str(input())

    livroString = criarJson("RemoverLivro",0,tituloLivro,"","",0)

    msg = comunicarServidor(livroString)
    print(msg)

def menu5():
    print("Titulo do livro: ")
    tituloLivro = str(input())

    livroString = criarJson("ConsultarLivroTitulo",0,tituloLivro,"","",0)

    msg = comunicarServidor(livroString)
    json_input = json.loads(msg)

    escolhaMenu5 = 0

    while (escolhaMenu5 != 5):
        print('''
            Sistema de consulta de livros - Sockets:
            
            [Alterar livro]
            [1] - Alterar autor
            [2] - Alterar titulo
            [3] - Alterar edicao
            [4] - Alterar ano de publicacao"
            [5] - Voltar
        ''')
        escolhaMenu5 = int(input('Escolha uma opção: '))

        if (escolhaMenu5 == 1) :
            print("Autor do livro: ")
            autorLivro = str(input())

            for livro in json_input:
                codigoLivro = livro['codigoLivro']
                tituloLivro = livro['tituloLivro']
                edicaoLivro = livro['edicaoLivro']
                anoPublicacaoLivro = livro['anoPublicacaoLivro']
            
                livroString = criarJson("AlterarLivro",codigoLivro,tituloLivro,autorLivro,edicaoLivro,anoPublicacaoLivro)
                print(livroString)

                msg = comunicarServidor(livroString)
                print(msg)

                return
        elif (escolhaMenu5 == 2) : 
            print("Titulo do livro: ")
            tituloLivro = str(input())

            for livro in json_input:
                codigoLivro = livro['codigoLivro']
                autorLivro = livro['autorLivro']
                edicaoLivro = livro['edicaoLivro']
                anoPublicacaoLivro = livro['anoPublicacaoLivro']
            
                livroString = criarJson("AlterarLivro",codigoLivro,tituloLivro,autorLivro,edicaoLivro,anoPublicacaoLivro)
                
                msg = comunicarServidor(livroString)
                print(msg)
                
                return
        elif (escolhaMenu5 == 3) :
            print("Edicao do livro: ")
            edicaoLivro = str(input())

            for livro in json_input:
                codigoLivro = livro['codigoLivro']
                autorLivro = livro['autorLivro']
                tituloLivro = livro['tituloLivro']
                anoPublicacaoLivro = livro['anoPublicacaoLivro']
            
                livroString = criarJson("AlterarLivro",codigoLivro,tituloLivro,autorLivro,edicaoLivro,anoPublicacaoLivro)
                
                msg = comunicarServidor(livroString)
                print(msg)

                return
        elif (escolhaMenu5 == 4) :
            print("ano de publicacao do livro: ")
            anoPublicacaoLivro = int(input())

            for livro in json_input:
                codigoLivro = livro['codigoLivro']
                autorLivro = livro['autorLivro']
                tituloLivro = livro['tituloLivro']
                edicaoLivro = livro['edicaoLivro']
            
                livroString = criarJson("AlterarLivro",codigoLivro,tituloLivro,autorLivro,edicaoLivro,anoPublicacaoLivro)
                
                msg = comunicarServidor(livroString)
                print(msg)

                return

        elif (escolhaMenu5 == 5) :
            return
        elif (escolhaMenu5 > 5) :
            print("Opcao invalida")
            

def mainMenu() :
	escolhaPrincipal = 0

	while (escolhaPrincipal != 6):
		menuPrincipal()
		escolhaPrincipal = int(input('Escolha uma opção: '))

		if (escolhaPrincipal == 1) :
			menu1()
		elif (escolhaPrincipal == 2) :
			menu2()

		elif (escolhaPrincipal == 3) :
			menu3()

		elif (escolhaPrincipal == 4) :
			menu4()

		elif (escolhaPrincipal == 5) :
			menu5()
		elif (escolhaPrincipal > 6) :
			print("Opcao invalida")


if len(sys.argv) != 3:
	print('%s <ip> <porta>' %sys.argv[0])
	sys.exit(0)

ip = sys.argv[1]
porta = int(sys.argv[2])

mainMenu()