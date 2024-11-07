# TODO: read in your yaml file and parse it using the data classes defined in dataclasses.py
import yaml
from nba.data_models import Config
from pathlib import Path

config_dict = yaml.safe_load((Path(__file__).parent.parent / "config.yaml").read_text())

config = Config.model_validate(config_dict)