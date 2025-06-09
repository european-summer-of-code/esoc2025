"""
Utility functions for causal time series analysis.
"""

import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns


def plot_causal_graph(edges, title="Causal Graph", figsize=(10, 8)):
    """Plot a causal graph using networkx and matplotlib.
    
    Parameters
    ----------
    edges : list of tuples
        List of (source, target) pairs representing causal edges
    title : str, default="Causal Graph"
        Title for the plot
    figsize : tuple, default=(10, 8)
        Figure size (width, height) in inches
        
    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure object
    """
    # Create directed graph
    G = nx.DiGraph()
    G.add_edges_from(edges)
    
    # Set up the plot
    plt.figure(figsize=figsize)
    pos = nx.spring_layout(G)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue',
                          node_size=500, alpha=0.6)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color='gray',
                          arrows=True, arrowsize=20)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=10)
    
    plt.title(title)
    plt.axis('off')
    
    return plt.gcf()


def plot_time_series_with_intervention(data, intervention_time, title="Time Series with Intervention"):
    """Plot time series data with an intervention point marked.
    
    Parameters
    ----------
    data : pd.DataFrame
        Time series data with variables as columns
    intervention_time : int or datetime
        Time point of the intervention
    title : str, default="Time Series with Intervention"
        Title for the plot
        
    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure object
    """
    plt.figure(figsize=(12, 6))
    
    for col in data.columns:
        plt.plot(data.index, data[col], label=col)
    
    plt.axvline(x=intervention_time, color='r', linestyle='--',
                label='Intervention')
    
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    
    return plt.gcf() 