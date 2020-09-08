import random
import numpy as np
def buenamelodiaMIalv(pobinicial2,hh,mm,v,mejorTem1,vm,rr):
    testData = [9,2,3]
    testData2 = [7,6,5]
    #matrizpadres=zeros(2,v+1);
    matrizpadres = np.zeros((2, v+1), dtype=float, order='C')
    padre1 = np.zeros((1, v+1), dtype=float, order='C') #new line
    for k in range(1,3):
        #a = random.randint(1,hh)
        #b = random.randint(1,hh)
        a = testData[k-1]
        b = testData2[k-1]
        print(a)
        print(b)
        while a == b:
            b = random.randint(1,hh)
        #endwhile
        if pobinicial2[a-1,v] >= pobinicial2[b-1,v]:
            padre1[0,0:v] = pobinicial2[a-1,0:v];
        else: 
            padre1[0,0:v]= pobinicial2[b-1,0:v];
        #endif
        matrizpadres[k-1,:] = padre1;
    #endfor
    print(padre1)
    return pobnueva22
