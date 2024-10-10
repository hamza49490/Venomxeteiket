from dotenv import load_dotenv
from os import getenv

load_dotenv()

# Required Variables
API_ID = int(getenv("API_ID", "26249846")
API_HASH = getenv("API_HASH", "d834f962ac4f88bf1d9aad19b264a865")
BOT_TOKEN = getenv("BOT_TOKEN", "7944281902:AAEo4HgCmsKdwx06Ce2STDVl8_ANrTv7oPs")
STRING_SESSION = getenv("STRING_SESSION", "BQGQinYAcTJcN9AEyEBRVIT4-Ly64BG4AwiwMuZEDxk9x1_x4Op9zGSOAuYbxxLHz-MNplvDFvgc9F0ui0PlLB35J7hQaQKQr_2zwpBnt_kfWoNzrnLiVQwtTUJ4Fvcr47Yn9eo-es043tB06BJiIb8CTavVMRSrm0-eRJAn7-IbRD5YRZ_C21Z8c8n6UQG6298VSNpvKt1bqYpv2quxqSNbCHn3rvf1Q2_FB6QipLTOcjvVGJBl3kL39jJtTkvnnEQ9xhBRoNHkmdGt3QMY4nzebPNwL1CqzatQH-sX0BI7rZ2f7c171j-QITr4EfwA6iwLdBsQAU2a7051m1ui_Xw-GULHUgAAAAGOWX0JAA")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002028213552"))


# Optional Variables
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())


# Don't Change After This Line.
COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')
