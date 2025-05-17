\"\"\"
logger.py: configuraciÃ³n de logging del proyecto.
\"\"\"
import logging

logging.basicConfig(
    level=logging.INFO,
    format=\"%(asctime)s [%(levelname)s] %(message)s\"
)
logger = logging.getLogger(__name__)
