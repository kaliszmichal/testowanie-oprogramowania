from unittest.mock import patch, mock_open
import pytest
from file_logger import FileLogger

def test_log_otwiera_plik_do_zapisu():
    logger = FileLogger("test.log")
    m = mock_open()
    with patch("builtins.open", m):
        logger.log("Test message")
    m.assert_called_once_with("test.log", "a", encoding="utf-8")

def test_log_zapisuje_wiadomosc():
    logger = FileLogger("test.log")
    m = mock_open()
    with patch("builtins.open", m):
        logger.log("Hello World")
    handle = m()
    written = handle.write.call_args[0][0]
    assert "Hello World" in written

def test_log_ioerror_jest_propagowany():
    logger = FileLogger("/readonly/test.log")
    with patch("builtins.open", side_effect=IOError("Brak dostępu")):
        with pytest.raises(IOError):
            logger.log("message")

def test_read_logs_zwraca_puste_gdy_brak_pliku():
    logger = FileLogger("nieistniejacy.log")
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = logger.read_logs()
    assert result == []