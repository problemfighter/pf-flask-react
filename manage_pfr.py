import os
from pf_flask.bismillah import Bismillah
from pf_fr.processor.config_processor import config_processor

base_path = os.path.abspath(os.path.dirname(__file__))
config = config_processor.get_config(base_path)
bismillah = Bismillah(__name__, config)

if __name__ == '__main__':
    bismillah.run()
