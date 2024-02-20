from src.config.dev import DevConfig
from src.config.prod import ProdConfig

class Config:
    def __init__(self):
        self.dev_config = DevConfig()
        self.prod_config = ProdConfig()