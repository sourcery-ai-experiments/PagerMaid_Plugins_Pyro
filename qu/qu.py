from pagermaid.listener import listener
from pagermaid.services import bot

usr1 = "自己"

@listener(command="qu",description="使用“qu”代替“/”,以拙劣地模仿 @fish_quote_reply_bot")
#命令

async def qu(message):

    me = await bot.get_me()
    mefirst_name = me.first_name
    melast_name = me.last_name
    idd = me.id
    if melast_name == None:
        usr = f'{mefirst_name}'
    else:
        usr = f'{mefirst_name+melast_name}'
    #读取你的 id 和昵称

    text = message.text.split(' ', 1)
    #分割命令和参数

    if len(text) > 1:
        cmd = text[0]
        text = ''.join(text[1:]).strip()
    else:
        cmd = text[0]
        text = ''
    #提取命令
        
    opt, _, opt1 = text.partition(' ')

    if opt == "" :
        return await message.edit("E:未指定内容")
    #opt 为空报错
    
    if opt1 == "" :
         opt +="了"
    #opt1 为空的话给 opt 加个"了"

    if not message.reply_to_message:
            return await message.edit(
                f"[{usr}](tg://user?id={idd})"
                f" {opt} "
                f"[{usr1}](tg://user?id={idd})"
                f" {opt1}"
                f"!"
            )
    #如果没有回复对象就是usr1（自己）
    
    reply = message.reply_to_message

    if reply.from_user:
        #回复对象是 User

        sid = reply.from_user.id
        first_name = reply.from_user.first_name
        last_name = reply.from_user.last_name
        if last_name == None:
            name = f'{first_name}'
        else:
            name = f'{first_name} {last_name}'
        await message.edit(
                f"[{usr}](tg://user?id={idd})"
                f" {opt} "
                f"[{name}](tg://user?id={sid})"
                f" {opt1}"  
                f"!",
            )
        
    else :
        #回复对象不是 User （是 频道、匿名管理 等）

        uname = reply.sender_chat.username
        name = reply.sender_chat.title
        await message.edit(
                f"[{usr}](tg://user?id={idd})"
                f" {opt} "
                f"[{name}](t.me/{uname})"
                f" {opt1}"  
                f"!",
                disable_web_page_preview=True
                #关闭链接预览
            )



@listener(command="uq",description="使用“uq”代替“\”,以拙劣地模仿 @fish_quote_reply_bot")
#和上面一样

async def uq(message):

    me = await bot.get_me()
    mefirst_name = me.first_name
    melast_name = me.last_name
    idd = me.id

    if melast_name == None:
        usr = f'{mefirst_name}'
    else:
        usr = f'{mefirst_name+melast_name}'

    text = message.text.split(' ', 1)

    if len(text) > 1:
        cmd = text[0]
        text = ''.join(text[1:]).strip()
    else:
        cmd = text[0]
        text = ''

    opt, _, opt1 = text.partition(' ')

    if opt == "" :
        return await message.edit("E:未指定内容")
    
    if opt1 == "" :
         opt +="了"

    if not message.reply_to_message:
            return await message.edit(
                f"[{usr}](tg://user?id={idd})"
                f" {opt} "
                f"[{usr1}](tg://user?id={idd})"
                f" {opt1}"
                f"!"
            )
    
    reply = message.reply_to_message

    if reply.from_user:
        sid = reply.from_user.id
        first_name = reply.from_user.first_name
        last_name = reply.from_user.last_name
        if last_name == None:
            name = f'{first_name}'
        else:
            name = f'{first_name} {last_name}'
        await message.edit(
                f"[{name}](tg://user?id={sid})"
                f" {opt} "
                f"[{usr}](tg://user?id={idd})"
                f" {opt1}"  
                f"!",
            )
        
    else :
        uname = reply.sender_chat.username
        name = reply.sender_chat.title
        await message.edit(
                f"[{name}](t.me/{uname})"
                f" {opt} "
                f"[{usr}](tg://user?id={idd})"
                f" {opt1}"  
                f"!",
                disable_web_page_preview=True
            )    