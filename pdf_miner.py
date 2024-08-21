from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from unidecode import unidecode
import os
import re
import attendees
import conduct_minute
import date_minute
import number_minute
import type_session


def pdf_parser() -> list:
    # Path of the folder containing the pdfs
    folder_path: str = "PDF"

    # We create a list empty which will contain the
    # text extracted from the pdfs
    texts_pdfs: list = []
    pages_text: list = []

    # We create an empty list which will contain the name of the files.
    nombres_archivos: list = []

    contador: int = 0

    # We iterate over the pdfs files that are inside the folder.
    for pdf_file in os.listdir(folder_path):
        if pdf_file.endswith('.pdf'):
            try:
                output_string: StringIO = StringIO()
                full_path: str = os.path.join(folder_path, pdf_file)

                with open(full_path, "rb") as in_file:

                    parser: PDFParser = PDFParser(in_file)
                    doc: PDFDocument = PDFDocument(parser)
                    rsrcmgr: PDFResourceManager = PDFResourceManager()
                    device: TextConverter = TextConverter(
                        rsrcmgr, output_string, laparams=LAParams())
                    interpreter: pdfinterp = PDFPageInterpreter(rsrcmgr, device)

                    for page in PDFPage.create_pages(doc):

                        interpreter.process_page(page)
                        pages_text.append(output_string.getvalue())
                        output_string.truncate(0)
                        output_string.seek(0)

            except:
                print("Error processing file:", pdf_file)

            print("{:<2}---> PDF:{:->64}{:->20}".format(contador, pdf_file, '> processed'))
            print(f'Tipo de archvio: {type(unidecode(output_string.getvalue()))}')

            texts_pdfs.append("\n".join(pages_text))
            contador += 1
            #print(texts_pdfs,"\n\n")

    print(f"A total of {len(texts_pdfs)} were processed\n\n\n")
    
    return texts_pdfs

dict_minute = {}

texts_pdf_list: list = pdf_parser()
#print(texts_pdf)

print("<(-_-)>|^(°_°)^|>(°|°)>|<(T_T)<|^(°-°)>|<(^-^)> <(-_-)>|^(°_°)^|>(°|°)>|<(T_T)<|^(°-°)>|<(^-^)>\n")



#Llamado de la función que extrae la fecha de la sesión

text_to_date: str = texts_pdf_list[0]
date_info: str = date_minute.date_minute(text_to_date)
#print("\n\nLa fecha corresponde a ", date_info)

#Llamado de la función que extrae el número del acta/sesión

text_to_number: str = texts_pdf_list[0]
number_info: str = number_minute.number_minute(text_to_number)
#print("\n\nEl número corresponde a ", number_info)

#Llamado de la función que extrae el tipo de sesión

text_to_session: str = texts_pdf_list[0]
session_info: str = type_session.type_session(text_to_session)
#print("\n\nLa sesión corresponde a ", session_info)

#Llamado de la función que extrae los asistentes

text_to_attendees: str = texts_pdf_list[0]
attendees_info: list = attendees.attendees(text_to_attendees)
#print("\n\nLos asistentes al recinto fueron:\n\n", attendees_info)

#Llamado de la función que extrae el orden del día

text_to_conduct: str = texts_pdf_list[0]
conduct_info: list = conduct_minute.conduct_minute(text_to_conduct)
#print("\n\nEl orden del día fue: \n\n", conduct_info)

dict_minute[number_info] = [session_info,
                            date_info,
                            number_info,
                            conduct_info,
                            attendees_info
                            ]

print("\n\n", dict_minute)

'''
#print(texts_pdf[0])

acta_text = texts_pdf[0][:1000]

#Patrón para el número del acta
pattern_acta = r"(ACTA\s\d+\s)"
acta = re.search(pattern_acta, acta_text).group(1)
print(texts_pdf[:5])
print("-"*100)
#print(acta)


#Patrón para el tipo de sesión
pattern_kind = r"(SESI[ÓO]N\s\w+\s)"
kind = re.search(pattern_kind, acta_text).group(1)
#print(kind)

date_pattern = r"ACTA\s\d+\s\n([A-Z]\w+\s\d{1,2}\sde\s\d{4})\n"
date = re.search(date_pattern, acta_text).group(1)
#print(date)

assistants_pattern = r"[A-Z]\w+\s[A-Z]\w+\s[A-Z]\w+"
assistants = re.findall(assistants_pattern, acta_text)
print(assistants)

lista_acta = []
lista_acta.append(acta)

data_actas = {}

data_actas["Acta N"] = lista_acta 
print(data_actas)
'''
