from unittest import TestCase
from src.leilao.dominio import Lance, Usuario, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.ri = Usuario('Ricardo', 500.0)
        self.lance_ri = Lance(self.ri, 150.0)
        self.leilao = Leilao('Celular')


    def test_deve_retornar_o_maior_valor_de_um_lance_quando_adicionado_em_ordem_crescente(self):
        gabi = Usuario('Gabi', 500.0)
        lance_gabi = Lance(gabi, 100.0)

        self.leilao.propoe(lance_gabi)
        self.leilao.propoe(self.lance_ri)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0


        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            gabi = Usuario('Gabi', 500.0)
            lance_gabi = Lance(gabi, 100.0)

            self.leilao.propoe(self.lance_ri)
            self.leilao.propoe(lance_gabi)

            menor_valor_esperado = 100.0
            maior_valor_esperado = 150.0


            self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
            self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_ri)

        self.assertEqual(150, self.leilao.menor_lance)
        self.assertEqual(150, self.leilao.maior_lance)


    def test_deve_retornar_o_maior_e_o_menos_valor_quando_o_leilao_tiver_tres_lances(self):
        gabi = Usuario('Gabi', 500.0)
        lance_gabi = Lance(gabi, 100.0)

        luna = Usuario('Luna', 500.0)
        lance_lu = Lance(luna, 200.0)

        self.leilao.propoe(lance_gabi)
        self.leilao.propoe(self.lance_ri)
        self.leilao.propoe(lance_lu)


        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0


        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)



    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lance(self):
        self.leilao.propoe(self.lance_ri)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)


    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        demar = Usuario('Demar', 500.0)

        lance_do_demar = Lance(demar, 200.0)

        self.leilao.propoe(self.lance_ri)
        self.leilao.propoe(lance_do_demar)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances_recebido)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_ri200 = Lance(self.ri, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_ri)
            self.leilao.propoe(lance_ri200)
