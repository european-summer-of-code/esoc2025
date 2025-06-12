"""
Causal Time Series Analysis Package

This package provides tools for causal inference in time series data,
integrating pgmpy for causal structure learning and sktime for time series analysis.
"""

__version__ = "0.1.0"

from causal_ts.models import CausalForecaster
from causal_ts.structure import CausalStructureLearner
from causal_ts.utils import plot_causal_graph

__all__ = ["CausalForecaster", "CausalStructureLearner", "plot_causal_graph"] 