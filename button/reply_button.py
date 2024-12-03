from aiogram import types

reply_kb_title_cryptocurrency = [[types.KeyboardButton(text='Узнать цену криптовалюты')],
                                 [types.KeyboardButton(text='Доллар'), types.KeyboardButton(text='Евро')],
                                 [types.KeyboardButton(text='Главное меню')]]

reply_keyboard_cryptocurrency = types.ReplyKeyboardMarkup(keyboard=reply_kb_title_cryptocurrency,
                                                          resize_keyboard=True)
