#12 f
#11 s

class Matrix:
    """dostring"""

    def __init__(self, x, y):
        """Constructor"""
        self.x = x
        self.y = y
        self.matr = [[1]*x] * y


    def printmatr(self):
        for i in range(0, self.x):
            for j in range(0, self.y):
                print(f"{self.matr[i][j]} ", end = "")
            print()


    def izmenenie(self, newY, newX):
        oldX = self.x
        oldY = self.y
        newmatr = self.matr
        x = newX
        y = newY
        if (oldX < x):
            nX = x - oldX
            for i in range(0, nX):
                newmatr.append([0] * x)
        else:
            nX = oldX - x
            for j in range (1, nX + 1):
                del newmatr[oldX-nX]
        if (oldY < y):
            nY = y - oldY
            for i in range(0, nY):
                newmatr[i].append(0)
        else:
            nY = oldY - y
            for j in range(0, nY):
                del newmatr[j][oldY-j-1]
        self.x = x
        self.y = y
        self.matr = newmatr

    def podmatr(self, x, y):
        for i in range(0, x):
            for j in range(0, y):
                print(f"{self.matr[i][j]} ", end = "")
            print()



def get_input():
    while True:
        try:
            return int(input("X:"))
        except Valueint as exc:
            print("Not int")


def print_output(y):
    print(f"{y}")

    
    
    
def main():
    while True:

        print("1. Создание матрицы")
        print("2. Просмотр матрицы")
        print("3. Изменение размерности матрицы")
        print("4. Методы класса")
        print("5. Вывод подматрицы")
        print("0. Выход")

        cmd = input("Выберите пункт: ")
        if cmd == "1":
            x = get_input() 
            y = get_input() 
            matrx = Matrix(x, y)
        elif cmd == "2":
            matrx.printmatr()
        elif cmd == "3":
            x = get_input() 
            y = get_input() 
            matrx.izmenenie(x, y)
            matrx.printmatr()            
        elif cmd == "4":
            print(dir(matrx))
        elif cmd == "5":
            x = get_input() 
            y = get_input() 
            matrx.podmatr(x, y)
        elif cmd == "0":
            break
        else:
            print("Вы ввели не правильное значение")


if __name__ == "__main__":
    main()
