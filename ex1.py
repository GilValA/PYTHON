def main():
    #escribe tu código abajo de esta línea
    print("type first number")
    Alpha = input()
    print("type second number")
    Beta = input()

    sum = int(Alpha) + int (Beta)
    substraction = int(Alpha) - int(Beta)
    Product = int(Alpha) * int(Beta)

    print("The sum is " + str(sum))
    print(" The difference is " + str(substraction))
    print(" The product is " + str(Product))

    pass


if __name__ == '__main__':
    main()

