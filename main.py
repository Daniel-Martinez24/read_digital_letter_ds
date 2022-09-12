import numpy as np # licencia BSD
from matplotlib import pyplot as plt # licencia BSD 

def take_img(n_elem) -> list:
    file1 = open('digital_letters.csv', 'r')
    list_lett = []

    temp = n_elem
    for _ in file1:
        if n_elem == temp:
            n_elem -= 1
        else:
            lett = _.strip().split(',')
            list_lett.append([int(lett[0]) ,  [float(x) for x in lett [1:-1]], lett[-1]])

            n_elem -= 1
            if n_elem == -1:
                break
    return list_lett
    
def print_img(list_lett: list , PIX_SIZE : int ) -> None:
    fig = plt.figure(figsize=(10, 7))

    num_fig = 1
    for _el in list_lett:

        if len(list_lett) > 3:
            rows = (pow(len(list_lett) , .5))
            if rows % 2 == 0:
                colums = (rows)
            elif rows % 2 > 0.5:
                colums = rows + 2
            elif rows % 2 < 0.5:
                colums = rows + 1
            rows, colums = int(rows), int(colums)
            fig.add_subplot(rows, colums, num_fig)
        else:
            fig.add_subplot(1, len(list_lett), num_fig)
        # plt.figure(num_fig)
        num_fig += 1
        a_a = np.array(_el[1])
        plt.imshow(a_a.reshape(PIX_SIZE, PIX_SIZE))
        plt.title(_el[-1])

    plt.show()

def main(n_elem : int , PIX_SIZE : int ) -> None:
    list_lett = take_img(n_elem)
    print_img(list_lett, PIX_SIZE)

if __name__ == '__main__':
    x = 1
    while x:
        n_elem = input('¿Cuandos elementos deseas mostrar en pantalla? \n')
        try:
            n_elem = int(n_elem)
            x = False
        except ValueError:
            print('Debes introducir un numero')

    PIX_SIZE = 28 # tamaño pixeles
    main(n_elem, PIX_SIZE)
    