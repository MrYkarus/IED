def Torre_Hanoi(discos , inicial="1", final="3", auxiliar="2"):
    
    if discos==1:
        print ("Mover disco 1 do pino",inicial,"para o pino",final)
    else:
        
        Torre_Hanoi(discos-1, inicial, auxiliar, final)
        print ("mova o disco",discos,"do pino",inicial,"para o pino",final)
        Torre_Hanoi(discos-1, auxiliar, final, inicial)

print("informe o numero de discos")
discos = int(input())
Torre_Hanoi(discos)