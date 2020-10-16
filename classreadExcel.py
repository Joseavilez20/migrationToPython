import pandas as pd 
class ReadExcel:
    archivo = None
    matrizdatos = None
    def __init__(self):
        self.archivo = pd.read_excel('MATRIZHV2.xlsx', header=None, skiprows=1, nrows=72)
        self.matrizdatos= self.archivo.to_numpy()
    def getMatriz(self):
        return self.matrizdatos
    
    def get_archivo(self):
        return self.archivo
        
##    def copia_matriz_datos():
##        return np.copy(matrizdatos)
