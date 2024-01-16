import pandas as pd


def analizar_datos(df):
    


    resumen_dict = {"Nombre": [], "Tipos de Datos Únicos": [], "% de Valores No Nulos": [], "% de Valores Nulos": [], "Cantidad de Valores Nulos": []}

    for columna in df.columns:
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        resumen_dict["Nombre"].append(columna)
        resumen_dict["Tipos de Datos Únicos"].append(df[columna].apply(type).unique())
        resumen_dict["% de Valores No Nulos"].append(round(porcentaje_no_nulos, 2))
        resumen_dict["% de Valores Nulos"].append(round(100 - porcentaje_no_nulos, 2))
        resumen_dict["Cantidad de Valores Nulos"].append(df[columna].isnull().sum())

    resumen_dataframe = pd.DataFrame(resumen_dict)
        
    return resumen_dataframe

def cantidad_porcentaje(dataframe, columna):
    
    cantidad = dataframe.shape[0]
    cantidad_columna = dataframe[columna].value_counts(dropna=False)
    porcentaje_columna = round((cantidad_columna / cantidad) * 100, 2)
    
    print(f'Los valores de {columna}:\n{cantidad_columna.to_string(header=False)}')
    print(f'\nEl porcentaje que representa cada valor:\n{porcentaje_columna.to_string(header=False)}')


def export_data_csv(ruta_nueva,dataframe):
    
    dataframe.to_csv(ruta_nueva,index=False,encoding='utf-8')
    print('El archivo se exportó con éxito')