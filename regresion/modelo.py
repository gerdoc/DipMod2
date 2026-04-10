from typing import AnyStr

import numpy as np
import logging
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor

from archivo.leer_data2 import LeerData2
from config.config import RANDOM_STATE, modelos, get_nombre_modelo


class Modelo:
    def __init__(self, datos:LeerData2, modelo1:bool = True, graficar: bool = False):
        self.__modelo = LinearRegression( )
        self.__datos:LeerData2 = datos
        self.__y_pred = None
        self.__mae: float = None
        self.__mse: float = None
        self.__rmse: float = None
        self.__r2: float = None
        self.__modelo1 = modelo1
        self.__resultado = None
        self.__graficar = graficar

    @property
    def y_pred(self):
        return self.__y_pred

    @property
    def mae(self):
        return self.__mae

    @property
    def mse(self):
        return self.__mse

    @property
    def rmse(self):
        return self.__rmse

    @property
    def r2(self):
        return self.__r2

    @property
    def resultado(self):
        return self.__resultado


    def __fit(self) -> bool:
        self.__modelo.fit(self.__datos.x_train, self.__datos.y_train)
        return hasattr(self.__modelo, "coef_")

    def __fit2(self) -> bool:
        pipeline_xgb = Pipeline([
            ( "model", XGBRegressor(
                objective="reg:squarederror",
                random_state=RANDOM_STATE,
                n_jobs=-1
            ))
        ])
        param_grid_xgb = {
            "model__n_estimators": [100, 200],
            "model__max_depth": [3, 5],
            "model__learning_rate": [0.05, 0.1],
            "model__subsample": [0.8, 1.0],
            "model__colsample_bytree": [0.8, 1.0]
        }

        gridSearchCV = GridSearchCV(
            estimator=pipeline_xgb,
            param_grid=param_grid_xgb,
            scoring="neg_root_mean_squared_error",
            cv=3,
            n_jobs=-1,
            verbose=1
        )
        gridSearchCV.fit(self.__datos.x_train, self.__datos.y_train)
        if gridSearchCV.best_params_ is None:
            return False
        self.__modelo = gridSearchCV.best_estimator_
        logging.info(gridSearchCV.best_params_)
        return self.__modelo is not None

    def __predict(self) -> bool:
        if self.__modelo1 and not self.__fit( ):
            return False
        if not self.__modelo1 and not self.__fit2( ):
            return False
        self.__y_pred = self.__modelo.predict( self.__datos.x_test )
        if self.__graficar:
            self.graficar_regresion( )
        return self.__y_pred is not None

    def procesa_regresion(self ) -> bool:
        if not self.__predict( ):
            return False
        self.__mae = mean_absolute_error( self.__datos.y_test, self.__y_pred)
        self.__mse = mean_squared_error( self.__datos.y_test, self.__y_pred)
        self.__rmse = np.sqrt( self.__mse )
        self.__r2 = r2_score(self.__datos.y_test, self.__y_pred)
        logging.info(f"MAE : {self.__mae:.10f}")
        logging.info(f"MSE : {self.__mse:.10f}")
        logging.info(f"RMSE: {self.__rmse:.10f}")
        logging.info(f"R²  : {self.__r2:.10f}")
        return self.__mae is not None and self.__mse is not None and self.__rmse is not None and self.__r2 is not None

    def prediccion(self, dataframe: pd.DataFrame ):
        self.__resultado = None
        if self.__modelo is None:
            logging.error("Módelo vacio")
            return
        prediccion = self.__modelo.predict( dataframe )
        if prediccion is None:
            logging.error("Predicción vacia")
            return
        self.__resultado = prediccion[0]
        logging.info(f"Predicción usando {get_nombre_modelo( self.__modelo1 )} del precio: {self.__resultado:.10f}")

    def graficar_matriz_confusion( self ):
        cm = confusion_matrix(self.__datos.y_test, self.__y_pred)
        plt.figure( )
        sns.heatmap( cm, annot=True, fmt="d", cmap="Blues")
        plt.xlabel("Predicción")
        plt.ylabel("Valor real")
        plt.title(f"Matriz de confusión - {get_nombre_modelo( self.__modelo1 )}")
        plt.tight_layout()
        plt.show( )

    def graficar_regresion(self, n_muestras:int=30 ):
        sns.set_theme(style="whitegrid")
        plt.rcParams["figure.figsize"] = (10, 6)
        y_true = np.array( self.__datos.y_test)
        y_pred = np.array( self.__y_pred )
        # 1) Gráfico de comparación real vs predicho
        plt.figure()
        sns.scatterplot(x=y_true, y=y_pred, s=70)
        min_val = min(y_true.min(), y_pred.min())
        max_val = max(y_true.max(), y_pred.max())
        plt.plot([min_val, max_val], [min_val, max_val], linestyle="--", linewidth=2)
        plt.xlabel("Valores reales")
        plt.ylabel("Valores predichos")
        plt.title(f"{get_nombre_modelo( self.__modelo1 )} - Reales vs Predichos")
        plt.tight_layout( )
        plt.show()

        # 2) Comparación por observación (t_test vs t_predicted)
        n = min(n_muestras, len(y_true))
        indices = np.arange(n)

        plt.figure()
        plt.plot(indices, y_true[:n], marker="o", label="y_test / t_test")
        plt.plot(indices, y_pred[:n], marker="s", label="y_pred / t_predicted")
        plt.xlabel("Observación")
        plt.ylabel("Precio")
        plt.title(f"{get_nombre_modelo( self.__modelo1 )} - Comparación de valores reales y predichos")
        plt.legend()
        plt.tight_layout()
        plt.show()

        # 3) Distribución de residuos
        residuos = y_true - y_pred
        plt.figure()
        sns.histplot(residuos, kde=True)
        plt.axvline(0, linestyle="--", linewidth=2)
        plt.xlabel("Residuo (real - predicho)")
        plt.title(f"{get_nombre_modelo( self.__modelo1 )} - Distribución de residuos")
        plt.tight_layout()
        plt.show()