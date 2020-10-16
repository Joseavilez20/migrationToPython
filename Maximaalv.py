import numpy as np

from evaluacionalvr2dummi import evaluacionalvr2
def maximaalv(pobinicial,e,v,u,z1,matrizdatos,matrizai,t,rr,ll):
##    print('**************COMPROBAR MATRIZDATOS******************')
##    print(np.allclose(matrizdatos,matrizdatos2))
##    breakpoint()
    
    if e>=z1 and  e<=(z1 + 0.25): 
        a = z1
        b = e
        c = z1 + 0.25
    #endif
    if e>=(z1+0.25) and  e<=(z1 + 0.5): 
        a = z1 + 0.25
        b = e
        c = z1 + 0.5
    #endif    
    primero = np.zeros((2, v+1), dtype=float, order='C')
    primero[0,:] = pobinicial[ll-1,:]
    primero[1,:] = pobinicial[ll-1,:]
    #primero[0,u-1] = np.random.uniform(a, b, size=(1,1))
    #primero[1,u-1] = np.random.uniform(b, c, size=(1,1))
    primero[0,u-1] = 0.315473
    primero[1,u-1] = 0.440822
    #primero( 1,u): -0.943167
    #primero( 2,u): -0.750958
    
    busqueda = np.zeros((2, v), dtype=float, order='C')

    busqueda[0,:] = primero[0,0:v]
    busqueda[1,:] = primero[1,0:v]
    
    
    R = np.zeros((2,1), dtype=float, order='C')


    for m in range(1,3):
      

        matrizai = evaluacionalvr2(busqueda,matrizdatos,m,rr,matrizai,t);

           
        rows , columns = matrizai.shape #new line
        manipulaMatriz = False
        for s in range(1,t+1):
            if columns < 3:  #new line
                if  manipulaMatriz is not True:
                    matrizai = np.hstack((matrizai,[[0]]*72))
                    manipulaMatriz = True
            matrizai[s-1,rr-1] = sum(matrizai[s-1,:])
                
        #endfor
        
        
        promedioai = np.mean(matrizai[:,rr-1])
        ybarra = np.mean(matrizdatos[:,rr-1])
        K = ybarra/promedioai

        for w in range(1,t+1):
            matrizdatos[w-1,rr] = K*matrizai[w-1,rr-1]
        #endfor


        for zx in range(1,t+1):
            matrizdatos[zx-1,rr+1] =  matrizdatos[zx-1,rr-1] - matrizdatos[zx-1,rr]
        #endfor


        for sa in range(1,t+1):
            matrizdatos[sa-1,rr+2]= matrizdatos[sa-1,rr] - ybarra
            
        #endfor
        

        sse = sum(matrizdatos[:,rr+1]**2)
        ssr = sum(matrizdatos[:,rr+2]**2)
        sst = sse + ssr

        R[m-1,0] = ssr /sst
         
    #endfor
    
         
        
##    #busqueda[:,v+1] = R

    rows , columns = busqueda.shape #new line
    manipulaMatriz = False
   
##    if  manipulaMatriz is not True:
    if columns < 41:  #new line
        busqueda = np.hstack((busqueda,[[0]]*2))
##            manipulaMatriz = True
    busqueda[:,v:] = R

    orden111 = busqueda[np.argsort(busqueda[:,v])]
    
    
    mejorTem111 = np.zeros((1,v+1), dtype=float, order='C')

    mejorTem111[0,0:v-1] = orden111[orden111.shape[0]-1,0:v-1]
    pobinicial = mejorTem111
             
    mas = pobinicial
   
    return mas
