import random
from PIL import Image

def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'productos':
        return 'Opciones disponibles: \n- Frutas \n- Mariscos \n- Carne \n- Ayuda'
    elif p_message == 'frutas':
        return 'Banana= 1.50$ \nManzana= 1.00$ \nPera= 1.00$ \nNaranja= 1.00$ \nSandia= 2.00$'
    elif p_message == 'mariscos':
        return 'Langosta= 5.00$ \nCamarones= 3.00$ \nCangrejo= 3.00$ \nOstras= 3.00$'
    elif p_message == 'carne':
        return 'Res= 3.00$ \nPollo= 2.00$ \nCerdo= 2.00$ \nConejo...'
    elif p_message == 'ayuda':
        return "`Este es un mensaje de ayuda que puede"
    elif p_message == 'imagen':
        with Image.open("pexels-a-k-3222255.jpg") as img:
            img.show()
    if p_message == 'hola':
        return 'Hola que tal?'
    #  return 'Yeah, I don\'t know. Try typing "!help".'
