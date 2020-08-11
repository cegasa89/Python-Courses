import random


def pintarDado(x):
    print("-----")
    print("| {x} |".format(x=x))
    print("-----")

if __name__ == "__main__":
    x = random.randint(1,6)
    pintarDado(x)


