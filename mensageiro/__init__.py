class CanalDeMensagem:
    def enviar_msg(self, msg):
        raise NotImplementedError('Você deve implementar esse método')


class Email(CanalDeMensagem):
    def enviar_msg(self, msg):
        return 'Enviando email: %s' % msg


class SMS(CanalDeMensagem):
    def enviar_msg(self, msg):
        return 'Enviando SMS: %s' % msg


class Telegram(CanalDeMensagem):
    def enviar_msg(self, msg):
        return 'Enviando por Telegram: %s' % msg


class Mensageiro:
    lista_de_canais = [Email(), SMS(), Telegram()]

    def enviar(self, msg):
        lst = []
        for canal in self.lista_de_canais:
            lst.append(canal.enviar_msg('Uma mensagem'))
        return lst


if __name__ == '__main__':
    lista_de_canais = [Email(), SMS(), Telegram()]
    for canal in lista_de_canais:
        canal.enviar_msg('Uma mensagem')
