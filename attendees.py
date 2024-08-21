#Script para extraer a los asistentes

import re
from unidecode import unidecode

def attendees(text:str):

    attendees: str = re.search(r"([\s\S*])(Sesiones del Concejo[\s\S]*)(INVITADOS[\s\S]*)", text).group(2)    


    def clean(attendees:str):

        text: str = re.sub(r"Sesiones del Concejo ", "", attendees)

        return text



    attendance = clean(attendees)

    attendance = re.search(r"(\n\n)([\s\S]*)(\n\n)", attendance).group(2)
    
    attendance_list: list = attendance.split("\n") 

    return attendance_list
