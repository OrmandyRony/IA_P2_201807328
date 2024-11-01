# Documentación del Proyecto - IA1_Proyecto2

Este proyecto de inteligencia artificial (IA) permite a los usuarios interactuar con diversos modelos de aprendizaje automático a través de una aplicación web amigable. Los modelos implementados abarcan desde regresiones hasta clustering y redes neuronales, proporcionando una plataforma educativa y práctica para el análisis de datos.

## Introducción

La aplicación está diseñada para que el usuario cargue datos, ajuste modelos de IA y visualice los resultados de manera intuitiva. Ofrece una serie de herramientas para realizar predicciones, analizar la precisión de los modelos y observar gráficamente los resultados.

## Modelos Disponibles

El proyecto incluye varias técnicas de IA y machine learning que abordan diferentes tipos de problemas. Aquí se describe brevemente cómo funcionan y se aplican:

### 1. Regresión Lineal

La regresión lineal es un método estadístico utilizado para predecir el valor de una variable de salida en función de una o más variables de entrada. Este modelo es ideal para relaciones lineales entre las variables.

- **Funcionalidad**: El usuario puede cargar datos, ajustar el modelo y realizar predicciones. Se calculan métricas como el error cuadrático medio (MSE) y el coeficiente de determinación (R2) para evaluar el rendimiento.
- **Visualización**: Se proporciona un gráfico que muestra la línea de regresión superpuesta a los datos originales.

---

### 2. Regresión Polinomial

Este modelo es una extensión de la regresión lineal que se adapta mejor a relaciones no lineales entre las variables. Permite a los usuarios definir el grado del polinomio y ajustar el modelo en consecuencia.

- **Funcionalidad**: El usuario puede ajustar el modelo polinomial y observar cómo varía la precisión con diferentes grados. También se calculan métricas de rendimiento para analizar la efectividad del modelo.
- **Visualización**: Una curva de regresión polinomial se muestra junto con los datos originales para una comprensión más clara de la relación no lineal.

---

### 3. Árbol de Decisión ID3

El algoritmo ID3 se utiliza para clasificar datos en función de atributos específicos, construyendo un árbol de decisión basado en el concepto de entropía y ganancia de información.

- **Funcionalidad**: Los usuarios pueden cargar conjuntos de datos para entrenamiento y realizar predicciones. El árbol de decisión generado se visualiza de manera jerárquica, facilitando la interpretación de las decisiones tomadas por el modelo.
- **Visualización**: Un diagrama de árbol se presenta, mostrando cómo se toman las decisiones basadas en los atributos de los datos.

---

### 4. Redes Neuronales

Este modelo emula la estructura de las neuronas biológicas para procesar datos y aprender de manera similar al cerebro humano. Las redes neuronales son adecuadas para resolver problemas complejos que requieren la identificación de patrones.

- **Funcionalidad**: Los usuarios pueden cargar la configuración de la red y los datos de entrenamiento. La red se entrena iterativamente, ajustando los pesos para minimizar el error. Las predicciones se realizan una vez finalizado el entrenamiento.
- **Visualización**: Los resultados de las predicciones se presentan de manera clara, destacando la capacidad de la red para generalizar los datos de entrada.

---

### 5. Clustering K-Means

K-Means es un algoritmo de agrupamiento que clasifica los datos en grupos basados en su similitud. Es útil para segmentar datos sin etiquetas y descubrir patrones ocultos.

- **Funcionalidad**: Se pueden cargar datos y configurar parámetros como el número de clusters y las iteraciones. El algoritmo asigna puntos a los clusters y optimiza la agrupación para minimizar la varianza dentro de cada grupo.
- **Visualización**: Los datos se representan en un gráfico de dispersión, con puntos coloreados según el cluster al que pertenecen. Esto ayuda a visualizar cómo se agrupan los datos en función de las características definidas.

---

## Interfaz y Uso

La interfaz de usuario permite seleccionar uno de los modelos de IA disponibles mediante un menú desplegable. Cada modelo tiene una sección específica donde se pueden cargar archivos de datos, ajustar parámetros y ejecutar los algoritmos. Los resultados se muestran en gráficos y cuadros de texto, proporcionando información inmediata sobre el rendimiento del modelo.

### Pasos para Utilizar la Aplicación:

1. Seleccione el modelo de IA que desea utilizar desde el menú desplegable.
2. Cargue los archivos CSV con los datos requeridos. Asegúrese de que el formato de los datos sea el correcto.
3. Ajuste el modelo y realice las predicciones. Los botones habilitados le guiarán a través de los pasos necesarios.
4. Analice los resultados visualizados y las métricas calculadas.

## Tecnologías y Herramientas

- **Gráficos y Visualización**: Se utilizan bibliotecas gráficas para mostrar los resultados de los modelos de manera clara y efectiva.
- **Manejo de Datos CSV**: La aplicación permite la carga y procesamiento de archivos CSV para facilitar el análisis de datos sin necesidad de preprocesarlos manualmente.
- **Interactividad**: Se ha implementado un flujo interactivo para que los usuarios experimenten con diferentes modelos y parámetros.

## Consideraciones y Recomendaciones

- Es importante cargar datos en el formato correcto para evitar errores durante la ejecución.
- Algunos modelos, como las redes neuronales, pueden requerir varios intentos de entrenamiento para obtener resultados óptimos.
- Ajustar correctamente los parámetros de modelos como K-Means puede mejorar significativamente la precisión del agrupamiento.

## Contribuciones

Las contribuciones al proyecto son bienvenidas. Si desea agregar nuevas funcionalidades o mejorar las existentes, siga los procedimientos habituales para la colaboración en proyectos de código abierto.

## Licencia

El proyecto está disponible bajo una licencia de software libre, lo que permite su uso y modificación. Consulte el archivo de licencia en el repositorio para obtener más detalles.

--- 

Esta documentación proporciona una descripción clara y detallada de las capacidades del proyecto, destacando su funcionalidad, uso y potencial para el aprendizaje y la experimentación en el campo de la inteligencia artificial.