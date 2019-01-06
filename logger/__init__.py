import platform
import logging.handlers
log_levels = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}


class Client:
    def __init__(self, name, log_level='info'):
        # Store local variables
        self.name = name
        self.log_level = log_level.lower()
        self.platform = platform.system()
        self.pushover_client = None
        self.nebula_client = None

        # Create logging instance
        self.logger = logging.getLogger(self.name)
        self.formatter = logging.Formatter('%(name)s [%(levelname)s] %(message)s')

        # Initialise and add logging handler (platform dependent)
        if self.platform == 'Windows':
            self.handler = logging.StreamHandler()
        elif self.platform == 'Linux':
            self.handler = logging.handlers.SysLogHandler(address='/dev/log')
        self.logger.addHandler(self.handler)

        # Configure logger
        self.set_name(self.name)
        self.set_log_level(self.log_level)

        # Initialise log
        self.debug('Logger \'%s\' started on %s with log level %s' %
                   (self.name, self.platform, self.log_level.upper()))

    def attach_pushover(self, pushover_client):
        self.pushover_client = pushover_client

    def attach_nebula(self, nebula_client):
        self.nebula_client = nebula_client

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
        if self.nebula_client:
            self.nebula_client.set_level(log_levels[self.log_level])

    def debug(self, message, push=False):
        # Log informational message
        self.logger.debug(message)
        if self.pushover_client and push:
            self.pushover_client.message(message, title=self.name)
        if self.nebula_client:
            self.nebula_client.debug(message)

    def info(self, message, push=False):
        # Log informational message
        self.logger.info(message)
        if self.pushover_client and push:
            self.pushover_client.message(message, title=self.name)
        if self.nebula_client:
            self.nebula_client.info(message)

    def warning(self, message, push=True):
        # Log informational message
        self.logger.warning(message)
        if self.pushover_client and push:
            self.pushover_client.message(message, title=self.name)
        if self.nebula_client:
            self.nebula_client.warning(message)

    def error(self, message, push=True):
        # Log informational message
        self.logger.error(message)
        if self.pushover_client and push:
            self.pushover_client.message(message, title=self.name, priority='high', sound='alien')
        if self.nebula_client:
            self.nebula_client.error(message)

    def critical(self, message, push=True):
        # Log informational message
        self.logger.critical(message)
        if self.pushover_client and push:
            self.pushover_client.message(message, title=self.name, priority='high', sound='alien')
        if self.nebula_client:
            self.nebula_client.critical(message)
