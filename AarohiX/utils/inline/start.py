from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


#
# Copyright (C) 2024-present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

from typing import Union
from pyrogram.types import InlineKeyboardButton
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_CHAT


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(text=_["S_B_2"], callback_data="settings_helper"),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_CHAT:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"),
                InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_CHAT}"),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}")]
            )
        if SUPPORT_CHAT:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_CHAT}")]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER_ID: Union[bool, int] = None):
    buttons = [[InlineKeyboardButton(text=_["S_B_8"], callback_data="shikharbro")]]
    if SUPPORT_CHANNEL and SUPPORT_CHAT:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"),
                InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_CHAT}"),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}")]
            )
        if SUPPORT_CHAT:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_CHAT}")]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )
    if GITHUB_REPO and OWNER_ID:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_7"], user_id=OWNER_ID),
                InlineKeyboardButton(text=_["S_B_6"], url=f"{GITHUB_REPO}"),
            ]
        )
    else:
        if GITHUB_REPO:
            buttons.append(
                [
                    InlineKeyboardButton(text=_["S_B_6"], url=f"{GITHUB_REPO}"),
                ]
            )
        if OWNER_ID:
            buttons.append(
                [
                    InlineKeyboardButton(text=_["S_B_7"], user_id=OWNER_ID),
                ]
            )
    buttons.append([InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG")])
    return buttons


def alive_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="- اضفني .", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_CHAT}"),
        ],
    ]
    return buttons
