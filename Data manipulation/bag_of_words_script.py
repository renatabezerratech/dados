from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import webtext

# Aqui você carrega o arquivo firefox.txt e salva ele na variável
firefox = webtext.raw('firefox.txt') #Dado bruto

# Remove todos os caracteres '\r'
newArq = firefox.replace('\r', '') #Tratamento de caracter indesejado

# Salva o conteúdo processado em um novo arquivo
try:
    with open('newArq.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(newArq)
    print("Arquivo newArq.txt salvo com sucesso!")
except Exception as e:
    print(f"(newArq.txt) Ocorreu um erro: {e}")

# Divide o conteúdo em documentos (por exemplo, por linhas)
documentos = newArq.splitlines()  # Isso cria uma lista de strings, uma para cada linha do texto

# Inicializa o CountVectorizer
vectorizer = CountVectorizer()

# Ajusta o vectorizer ao conjunto de documentos
try:
    vocabulario = vectorizer.fit(documentos) # Contagem de qtd de cada palavra

    with open('vocabulario.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(str(vocabulario.vocabulary_)) # Vocabulario de frequencia de palavras 
    print("Arquivo vocabulario.txt salvo com sucesso!")

    matriz = vectorizer.transform(documentos) #Tranformação de vocabulario em matriz
    print("Matriz de características criada com sucesso!") 

    # Salva a forma da matriz em um arquivo
    with open('matriz.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(str(matriz.shape))  # Quantidade de linhas e colunas gerados na matriz de dados
    print("Arquivo matriz.txt salvo com sucesso!")
except Exception as e:
    print(f"(matriz.txt) Ocorreu um erro: {e}")
