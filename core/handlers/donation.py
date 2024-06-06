from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message, PreCheckoutQuery, LabeledPrice
from core.Settings import settings

router = Router()  # [1]


@router.message(Command("donation"))  # [2]
async def cmd_start(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Пожертвование через Telegram бот",
        description="Пожертвование через Telegram бот",
        payload="donation",
        provider_token=settings.bots.donation_provider_token,
        currency="rub",
        prices=[
            LabeledPrice(label="Пожертвование", amount=10000),
        ],

        max_tip_amount=50000000,

        suggested_tip_amounts=[1000, 5000, 10000, 50000],
        start_parameter="donation",
        provider_data=None,
        need_name=True,
        need_email=True,
        need_phone_number=True,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=False,
        protect_content=True,
        request_timeout=15
    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message, bot: Bot):
    await bot.send_message(message.chat.id, "Спасибо за пожертвование!")
