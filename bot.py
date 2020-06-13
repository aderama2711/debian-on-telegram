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
			bot.sendMessage(chat_id, 'Ketik perintah seperti perintah pada server(khusus master && hanya untuk command selain cd dan nano)\ncd untuk masuk direktori root\nhome untuk masuk direktori home user telegram\nselain master dapat menggunakan fitur, selengkapnya ketik user.')
		elif text == '/start':
			bot.sendMessage(chat_id, 'help untuk bantuan')			
		elif text == 'user':
			bot.sendMessage(chat_id, 'Time untuk menunjukkan waktu sekarang\nSayang untuk anda yang Jones :p\n\n\n\n*untuk penambahan fitur silahkan hubungi admin(ade.ramadha@gmail.com)*')
		elif text == 'cd':
			risp=subprocess.check_output("cd", shell=True)
			bot.sendMessage(adrama, 'Direktori root')
		elif text == 'home':
			risp=subprocess.check_output("su telegram", shell=True)
			risp=subprocess.check_output("cd ~", shell=True)
			bot.sendMessage(adrama, 'Direktori home user default(Telegram)')
		elif text == 'Time':
			bot.sendMessage(chat_id, str(datetime.datetime.now()))
		elif text == 'Sayang':
			h = datetime.datetime.now().strftime('%H%M')
			ho = int(h)
			if ho>1900 and ho<2300:
				bot.sendMessage(chat_id, 'Hai sayang, selamat malam')
			elif ho>0000 and ho<1100:
				bot.sendMessage(chat_id, 'Hai sayang, selamat pagi')
			elif ho>1200 and ho<1400:
				bot.sendMessage(chat_id, 'Hai sayang, selamat siang')
			elif ho>1500 and ho<1800:
				bot.sendMessage(chat_id, 'Hai sayang, selamat sore')
		else:
            		risp=subprocess.check_output(text, shell=True)
			if risp == "":
				bot.sendMessage(user, 'Operasi telah dijalankan')
			else:	
				bot.sendMessage(user, risp)
bot = telepot.Bot('token')
MessageLoop(bot, handle).run_as_thread()
print 'Listening...'
bot.sendMessage(user,'Bot sudah dijalankan')
while 1:
    time.sleep(10)
