from PIL import Image
import numpy as np

def calcular_area_impressao(img):
    # Converter a imagem para escala de cinza
    img_gray = img.convert('L')
    
    # Converter a imagem para uma matriz de pixels
    img_array = np.array(img_gray)
    
    # Calcular a quantidade de pixels claros e escuros (para simplificação)
    # Aqui, 200 é um valor de threshold para diferenciar a cor preta da colorida
    total_pixels = img_array.size
    pixels_preto = np.sum(img_array < 128)  # Considerando que o valor 128 representa uma cor escura
    
    # A área preta seria o número de pixels escuros sobre o total de pixels
    preta_percentual = (pixels_preto / total_pixels) * 100
    
    # Para fins ilustrativos, vamos supor que o resto seja tinta colorida
    colorida_percentual = 100 - preta_percentual
    
    return preta_percentual, colorida_percentual
