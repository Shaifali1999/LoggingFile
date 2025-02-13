import sys
import logging

__author__ = "Shaifali Rao"

class Logger:
    """
    Logger class to set up logging with both file and console output.
    """

    def __init__(self, file_name):
        """
        Initialize logger.

        :param file_name: Name of the log file (without extension).
        """
        self.file_name = file_name
        self.log_obj = self._setup_logger()

    def _setup_logger(self):
        """
        Configures the logger.

        :return: Logger object.
        """
        log_obj = logging.getLogger(self.file_name)
        log_obj.setLevel(logging.DEBUG)

        # Formatter (Day Name + Date + Process ID)
        formatter = logging.Formatter(
            fmt='%(asctime)s [PID: %(process)d] %(module)s, line: %(lineno)d %(levelname)8s | %(message)s',
            datefmt='%A %Y/%m/%d %H:%M:%S'  # Includes day name at the start
        )

        # File handler
        file_handler = logging.FileHandler(f"{self.file_name}.log", mode='w')
        file_handler.setFormatter(formatter)
        log_obj.addHandler(file_handler)

        # Console handler
        console_handler = logging.StreamHandler(stream=sys.stdout)
        console_handler.setFormatter(formatter)
        log_obj.addHandler(console_handler)

        log_obj.info("Logger initialized successfully.")
        return log_obj

    def get_logger(self):
        """
        Returns the configured logger.

        :return: Logger object.
        """
        return self.log_obj

    def close_logger(self):
        """
        Clears all handlers to prevent duplicate logging.
        """
        self.log_obj.handlers.clear()

# Usage example
if __name__ == "__main__":
    logger = Logger('shaifali')
    log_obj = logger.get_logger()

    log_obj.info("I am from logger call class")
    log_obj.critical("CRITICAL ERROR")
    log_obj.error("ERROR")
    log_obj.warning("WARNING")
    log_obj.debug("DEBUG MESSAGE")
    log_obj.info("qwerty")
    log_obj.info("asdfghjkl")
    log_obj.info("End")

    # Closing logger
    logger.close_logger()














































# import sys
# import logging

# __author__ = "Shaifali Rao"

# class Logger:
#     """
#     Logger class to set up logging with both file and console output.
#     """

#     def __init__(self, file_name):
#         """
#         Initialize logger.

#         :param file_name: Name of the log file (without extension).
#         """
#         self.file_name = file_name
#         self.log_obj = self._setup_logger()

#     def _setup_logger(self):
#         """
#         Configures the logger.

#         :return: Logger object.
#         """
#         log_obj = logging.getLogger(self.file_name)
#         log_obj.setLevel(logging.DEBUG)

#         # Formatter
#         formatter = logging.Formatter(
#             fmt='%(asctime)s %(module)s, line: %(lineno)d %(levelname)8s | %(message)s',
#             datefmt='%Y/%m/%d %H:%M:%S'
#         )

#         # File handler
#         file_handler = logging.FileHandler(f"{self.file_name}.log", mode='w')
#         file_handler.setFormatter(formatter)
#         log_obj.addHandler(file_handler)

#         # Console handler
#         console_handler = logging.StreamHandler(stream=sys.stdout)
#         console_handler.setFormatter(formatter)
#         log_obj.addHandler(console_handler)

#         log_obj.info("Logger initialized successfully.")
#         return log_obj

#     def get_logger(self):
#         """
#         Returns the configured logger.

#         :return: Logger object.
#         """
#         return self.log_obj

#     def close_logger(self):
#         """
#         Clears all handlers to prevent duplicate logging.
#         """
#         self.log_obj.handlers.clear()

# # Usage example
# if __name__ == "__main__":
    
#     logger = Logger('shaifali')
#     log_obj = logger.get_logger()

#     log_obj.info("I am from logger call class")
#     log_obj.critical("CRITICAL ERROR")
#     log_obj.error("ERROR")
#     log_obj.warning("WARNING")
#     log_obj.debug("DEBUG MESSAGE")
#     log_obj.info("qwerty")
#     log_obj.info("asdfghjkl")
#     log_obj.info("End")

#     # Closing logger
#     logger.close_logger()
