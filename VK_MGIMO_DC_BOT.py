#!/usr/bin/env python
# coding: utf-8

# Импортируем нужные модули

# In[1]:


import pandas as pd
import random


# In[2]:


themes = pd.read_csv(r'themes_rus.csv')
themes_eng = pd.read_csv(r'themes_eng.csv')

# In[3]:


a = themes['Резолюция'].shape[0]
b = themes_eng['Резолюция'].shape[0]

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




# In[6]:


keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Информация о нас',color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Как к нам попасть',color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Тема для дебатов',color=VkKeyboardColor.POSITIVE)

keyboard2 = VkKeyboard(one_time=True)
keyboard2.add_button('Русский',color=VkKeyboardColor.PRIMARY)
keyboard2.add_button('English',color=VkKeyboardColor.PRIMARY)
# Функция вывода ответа
eng_keyboard = VkKeyboard(one_time=True)
eng_keyboard.add_button('Information',color=VkKeyboardColor.PRIMARY)
eng_keyboard.add_line()
eng_keyboard.add_button('How to join us',color=VkKeyboardColor.PRIMARY)
eng_keyboard.add_line()
eng_keyboard.add_button('Theme for debates',color=VkKeyboardColor.POSITIVE)
# In[7]:


def write_message(sender,message):
    vk.messages.send (user_id = sender, message = message, random_id = get_random_id(), keyboard = keyboard.get_keyboard())

def language_keyboard(sender,message):
    vk.messages.send (user_id = sender, message = message, random_id = get_random_id(), keyboard = keyboard2.get_keyboard())

def keyboard_third(sender,message):
    vk.messages.send (user_id = sender, message = message, random_id = get_random_id(), keyboard = eng_keyboard.get_keyboard())
# Тело бота

# In[ ]:


vk_session = vk_api.VkApi(token="48ffce535d8216c46187da6eaeed6b9e782391faada162d8299b2ddc24e83ce623d217d438a1db1b42d30")
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 62336)
for event in longpoll.listen():
    class MyVkLongPoll(VkLongPoll):
        def listen(self):
            while True:
                try:
                    for event in self.check():
                        yield event
                except Exception as e:
                    print('error', e)
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.text != '':
            if event.from_user:
                if (event.obj.text == 'Начать') or (event.obj.text == 'Start'):
                    write_message(event.obj.from_id, 'Привет!')
                elif event.obj.text == 'Тема для дебатов':
                    mas = 'Выбери язык'
                    language_keyboard(event.obj.from_id, mas)
                elif (event.obj.text == 'Русский') or (event.obj.text == 'English'):
                    if event.obj.text == 'Русский':
                        mas = themes['Резолюция'][random.randint(2153,a)]
                        write_message(event.obj.from_id, mas)
                    elif event.obj.text == 'English':
                        mas = themes_eng['Резолюция'][random.randint(0,b)]
                        write_message(event.obj.from_id, mas)
                elif event.obj.text == 'Информация о нас':
                    mas = 'Дебаты - это интеллектуальная ролевая игра, где команды доказывают позицию, выпавшую по жребию\n\nMGIMO DC является одним из крупнейших клубов дебатов в России\n\nНаши ребята участвуют в международных чемпионатах, работают в крутых компаниях и путешествуют по всему миру\n\nЕсли ты хочешь развить навыки критического мышления, научиться делать сильные речи и получить море эмоций, то присоединяйся'
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
 #   def start_event_listener(self):
  #      while True:
   #         try:
    #            for event in self.long_poll.listen():
     #               self.dispatcher.did_receive_event(event)
      #      except Exception as e:
       #         logging.warning("vk_core: long poll exception: {}".format(e))




# In[ ]:




