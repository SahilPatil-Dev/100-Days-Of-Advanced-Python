from datetime import datetime

def log(message):

    with open("execution_log.txt", "a") as f:
        f.write(f"{datetime.now()} - {message}\n")