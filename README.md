# Detector de Spam con Python

Este proyecto es una práctica donde desarrollamos una aplicación de escritorio en Python que permite analizar el texto de un correo y clasificarlo como **SPAM** o **NO SPAM** usando un modelo de Machine Learning y una interfaz gráfica hecha con **Tkinter**.

---

## ¿Qué es y qué hace la práctica? / ¿Qué aprendimos?

En esta práctica hicimos un **detector de spam** sencillo:

- El usuario escribe el contenido de un email en una caja de texto.
- Al presionar el botón **“Analizar”**, el programa manda el texto a un modelo entrenado en el módulo `spam_detector`.
- El modelo responde si ese texto tiene características de **SPAM** o **NO SPAM**, y lo mostramos en pantalla con un mensaje y un color diferente.

Con esta práctica aprendimos a:

- Trabajar con un **modelo de clasificación de texto** (spam vs no spam).
- Entrenar, evaluar y reutilizar un modelo usando funciones (`entrenar_modelo`, `evaluar_modelo`, `predecir_spam`).
- Conectar la parte de **inteligencia artificial** con una **interfaz gráfica** para que el usuario lo use de forma más amigable.
- Organizar el código en **módulos** (archivo `spam_detector.py` y archivo principal con Tkinter).
- Manejar un entorno de Python con sus dependencias usando `requirements.txt`.

---

## ¿Cómo lo hicimos? / Tecnologías–Librerías utilizadas

### 1. Proceso general de la práctica

1. Creamos la carpeta del proyecto y el repositorio (local y en GitHub).
2. Generamos un **entorno virtual** para aislar las librerías del proyecto:
   - `python -m venv venv`
   - Activamos el entorno:
     - En Windows: `venv\Scripts\activate`
3. Instalamos las dependencias desde el archivo `requirements.txt` usando:
   - `pip install -r requirements.txt`
4. Utilizamos **Git** y **GitHub** para el control de versiones:
   - `git init`, `git add .`, `git commit -m "Primer commit"`, `git push origin main`.
5. Programamos el módulo `spam_detector` donde se entrena el modelo y se definen las funciones:
   - `entrenar_modelo()`: entrena el modelo y regresa el modelo y el vectorizador de texto.
   - `evaluar_modelo(modelo, vectorizer)`: calcula la precisión del modelo.
   - `predecir_spam(texto, modelo, vectorizer)`: recibe un texto y predice si es SPAM o NO SPAM.
6. Finalmente creamos el archivo principal con Tkinter (donde está la función `main()`) para mostrar la ventana gráfica y conectar el botón con la función `analizar_email()`.

### 2. Tecnologías y librerías utilizadas

- **Python 3**: lenguaje principal del proyecto.
- **Tkinter**: para la interfaz gráfica de usuario (ventana, etiquetas, entrada de texto, botón).
- **scikit-learn (`scikit-learn==1.7.2`)**: para el modelo de Machine Learning que clasifica spam / no spam.
- **pandas (`pandas==2.3.3`)**: para cargar y manejar el conjunto de datos de correos/mensajes etiquetados.
- **numpy (`numpy==2.3.4`)**: operaciones numéricas y manejo de arreglos.
- **joblib (`joblib==1.5.2`)**: guardar y cargar el modelo entrenado (si se requiere).
- Otras librerías de apoyo:
  - `scipy`, `python-dateutil`, `pytz`, `threadpoolctl`, `tzdata`, `six`.

Todas estas dependencias están listadas en el archivo **`requirements.txt`**, lo que facilita volver a instalar el entorno en otra computadora.

### 3. Interfaz gráfica (Tkinter)

En el código principal:

- Creamos la ventana con `tk.Tk()`, establecemos el título y tamaño.
- Añadimos:
  - Un **label** de título: `"Detector de Spam"`.
  - Un **label** de instrucción: `"Escribe un email para analizar:"`.
  - Una **entrada de texto** `tk.Entry` donde el usuario escribe el contenido del correo.
  - Un **botón** `"Analizar"` que llama a la función `analizar_email()`.
  - Un **label** para mostrar el resultado: `"⚠️ SPAM"` o `"✅ NO SPAM"`.
- Antes de abrir la ventana, entrenamos el modelo y mostramos en consola la **precisión** (`accuracy`) que obtuvimos en la práctica.

---

## Trabajo futuro / Oportunidades de mejora / Solución de sus posibles errores

### Trabajo futuro y mejoras posibles

- **Mejorar el modelo**:
  - Usar un conjunto de datos más grande y más limpio (más correos etiquetados).
  - Probar diferentes algoritmos de clasificación y parámetros para subir la precisión.
- **Mejorar la interfaz**:
  - Agregar un área de texto más grande (por ejemplo `Text` en lugar de `Entry`) para correos largos.
  - Cambiar estilos, colores y fuentes para que sea más agradable.
  - Mostrar también el porcentaje de confianza de la predicción.
- **Funciones extra**:
  - Guardar un historial de correos analizados.
  - Permitir pegar directamente desde el portapapeles o cargar un archivo `.txt`.
  - Empaquetar el programa como `.exe` para que alguien lo use sin tener que instalar Python.

### Posibles errores y cómo los solucionamos

- **Error “ModuleNotFoundError: No module named 'spam_detector'”**  
  Sucede cuando el archivo `spam_detector.py` no está en la misma carpeta o el nombre está mal escrito.  
  **Solución:** revisar que el archivo esté en el mismo directorio del programa principal y que el import sea exactamente `import spam_detector`.

- **Error al importar librerías (por ejemplo scikit-learn, pandas, etc.)**  
  Normalmente pasa cuando no se activa el entorno virtual o no se instaló el `requirements.txt`.  
  **Solución:** activar el entorno con `venv\Scripts\activate` y luego ejecutar `pip install -r requirements.txt`.

- **Ventana se cierra o no aparece mensaje cuando no hay texto**  
  Se maneja validando si el usuario dejó la entrada vacía. En la función `analizar_email()` se revisa:
  ```python
  if texto == "":
      etiqueta_resultado.config(text="Por favor escribe un email")
      return
