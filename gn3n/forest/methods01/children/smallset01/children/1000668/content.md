# Opposite reverse hooks on a five-path force a Hamiltonian outer five-window

## Statement

Let H be a boundary tournament, let (a,b,c,d,e) be a tight path, and let x be a sixth vertex such that (x,b,a) and (e,d,x) are tight. Then the two five-sets X_L={a,b,c,d,x} and X_R={b,c,d,e,x} cannot both be non-Hamiltonian. More precisely, if X_L is non-Hamiltonian then (x,b,c,d,e) is a tight Hamilton path on X_R; symmetrically, if X_R is non-Hamiltonian then (a,b,c,d,x) is a tight Hamilton path on X_L.

## Body

Assume first that X_L is non-Hamiltonian. By smallset01, every non-Hamiltonian five-vertex boundary tournament is edge-orderable, so choose an edge order representing H[X_L]. Tightness of (x,b,a), (a,b,c), and (b,c,d) gives the strict chain xb<ab<bc<cd. Hence xb<bc, which means (x,b,c) is tight. Together with the inherited tight triples (b,c,d) and (c,d,e), this makes (x,b,c,d,e) a tight Hamilton path on X_R. The symmetric argument starts from non-Hamiltonicity of X_R: in an edge order representing H[X_R], tightness of (b,c,d), (c,d,e), and (e,d,x) gives bc<cd<de<dx, hence cd<dx, so (c,d,x) is tight. Together with (a,b,c) and (b,c,d), this makes (a,b,c,d,x) a tight Hamilton path on X_L. Therefore X_L and X_R cannot both be non-Hamiltonian.