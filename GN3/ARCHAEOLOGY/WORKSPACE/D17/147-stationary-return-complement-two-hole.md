# The return-path complement is a two-hole deletion of the ancestral Y-Z source seam

**Workspace:** D17
**State:** working
**Key:** `stationary-return-complement-two-hole`

**Summary:** In the stationary SANDWICH return orientation, write Y=(N,s,b,y) and retain the ancestral source path Y-z-(Z-z). For the actual (k+1)-path Q=(M,r,u,p,y), put C=(Y-y)+Z. The inherited word (N,s,b,z,z_2,...) spans C and has exactly two uncertified turns alpha=(s,b,z) and beta=(b,z,z_2). If both are tight, C is Hamiltonian and Q|C is an exact H-a singleton cover with rail sizes k+1 and 2k-1, contradicting subminimum-source saturation. If both are bad, R3 gives the labelled reverse P4 (z_2,z,b,s). The two one-hole cells yield the corresponding single exact reverse turn. R933 does not apply automatically because no Hamilton absorber on the outside support exposing b,z in the required roles has been constructed. This is a complement-completion reduction, not a closure theorem.

### Setup\
Retain `stationary-sandwich-return-square` in the orientation (u,p,y), with X=(M,r,a,u), Y=(N,s,b,y), and the actual Hamilton path Q=(M,r,u,p,y) on (X+p-a)+y. Put C=(Y-y)+Z. The complement of Q in H is C+{a}.\
\
The stationary ancestral Y-source is the literal tight path\
\
  (N,s,b,y,z,z_2,...),\
\
where (z,z_2,...) is the retained Z suffix, with nonexistent boundary turns omitted in the short terminal degeneracy. Delete the internal vertex y. The resulting vertex-simple word\
\
  R_C=(N,s,b,z,z_2,...)\
\
spans exactly C. Every consecutive turn is inherited from the ancestral source except possibly\
\
  alpha=(s,b,z),\
  beta=(b,z,z_2).\
\
Thus C has a canonical two-hole Hamilton proposal tied to the actual source order.\
\
### Immediate cases\
If every existing hole is tight, R_C Hamiltonizes C. Then Q|R_C is an exact two-cover of H-a with rail sizes k+1 and 2k-1. In the live stationary regime both are below a=2k, so `subminimum-source-saturation` contradicts this singleton source.\
\
If alpha and beta both exist and are both bad, boundary antisymmetry gives\
\
  (z,b,s),  (z_2,z,b)\
\
tight, hence the literal labelled P4\
\
  (z_2,z,b,s).\
\
If exactly one of alpha,beta is bad, its complete reverse is a graph-intrinsic tight turn and the other seam is tight. These are the two one-hole complement cells. No closure is claimed from the single reverse turn or from the both-bad P4.\
\
### Why R933 is not an automatic consumer\
The accepted two-ended absorber theorem R933 would require, for the two literal rails Y-y and Z and chosen endpoints b,z, a Hamilton absorber on the complementary support together with b,z exposed in the required endpoint roles. The return path Q has support (X+p-a)+y, while the complement of C in H is Q-support plus a. No Hamilton path on that outside support with the required b,z roles has been constructed. Therefore R933 cannot be invoked merely from the existence of Q.\
\
### Current target\
The return branch is reduced to consuming the two one-hole seam cells or the labelled reverse-P4 cell using the actual return-square fibers and the retained terminal reversal y->b. A successful consumer may Hamiltonize C, Hamiltonize C+a, realize R561 on one fixed support, or produce a legal support transfer. Any such proof must retain literal vertex partitions and complete seam windows.\
\
Status: working reduction only.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "related",
        "revision_id": "R933"
    },
    {
        "relation": "dependency",
        "revision_id": "R953"
    }
]
```
