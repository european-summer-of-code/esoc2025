"""
Causal structure learning for time series data.
"""

import numpy as np
import pandas as pd
from pgmpy.estimators import HillClimbSearch, BicScore
from pgmpy.models import DynamicBayesianNetwork


class CausalStructureLearner:
    """Learn causal structure from time series data.
    
    This class implements methods for learning causal relationships
    between time series variables using score-based structure learning.
    
    Parameters
    ----------
    n_lags : int, default=1
        Number of time lags to consider in the causal model.
    scoring_method : str, default='bic'
        Scoring method to use for structure learning.
        Options: 'bic', 'aic', 'k2'
    """
    
    def __init__(self, n_lags=1, scoring_method='bic'):
        self.n_lags = n_lags
        self.scoring_method = scoring_method
        self.model = None
        
    def fit(self, data):
        """Learn causal structure from time series data.
        
        Parameters
        ----------
        data : pd.DataFrame
            Time series data with variables as columns
            
        Returns
        -------
        self : returns an instance of self
        """
        # Create lagged features
        lagged_data = self._create_lagged_features(data)
        
        # Initialize structure learning
        if self.scoring_method == 'bic':
            scoring_method = BicScore(lagged_data)
        else:
            raise ValueError(f"Scoring method {self.scoring_method} not implemented")
            
        # Learn structure using hill climbing
        hc = HillClimbSearch(lagged_data)
        self.model = hc.estimate(scoring_method=scoring_method)
        
        return self
    
    def _create_lagged_features(self, data):
        """Create lagged features for structure learning.
        
        Parameters
        ----------
        data : pd.DataFrame
            Original time series data
            
        Returns
        -------
        lagged_data : pd.DataFrame
            Data with lagged features
        """
        lagged_data = pd.DataFrame()
        
        for col in data.columns:
            for lag in range(self.n_lags + 1):
                lagged_data[f"{col}_{lag}"] = data[col].shift(lag)
                
        return lagged_data.dropna()
    
    def get_edges(self):
        """Get learned causal edges.
        
        Returns
        -------
        edges : list of tuples
            List of (source, target) pairs representing causal edges
        """
        if self.model is None:
            raise ValueError("Model has not been fitted yet.")
            
        return list(self.model.edges())
    
    def to_dbn(self):
        """Convert learned structure to Dynamic Bayesian Network.
        
        Returns
        -------
        dbn : DynamicBayesianNetwork
            Dynamic Bayesian Network representation of the causal structure
        """
        if self.model is None:
            raise ValueError("Model has not been fitted yet.")
            
        dbn = DynamicBayesianNetwork()
        
        # Add nodes and edges from learned structure
        for edge in self.model.edges():
            source, target = edge
            dbn.add_edge(source, target)
            
        return dbn 