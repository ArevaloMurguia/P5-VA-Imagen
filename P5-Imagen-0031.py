import cv2
# Leer la imagen con cv2 = computer vision 
img = cv2.imread('Doberman.jpg')
# Determinar el tipo de imagen numpy.ndarray
print(type(img))
# mostrar pixeles 554, 554, 3
print(img.shape)
# Mostrando imagen en ventana barra de titilo Dalmata 0031
cv2.imshow('Doberman 0031', img)
## tiempo de espera 
cv2.waitKey(0)
# destruir todas las ventanas 
cv2.destroyAllWindows()
