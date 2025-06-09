# Causal Time Series Analysis

A Python package for causal inference in time series data, integrating `pgmpy` for causal structure learning and `sktime` for time series analysis.

## Installation

```bash
pip install -r requirements.txt
```

## Features

- Causal structure learning for time series data
- Dynamic Bayesian Network-based forecasting
- Integration with scikit-learn and sktime ecosystems
- Visualization tools for causal graphs and interventions

## Quick Start

```python
import pandas as pd
from causal_ts import CausalForecaster, CausalStructureLearner, plot_causal_graph

# Load your time series data
data = pd.DataFrame(...)

# Learn causal structure
structure_learner = CausalStructureLearner(n_lags=2)
structure_learner.fit(data)

# Plot learned causal graph
edges = structure_learner.get_edges()
plot_causal_graph(edges)

# Create and fit causal forecaster
forecaster = CausalForecaster(n_lags=2)
forecaster.fit(data['target'], X=data[['feature1', 'feature2']])

# Make predictions
predictions = forecaster.predict(fh)
```

## Components

### CausalForecaster

A forecasting model that combines time series forecasting with causal inference using Dynamic Bayesian Networks.

```python
from causal_ts import CausalForecaster

forecaster = CausalForecaster(n_lags=2)
forecaster.fit(y, X)
predictions = forecaster.predict(fh)
```

### CausalStructureLearner

Learn causal relationships between time series variables using score-based structure learning.

```python
from causal_ts import CausalStructureLearner

learner = CausalStructureLearner(n_lags=2)
learner.fit(data)
edges = learner.get_edges()
```

### Visualization Tools

Plot causal graphs and time series with interventions.

```python
from causal_ts import plot_causal_graph, plot_time_series_with_intervention

# Plot causal graph
plot_causal_graph(edges)

# Plot time series with intervention
plot_time_series_with_intervention(data, intervention_time)
```

## Examples

See the `examples` directory for complete examples:

- `simple_example.py`: Basic usage with synthetic data
- More examples coming soon...

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 