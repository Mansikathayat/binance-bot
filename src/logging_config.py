import logging

def setup_logger():
    """
    Global logging configuration.
    Saare modules isi logger ko use karenge.
    """
    logging.basicConfig(
        filename="bot.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )
