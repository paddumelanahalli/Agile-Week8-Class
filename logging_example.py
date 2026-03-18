import logging

logging.basicConfig(filename="newfile1.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()

logger.setLevel(logging.DEBUG)


logger.debug("debug msg")
logger.info("Info msg")
logger.warning("Warning msg")
logger.error("Error msg")
logger.critical("Critical msg")

newfile.log
============

2026-03-17 20:54:46,115 debug msg
2026-03-17 20:54:46,115 Info msg
2026-03-17 20:54:46,115 Warning msg
2026-03-17 20:54:46,115 Error msg
2026-03-17 20:54:46,115 Critical msg
