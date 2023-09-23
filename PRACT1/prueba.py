import os
os.environ['QT_QPA_PLATFORM'] = 'xcb' ##

import cv2
import numpy as np

# Cargar una imagen desde el archivo
image = cv2.imread('troste.jpg')



print("Hola, este programa te genera distintos filtros:")

#############################################
#############################################
#############################################
print("Aquí filtro rojo")
# APLICAR FILTRO ROJO 
rojo = image.copy()
for fil in range(rojo.shape[0]):
    for col in range(rojo.shape[1]):
        pixel_value = rojo[fil, col]
        pixel_value[0] = 0 # Azul
        pixel_value[1] = 0 # Verde


# Guardar la imagen con filtro rojo
cv2.imwrite('FiltroRojo.jpg', rojo)
print("Filtro Rojo guardado.")






#############################################
#############################################
#############################################
print("Aquí filtro azul")
# APLICAR FILTRO AZUL
azul = image.copy()
for fil in range(azul.shape[0]):
    for col in range(azul.shape[1]):
        pixel_value = azul[fil, col]
        pixel_value[1] = 0 # Verde
        pixel_value[2] = 0 # Rojo

# Guardar la imagen con filtro azul
cv2.imwrite('FiltroAzul.jpg', azul)
print("Filtro Azul guardado.")




#############################################
#############################################
#############################################
print("Aquí filtro verde")
# APLICAR FILTRO VERDE
verde = image.copy()
for fil in range(verde.shape[0]):
    for col in range(verde.shape[1]):
        pixel_value = verde[fil, col]
        pixel_value[0] = 0 # azul
        pixel_value[2] = 0 # Rojo


# Guardar la imagen con filtro verde
cv2.imwrite('FiltroVerde.jpg', verde)
print("Filtro Verde guardado.")



#############################################
#############################################
#############################################
print("Aquí filtro MICA")
# APLICAR FILTRO MICA
mica = image.copy()
pixelRosa =  (230, 50, 250) #(255,0,0) #(255, 182, 193)
for fil in range(mica.shape[0]):
    for col in range(mica.shape[1]):
        mica[fil, col] = mica[fil, col] & pixelRosa
       

# Guardar la imagen con filtro mica
cv2.imwrite('FiltroMica.jpg', mica)
print("Filtro Mica guardado.")




#############################################
#############################################
#############################################
print("Aquí filtro brillo")
# APLICAR FILTRO BRILLO
brillo = image.copy()
const = 50
for fil in range(brillo.shape[0]):
    for col in range(brillo.shape[1]):
        for rgb in range (2):
            pixel_value = brillo[fil, col]
            if (pixel_value[rgb] + const)>255 :
                pixel_value[rgb] = 255
            else :
                pixel_value[rgb] = pixel_value[rgb] + const



# Guardar la imagen con filtro brillo
cv2.imwrite('FiltroBrillo.jpg', brillo)
print("Filtro Mica guardado.")




#############################################
#############################################
#############################################
print("Aquí filtro gris")
# APLICAR FILTRO GRIS
gris = image.copy()
prom = 0
for fil in range(gris.shape[0]):
    for col in range(gris.shape[1]):
        pixel_value = gris[fil, col]
        cero = int(pixel_value[0])
        uno =  int(pixel_value[1])
        dos = int(pixel_value[2])
        prom = ( cero + uno + dos)/3

        if prom > 255:
            prom = 255

        pixel_value[0] = prom
        pixel_value[1] = prom
        pixel_value[2] = prom

# Guardar la imagen con filtro gris
cv2.imwrite('FiltroGris.jpg', gris)
print("Filtro GRis guardado.")




#############################################
#############################################
#############################################
image2 = cv2.imread('FiltroGris.jpg')

print("Aquí filtro Alto Contraste")
# APLICAR FILTRO 
altoC = image2.copy()
for fil in range(altoC.shape[0]):
    for col in range(altoC.shape[1]):
        pixel_value = altoC[fil, col]

        if pixel_value[0] >= 128 :
            pixel_value[0] = 255
            pixel_value[1] = 255
            pixel_value[2] = 255
        else:
            pixel_value[0] = 0
            pixel_value[1] = 0
            pixel_value[2] = 0


# Guardar la imagen con filtro 
cv2.imwrite('FiltroALtoContraste.jpg', altoC)
print("Filtro Alto Contraste guardado.")




#############################################
#############################################
#############################################
print("Aquí filtro Inverso")
# APLICAR FILTRO 
inverso = image2.copy()
for fil in range(inverso.shape[0]):
    for col in range(inverso.shape[1]):
        pixel_value = inverso[fil, col]

        if pixel_value[0] <= 128 :
            pixel_value[0] = 255
            pixel_value[1] = 255
            pixel_value[2] = 255
        else:
            pixel_value[0] = 0
            pixel_value[1] = 0
            pixel_value[2] = 0
# Guardar la imagen con filtro 
cv2.imwrite('FiltroInverso.jpg', inverso)
print("Filtro Inverso guardado.")




#############################################
#############################################
#############################################
print("Aquí filtro Mosaico")
# APLICAR FILTR0
mosaico = image.copy()

tamMosaico = 20

largo= image.shape[0] #Saco dimensiones de la imagen
ancho = image.shape[1]

for fila in range(0, largo, tamMosaico):
    for columna in range(0, ancho, tamMosaico):

        prom0 = 0
        prom1 = 0
        prom2 = 0

        for fil in range(fila, min(fila + tamMosaico, largo)):
            for col in range(columna, min(columna + tamMosaico, ancho)):
                pixel_value = mosaico[fil, col]
                prom0 += int(pixel_value[0])
                prom1 += int(pixel_value[1])
                prom2 += int(pixel_value[2])

        prom0 /=(tamMosaico*tamMosaico)
        prom1 /=(tamMosaico*tamMosaico)
        prom2 /=(tamMosaico*tamMosaico)

        if prom0 > 255:
            prom0 = 255

        if prom1 > 255:
            prom1 = 255

        if prom2 > 255:
            prom2 = 255
        for fil in range(fila, min(fila + tamMosaico, largo)):
            for col in range(columna, min(columna + tamMosaico, ancho)):
                mosaico[fil, col]=(prom0,prom1,prom2)



                

        



# Guardar la imagen con filtro 
cv2.imwrite('FiltroMosaico.jpg', mosaico)
print("Filtro Mosaico guardado.")




print("Fin programa. Las imagenes con filtro se guardaron en esta carpeta.")



