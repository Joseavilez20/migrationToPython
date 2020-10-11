import random
import numpy as np
def buenamelodiaMIalv(pobinicial2,hh,mm,v,mejorTem1,vm,rr):
    testData = [9,2,3]
    testData2 = [7,6,5]
    #matrizpadres=zeros(2,v+1);
    matrizpadres = np.zeros((2, v+1), dtype=float, order='C')
    padre1 = np.zeros((1, v+1), dtype=float, order='C') #new line
    for k in range(1,3):
        #ESTO PUEDE CAMBIAR A random.uniform(0,1)
        #a = random.randint(1,hh)
        #b = random.randint(1,hh)
        a = testData[k-1]
        b = testData2[k-1]
        
        while a == b:
            b = random.randint(1,hh)
        #endwhile
        if pobinicial2[a-1,v] >= pobinicial2[b-1,v]:
            padre1[0,:] = pobinicial2[a-1,:]
        else: 
            padre1[0,:]= pobinicial2[b-1,:]
        #endif
        
        
        matrizpadres[k-1,:] = padre1
    #endfor
    pobnueva1 = np.zeros((2, v+1), dtype=float, order='C')
    pobnueva22 = np.zeros((1, v+1), dtype=float, order='C')
    #e = np.random.rand()
    e = 0.63675
    
    if e < mm:
        pobnueva22[0,:]=mejorTem1[0,:]  
    else:
        pobnueva1[0,:]= matrizpadres[0,:]
        pobnueva1[1,:]=  matrizpadres[1,:]
        
        for j in range(1, v+1):
            
            #k= random.randint(1,2)
            #####################
            if np.mod(j,2) == 0:
                k = 1
            else:
                k = 2
            #####################
           
            if k == 1:
                pobnueva22[0,j-1] = pobnueva1[0,j-1] 
            #endif
            if k == 2:
                pobnueva22[0,j-1]=pobnueva1[1,j-1]  
            #endif

        #endfor
        
        
    #endif

    for j in range(1, rr):

        #prob = np.random.uniform(0, 1, size=(1, 1))
        #####################
        if np.mod(j,2) == 1:
            prob = 0.85040
        else:
            prob = 0.11480
        #####################

        ####MODIFICATED SHAPE FOR THE CHANGE OF  40 TO 41 ###
              
        if pobnueva22.shape[1] < 41:
            pobnueva22 = np.hstack((pobnueva22,[[0]]*1))
            #v = v - 1
        
        ####vm = 0.233438
        pobnueva22[0,v] = prob
        #print("pobnueva22[0,v]:",pobnueva22[0,v])
        
        if pobnueva22[0,v] < vm: 
            
            #na = random.randint((1 +(20*(j-1))),(20*j))
            ##random('unif',-1,1) -> np.random.uniform(-1, 1, size=(1, 1)) NO TEST
            #pobnueva22[0,na-1] = np.random.uniform(-1, 1, size=(1, 1));
            #################
            if np.mod(j,2) == 1:
                na = 7
                pobnueva22[0,na-1] = -0.93007
            else:
                na = 32
                pobnueva22[0,na-1] = 0.20198
            #endif
            #################

        else:
        
    
            #mod=zeros(1,v);
            mod = np.zeros((1, v), dtype=float, order='C')
            
            mod[0,:] = pobnueva22[0,:v]
   
            #sa = random.randint(1,2)
            sa = 2 ###
            #if sa==1;
            if sa == 1:
                
                #a = random.randint(8 +(20*(j-1)), (20*j))
                a = 10 - 1
                b = a - 7
                c = a - 4
                d = a - 3
                  
                mod[0,b] = pobnueva22[0,a]
                mod[0,c] = pobnueva22[0,b]
                mod[0,d] = pobnueva22[0,c]
                mod[0,a] = pobnueva22[0,d]
         
                pobnueva22 = mod
                
                
            else:
                #a= random.randint((1 +(20*(j-1))), ((20*j)-8)) 
                a = 5 - 1 
                b = a + 7;
                c = a + 3;
                d = a + 4;
                mod[0,b] = pobnueva22[0,a];
                mod[0,c] = pobnueva22[0,d];
                mod[0,d] = pobnueva22[0,b];
                mod[0,a] = pobnueva22[0,c];  
                pobnueva22 = mod;
                
            #endif

        #endif
                
    #endfor
    
    
    
    return pobnueva22
