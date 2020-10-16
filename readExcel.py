import pandas as pd
import numpy as np
import math
import timeit
##from readExcel2 import ReadExcel
from evaluacionalvr2dummi import evaluacionalvr2
from buenamelodiaMIalv import buenamelodiaMIalv
from notacromaticaMIalvmaxima import notacromaticaMIalvmaxima
from TestData import testpobinicial2, testrand1
archivo = pd.read_excel('MATRIZHV2.xlsx', header=None, skiprows=1, nrows=72)
matrizdatos= archivo.to_numpy()


##read_excel = ReadExcel()
##archivo = read_excel.get_archivo()
##matrizdatos = np.copy(read_excel.getMatriz)

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

mejor1[0,v]=-math.inf #set a value infinite negative

######
mejorTemsab1= np.zeros((1,v), dtype=float, order='C') #new line 

tic=timeit.default_timer()
toc = tic

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
        
        matrizai22 = evaluacionalvr2(pobinicial2,matrizdatos,m,rr,matrizai,t)
##        #se redeclara matrizai para que vuelva a contener zeros
##        matrizai = np.zeros((t, rr-1), dtype=float, order='C')
        manipulaMatriz = False
        for s in range(1,t+1):
            #np.insert(arr, 3, [0]*72, axis=1)
            #stack a new column with zeros data [[0]]*72 2-dimension in the last axis the array
            if  manipulaMatriz is not True:
                matrizai22 = np.hstack((matrizai22,[[0]]*72))
                manipulaMatriz = True
      
            matrizai22[s-1][rr-1] = sum(matrizai22[s-1,:t+1])
        #endfor    
            
        
        promedioai2 = np.mean(matrizai22[:,rr-1])
        ybarra2 = np.mean(matrizdatos[:,rr-1])
        K2 = ybarra2/promedioai2
        manipulaMatriz = False
        for w in range(1,t+1):
            #Note: Add in a fuction
            if  manipulaMatriz is not True and matrizdatos.shape[1] < 4:
                matrizdatos = np.hstack((matrizdatos,[[0]]*72))
                manipulaMatriz = True
                
            matrizdatos[w-1,rr] = K2*matrizai22[w-1,rr-1]
            
        #endfor    
            
        manipulaMatriz = False
        for zx in range(1,t+1):
            if  manipulaMatriz is not True and matrizdatos.shape[1] < 5:
                matrizdatos = np.hstack((matrizdatos,[[0]]*72))
                manipulaMatriz = True
                
            matrizdatos[zx-1,rr+1] =  matrizdatos[zx-1,rr-1] - matrizdatos[zx-1,rr]
        #endfor    
        manipulaMatriz = False    
        for sa in range(1,t+1):
            if  manipulaMatriz is not True and matrizdatos.shape[1] < 6:
                matrizdatos = np.hstack((matrizdatos,[[0]]*72))
                manipulaMatriz = True
                
            matrizdatos[sa-1,rr+2] = matrizdatos[sa-1,rr] - ybarra2      
        #endfor
##        print('!!SHAPE MATRIZDATOS::',matrizdatos.shape)


        sse = sum(matrizdatos[:,rr+1]**2)
        ssr = sum(matrizdatos[:,rr+2]**2)
        sst = sse + ssr
        
        R[m-1,0] = ssr / sst
       
        
    #endfor
    manipulaMatriz = False

    #pobinicial2[:,v]= R;
    ##NOTA ,puede tener problemas en otra iteración
    if  manipulaMatriz is not True:
        pobinicial2 = np.hstack((pobinicial2,R))
        manipulaMatriz = True
        
    #sort array by column specified (v)
    #orden1=sortrows(pobinicial2,v+1); in octave
    orden1 = pobinicial2[np.argsort(pobinicial2[:,v])]

    #mejorTem1=zeros(1,v+1);
    mejor = np.zeros((1, v+1), dtype=float, order='C') #new line
    mejorTem1 = np.zeros((1, v+1), dtype=float, order='C')
    mejorTem1[0,:] = orden1[hh-1,:]
    
    if mejor1[0,v] >= mejorTem1[0,v]:
        mejor[0,:] = mejor1[0,:]
    else:
        mejor[0,:] = mejorTem1[0,:]
    
    #endif
    
    
    mejor1[0,:] = mejor[0,:]
    
  
    if math.isinf(mejor1[0,v]): 
        cd = 0
    else:
        cd = 1
    #endif
    
    print('estas  en el ciclo de busqueda')
