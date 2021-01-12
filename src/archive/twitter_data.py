import twitter

SESSION_FILE = "keys.txt"


def get_session(session_file: str):
    file = open(session_file, "r")
    return twitter.Api(consumer_key="",
                       consumer_secret="",
                       access_token_key="",
                       access_token_secret="")