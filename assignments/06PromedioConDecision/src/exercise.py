def main():
    #escribe tu código abajo de esta línea
    
    num=0
    suma=0
    n=0
    while num>=0:  
        
        num=float(input())
        if num>=0: 
            suma=suma+num
            n=n+1
        else:
            break

    promedio=suma/n
    print(promedio)
    
if __name__=='__main__':
    main()
