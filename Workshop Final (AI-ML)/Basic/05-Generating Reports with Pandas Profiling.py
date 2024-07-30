# Automated Reporting: Generating Reports with Pandas Profiling

import pandas as pd
from pandas_profiling import ProfileReport

# Example data
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 3, 5, 7, 11]
})

profile = ProfileReport(data, title="Pandas Profiling Report")
profile.to_file("report.html")
