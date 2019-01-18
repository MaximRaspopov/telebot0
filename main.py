
import telegrambot
import weathermap

token = '690289812:AAHUXep5LlyqEPyMInufozj3feGQ54UHTzg'

repeat_bot = telegrambot.teleBot(token)
wether_bot = weathermap.weatherBot()


def main():
    new_offset = None

    while True:
        repeat_bot.get_updates(new_offset)
        last_update = repeat_bot.get_last_update()
        last_chat_text = ''

        if last_update != None:
            last_update_id = last_update['update_id']
            try:
                last_chat_text = last_update['message']['text']
            except:
                last_chat_text = "Not city"

            last_chat_id = last_update['message']['chat']['id']

            city = wether_bot.weather_id(last_chat_text)
            result = wether_bot.weather_for_5(city)
            repeat_bot.send_message(last_chat_id, '{}'.format(result))

            new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()