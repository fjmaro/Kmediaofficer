"""
------------------------------------------------------------------------------
Executable file for running MediaOfficer. This is Designed for being allocated
inside the negatives folder (which is inside the positives folder)
------------------------------------------------------------------------------
"""
import os
import time
from pathlib import Path
from kmediaofficer import MediaOfficer

# ======================== TO UPDATE / EDIT IF NEEDED ========================
_RAW_EXTENSIONS = ("RAW", "NEF", "LRCAT")
_FOLDER_PATTERNS = ("1.*", "2.*", "3.*", "4.*", "5.*")

# =============================== DO NOT EDIT ================================
_NEGATIVE_FOLDER = Path(__file__).parent.resolve()
_POSITIVE_FOLDER = _NEGATIVE_FOLDER.parent
_RESULTS_PATH = _NEGATIVE_FOLDER.joinpath("MediaOfficer")
if not _RESULTS_PATH.exists():
    os.mkdir(_RESULTS_PATH)
_PARAMS = (_POSITIVE_FOLDER, _NEGATIVE_FOLDER, _RESULTS_PATH,
           _FOLDER_PATTERNS, _RAW_EXTENSIONS)

# =============================== DO NOT EDIT ================================
_OPTION_SELECTED = -1
_ALLOWED_OPTIONS = (0, 1, 2, 8, 9)
_CMD_HELP = MediaOfficer.load_cmd_file("cmd_help.txt")
_CMD_INPUT = MediaOfficer.load_cmd_file("cmd_input.txt")
while _OPTION_SELECTED != 9:
    print(_CMD_INPUT)
    _OPTION_STR = input(" > Select Option: ")
    if _OPTION_STR.isdigit() and int(_OPTION_STR) in _ALLOWED_OPTIONS:
        _OPTION_SELECTED = int(_OPTION_STR)

        if _OPTION_SELECTED == 0:
            _MDO = MediaOfficer(*_PARAMS)
            _MDO.init_raw_arranger()
            _MDO.init_file_maintainer()
            _MDO.run()

        elif _OPTION_SELECTED == 1:
            _MDO = MediaOfficer(*_PARAMS)
            _MDO.init_raw_arranger()
            _MDO.run()

        elif _OPTION_SELECTED == 2:
            _MDO = MediaOfficer(*_PARAMS)
            _MDO.init_file_maintainer()
            _MDO.run()

        elif _OPTION_SELECTED == 8:
            print(_CMD_HELP)
            input(" > Press ENTER to return...")
    else:
        print(f" The selected option ({_OPTION_STR}) is not in the list.")
        print(" Please select a valid option...")
        time.sleep(0.5)
        continue
    if _OPTION_SELECTED == 9:
        print("\n Closing the program...")
        time.sleep(1)
