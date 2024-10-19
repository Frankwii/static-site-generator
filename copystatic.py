import os
import shutil
import logging
logging.basicConfig(filename="LOG-copystatic", level=logging.INFO)
logger=logging.getLogger(__name__)

def copystatic():
    logger.info(f"Deleting public...")
    if os.path.exists("public"):
        shutil.rmtree("public")
    
    copydir("static","public")

def copydir(originPath,destinationPath):
    if os.path.isfile(originPath):
        logger.info(f"Trying to copy file {originPath} to folder {destinationPath}")

        shutil.copy(originPath,destinationPath)

    else:
        logger.info(f"Copying folder {originPath} into {destinationPath}")
        os.mkdir(destinationPath)

        children=os.listdir(originPath)

        # list forces map into executing
        list(map(lambda child: copydir(originPath=os.path.join(originPath,child),destinationPath=os.path.join(destinationPath,child)), children))

if __name__=="__main__":
    copystatic()
