import cv2
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import filedialog

caminho_arquivo = ""

def abrir_arquivo():
    global caminho_arquivo 
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
    )
    if caminho_arquivo:
        print(f"Arquivo selecionado: {caminho_arquivo}")
        btn_fechar.pack(pady=20)


# Criando a janela principal
root = tk.Tk()
root.title("Seletor de Imagens")

# Criando o botão para abrir o seletor de arquivos
btn_abrir = tk.Button(root, text="Escolher Imagem", command=abrir_arquivo)
btn_abrir.pack(pady=20)
btn_fechar = tk.Button(root, text="Fechar", command=root.destroy)
root.mainloop()

# Lendo a imagem
img = cv2.imread(caminho_arquivo)

# Aplicando o filtro de mediana da biblioteca OpenCV que é importada como cv2 e atribuindo a variavel median utilizando uma mascara 5x5﻿
median = cv2.medianBlur(img,5)
img_suavizada = cv2.GaussianBlur(median, (5,5), 0)

# comparacao
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_suavizada),plt.title('Mediana')
plt.xticks([]), plt.yticks([])
plt.show()
