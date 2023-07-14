from pydantic import BaseModel
from typing import Optional,List

from utils.helpers import *


class Data(BaseModel):
  fecha:          str = getDate()
  senHumedadAgua: dict
  senHumedadAire: dict
  senPh:          dict
  senCalidadAire: dict


class DataRealTime(BaseModel):
  senHumedadAgua: str
  senHumedadAire: str
  senPh:          str
  senCalidadAire: str
