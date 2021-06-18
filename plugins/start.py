from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Group", url="https://t.me/songsrobo")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/@tom_jerry_m")]
    ])
    welcomed = f"Hey <b>{message.from_user.full_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
