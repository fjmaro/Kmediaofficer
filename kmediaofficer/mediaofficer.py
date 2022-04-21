"""Kiwuku Media Officer"""
from typing import Optional, Tuple
from pathlib import Path

from kjmarotools.basics import logtools

from kmaintainer import FileMaintainer
from krawarranger import RawArranger
from kanalyxer import Analyxer


class MediaOfficer:
    """
    --------------------------------------------------------------------------
    Media Officer
    --------------------------------------------------------------------------
    """
    # pylint: disable=too-many-instance-attributes
    LOGGER_NAME = "MediaOfficer"
    YEAR_BOUNDS = 1800, 2300

    def __init__(self, pos_base_path: Path, neg_base_path: Path,
                 results_path: Path, folder_patterns: Tuple[str, ...]):
        self._mant: Optional[FileMaintainer] = None
        self._rawa: Optional[RawArranger] = None
        self._anlx: Optional[Analyxer] = None
        self.log = logtools.get_fast_logger(self.LOGGER_NAME, results_path)
        self.log.info("Positives Path: %s", pos_base_path)
        self.log.info("Negatives Path: %s", neg_base_path)
        self.log.info("Results Path:   %s", results_path)
        inf_msg0 = "[MDO] <HELP> The Tag <NewModulePhase> indicates a new %s"
        inf_msg1 = "[MDO] <HELP> The Tag <NewResultsBlock> indicates the %s"
        inf_msg2 = "[MDO] <HELP> The three modules contain their own module%s"
        self.log.info(inf_msg0, "phase of the program")
        self.log.info(inf_msg1, " results for a block")
        self.log.info(inf_msg2, " tag [RWA], [ALX] and [MNT]")

        # Configuration parameters
        self.pos_path = pos_base_path
        self.neg_path = neg_base_path
        self.patterns = folder_patterns
        self.results_path = results_path

    def init_raw_arranger(self) -> None:
        """Initializing the RawArranger"""
        self._rawa = RawArranger(self.pos_path, self.neg_path, self.log,
                                 self.patterns)

    def init_file_analyxer(self, pilexif_log=False) -> None:
        """Initializing the Analyxer"""
        self._anlx = Analyxer(self.pos_path, self.log, self.results_path,
                              self.patterns, self.YEAR_BOUNDS, pilexif_log)

    def init_file_maintainer(self) -> None:
        """Initializing the FileMaintainer"""
        self._mant = FileMaintainer(self.pos_path, self.log, self.patterns,
                                    self.YEAR_BOUNDS)

    def run(self):
        "Run the MediaOfficer"
        self.log.info(".....")
        if self._rawa is not None:
            self._rawa.run(embedded=True)
            self.log.info(".....")

        if self._anlx is not None:
            self._anlx.run(embedded=True)
            self.log.info(".....")

        if self._mant is not None:
            self._mant.run(embedded=True)
            self.log.info(".....")

        self.log.info("[OK] PROCESS SUCCESSFULLY FINALIZED")
        print("\n ┏" + "━" * 76 + "┓")
        print("" + f" ┃{'PROCESS SUCCESSFULLY FINALIZED':^76s}┃")
        print(" ┗" + "━" * 76 + "┛\n")
        input(" > PRESS ENTER TO RESUME...")

    @staticmethod
    def cmd_and_help() -> Tuple[str, str]:
        """Return the CMD and Help info box"""
        # pylint: disable=line-too-long
        cmd = " ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
        cmd += " ┃        MEDIA OFFICER        ┃\n"
        cmd += " ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫\n"
        cmd += " ┃ Select one of the following ┃\n"
        cmd += " ┃    options from the list    ┃\n"
        cmd += " ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫\n"
        cmd += " ┃ (0) Run options 1-2-3       ┃\n"
        cmd += " ┃ (1) Run Raw Arranger        ┃\n"
        cmd += " ┃ (2) Run Files Analyxer      ┃\n"
        cmd += " ┃ (3) Run Files Maintainer    ┃\n"
        cmd += " ┃                             ┃\n"
        cmd += " ┃ (8) Help and info           ┃\n"
        cmd += " ┃ (9) Exit                    ┃\n"
        cmd += " ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"

        hlp = " ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
        hlp += " ┃                                                 HELP AND INFORMATION                                               ┃\n"
        hlp += " ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫\n"
        hlp += " ┃ - Raw Arranger:     Move the negative files allocated in positive folders to its corresponding folder in the       ┃\n"
        hlp += " ┃                     negatives tree. It will raise errors if the negatives folder-tree is not found in positives or ┃\n"
        hlp += " ┃                     in case of moving files from positives to negatives already existing to avoid overwriting.     ┃\n"
        hlp += " ┃ - Files Analyxer:   The actions of this module are focused on analyzing and fixing file-dates in different steps:  ┃\n"
        hlp += " ┃                     1) Rename the files with proprietary conventions.                                              ┃\n"
        hlp += " ┃                     2) For the files in risk of loosing its original date add the modify-date according to TRKDIN. ┃\n"
        hlp += " ┃                     3) Check for the files with valid Meta-date and KDIN that both are the same.                   ┃\n"
        hlp += " ┃                     4) Find the files out of the folder-date bounds.                                               ┃\n"
        hlp += " ┃ - Files Maintainer: Update the files modification-date according to the date-in-name given in the file.            ┃\n"
        hlp += " ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫\n"
        hlp += " ┃ - Raw Arranger:     [FolderCreated] New folder created in Negatives.                                               ┃\n"
        hlp += " ┃                     [FileMoved] File moved from positives to negatives.                                            ┃\n"
        hlp += " ┃ - Files Analyxer:   [PropRenamed] File with PROPDIN renamed to KDIN.                                               ┃\n"
        hlp += " ┃                     [Duplicated] File with PROPDIN not renamed because a file with the same KDIN already exist.    ┃\n"
        hlp += " ┃                     [DateDamaged] Original Date found in metadata of the file but the date is damaged.             ┃\n"
        hlp += " ┃                     [Date2Review] File in risk of loosing its date, modify date is added as TRKDIN to preserve it. ┃\n"
        hlp += " ┃                     [EdinRenamed] File with EKDIN renamed to KDIN because its metadata is not editable.            ┃\n"
        hlp += " ┃                     [Edin2Metadt] File with EKDIN added to the metadata and removed from the filename.             ┃\n"
        hlp += " ┃                     [Inconsistent] File with Metadata original Date and KDIN mismatching.                          ┃\n"
        hlp += " ┃                     [OutOfBounds] File with date out of the folder date-bounds where it is allocated.              ┃\n"
        hlp += " ┃ - Files Maintainer: [DateUpdated] File Modify Date updated to match its KDIN/TRKDIN.                               ┃\n"
        hlp += " ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫\n"
        hlp += " ┃ - KDIN: Kiwuku Date-In-Name Convention [YYYYmmdd-HHMMSS*]                                                          ┃\n"
        hlp += " ┃ - EKDIN: Kiwuku Editing-Date-In-Name Convention [*++YYYY-mm-dd+HH-MM-SS++*]                                        ┃\n"
        hlp += " ┃ - TRKDIN: Kiwuku Date-In-Name-To-Review Convention [YYYYmmdd-HHMMSS(DTR)*]                                         ┃\n"
        hlp += " ┃ - PROPDIN: Proprietary Date-In-Name Convention [Google, Whatsapp, Screenshots, ...]                                ┃\n"
        hlp += " ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"
        return cmd, hlp


if __name__ == "__main__":
    # ========================================================================
    # For executing this example remove the relative '.' imports
    # ========================================================================
    _THIS_FILE_PATH = Path(__file__).parent.resolve()
    _POSITIVE_FOLDER = _THIS_FILE_PATH.parent.parent
    _NEGATIVE_FOLDER = _THIS_FILE_PATH.parent
    _FOLDER_PATTERNS = ("1.*", "2.*", "3.*", "4.*", "5.*", )
    MediaOfficer(_POSITIVE_FOLDER, _NEGATIVE_FOLDER, _THIS_FILE_PATH,
                 _FOLDER_PATTERNS).run()
