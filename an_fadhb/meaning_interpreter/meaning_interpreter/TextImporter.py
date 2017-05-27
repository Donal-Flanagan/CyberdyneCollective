class TextImporter:
    def __init__(self):
        """ This is where we initialize the class """
        self.initial_variable = 'Some initial var here'

    def import_txt_file(self, filepath):
        print('initial_variable:', self.initial_variable)
        print('\nfilepath:', filepath)