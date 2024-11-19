from nltk.stem import SnowballStemmer

def demonstrate_spanish_stemmer():
    # Crear el stemmer para español
    spanish_stemmer = SnowballStemmer('spanish')
    
    # Lista de palabras de ejemplo
    words = [
        "caminando", "caminar", "caminante", "caminantes",  # Familia de 'caminar'
        "estudiantes", "estudiante", "estudiar", "estudioso",  # Familia de 'estudiar'
        "computadoras",  "computadora","computación",  # Familia de 'computadora'
    ]
    
    print("Demostración de Stemming en español:")
    print("-" * 50)
    
    # Procesar cada palabra
    for word in words:
        stem = spanish_stemmer.stem(word)
        print(f"Palabra original: {word:15} -> Raíz: {stem}")
    


    # Mostrar idiomas disponibles
    #print("\nIdiomas disponibles en SnowballStemmer:")
    #print(SnowballStemmer.languages)

# Ejecutar la demostración
demonstrate_spanish_stemmer()