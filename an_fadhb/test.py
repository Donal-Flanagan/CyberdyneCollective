# Import the classes from the package to try them out
#from an_fadhb.meaning_interpreter.meaning_interpreter import TextImporter
from meaning_interpreter.meaning_interpreter import TextImporter

# Create an object of the TextImporter class
TI = TextImporter()
TI.import_txt_file('some file path')
