import numpy as np
import itertools
from datetime import datetime
import time



start_time = datetime.now()
idx = np.transpose(np.triu_indices(10000, 1)).tolist()
print(datetime.now() - start_time)

print(type(idx))
