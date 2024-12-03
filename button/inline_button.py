from aiogram import types

inline_kb_title_cryptocurrency = [[types.InlineKeyboardButton(text='Bitcoin(BTC)', callback_data='BTCUSDT'),
                                   types.InlineKeyboardButton(text='Ethereum(ETH)', callback_data='ETHUSDT')],
                                  [types.InlineKeyboardButton(text='Binance Coin(BNB)', callback_data='BNBUSDT'),
                                   types.InlineKeyboardButton(text='Cardano (ADA)', callback_data='ADAUSDT')],
                                  [types.InlineKeyboardButton(text='Solana (SOL)', callback_data='SOLUSDT'),
                                   types.InlineKeyboardButton(text='Ripple (XRP)', callback_data='XRPUSDT')],
                                  [types.InlineKeyboardButton(text='Dollar', callback_data='dollar'),
                                   types.InlineKeyboardButton(text='Euro', callback_data='euro')]]

inline_keyboard_cryptocurrency = types.InlineKeyboardMarkup(inline_keyboard=inline_kb_title_cryptocurrency)
