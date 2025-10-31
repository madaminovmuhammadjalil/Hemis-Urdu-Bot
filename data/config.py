from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMIN")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
URL = env.str("URL")
CHANNELS = ['@URDU_PRESSA']
get_path = ['test.xlsx']
