"""
author: YutoWatanabe <yuto.w51942@gmail.com>

version: 1.0.0

Copyright (C) 2020 tdu-historylog project
"""
import os
from typing import Optional, List

import rstr
import qrcode


class QrGenerate:
  """
  Generate qr codes.
  """
  dir_name: str
  dir_path: str
  path: str
  pattern: str

  def __init__(self, dir_name: str, pattern: str, dir_path: Optional[str]):
    """
    Create instance.

    Args:
        dir_name (str): qr codes save directory name.
        dir_path (Optional[str]): path of directory.
    """
    self.dir_name = dir_name
    self.pattern = pattern

    if dir_path is None:
      self.dir_path = os.path.dirname(os.path.dirname(__file__))
    else:
      self.dir_path = dir_path

    self.path = os.path.join(self.dir_path, self.dir_name)

    if not os.path.isdir(self.path):
      os.makedirs(self.path)

  def generate(self, quantity: int) -> List[str]:
    """
    generate qr codes.

    Args:
        quantity (int): Number of qr codes to export.
    """
    ids = []
    header = 'jp.ac.dendai/'

    for index in range(quantity):
      id: str = self.create_id(self.pattern)
      ids.append(header+id)
      file = os.path.join(self.path, f'{id}.png')

      qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=10,
          border=4,
      )
      qr.add_data(header+id)
      qr.make(fit=True)
      img = qr.make_image(fill_color="black", back_color="white")
      img.save(file)

    return ids

  @staticmethod
  def create_id(pattern: str) -> str:
    """
    Create id string.

    Args:
        pattarn (str): Regular expression.

    Returns:
        str: generated id.
    """
    return rstr.xeger(pattern)
