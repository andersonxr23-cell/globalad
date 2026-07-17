






import telebot
from telebot import types

# ⚠️ জরুরি: @BotFather থেকে পাওয়া আপনার বটের আসল টোকেনটি এখানে বসান
BOT_TOKEN = '8998386106:AAEE1vOKOTqJ_gRVmWkFMxVxF4UcrjHYx_o'


bot = telebot.TeleBot(BOT_TOKEN)

# ১. কেউ /start দিলে এই সুন্দর ওয়েলকাম মেসেজ এবং বাটনগুলো দেখাবে
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    
    # বটের কার্যকারী বাটনগুলো তৈরি করা হচ্ছে
    button1 = types.InlineKeyboardButton("🛒 Available Services", callback_data="services")
    button2 = types.InlineKeyboardButton("📞 Contact Support", callback_data="support")
    
    markup.add(button1, button2)
    
    welcome_text = (
        "🤖 **Welcome to global Ads Bot!**\n\n"
        "We provide global telegram channel advertisement and view boosting services.\n\n"
        "Please select an option from the menu below to get started:"
    )
    bot.reply_to(message, welcome_text, reply_markup=markup, parse_mode="Markdown")

# ২. বাটনগুলোতে ক্লিক করলে কী রিপ্লাই আসবে, তা এখানে সেট করা হয়েছে
@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    if call.data == "services":
        # এখানে আপনার সার্ভিসের তালিকা ও দাম স্পষ্ট করা হয়েছে
        services_text = (
            "📊 **Our Advertising Services & Pricing:**\n\n"
            "🔹 **Package 1:** 1,000 Post Views = $5\n"
            "🔹 **Package 2:** 5,000 Post Views = $20\n"
            "🔹 **Package 3:** Channel Banner Ad (24 Hours) = $10\n\n"
            "💳 _Cryptomus payment integration is currently under moderation. Once approved, you can pay instantly here._"
        )
        bot.send_message(call.message.chat.id, services_text, parse_mode="Markdown")
        
    elif call.data == "support":
        # ⚠️ জরুরি: এখানে @Mswapon এর জায়গায় আপনার আসল ইউজারনেম দিন
        support_text = (
            "📞 **Customer Support:**\n\n"
            "If you have any questions or need manual assistance, please feel free to contact our support admin directly:\n\n"
            "👉 **Admin:** @YourTelegramUsername\n\n"
            "We are available 24/7 to help you!"
        )
        bot.send_message(call.message.chat.id, support_text, parse_mode="Markdown")

print("Bot is successfully running...")
bot.infinity_polling()
