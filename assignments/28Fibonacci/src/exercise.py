
def main():
    #escribe tu código abajo de esta línea
    
    index = int(input("Enter the index: "))
    inicio=0
    sig=1
    if index==0:
        print("0")
    else: 
        for i in range(index-1):
            acumulado=inicio+sig
            inicio=sig
            sig=acumulado
        print(sig)

if __name__=='__main__':
    main()
