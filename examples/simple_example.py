"""
Simple example demonstrating the usage of causal_ts package.
"""

import numpy as np
import pandas as pd
from causal_ts import CausalForecaster, CausalStructureLearner, plot_causal_graph

# Generate synthetic data
np.random.seed(42)
n_samples = 1000

# Create time series with causal relationships
t = np.arange(n_samples)
price = 100 + 0.1 * t + np.random.normal(0, 5, n_samples)
demand = 50 - 0.2 * price + 0.1 * t + np.random.normal(0, 3, n_samples)
inventory = 200 - 0.5 * demand + np.random.normal(0, 10, n_samples)

# Create DataFrame
data = pd.DataFrame({
    'price': price,
    'demand': demand,
    'inventory': inventory
}, index=pd.date_range('2023-01-01', periods=n_samples, freq='D'))

# Learn causal structure
structure_learner = CausalStructureLearner(n_lags=2)
structure_learner.fit(data)

# Plot learned causal graph
edges = structure_learner.get_edges()
fig = plot_causal_graph(edges, title="Learned Causal Structure")
fig.savefig('causal_graph.png')

# Create and fit causal forecaster
forecaster = CausalForecaster(n_lags=2)
forecaster.fit(data['demand'], X=data[['price', 'inventory']])

# Make predictions
fh = pd.date_range('2023-04-01', periods=30, freq='D')
predictions = forecaster.predict(fh)

print("\nPredictions for next 30 days:")
print(predictions) 