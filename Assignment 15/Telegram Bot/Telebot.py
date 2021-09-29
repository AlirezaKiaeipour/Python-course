import random
from gtts import gTTS
from khayyam import JalaliDate
from pytube import YouTube
import qrcode
import telebot


bot = telebot.TeleBot("Token")
nums = random.randint(1,20)

@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id,f"سلام {message.chat.first_name} به بات من خوش اومدی😉")
    bot.send_message(message.chat.id,"اگه نیاز به کمک داری از /help استفاده کن")

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id,"کاربر گرامی:\nبا /game شما می توانید بازی حدس عدد را انجام دهید.\nبا /age شما می توانید تاریخ تولد خود را به هجری شمسی وارد کنید تا سن دقیق شما محاسبه شود.\nبا /voice شما می توانید یک جمله انگلیسی را وارد کنید تا برایتان به صورت صوتی پخش شود.\nبا /qrcode شما می توانید اطلاعات مورد نیاز خود را وارد کنید و qrcode آن را دریافت کنید.\nبا /youtube شما می توانید لینک یک ویدیو از یوتوب را وارد کنید و آن ویدیو را دریافت کنید.\nبا /max شما می توانید یک لیستی از اعداد را وارد کنید و بزرگترین عدد را دریافت کنید.\nبا /argmax شما می توانید یک لیستی از اعداد را وارد کنید و اندیس بزرگترین عدد را دریافت کنید.\n")

@bot.message_handler(commands=["qrcode"])
def qr(message):
    ms = bot.send_message(message.chat.id,"واسه من یک متن بفرست من واست qrcode میفرستم")
    bot.register_next_step_handler(ms,make_qr)

def make_qr(message):
    try:
        image = qrcode.make(message.text)
        image.save("test.png")
        phpto =  open("test.png","rb")
        bot.send_photo(message.chat.id,phpto)
    except:
        bot.send_message(message.chat.id,"عملیات ناموفق بود")

@bot.message_handler(commands=["voice"])
def voice(message):
    ms = bot.send_message(message.chat.id,"میتونی یک جمله انگلیسی واسم بفرستی من برات به صورت صوتی پخش کنم🔊")
    bot.register_next_step_handler(ms,make_voice)

def make_voice(message):
    try:
        language_voice = gTTS(text=message.text,lang="en",slow=False)
        language_voice.save("voice.mp3")
        audio = open("voice.mp3","rb")
        bot.send_audio(message.chat.id,audio)
    except:
        bot.send_message(message.chat.id,"نه به زبان انکلیسی وارد کن🙂")


@bot.message_handler(commands=["age"])
def age(message):
    ms = bot.send_message(message.chat.id,"تاریخ تولدتو به هجری شمسی بگو من سنتو بهت بگم\n باید تاریخ رو به شکل زیر وارد کنی\nYYYY/MM/DD")
    bot.register_next_step_handler(ms,cal_age)

def cal_age(message):
    try:
        message_text = message.text.split("/")
        today = JalaliDate.today()

        res = {}
        if today.day < JalaliDate(int(message_text[0]),int(message_text[1]),int(message_text[2])).day:
            if 1<=JalaliDate(int(message_text[0]),int(message_text[1]),int(message_text[2])).month <=6 :
                today.day +=31
            elif 7<=JalaliDate(int(message_text[0]),int(message_text[1]),int(message_text[2])).month<=11 :
                today.day +=30
            elif JalaliDate(int(message_text[0]),int(message_text[1]),int(message_text[2])).month==12 :
                today.day +=29
            today.month -=1
        if today.month < JalaliDate(int(message_text[0]),int(message_text[1]),int(message_text[2])).month:
                today.month +=12
                today.year -=1
        
        res[0] = today.year - JalaliDate(int(message_text[0]),int(message_text[1]),int(message_text[2])).year
        res[1] = today.month - JalaliDate(int(message_text[0]),int(message_text[1]),int(message_text[2])).month
        res[2] = today.day - JalaliDate(int(message_text[0]),int(message_text[1]),int(message_text[2])).day
        bot.send_message(message.chat.id,f"سن شما {res[0]} سال و {res[1]} ماه و {res[2]}روز است")
        print(today.month)
    except:
        bot.send_message(message.chat.id,"نه نه باید تاریخ رو درست وارد کنی🙂")

@bot.message_handler(commands=["max"])
def max_list(message):
    ms = bot.send_message(message.chat.id," میتونی یک سری عدد به من بدی من برات ماکزیمم اعداد رو پیدا کنم فقط باید اعداد رو به صورت زیر وارد کنی\n1,2,3,...")
    bot.register_next_step_handler(ms,cal_max_list)

def cal_max_list(message):
    try:
        text = message.text
        obj = list(map(int,text.split(",")))
        bot.send_message(message.chat.id,f"ماکزیمم عدد برابر است با: {max(obj)}")
    except:
        bot.send_message(message.chat.id,"نه نه باید اعداد رو درست وارد کنی🙂")

@bot.message_handler(commands=["argmax"])
def max_arg_list(message):
    ms = bot.send_message(message.chat.id," میتونی یک سری عدد به من بدی من برات اندیس ماکزیمم اعداد رو پیدا کنم فقط باید اعداد رو به صورت زیر وارد کنی\n1,2,3,...")
    bot.register_next_step_handler(ms,cal_max_arg_list)

def cal_max_arg_list(message):
    try:
        text = message.text
        obj = list(map(int,text.split(",")))
        obj = obj.index(max(obj))
        bot.send_message(message.chat.id,f"اندیس ماکزیمم عدد برابر است با: {obj}")
    except:
        bot.send_message(message.chat.id,"نه نه باید اعداد رو درست وارد کنی🙂")

@bot.message_handler(commands=["youtube"])
def video(message):
    ms = bot.send_message(message.chat.id,"واسه من لینک یوتوب بفرست تا برات ویدیو کامل رو بفرستم")
    bot.register_next_step_handler(ms,make_video)

def make_video(message):
    try:
        YouTube(message.text).streams.get_highest_resolution().download(output_path="./",filename="video.mp4")
        video = open("video.mp4","rb")
        bot.send_video(message.chat.id,video)
    except:
        bot.send_message(message.chat.id,"ارور 404 الان نمیتونم دانلود کنم😎")

@bot.message_handler(commands=["game"])
def game(message):
    global markup
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.add('دوباره می خوام بازی کنم')
    ms = bot.send_message(message.chat.id, 'بیا بازی حدس عدد انجام بده سرگرم بشی\nباید بین عدد 1 تا 20 عدد مورد نظر رو تشخیص بدی', reply_markup=markup)
    bot.register_next_step_handler(ms,make_game)

@bot.message_handler(func=lambda message:True)
def make_game(message):
    global nums
    global markup
    if message.text == 'دوباره می خوام بازی کنم':
        nums = random.randint(1,20)
        bot.reply_to(message,"بازی شروع شد")
    else:
        try:
            if int(message.text) == nums:
                markup = telebot.types.ReplyKeyboardRemove(selective=False)
                bot.send_message(message.chat.id, "👍", reply_markup=markup)
            elif int(message.text) > nums:
                bot.reply_to(message,"برو پایین")
            elif int(message.text) < nums:
                bot.reply_to(message,"برو بالا")
        except:
            bot.send_message(message.chat.id,"اونقدرا باهوش نیستم که بفهمم چی میگی\nنیاز به کمک داری؟ /help کن")
bot.polling()