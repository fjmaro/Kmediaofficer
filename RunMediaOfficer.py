"""
------------------------------------------------------------------------------
Executable file for running MediaOfficer. This is Designed for being allocated
inside the negatives folder
------------------------------------------------------------------------------
"""
# pylint: disable=invalid-name, line-too-long
import os
import time
from pathlib import Path
from kmediaofficer import MediaOfficer

_FOLDER_PATTERNS = ("1.*", "2.*", "3.*", "4.*", "5.*")
_NEGATIVE_FOLDER = Path(__file__).parent.resolve()
_POSITIVE_FOLDER = _NEGATIVE_FOLDER.parent
_RESULTS_PATH = _NEGATIVE_FOLDER.joinpath("MediaOfficer")
if not _RESULTS_PATH.exists():
    os.mkdir(_RESULTS_PATH)
_MDO = MediaOfficer(_POSITIVE_FOLDER, _NEGATIVE_FOLDER,
                    _RESULTS_PATH, _FOLDER_PATTERNS)

# ============================================================================
_OPTION_SELECTED = -1
while _OPTION_SELECTED != 9:
    print("\n" + _MDO.cmd_and_help()[0] + "\n")
    _OPTION_STR = input(" > Select Option: ")
    if _OPTION_STR.isdigit() and int(_OPTION_STR) in (0, 1, 2, 3, 8, 9):
        _OPTION_SELECTED = int(_OPTION_STR)
        if _OPTION_SELECTED == 0:
            _MDO.init_raw_arranger()
            _MDO.init_file_analyxer()
            _MDO.init_file_maintainer()
            _MDO.run()
        elif _OPTION_SELECTED == 1:
            _MDO.init_raw_arranger()
            _MDO.run()
        elif _OPTION_SELECTED == 2:
            _MDO.init_file_analyxer()
            _MDO.run()
        elif _OPTION_SELECTED == 3:
            _MDO.init_file_maintainer()
            _MDO.run()
        elif _OPTION_SELECTED == 8:
            print("\n" + _MDO.cmd_and_help()[1] + "\n")
            input(" > Press ENTER to return...")
    else:
        print(f" The selected option ({_OPTION_STR}) is not in the list.")
        print(" Please select a valid option...")
        time.sleep(0.5)
        continue
    if _OPTION_SELECTED == 9:
        print("\n Closing the program...")
        time.sleep(1)
