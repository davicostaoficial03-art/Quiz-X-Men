# Exibe a mensagem de boas-vindas ao quiz
Int(input("bem vindo ao quiz"))

# Inicializa a pontuação do jogador
pontos = 0

# Exibe a primeira pergunta e suas alternativas
print("Quem fundou o instituto Xavier ?", "\n a) Brian Xavier", "\n b) Charler Xavier", "\n c) Sharon Xavier", "\n d) Cassandra Nova", "\n e) Kurt Marko")

# Solicita a resposta do jogador
resposta = input("insira resposta ")

# Verifica se a resposta corresponde à alternativa correta
if resposta.lower() == "b":
    print("Correto")
    pontos += 1  # Adiciona um ponto à pontuação
else:
    print("errado")  # Informa que a resposta está incorreta

# Exibe a segunda pergunta e suas alternativas
print("Quais foi o primeiro mutante que o professor Charles Xavier recrutou para sua instituição ?", "\n a) Ciclope", "\n b) Homem de gelo", "\n c) Anjo", "\n d) Fera", "\n e) Jean Grey")

# Solicita a resposta do jogador
resposta = input("Ciclope ")

# Verifica se a alternativa A foi selecionada
if resposta.lower() == "a":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a terceira pergunta sobre os poderes do Professor Xavier
print("Quais são os poderes do professor Xavier ?", "\n a) visão raio X, intangibilidade e telepatia", "\n b) manipulação do gelo e telescinesse", "\n c) voar e telepatia", "\n d) telepatia, manipulação mental e projeção astral", "\n e) super força, super velocidade e projeção astral")

# Solicita a resposta do jogador
resposta = input("telepatia, manipulação mental e projeção astral ")

# Verifica se a alternativa D foi selecionada
if resposta.lower() == "d":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a quarta pergunta sobre os poderes do Ciclope
print("Quais são os poderes do ciclope ?", "\n a) super velocidade", "\n b) voar", "\n c) manipulação do tempo", "\n d) telecinese", "\n e) emissão de raios ópticos")

# Solicita a resposta do jogador
resposta = input("emissão de raios ópticos")

# Verifica se a alternativa E foi selecionada
if resposta.lower() == "e":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a quinta pergunta sobre os poderes de Bobby Drake
print("qual os poderes do Bobby Drake ?", "\n a) criocinese", "\n b) pirocinese", "\n c) telecinese", "\n d) clorocinese", "\n e) electrocinese")

# Solicita a resposta do jogador
resposta = input("criocinese ")

# Verifica se a alternativa A foi selecionada
if resposta.lower() == "a":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a sexta pergunta sobre os poderes do Fera
print("Quais são os poderes do fera ?", "\n a) intelecto genial", "\n b) super agilidade", "\n c) atributos aprimorados", "\n d) super força", "\n e) super velocidade")

# Solicita a resposta do jogador
resposta = input("atributos aprimorados ")

# Verifica se a alternativa C foi selecionada
if resposta.lower() == "c":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a sétima pergunta sobre os poderes do Anjo
print("Quais são os poderes do anjo ?", "\n a) capacidade de voar e atributos aprimorados", "\n b) super força e velocidade", "\n c) voar e nadar", "\n d) super velocidade e voo", "\n e) voo e super agilidade")

# Solicita a resposta do jogador
resposta = input("capacidade de voar e atributos aprimorados ")

# Verifica se a alternativa A foi selecionada
if resposta.lower() == "a":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a oitava pergunta sobre a primeira integrante dos X-Men
print("Qual foi a primeira integrante dos X-men ?", "\n a) Vampira", "\n b) Kitty Pryde", "\n c) Jean Grey", "\n d) Tempestade", "\n e) Mística")

# Solicita a resposta do jogador
resposta = input("jean Grey ")

# Verifica se a alternativa C foi selecionada
if resposta.lower() == "c":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a nona pergunta sobre os poderes de Jean Grey
print("Quais são os poderes da Jean Grey ?", "\n a) super velocidade e manipulação do tempo", "\n b) manipulação do tempo e pirocinese", "\n c) telepatia e telecinese", "\n d) falar com animais e clorocinese", "\n e) super força e criocinese")

# Solicita a resposta do jogador
resposta = input("capacidade de voar e atributos aprimorados ")

# Verifica se a alternativa A foi selecionada
if resposta.lower() == "a":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a décima pergunta sobre os poderes da Tempestade
print("Qual é o poder da tempestade ?", "\n a) absorção de poderes", "\n b) telepatia", "\n c) criocinese", "\n d) teletransporte", "\n e) manipulação do clima")

