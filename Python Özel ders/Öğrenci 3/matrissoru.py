import numpy as np 
def matrix_denklemi_coz(A,y):
    A = np.array(A)
    y = np.array(y)
    
    #A.shape[0] = satır sayısı
    #A.shape[1] = sutün sayısı
    
    if A.shape[0] == A.shape[1]:
        try:
            x = np.linalg.solve(A,y)
            flag = 1
            return x,flag
        except np.linalg.LinAlgError:
            pass
        
    
    x , residuals , rank ,s = np.linalg.lstsq(A,y,rcond = None)
    
    if residuals.size == 0 and rank < A.shape[1]:
        #sonsuz sayıda çözüm var 
        flag = np.inf
    elif np.allclose(A @ x,y):
        #tekil çözüm 
        flag = 1
    else:
        #çözüm yok 
        flag =  0
        x = np.full(y.shape,np.nan)
        
    return x,flag
    