import logging
import warnings

logging.basicConfig(level=logging.INFO,)
warnings.warn('This warning is not sent to the logs')
logging.captureWarnings(True)
warnings.warn('This warning is sent to the logs')

