from pydantic import BaseSettings, Field
from pathlib import Path


class DataConfig(BaseSettings):
    data_path: Path = Field(default=None, env='DATA_PATH')