from signLanguage.logger import logging
from signLanguage.exception import SignException
import sys

try:
    a = 7/"Z"

except Exception as e:
    raise SignException(e, sys) from e