from pymessenger.bot import Bot
import os

ACCESS_TOKEN = os.environ['EAAyHnBZB7ZApQBAC21F0ssHwqMJi5ZCbt6LS2zZB2E1FOxGmNn9sJN7UZBWLpLJ7gH3Ws18ClDxXy6HXPChbaMr9uprxFG4NSlRrDFW6cU0Nzhi3Q5TL2qygYjG3FhaLlbqb4pNPgBtr8GGW7Qq1qdmXpqwBkUlPgvZCPR6aq5QMWztuRxnNT2jS3RLWhZB1MsZD']
VERIFY_TOKEN = os.environ['chatbotmypage']

bot = Bot(ACCESS_TOKEN)


def respond_to_user(sender_id, message):
    if "hola" in message.lower():
        bot.send_text_message(sender_id, "Hola, ¿cómo estás?")
    else:
        bot.send_text_message(
            sender_id, "Lo siento, no entiendo lo que quieres decir. ¿Podrías reformularlo?")


def verify_fb_token(token_sent):
    return token_sent == VERIFY_TOKEN


if __name__ == "__main__":
    app.run()
