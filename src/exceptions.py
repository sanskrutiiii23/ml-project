import sys
from logger import logging
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message




# ================= REVISION NOTES =================
#
# 1. logger.py:
#    Records application events (INFO, WARNING, ERROR).
#    logging.info() records a message.
#    logging.exception() records an error + its traceback.
#
# 2. exceptions.py:
#    CustomException displays the filename, line number,
#    and actual error message when an exception occurs.
#
# 3. sys.exc_info():
#    Returns (exception_type, exception_value, traceback).
#    _, _, exc_tb = sys.exc_info()
#    exc_tb.tb_lineno gives the error line number.
#    exc_tb.tb_frame.f_code.co_filename gives the filename.
#
# 4. import logging vs from src.logger import logging:
#    import logging -> Imports Python's built-in logging module.
#    from src.logger import logging -> Also executes our
#    logger.py configuration, enabling file logging.
#
# 5. Running exceptions.py:
#    python src/exceptions.py -> Runs as a standalone script.
#    May cause ModuleNotFoundError for 'src'.
#
#    python -m src.exceptions -> Runs as a package module.
#    Recommended when executing from the project root.
#
#    To use direct execution:
#    python -m pip install -e .
#    Then: python src/exceptions.py
#
# 6. __pycache__:
#    Automatically generated Python bytecode files.
#    Safe to ignore. Add __pycache__/ and *.pyc to .gitignore.
#
# 7. logs/ folder:
#    Stores log files from program executions.
#    Each run may create a new timestamped folder/file.
#    Old logs can be deleted if no longer needed.
#
# ==================================================