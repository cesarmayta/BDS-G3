from PIL import Image,ImageFont,ImageDraw

image = Image.open('matrix.jpg')
print(image.size)
print(image.mode)
print(image.format)

#convertir imagen a blanco y negro
#image_blackwhite = image.convert('L')
#image_blackwhite.show()

#redimensionar imagen
width = image.size[0]
height = image.size[1]
print(f'ancho : {width}')
print(f'alto : {height}')

new_width = width // 5
new_height = height // 5

print(f'nuevo ancho : {new_width}')
print(f'nuevo alto : {new_height}')

new_size = (new_width,new_height)

image_short = image.resize(new_size)
#image_short.show()
image.save('matrix_short.jpg','JPEG',quality=90)

#incrustar texto en la imagen
font = ImageFont.truetype('Roboto-Bold.ttf',120)
draw = ImageDraw.Draw(image)
#RGB RED GREEN BLUE
draw.text(
    (10,0),
    "CESAR MAYTA EN CODIGO G3",
    (255,255,255),
    font
)
image.show()