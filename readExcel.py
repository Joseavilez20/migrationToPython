import pandas as pd
import numpy
from evaluacionalvr2dummi import evaluacionalvr2
from TestData import testpobinicial2
archivo = pd.read_excel('MATRIZHV2.xlsx', header=None, skiprows=1, nrows=72)
matrizdatos= archivo.to_numpy()
print(testpobinicial2[0][0])
print(testpobinicial2[0][20])


t = archivo.count()[2]  #output 72 
rr = archivo.columns.size  #output 3

#matrizai=zeros(t,(rr-1)); #output array dimension 72x2  with zeros

matrizai = numpy.zeros((t, rr-1), dtype=float, order='C')
matrizai2= numpy.zeros((t, rr-1), dtype=float, order='C')
matrizai22= numpy.zeros((t, rr-1), dtype=float, order='C')

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
mejor1 = numpy.zeros((1, v+1), dtype=float, order='C')

#mejor1(1,1:v+1)=random('unif',-1,1,1,v+1); #output aleatory number with uniform distribution
mejor1 = numpy.random.uniform(-1, 1, size=(1, v+1))

#mejor1(1,v+1)=-inf; #set a value infinite negative
cd=0

while cd == 0:
    #pobinicial2=random('unif',-1,1,hh,v); #output aleatory number with uniform distribution, 10x40
    #pobinicial2 = numpy.random.uniform(-1, 1, size=(hh, v))
    pobinicial2 = testpobinicial2
    print("BUSQUEDA");
    #R=zeros(hh,1); #array dimension 10x1 with zeros
    R = numpy.zeros((hh, 1), dtype=float, order='C')
    #for  m=1:hh
    for m in range(1,hh+1):
       
        evaluacionalvr2(pobinicial2,matrizdatos,m,rr,matrizai,t);
    cd = 1      


        
  
    


