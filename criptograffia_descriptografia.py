""" Trabalho de criptografia para conclusão semestral - Class """

import random as rd
import numpy as np

class Criptografar:
    """ Class para criptografar mensagem """
    __slots__ = ['frase', 'chave']

    def __init__(self, frase, chave):
        self.frase = frase
        self.chave = str(chave)

    @classmethod
    def criar_matriz(cls, bloco):
        ''' função que add '¬' para completar 16 e gera os blocos '''
        bloco += " "*(16 - len(bloco))
        matriz = np.array(list(bloco)).reshape(4, 4)
        return matriz

    @classmethod
    def frase_div_16(cls, mensagem, bloco=16):
        """ função que faz listas com 16 caracteres """
        return [mensagem[i:i + bloco] for i in range(0, len(mensagem), bloco)]

    def tirar_0b_bytes(self, mensagem):
        """ converte para binario e tira os 0b """
        bytes_da_frase = bytes(mensagem.encode('utf-8'))
        frase_sem_0b = [bin(byt)[2:10] for byt in bytes_da_frase]
        return frase_sem_0b

    @classmethod
    def mensagem_xor_password(cls, mensagem_bi, pasword_bi):
        """ Função que ira realizar um xor entre a chave e os valores dos blocos """
        mensagem_xor = []
        j =0
        for bits in mensagem_bi:
            if bits == '100000':
                mensagem_xor.append(32)
            else:
                mensagem_xor.append(int(bits,2) ^ int(list(reversed(pasword_bi))[j], 2))
        return mensagem_xor

    @staticmethod
    def password_asci_bi(password):
        """  senha converte em asci dps em otal e dps em binario e tira os 0b0 """
        password_bin = [format(ord(char), '08b')[2:10] for char in password]
        return password_bin

    @classmethod
    def reverse_line_bloco(cls, matriz):
        """ Inverte a ordem das colunas e inverte a ordem dos blocos """
        return [np.array(list(reversed(m))) for m in reversed(matriz)]

    def mensagem_cifra(self, mix_blocos):
        """ Converte em letras e concatena """
        frase_resultante = ''
        for matriz in mix_blocos:
            for elemento in matriz:
                for indice in elemento:
                    if indice in (' ', 32, '32'):
                        indice = rd.randrange(35, 38)
                        frase_resultante += str(chr(int(indice)))
                    else:
                        frase_resultante += str(chr(int(indice)))
        return frase_resultante

    def realizar_criptografia(self):
        """ Uni todas as funções para de fato gerar uma cifraa """
        password_bi = self.password_asci_bi(self.chave)
        mensagem_bi = self.tirar_0b_bytes(self.frase)
        chave_xor = self.mensagem_xor_password(mensagem_bi, password_bi)
        frase_bloco_16 = self.frase_div_16(chave_xor)
        matriz = [self.criar_matriz(bloco) for bloco in frase_bloco_16]
        mix_bloco = self.reverse_line_bloco(matriz)
        cifra = self.mensagem_cifra(mix_bloco)

        return cifra

class Descriptografar:
    """Class para realizar a descriptografia da cifrada """
    __slots__ = ['msg_cifrada', 'chave', 'espaco_em_branco', 'password_bi']

    def __init__(self, msg_cifrado, chave):
        self.msg_cifrada = msg_cifrado
        self.chave = str(chave)
        self.espaco_em_branco = []
        self.password_bi = Criptografar.password_asci_bi(self.chave)

    def descriptogrfia(self, cifra):
        """ A cifra volta a ser binario """
        return [ord(c) for c in cifra]

    def cifra_xor_password(self, mix):
        """ realizar o xor com a chave e a cifra e tira os espaços em branco """
        lista_letra_bi = []
        my_slice = slice(2,10)
        for b in mix:
            for c in b:
                for d in c:
                    if d == '¬':
                        d = rd.randrange(35, 38)
                    if d in (35, 36, 37):
                        d = 32
                    lista_letra_bi.append(bin(int(d)))
        list_limpa_bi = [element[my_slice] for element in lista_letra_bi]
        return Criptografar.mensagem_xor_password(list_limpa_bi, self.password_bi)

    def deixar_texto_legivel(self, cifra):
        """ retonar um texto legivel """
        return ''.join(chr(l) for l in cifra)

    def entregar_descriptografia(self):
        """ retorna o obj descriptografado """
        new_cifra = self.descriptogrfia(self.msg_cifrada)
        cifra_div_16 = Criptografar.frase_div_16(new_cifra)
        matrizes = [Criptografar.criar_matriz(bloco) for bloco in cifra_div_16]
        mix = Criptografar.reverse_line_bloco(matrizes)
        pre_xor = self.cifra_xor_password(mix)
        texto_descriptografado = self.deixar_texto_legivel(pre_xor)

        return texto_descriptografado
