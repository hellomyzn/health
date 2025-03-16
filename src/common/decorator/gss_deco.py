"""common.decorator.decorator for gss"""
#########################################################
# Builtin packages
#########################################################
import functools
import time
import requests

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from common.log import error, warn
from common.exceptions import (
    MyGssException,
    MyGssInvalidArgumentException,
    MyGssResourceExhaustedException
)


def gss_module(func):
    """_summary_

    Args:
        func (_type_): _description_

    Raises:
        MyGssException: _description_

    Returns:
        _type_: _description_
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        attempts = 1
        max_attempts = 3
        while attempts <= max_attempts:
            try:
                return func(*args, **kwargs)
            except requests.exceptions.ConnectionError as exc:
                sec = 30
                warn("connection error. {0}: {1}", exc.__class__.__name__, exc)
            except MyGssInvalidArgumentException:
                sec = 5
            except MyGssResourceExhaustedException:
                sec = 60
            except MyGssException:
                sec = 1
            attempts += 1
            warn("wait {0} sec", sec)
            time.sleep(sec)

        # failed
        mes = ("failed to connect to gss 3 times. "
               "please check your internet connection or logs.")
        error(mes)
        raise MyGssException(mes)
    return wrapper
