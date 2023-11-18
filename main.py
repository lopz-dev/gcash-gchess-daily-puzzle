import os
import requests

API_TOKEN = os.environ.get("API_TOKEN")

GCHESS_CHAT_ID = os.environ.get("GCHESS_CHAT_ID")
GCHESS_MESSAGE_THREAD_ID = os.environ.get("GCHESS_MESSAGE_THREAD_ID")

def get_lichess_puzzle_of_the_day() -> str:
    LICHESS_GET_PUZZLE_URL = "https://lichess.org/api/puzzle/daily"
    
    # Get Puzzle from Lichess API
    lichess_daily_puzzle_req = requests.get(LICHESS_GET_PUZZLE_URL).json()

    # Get Puzzle ID from response["puzzle"]["id"]
    lichess_daily_puzzle_id = lichess_daily_puzzle_req["puzzle"]["id"]

    return f"https://lichess.org/training/{lichess_daily_puzzle_id}/"

def get_today() -> str:
    import datetime
    return datetime.date.today().strftime("%B %d, %Y")

def send_message(
    message: str,
    chat_id: str,
    message_thread_id: str,
    
):
    message_url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"

    try:
        response = requests.post(message_url, json={'chat_id': chat_id, 'text': message, 'message_thread_id': message_thread_id})
        print(response.text)
    except Exception as e:
        print(e)

def get_updates():
    updates_url = f"https://api.telegram.org/bot{API_TOKEN}/getUpdates"
    print(requests.get(updates_url).json())
    
def main():

    message = f"""{get_today()}
Puzzle

{get_lichess_puzzle_of_the_day()}
"""
    # GChess
    send_message(message=message, chat_id=GCHESS_CHAT_ID, message_thread_id=GCHESS_MESSAGE_THREAD_ID)

    
def lambda_handler(event, context):
    main()