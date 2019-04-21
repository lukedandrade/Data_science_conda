import pandas as pd
import numpy as np



def selection(path, word, column_names):

    #criacao do dataframe pelo pandas
    #path, segundo a documentação, pode receber tanto um objeto PATH quanto string.
    #word é a palavra em questão que estamos buscando.
    #column_names deve vir em formato de lista, de forma respectiva com os dados do csv.
        #Exemplo: Se primeira coluna do arquivo é palavras, primeira posição da lista deve ser 'palavras'
    csv_dataframe = pd.read_csv(path, '|', names=column_names)

    #Método para organização do dataframe, baseado na contagem de palavras, em ordem decrescente.
        #inplace indica que a alteração está sendo feita no próprio dataframe.
    csv_dataframe.sort_values('count', inplace=True, ascending=False)

    #Método de filtragem do dataframe, restando apenas as linhas onde 'palavras' é igual à palavra desejada.
    #Como o dataframe previamente estava ordenado, o restante são as maiores ocorrências dessa palavra.
    csv_dataframe.where(csv_dataframe['palavras'] == word, inplace=True)

    #Impressão na tela das 3 primeiras linhas do dataframe.
    print(csv_dataframe.head(3))