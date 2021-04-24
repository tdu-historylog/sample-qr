from .generate import QrGenerate
import pprint


def main():
  dir_name = 'export'

  qr: QrGenerate = QrGenerate(dir_name, r'(20)?([1-9])([01]?[0-9])([0-9][0-9])-[0-9A-Z]{2,4}', None)
  ids = qr.generate(10)

  pprint.pprint(ids)
