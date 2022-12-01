# autobackup.py

import dirsync
import json
import os
import time
import logging


logging.basicConfig(format='%(asctime)s %(funcName)s %(levelname)s %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

with open('dirs.json', 'r') as f:
    mappings = json.loads(f.read())

def sync_dirs(src:str, dest:str) -> None:
    ''' Backs up a source directory to a backup directory '''
    logger.info(str(src), str(dest))
    if os.path.exists(dest):
        start = time.perf_counter()
        dirsync.sync(src, dest, 'sync', purge=True)
        elapsed = time.perf_counter()-start
        logger.info(f'Elapsed: {elapsed//60} minutes {elapsed%60} seconds')
    else:
        logger.info("Backup storage not found. Exiting...")

for mapping in mappings:
    sync_dirs(mapping['src'], mapping['dest'])