import os
import logging
from from_root import from_root
from datetime import datetime
file_name=f"{datetime.now().strftime("%Y_%M_%D_%H_%M_%S")}.log"
rootfolder="logs"
filepath=os.path.join(from_root(),rootfolder,file_name)
os.makedirs(os.path.dirname(filepath),exist_ok=True)
logging.basicConfig(
    filename=filepath,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
