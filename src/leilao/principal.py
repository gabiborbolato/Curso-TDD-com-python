from leilao.dominio import Usuario, Lance, Leilao, Avaliador

gabi = Usuario('Gabi')
ri = Usuario('Ricardo')



lance_gabi = Lance(gabi, 100.0)
lance_ri = Lance(ri, 150.0)



leilao = Leilao('Celular')



leilao.lances.append(lance_ri)
leilao.lances.append(lance_gabi)


for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')


avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menos lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')

