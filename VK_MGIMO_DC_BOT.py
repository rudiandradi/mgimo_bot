#!/usr/bin/env python
# coding: utf-8

# Импортируем нужные модули

# In[1]:


import pandas as pd
import random


# In[2]:


themes = pd.read_csv(r'themes_rus.csv')


# In[3]:


a = themes['Резолюция'].shape[0]


# In[4]:




import json
import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id


# Пишем клавиатуру

# In[6]:


keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Информация о нас',color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Как к нам попасть',color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Тема для дебатов',color=VkKeyboardColor.POSITIVE)


# Функция вывода ответа

# In[7]:


def write_message(sender,message):
    vk.messages.send (user_id = sender, message = message, random_id = get_random_id(), keyboard = keyboard.get_keyboard())


# Тело бота

# In[ ]:


vk_session = vk_api.VkApi(token="48ffce535d8216c46187da6eaeed6b9e782391faada162d8299b2ddc24e83ce623d217d438a1db1b42d30")
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 62336)
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.text != '': 
            if event.from_user:
                if (event.obj.text == 'Начать') or (event.obj.text == 'Start'):
                    write_message(event.obj.from_id, 'Привет!')
                elif event.obj.text == 'Тема для дебатов':
                    mas = themes['Резолюция'][random.randint(2153,a)]
                    write_message(event.obj.from_id, mas)
                elif event.obj.text == 'Информация о нас':
                    mas = 'Дебаты - это интеллектуальная ролевая игра, где команды доказывают позицию, выпавшую по жребию!\n\nMGIMO DC является одним из крупнейших клубов дебатов в России!\n\nНаши ребята участвуют в международных чемпионатах, работают в крутых компаниях и путешествуют по всему миру!\n\nЕсли ты хочешь развить навыки критического мышления, научиться делать сильные речи и получить море эмоций, то присоединяйся!'
                    write_message(event.obj.from_id, mas)
                elif event.obj.text == 'Как к нам попасть':
                    mas = 'Презентация нашего клуба состоится совсем скоро!\n\nДля того, чтобы прийти, просто зарегистрируйся:\nhttps://docs.google.com/forms/d/e/1FAIpQLScR3McA4NI5iO1UGW3UOdNFoNcq52oXUY36uxRyN8rpqHiElw/viewform?vc=0&c=0&w=1&flr=0&gxids=7628\n\nБолее подробная информация у нас в группе!'
                    write_message(event.obj.from_id, mas)
                elif 'дай тему' in event.obj.text.lower():
                    mas = themes['Резолюция'][random.randint(2153, a)]
                    write_message(event.obj.from_id, mas)
                elif event.obj.text != '':
                    mas = 'Выбери опцию'
                    write_message(event.obj.from_id, mas)



# In[ ]:





# In[ ]:




