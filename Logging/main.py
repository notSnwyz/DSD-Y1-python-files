import os
from logging_system import setup_logger

LOG_FILE = "app.log"

# Ask user if they want to clear the log
clear = input("Clear app.log? Type 'yes' to confirm: ").strip().lower()

def clear_log(clear):
    if clear == "yes":
        if os.path.exists(LOG_FILE):
            open(LOG_FILE, "w").close()
            print("app.log cleared.")
        else:
            print("Log file does not exist yet.")

logger = setup_logger(__name__)

def main():
    logger.info("Program started")
    logger.warning("Example warning")
    logger.error("Example error")

    clear_log(clear)

if __name__ == "__main__":
    main()