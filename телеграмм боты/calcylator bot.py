import telebot
from telebot import types
token=""
bot=telebot.TeleBot(token)


# клавиотура
klav=types.InlineKeyboardMarkup()
klav.row(types.InlineKeyboardButton("🔙",callback_data="exit") ,
        types.InlineKeyboardButton("c",callback_data="c"), 
        types.InlineKeyboardButton("ac",callback_data="ac"), 
        types.InlineKeyboardButton("➗",callback_data="/"))

klav.row(types.InlineKeyboardButton("1️⃣",callback_data="1") ,
         types.InlineKeyboardButton("2️⃣",callback_data="2") ,
         types.InlineKeyboardButton("3️⃣",callback_data="3") ,
         types.InlineKeyboardButton("✖️",callback_data="*"))

klav.row(types.InlineKeyboardButton("4️⃣",callback_data="4") ,
        types.InlineKeyboardButton("5️⃣",callback_data="5") ,
        types.InlineKeyboardButton("6️⃣",callback_data="6") ,
        types.InlineKeyboardButton("➕",callback_data="+") )

klav.row(types.InlineKeyboardButton("7️⃣",callback_data="7") ,
         types.InlineKeyboardButton("8️⃣",callback_data="8") ,
         types.InlineKeyboardButton("9️⃣",callback_data="9") ,
         types.InlineKeyboardButton("➖",callback_data="-"))

klav.row(types.InlineKeyboardButton("⚫",callback_data=".") ,
         types.InlineKeyboardButton("0️⃣",callback_data="0") ,
         types.InlineKeyboardButton("🟰",callback_data="="))
#калькулятор
prim=" "
oldprim=" "
@bot.message_handler(commands=["start"])
def privet(message):
    bot.send_message(message.chat.id,'привет')

@bot.message_handler(commands=["info"])
def inform (message):
    bot.send_message(message.chat.id,'Это мой первй бот')

@bot.message_handler(commands=["kalc"])
def kalc (message):
    global prim
    if prim==" ":
        bot.send_message(message.chat.id,'введите пример',reply_markup=klav)
    else:
        bot.send_message(message.chat.id,prim,reply_markup=klav)

@bot.callback_query_handler(func=lambda call:True)
def obr(query):
    global prim ,oldprim
    data=query.data
    if data =="exit":
        print("выход")
        prim=" "
    elif data == "=":
         prim= str(eval(prim))
    elif data == "ac":
        prim=" "
    elif data == "c" and prim != " ":
        prim = prim[:-1]
    else :
        prim+=data

    if prim!= oldprim:
        if prim==" ":
            bot.edit_message_text(chat_id= query.message.chat.id,
                                   message_id=query.message.message_id, 
                                   text = 0, reply_markup=klav)
        else :
            bot.edit_message_text(chat_id= query.message.chat.id,
                                   message_id=query.message.message_id,
                                     text = prim, reply_markup=klav)
    oldprim=prim
    #текст
@bot.message_handler(content_types=["text"])
def povtor(message):
    #bot.send_message(message.chat.id,message.text) 
    if "как дела" in message.text.lower() :
        bot.send_message(message.chat.id,"отлично")
    elif "делаешь" in message.text.lower() :
        bot.send_message(message.chat.id,"сижу")
    elif "любишь " in message.text.lower() or "нравится" in message.text.lower() :
        bot.send_message(message.chat.id,"с тобой болтать")
    elif "кот" in message.text.lower() :
        bot.send_photo(message.chat.id,"https://cataas.com/cat", caption='это котик')
    elif "настроение" in message.text.lower():
        bot.send_message(message.chat.id,"хорошое")
    
   
bot.polling()