=======================
Ejecución:
=======================
Para ejecutar la aplicación primero debe hacer doble click en el archivo 'install requirements.bat', seguido a esto ejecute el archivo 'main.py' desde cualquier editor de código.
Más adelante se comprimirá en un archivo .exe
=======================
Instrucciones de uso:
=======================
1. Al ejecutar el programa aparecerá en el menú de inicio. Encontrará dos botones para dirigirse a las distintas opciones. Tambien, haciendo click en el icono superior que tiene tres lineas se abrirá una barra lateral para navegar entre las distintas opciones.
-----------------------------------------------------------------------------------------------------------
2. Si se dirige a Criptografía Cisual, encontrará el esquema Two Out of Two el cual le permitirá encriptar una imagen en dos capas que al superponerse revelarán la imagen original. Para usarlo, solo debe acceder haciendo click al botón TWO OUT OF TWO, lo que lo llevará a una pestaña donde tiene distintas opciones:
a) Cifrar: Si desea cifrar una imagen simplemente debe darle click al botón Cifrar, esto lo llevará a un cuadro de diálogo que le permitirá escoger la imagen desde el explorador de archivos. Las sub-imagenes cifradas quedarán guardadas en la carpeta "ProyectoCriptografia/Pruebas".
b) Descifrar: Si desea descifrar una imagen simplemente debe darle click al botón Desifrar esto lo llevará a un cuadro de diálogo que le permitirá escoger la imagen desde el explorador de archivos, esto ocurrirá dos veces. Primero debe escoger la capa 1 y luego la capa 2. La imagen descifrada quedará guardada en la carpeta "ProyectoCriptografia/Pruebas".
-----------------------------------------------------------------------------------------------------------
3. Si se dirige a Marca de Agua, encontrará dos opciones, una inserta la marca de agua en el dominio de frecuencias (wavelets) y la otra inserta la marca de agua en el dominio espacial.
-----------------------------------------------------------------------------------------------------------
3.1 Si se dirige al Dominio de Frecuencia encontrará dos opciones:
a) Marcar: Si desea marcar una imagen simplemente debe darle click al botón Marcar, esto lo llevará a un cuadro de diálogo que le permitirá escoger primero la imagen base y luego la imagen que desea usar como marca de agua desde el explorador de archivos. La imagen marcada se guardará en la carpeta "ProyectoCriptografia/Pruebas".
b) Extraer:  Si desea extraer la marca de agua de una imagen simplemente debe darle click al botón Extraer, esto lo llevará a un cuadro de diálogo que le permitirá escoger primero la imagen marcada y luego la imagen original desde el explorador de archivos. Además se guardará y mostrará la información obtenida en las distintas sub-bandas. Tanto la marca de agua extraída como las imagenes obtenidas con las distintas sub-bandas se guardará en la carpeta "ProyectoCriptografia/Pruebas"
-----------------------------------------------------------------------------------------------------------
3.1 Si se dirige al Dominio Espacial encontrará dos opciones:
a) Marcar: Si desea marcar una imagen simplemente debe darle click al botón Marcar, esto lo llevará a un cuadro de diálogo que le permitirá escoger primero la imagen base y luego la imagen que desea usar como marca de agua desde el explorador de archivos. La imagen marcada se guardará en la carpeta "ProyectoCriptografia/Pruebas".
b) Extraer:  Si desea extraer la marca de agua de una imagen simplemente debe darle click al botón Extraer, esto lo llevará a un cuadro de diálogo que le permitirá escoger primero la imagen marcada y luego la imagen original desde el explorador de archivos. La marca de agua extraída se guardará en la carpeta "ProyectoCriptografia/Pruebas"
-----------------------------------------------------------------------------------------------------------
4. Para cerrar o minimizar la aplicación podrá hacerlo usando los botones en la esquina superior derecha.
-----------------------------------------------------------------------------------------------------------
=======================
Información:
=======================
Para realizar la marca de agua en el dominio de frecuencia se utilizó la librería PyWavelets. La transformadas usada es la transformadas Haar por defecto sin embargo el usuario puede escoger entre algunas otras opciones con ayuda del menú desplegable.
Para trabajar las imágenes se usó la librería Pillow y Numpy para operar entre matrices.
La interfaz gráfica fue realizada usando QtDesigner.
Para la marca de agua con wavelets el programa guarda una sola imagen para todas las bandas, sería posible a futuro añadir 4 imagenes y guardar cada una en una banda distinta.


