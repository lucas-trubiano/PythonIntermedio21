#para el bot de telegram
import telebot
from telebot import types
import ast

#pip install telegram-notifier #es solo un notificador
#pip install pyTelegramBotAPI # es para bots en general

import _thread # para hacer multihilos
import time

# check some links
#https://pocketadmin.tech/en/telegram-bot-on-python/
#https://www.mindk.com/blog/how-to-develop-a-chat-bot/
#https://www.programcreek.com/python/example/91615/telebot.types.InlineKeyboardMarkup
#https://stackoverflow.com/questions/45558984/how-to-make-telegram-bot-dynamic-keyboardbutton-in-python-every-button-on-one-ro/51904640
#https://stackoverflow.com/questions/63927835/how-to-use-telebot-module-to-create-an-inline-button-in-bot-window-which-if-cli
#https://dev-qa.com/468261/how-edit-the-message-text-and-the-button-itself-inline-python


class TelegramBot():
    numBots = 0

    def __init__(self,Token):
        self.token = Token
        self.bot = telebot.TeleBot(self.token, parse_mode=None)
        self.user_id = None
        self.username = None
        self.flagMessage = False
        self.newMessage = False

        self.opc = False
        self.flagOpc = False

        @self.bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            if message.text.startswith("/start"):
                self.user_id = message.from_user.id
                self.username = message.from_user.username
                markup = types.ReplyKeyboardRemove()
                mensaje = f"""Te hemos registrado {self.username}"""# [ID:{self.user_id}]"""
                self.bot.send_message(self.user_id, mensaje, None, None, markup)
        
        @self.bot.message_handler(func=lambda m: True)
        def echo_all(message):
            msje = {
                "message_id":message.message_id,
                "user_id":message.from_user.id,
                "first_name":message.from_user.first_name,
                "last_name":message.from_user.last_name,
                "username":message.from_user.username,
                "language_code":message.from_user.language_code,
                "date":message.date,
                "text":message.text
            }
            if self.user_id == msje['user_id']: #Guardar mensaje
                print(f"Mensaje recibido de {self.username} [{self.user_id}]")
                self.newMessage = msje['text']
                self.flagMessage = True
            elif msje['text'] == "Iniciar Conversación":
                self.user_id = message.from_user.id
                self.username = message.from_user.username
                markup = types.ReplyKeyboardRemove()
                mensaje = f"""Iniciando conversacion con {self.username} [ID:{self.user_id}]"""
                self.bot.send_message(self.user_id, mensaje, None, None, markup)
            else: # es otro usuario, no responder
                pass #ignorar
        
        @self.bot.callback_query_handler(func=lambda call: True)
        def handle_query(call):
            #print(call.data)
            msje = call.data
            #print(msje)

            if (msje.startswith("callback_")):
                self.opc = int(msje.replace('callback_','').split("/")[0])
                boton = msje.split("/")[1]
                self.flagOpc = True
                self.bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text=f"You Clicked: {boton}")
            elif msje.startswith("/start"):
                #print(call)
                self.user_id = call.from_user.id
                self.username = call.from_user.username
                markup = types.ReplyKeyboardRemove()
                mensaje = f"""Iniciando conversacion con {self.username}"""# [ID:{self.user_id}]"""
                #self.bot.send_message(self.user_id, mensaje, None, None, markup)
                self.bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text=mensaje)

        self.iniciarBucle()
    
    def startConversation(self,msjeBienvenida=None):
        while self.user_id == None:
            pass
        print(f"Conversacion iniciada {self.username} [ID:{self.user_id}]!!!")
        if msjeBienvenida!=None:
            self.printMessage(msjeBienvenida)
        time.sleep(0.1)
        
    def startConversationWith(self,id_usuario,msjeBienvenida=None):
        while self.user_id != id_usuario:
            pass
        print(f"Conversacion iniciada {self.username} [ID:{self.user_id}]!!!")
        if msjeBienvenida!=None:
            self.printMessage(msjeBienvenida)
        time.sleep(0.1)

    def inputMessage(self):
        # se queda en un while hasta que haya un mensaje nuevo
        # guardar el msje en self.message
        # apagar el flag de nuevo mensaje

        #self.flagMessage = False
        while self.flagMessage == False:
            pass
        self.flagMessage = False
        return self.newMessage

    def inputOption(self,opciones,mensaje = None):
        # enviar una seria de opciones como comandos y devolver el numero de rpta que se recibio
        if mensaje == None:
            mensaje="Haga click en una opcion:"
        
        self.flagOpc = False
        markup = types.ReplyKeyboardRemove()
        markup = types.InlineKeyboardMarkup()
        for i in range(len(opciones)):
            markup.add(types.InlineKeyboardButton(  text=opciones[i],
                                                    callback_data=f"callback_{i}/{opciones[i]}") )
        self.bot.send_message(self.user_id, mensaje, None, None, markup)
        #print("se enviarion las opciones")
        #esperar la respuesta
        while self.flagOpc == False:
            pass
        self.flagOpc = False
        #print(f"se recibio rpta ;{self.opc};{type(self.opc)}")
        return self.opc

    def printMessage(self,mensaje):
        self.bot.send_message(self.user_id, mensaje)

    def printOptions(self):
        # sirve para darle al usuario una serie de opciones en los botones
        pass

    def iniciarBucle(self):
        #self.bucle()
        _thread.start_new_thread( self.bucle,() )

    def bucle(self):
        # Always get updates.
        # :param interval: Delay between two update retrivals
        # :param none_stop: Do not stop polling when an ApiException occurs.
        # :param timeout: Request connection timeout
        # :param long_polling_timeout: Timeout in seconds for long polling (see API docs)
        
        # Upon calling this function, TeleBot starts polling the Telegram servers for new messages.
        # - none_stop: True/False (default False) - Don't stop polling when receiving an error from the Telegram servers
        # - interval: True/False (default False) - The interval between polling requests
        #           Note: Editing this parameter harms the bot's response time
        # - timeout: integer (default 20) - Timeout in seconds for long polling.
        try:
            self.bot.polling(none_stop=True, interval=0, timeout=60)
            #bot.polling(none_stop=True, timeout=60) #constantly get messages from Telegram
        except:
            print("Terminó un ciclo")
            # traceback_error_string=traceback.format_exc()
            # with open("Error.Log", "a") as myfile:
            #     myfile.write("\r\n\r\n" + time.strftime("%c")+"\r\n<<ERROR polling>>\r\n"+ traceback_error_string + "\r\n<<ERROR polling>>")
            self.bot.stop_polling()
            time.sleep(10)
            self.bucle()
        # self.bot.polling(none_stop=False, interval=0, timeout=20)
    
    def fin(self):
        self.flagOpc = False
        markup = types.ReplyKeyboardRemove()
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(  text="Iniciar Nueva Conversación 💬",
                                                callback_data=f"/start") )
        self.bot.send_message(self.user_id, "Adios 👋 !! Haga click aqui abajo si quiere iniciar una nueva conversación\n======================================", None, None, markup)
        #self.bot.stop_bot()
        self.user_id = None
        self.username = None
    
    def exit(self):
        self.bot.stop_bot()

    # def restart(self):
    #     self.bot.

    # def close(self):
    #     return self.bot.stop_polling()
    

