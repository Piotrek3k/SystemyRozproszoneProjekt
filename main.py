# 1 czarne 2 biale
default_array = [1, 1, 1, 1, 2, 2, 2, 2, 0]


def move():
    while True:
        print("Ruch czarnych, wybierz żeton")
        x1 = int(input())
        print("Wybierz gdzie chcesz się poruszyć")
        x2 = int(input())
        
        if x1 != 0:
            if x2 == x1 - 1 or x2 == x1 + 1 or x2 == 8:
                if default_array[x2] == 0:
                    default_array[x1] = 0
                    default_array[x2] = 1
                else:
                    print("Przegrałeś")
                    break
            else:
                print("Brak możliwości")
        else:
            if x2 == 7 or x2 == x1 + 1 or x2 == 8:
                if default_array[x2] == 0:
                    default_array[x1] = 0
                    default_array[x2] = 1
                else:
                    print("Przegrałeś")
                    break
            else:
                print("Brak możliwości")

        print("Ruch białych, wybierz żeton")
        x1 = int(input())
        print("Wybierz gdzie chcesz się poruszyć")
        x2 = int(input())

        if x1 != 0:
            if x2 == x1 - 1 or x2 == x1 + 1 or x2 == 8:
                if default_array[x2] == 0:
                    default_array[x1] = 0
                    default_array[x2] = 2
                else:
                    print("Przegrałeś")
                    break
            else:
                print("Brak możliwości")
        else:
            if x2 == 7 or x2 == x1 + 1 or x2 == 8:
                if default_array[x2] == 0:
                    default_array[x1] = 0
                    default_array[x2] = 2
                else:
                    print("Przegrałeś")
                    break
            else:
                print("Brak możliwości")
