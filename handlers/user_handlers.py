from button.reply_button import reply_keyboard_cryptocurrency
from button.inline_button import inline_keyboard_cryptocurrency
from pars.pars import return_price_crypto, return_price_dollar, return_price_euro
from state.user_state import user_state

from aiogram import types, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


async def start_1(message: types.Message, state: FSMContext):
    await message.answer(f'Здравствуйте, {message.from_user.first_name}\n'
                         f'Напишите тикер криптовалюты, которая вас интересует\n'
                         f'или выберите из предложенных',
                         reply_markup=inline_keyboard_cryptocurrency)
    await state.set_state(user_state.name_crypto)


async def start_2(message: types.Message, state: FSMContext):
    await message.answer(f'Напишите тикер криптовалюты, которая вас интересует',
                         reply_markup=reply_keyboard_cryptocurrency)
    await state.set_state(user_state.name_crypto)


async def price_1(message: types.Message, state: FSMContext):
    if return_price_crypto(str(message.text).upper() + 'USDT') is None:
        await message.answer('Нет такой криптовалюты',
                             reply_markup=reply_keyboard_cryptocurrency)
    else:
        await message.answer(f"На данный момент цена {message.text.upper()}\n"
                             f"{float(return_price_crypto(str(message.text.upper()) + 'USDT'))} $\n"
                             f"{round(float(return_price_crypto(str(message.text.upper()) + 'USDT')) * float(return_price_dollar()), 2)}"
                             f" рублей",
                             reply_markup=reply_keyboard_cryptocurrency)
    await state.clear()


async def price_2(query: types.CallbackQuery):
    await query.message.answer(f"На данный момент цена {str(query.data)[:-4]}\n"
                               f"{return_price_crypto(query.data)} $\n"
                               f"{round(float(return_price_crypto(query.data)) * float(return_price_dollar()), 2)} рублей",
                               reply_markup=reply_keyboard_cryptocurrency)


async def price_dollar_1(query: types.CallbackQuery):
    await query.message.answer(f"На данный момент цена доллара\n"
                               f"{return_price_dollar()} рублей",
                               reply_markup=reply_keyboard_cryptocurrency)


async def price_dollar_2(message: types.Message):
    await message.answer(f"На данный момент цена доллара\n"
                         f"{return_price_dollar()} рублей",
                         reply_markup=reply_keyboard_cryptocurrency)


async def price_euro_1(query: types.CallbackQuery):
    await query.message.answer(f"На данный момент цена евро\n"
                               f"{return_price_euro()} рублей",
                               reply_markup=reply_keyboard_cryptocurrency)


async def price_euro_2(message: types.Message):
    await message.answer(f"На данный момент цена евро\n"
                         f"{return_price_euro()} рублей",
                         reply_markup=reply_keyboard_cryptocurrency)


def register(dp: Dispatcher):
    dp.message.register(start_1, Command('start'))
    dp.message.register(start_1, F.text == 'Главное меню')

    dp.callback_query.register(price_dollar_1, F.data == 'dollar')
    dp.message.register(price_dollar_2, F.text == 'Доллар')

    dp.callback_query.register(price_euro_1, F.data == 'euro')
    dp.message.register(price_euro_2, F.text == 'Евро')

    dp.message.register(start_2, F.text == 'Узнать цену криптовалюты')

    dp.message.register(price_1, user_state.name_crypto)

    dp.callback_query.register(price_2, F.data == 'BTCUSDT')
    dp.callback_query.register(price_2, F.data == 'ETHUSDT')
    dp.callback_query.register(price_2, F.data == 'BNBUSDT')
    dp.callback_query.register(price_2, F.data == 'ADAUSDT')
    dp.callback_query.register(price_2, F.data == 'SOLUSDT')
    dp.callback_query.register(price_2, F.data == 'XRPUSDT')
