class script(object):
    START_TXT = """đˇđ´đťđž {},
đźđ˘ đđđđ , <a href='http://t.me/maariimdbbot'>Maari</a>, đ¸đ'đ đđđđ˘ đđđđ˘ đđđđ đđđ đđ đđ đ˘đđđ đđđđđ đđđ đđđđ đđ đđđđđ, đđđđđ đđđ đ¸'đđ đđđđđđđ đđđđđđ đđđđđ đż
"""
    HELP_TXT = """đˇđ´đ {}
đđŚđłđŚ đđ´ đđŠđŚ đđŚđ­đą đđ°đł đđş đđ°đŽđŽđ˘đŻđĽđ´."""
    ABOUT_TXT = """
   đđđ˘đ¨đ§ đ đŚđ
âľâľâľâľâľâľâľâľâľâľâľâľâľâľâľâľâľâľâľâľ
ââââââ° đđđđđđđđ âąâââąâŰŞŰŞ
ââ­ââââââââââââââââŁ 
ââŁâŞź đźđ đ˝đ°đźđ´ - <a href="http://t.me/maariimdbbot"> Maari </a>
ââŁâŞź đ˛đđ´đ°đđžđ- <a href="https://t.me/Master_Brain1"> Hacker </a>
ââŁâŞź đťđ¸đąđđ°đđ - đżđđđžđśđđ°đź
ââŁâŞź đťđ°đ˝đśđđ°đśđ´ - đżđđđˇđžđ˝ đš
ââŁâŞź đłđ°đđ°đąđ°đđ´ - đźđžđ˝đśđž đłđą
ââŁâŞź đđ´đđđ´đ -  đˇđ´đđžđşđ
ââŁâŞź đąđđ¸đťđ đđđ°đđ - v1.0.2 [ đąđ´đđ° ]
ââ°ââââââââââââââââŁ âââââââââââââââââââââąâŰŞŰŞ"""
    SOURCE_TXT = """<b>NOTE:</b>
- đ° đđ  đ đđđđ đđđđđđ đđđđđđđ. 
- ŐOáááá´ áOáŞá´ - <a href="https://t.me/nokkiyiruno"> đđđđđ đđđĽđ </a>
  

<b>DEVS:</b>
- <a href=https://t.me/Master_Brain1>Hacker</a>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
â˘/whois :-give a user full details"""
    FUN_TXT ="""<b>Gá´á´á´s</b> 
    
<b>đ˛ NOTHING MUCH JUST SOME FUN THINGS</b>
tđđ đđđđ đŽđđ: 
đŁ. /dice - Roll The Dice 
đ¤. /Throw đđ /Dart - đłđ đŹđşđđž Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin the Lucky"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â˘ /filter - <code>add a filter in chat</code>
â˘ /filters - <code>list all the filters of a chat</code>
â˘ /del - <code>delete a specific filter in chat</code>
â˘ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """<b>đźSong Downloadđź</b>
Song Download Module, For Those Who Love Music

<b>đ Command đ</b>

- /song [Song Name] - To Download Music đ

<b>đUsageđ</b>
- Can Be Used By Everyone
- Works in bot pm

Made By @albintko"""
    PIN_TXT ="""<b>PIN MODULE</b>
<b>Pin :</b>

<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>

<b>đ Commands & Usage:</b>

â /pin :- Pin The Message You Replied To Message To Send A Notification To Group Members
â /unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

â˘ /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

â˘ These commands works on both pm and group.
â˘ These commands can be used by any group member."""
    GTRANS_TXT = """Help: <b> TTS đ¤ module:</b>

Translate text to speech

<b>Commands and Usage:</b>

â˘ /tts <text> : convert text to speech

<b>NOTE:</b>

â˘ IMDb should have admin privillage.
â˘ These commands works on both pm and group.
â˘ IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>đ Ping:</b>

Helps you to know your ping đśđźââď¸

<b>Commands:</b>

