import numpy as np
def calculate(liste):
  dict={}
  
  if len(liste) < 9:
    raise ValueError("List must contain nine numbers.")
  else:
    array=np.array(liste).reshape(3,3)
    dict['mean']=[list(array.mean(axis=0)),list(array.mean(axis=1)),array.mean()]
    dict['variance']=[list(array.var(axis=0)),list(array.var(axis=1)),array.var()]
    dict['standard deviation']=[list(array.std(axis=0)),list(array.std(axis=1)),array.std()]
    dict['max']=[list(array.max(axis=0)),list(array.max(axis=1)),array.max()]
    dict['min']=[list(array.min(axis=0)),list(array.min(axis=1)),array.min()]
    dict['sum']=[list(array.sum(axis=0)),list(array.sum(axis=1)),array.sum()]
    
    return dict



    
    
    
    
    
    
   