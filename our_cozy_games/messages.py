messages = {"Cantidad de jugadores": "Hoy ha sido uno de esos días en los que la soledad se siente más pesada. Decidí buscar un juego para distraerme un poco, pero me encontré con que todos los juegos que tengo son para dos jugadores. Es frustrante ver cómo cada caja me recuerda que no tengo a nadie con quien compartir estos momentos. Me siento atrapada, no solo por la vegetación tóxica que rodea mi casa, sino también por esta sensación de aislamiento. A veces, solo quiero reírme con alguien, competir en un juego de mesa o simplemente tener una conversación cara a cara. Pero aquí estoy, rodeada de juegos que no puedo jugar sola. Supongo que tendré que ser creativa y encontrar una manera de adaptarlos para jugar sola, o tal vez inventar mis propias reglas. Pero hoy, solo necesitaba desahogarme y expresar lo mucho que extraño la compañía humana."}

def get_message(tittle):
    global messages
    if tittle in messages:
        return messages[tittle]
    else:
        return "No se encontró el mensaje."