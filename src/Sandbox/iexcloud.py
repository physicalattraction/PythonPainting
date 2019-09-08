import json
import os.path
from typing import Dict, Any, Union, List

import requests

STOCKS = [
    'ABBV',
    'ALSN',
    'ARNA',
    'BIIB',
    'BPT',
    'DLX',
    'GTX',
    'GILD',
    'EAF',
    'HSII',
    'HPQ',
    'INVA',
    'LGORF',
    'LEE',
    'MBUU',
    'MCFT',
    'MDWD',
    'MSB',
    'MSGN',
    'NHTC',
    'PCOM',
    'SIGA',
    'STMP',
    'SUPN',
    'HEAR',
    'UIS',
    'UTHR',
    'USNA',
    'EGY',
    'VIAB',
    'AAPL',  # Apple, for comparison reasons
]


class IexCloudService:
    ENVIRONMENT_PRODUCTION = 'production'
    ENVIRONMENT_SANDBOX = 'sandbox'

    _secrets: {str: Any} = None

    def __init__(self, environment: str):
        assert environment in (self.ENVIRONMENT_PRODUCTION, self.ENVIRONMENT_SANDBOX)
        self.environment = environment

    @property
    def secrets(self) -> Dict:
        if not self._secrets:
            root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            with open(os.path.join(root_dir, 'secrets.json')) as f:
                self._secrets = json.load(f)
        return self._secrets

    @property
    def token(self) -> str:
        if self.environment == self.ENVIRONMENT_SANDBOX:
            return self.secrets['SANDBOX_PUBLIC_API_KEY']
        else:
            return self.secrets['PUBLIC_API_KEY']

    @property
    def base_url(self) -> str:
        if self.environment == self.ENVIRONMENT_SANDBOX:
            return 'https://sandbox.iexapis.com/stable'
        else:
            return 'https://cloud.iexapis.com/stable'

    def get_epratio(self, symbols: Union[str, List[str]]) -> float:
        url = f'{self.base_url}/stock/market/stats/peRatio'
        if isinstance(symbols, str):
            symbols = [str]
        params = {'symbols': ','.join(symbols)}
        return self._get(url, params)

    def _get(self, url: str, params: dict = None):
        if params is None:
            params = {}
        params.update({'token': self.token})
        response = requests.get(url, params)
        if response.status_code != 200:
            msg = response.json()
            raise ValueError(msg)
        return response.json()


if __name__ == '__main__':
    iex = IexCloudService(IexCloudService.ENVIRONMENT_SANDBOX)
    print('stock;peratio')
    peratios = iex.get_epratio(STOCKS)
    for symbol, peratio in zip(STOCKS, peratios):
        print(f'{symbol};{peratio}')
