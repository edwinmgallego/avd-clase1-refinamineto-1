#Problema: Un dataset tiene valores faltantes en algunas columnas.
#Solución: Usar pandas para eliminar filas con valores faltantes o imputarlos con la media.

import pandas as pd
data = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5, None, 7, 8]})
data_cleaned = data.fillna(data.mean())
print(data_cleaned)
