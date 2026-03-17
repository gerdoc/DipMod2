from typing import List

FLAGS: List[int] = [ 1, 1, 1, 1, 1,1 ,1, 1]
EPOCHS: int = 1000
LEARNING_RATE: float = 0.0000000001
PORCENTAGE_TRAIN: float = 0.8
FILE_PATH: str = "csv/housing.csv"
COLUMNS: List[str] = ['_w_long', '_w_lat', '_w_age', '_w_rooms', '_w_bedrooms','_w_pop', '_w_house', '_w_income', '_bias']
SEED: int = 12345
MU: float = 0.0
SIGMA: float = 0.001
