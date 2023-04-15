from telebot import TeleBot,types

TOKEN = "6269848005:AAHrjCp5mBWKL095J8j0H-Wy5vgJ3DraoT8"
mybot = TeleBot(TOKEN)

geo_practice = "Pythonda geoma'lumotlar tahlili (Amaliyot)"
geo_lecture = "Pythonda geoma'lumotlar tahlili (Ma'ruza)"
formal_practice = "Dasturni tekshirishning formal usullari (Amaliyot)"
formal_lecture = "Dasturni tekshirishning formal usullari (Ma'ruza)"
bio_practice = "Bioinformatika va biomexanika (Amaliyot)"
bio_lecture = "Bioinformatika va biomexanika (Ma'ruza)"

@mybot.message_handler(commands=['start'])
def start(message):
    buttons = types.ReplyKeyboardMarkup(True)
    buttons.row("Dushanba","Seshanba")
    buttons.row("Chorshanba","Payshanba")
    buttons.row("Juma","Shanba")
    mybot.send_message(message.chat.id,"Salom botga hush kelibsiz!",reply_markup=buttons)  
    
@mybot.message_handler(content_types=['photo'])
def rsam(message):
    mybot.delete_message(message.chat.id,message.id)

@mybot.message_handler(content_types=['text'])
def send_fanlar(message):
    day = message.text.lower()
    buttons = types.InlineKeyboardMarkup()

    if day == "dushanba":
        b1 = types.InlineKeyboardButton(text=geo_practice,callback_data="mon_geo_prac")
        b2 = types.InlineKeyboardButton(text=bio_practice,callback_data="mon_bio_prac")
        b3 = types.InlineKeyboardButton(text=geo_lecture,callback_data="mon_geo_lec")
        buttons.add(b1)
        buttons.add(b2)
        buttons.add(b3)
        mybot.send_message(message.chat.id,"Dushanba kungi darslar 👇🏻", reply_markup=buttons)

    elif day == "seshanba":
        b1 = types.InlineKeyboardButton(text=bio_practice,callback_data="tues_bio_prac")
        b2 = types.InlineKeyboardButton(text=bio_lecture,callback_data="tues_bio_lec")
        b3 = types.InlineKeyboardButton(text=formal_lecture,callback_data="tues_formal_lec")
        buttons.add(b1)
        buttons.add(b2)
        buttons.add(b3)
        mybot.send_message(message.chat.id,"Seshanba kungi darslar 👇🏻", reply_markup=buttons)
    
    elif day == "chorshanba":
        b1 = types.InlineKeyboardButton(text=geo_practice,callback_data="wed_geo_prac")
        b2 = types.InlineKeyboardButton(text=formal_practice,callback_data="wed_formal_prac")
        b3 = types.InlineKeyboardButton(text=bio_practice,callback_data="wed_bio_prac")
        buttons.add(b1)
        buttons.add(b2)
        buttons.add(b3)
        mybot.send_message(message.chat.id,"Chorshanba kungi darslar 👇🏻", reply_markup=buttons)

    elif day == "payshanba":
        b1 = types.InlineKeyboardButton(text=formal_lecture,callback_data="thurs_formal_lec")
        b2 = types.InlineKeyboardButton(text=formal_practice,callback_data="thurs_formal_prac")
        b3 = types.InlineKeyboardButton(text=bio_lecture,callback_data="thurs_bio_lec")
        buttons.add(b1)
        buttons.add(b2)
        buttons.add(b3)
        mybot.send_message(message.chat.id,"Payshanba kungi darslar 👇🏻", reply_markup=buttons)
    
    elif day == "juma":
        b1 = types.InlineKeyboardButton(text=bio_practice,callback_data="fri_bio_prac")
        b2 = types.InlineKeyboardButton(text=geo_practice,callback_data="fri_geo_prac")
        b3 = types.InlineKeyboardButton(text=formal_practice,callback_data="fri_formal_prac")
        buttons.add(b1)
        buttons.add(b2)
        buttons.add(b3)
        mybot.send_message(message.chat.id,"Juma kungi darslar 👇🏻", reply_markup=buttons)
        
    elif day == "shanba":
        b1 = types.InlineKeyboardButton(text=geo_practice,callback_data="sat_geo_prac")
        b2 = types.InlineKeyboardButton(text=geo_lecture,callback_data="sat_geo_lec")
        b3 = types.InlineKeyboardButton(text=formal_practice,callback_data="sat_formal_prac")
        buttons.add(b1)
        buttons.add(b2)
        buttons.add(b3)
        mybot.send_message(message.chat.id,"Shanba kungi darslar 👇🏻", reply_markup=buttons)


