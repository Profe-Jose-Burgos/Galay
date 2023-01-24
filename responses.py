import random
import json
from PIL import Image

def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'menu':
        return 'Opciones disponibles: \n- Frutas \n- Mariscos \n- Carne \n- Imagen'
    if p_message == 'Quejas':
        return 'Comentanos en que podemos mejorar para que tu experiencia sea mejor'
    if p_message == 'Ofertas':
        return 'Aprovecha nuestras ofertas para que tu experiencia sea mejor'
    if p_message == 'Ayuda':
        return "`Este es un mensaje de ayuda que puede ayudar a los usuarios a entender el funcionamiento del bot"
    if p_message == 'Frutas':
       return "Banana= 1.50$ \nManzana= 1.00$ \nPera= 1.00$ \nNaranja= 1.00$ \nSandia= 2.00$"
    if p_message == 'Mariscos':
       return "Langosta= 5.00$ \nCamarones= 3.00$ \nCangrejo= 3.00$ \nOstras= 3.00$"
    if p_message == 'Carne':
        return "Res= 3.00$ \nPollo= 2.00$ \nCerdo= 2.00$"
    if p_message == 'Lacteos':
        return "Leche= 1.00$ \nQueso= 1.50$ \nYogurt= 1.00$"
    elif p_message == 'productos':
        respuestas = {
            "Frutas": {"Banana": "1.50$", "Manzana": "1.00$", "Pera": "1.00$", "Naranja": "1.00$", "Sandia": "2.00$"},
            "Mariscos": {"Langosta": "5.00$", "Camarones": "3.00$", "Cangrejo": "3.00$", "Ostras": "3.00$"},
            "Carne": {"Res": "3.00$", "Pollo": "2.00$", "Cerdo": "2.00$"},
            "Lacteos": {"Leche": "1.00$", "Queso": "1.50$", "Yogurt": "1.00$"},
            "Ayuda": {"Este es un mensaje de ayuda que puede": "ayudar a los usuarios a entender el funcionamiento del bot"},
            "Quejas": {"Comentanos en que podemos mejorar": "para que tu experiencia sea mejor"},
            "Ofertas": {"Aprovecha nuestras ofertas": "para que tu experiencia sea mejor"}
        }
        result = ""
        for category, products in respuestas.items():
            result += f"{category}:\n"
            for product, price in products.items():
                result += f"{product}={price}\n"
        return result
   