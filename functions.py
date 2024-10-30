
class Cipher:
    def __init__(self, alpha):
        self.alpha = alpha

    def encoder(self):
        user_input = input("Enter your text: ").lower()
        shift = int(input("Enter your shift: "))
        shift = shift%26
        encoder = ''
        for i in user_input:
            index = self.alpha.index(i) + shift
            encoder = encoder + self.alpha[index]
        return encoder


    def decoder(self):
        user_input = input("Enter your text: ").lower()
        shift = int(input("Enter your shift: "))
        shift = shift%26

        decoder=''
        for i in user_input:
            index = self.alpha.index(i) - shift
            decoder = decoder + self.alpha[index]
        return decoder




