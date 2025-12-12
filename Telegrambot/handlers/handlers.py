from aiogram import types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from services.crypto import get_price


async def start_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💎 TON")],
            [KeyboardButton(text="₿ BTC")],
            [KeyboardButton(text="Ξ ETH")],
        ],
        resize_keyboard=True
    )
    await message.answer("Вибери криптовалюту:", reply_markup=keyboard)


async def button_handler(message: types.Message):
    t = message.text.lower().strip()

    if "ton" in t or "💎" in t:
        coin = "TON"
        price = await get_price("ton")

    elif "btc" in t or "₿" in t:
        coin = "BTC"
        price = await get_price("btc")

    elif "eth" in t or "ξ" in t:
        coin = "ETH"
        price = await get_price("eth")

    else:
        return await message.answer("Не знаю такої команди 🤔")

    await message.answer(f"💰 Ціна {coin}: *{price} USD*", parse_mode="Markdown")


def register_handlers(dp):
    dp.message.register(start_handler, Command("start"))
    dp.message.register(button_handler)