# Solicita a resposta do jogador
resposta = input("manipulação do clima ")

# Verifica se a alternativa E foi selecionada
if resposta.lower() == "e":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a décima primeira pergunta sobre os poderes da Vampira
print("Qual é o poder da vampira ?", "\n a) clorocinese", "\n b) projeção de escudos", "\n c) absorção de poderes", "\n d) intangibilidade", "\n e) super velocidade")

# Solicita a resposta do jogador
resposta = input("absorção de poderes ")

# Verifica se a alternativa C foi selecionada
if resposta.lower() == "c":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a décima segunda pergunta sobre os poderes de Kitty Pryde
print("Qual é o poder da Kitty Pryde ?", "\n a) projeção astral", "\n b) manipulação de densidade", "\n c) super velocidade", "\n d) intangibilidade", "\n e) pirocinese")

# Solicita a resposta do jogador
resposta = input("intangibilidade ")

# Verifica se a alternativa D foi selecionada
if resposta.lower() == "d":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a décima terceira pergunta sobre o interesse romântico de Kitty em X-Men: Evolution
print("Qual é o interesse romântico de Kitty Pryde em X-Men Evolution ?", "\n a) Noturno", "\n b) Bobby Drake", "\n c) Lance Alvers", "\n d) Gambit", "\n e) Ciclope")

# Solicita a resposta do jogador
resposta = input("Lance Alvers")

# Verifica se a alternativa C foi selecionada
if resposta.lower() == "c":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a décima quarta pergunta sobre o interesse romântico de Kitty em Wolverine e os X-Men
print("Qual é o interesse romântico de Kitty Pryde em Wolverine e os X-Men ?", "\n a) Noturno", "\n b) Bobby Drake", "\n c) Lance Alvers", "\n d) Gambit", "\n e) Ciclope")

# Solicita a resposta do jogador
resposta = input("Bobby Drake")

# Verifica se a alternativa B foi selecionada
if resposta.lower() == "b":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a décima quinta pergunta sobre o interesse romântico de Kitty no filme X-Men: O Confronto Final
print("Qual é o interesse romântico de Kitty Pryde em X-Men: O Confronto Final ?", "\n a) Noturno", "\n b) Bobby Drake", "\n c) Lance Alvers", "\n d) Gambit", "\n e) Ciclope")

# Solicita a resposta do jogador
resposta = input("Bobby Drake")

# Verifica se a alternativa B foi selecionada
if resposta.lower() == "b":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a décima sexta pergunta sobre os poderes do Noturno
print("Qual é o poder do Noturno ?", "\n a) criocinese", "\n b) voar", "\n c) teletransporte", "\n d) intangibilidade", "\n e) super velocidade")

# Solicita a resposta do jogador
resposta = input("teletransporte ")

# Verifica se a alternativa C foi selecionada
if resposta.lower() == "c":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a décima sétima pergunta sobre a cor do Noturno
print("Qual é a cor do Noturno ?", "\n a) Verde", "\n b) Vermelho", "\n c) Rosé", "\n d) Violeta", "\n e) Azul")

# Solicita a resposta do jogador
resposta = input("Azul ")

# Verifica se a alternativa E foi selecionada
if resposta.lower() == "e":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a décima oitava pergunta sobre a mãe do Noturno
print("Quem é a mãe do Noturno ?", "\n a) Vampira", "\n b) Tempestade", "\n c) Mística", "\n d) Jean Grey", "\n e) Tabitha Smith")

# Solicita a resposta do jogador
resposta = input("mística ")

# Verifica se a alternativa C foi selecionada
if resposta.lower() == "c":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a décima nona pergunta sobre os poderes da Mística
print("Qual é o poder da mística ?", "\n a) Regeneração", "\n b) Metamorfose", "\n c) Criação de escudos", "\n d) Criocinese", "\n e) Clorocinese")

# Solicita a resposta do jogador
resposta = input("mística ")

# Verifica se a alternativa C foi selecionada
if resposta.lower() == "c":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a vigésima pergunta sobre os vilões dos X-Men
print("Qual desses é um vilão ?", "\n a) Kitty Pryde", "\n b) Noturno", "\n c) Professor Xavier", "\n d) Magneto", "\n e) Bobby Drake")

# Solicita a resposta do jogador
resposta = input("Magneto ")

# Verifica se a alternativa D foi selecionada
if resposta.lower() == "d":
    print("Correto")
    pontos += 1
else:
    print("errado")

# Exibe a pontuação total obtida pelo jogador
print("pontos totais:", pontos)
