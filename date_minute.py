#Script para extraer la fecha

import re
from unidecode import unidecode

def date_minute(text:str):

    date_pattern: str = r"ACTA\s\d+\s\n([A-Z]\w+\s\d{1,2}\sde\s\d{4})\n"
    date: str = re.search(date_pattern, text).group(1)

    return date
