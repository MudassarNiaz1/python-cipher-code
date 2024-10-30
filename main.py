from functions import Cipher


def main():
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    object = Cipher(alpha)

    while True:
        option = int(input('option (1/2): '))

        if option == 1:
            encode = object.encoder()
            print(f'Encode: {encode}')
            continue
        elif option == 2:
            decode = object.decoder()
            print(f'Decode: {decode}')
            break

if __name__ == '__main__':
    main()

