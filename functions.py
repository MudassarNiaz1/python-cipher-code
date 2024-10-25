
def encoder(alpha):
  user = input("Enter the text:").lower()
  shift = int(input("Enter the shift:"))

  shift = shift % 26
  encoder = ''

  for i in user:
    index = alpha.index(i) + shift
    encoder = encoder + alpha[index]
  return encoder 


def decoder(alpha):
  user = input('Enter the text:').lower()
  shift = int(input("Enter the shift:"))
  shift = shift % 26

  decoder = ''

  for i in user:
    index = alpha.index(i) - shift
    decoder = decoder + alpha[index]
  return decoder

