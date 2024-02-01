import logging.config

# Define logging configuration dictionary
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    # Formatters define the layout of log messages
    'formatters': {
        'detailed': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s\n\t%(pathname)s:%(lineno)d\n'
        },
        'simple': {
            'format': '[%(levelname)s] %(message)s'
        },
    },

    # Handlers determine where the log messages go
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout',  # Use sys.stdout instead of the default stderr
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'detailed',
            'filename': 'log_file.log',
            'mode': 'a',
        },
    },

    # Loggers define the application modules that use the loggers
    'loggers': {
        '': {  # root logger
            'handlers': ['console', 'file'],
            'level': 'WARNING',
        },
        'EnBed': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,  # Prevents duplication of log messages when propagate is True
        },
    },
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)