import psycopg2
import json
import requests
import urllib
from properties import *



def connection(params):
    try:
        conn = psycopg2.connect(**params)
        print(f"Databazaga bo'g'lanish muvofaqyatli")
        return conn
    except Exception as e:
        print(f"Bo'g'lanishda xatolik mavjud: {e}")
        return None




def check_access(phone_number, chat_id):
    conn = connection(db_params)
    try:
        with conn.cursor() as cursor:
            # 1️⃣ Avval promont.user_chat_ids jadvalidan phone_number bor-yo‘qligini tekshiramiz
            cursor.execute("""
                SELECT chat_id
                FROM promont.user_chat_ids
                WHERE phone_number = %s
                FOR UPDATE
            """, (phone_number,))
            row = cursor.fetchone()

            if row:
                current_chat_id = row[0]

                # Case A: Agar chat_id mos kelsa 1 qaytariladi
                if current_chat_id == chat_id:
                    conn.commit()
                    return 1

                # Case B: Agar chat_id farq qilsa → yangilab yozamiz va 1 qaytaramiz
                cursor.execute("""
                    UPDATE promont.user_chat_ids
                    SET chat_id = %s
                    WHERE phone_number = %s
                """, (chat_id, phone_number))
                conn.commit()
                return 1

            # 2️⃣ Agar promont.user_chat_ids da yo‘q bo‘lsa → promont.staff_users ni oxirgi 9 ta belgisi bilan tekshiramiz
            cursor.execute("""
                SELECT 1
                FROM promont.staff_users
                WHERE RIGHT(phone_number, 9) = %s
                LIMIT 1
            """, (phone_number,))
            staff_exists = cursor.fetchone()

            if staff_exists:
                # Agar staff_users da mavjud bo‘lsa → promont.user_chat_ids ga yangi yozuv qo‘shamiz
                cursor.execute("""
                    INSERT INTO promont.user_chat_ids (phone_number, chat_id,language_code,create_time, update_time)
                    VALUES (%s, %s,'uz',now(),now())
                """, (phone_number, chat_id))
                conn.commit()
                print('new raw inserted')
                return 1
            else:
                # Agar staff_users da ham topilmasa → 0 qaytaramiz
                conn.commit()
                return 0

    except Exception as e:
        # Xatolik yuz bersa → tranzaksiyani orqaga qaytaramiz va -1 qaytaramiz
        conn.rollback()
        print(f"❌ check_role funksiyasida xatolik: {e}")
        return -1






def update_language(chat_id, language_code):
    conn = connection(db_params)
    try:
        with conn.cursor() as cursor:
            # 1️⃣ chat_id bo‘yicha foydalanuvchini qidiramiz
            cursor.execute("""
                SELECT 1
                FROM promont.user_chat_ids
                WHERE chat_id = %s
                FOR UPDATE
            """, (chat_id,))
            row = cursor.fetchone()

            if row:
                # 2️⃣ Agar topilsa → language_code yangilanadi
                cursor.execute("""
                    UPDATE promont.user_chat_ids
                    SET language_code = %s
                    WHERE chat_id = %s
                """, (language_code, chat_id))
                conn.commit()
                return 1
            else:
                # 3️⃣ Agar chat_id topilmasa → 0 qaytariladi
                conn.commit()
                return 0

    except Exception as e:
        # Xatolik bo‘lsa → rollback va -1 qaytariladi
        conn.rollback()
        print(f"❌ update_language funksiyasida xatolik: {e}")
        return -1


def get_language_message(language_code):
    messages = {
        "uz": "✅ Siz uchun \"O'zbek tili\" o'rnatildi. Rahmat!",
        "ru": "✅ Для вас был установлен \"Русский язык\". Спасибо!",
        "en": "✅ The \"English language\" has been set for you. Thank you!"
    }
    return messages.get(language_code, "⚠️ Mavjud bo'lmagan til!")





def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = telegram_api + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def build_keyboard(keyboard):
    reply_markup = {"keyboard":keyboard,"one_time_keyboard":True,"resize_keyboard":True}
    return json.dumps(reply_markup)           
        

def inline_keyboard(keyboard):
    reply_markup = {'inline_keyboard':keyboard}
    return json.dumps(reply_markup)
        
        
def send_message(text,chat_id, reply_markup=None):
    text = urllib.parse.quote_plus(text)
    url = telegram_api + "sendMessage?text={}&chat_id={}&parse_mode=HTML".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)





