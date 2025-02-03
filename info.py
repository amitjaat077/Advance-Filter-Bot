import re
from os import getenv, environ
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information *
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID','28357096'])
API_HASH = environ['API_HASH','9d3fcfcc79e60fd7cd8f69487ab87572']
BOT_TOKEN = environ['BOT_TOKEN','7733307996:AAH2NPA5HoBw3gV2Ab1SaDDgCmhsre36UAY']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg')).split()
PRIME_LOGO = (environ.get('PRIME_LOGO', 'https://telegra.ph/file/ca18e2c794f4ea1c3135b.jpg'))

# Admins, Channels & Users *
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6934214252').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '6934214252').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information *
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://fatherjaat07:TnEExUVN6dGHE9wu@cluster0.6vbar.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# LOG CHANNELS *
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
LAZY_GROUP_LOGS = int(environ.get('LAZY_GROUP_LOGS', 0))
REQ_CHANNEL = int(environ.get('REQ_CHANNEL'))
PRIME_MEMBERS_LOGS = int(environ.get('PRIME_MEMBERS_LOGS'))

# PREMIUM ACCESS *
lazydownloaders = [int(lazydownloaders) if id_pattern.search(lazydownloaders) else lazydownloaders for lazydownloaders in environ.get('PRIME_DOWNLOADERS', ' 6934214252 5251747047').split()]
PRIME_USERS = (lazydownloaders) if lazydownloaders else [] # users who can get & download file without url shortner
lazy_renamers = [int(lazrenamers) if id_pattern.search(lazrenamers) else lazrenamers for lazrenamers in environ.get('LAZY_RENAMERS', '').split()]
LAZY_RENAMERS = (lazy_renamers + ADMINS) if lazy_renamers else [] #Add user id of the user in this field those who you want to be Authentic user for file renaming features
LZURL_PRIME_USERS = [int(lazyurlers) if id_pattern.search(lazyurlers) else lazyurlers for lazyurlers in environ.get('LZURL_PRIME_USERS', ' 6934214252 5251747047').split()]

QR_CODE_IMG = environ.get('QR_CODE_IMG','https://telegra.ph/file/ca18e2c794f4ea1c3135b.jpg') #add url link of your qr code to recieve money - use telegraph bot or other source to get image
UPI_ID = environ.get('UPI_ID', '9466511384@ybl') #enter your upi id here - grab it from your online payment methods.

# Others
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/warning2_movie07/2') # Tutorial video link for opening shortlink website 
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'LazyDeveloper')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "⚡<b>File uploaded by [Movies Update™](https://t.me/MovieUpdate077)</b>⚡\n\n📂<b>File Name:</b> ⪧ {file_caption} \n <b>Size: </b>{file_size}\n\n❤")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Your Query: {query}</b> \n‌‌‌‌🎁Support: @LazyDeveloper 🎁\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 \n\n♥️ we are nothing without you ♥️ \n\n💛 Please Share Us 💛\n\n⚠️Click on the button 👇 below to get your query privately")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002030560974')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

#LazyRenamer Configs
FLOOD = int(environ.get("FLOOD", "10"))
LAZY_MODE = bool(environ.get("LAZY_MODE")) #make it true to enable file renaming feature in bot

# Requested Content template variables --- 
ADMIN_USRNM = environ.get('ADMIN_USRNM','AMIT_JAAT_07') # WITHOUT @
MAIN_CHANNEL_USRNM = environ.get('MAIN_CHANNEL_USRNM','AMIT_JAAT_07') # WITHOUT @
DEV_CHANNEL_USRNM = environ.get('DEV_CHANNEL_USRNM','AMIT_JAAT_07') # WITHOUT @
LAZY_YT_HANDLE = environ.get('LAZY_YT_HANDLE','AMIT_JAAT_07')  # WITHOUT @ [  add only handle - don't add full url  ] 
MOVIE_GROUP_USERNAME = environ.get('MOVIE_GROUP_USERNAME', "Movies_4u_movies") #[ without @ ]

# Url Shortner
URL_MODE = is_enabled((environ.get("URL_MODE","True")), False) # make it true to enable url shortner in groups or pm
URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'Krownlinks.com') #Always use website url from api section 
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', 'ac72620ccdd91a25c914646dec9ece5c30dcbec9')

#4 #> verification_steps | [Youtube@LazyDeveloper]
#URL SHORTNER FOR USER VERIFICATION
IS_LAZYUSER_VERIFICATION = is_enabled((environ.get("IS_LAZYUSER_VERIFICATION","True")),False)
LAZY_URL_SHORTNER = environ.get('LAZY_SHORTNER_URL', 'Krownlinks.com')
LAZY_SHORTNER_API = environ.GET('LAZY_SHORTNER_API','ac72620ccdd91a25c914646dec9ece5c30dcbec9')

lazy_groups = environ.get('LAZY_GROUPS','')
LAZY_GROUPS = [int(lazy_groups) for lazy_groups in lazy_groups.split()] if lazy_groups else None # ADD GROUP ID IN THIS VARIABLE 
my_users = [int(my_users) if id_pattern.search(my_users) else my_users for my_users in environ.get('MY_USERS', '').split()]
MY_USERS = (my_users) if my_users else [] #input the id of that users who can share file in file protection mode

# Online Stream and Download
PORT = int(environ.get('PORT', 8080))
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "http://{}:{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'LazyPrincess'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))    
else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)
BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001987654567")).split())) 
OWNER_USERNAME = "AMIT_JAAT_07"

lazydownloaders = [int(lazydownloaders) if id_pattern.search(lazydownloaders) else lazydownloaders for lazydownloaders in environ.get('PRIME_DOWNLOADERS', '').split()]
PRIME_DOWNLOADERS = (lazydownloaders) if lazydownloaders else []

# URL UPLOADING
BANNED_USERS = set(int(x) for x in environ.get("BANNED_USERS", "").split())
DOWNLOAD_LOCATION = "./DOWNLOADS"
MAX_FILE_SIZE = 4194304000
TG_MAX_FILE_SIZE = 4194304000
FREE_USER_MAX_FILE_SIZE = 4194304000
CHUNK_SIZE = int(environ.get("CHUNK_SIZE", 128))
HTTP_PROXY = environ.get("HTTP_PROXY", "")
OUO_IO_API_KEY = ""
MAX_MESSAGE_LENGTH = 4096
PROCESS_MAX_TIMEOUT = 0
DEF_WATER_MARK_FILE = ""
LOGGER = logging

# Adding Language Feature : 
LANGUAGES = ["hindi", "hin", "english", "eng", "korean", "kor", "urdu", "urd","chinese","chin","tamil", "tam", "malayalam", "mal",  "telugu", "tel", "kannada", "kan"]
SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]
QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]

MAX_B_TN = environ.get("MAX_B_TN", "10")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)


# Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

DISCUSSION_TITLE = "Click Here"
DISCUSSION_CHAT_USRNM = "Discusss_Here" #without @

# Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/warning2_movie07/2"

# Custom Caption Under Button #
CAPTION_BUTTON = "Get Updates"
CAPTION_BUTTON_URL = "https://t.me/MovieUpdate077"

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
# Credit @LazyDeveloper.
# Please Don't remove credit.
# Born to make history @LazyDeveloper !
# Thank you LazyDeveloper for helping us in this Journey
# 🥰  Thank you for giving me credit @LazyDeveloperr  🥰
# for any error please contact me -> telegram@LazyDeveloperr or insta @LazyDeveloperr 
# rip paid developers 🤣 - >> No need to buy paid source code while @LazyDeveloperr is here 😍😍
