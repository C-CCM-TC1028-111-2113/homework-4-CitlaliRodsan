

def main():
    #Escribe tu código debajo de esta línea
    
   num = int(input("Escribe un numero : "))
    
    for i in range(-1,num+1):
        pow=i*i
        if pow>num:
            print(i)
            break

if __name__=='__main__':
    main()
