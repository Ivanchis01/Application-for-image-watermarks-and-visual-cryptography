import pywt #PyWavelet
import numpy as np
from PIL import Image

#============================================================================
class FrquencyDomain:
    def resize_watermark(watermark, target_shape): #Cambiamos el tamaño de la marca de agua para que coincida con la original
        return np.array(Image.fromarray(watermark).resize((target_shape[1], target_shape[0]), Image.Resampling.LANCZOS))

    def embed_watermark(original_image_path, watermark_image_path,modo):
        # Cargar la imagen original
        original_image = Image.open(original_image_path).convert('L')
        original_array = np.array(original_image, dtype=np.float32)

        # Aplicar la DWT a la imagen original
        coeffs_original = pywt.dwt2(original_array, modo)
        LL, (LH, HL, HH) = coeffs_original

        # Cargar y normalizar la marca de agua
        watermark_image = Image.open(watermark_image_path).convert('L')
        watermark_array = np.array(watermark_image, dtype=np.float32)
        watermark_array = watermark_array / 255.0
        watermark_resizedLH = FrquencyDomain.resize_watermark(watermark_array, LH.shape)
        watermark_resizedHH = FrquencyDomain.resize_watermark(watermark_array, HH.shape)
        watermark_resizedHL = FrquencyDomain.resize_watermark(watermark_array, HL.shape)
        watermark_resizedLL = FrquencyDomain.resize_watermark(watermark_array, LL.shape)

        # Incrustar la marca de agua en la sub-banda LH
        alpha = 5  # Factor de escala para la marca de agua
        LH += alpha * watermark_resizedLH
        HH += alpha * watermark_resizedHH
        HL += alpha * watermark_resizedHL
        LL += alpha * watermark_resizedLL

        # Aplicar la IDWT para obtener la imagen con la marca de agua
        coeffs_watermarked = (LL, (LH, HL, HH))
        watermarked_array = pywt.idwt2(coeffs_watermarked, modo)

        # Convertir a imagen y guardar
        watermarked_image = Image.fromarray(np.uint8(np.clip(watermarked_array, 0, 255)))
        watermarked_image.save('Prueba/watermarked_image.png')

    def extract_watermark(watermarked_image_path, original_image_path,modo):
        # Cargar la imagen con la marca de agua y la imagen original
        watermarked_image = Image.open(watermarked_image_path).convert('L')
        original_image = Image.open(original_image_path).convert('L')

        watermarked_array = np.array(watermarked_image, dtype=np.float32)
        original_array = np.array(original_image, dtype=np.float32)

        # Aplicar la DWT a ambas imágenes
        coeffs_watermarked = pywt.dwt2(watermarked_array, modo)
        LL_watermarked, (LH_watermarked, HL_watermarked, HH_watermarked) = coeffs_watermarked

        coeffs_original = pywt.dwt2(original_array, modo)
        LL_original, (LH_original, HL_original, HH_original) = coeffs_original

        # Extraer la marca de agua
        alpha = 5  # El mismo factor de escala utilizado para incrustar

        approximation = (LL_watermarked - LL_original) / alpha
        horizontal_detail = (LH_watermarked - LH_original) / alpha
        vertical_detail = (HL_watermarked - HL_original) / alpha
        diagonal_detail = (HH_watermarked - HH_original) / alpha

        combined_watermark = (approximation + horizontal_detail + vertical_detail + diagonal_detail) / 4

        # Convertir a imagen y guardar
        extracted_watermark_image = Image.fromarray(np.uint8(np.clip(combined_watermark * 255, 0, 255)))
        extracted_watermark_image.save('Prueba/extracted_watermark.png')
        

        extracted_watermark_image = Image.fromarray(np.uint8(np.clip(approximation * 255, 0, 255)))
        extracted_watermark_image.save('Prueba/approximation.png')
        extracted_watermark_image = Image.fromarray(np.uint8(np.clip(horizontal_detail * 255, 0, 255)))
        extracted_watermark_image.save('Prueba/horizontal_detail.png')
        extracted_watermark_image = Image.fromarray(np.uint8(np.clip(vertical_detail * 255, 0, 255)))
        extracted_watermark_image.save('Prueba/vertical_detail.png')
        extracted_watermark_image = Image.fromarray(np.uint8(np.clip(diagonal_detail * 255, 0, 255)))
        extracted_watermark_image.save('Prueba/diagonal_detail.png')
        return



#============================================================================
class SpacialDomain:
    def embed_watermark(original_image_path, watermark_image_path):
        # Cargar la imagen original
        original_image = Image.open(original_image_path).convert('L')
        original_array = np.array(original_image, dtype=np.float32)


        # Cargar y normalizar la marca de agua
        watermark_image = Image.open(watermark_image_path).convert('L')
        watermark_image = watermark_image.resize((original_image.width,original_image.height))
        watermark_array = np.array(watermark_image, dtype=np.float32)
        watermark_array = watermark_array

        watermarked_array = original_array + 0.1*watermark_array

        # Convertir a imagen y guardar
        watermarked_image = Image.fromarray(np.uint8(np.clip(watermarked_array, 0, 255)))
        watermarked_image.save('Prueba/watermarked_image_weak.png')

    def extract_watermark(watermarked_image_path, original_image_path):
        # Cargar la imagen con la marca de agua y la imagen original
        watermarked_image = Image.open(watermarked_image_path).convert('L')
        original_image = Image.open(original_image_path).convert('L')

        watermarked_array = np.array(watermarked_image, dtype=np.float32)
        original_array = np.array(original_image, dtype=np.float32)
        watermark = ((watermarked_array - original_array))

        # Convertir a imagen y guardar
        extracted_watermark_image = Image.fromarray(np.uint8(np.clip(watermark, 0, 255)))
        extracted_watermark_image.save('Prueba/extracted_watermark_weak.png')

        return