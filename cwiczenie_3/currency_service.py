import requests

class CurrencyService:
    BASE_URL = "https://api.nbp.pl/api/exchangerates/rates/a"

    def get_rate(self, currency: str) -> float:
        url = f"{self.BASE_URL}/{currency.upper()}/?format=json"
        try:
            response = requests.get(url, timeout=5)
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Błąd połączenia: {e}") from e

        if response.status_code == 404:
            raise ValueError(f"Nieznana waluta: {currency}")
        response.raise_for_status()
        data = response.json()
        return data["rates"][0]["mid"]

    def convert(self, amount: float, currency: str) -> float:
        rate = self.get_rate(currency)
        return round(amount * rate, 2)