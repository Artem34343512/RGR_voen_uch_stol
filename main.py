from telegram import Bot, Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, Application
from queue import Queue
from pathlib import Path

# Обработчик команды /start
async def start(update: Update, context):
  await update.message.reply_text(
      "Добро пожаловать! Я помогу вам заполнить личную карточку военнообязанного.\n"
      "Для начала, введите /fill чтобы начать заполнение.",
      reply_markup=ReplyKeyboardRemove()
  )

# Обработчик команды /fill
async def fill(update: Update, context):
  context.user_data['index'] = 0
  await update.message.reply_text(questions[0], reply_markup=ReplyKeyboardRemove())

# Обработчик текстовых сообщений
async def handle_message(update: Update, context):
 index = context.user_data.get('index', 0)
 if index < len(questions):
     context.user_data[index] = update.message.text # Сохраняем ответ пользователя
     if index + 1 < len(questions):
         context.user_data['index'] = index + 1
         await update.message.reply_text(questions[index + 1], reply_markup=ReplyKeyboardRemove())
     else:
         context.user_data['index'] = index + 1
         await create_card(update, context)
 else:
     await create_card(update, context)

# Создание карточки и переход к следующему заполнению
async def create_card(update: Update, context):
  # Получение данных из context.user_data
  card = []
  for index, question in enumerate(questions):
      answer = context.user_data.get(index)
      card.append(f"{question}: {answer}")

  # Вывод карточки на экран
  for item in card:
      await update.message.reply_text(item)

  # Запись карточки в файл
  file_path = Path(r'C:\Users\DNS\Desktop\таблица.txt')
  with file_path.open('a') as f:
      for item in card:
          f.write(item + '\n')

  # Очистка данных из context.user_data
  context.user_data.clear()

  # Отправка сообщения о сохранении карточки
  await update.message.reply_text("Спасибо! Карточка сохранена.")
  await fill(update, context)

# Список вопросов
questions = [
  "ФИО",
  "Дата рождения",
  "Должность",
  "Образование",
  "Семейное положение",
  "Адрес",
  "Номер телефона",
  "Категория",
  "Введите данные документа воинского учета",
  "Воинское звание",
]

# Токен вашего бота
TOKEN = "6712135740:AAHqSn7Sj_GjTwguL78Q5-DwhedQxC7Hb7c"

# Создание экземпляра Bot
bot = Bot(token=TOKEN)
# Создание очереди обновлений
update_queue = Queue()

# Создание экземпляра Application с передачей очереди обновлений
application = Application.builder().token(TOKEN).build()

# Регистрация обработчиков команд
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("fill", fill))

# Регистрация обработчика текстовых сообщений
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Запуск бота
application.run_polling(1.0)