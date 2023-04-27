import os
import time

LOG_FILE = "/app/logs/app.log"
APP_NAME = "APP_" + os.environ.get("TASK_SLOT")

def log_with_timestamp(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{timestamp}: [{APP_NAME}] {message}\n"
    with open(LOG_FILE, "a") as f:
        f.write(log_message)

if __name__ == "__main__":
    log_with_timestamp("Application started.")
    while True:
        log_with_timestamp("Hello, world!")
        time.sleep(10)

