import os
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
from telethon.tl.types import MessageEntityCode
from telethon import TelegramClient, events, Button
import telethon.sync #lol copied from docs
import asyncio
import logging #lol copied from docs

API_ID = os.environ.get('API_ID', None)
API_HASH = os.environ.get('API_HASH', None)
TOKEN = os.environ.get('TOKEN', None)
LOG_CHANNEL = os.environ.get('LOG_CHANNEL', None)
POST_CHANNEL = os.environ.get('POST_CHANNEL', None)
MOD_CHANNEL = os.environ.get('MOD_CHANNEL', None)
REJECT_CHANNEL = os.environ.get('REJECT_CHANNEL', None)
APPROVE_CHANNEL = os.environ.get('APPROVE_CHANNEL', None)
OWNER_USERNAME = os.environ.get('OWNER_USERNAME', None)
AUCTION_GROUP_LINK = os.environ.get('AUCTION_GROUP_LINK', None)
AUCTION_CHANNEL_LINK = os.environ.get('AUCTION_CHANNEL_LINK', None)
START_IMAGE = os.environ.get('START_IMAGE', None)
CAPTION = os.environ.get('CAPTION', None)
PENDING_CHANNEL_LINK = os.environ.get('PENDING_CHANNEL_LINK', None)
APPROVED_CHANNEL_LINK = os.environ.get('APPROVED_CHANNEL_LINK', None)
REJECTED_CHANNEL_LINK = os.environ.get('REJECTED_CHANNEL_LINK', None)
SCAMMER_CHANNEL_LINK = os.environ.get('SCAMMER_CHANNEL_LINK', None)
COMMUNITY_NAME = os.environ.get('COMMUNITY_NAME', None)
COMMUNITY_LINK = os.environ.get('COMMUNITY_LINK', None)
APPROVE_LIST = os.environ.get('APPROVE_LIST', None)
ENEMY_LIST = os.environ.get('ENEMY_LIST', None)


api_id = API_ID
api_hash = API_HASH
bot_token = TOKEN
log_channel = LOG_CHANNEL
post_channel = POST_CHANNEL
log_channel = int(log_channel)
post_channel = int(post_channel)
scammer_channel = int(MOD_CHANNEL)
reject_channel = int(REJECT_CHANNEL)
approve_channel = int(APPROVE_CHANNEL)
CAPTION = str(CAPTION)
COMMUNITY_LINK = str(COMMUNITY_LINK)
OWNER_LINK = "https://t.me/"+OWNER_USERNAME
AUCTION_CHANNEL_LINK = str(AUCTION_CHANNEL_LINK)
AUCTION_GROUP_LINK = str(AUCTION_GROUP_LINK)



client = TelegramClient('aucbot', api_id, api_hash).start(bot_token=bot_token) #i dont really understand it lol but without this bot wont work

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', #copy pasted from telethon docs lol..... so usually it logs error
                    level=logging.WARNING)



@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    sender = await event.get_sender()
    await client.send_file(event.sender_id, START_IMAGE, caption = CAPTION
        ,
        buttons=[
        [
            Button.url('AUCTION', AUCTION_GROUP_LINK),
            Button.url('CHANNEL', AUCTION_CHANNEL_LINK)
        ],
        [
            Button.url('OWNER', OWNER_LINK),
        ]
      ]
    )




user_cache = {}

@client.on(events.NewMessage(pattern='/sell'))
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
    await client.edit_message(event.sender_id, event.message_id, 'OK! Legendary', buttons=Button.clear())
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
            Button.url('PENDING', PENDING_CHANNEL_LINK)
        ],
        [
            Button.url('APPROVED', APPROVED_CHANNEL_LINK),
            Button.url('REJECTED', REJECTED_CHANNEL_LINK)
        ],
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
            Button.url('PENDING', PENDING_CHANNEL_LINK)
        ],
        [
            Button.url('APPROVED', APPROVED_CHANNEL_LINK),
            Button.url('REJECTED', REJECTED_CHANNEL_LINK)
        ],
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

client.start()
client.run_until_disconnected()
