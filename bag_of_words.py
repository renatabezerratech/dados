
# OBSERVAÇÃO: é melhor fazer isso no Colab
# esse eu fiz aqui por curiosidade!

# para fazer uma matriz de frequência: 
# instale a biblioteca scikit-learn no terminal: pip install scikit-learn
# quando quiser conferir a intalação: pip show scikit-learn
# faça a importação:
from sklearn.feature_extraction.text import CountVectorizer

# instale pip install nltk
# Natural Language Toolkit (nltk) - vou importar um conjunto (uma base) de texto para trabalhar:
import nltk
from nltk.corpus import webtext

# para fazer o download do dataset:
nltk.download('webtext')

# O nlkt tem vários arquivos da web, para imprimir:
webtext.fileids()

# O resultado desse download no terminal será:
# [nltk_data] Downloading package webtext to
# [nltk_data]     C:\Users\rsbez\AppData\Roaming\nltk_data...
# O nltk está informando que iniciou o download do pacote webtext e que o arquivo será salvo no diretório C:\Users\rsbez\AppData\Roaming\nltk_data
# [nltk_data]   Unzipping corpora\webtext.zip.
# o nltk está descompactando (unzipping) o conteúdo do arquivo para que possa ser utilizado. O termo "corpora" refere-se ao conjunto de textos (corpus) que foi baixado.

# Agora abra o terminal do python:
# Ctrl+Shift+P e digite Python: Start Terminal REPL

# NO TERMINAL DO PYTHON EXECUTE OS PASSOS:
# 1 - import nltk
# 2 - from nltk.corpus import webtext
# 3 - nltk.download('webtext')
# 4 - webtext.fileids()
# O resultado será: ['firefox.txt', 'grail.txt', 'overheard.txt', 'pirates.txt', 'singles.txt', 'wine.txt']

# Criei uma variável e atribui um arquivo desse que foi dado:
# firefox = webtext.raw('firefox.txt')
# se quiser vizualizar o conteúdo, vai ver muito texto no terminal:
# basta chamar o nome da variável em um print formatado o número de linhas: print([firefox:5])


#  *******************  AGORA VAMOS TRABALHAR  ******************* 
#
#  ----> separando em frases:  frases = firefox.replace('\r', '').split('\n')

# frases = firefox.splitlines()
#
#
#
#
#
