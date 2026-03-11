import numpy as np
def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    ans = []
    hits = 0
    for i in range(k):
        if recommended[i] in relevant:
            hits += 1
    ans.append(hits/k)
    ans.append(hits/len(relevant))
    return ans