import os
from pf_fr.config.pfr_app_config import PFRAppConfig
from pf_flask.bismillah import Bismillah


base_path = os.path.abspath(os.path.dirname(__file__))
config = PFRAppConfig()
config.PORT = 1201
config.set_base_dir(base_path)
bismillah = Bismillah(__name__, config)


if __name__ == '__main__':
    bismillah.run()
