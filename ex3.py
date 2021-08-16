def main():
    #escribe tu código abajo de esta línea
    print( "input math score")
    math = float(input())
    print(" input science score")
    science = float(input())
    print (" input geography score")
    geography = float(input())
    print (" input spanish class score")
    spanish = float(input())

    mean = (math + science + geography + spanish)/4
    print( "Your report card is:  " + 
    "  Math: " + str(math) + 
    "  Science: " + str(science) +
    "  Geography: " + str(geography) +
    "  Spanish: " + str (spanish) +
    "  Mean: " + str (mean) )
    
    
    
    
    pass


if __name__ == '__main__':
    main()
