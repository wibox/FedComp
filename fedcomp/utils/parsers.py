import argparse

class ManagerParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()
        self._add_default_arguments()
        self.args = self.parser.parse_args()

    def _add_default_arguments(self):
        self.parser.add_argument()

    def get_parser(self):
        return self.parser
    
    def get_arguments_collection(self):
        return vars(self.args)