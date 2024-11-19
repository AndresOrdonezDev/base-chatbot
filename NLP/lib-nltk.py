import nltk
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

def text_normalization_demo():
    # Texto de ejemplo
    text = "Los estudiantes están corriendo rápidamente en el parque mientras juegan y aprenden nuevas habilidades."
    
    # Tokenización del texto
    tokens = word_tokenize(text, language='spanish')
    
    # Inicializar el stemmer para español
    spanish_stemmer = SnowballStemmer('spanish')
    
    print("Texto original:", text)
    print("\nTokens y Stemming en español:")
    
    for token in tokens:
        stemmed = spanish_stemmer.stem(token)
        print(f"Original: {token} → Raíz: {stemmed}")


text_normalization_demo()