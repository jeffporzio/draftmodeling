import logging
logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO)

def log(output): 
    # Abstract printing here to easy python 2/3 syntax switching
    print(output)
