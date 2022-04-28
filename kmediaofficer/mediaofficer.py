"""Kiwuku Media Officer"""
from typing import Optional, Tuple
from pathlib import Path

from kjmarotools.basics import logtools
from kmaintainer import FileMaintainer
from krawarranger import RawArranger


class MediaOfficer:
    """
    --------------------------------------------------------------------------
    Media Officer
    --------------------------------------------------------------------------
    """
    # pylint: disable=too-many-instance-attributes,too-many-arguments
    LOGGER_NAME = "MediaOfficer"
    YEAR_BOUNDS = 1800, 2300

    def __init__(self, pos_base_path: Path, neg_base_path: Path,
                 results_path: Path, folder_patterns: Tuple[str, ...],
                 raw_extensions: Tuple[str, ...] = ("RAW", "NEF", "LRCAT")):
        self._mant: Optional[FileMaintainer] = None
        self._rawa: Optional[RawArranger] = None

        self.log = logtools.get_fast_logger(self.LOGGER_NAME, results_path)
        self.log.info("Positives Path: %s", pos_base_path)
        self.log.info("Negatives Path: %s", neg_base_path)
        self.log.info("Results Path:   %s", results_path)
        inf_msg0 = "[MDO] <HELP> The Tag <NewModulePhase> indicates a new %s"
        inf_msg1 = "[MDO] <HELP> The Tag <NewResultsBlock> indicates the %s"
        inf_msg2 = "[MDO] <HELP> All the modules contain their own %s"
        self.log.info(inf_msg0, "phase of the program")
        self.log.info(inf_msg1, " results for a block")
        self.log.info(inf_msg2, "tags: [RWA], [MNT], etc.")

        # Configuration parameters
        self.pos_path = pos_base_path
        self.neg_path = neg_base_path
        self.patterns = folder_patterns
        self.results_path = results_path
        self.raw_extensions = raw_extensions

    def init_raw_arranger(self) -> None:
        """Initializing the RawArranger"""
        self._rawa = RawArranger(self.pos_path, self.neg_path, self.log,
                                 self.patterns, self.raw_extensions)

    def init_file_maintainer(self) -> None:
        """Initializing the FileMaintainer"""
        self._mant = FileMaintainer(self.pos_path, self.log, self.patterns,
                                    self.YEAR_BOUNDS)

    def run(self, embedded=False) -> bool:
        """
        ----------------------------------------------------------------------
        Execute MediaOfficer with the defined configuration
        - embedded: It won't stop after successful execution
        ----------------------------------------------------------------------
        return:
            - True: An error was raised during execution
            - False: No error raised during execution
        ----------------------------------------------------------------------
        """
        self.log.info(".....")
        rawa_err = False
        mant_err = False

        if self._rawa is not None:
            rawa_err = self._rawa.run(embedded=True)
            self.log.info(".....")

        if self._mant is not None:
            mant_err = self._mant.run(embedded=True)
            self.log.info(".....")

        if not rawa_err and not mant_err:
            self.log.info("[OK] PROCESS SUCCESSFULLY FINALIZED")
            print("\n ┏" + "━" * 76 + "┓")
            print("" + f" ┃{'PROCESS SUCCESSFULLY FINALIZED':^76s}┃")
            print(" ┗" + "━" * 76 + "┛\n")
        else:
            self.log.warning("[WARNING] PROCESS FINALIZED WITH WARNINGS")
            print("\n ┏" + "━" * 76 + "┓")
            print("" + f" ┃{'PROCESS FINALIZED WITH WARNINGS':^76s}┃")
            print(" ┗" + "━" * 76 + "┛\n")

        if not embedded:
            input(" > PRESS ENTER TO RESUME...")
        return rawa_err or mant_err

    @staticmethod
    def load_cmd_file(filename: str) -> str:
        """Return the file with name 'filename' allocated in cmd folder"""
        filepath = Path(__file__).parent.resolve().joinpath("cmd") / filename
        with open(filepath, "r", encoding="utf8") as fle:
            return fle.read()


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
