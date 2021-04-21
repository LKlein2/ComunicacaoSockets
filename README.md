Trabalho de comunicação cliente/servidor através de sockets.
Desenvolvido em conjunto com os colegas do curso de ciência da computação na universidade de caxias do sul.

Métodos de entrada esperados:

[
  {
    "method": "CriarLivro",
    "livro": {
      "tituloLivro": "Harry Potter e o prisioneiro de Azkaban",
      "autorLivro": "Nome de alguem",
      "edicaoLivro": "Segunda",
      "anoPublicacaoLivro": 2010
    }
  },
  {
    "method": "ConsultarLivroAutor",
    "livro": {
      "autorLivro": "Nome de alguem"
    }
  },
  {
    "method": "ConsultarLivroTitulo",
    "livro": {
      "tituloLivro": "Harry Potter e o prisioneiro de Azkaban"
    }
  },
  {
    "method": "ConsultarLivroPorAnoEdicao",
    "livro": {
      "edicaoLivro": "Segunda",
      "anoPublicacaoLivro": 2010
    }
  },
  {
    "method": "RemoverLivro",
    "livro": {
      "tituloLivro": "Harry Potter e o prisioneiro de Azkaban"
    }
  },
  {
    "method": "AlterarLivro",
    "livro": {
      "codigoLivro": "1",
      "tituloLivro": "Harry Potter e o prisioneiro de Azkaban",
      "autorLivro": "Nome de alguem",
      "edicaoLivro": "Segunda",
      "anoPublicacaoLivro": 2010
    }
  }
]

Execução no server(Linux): python3 server_tcp.py {Porta}
Execução no client(Linux): python3 client_tcp.py {IP server} {Porta server}