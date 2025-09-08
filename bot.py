from bot_functions import *
from properties import *
import time


menus=build_keyboard(restart_keyboard)

def handle_updates(updates):
    for update in updates["result"]:
        # print('update.keys():',update.keys())
        if 'callback_query' in update.keys() :
            chat_id = update['callback_query']['message']['chat']['id']
            data = update['callback_query']['data']
            if data and data in language_codes:
                update_language(chat_id,data)
                lang_msg=get_language_message(data)
                send_message(lang_msg,chat_id,menus)
            else:
                send_message("Biror xatolik ro'y berdi",chat_id,build_keyboard(restart_keyboard))
        elif 'message' in update:
            chat_id = update["message"]["chat"]["id"]
            if "text" in update["message"].keys():
                text = update["message"]["text"]
                print('Text: ',text)
                if text == "/start" or text=="🔄 Qayta boshlash":
                    send_message(ask_contact_msg,chat_id,build_keyboard(ask_contact))
                else:
                    send_message(unknown_command,chat_id)
            elif "contact" in update["message"].keys():
                user_id = update["message"]["contact"]["user_id"]
                phone_number=update["message"]["contact"]["phone_number"][-9:]
                print(phone_number)
                check_result=check_access(phone_number,chat_id)
                print('chat_id: ',chat_id)
                print('check_result: ',check_result)
                if user_id == chat_id:
                    send_message(check_contact_msg,chat_id)
                    if check_result==1:
                        send_message(bot_access_msg,chat_id,inline_keyboard(languages))
                    elif check_result==0:
                        send_message(permission_message,chat_id,build_keyboard(restart_keyboard))
                    elif check_result==-1:
                        send_message(not_working_bot,chat_id,build_keyboard(restart_keyboard))
                    else:
                        send_message(permission_message,chat_id,build_keyboard(restart_keyboard))  
                else:
                    send_message(only_your_contact,chat_id,build_keyboard(ask_contact))
            else:
                print(f"Boshqa ma'lumot turi junatildi !")
            
                

def main():  
    last_update_id = None
    while True:
        try:
            updates = get_updates(last_update_id)
            if len(updates["result"]) > 0:
                last_update_id = get_last_update_id(updates) + 1
                handle_updates(updates)
            time.sleep(0.1)
        except Exception as e:
            print('Something bad happened',str(e))

if __name__ == '__main__':
    main()
  