cd2=0
#while toc <= 60:
##while cd2 == 0:   
##    ta=np.random.rand()
##    
##    pobinicial2 = testpobinicial2
##   
##    #pobinicial2 = np.random.uniform(-1, 1, size=(hh, v))
##   
##    for i in range(1, ncte2+1):
##        print(i);
##        
##        R = np.zeros((hh, 1), dtype=float, order='C')
##        
##        for m in range(1, hh+1):
##           
##            matrizai22=evaluacionalvr2(pobinicial2,matrizdatos,m,rr,matrizai,t)
##        
##            
##            manipulaMatriz = False
##            for s in range(1, t+1):
##                if  manipulaMatriz is not True:
##                    matrizai22 = np.hstack((matrizai22,[[0]]*72))
##                    manipulaMatriz = True
##                matrizai22[s-1,rr-1]= sum(matrizai22[s-1,:])
##                
##            #endfor
##                
##            promedioai2=np.mean(matrizai22[:,rr-1])
##
##            ybarra2=np.mean(matrizdatos[:,rr-1])
##            K2= ybarra2/promedioai2 
##
##            manipulaMatriz = False
##            
##            for w in range(1,t+1):
##                #Note: Add in a fuction
##                if  manipulaMatriz is not True and matrizdatos.shape[1] < 4:
##                    matrizdatos = np.hstack((matrizdatos,[[0]]*72))
##                    manipulaMatriz = True
##                    
##                matrizdatos[w-1,rr] = K2*matrizai22[w-1,rr-1]
##            
##            #endfor
##                    
##            manipulaMatriz = False
##            for zx in range(1,t+1):
##                if  manipulaMatriz is not True and matrizdatos.shape[1] < 5:
##                    matrizdatos = np.hstack((matrizdatos,[[0]]*72))
##                    manipulaMatriz = True
##                    
##                matrizdatos[zx-1,rr+1] =  matrizdatos[zx-1,rr-1] - matrizdatos[zx-1,rr]
##            #endfor    
##            manipulaMatriz = False    
##            for sa in range(1,t+1):
##                if  manipulaMatriz is not True and matrizdatos.shape[1] < 6:
##                    matrizdatos = np.hstack((matrizdatos,[[0]]*72))
##                    manipulaMatriz = True
##                    
##                matrizdatos[sa-1,rr+2] = matrizdatos[sa-1,rr] - ybarra2      
##            #endfor
##           
##              
##
##            sse = sum(matrizdatos[:,rr+1]**2)
##            ssr = sum(matrizdatos[:,rr+2]**2)
##            sst = sse + ssr
##            
##            R[m-1,0] = ssr / sst
##                
##            
##        #endfor
##        
##        #pobinicial2[:,v+1]=R;
##        rows , columns = pobinicial2.shape #new line
##        manipulaMatriz = False
##        if  manipulaMatriz is not True:
##            if columns < 41:  #new line
##                pobinicial2 = np.hstack((pobinicial2,R))
##                manipulaMatriz = True
##        
##        orden1 = pobinicial2[np.argsort(pobinicial2[:,v])]
##        
##        mejor = np.zeros((1, v+1), dtype=float, order='C') #new line
##        mejorTem1 = np.zeros((1, v+1), dtype=float, order='C')
##        
##        mejorTem1[0,:] = orden1[hh-1,:]
##        
##        if mejor1[0,v] >= mejorTem1[0,v]:
##            mejor[0,:]=mejor1[0,:]
##        else:
##            mejor[0,:]=mejorTem1[0,:]
##            
##        #endif
##        mejor1[0,:]=mejor[0,:]
##
##        conteo=i
##        
##        for ll in range(1, hh+1):
##            ##x=rand(1);
##            x = testrand1[ll-1]
##            matrizdatos2 = np.copy(matrizdatos)
##            if x> pn2:
##                pobnueva22 = buenamelodiaMIalv(pobinicial2,hh,mm,v,mejorTem1,vm,rr)
##                pobinicial2[ll-1,0:v] = pobnueva22[0,0:v]
##                
##            else:
##                
##                
##                mejorTemsab1[0,0:v] = notacromaticaMIalvmaxima(pobinicial2,v,mejor1,opp,ll,matrizdatos2,matrizai,t,rr)
##                    
##                  
##                pobinicial2[ll-1,0:v]= mejorTemsab1[0,0:v];
##                
##                        
##            ##endif
##            
##
##        #endfor
##
##                
##    #endfor
##    #toc = timeit.default_timer() - tic
####    print("---------pobnueva22------------\n")
##    #print(pobnueva22)
##    cd2 = 1
###endWhile
##print(mejor)
R = np.zeros((hh, 1), dtype=float, order='C')


matrizdatosb = pd.read_excel('MATRIZHV2.xlsx', header=None, skiprows=73, usecols='A:B')
matrizdatosb= archivo.to_numpy()
xc = archivo.count()[2]  #output  
## = archivo.columns.size  #output
print(xc)
c=t+xc
op=1
ml=t

matrizhan=np.zeros((c, rr+3), dtype=float, order='C')
#84 6
for s in range(1,t+1):
    for j in range(1,(rr+3)+1):
        matrizhan[s-1,j-1]=(matrizdatos[s-1,j-1])
  
    #endfor
#endfor
for s in range(t+1,xc+t+1):
    for ss in range(1,rr):
        matrizhan[s-1,ss-1]=(matrizdatosb[op-1,ss-1])
    #endfor

    op=op+1
#endfor
matrizai33=np.zeros((t, rr-1), dtype=float, order='C')
matrizai3=np.zeros((t, rr-1), dtype=float, order='C')
m=1
matrizai3=evaluacionalvr2(mejor1,matrizhan,m,rr,matrizai33,t)

for s in range(1,t+1):
   matrizai3[s-1,rr-1]= sum(matrizai3[s-1,:])
#endfor
promedioai3=np.mean(matrizai3[:,rr-1])

ybarra3=np.mean(matrizhan[0:t-1,rr-1])
K3= ybarra3/promedioai3

matrizai44=np.zeros((t+xc, rr-1), dtype=float, order='C')
matrizai4=np.zeros((t+xc, rr-1), dtype=float, order='C')
m=1


matrizai4=evaluacionalvr2(mejor1,matrizhan,m,rr,matrizai44,c)

for s in range(1,t+xc+1):
   matrizai4[s-1,rr-1]= sum(matrizai4[s-1,:]);
#endfor
promedioai4=np.mean(matrizai4[:,rr-1]);

ybarra4=np.mean(matrizhan[0:t-1,rr-1]);
K4= ybarra4/promedioai4

for w in range(1,t+xc+1):
   matrizhan[w-1,rr]=K3*matrizai4[w-1,rr-1]
#endfor
for zx in range(1,t+xc+1):
    matrizhan[zx-1,rr+1]=  matrizhan[zx-1,rr-1]- matrizhan[zx-1,rr]
#endfor
for sa in range(1,t+xc+1):
    matrizhan[sa-1,rr+2]= matrizhan[sa-1,rr]- ybarra3;
    
#endfor
for sa in range(1,t+xc+1):
    matrizhan[sa-1,rr+2]= matrizhan[sa-1,rr]- ybarra3;
    
#endfor

sse=sum(matrizhan[:,rr+1]**2)
ssr=sum(matrizhan[:,rr+2]**2)
sst= sse + ssr
print(sst)
breakpoint()
    
         


        
  
    


