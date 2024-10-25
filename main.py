from functions import decoder, encoder

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
  print("option 1")
  print("option 2")
  option = int(input("Choose the option"))

  if option == 1:
    encode = encoder(alpha)
    print(f"encode word is {encode}")
    continue
  elif option == 2:
    decode = decoder(alpha)
    print(f"decode word is {decode}")
    break