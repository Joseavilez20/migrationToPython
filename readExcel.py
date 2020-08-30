import pandas as pd
import numpy as np
from evaluacionalvr2dummi import evaluacionalvr2
from TestData import testpobinicial2
archivo = pd.read_excel('MATRIZHV2.xlsx', header=None, skiprows=1, nrows=72)
matrizdatos= archivo.to_numpy()

t = archivo.count()[2]  #output 72 
rr = archivo.columns.size  #output 3
 

#matrizai=zeros(t,(rr-1)); #output array dimension 72x2  with zeros

matrizai = np.zeros((t, rr-1), dtype=float, order='C')
matrizai2= np.zeros((t, rr-1), dtype=float, order='C')
matrizai22= np.zeros((t, rr-1), dtype=float, order='C')

v=(rr-1)*20; #output 40

ncte1=5
ncte2=30

hh=10
mm=0.552618
vm=0.233438
 
pn2=0.0971352
opp=0.483767
jk2=50
ww=jk2
jk=ww
ni=6

cont=1
c4=0

#mejor1=zeros(1,v+1); #output array dimension 1x41 with zeros
mejor1 = np.zeros((1, v+1), dtype=float, order='C')

#mejor1(1,1:v+1)=random('unif',-1,1,1,v+1); #output aleatory number with uniform distribution
mejor1 = np.random.uniform(-1, 1, size=(1, v+1))

#mejor1(1,v+1)=-inf; #set a value infinite negative
cd=0

#manipulaMatriz = False
while cd == 0:
    #pobinicial2=random('unif',-1,1,hh,v); #output aleatory number with uniform distribution, 10x40
    #pobinicial2 = np.random.uniform(-1, 1, size=(hh, v))
    pobinicial2 = testpobinicial2
    print("BUSQUEDA");
    #R=zeros(hh,1); #array dimension 10x1 with zeros
    R = np.zeros((hh, 1), dtype=float, order='C')
    #for  m=1:hh
    for m in range(1,hh+1):
        
        matrizai22 = evaluacionalvr2(pobinicial2,matrizdatos,m,rr,matrizai,t);
        manipulaMatriz = False
        for s in range(1,3):
            #np.insert(arr, 3, [0]*72, axis=1)
            #stack a new column with zeros data [[0]]*72 2-dimension in the last axis the array
            if  manipulaMatriz is not True:
                matrizai22 = np.hstack((matrizai22,[[0]]*72))
                manipulaMatriz = True
      
            matrizai22[s-1][rr-1] = sum(matrizai22[s-1,:t+1])
            
            
        
        promedioai2 = np.mean(matrizai22[:,rr-1])
        ybarra2 = np.mean(matrizdatos[:,rr-1])
        K2 = ybarra2/promedioai2
        manipulaMatriz = False
        for w in range(1,t+1):
            #Note: Add in a fuction
            if  manipulaMatriz is not True:
                matrizdatos = np.hstack((matrizdatos,[[0]]*72))
                manipulaMatriz = True
                
            matrizdatos[w-1,rr] = K2*matrizai22[w-1,rr-1]
            
            
        manipulaMatriz = False
        for zx in range(1,t+1):
            if  manipulaMatriz is not True:
                matrizdatos = np.hstack((matrizdatos,[[0]]*72))
                manipulaMatriz = True
                
            matrizdatos[zx-1,rr+1] =  matrizdatos[zx-1,rr-1] - matrizdatos[zx-1,rr]
            
        manipulaMatriz = False    
        for sa in range(1,t+1):
            if  manipulaMatriz is not True:
                matrizdatos = np.hstack((matrizdatos,[[0]]*72))
                manipulaMatriz = True
                
            matrizdatos[sa-1,rr+2] = matrizdatos[sa-1,rr] - ybarra2      
            

        sse = sum(matrizdatos[:,rr+1]**2)
        ssr = sum(matrizdatos[:,rr+2]**2)
        sst = sse + ssr
        
        R[m-1,0] = ssr / sst
        print (R[m-1,0])
        print ("--------------------\n")
    cd = 1      


        
  
    


