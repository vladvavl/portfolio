import telebot
import requests
import json
from telebot import types
from random import randint, choice, random
token=""
bot=telebot.TeleBot(token)
users={}
# класс для игры
class  Player:
    def __init__(self,id):
        self.id = id
        self.hp = 10
        self.exp = 0
        self.maxhp=10
        self.atac=5
        self.ur=1
        self.mane=0
    
    
    def level_up(self):
        self.exp = 0
        self.ur+=1
        self.maxhp+=10
        self.hp=self.maxhp
        self.atac+=2

    def get_exp(self,colvo):
        self.exp+=colvo
        if self.exp>self.ur*10:
            self.level_up()

class Monster:
    def __init__(self,name,plyaerlv,cartinca):
        self.hp = randint(plyaerlv*2,plyaerlv*5)
        self.atac= randint(plyaerlv*2,plyaerlv*3)
        self.name=name 
        self.mexp=randint(plyaerlv*3,plyaerlv*5)
        self.foto=cartinca
        self.nag= randint(plyaerlv*20,plyaerlv*40)
def save ():
    danie={}
    for id,player in users.items():
        player_danie={"id" : player.id,
        "hp" : player.hp,
        "exp" : player.exp,
        "maxhp" : player.maxhp,
        "atac" : player.atac,
        "ur" : player.ur,
        "mane" : player.mane}
        danie[id]=player_danie
    with open ("danie.json","w") as fail:
        json.dump(danie,fail,indent=4)

def lod():
    global users
    try:
        with open("danie.json", 'r') as f:
            user_data = json.load(f)
            users = {id: Player(data["id"]) for id, data in user_data.items()}
            for id, player in users.items():
                player.hp = user_data[id]["hp"]
                player.exp = user_data[id]["exp"]
                player.maxhp = user_data[id]["maxhp"]
                player.atac = user_data[id]["atac"]
                player.ur = user_data[id]["ur"]
                player.mane = user_data[id]["mane"]
        print(users)
    except FileNotFoundError:
        print("No save file found, starting with an empty user dictionary.")

lod()
def spaun(level):
    monstr=[Monster("Гоблин",level,"https://i.imgur.com/ujlGm6m.jpeg"),
            Monster("Орк",level,"https://i.imgur.com/PHNRszA.jpeg"),
            Monster("Разбойник",level,"https://i.imgur.com/ImNbcIy.jpeg")]

    if level >=4:
        monstr.append( Monster("Леший",level,"https://i.imgur.com/JSMvkO1.jpeg"))
        monstr.append(Monster("Темный эльф",level,"https://i.imgur.com/hpyqs9B.jpeg"))
        monstr.append(Monster("Эльфийский лучник",level,"https://i.imgur.com/43tOQN6.jpeg"))
        monstr.append(Monster("Король гоблинов",level,"https://i.imgur.com/TTXpTH7.png"))
    elif level>=6:
        monstr.append(Monster("Дракон",level,"https://i.imgur.com/UjtqQjm.jpeg"))
        monstr.append(Monster("Злой Маг",level,"https://i.imgur.com/6LYT50P.png"))
        monstr.append(Monster("Лесной Маг",level,"https://i.imgur.com/j5r1sJi.png"))
    return choice(monstr)

def get_player(id):
    id=str(id)
    global users 
    if id not in users:
        users[id]=Player(id)
    return users[id]  

def explor(message,player):
    ivent=random()
    if ivent<0.5 :
        batl(message,player)
    elif ivent > 0.85:
        bot.send_message(message.chat.id,'Ты наткнулся на торговца.')
        shop(message)
    elif ivent >0.95:
        otvet= requests.get("https://api.thecatapi.com/v1/images/search").json()[0]["url"]
        bot.send_photo(message.chat.id,otvet, caption="Ты встретил магического кота, который поднял тебе 5 уровень.")
        for i in range (5) :
            player.level_up()
    else :
        bot.send_message(message.chat.id,'Ты погулял и вернулся назад.')

def pacypca(message,player,gold):
    if player.mane >= gold :
        bot.send_message(message.chat.id,'Успешная покупка.')
        player.mane-=gold
        return True
    else :
        bot.send_message(message.chat.id,'недостаточно золота.')

def shop (message):
    bot.send_photo(message.chat.id,"https://i.imgur.com/BHtpi49.jpeg", caption="")
    bot.send_message(message.chat.id,'Торговец предлагает тебе : зелья здоровья(100), ржавый меч(150), зелья мудрости(200), железный меч(400), серебрянный меч(1000).')
    klav=types.InlineKeyboardMarkup()
    klav.row(types.InlineKeyboardButton("зелье здоровья",callback_data="хп") ,
        types.InlineKeyboardButton("зелье мудрости",callback_data="левел"))
    klav.row(types.InlineKeyboardButton("ржавый меч",callback_data="+атака") ,
        types.InlineKeyboardButton("железный меч",callback_data="+2атаки"),
        types.InlineKeyboardButton("серебрянный меч",callback_data="+3атаки"))
    klav.add(types.InlineKeyboardButton("Уйти",callback_data="Выход"))
           
    bot.send_message(message.chat.id,'Что бы ты хотел купить?',reply_markup=klav)

