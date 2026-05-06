import telebot
import random

TOKEN = "ТВОЙ_ТОКЕН_БОТА"

bot = telebot.TeleBot(TOKEN)

answers = [
    "Сегодня кэфы вообще мертвые 😄",
    "На Правом вроде начинает гореть 🔥",
    "Яндекс опять чудит",
    "После 18:00 должно быть веселее",
    "Центр пока тухло",
]

@bot.message_handler(func=lambda message: True)
def reply(message):
    if random.randint(1, 4) == 1:
        bot.reply_to(message, random.choice(answers))

bot.infinity_polling()