@mybot.callback_query_handler(func=lambda call:True)
def tugma_bosildis(call):
    mybot.delete_message(call.message.chat.id,call.message.id)
    if call.data == "mon_geo_prac":
        mybot.send_message(call.message.chat.id,"109-xona Amaliyot. \nO'qituvchi: Alloyorov Oybek.M")
    elif call.data == "mon_bio_prac":
        mybot.send_message(call.message.chat.id,"303-xona Amaliyot. \nO'qituvchi: Baltayev Rustam.Sh")
    elif call.data == "mon_geo_lec":
        mybot.send_message(call.message.chat.id,"315-xona Ma'ruza. \nO'qituvchi: Xakimov Zohidjon.A")
    #*****************************************      
    elif call.data == "tues_bio_prac":
        mybot.send_message(call.message.chat.id,"213-xona Amaliyot. \nO'qituvchi: Baltayev Rustam.Sh")
    elif call.data == "tues_bio_lec":
        mybot.send_message(call.message.chat.id,"315-xona Ma'ruza. \nO'qituvchi: Baltayev Rustam.Sh")
    elif call.data == "tues_formal_lec":
        mybot.send_message(call.message.chat.id,"315-xona Ma'ruza. \nO'qituvchi: Otamurotov Hurmat.Q")
    #*****************************************       
    elif call.data == "wed_geo_prac":
        mybot.send_message(call.message.chat.id,"114-xona Amaliyot. \nO'qituvchi: Allayorov Oybek.Sh")
    elif call.data == "wed_formal_prac":
        mybot.send_message(call.message.chat.id,"114-xona Amaliyot. \nO'qituvchi: Baltayev Rustam.Sh")
    elif call.data == "wed_bio_prac":
        mybot.send_message(call.message.chat.id,"114-xona Amaliyot. \nO'qituvchi: Baltayev Rustam.Sh")
    #*****************************************       
    elif call.data == "thurs_formal_lec":
        mybot.send_message(call.message.chat.id,"315-xona Ma'ruza. \nO'qituvchi: Otamurotov Hurmat.Q")
    elif call.data == "thurs_formal_prac":
        mybot.send_message(call.message.chat.id,"107-xona Amaliyot. \nO'qituvchi: Baltayev Rustam.Sh")
    elif call.data == "thurs_bio_lec":
        mybot.send_message(call.message.chat.id,"315-xona Ma'ruza. \nO'qituvchi: Baltayev Rustam.Sh")
    #*****************************************      
    elif call.data == "fri_bio_prac":
        mybot.send_message(call.message.chat.id,"305-xona Amaliyot. \nO'qituvchi: Baltayev Rustam.Sh")
    elif call.data == "fri_geo_prac":
        mybot.send_message(call.message.chat.id,"109-xona Amaliyot. \nO'qituvchi: Allayorov Oybek.Sh")
    elif call.data == "fri_formal_prac":
        mybot.send_message(call.message.chat.id,"109-xona Amaliyot. \nO'qituvchi: Baltayev Rustam.Sh")
    #*****************************************   
    elif call.data == "sat_geo_prac":
        mybot.send_message(call.message.chat.id,"109-xona Amaliyot. \nO'qituvchi: Allayorov Oybek.Sh")
    elif call.data == "sat_geo_lec":
        mybot.send_message(call.message.chat.id,"315-xona Ma'ruza. \nO'qituvchi: Xakimov Zohidjon.A")
    elif call.data == "sat_formal_prac":
        mybot.send_message(call.message.chat.id,"213-xona Amaliyot. \nO'qituvchi: Baltayev Rustam.Sh")
        

mybot.polling()