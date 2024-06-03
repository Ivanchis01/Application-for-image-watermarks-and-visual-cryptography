from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
from PyQt5 import QtGui
import cv2
import imutils
import sys
import visualCrypt,watermark

class MainGui(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("troncriptos.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton_2.clicked.connect(lambda: MainApp.exit())
        self.pushButton.clicked.connect(lambda: self.showMinimized())
        self.frame_2.mouseMoveEvent = self.MoveWindow

        self.stackedWidget.setCurrentWidget(self.inicio)
##SIDE BAR===============================================================================================================
        self.toolButton.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.inicio))
        self.toolButton_5.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clave))
        self.toolButton_6.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.firma))
##=======================================================================================================================
##INICIO=================================================================================================================

        self.toolButton_10.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clave))
        self.toolButton_11.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.firma))
##=======================================================================================================================
##=======================================================================================================================
##CLAVE PUBLICA==========================================================================================================
        self.toolButton_24.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.clRsa))
##=======================================================================================================================
##FIRMA DIGITAL==========================================================================================================
        self.toolButton_27.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.fiDsa))
        self.toolButton_28.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.fiGamal))
##=======================================================================================================================
##Ocultar SIDEBAR========================================================================================================
        self.toolButton_4.clicked.connect(lambda: self.Side_Menu_Def_0())
        self.frame_5.mousePressEvent = self.Side_Menu_Def_1
        self.clave.mousePressEvent = self.Side_Menu_Def_1
        self.firma.mousePressEvent = self.Side_Menu_Def_1

        self.clRsa.mousePressEvent = self.Side_Menu_Def_1
        self.fiDsa.mousePressEvent = self.Side_Menu_Def_1
        self.fiGamal.mousePressEvent = self.Side_Menu_Def_1

        self.pushButton_6.mousePressEvent = self.Side_Menu_Def_1

##==========================================Conectar botones===========================================================
##Rsa========================================================================================================
        self.rsaCifrar.clicked.connect(self.rsaBCifrar)
        self.rsaDescifrar.clicked.connect(self.rsaBDescifrar)
##FirmaDigitalDsa========================================================================================================
        self.fiDsaCifrar.clicked.connect(self.dsaBFirmar)
        self.fiDsaDescifrar.clicked.connect(self.dsaBVerificar)
##FirmaDigitalGamal========================================================================================================
        self.fiGamCifrar.clicked.connect(self.gamalfiFirmar)
        self.fiGamDescifrar.clicked.connect(self.gamalfiVerificar)
##=======================================================================================================================        
##=====================================FUNCIONES DE BOTONES Y CAMPOS DE TEXTO============================================
##=======================================================================================================================
        
