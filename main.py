import numpy as np
import pandas as pd
import scipy
import pickle
import os

class cora_reader:

  def print(self):
    
    # openFile
    fcora = open(os.path.abspath(self),'rb')

    # Carrega o cora
    cora = pickle.load(fcora, encoding="latin1")

    #seta o dataFreame
    df = pd.DataFrame(cora)

    print("Dados do arquivo {}: \n".format(self [6:]))
    print(df)

if __name__ == "__main__":

  lista = ['./cfg/ind.cora.allx', './cfg/ind.cora.ally',
           './cfg/ind.cora.tx','./cfg/ind.cora.ty',
           './cfg/ind.cora.x','./cfg/ind.cora.y']

  for i in range(len(lista)):
    cora_reader.print(lista[i])