# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import pandas as pd
import os

def pregunta_01():

    if not os.path.exists("files/output"):
        os.makedirs("files/output")

    data_test_neg = []

    #Crear lista con nombres de archivos
    list_test_negs = [ "{:04d}".format(number) for number in range(67)]
    url_test_neg = "files/input/test/negative/{}.txt"

    #Crear columna con información de cada archivo
    for num in list_test_negs:
        with open(url_test_neg.format(num),"r",encoding="utf-8") as archivo:
            linea = archivo.readline()
            data_test_neg.append(linea)
    
    #Convertirlo a Dataframe y crear columna de target
    test_neg = pd.DataFrame(data_test_neg,columns=["phrase"])
    test_neg["target"] = "negative"
    
    data_test_neu = []

    #Crear lista con nombres de archivos
    list_test_neu = [ "{:04d}".format(number) for number in range(274)]
    url_test_neu = "files/input/test/neutral/{}.txt"

    #Crear columna con información de cada archivo
    for num in list_test_neu:
        with open(url_test_neu.format(num),"r",encoding="utf-8") as archivo:
            linea = archivo.readline()
            data_test_neu.append(linea)
    
    #Convertirlo a Dataframe y crear columna de target
    test_neu = pd.DataFrame(data_test_neu,columns=["phrase"])
    test_neu["target"] = "neutral"


    data_test_pos = []

    #Crear lista con nombres de archivos
    list_test_pos = [ "{:04d}".format(number) for number in range(112)]
    url_test_pos = "files/input/test/positive/{}.txt"

    #Crear columna con información de cada archivo
    for num in list_test_pos:
        with open(url_test_pos.format(num),"r",encoding="utf-8") as archivo:
            linea = archivo.readline()
            data_test_pos.append(linea)
    
    #Convertirlo a Dataframe y crear columna de target
    test_pos = pd.DataFrame(data_test_pos,columns=["phrase"])
    test_pos["target"] = "positive"

    df_test = pd.concat(objs=[test_neg, test_neu, test_pos], axis=0)


    data_train_neg = []

    #Crear lista con nombres de archivos
    list_train_negs = [ "{:04d}".format(number) for number in range(236)]
    url_train_neg = "files/input/train/negative/{}.txt"

    #Crear columna con información de cada archivo
    for num in list_train_negs:
        with open(url_train_neg.format(num),"r",encoding="utf-8") as archivo:
            linea = archivo.readline()
            data_train_neg.append(linea)
    
    #Convertirlo a Dataframe y crear columna de target
    train_neg = pd.DataFrame(data_train_neg,columns=["phrase"])
    train_neg["target"] = "negative"
    
    data_train_neu = []

    #Crear lista con nombres de archivos
    list_train_neu = [ "{:04d}".format(number) for number in range(1117)]
    url_train_neu = "files/input/train/neutral/{}.txt"

    #Crear columna con información de cada archivo
    for num in list_train_neu:
        with open(url_train_neu.format(num),"r",encoding="utf-8") as archivo:
            linea = archivo.readline()
            data_train_neu.append(linea)
    
    #Convertirlo a Dataframe y crear columna de target
    train_neu = pd.DataFrame(data_train_neu,columns=["phrase"])
    train_neu["target"] = "neutral"


    data_train_pos = []

    #Crear lista con nombres de archivos
    list_train_pos = [ "{:04d}".format(number) for number in range(458)]
    url_train_pos = "files/input/train/positive/{}.txt"

    #Crear columna con información de cada archivo
    for num in list_train_pos:
        with open(url_train_pos.format(num),"r",encoding="utf-8") as archivo:
            linea = archivo.readline()
            data_train_pos.append(linea)
    
    #Convertirlo a Dataframe y crear columna de target
    train_pos = pd.DataFrame(data_train_pos,columns=["phrase"])
    train_pos["target"] = "positive"

    df_train = pd.concat(objs=[train_neg, train_neu, train_pos], axis=0)

    #Guardar los DataFrames en la carpeta files/output
    df_test.to_csv("files/output/test_dataset.csv", encoding="utf-8")
    df_train.to_csv("files/output/train_dataset.csv", encoding="utf-8")

    return df_train, df_test

"""
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


"""
