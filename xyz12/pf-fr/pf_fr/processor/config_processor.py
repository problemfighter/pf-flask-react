from pf_flask.pff_config_manager import PFFConfigManager
from pf_flask.pff_utils import import_from_string
from pf_fr.config.pfr_app_config import PFRAppConfig


class ConfigProcessor:
    _pff_config_manager = PFFConfigManager()

    def get_config(self, base_path):
        config = PFRAppConfig()
        config.set_base_dir(base_path)
        config.PORT = 1201
        application_config = import_from_string(config.APPLICATION_CONFIGURATION, config.STRING_IMPORT_SILENT)
        if application_config:
            config = self._pff_config_manager.merge_config_by_config(application_config, config)
        return config


config_processor = ConfigProcessor()
