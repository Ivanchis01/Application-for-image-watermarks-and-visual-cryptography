from PIL import Image
import random


#============================================================================
class TwoOutOfTwo:
    def switch(color):
        #Asignacion colores subpixeles
        op=random.randint(0,3)
        if color==0: #colorNegro
          if op==0:
            a,b,c,d=1,0,1,0
            e,f,g,h=0,1,0,1
          elif op==1:
            a,b,c,d=0,1,0,1
            e,f,g,h=1,0,1,0
          elif op==2:
            a,b,c,d=0,0,1,1
            e,f,g,h=1,1,0,0
          elif op==3:
            a,b,c,d=1,1,0,0
            e,f,g,h=0,0,1,1
          return(a,b,c,d,e,f,g,h)
        else: #colorNegro
          if op==0:
            a,b,c,d=1,0,1,0
            e,f,g,h=1,0,1,0
          elif op==1:
            a,b,c,d=0,1,0,1
            e,f,g,h=0,1,0,1
          elif op==2:
            a,b,c,d=0,0,1,1
            e,f,g,h=0,0,1,1
          elif op==3:
            a,b,c,d=1,1,0,0
            e,f,g,h=1,1,0,0
          return(a,b,c,d,e,f,g,h)
        #Asignado de acuerdo a la presentación del profe

    def create_shares(image_path):
        # Cargar la imagen en blanco y negro
        image = Image.open(image_path).convert('1')
        pixels = image.load()

        width, height = image.size

        # Crear imágenes en blanco para las compartes
        share1 = Image.new('1', (width * 2, height * 2), 1)
        share2 = Image.new('1', (width * 2, height * 2), 1)

        pixels_share1 = share1.load()
        pixels_share2 = share2.load()

        for y in range(height):
            for x in range(width):
                pixel = pixels[x, y]
                subpixels = [(0, 0), (0, 1), (1, 0), (1, 1)]
                random.shuffle(subpixels)

                if pixel == 0:  # Pixel negro
                  pixels_share1[2 * x, 2 * y], pixels_share1[2 * x +1, 2 * y],pixels_share1[2 * x, 2 * y +1],pixels_share1[2 * x + 1, 2 * y + 1],pixels_share2[2 * x, 2 * y], pixels_share2[2 * x +1, 2 * y],pixels_share2[2 * x, 2 * y +1],pixels_share2[2 * x + 1, 2 * y + 1]=TwoOutOfTwo.switch(pixel)
                else:  # Pixel blanco
                  pixels_share1[2 * x, 2 * y], pixels_share1[2 * x +1, 2 * y],pixels_share1[2 * x, 2 * y +1],pixels_share1[2 * x + 1, 2 * y + 1],pixels_share2[2 * x, 2 * y], pixels_share2[2 * x +1, 2 * y],pixels_share2[2 * x, 2 * y +1],pixels_share2[2 * x + 1, 2 * y + 1]=TwoOutOfTwo.switch(pixel)
        TwoOutOfTwo.save_shares(share1, share2)
        return share1, share2

    def combine_shares(share1_path, share2_path):
        # Cargar las compartes
        share1 = Image.open(share1_path).convert('1')
        share2 = Image.open(share2_path).convert('1')

        width, height = share1.size

        # Crear una nueva imagen en blanco para la imagen resultante
        result = Image.new('1', (width, height), 1)
        pixels_result = result.load()

        pixels_share1 = share1.load()
        pixels_share2 = share2.load()

        for y in range(0,height):
            for x in range(0,width):
                if (pixels_share1[x, y]==0 or pixels_share2[x, y]==0) and not (pixels_share1[x, y]==0 and pixels_share2[x, y]==0):
                    pixels_result[x, y] = 0
                else:
                    pixels_result[x, y] = pixels_share1[x, y]

        # Guardar la imagen resultante
        result.save('Prueba/decoded_image.png')

    def save_shares(share1, share2):
        share1.save('Prueba/share1.png')
        share2.save('Prueba/share2.png')
