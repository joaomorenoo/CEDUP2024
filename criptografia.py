import base64

class Cryp:
    def __init__(self, mensagem_original="", mensagem_criptografada=''):
        self.mensagem_original = mensagem_original
        self.mensagem_criptografada = mensagem_criptografada

    def criptografia(self):
        mensagem_bytes = self.mensagem_original.encode('ascii')
        base64_bytes = base64.b64encode(mensagem_bytes)
        base64_mensagem = base64_bytes.decode('ascii')
        self.mensagem_criptografada = base64_mensagem
        print(f'Frase criptografada: {base64_mensagem}')

    def descriptografar(self):
        Dbase64_bytes = self.mensagem_criptografada.encode('ascii')
        mensagem_descriptografada = base64.b64decode(Dbase64_bytes)
        self.mensagem_descripto = mensagem_descriptografada.decode('ascii')
        print(f'{self.mensagem_descripto}')    

if __name__ == '__main__':
    primeira_mensagem = Cryp("estudar python com o professor mais lindo do mundo")
    primeira_mensagem.criptografia()
    primeira_mensagem.descriptografar()
    