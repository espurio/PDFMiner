#Script para extraer el orden del día

import re
from unidecode import unidecode

def conduct_minute(text:str):

    ordered_text: str = re.search(r"([\s\S*])(ORDEN DEL DÍA[\s\S]*)(DESARROLLO[\s\S]*)", text).group(2)
    
    def clean(ordered_text:str):

        ordered_text: str = re.sub(r"\n\d{1,2}", "", ordered_text) #Limpia los números del orden del día.

        ordered_text: str = re.sub(r"\x0c", "\n", ordered_text) #Limpia los caracteres "x0c"
        
        ordered_text: str = re.sub(r"ACTA DE SESIÓN ORDINARIA\s\d+", "", ordered_text)

        ordered_text: str = re.sub(r"ORDEN DEL DÍA", "", ordered_text)

        ordered_text: str = re.sub(r"\n\D\n", " ", ordered_text) #Limpia el exceso de puntos.

        #text = re.sub(r"\s{1,5}", " ", text)

        return ordered_text


    clean_text: str = clean(ordered_text)
    
    clear_text: str = re.findall(r"[A-Z][a-z]\D+\n\n", clean_text)

    clear_text: list = "\n\n".join(clear_text)  

    clear_text: list = clear_text.split("\n\n")

    return clear_text
