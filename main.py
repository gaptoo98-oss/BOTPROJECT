import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import random

TOKEN = "8518483815:AAEKmPB0lLLYVLJjpTau2YdEMriniI8n1FQ"
bot = telebot.TeleBot(TOKEN)
def main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton("🌡️ Факт")
    btn2 = KeyboardButton("🔥 Причины")
    btn3 = KeyboardButton("⚠️ Последствия")
    btn4 = KeyboardButton("💡 Что делать?")
    keyboard.add(btn1, btn2, btn3, btn4)
    return keyboard

def inline_buttons():
    keyboard = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton("🌡️ Факт", callback_data="fact")
    btn2 = InlineKeyboardButton("🔥 Причины", callback_data="causes")
    btn3 = InlineKeyboardButton("⚠️ Последствия", callback_data="effects")
    btn4 = InlineKeyboardButton("💡 Советы", callback_data="tips")
    keyboard.add(btn1, btn2, btn3, btn4)
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🌍 Привет! Я бот про глобальное потепление.\n\n"
        "👇 Нажимай на кнопки внизу или под сообщением!",
        reply_markup=main_keyboard()
    )
    bot.send_message(
        message.chat.id,
        "🔘 А вот еще кнопки прямо под этим сообщением:",
        reply_markup=inline_buttons()
    )

@bot.message_handler(func=lambda message: message.text == "🌡️ Факт")
def send_fact(message):
    facts = [
        "🌡️ 2023 год — самый жаркий за всю историю наблюдений",
        "🧊 Ледники Гренландии теряют 270 миллиардов тонн льда в год",
        "🌊 Уровень Мирового океана поднялся на 20 см за последние 100 лет",
        "🔥 Лесные пожары стали происходить в 2 раза чаще из-за засух",
        "🐧 Пингвины и белые медведи теряют среду обитания",
        "💨 Концентрация CO2 — самая высокая за 800 000 лет"
    ]
    bot.send_message(message.chat.id, random.choice(facts))

@bot.message_handler(func=lambda message: message.text == "🔥 Причины")
def send_causes(message):
    bot.send_message(
        message.chat.id,
        "🔥 ОСНОВНЫЕ ПРИЧИНЫ:\n\n"
        "🏭 Сжигание угля, нефти и газа\n"
        "🌳 Вырубка лесов (Амазония уменьшилась на 17%)\n"
        "🐄 Животноводство (коровы выделяют метан)\n"
        "🗑️ Свалки и отходы\n"
        "✈️ Транспорт и авиация"
    )

@bot.message_handler(func=lambda message: message.text == "⚠️ Последствия")
def send_effects(message):
    bot.send_message(
        message.chat.id,
        "⚠️ ПОСЛЕДСТВИЯ:\n\n"
        "🌡️ Аномальная жара (50°C в некоторых странах)\n"
        "🌊 Наводнения и ураганы\n"
        "🏝️ Исчезновение островных государств\n"
        "🐠 Гибель коралловых рифов\n"
        "🥤 Нехватка питьевой воды"
    )

@bot.message_handler(func=lambda message: message.text == "💡 Что делать?")
def send_tips(message):
    bot.send_message(
        message.chat.id,
        "💡 ЧТО МОЖЕТ СДЕЛАТЬ КАЖДЫЙ:\n\n"
        "🔹 Экономить электричество\n"
        "🔹 Сортировать мусор\n"
        "🔹 Ходить пешком или на велосипеде\n"
        "🔹 Сажать деревья\n"
        "🔹 Меньше покупать пластик\n"
        "🔹 Не выбрасывать еду"
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_inline(call):
    if call.data == "fact":
        facts = ["🌡️ 2023 — самый жаркий год", "🧊 Ледники тают всё быстрее", "🌊 Уровень моря растет"]
        bot.send_message(call.message.chat.id, random.choice(facts))
    elif call.data == "causes":
        bot.send_message(call.message.chat.id, "🔥 Причины: топливо, вырубка лесов, заводы")
    elif call.data == "effects":
        bot.send_message(call.message.chat.id, "⚠️ Последствия: жара, наводнения, засухи")
    elif call.data == "tips":
        bot.send_message(call.message.chat.id, "💡 Экономь свет, сортируй мусор, сажай деревья!")

    bot.answer_callback_query(call.id)

@bot.message_handler(func=lambda message: True)
def unknown(message):
    bot.send_message(
        message.chat.id,
        "❓ Нажми на кнопки внизу экрана!\nИли отправь /start",
        reply_markup=main_keyboard()
    )

bot.infinity_polling()
print("✅ Бот с кнопками запущен!")
