import pandas as pd
from init_support import AFIT
from Utilize import init_SRS_edges
afit = AFIT('reqlf13')

print(afit.visibility_arcs_length)
print(afit.read_support_id()[3])

edges = init_SRS_edges(AFIT)
print(edges)
