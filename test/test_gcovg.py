import sys
import subprocess
import pytest
import logging
from unittest.mock import patch

logger = logging.getLogger(__name__)

PYTEST_GCOV_PATH = "gcov"


def test_gcov_command_exists(capsys):
    logger.debug(f"gcov path : {PYTEST_GCOV_PATH}")
    proc = subprocess.Popen(PYTEST_GCOV_PATH, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    assert proc.returncode == 1
    assert out.decode("utf-8") == ""
    assert err.decode("utf-8").startswith("Usage:")
