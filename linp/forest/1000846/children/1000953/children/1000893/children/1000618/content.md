# Joint-residue normal form for spanning paths in Boolean Schur systems

## Statement

Let A be a finite subset of an elementary abelian 2-group with 0 notin A and |A|=2ell+1. Let H(A) consist of all triples {x,y,x+y} contained in A. Then H(A) has a spanning P_ell if and only if there are distinct joints j_1,...,j_{ell-1} in A such that the ell-2 consecutive sums s_i=j_i+j_{i+1} are distinct and lie in A\J, and the four residual points R=A\(J union {s_1,...,s_{ell-2}}) can be partitioned R={a,b,c,d} with a+b=j_1 and c+d=j_{ell-1}. Necessarily XOR(J)=XOR(A).

## Body

Suppose first that e_1,...,e_ell is a spanning linear path. Let
  j_i=e_i intersect e_{i+1},  1<=i<=ell-1.
These ell-1 joints are distinct. For each internal edge e_{i+1}, 1<=i<=ell-2, its third vertex is forced by the additive triple law to be
  s_i=j_i+j_{i+1}.
Because the path is linear, the s_i are distinct, none lies in J, and all lie in A.

A spanning ell-edge 3-uniform linear path has 2ell+1 vertices. The joints account for ell-1 vertices and the internal private vertices s_i account for ell-2 more, so exactly four vertices remain. They are the two private vertices a,b of the first edge and the two private vertices c,d of the last edge. Since every edge has vector sum zero,
  a+b=j_1,
  c+d=j_{ell-1}.
Thus the stated normal form holds.

Conversely, suppose distinct j_1,...,j_{ell-1} and residual points a,b,c,d satisfy the stated conditions, and all sets involved are pairwise disjoint by definition of the residual set. Define
  e_1={a,b,j_1},
  e_{i+1}={j_i,j_i+j_{i+1},j_{i+1}}  for 1<=i<=ell-2,
  e_ell={j_{ell-1},c,d}.
Every displayed triple is an edge of H(A). Consecutive edges meet in the designated joint, and all other vertices used by the edges are distinct, so nonconsecutive edges are disjoint. The edges therefore form a spanning P_ell.

For the XOR identity, telescope:
  XOR_i s_i
   = (j_1+j_2)+...+(j_{ell-2}+j_{ell-1})
   = j_1+j_{ell-1}.
Also
  a+b+c+d=j_1+j_{ell-1}.
Since A is the disjoint union of J, the internal-sum set, and the four residual points, these two contributions cancel in characteristic two and
  XOR(A)=XOR(J).

Equivalently, for a candidate joint set J define the allowable joint graph Gamma_A(J) on J by joining x,y when x+y lies in A\J, and color xy by x+y. A spanning P_ell is exactly a rainbow Hamilton path of Gamma_A(J) whose unused four A-points admit the two endpoint pairings above. This is the natural graph-theoretic generalization of the new PG(3,2) proof.
