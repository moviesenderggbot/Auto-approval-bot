# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22620068"))
    API_HASH = getenv("API_HASH", "11e2c113078324f7e36688baa86c3911")
    BOT_TOKEN = getenv("BOT_TOKEN", "7025776766:AAGB2MX1-TCinP1okw-aJAgALwZh9pmPZdU")
    FSUB = getenv("FSUB", "MX_FLIX")
    CHID = int(getenv("CHID", "-1002050604893"))
    SUDO = list(map(int, getenv("SUDO", "6062527012").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://0qxwx42ukf:oxfFP9wSRVYt7awV@cluster0.abjqxfe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