print("INICIO")
TOKEN = "1351036689:AAFIIjF0bzjaOxM5j3Iqm1qcsCqdV3mZFFc" #IQ_notifier_bot
teleg = TelegramBot(TOKEN)
mensajeBienvenida = """Hola 😁 !! has iniciado una nueva conversación en que puedo ayudarte?"""
menu = ["Agregar producto","Eliminar producto","Ver productos","Salir"]
menuMsje = """============ MENU ============
Qué accion quieres realizar? 👇👇"""

teleg.startConversation(mensajeBienvenida)

while True:
    #teleg.printMessage(menu)
    #opc = int(teleg.inputMessage())
    opc = teleg.inputOption(menu,menuMsje)+1

    if opc==1:
        teleg.printMessage("agregando producto")
    elif opc==2:
        teleg.printMessage("eliminando productos")
    elif opc ==3:
        teleg.printMessage("Viendo Productos")
    elif opc==4:
        #teleg.printMessage("Adios")
        print("Termino un bucle")
        teleg.fin()
        break
    else:
        print("opcion incorrecta elija otra")

teleg.exit()

# teleg.printMessage("Hola como estas?")
# rpta = teleg.inputMessage()
# print("El usuario respondió:",rpta)
# teleg.printMessage(f"Respondiste: {rpta}")
# teleg.printMessage(f"Mandanos otro mensaje para finalizar")
# rpta2 = teleg.inputMessage()
# print(rpta2)
# teleg.printMessage(f"su otra rpta: {rpta2}")
# teleg.fin()
print("FIN")