# -------КОМАНДЫ БОТА-------

@bot.message_handler(commands=["rest"])
def otdih (message):
    userid=message.from_user.id
    player=get_player(userid)
    bot.send_message(message.chat.id,'Ты хорошенько отдохнул.Твое XP востановленно.')
    player.hp = player.maxhp

@bot.message_handler(commands=["osmotr"])
def osmotr (message):
    klav=types.InlineKeyboardMarkup()
    klav.row(types.InlineKeyboardButton("🌳",callback_data="лес") ,
        types.InlineKeyboardButton("🌾",callback_data="поле"), 
        types.InlineKeyboardButton(" 🗿",callback_data="пещера"), 
        types.InlineKeyboardButton("🏞",callback_data="озеро"))

    bot.send_message(message.chat.id,'Куда бы ты хотел пойти?',reply_markup=klav)

@bot.message_handler(commands=["start"])
def privet(message):
    bot.send_message(message.chat.id,'привет')
  #игра
@bot.message_handler(commands=["igra"])
def game(message):
    bot.send_message(message.chat.id,f'{message.from_user.first_name},добро пожаловать в игру!!!')
    bot.send_photo(message.chat.id,"https://masterpiecer-images.s3.yandex.net/a1023dbba4a211ee86a3d6f07e64960d:upscaled", caption='Приветствую тебя юный воин! Тебя ждет много приключений и захватывающих сражений')
    userid=message.from_user.id
    player=get_player(userid)
    bot.send_message(message.chat.id,f"Твой уровень {player.ur}.\n Твое хп {player.hp}")

@bot.message_handler(commands=["level_up"])
def level(message):
    bot.send_message(message.chat.id,'Ты повысл уровень')
    userid=message.from_user.id
    player=get_player(userid)
    player.level_up()
    bot.send_message(message.chat.id,f"Твой уровень {player.ur}.\n Твое хп {player.hp}")

@bot.message_handler(commands=["stats"]) 
def stat(message):
    userid=message.from_user.id
    player=get_player(userid)
    bot.send_message(message.chat.id,f'Твое хп: {player.hp},твоя атака : {player.atac}, твой уровень  : {player.ur}, твое золото :{player.mane}')

def batl(message,player):
    monstr = spaun(player.ur)
    bot.send_message(message.chat.id,f'Ты встретил монстра: {monstr.name},его хп : {monstr.hp}, его атака : {monstr.atac}')
    bot.send_photo(message.chat.id,monstr.foto)
    while player.hp>0 and monstr.hp>0:
        monstr.hp-=player.atac
        bot.send_message(message.chat.id,f'Ты ударил монстра :{monstr.name},его хп : {monstr.hp},ты ударил его на : {player.atac}')
        if  monstr.hp>0:
            player.hp-=monstr.atac
            bot.send_message(message.chat.id,f'  {monstr.name} ударил тебя ,твое хп : {player.hp}')
        if player.hp<=0 :
            bot.send_message(message.chat.id,"Ты убежал с поля боя. Очки опыта потеряны")
            player.hp=1
            player.exp-=monstr.mexp
            break
        elif monstr.hp<=0:
            player.get_exp(monstr.mexp)
            player.mane+=monstr.nag
            bot.send_message(message.chat.id,f'Ты победил монстра: {monstr.name}. Получено {monstr.nag} золотых. Очки опыта {monstr.mexp} получены. Твой уровень {player.ur}')
@bot.message_handler(commands=["save"]) 
def save2(message):
    save()

    bot.send_message(message.chat.id,f'Твой прогресс сохранен')


#КЛАВИАТУРА
@bot.callback_query_handler(func=lambda call:True)
def obr(query):
    message = query.message
    userid=query.from_user.id
    player=get_player(userid)
    if query.data =="лес":
       bot.send_message(query.message.chat.id,'Ты попал в лес')
       bot.send_photo(query.message.chat.id,"https://i.imgur.com/XEee8sj.jpeg", caption="Посмотри, этот лес окутан магией")
       explor(message,player)
    elif query.data =="поле":
       bot.send_message(query.message.chat.id,'Добро пожаловать в поле')
       bot.send_photo(query.message.chat.id,'https://i.imgur.com/vdb7F01.jpeg', caption="Ты только погляди на размах этого поля")
       explor(message,player)
    elif query.data =="пещера":
        bot.send_message(query.message.chat.id,'Будь внимательнее в пещере')
        bot.send_photo(query.message.chat.id,"https://i.imgur.com/bdgZ44j.jpeg", caption="")
        explor(message,player)
    elif query.data =="озеро":
        bot.send_message(query.message.chat.id,'Приятного отдыха на озере,но будь осторожнее ')
        bot.send_photo(query.message.chat.id,"https://i.imgur.com/ujDBKax.jpeg", caption="")
        explor(message,player)
    elif query.data == "хп":
        if pacypca(message,player,100)==True:
            bot.send_message(query.message.chat.id,'Твое здоровье увеличено')
            player.maxhp+=2
            player.hp = player.maxhp
    elif query.data == "Выход":
        bot.send_message(query.message.chat.id,'Ты ушел')
        

bot.polling()
save()
#расписать монстров,
