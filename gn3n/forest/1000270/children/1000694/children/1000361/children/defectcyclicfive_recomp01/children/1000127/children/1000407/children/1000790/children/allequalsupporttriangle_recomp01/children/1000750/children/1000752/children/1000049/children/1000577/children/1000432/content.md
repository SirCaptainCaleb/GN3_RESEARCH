# Without an endpoint-edge reversal, all three transferred-label insertions are internal

## Statement

Assume the all-three-successful-insertion branch of 1278e049ce8e. If the endpoint-edge-reversal alternative of b2f0a8047d8d does not occur, then for every j modulo three the successful insertion of t_{j+2} into P_j=(t_j,M_j,t_{j+1}) lies strictly between t_j and t_{j+1}; in particular it is neither before t_j nor after t_{j+1}. Thus the reversal-free successful-insertion residue consists of three genuine internal insertion gaps, one in each M_j corridor.

## Body

Fix j. Suppose first that t_{j+2} is inserted before t_j, so R_j=(t_{j+2},t_j,M_j,t_{j+1}) in block notation. Then R_j reverses the cyclic pair t_{j+1},t_{j+2} relative to P_{j+1}=(t_{j+1},M_{j+1},t_{j+2}). Apply b2f0a8047d8d with i=j+1. By hypothesis its endpoint-edge-reversal alternative is absent, so its tight-cycle alternative occurs. Here the R_j subpath from t_{j+2} to t_{j+1} is all of R_j, hence the resulting tight cycle has support T union V(M_j) union V(M_{j+1}). Opening that cycle gives a Hamilton path on this support. The complementary vertex set is exactly V(M_{j+2}), which is already a tight path. These two paths span H, contradiction. Dually, if t_{j+2} is inserted after t_{j+1}, then R_j reverses the pair t_{j+2},t_j relative to P_{j+2}; applying b2f0a8047d8d with i=j+2 again makes the cycle support all of T union V(M_j) union V(M_{j+2}), whose complement M_{j+1} is a tight path, giving a spanning two-cover. Hence neither endpoint insertion is possible. Applying this for all j proves the claim.
