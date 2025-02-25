from typing import Optional, List, Dict

class   Result:
    """
    Result returned from RestAdapter
    :param status_code: Standard HTTP Status code
    :param message: HTTP Status message
    :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
    """
    def __init__(self, status_code: int, message: Optional[str] = None, data: Optional[Dict] = None):
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data