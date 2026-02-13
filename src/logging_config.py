import logging


def setup_logger():
    """
    Configure global logging for the application.

    - Logs are written to bot.log file
    - Logs include timestamp, level, and message
    - Default level is INFO
    """

    logging.basicConfig(
        filename="bot.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        filemode="a"  # append mode (important)
    )

    # Also log to console (useful for CLI)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    console_format = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    console_handler.setFormatter(console_format)

    # Add console handler to root logger
    logging.getLogger().addHandler(console_handler)

    logging.info("Logging initialized successfully.")
