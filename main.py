def main():
    pass

if __name__ == '__main__':
    x = 1
    while x:
        n_elem = input('¿Cuandos elementos deseas mostrar en pantalla? \n')
        try:
            n_elem = int(n_elem)
            x = False
        except ValueError:
            print('Debes introducir un numero')
    PIX_SIZE = 28
    main()
    