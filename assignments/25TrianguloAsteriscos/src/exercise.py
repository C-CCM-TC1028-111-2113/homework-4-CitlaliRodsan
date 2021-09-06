
def main():
    #Escribe tu código debajo de esta línea
    
    height = int(input("Enter triangle height: "))
    
    for i in range(height-1,-1,-1): 
        for espacio in range(i):
            print(" ", end="")
        for asterisco in range(height-i):
            print("*", end="")
        print("")
        
if __name__=='__main__':
    main()
