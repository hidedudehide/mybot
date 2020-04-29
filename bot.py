import telebot
import requests
import time



bot = telebot.TeleBot('1165307703:AAFqwD_-QClixH-EbjJzuS1kIS4c4G_HyNE')



#methodGetUpdates = 'https://api.telegram.org/bot{token}/getUpdates?offset=-10'.format(token=config.TOKEN)


id_list = []
schet_list = []


first_list = [] #список будет хранить все текстовые сообщения, отправленные с канала
number_list = [] #список будет хранить себе номер вопроса по которому будем обращаться
channel_id = '-1001455312363'
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id,'Hello, {0.first_name}! Nice to meet you!\nSend me number of question and  write your opinion '
                     'about this question!\n\nFor example: "I think it"s a good idea because you will spend time with benefit!"\n\n'
                                     'But you can send only 1 answer or question per 1 hour. \n\nThis is a simple spam-protect in my channel!'.format(message.from_user))

#user_dict = dict.fromkeys([user_id], schet)
@bot.message_handler(content_types=['text'])
def get_msg(message):
    #schet = 0
    user_id = message.from_user.id
    id_list.append(user_id)

    for i in range(0,len(id_list)):
        i = 0
        schet_list.append(i)

    for elem in id_list:
        user_dict = dict.fromkeys([elem], schet_list[i])
    #user_dict = dict.fromkeys([user_id], 0)
    text_from_user = message.text
    for key in user_dict:
        if text_from_user == message.text:
            user_dict[key] = user_dict[key] + 1
            # if user_dict[key] == 1:
            #     schet_list[i] = schet_list[i] + 1
            # if user_dict[key] == 2:
            #     schet_list[i] = schet_list[i] + 1
            # if user_dict[key] == 3:
            #     schet_list[i] = schet_list[i]  + 1
            #per_day(user_dict[key])
            if user_dict[key] == 1:
                methodSend = 'https://api.telegram.org/bot{token}/sendMessage?chat_id=-1001455312363&text={text}'.format(token=config.TOKEN,
                text=("Ответ через бота @Think_AI_bot:\n" + text_from_user))
                #methodSend = 'https://api.telegram.org/bot{token}/sendMessage?chat_id=-1001484250624&text={text}'.format(
                    #token=config.TOKEN,
                    #text=("Ответ через бота @Think_AI_bot:\n" + text_from_user))
                response = requests.post(methodSend)
                result = response.json()
                time.sleep(1)
                bot.send_message(message.chat.id, "Sorry! You can't send message now.You should wait 1 hour for new message!\n\nCome back after 1 hour!😉")
                time.sleep(3600)
                user_dict[key] = 0
                #return schet
    #first_list.append(result)
    if message.text == 'show':
        bot.send_message(message.chat.id, str(result) +'\n\n'+  str(user_dict) + '\n\n' + str(id_list))
    #if message.text == 'send':
        #bot.send_message(message.chat.id, 'We send' + str(result2))


bot.polling(none_stop=True)
