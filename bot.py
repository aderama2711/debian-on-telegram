import sys
import time
import random
import datetime
import telepot
import subprocess
from telepot.loop import MessageLoop
adrama='413983527'
def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)
	text = msg['text']	
	if content_type == 'text':
		if text == 'help':
			bot.sendMessage(chat_id, 'Ketik perintah seperti perintah pada server(khusus master && hanya untuk command selain cd dan nano)')
		elif text == '/start':
			bot.sendMessage(chat_id, 'Ketik help untuk bantuan')
		else:
			risp=subprocess.check_output(text, shell=True)
             		if risp == "":
				bot.sendMessage(adrama, 'Operasi telah dijalankan')
			else:	
				bot.sendMessage(adrama, risp)
bot = telepot.Bot('391383020:AAHFLVnwpTYzMmQZs-3HUTBROFrOUdbiTPk')
MessageLoop(bot, handle).run_as_thread()
print 'Listening...'
bot.sendMessage(adrama,'Bot sudah dijalankan')
while 1:
    time.sleep(10)
