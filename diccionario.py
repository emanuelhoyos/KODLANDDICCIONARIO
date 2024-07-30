meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'XD':'Expresar una risa',
            'WOW':'Sorpresa de algo',
            'MEME':'Expresa algo divertido y sorprendente',
            'AFK':'Un jugador va a estar ausente en la aprtida',
            'EZ':'Easy osea que estuvo facil contra algun rival',
            
            
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")            

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print('la palabra no existe en nuestro diccionario')

