import pandas as pd
import numpy as np
import networkx as nx

df=pd.read_csv('calles_de_medellin_con_acoso.csv', delimiter=';')
medellin=nx.from_pandas_edgelist(df,source='origin',target='destination',edge_attr='length' )
##medellin=nx.from_pandas_edgelist(df,source='origin',target='destination',edge_attr='harassmentRisk' )

medellin.nodes()
medellin.edges()
medellin.order()

camino = nx.dijkstra_path(medellin, source='(-75.5728593, 6.2115169)', target='(-75.5686884, 6.2063927)', weight= True)
