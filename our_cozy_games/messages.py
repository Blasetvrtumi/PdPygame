messages = {}

def get_message(tittle):
    global messages
    if tittle in messages:
        return messages[tittle]
    else:
        return "No se encontró el mensaje."