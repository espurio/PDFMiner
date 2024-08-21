#Script para extraer el número del acta_text

import re
from unidecode import unidecode

def number_minute(text:str):
    
    pattern_minute: str = r"(ACTA\s\d+)"
    minute: str = re.search(pattern_minute, text).group(1)
    return minute
