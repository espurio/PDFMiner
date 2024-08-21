#Script para extraer el tipo de acta

import re
from unidecode import unidecode

def type_session(text:str):

    pattern_type_minute: str = r"(SESI[ÓO]N\s\w+\s)"
    type_minute: str = re.search(pattern_type_minute, text).group(1)
    return type_minute
