import sys
import socket
import json
import pickle

def ConsultarBaseLivros():
	try:
		with open("dados.json", "r") as json_file:
			dados = json.load(json_file)
	except:
		dados = json.loads('[]')
	return dados

def PersistirBaseLivros(baseLivros):
	with open("dados.json", "w") as json_file:
		json.dump(baseLivros, json_file, indent=4)

def CriarLivro(json_input):
	livro_novo = json_input
	livro = json_input
	baseLivros = ConsultarBaseLivros()

	ultimoCodigo = 0
	for livro in baseLivros:
		if (livro["codigoLivro"] > ultimoCodigo):
			ultimoCodigo = livro["codigoLivro"]

	livro_novo["codigoLivro"] = ultimoCodigo + 1

	baseLivros.append(livro_novo)
	PersistirBaseLivros(baseLivros)
	return "Livro inserido com sucesso!"

def ConsultarLivroAutor(json_input):
	livro_consulta = json_input
	baseLivros = ConsultarBaseLivros()
	livrosRetorno = json.loads('[]')

	for livro in baseLivros:
		if (livro["autorLivro"] == livro_consulta["autorLivro"]):
			livrosRetorno.append(livro)

	return json.dumps(livrosRetorno)


def ConsultarLivroTitulo(json_input):
	livro_consulta = json_input
	baseLivros = ConsultarBaseLivros()
	livrosRetorno = json.loads('[]')

	for livro in baseLivros:
		if (livro["tituloLivro"] == livro_consulta["tituloLivro"]):
			livrosRetorno.append(livro)

	return json.dumps(livrosRetorno)


def ConsultarLivroPorAnoEdicao(json_input):
	livro_consulta = json_input
	baseLivros = ConsultarBaseLivros()
	livrosRetorno = json.loads('[]')

	for livro in baseLivros:
		if (livro["edicaoLivro"] == livro_consulta["edicaoLivro"] and livro["anoPublicacaoLivro"] == livro_consulta["anoPublicacaoLivro"]):
			livrosRetorno.append(livro)

	return json.dumps(livrosRetorno)


def RemoverLivro(json_input):
	livro_exclusao = json_input
	baseLivros = ConsultarBaseLivros()

	for livro in baseLivros:
		if (livro["tituloLivro"] == livro_exclusao["tituloLivro"]):
			baseLivros.remove(livro)

	PersistirBaseLivros(baseLivros)
	return "Livro removido com sucesso!"


def AlterarLivro(json_input):
	livro_alteracao = json_input
	baseLivros = ConsultarBaseLivros()

	for livro in baseLivros:
		if (livro["codigoLivro"] == livro_alteracao["codigoLivro"]):
			baseLivros.remove(livro)
			baseLivros.append(livro_alteracao)

	PersistirBaseLivros(baseLivros)
	return "Livro alterado com sucesso!"

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = 'localhost'
porta = int(sys.argv[1])

soquete.bind((ip,porta))

soquete.listen(10)

#------------- TESTE -------------
#livroteste = '{ "codigoLivro": "1", "tituloLivro": "Harry Potter e o prisioneiro de Azkaban", "autorLivro": "Nome de alguem", "edicaoLivro": "Segunda", "AnoPublicacaoLivro": 2010 }'
#CriarLivro(livroteste)
#------------        -------------

while True:
	s, end = soquete.accept()
	msg = s.recv(1024)

	json_input = json.loads(msg.decode())

	if (json_input["method"] == "CriarLivro"):
		s.send(CriarLivro(json_input["livro"]).encode())

	elif (json_input["method"] == "ConsultarLivroAutor"):
		s.send(ConsultarLivroAutor(json_input["livro"]).encode())

	elif (json_input["method"] == "ConsultarLivroTitulo"):
		s.send(ConsultarLivroTitulo(json_input["livro"]).encode())

	elif (json_input["method"] == "ConsultarLivroPorAnoEdicao"):
		s.send(ConsultarLivroPorAnoEdicao(json_input["livro"]).encode())

	elif (json_input["method"] == "RemoverLivro"):
		s.send(RemoverLivro(json_input["livro"]).encode())

	elif (json_input["method"] == "AlterarLivro"):
		s.send(AlterarLivro(json_input["livro"]).encode())

	s.close()

soquete.close()