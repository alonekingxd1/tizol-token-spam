from RiZoeLXSpam import Riz, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from RiZoeLXSpam import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/9acc785291052c8f8998d.jpg"

Riz_Help = "π₯ π₯ππ­π’ππ π« π¦π£ππ  π₯\n\n"
 
Riz_Help += f"__α΄α΄α΄s α΄α΄ α΄ΙͺΚα΄ΚΚα΄ ΙͺΙ΄ ΚΙͺα΄’α΄α΄Κ x sα΄α΄α΄__\n\n"

Riz_Help += f" β§ πππ΄ππ±πΎπ π²πΌπ³π β§\n\n"

Riz_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n .`restart` - to restart all spam bots \n `.addecho` - to addecho \n `.rmecho` - To remove Echo \n `.addsudo` - To add sudo user using spam bot \n\n"
 
Riz_Help += f" β§ π»π΄π°ππ΄ π²πΌπ³ β§\n\n"

Riz_Help += f" `.leave` - to leave public/private channel/groups\n\n"
 
Riz_Help += f" β§ ππΏπ°πΌ π²πΌπ³π β§\n\n"

Riz_Help += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.delayspam` - this cmd use for delay spam\n `.pornspam` - this cmd is use for porn spam\n\n"

Riz_Help += f"Β© @RiZoeLX | @DNHxHELL\n"


@Riz.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
      await Riz.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Riz_Help,
                                  buttons=[
        [
        Button.url("α΄ΚΚ α΄α΄α΄s", "https://telegra.ph/%F0%9D%97%A5%F0%9D%97%9C%F0%9D%97%AD%F0%9D%97%A2%F0%9D%97%98%F0%9D%97%9F-%F0%9D%97%AB-%F0%9D%97%A6%F0%9D%97%A3%F0%9D%97%94%F0%9D%97%A0-11-28-2")
        ],
        [
        Button.url("α΄Κα΄Ι΄Ι΄α΄Κ", "https://t.me/RiZoeLX")
        ] 
        ]
        )                                                         
