"""
This module contains the Two Model Approach (Double Model, Separate Model)

Based on: 
- "Incremental Value Modeling" (Hansotia, 2002)
"""

# =============================================================================
# Contents:
# 1. TwoModel Class
#   1.1 __init__
#   1.2 fit
#   1.3 predict
# =============================================================================

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from causeinfer.algorithms.base_models import BaseModel

class TwoModel(BaseModel):
    
    def __init__(self, control_model=LinearRegression(), treatment_model=LinearRegression()):
        """
        Checks the attributes of the contorl and treatment models before assignment
        """
        try:
            control_model.__getattribute__('fit')
            control_model.__getattribute__('predict')
        except AttributeError:
            raise ValueError('Control model should contains two methods: fit and predict.')

        try:
            treatment_model.__getattribute__('fit')
            treatment_model.__getattribute__('predict')
        except AttributeError:
            raise ValueError('Treatment model should contains two methods: fit and predict.')

        self.control_model = control_model
        self.treatment_model = treatment_model


    def fit(self, X, y, w):
        """
        Parameters
        ----------
        X : numpy ndarray (num_units, num_features) : int, float 
            Dataframe of covariates

        y : numpy array (num_units,) : int, float
            Vector of unit reponses

        w : numpy array (num_units,) : int, float
            Designates the original treatment allocation across units
        ----------
        
        Returns
        -------
        - Two trained models (one for training group, one for control)
        """
        control_X, control_y = [], []
        treatment_X, treatment_y = [], []

        for idx, el in enumerate(w):
            if el:
                treatment_X.append(X[idx])
                treatment_y.append(y[idx])
            else:
                control_X.append(X[idx])
                control_y.append(y[idx])
        
        self.control_model.fit(control_X, control_y)
        self.treatment_model.fit(treatment_X, treatment_y)
        
        return self


    def predict(self, X_pred, w_pred=None):
        """
        Parameters
        ----------
        X_pred : int, float
            New data on which to make a prediction
        ----------
        
        Returns
        -------
        - A NumPy array of predicted outcomes for each unit in X_pred based on treatment assignment
        """
        pred_treatment = self.treatment_model.predict(X_pred)
        pred_control = self.control_model.predict(X_pred)

        pred_tuple = (pred_treatment, pred_control)
        
        return pred_tuple