import subprocess
import sys

class Setup:
    def __init__(self):
        pass
    
    def install_packages(self, pckg_list):
        for pckg in pckg_list:
            self.install(pckg)
            
    def install(self, package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])