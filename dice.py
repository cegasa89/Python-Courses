import random


def pintarDado(x):
    print("-----")
    print("| {x} |".format(x=x))
    print("-----")

def pintarDado2(x):
    print("-------------")
    switch (x) {
        case 1:
            print("|         |")
            print("|    O    |")
            print("|         |")
        
        }
    print("-------------")

if __name__ == "__main__":
    x = random.randint(1,6)
    pintarDado(x)
    pintarDado2(x)

