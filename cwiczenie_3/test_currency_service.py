from unittest.mock import patch, MagicMock
import pytest
from currency_service import CurrencyService

NBP_USD_RESPONSE = {
    "table": "A",
    "currency": "dolar amerykański",
    "code": "USD",
    "rates": [{"no": "001/A/NBP/2026", "effectiveDate": "2026-01-02", "mid": 4.0832}]
}

def test_get_rate_zwraca_kurs():
    service = CurrencyService()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = NBP_USD_RESPONSE
    with patch("requests.get", return_value=mock_response):
        rate = service.get_rate("USD")
    assert rate == 4.0832

def test_get_rate_nieznana_waluta_rzuca_value_error():
    service = CurrencyService()
    mock_response = MagicMock()
    mock_response.status_code = 404
    with patch("requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Nieznana waluta"):
            service.get_rate("XYZ")

def test_get_rate_blad_sieci_rzuca_connection_error():
    import requests as req
    service = CurrencyService()
    with patch("requests.get", side_effect=req.exceptions.ConnectionError("timeout")):
        with pytest.raises(ConnectionError):
            service.get_rate("EUR")

def test_convert_przelicza_kwote():
    service = CurrencyService()
    with patch.object(service, "get_rate", return_value=4.0832):
        result = service.convert(100, "USD")
    assert result == 408.32

def test_get_rate_z_mocker(mocker):
    service = CurrencyService()
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = NBP_USD_RESPONSE
    rate = service.get_rate("USD")
    assert rate == 4.0832
    mock_get.assert_called_once()