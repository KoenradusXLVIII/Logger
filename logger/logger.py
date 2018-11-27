import platform
import logging.handlers
log_levels = {'debug':logging.DEBUG,
              'info':logging.INFO,
              'warning':logging.WARNING,
              'error':logging.ERROR,
              'critical':logging.CRITICAL}


class Client:
    def __init__(self, name, log_level='info'):
        # Store local variables
        self.name = name
        self.log_level = log_level.lower()

        # Create logging instance
        self.logger = logging.getLogger(self.name)
        self.formatter = logging.Formatter('%(name)s [%(levelname)s] %(message)s')

        # Initialise and add logging handler (platform dependent)
        if platform.system() == 'Windows':
            self.handler = logging.StreamHandler()
        elif platform.system() == 'Linux':
            self.handler = logging.handlers.SysLogHandler(address='/dev/log')
        self.logger.addHandler(self.handler)

        # Configure logger
        self.set_name(self.name)
        self.set_log_level(self.log_level)

    def get_name(self):
        # Return current name
        return self.name

    def set_name(self, name):
        # Set new name
        self.name = name
        self.formatter = logging.Formatter('%(name)s [%(levelname)s] %(message)s')
        self.handler.setFormatter(self.formatter)

    def set_log_level(self, log_level):
        # Set new log level
        self.log_level = log_level.lower()
        self.logger.setLevel(log_levels[self.log_level])
        self.handler.setLevel(log_levels[self.log_level])

    def get_log_level(self):
        # Return current log level
        return self.log_level

    def debug(self, message):
        # Log informational message
        self.logger.debug(message)

    def info(self, message):
        # Log informational message
        self.logger.info(message)

    def warning(self, message):
        # Log informational message
        self.logger.warning(message)

    def error(self, message):
        # Log informational message
        self.logger.error(message)

    def error(self, message):
        # Log informational message
        self.logger.critical(message)
