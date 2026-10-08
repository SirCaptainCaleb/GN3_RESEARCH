# Odd uniform middle layer has universal two-ended maximum-path reversal — preserved pre-item development

## Development

Assume the exact odd uniform middle-layer state:
n=2r+1, every r-set is Hamiltonian, and every (r+1)-set is non-Hamiltonian.

Then the maximum Hamiltonian-support order is exactly r.

Let
P=(p_1,...,p_r)
be ANY Hamiltonian path of order r. For every exterior vertex x, P+x is a non-Hamiltonian (r+1)-set. Therefore x cannot be inserted at either endpoint of this displayed order. Boundary antisymmetry gives
h(p_2,p_1,x)=1,
h(x,p_r,p_{r-1})=1.
Hence every exterior vertex simultaneously reverses both exposed end-edges of every displayed maximum path.

More generally fix x outside P. The complement
Q=V(H)-(V(P) union {x})
has order r and is Hamiltonian by the uniform hypothesis. Thus
H-x=P|Q
is a balanced deletion cover. Since adjoining x to either side creates an (r+1)-set, both extensions are non-Hamiltonian; consequently x reverses all four exposed end-edges of the displayed two-cover, for every choice of Hamilton orders on P and Q.

Equivalently, for every vertex x and every balanced bipartition
V(H)-{x}=A sqcup B,
both A and B are Hamiltonian and x is absolutely noninsertable into every Hamilton order of either side.

In particular, choosing any maximum path A, its complement has order r+1 and is non-Hamiltonian but is two-covered by an r-path and a singleton. Thus the lexicographic longest-path normal form collapses to the exact spanning size profile
r | r | 1,
and the singleton reverses both end-edges of both maximum paths.

This is an exact path-order form of the odd uniform obstruction. Any closure proof for this residue must exploit the simultaneous end-reversal and complete one-for-one exchange structure; support-rank data alone cannot distinguish it from the abstract truncated-path countermodel.
