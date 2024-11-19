import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('all')  # Descargamos el recurso para tokenización

# Texto de ejemplo
texto = """
El procesamiento de lenguaje natural es una rama de la inteligencia artificial que estudia la forma en que las computadoras pueden interpretar y comprender el lenguaje humano. NLP se utiliza en aplicaciones como chatbots, análisis de sentimientos, y motores de búsqueda.
"""

# Tokenizar el texto en palabras
palabras = word_tokenize(texto.lower())  # Convertimos a minúsculas para evitar duplicados por mayúsculas

# Contar la frecuencia de cada palabra
frecuencia_palabras = Counter(palabras)

# Mostrar las palabras y su frecuencia
print("Frecuencia de palabras:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"{palabra}: {frecuencia}")