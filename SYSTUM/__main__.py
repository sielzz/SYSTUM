import asyncio
import importlib

from pyrogram import idle

import config
from SYSTUM import LOGGER, app, userbot
from SYSTUM.core.call import KING
from SYSTUM.misc import sudo
from SYSTUM.plugins import ALL_MODULES
from SYSTUM.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("SYSTUM.plugins" + all_module)
    LOGGER("SYSTUM.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await KING.start()
    await KING.decorators()
    LOGGER("SYSTUM").info(
        "DROP YOUR GIRLFRIEND'S NUMBER AND SEXY PIC TO @APASIIAJG JOIN @AAF_STORE FOR ANY ISSUES"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("SYSTUM").info("Stopping SYSTUM Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
