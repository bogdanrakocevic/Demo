import yaml
import os
from attrdict import AttrDict


def load_config(config_file=None):
    if config_file is None:
        config_file = 'system'
    else:
        config_file = config_file
    with open(os.path.join(os.path.dirname(__file__), '../config/{}.yaml'.format(config_file))) as f:
        try:
            return AttrDict(yaml.safe_load(f))
        except IOError:
            return None
