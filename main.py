#Initial commit
#haba
#dsiufhiasodfjksodfjko

#1 czarne 2 biale
default_array=[1,1,1,1,2,2,2,2,0]


def move():
    while True:
        print("Ruch czarnych, wybierz żeton")
        x1 = int(input())
        print("gdzie chcesz się ruszyć")
        x2 = int(input())
        if x1!=0:
            if x2==x1-1 or x2==x1+1 or x2==8:
                if default_array[x2]==0:
                    default_array[x1]=0
                    default_array[x2]=1
                else:
                    print("Przegrałeś")
                    break
            else:
                print("no nie")
        else:
            if x2==7 or x2==x1+1 or x2==8:
                if default_array[x2]==0:
                    default_array[x1]=0
                    default_array[x2]=1
                else:
                    print("Przegrałeś")
                    break
            else:
                print("no nie")
    #Ogolnie to jest szkic jak cos ale o to mi chodzilo(ta wiem najebane ifow jak u hindusa, ale chyba one zostana jakos zastapione
    # w koncu beda to przyciski)
    #i chyba juz warto te gui robic zeby zobaczyc jak to wychodzi i tutaj no by przesylalo gdzie
    #ruch zostal wykonany, nie testuje bo to szkic, te printy to wiadomo jako nowe okienka damy
    #daj znac czy takie gowno moze byc 
        print("Ruch czarnych, wybierz żeton")
        x1 = int(input())
        print("gdzie chcesz się ruszyć")
        x2 = int(input())
        if x1!=0:
            if x2==x1-1 or x2==x1+1 or x2==8:
                if default_array[x2]==0:
                    default_array[x1]=0
                    default_array[x2]=1
                else:
                    print("Przegrałeś")
                    break
            else:
                print("no nie")
        else:
            if x2==7 or x2==x1+1 or x2==8:
                if default_array[x2]==0:
                    default_array[x1]=0
                    default_array[x2]=1
                else:
                    print("Przegrałeś")
                    break
            else:
                print("no nie")