##=======================================================================================================================
##toot=================================================================================================================== 
    def tootCargarImagen(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image)
        return(self.filename)
    def tootCargarImagen1_1(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto2(self.image)
        return(self.filename)
    def tootCargarImagen1_2(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto3(self.image)
        return(self.filename)
    
    def tootCargarImagen2(self,filename):
        self.image = cv2.imread(filename)
        self.setPhoto2(self.image)
    def tootCargarImagen3(self,filename):
        self.image = cv2.imread(filename)
        self.setPhoto3(self.image)
    def tootCargarImagen4(self,filename):
        self.image = cv2.imread(filename)
        self.setPhoto4(self.image)


    def rsaBCifrar(self):
        path=self.tootCargarImagen()
        visualCrypt.TwoOutOfTwo.create_shares(path)
        self.tootCargarImagen2('Prueba/share1.png')
        self.tootCargarImagen3('Prueba/share1.png')

    def rsaBDescifrar(self):
        path1=self.tootCargarImagen1_1()
        path2=self.tootCargarImagen1_2()
        self.tootCargarImagen2(path1)
        self.tootCargarImagen3(path2)
        visualCrypt.TwoOutOfTwo.combine_shares(path1,path2)
        self.tootCargarImagen4('Prueba/decoded_image.png')
    

    def setPhoto(self,image):
        self.tmp = image
        image=imutils.resize(image, width=251)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.imagenCarga_1.setPixmap(QtGui.QPixmap.fromImage(image))
    def setPhoto2(self,image):
        self.tmp = image
        image=imutils.resize(image, width=251)
        frame =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.imagenCarga_2.setPixmap(QtGui.QPixmap.fromImage(image))
    def setPhoto3(self,image):
        self.tmp = image
        image=imutils.resize(image, width=251)
        frame =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.imagenCarga_3.setPixmap(QtGui.QPixmap.fromImage(image))
    def setPhoto4(self,image):
        self.tmp = image
        image=imutils.resize(image, width=251)
        frame =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.imagenCarga_4.setPixmap(QtGui.QPixmap.fromImage(image))


    
##=======================================================================================================================

##FrecDomain=============================================================================================================
    def waveletCargarImagen(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto5(self.image)
        return(self.filename)
    def waveletCargarImagen3(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        return(self.filename)
    def waveletCargarImagen4(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto6(self.image)
        return(self.filename)
    def waveletCargarImagen5(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        return(self.filename)
    
    def waveletCargarImagen2(self,filename):
        self.image = cv2.imread(filename)
        self.setPhoto6(self.image)
    def waveletCargarImagen6(self,filename):
        self.image = cv2.imread(filename)
        self.setPhoto5(self.image)
    def waveletCargarImagen7(self,filename):
        self.image = cv2.imread(filename)
        self.setPhoto7(self.image)
    def waveletCargarImagen8(self,filename):
        self.image = cv2.imread(filename)
        self.setPhoto8(self.image)
    def waveletCargarImagen9(self,filename):
        self.image = cv2.imread(filename)
        self.setPhoto9(self.image)
    def waveletCargarImagen10(self,filename):
        self.image = cv2.imread(filename)
        self.setPhoto10(self.image)
    
    
    def dsaBFirmar(self):#Marcar
        modo=self.aesImageModo.currentText()
        path1=self.waveletCargarImagen() #Ruta a la imagen original
        path2=self.waveletCargarImagen3() #Ruta a la marca de agua a aplicar
        if modo=='Haar':
            modo='haar'
        elif modo=='Daubechies':
            modo='db1'
        elif modo=='Symlets':
            modo='sym2'
        elif modo=='Coiflets':
            modo='coif1'
        elif modo=='Biortogonal':
            modo='bior1.1'
        elif modo=='Biortogonal Reverso':
            modo='rbio1.1'
        elif modo=='Discreto o Meyer':
            modo='dmey'
        watermark.FrquencyDomain.embed_watermark(path1,path2,modo)
        self.waveletCargarImagen2('Prueba/watermarked_image.png')
        self.label_6.setText('Imagen Original')
        self.label_7.setText('Imagen marcada')

    def dsaBVerificar(self):#Extraer
        modo=self.aesImageModo.currentText()
        path1=self.waveletCargarImagen4() #Ruta a la imagen marcada
        path2=self.waveletCargarImagen5() #Ruta a la imagen original
        if modo=='Haar':
            modo='haar'
        elif modo=='Daubechies':
            modo='db1'
        elif modo=='Symlets':
            modo='sym2'
        elif modo=='Coiflets':
            modo='coif1'
        elif modo=='Biortogonal':
            modo='bior1.1'
        elif modo=='Biortogonal Reverso':
            modo='rbio1.1'
        elif modo=='Discreto o Meyer':
            modo='dmey'
        watermark.FrquencyDomain.extract_watermark(path1,path2,modo)
        self.waveletCargarImagen6('Prueba/extracted_watermark.png')
        self.label_6.setText('Marca extraída')
        self.label_7.setText('Imagen marcada')
        self.waveletCargarImagen7('Prueba/approximation.png')
        self.waveletCargarImagen8('Prueba/vertical_detail.png')
        self.waveletCargarImagen9('Prueba/horizontal_detail.png')
        self.waveletCargarImagen10('Prueba/diagonal_detail.png')

    def setPhoto5(self,image):
        self.tmp = image
        image=imutils.resize(image, width=251)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.imagenCarga_5.setPixmap(QtGui.QPixmap.fromImage(image))
    def setPhoto6(self,image):
        self.tmp = image
        image=imutils.resize(image, width=251)
        frame =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.imagenCarga_6.setPixmap(QtGui.QPixmap.fromImage(image))
    def setPhoto7(self,image):
        self.tmp = image
        image=imutils.resize(image, width=91)
        frame =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.imagenCarga_7.setPixmap(QtGui.QPixmap.fromImage(image))
    def setPhoto8(self,image):
        self.tmp = image
        image=imutils.resize(image, width=91)
        frame =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.imagenCarga_8.setPixmap(QtGui.QPixmap.fromImage(image))
    def setPhoto9(self,image):
        self.tmp = image
        image=imutils.resize(image, width=91)
        frame =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.imagenCarga_9.setPixmap(QtGui.QPixmap.fromImage(image))
    def setPhoto10(self,image):
        self.tmp = image
        image=imutils.resize(image, width=91)
        frame =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.imagenCarga_10.setPixmap(QtGui.QPixmap.fromImage(image))
##=======================================================================================================================

##Gamal(firma)=========================================================================================================
    def espacialCargarImagen(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto11(self.image)
        return(self.filename)
    def espacialCargarImagen4(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto12(self.image)
        return(self.filename)
    def espacialCargarImagen3(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        return(self.filename)
    def espacialCargarImagen2(self,filename):
        self.image = cv2.imread(filename)
        self.setPhoto12(self.image)
    def espacialCargarImagen5(self,filename):
        self.image = cv2.imread(filename)
        self.setPhoto11(self.image)
    
    def gamalfiFirmar(self):
        path1=self.espacialCargarImagen() #Ruta a la imagen original
        path2=self.espacialCargarImagen3() #Ruta a la marca de agua a aplicar
        watermark.SpacialDomain.embed_watermark(path1,path2)
        self.espacialCargarImagen2('Prueba/watermarked_image_weak.png')
        self.label_12.setText('Imagen Original')
        self.label_13.setText('Imagen marcada')

    def gamalfiVerificar(self):
        path1=self.espacialCargarImagen4() #Ruta a la imagen watermarked
        path2=self.espacialCargarImagen3() #Ruta a la imagen original
        watermark.SpacialDomain.extract_watermark(path1,path2)
        self.espacialCargarImagen5('Prueba/extracted_watermark_weak.png')
        self.label_12.setText('Marca extraída')
        self.label_13.setText('Imagen marcada')

    def setPhoto11(self,image):
        self.tmp = image
        image=imutils.resize(image, width=251)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.imagenCarga_11.setPixmap(QtGui.QPixmap.fromImage(image))
    def setPhoto12(self,image):
        self.tmp = image
        image=imutils.resize(image, width=251)
        frame =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.imagenCarga_12.setPixmap(QtGui.QPixmap.fromImage(image))
##=======================================================================================================================

##=======================================================================================================================
    def Side_Menu_Def_0(self):
        if self.frame.width() <= 10:
            self.animation1 = QtCore.QPropertyAnimation(self.frame,b"maximumWidth")
            self.animation1.setDuration(500)
            self.animation1.setStartValue(0)
            self.animation1.setEndValue(163)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation1.start()

            self.animation2 = QtCore.QPropertyAnimation(self.frame,b"minimumWidth")
            self.animation2.setDuration(500)
            self.animation2.setStartValue(0)
            self.animation2.setEndValue(163)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()

        else:
            self.animation1 = QtCore.QPropertyAnimation(self.frame,b"maximumWidth")
            self.animation1.setDuration(500)
            self.animation1.setStartValue(163)
            self.animation1.setEndValue(0)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation1.start()

            self.animation2 = QtCore.QPropertyAnimation(self.frame,b"minimumWidth")
            self.animation2.setDuration(500)
            self.animation2.setStartValue(163)
            self.animation2.setEndValue(0)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()

    def Side_Menu_Def_1(self,Event):
        if Event.button()==QtCore.Qt.LeftButton:
            if self.frame.width()>=10:
                 self.animation1 = QtCore.QPropertyAnimation(self.frame,b"maximumWidth")
                 self.animation1.setDuration(500)
                 self.animation1.setStartValue(163)
                 self.animation1.setEndValue(0)
                 self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                 self.animation1.start()
                 
                 self.animation2 = QtCore.QPropertyAnimation(self.frame,b"minimumWidth")
                 self.animation2.setDuration(500)
                 self.animation2.setStartValue(163)
                 self.animation2.setEndValue(0)
                 self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                 self.animation2.start()
        else:
            pass

    def MoveWindow(self, event):
        self.move(self.pos() + event.globalPos() - self.clickPosition)
        self.clickPosition = event.globalPos()
        event.accept()
        pass
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        pass

    def copiar(self, event):
        self.stackedWidget.currentWidget()

def ajustar(texto):
    texto=texto.upper()
    return texto.replace(" ","")

if __name__ == "__main__":
    MainApp = QtWidgets.QApplication([])
    App = MainGui()
    App.show()
    sys.exit(MainApp.exec_())