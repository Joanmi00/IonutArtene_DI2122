
x=[1,2,3,4,20,45,34,25,67,12]

   

llista_par=list(filter(lambda x: x%2==0,x))  
llista_impar=list(filter(lambda x2: x2%2!=0,x))
        
  
print(llista_par)
print(llista_impar)
