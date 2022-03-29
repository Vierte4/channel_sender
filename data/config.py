from utils.db_creator import TxtData, JsonData

sub_channels_path = 'data\sub_channels.txt'
last_messages_path = 'data\last_message_id.json'
BOT_TOKEN = '5136453943:AAEYOv0Zmj6VPMaKTon-jYGvzWClUNyt37s'  # Забираем значение типа str
ADMINS = ['319503958','115499611']  # Тут у нас будет список из админов
main_channel = -1001281263518
sub_channels = TxtData(sub_channels_path)
last_messages = JsonData(last_messages_path)

temp_data = {}
