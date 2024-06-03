# Application-for-image-watermarks-and-visual-cryptography
This application allows the user to encrrypt image and insert watermarks

=======================
Execution:
=======================
To run the application you must first double click on the 'install requirements.bat' file, followed by running the 'main.py' file from any code editor.
Later it will be compressed into an .exe file
=======================
Instructions for use:
=======================
1. When you run the program it will appear in the start menu. You will find two buttons to go to the different options. Also, clicking on the top icon that has three lines will open a sidebar to navigate between the different options.
-------------------------------------------------- -------------------------------------------------- -------
2. If you go to Cisual Cryptography, you will find the Two Out of Two scheme which will allow you to encrypt an image in two layers that, when superimposed, will reveal the original image. To use it, you just have to access it by clicking on the TWO OUT OF TWO button, which will take you to a tab where you have different options:
a) Encrypt: If you want to encrypt an image you simply have to click on the Encrypt button, this will take you to a dialog box that will allow you to choose the image from the file explorer. The encrypted sub-images will be saved in the "Cryptography Project/Tests" folder.
b) Decrypt: If you want to decrypt an image you simply have to click on the Decrypt button this will take you to a dialog box that will allow you to choose the image from the file explorer, this will happen twice. First you must choose layer 1 and then layer 2. The decrypted image will be saved in the "Cryptography Project/Tests" folder.
-------------------------------------------------- -------------------------------------------------- -------
3. If you go to Watermark, you will find two options, one inserts the watermark in the frequency domain (wavelets) and the other inserts the watermark in the spatial domain.
-------------------------------------------------- -------------------------------------------------- -------
3.1 If you go to the Frequency Domain you will find two options:
a) Mark: If you want to mark an image you simply have to click on the Mark button, this will take you to a dialog box that will allow you to first choose the base image and then the image you want to use as a watermark from the file explorer. The marked image will be saved in the "Cryptography Project/Tests" folder.
b) Extract: If you want to extract the watermark from an image you simply have to click on the Extract button, this will take you to a dialog box that will allow you to first choose the marked image and then the original image from the file explorer. In addition, the information obtained in the different sub-bands will be saved and displayed. Both the extracted watermark and the images obtained with the different sub-bands will be saved in the "Cryptography Project/Tests" folder.
-------------------------------------------------- -------------------------------------------------- -------
3.1 If you go to the Spatial Domain you will find two options:
a) Mark: If you want to mark an image you simply have to click on the Mark button, this will take you to a dialog box that will allow you to first choose the base image and then the image you want to use as a watermark from the file explorer. The marked image will be saved in the "Cryptography Project/Tests" folder.
b) Extract: If you want to extract the watermark from an image you simply have to click on the Extract button, this will take you to a dialog box that will allow you to first choose the marked image and then the original image from the file explorer. The extracted watermark will be saved in the "Cryptography Project/Tests" folder
-------------------------------------------------- -------------------------------------------------- -------
4. To close or minimize the application you can do so using the buttons in the upper right corner.
-------------------------------------------------- -------------------------------------------------- -------
=======================
Information:
=======================
To perform the watermark in the frequency domain, the PyWavelets library was used. The transform used is the default Haar transform, however the user can choose between some other options with the help of the drop-down menu.
To work on the images, the Pillow library and Numpy were used to operate between matrices.
The graphical interface was made using QtDesigner.
For the watermark with wavelets, the program saves a single image for all bands. It would be possible in the future to add 4 images and save each one in a different band.
