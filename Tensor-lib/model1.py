import tensorflow as tf
from tensorflow.keras.models import Sequential # para agregar capas en secuencia
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten #1D


from tensorflow.keras.optimizers import Adam
import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def create_model():
    # Modelo más robusto con capas convolucionales
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        MaxPooling2D((2, 2)),
        
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        
        Conv2D(64, (3, 3), activation='relu'),
        
        Flatten(),#convierte esto en un vector de una sola dimensión para que pueda conectarse con las capas densas 
        Dense(64, activation='relu'),#Cada neurona está conectada a todas las entradas
        Dropout(0.5),#50% neurona apagadas
        Dense(10, activation='softmax')
    ])
    
    optimizer = Adam(learning_rate=0.001) #ajustar sus pesos durante el entrenamiento
    model.compile(
        optimizer=optimizer,
        loss='sparse_categorical_crossentropy',#medir que tan lejos están predicciones, probabilidad
        metrics=['accuracy'] # Calcula el porcentaje de predicciones correctas
    )
    return model


def prepare_image(image_path):
    """
    Prepara una imagen para la predicción con mejor preprocesamiento
    """
    # Cargar imagen
    img = Image.open(image_path)
    
    # Convertir a escala de grises
    img = img.convert('L')
    
    # Invertir colores si es necesario (MNIST usa números blancos sobre fondo negro)
    img = ImageOps.invert(img)
    
    # Aumentar el contraste
    img = ImageOps.autocontrast(img)
    
    # Redimensionar a 28x28 píxeles
    img = img.resize((28, 28), Image.LANCZOS)
    
    # Convertir a array y normalizar
    img_array = np.array(img)
    
    # Asegurar que los valores están entre 0 y 1
    img_array = img_array.astype('float32') / 255.0
    
    # Reshape para el modelo convolucional
    img_array = img_array.reshape(1, 28, 28, 1)
    
    return img_array, img

def predict_and_display(model, image_path):
    """
    Hace una predicción y muestra la imagen con el resultado
    """
    # Preparar imagen
    img_array, img = prepare_image(image_path)
    
    # Hacer predicción
    prediction = model.predict(img_array)
    digit = np.argmax(prediction[0])
    confidence = prediction[0][digit] * 100
    
    # Mostrar imagen y predicción
    plt.figure(figsize=(12, 4))
    
    # Imagen original
    plt.subplot(1, 3, 1)
    plt.imshow(Image.open(image_path))
    plt.title('Imagen Original')
    plt.axis('off')
    
    # Imagen procesada
    plt.subplot(1, 3, 2)
    plt.imshow(img, cmap='gray')
    plt.title('Imagen Procesada')
    plt.axis('off')
    
    # Gráfico de predicciones
    plt.subplot(1, 3, 3)
    bars = plt.bar(range(10), prediction[0])
    plt.title(f'Predicción: {digit}\nConfianza: {confidence:.2f}%')
    plt.xlabel('Dígito')
    plt.ylabel('Probabilidad')
    
    # Colorear la barra de la predicción
    bars[digit].set_color('red')
    
    plt.tight_layout()
    plt.show()

def main():
   
    print("Cargando y preparando el modelo...")
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
    
  
    X_train = X_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0 
    X_test = X_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0
    
    # Crear y entrenar modelo
    model = create_model()
    
    # Entrenar épocas 
    model.fit(
        X_train, y_train,
        epochs=10,
        batch_size=128,
        validation_data=(X_test, y_test),
        verbose=1 
    )
    
    # Ruta de tu imagen
    image_path = "numero6.jpg"  # Ajusta esta ruta
    
    # Predecir y mostrar resultados
    predict_and_display(model, image_path)

if __name__ == "__main__":
    main()