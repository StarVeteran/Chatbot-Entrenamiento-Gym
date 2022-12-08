#Requisito Instalar por separado chatterbot_corpus mediante pip install chatterbot_corpus   

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot(name='PyBot', read_only=True,
          logic_adapters=
    [
    'chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'
    ])

pecho = ['hola',
          'Que Onda',
          'como andas?',
          'Muy bien y tu?',
          'estoy bien',
          'En que te puedo ayudar?',
          'tengo dudas acerca de la rutina',
          'Claro, que toca hoy?',
          'me toca pecho',
          'Entoces empieza calentando un poco con una barra',
          'esta bien y luego?',
          'Ya le das al press de pecho con peso moderado a pesado',
          'Ok',
          'Y ya despues le das press de pecho con mancuernas',
          'esta bien'
          'Hechale ganas'
          ]
pierna = ['hola',
          'Que Onda',
          'como andas?',
          'Muy bien y tu?',
          'Estoy bien',
          'En que te puedo ayudar?',
          'tengo una duda',
          'Claro, que toca hoy?',
          'me toca pierna',
          'Entoces empieza calentando un poco con la prensa',
          'despues de eso?',
          'Te vas hacer sentadillas con la barra con peso moderado a pesado',
          'Ok',
          'Y ya despues le das a las extensiones',
          'esta bien'
          'Alivianese macizo']

espalda = ['hola',
          'Que Onda',
          'como andas?',
          'Muy bien y tu?',
          'Estoy bien',
          'En que te puedo ayudar?',
          'tengo una duda',
          'Que le vas a dar hoy?',
          'me toca espalda',
          'Entoces empieza calentando un poco con la maquina de remos',
          'luego?',
          'Te vas hacer remos con mancuerno',
          'Ok',
          'Y ya despues te lanzas a los remos dobles con mancuerna',
          'esta bien'
          'Fierro']

tricep = ['que rollo',
          'Que Rollo',
          'como andas?',
          'Muy bien y tu?',
          'Estoy bien',
          'En que te puedo ayudar?',
          'Ocupo ayuda con la rutina',
          'Que le vas a dar?',
          'me toca tricep',
          'Empieza calentando con la maquina de tricep',
          'despues?',
          'Te pasas al press frances con peso moderado',
          'Ok',
          'Y ya despues te lanzas a la maquina de tricep',
          'muy bien'
          'Todo bien']

bicep = [ 'que onda',
          'Quiubole ',
          'como andas?',
          'Muy bien y tu?',
          'ando al 100',
          'Que ocupas?',
          'ayuda con la rutina',
          'Que le vas a dar?',
          'me toca bicep',
          'Lanzate a calentar con la maquina de bicep livianon',
          'despues?',
          'Ya le metes con la maquina de bicep mas peso',
          'Ok',
          'Y ya despues haces curl de bicep con mancuerna y con barra peso moderado',
          'fierro'
          'Dale con todo']

list_trainer = ListTrainer(my_bot)

for item in (pecho, pierna,espalda,tricep,bicep):
          list_trainer.train(item) 


while True:
    try:
        bot_input = input("You: ")
        bot_response = my_bot.get_response(bot_input)
        print(f"{my_bot.name}: {bot_response}")
    except (KeyboardInterrupt, EOFError, SystemExit):
        break;       
