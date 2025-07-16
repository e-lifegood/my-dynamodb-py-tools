import logging

def setup_logging(file_name='execution-trace.log'):
    """
    Configures the logging settings for the application.
    """
    logging.basicConfig(
        filename=file_name,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding='utf-8'
    )

def print_log(log_message, type='info'):
    print(f"{log_message}")
    if type == 'info':
        logging.info(f"{log_message}")
    elif type == 'error':
        logging.error(f"{log_message}")
    elif type == 'warning':
        logging.warning(f"{log_message}")
    else:
        raise ValueError("Invalid log type specified. Use 'info', 'error', or 'warning'.")