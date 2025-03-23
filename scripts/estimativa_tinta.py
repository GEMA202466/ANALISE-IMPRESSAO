from PIL import Image
import numpy as np

def calcular_area_impressao(imagem_input):
    """
    imagem_input pode ser o caminho para o arquivo ou um objeto Image do PIL.
    """
    # Se for um caminho (string), abre a imagem; se já for uma imagem, usa-a
    if isinstance(imagem_input, str):
        img = Image.open(imagem_input)
    else:
        img = imagem_input

    # Converter a imagem para escala de cinza para estimar a tinta preta
    img_gray = img.convert('L')
    img_array = np.array(img_gray)
    
    # Pixels com valor menor que 128 são considerados tinta preta
    tinta_preta = (img_array < 128).sum()
    
    # Para tinta colorida, contamos os pixels que não são totalmente brancos
    img_array_color = np.array(img)
    tinta_colorida = (np.any(img_array_color[:, :, :3] < 128, axis=-1)).sum()
    
    # Total de pixels
    area_total = img_array.size
    tinta_preta_percentual = tinta_preta / area_total * 100
    tinta_colorida_percentual = tinta_colorida / area_total * 100

    return tinta_preta_percentual, tinta_colorida_percentual

if __name__ == "__main__":
    caminho_imagem = "assets/imagem_teste.png"  # Certifique-se de enviar uma imagem para a pasta assets
    preta, colorida = calcular_area_impressao(caminho_imagem)
    print(f"Tinta preta estimada: {preta:.2f}%")
    print(f"Tinta colorida estimada: {colorida:.2f}%")
