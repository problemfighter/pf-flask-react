import os
from pf_fr.pfre_system import PFRFSystem

base_path = os.path.abspath(os.path.dirname(__file__))
application = PFRFSystem(__name__, base_path).initialize()

if __name__ == '__main__':
    application.run()
else:
    run_server = application
