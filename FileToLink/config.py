import os


class Config:
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    Token = os.environ.get("BOT_TOKEN")
    Session = os.environ.get("Session_String")
    if Session is None or Session == "":
        Session = ":memory:"
    App_Name = os.environ.get("APP_NAME")
    Port = int(os.environ.get("PORT"))
    Archive_Channel_ID = int(os.environ.get("ARCHIVE_CHANNEL_ID"))
    Start_Message = os.environ.get("Start_Message")
    Bot_Channel = os.environ.get("Bot_Channel_UserName")
    if Bot_Channel and Bot_Channel.startswith("@"):
        Bot_Channel = Bot_Channel[1:]
    elif Bot_Channel == "":
        Bot_Channel = None

    Link_Root = f"https://{App_Name}.herokuapp.com/"
    Download_Folder = "Files"
    Dev_Channel = "shadow_bots"
    Bot_UserName = None  # The bot will set it after starting
    Part_size = 10 * 1024 * 1024  # (10MB) For Pyrogram
    Buffer_Size = 512 * 1024  # For Quart
    Pre_Dl = 3  # How many parts to download from telegram before client request them
    Separate_Time = 4  # (seconds)  wait time between messages if user send more than one
    Sleep_Threshold = 60  # (Seconds) sleep threshold for flood wait exceptions
    Max_Fast_Processes = 1  # How many links user can update them to fast links at the same time


class Strings:
    start = Config.Start_Message
    dl_link = "🔗 لینک دانلود"
    st_link = "🎞 لینک استریم"
    generating_link = "**⏳ کمی صبر کنید...**"
    bot_channel = "📢 Bot Channel"
    dev_channel = "🤖 Developer"
    fast = "⚡️**پیوند به یک لینک سریع به روز شد**"
    update_link = "⚡ به لینک سریع اپدیت شد"
    update_limited = (f"⛔ شما میتوانید هر{Config.Max_Fast_Processes} لینک را بروز کنید, "
                      "لطفا صبر کنید تا به روز رسانی قبلی کامل شود")
    re_update_link = "🔄 به روز رسانی مجدد لینک"
    already_updated = "پیوند قبلاً به روز شده است"
    wait_update = "⏳ در حال اپدیت..."
    wait = "⏳ لطفا صبر کنید..."
    progress = "⏳ پیشرفت"
    file_not_found = "⚠️فایل یافت نشد، لطفا دوباره آن را ارسال کنید"
    delete_manually_button = "⚠️می توانید آن را حذف کنید"
    delete_forbidden = "ربات نمی تواند پیام های قدیمی تر از 48 ساعت را حذف کند، می توانید این پیام را به صورت دستی حذف کنید"
    force_join = "⚠ برای استفاده از این ربات به کانال ربات بپیوندید"