â˘ /alive - To check you are alive.
â˘ /help - To get help 
â˘ /ping - To get your ping 
â˘ /repo - Source Code. 

<b>đšUsageđš :</b>

â˘ This commands can be used in pms and groups
â˘ This commands can be used buy everyone in the groups and bots pm
â˘ Share us for more features"""
    TELE_TXT = """<b>âŤď¸HELP: TelegraphâŞď¸</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

đ¤§ /telegraph - Send me Picture or Vide Under (5MB)

<b>NOTE:</b>

â˘ This Command Is Available in goups and pms
â˘ This Command Can be used by everyone"""
    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """<b>đŁPurgeđŁ</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

â /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Samantha supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â˘ /connect  - <code>connect a particular chat to your PM</code>
â˘ /disconnect  - <code>disconnect from a chat</code>
â˘ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
â˘ /id - <code>get id of a specifed user.</code>
â˘ /info  - <code>get information about a user.</code>
â˘ /imdb  - <code>get the film information from IMDb source.</code>
â˘ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â˘ /logs - <code>to get the rescent errors</code>
â˘ /stats - <code>to get status of files in db.</code>
â˘ /delete - <code>to delete a specific file from db.</code>
â˘ /users - <code>to get list of my users and ids.</code>
â˘ /chats - <code>to get list of the my chats and ids </code>
â˘ /leave  - <code>to leave from a chat.</code>
â˘ /disable  -  <code>do disable a chat.</code>
â˘ /ban_user  - <code>to ban a user.</code>
â˘ /unban_user  - <code>to unban a user.</code>
â˘ /channel - <code>to get list of total connected channels</code>
â˘ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â đđžđđ°đť đľđ¸đťđ´đ: <code>{}</code>
â đđžđđ°đť đđđ´đđ: <code>{}</code>
â đđžđđ°đť đ˛đˇđ°đđ: <code>{}</code>
â đđđ´đł đđđžđđ°đśđ´: <code>{}</code> đźđđą
â đľđđ´đ´ đđđžđđ°đśđ´: <code>{}</code> đźđđą"""
    LOG_TEXT_G = """#đđđ°đđŤđ¨đŽđŠ
âŽ đđŤđ¨đŽđŠ âşâş {}(<code>{}</code>)
âŽ đđ¨đ­đđĽ đđđŚđđđŤđŹ âşâş <code>{}</code>
âŽ đđđđđ đđ˛ âşâş {}
"""
    LOG_TEXT_P = """#đđđ°đđŹđđŤ
âŽ đđ âşâş <code>{}</code>
âŽ đđđŚđ âşâş {}
"""
    REPORT_TXT = """â¤ đđđĽđŠ: Rá´á´á´Ęá´ â ď¸

đđđđ đđđđđđđ đđđđđ đ˘đđ đđ đđđđđđ đ đđđđđđđ đđ đ đđđđ đđ đđđ đđđđđđ đđ đđđ đđđđđđđđđđ đđđđđ. đłđđ'đ đđđđđđ đđđđ đđđđđđđ.

â¤ đđ¨đŚđŚđđ§đđŹ đđ§đ đđŹđđ đ:

âŞ/report đđ @admins - đłđ đđžđđđđ đş đđđžđ đđ đđđž đşđ˝đđđđ (đđžđđđ đđ đş đđžđđđşđđž)."""

    CORONA_TXT = """â¤ đđđĽđŠ: đ˘đđđđ˝đž

đđđđ đ˛đđđđđđ đđđđđ đ˘đđ đđ đđđđ  đđđ˘đđ đđđđđđđđđđđ đđđđđ đđđđđđ

â¤ đđ¨đŚđŚđđ§đđŹ đđ§đ đđŹđđ đ:

âŞ /covid - đđđž đđđđ đźđđđđşđđ˝ đđđđ đđđđ đźđđđđđđ đđşđđž đđ đđžđ đźđđđđ˝đž đđđżđđđđşđđđđ

