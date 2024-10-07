import subprocess
import sys

class Setup:
    def __init__(self):
        self.__required_packages = ["beautifulsoup4", "selenium", "icalendar", "pathlib"]
    
    def install_packages(self):
        for pckg in self.__required_packages:
            self.install(pckg)
            
    def install(self, package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])