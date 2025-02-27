import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 101, size=(5, 2)), columns=['X', 'Y'])
print(df['X'].sum())