âđ¤đđşđđđđž:
/covid đ¨đđ˝đđş"""

    URLSHORT_TXT = """â¤ đđđĽđŠ: đ´đđ đđđđđđđžđ

đđđđ đđđđđđđ đđđđđ đ˘đđ đđ đđđđđ đ đđđ 

â¤ đđ¨đŚđŚđđ§đđŹ đđ§đ đđŹđđ đ:

âŞ /short: đđđž đđđđ đźđđđđşđđ˝ đđđđ đđđđ đđđđ đđ đđžđ đđđđđđžđ˝ đđđđđ

âđ¤đđşđđđđž:
/short https://t.me/Master_Brain1"""

    VIDEO_TXT ="""đđđĄđĽ đđ¤đ§ đżđ¤đŹđŁđĄđ¤đđ đźđŁđŽ đđđđđ¤ đđ§đ¤đ˘ đđ.

â˘ đđ´đ˘đ¨đŚ
đ đ°đś đđ˘đŻ đđ°đ¸đŻđ­đ°đ˘đĽ đđŻđş đđŞđĽđŚđ° đđłđ°đŽ đ đ°đśđľđśđŁđŚ

đđ¤đŹ đđ¤ đđ¨đ
â˘ đđşđąđŚ /video or /mp4 đđŻđĽ (đđŞđĽđŚđ° Link)
â˘ đđšđ˘đŽđąđ­đŚ:
/đŽđą4 https://youtu.be/Your Link"""

    ZOMBIES_TXT = """đđđĄđĽ đđ¤đ§ đđđđ 

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
â˘ /inkick - command with required arguments and i will kick members from group.
â˘ /instatus - to check current status of chat member from group.
â˘ /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
â˘ /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
â˘ /dkick - to kick deleted accounts."""

    IMAGE_TXT = """â¤ đđđĽđŠ: Iá´á´É˘á´

đđđđ đđđđđđđ đđđđđ đ˘đđ đđ đđđđ đđđđđ đđđđ˘ đđđđđđ˘ 

â¤ đđ¨đŚđŚđđ§đđŹ đđ§đ đđŹđđ đ:

âŞ đŠđđđ đđžđđ˝ đđž đş đđđşđđž đđ đžđ˝đđ â¨

đŹđşđ˝đž đťđ @Devil"""

    STICKER_TXT = """đđđĄđĽ đđ¤đ§ đđŠđđđ đđ§ đđ
â˘ đđ¨đđđ
To Get Sticker ID
  â­ đđ¤đŹ đđ¤ đđ¨đ
â Reply To Any Sticker [/stickerid]"""

    YTTHUMB_TXT = """đđđĄđĽ đđ¤đ§ đżđ¤đŹđŁđĄđ¤đđ đđ¤đŞđŠđŞđđ đđđđđ¤ đđđŞđ˘đđŁđđđĄ
â­đđ¤đŹ đđ¤ đđ¨đ
đđşđąđŚ /ytthumb đđŻđĽ đđŞđĽđŚđ° đđŞđŻđŹ

â˘ đđšđ˘đŽđąđ­đŚ
/ytthumb https://youtu.be/yourlink"""

    ABOOK_TXT = """â¤ đđđĽđŠ: đ đđ˝đđđťđđđ

đđđ đđđ đđđđđđđ đ đżđłđľ đđđđ đđ đ đđđđđ đđđđ đ đđđ đđđđ đđđđđđđ âŻ

â¤ đđ¨đŚđŚđđ§đđŹ đđ§đ đđŹđđ đ:

âŞ /audiobook: đąđžđđđ đđđđ đźđđđđşđđ˝ đđ đşđđ đŻđŁđĽ đđ đđžđđžđđşđđž đđđž đşđđ˝đđ"""

    FILE_TXT = """â¤ đđđĽđŠ: đĽđđđž đ˛đđđđž

đđđđ đđđđ đđđđđđđ đ đđđ đđđđđ đđđđđ đđđ đđđđ đ˘đđ đ đđđđđđđđđ đđđđ đ đđđ đđđđ đđđđ đ đđđ đđđđđ đđđđ đđđđđ đ˘đđ đđđđ đđ đđđđ đđđ˘ đđđđđđđ đ đđđđđđ đđđđđđ đđ

â¤ đđ¨đŚđŚđđ§đđŹ đđ§đ đđŹđđ đ:

âŞ /plink - đąđžđđđ đđ đşđđ đđžđ˝đđş đđ đđžđ đđđđ
âŞ /pbatch - đ´đđž đđđđ đđşđ˝đđş đđđđ đđđđ đđđđ đźđđđđşđđ˝
âŞ /batch - To create link for multiple post
âđ¤đđşđđđđž:
/pbatch <code>https://t.me/Sflix2k/497 https://t.me/Sflix2k/498</code>"""

    GTRANS_TXT = """â¤ đđđĽđŠ: đŚđđđđđž đłđđşđđđđşđđžđ

đđđđ đđđđđđđ đđđđđ đ˘đđ đđ đđđđđđđđđ đ đđđĄđ đđ đşđđ đđđđđđđđđ đ˘đđ đ đđđ. đđđđ đđđđđđđ đ đđđđ đđ đđđđ đđ đđđ đđđđđ âŻ

â¤ đđ¨đŚđŚđđ§đđŹ đđ§đ đđŹđđ đ:

âŞ/tr - đłđ đđđşđđđđşđđžđ đđžđđđ đđ đş đđđžđźđđżđź đđşđđđđşđđž

â¤ đ­đđđž:
đśđđđđž đđđđđ /tr đđđ đđđđđđ˝ đđđžđźđđżđ đđđž đđşđđđđşđđž đźđđ˝đž

âđ¤đđşđđđđž: /đđ đđ
â˘ đžđ = đ¤đđđđđđ
â˘ đđ = đŹđşđđşđđşđđşđ
â˘ đđ = đ§đđđ˝đ"""

    RESTRIC_TXT = """â¤ đđđĽđŠ: Má´á´á´ đŤ

đđđđđ đđđ đđđ đđđđđđđđ đ đđđđđ đđđđđ đđđ đđđ đđ đđđđđđ đđđđđ đđđđđ đđđđ đđđđđđđđđđđ˘.

âŞ/ban: đłđ đťđşđ đş đđđžđ đżđđđ đđđž đđđđđ.
âŞ/unban: đłđ đđđťđşđ đş đđđžđ đđ đđđž đđđđđ.
âŞ/tban: đłđ đđžđđđđđşđđđđ đťđşđ đş đđđžđ.
âŞ/mute: đłđ đđđđž đş đđđžđ đđ đđđž đđđđđ.
âŞ/unmute: đłđ đđđđđđž đş đđđžđ đđ đđđž đđđđđ.
âŞ/tmute: đłđ đđžđđđđđşđđđđ đđđđž đş đđđžđ.

â¤ đ­đđđž:
đśđđđđž đđđđđ /tmute đđ /tban đđđ đđđđđđ˝ đđđžđźđđżđ đđđž đđđđž đđđđđ.

âđ¤đđşđđđđž: /đđťđşđ 2đ˝ đđ /đđđđđž 2đ˝.
đ¸đđ đźđşđ đđđž đđşđđđžđ: đ/đ/đ˝. 
 â˘ đ = đđđđđđžđ
 â˘ đ = đđđđđ
 â˘ đ˝ = đ˝đşđđ"""
    CREATOR_REQUIRED = """â<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "â **Arguments Required**"
      
    KICKED = """âď¸ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """đŽ Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """â<b>I Am Not An Admin Here\n__Leaving This Chat, Add Me Again As Admin With Ban User Permission.</b>"""
      
    DKICK = """âď¸ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>Collecting Users Information...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
