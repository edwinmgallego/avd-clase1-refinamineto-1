import os
import pandas as pd

def clean_data(file):
    # Leer el archivo CSV
    data = pd.read_csv(file)

    # Eliminar filas con valores nulos
    data = data.dropna()

    # Filtrar solo las columnas numéricas
    numeric_data = data.select_dtypes(include=['number'])

    # Calcular los cuartiles e IQR
    Q1 = numeric_data.quantile(0.25)
    Q3 = numeric_data.quantile(0.75)
    IQR = Q3 - Q1

    # Eliminar los outliers
    numeric_data = numeric_data[~((numeric_data < (Q1 - 1.5 * IQR)) | (numeric_data > (Q3 + 1.5 * IQR))).any(axis=1)]

    # Reintegrar las columnas no numéricas
    cleaned_data = numeric_data.join(data.select_dtypes(exclude=['number']))

    return cleaned_data

directory = 'C:/Users/cript/OneDrive/Documentos/tecnalia_analisis de datos/clase-1/avd-clase1-refinamineto-1/example_csv_files'

for file in os.listdir(directory):
    if file.endswith('.csv'):
        cleaned_data = clean_data(os.path.join(directory, file))
        cleaned_data.to_csv(f'cleaned_{file}', index=False)
