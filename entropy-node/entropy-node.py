import numpy as np
from collections import Counter
def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    counts = Counter(y)
    ans = 0
    for item, count in counts.items():
        p = count/(len(y))
        ans += -(p*np.log2(p))
    return float(ans)
    pass