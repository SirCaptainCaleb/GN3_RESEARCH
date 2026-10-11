# Checkerboard-free extraction and four-local Hamilton completion limitations

- Stable ID: note_checkerboard_submatrix_and_four_local_hamilton_completion_limits
- Author: NORI editorial extraction; mathematical proofs from cited original composition
- Primary home: subsection:coupled_chronological_saddle_potentials_and_checkerboard_obstructions
- Labels: obstruction, counterexample
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r4593_2
- Updated session: session_nori_r4593_2
- Disposition: none
- Successor: none

## Related references

- subsection:coupled_chronological_saddle_potentials_and_checkerboard_obstructions, exact version 2

## Research note

# Editorial scope and exact provenance

These sections supply proved limitations and finite counterexamples to specific checkerboard/exchange strategies. The independent saddle, minimax and full-class path/defect reductions stay in the Subsection manuscript.

Copied verbatim from Subsection `coupled_chronological_saddle_potentials_and_checkerboard_obstructions`, publication composition v2. The original complete composition remains retrievable.

## 4. Why extraction of large checkerboard-free submatrices cannot yield the general altitude bound

**Theorem 4 (logarithmic clean-submatrix barrier).** In a uniformly random ordering of all edges of \(K_N\), with probability tending to one, every checkerboard-free complete bipartite subgraph with disjoint parts of the same order \(k\) satisfies
\[
k\le \left(\frac8{\log(3/2)}+o(1)\right)\log N.
\tag{5}
\]

**Proof.** Fix disjoint sets \(A,B\) of size \(k\). Partition \(\lfloor k/2\rfloor\) disjoint pairs from \(A\), and likewise from \(B\). The pair products generate \(\lfloor k/2\rfloor^2\) edge-disjoint \(K_{2,2}\) rectangles. For each rectangle, among the six choices of its two smallest edges exactly two choices yield a disjoint pair; its checkerboard-obstruction probability is \(1/3\). Relative orders on disjoint edge sets in a uniform random permutation are independent. Hence
\[
\Pr[(A,B)\ \text{checkerboard-free}]
\le (2/3)^{\lfloor k/2\rfloor^2}.
\]
There are at most \(N^{2k}\) ordered pairs \((A,B)\). The union bound gives
\[
\Pr[\exists\ \text{checkerboard-free }K_{k,k}]
\le N^{2k}(2/3)^{\lfloor k/2\rfloor^2}.
\tag{6}
\]
For \(k=\lceil C\log N\rceil\), the logarithm of (6) equals at most
\[
\left(2C-\frac{C^2}{4}\log(3/2)+o(1)\right)(\log N)^2,
\]
which tends to \(-\infty\) for every \(C>8/\log(3/2)\). The forbidden-rectangle property is hereditary, so exclusion of size \(\lceil C\log N\rceil\) excludes every larger such subgraph. Let \(C\) approach the displayed constant. \(\square\)

Consequently, attempting to prove a polynomial or nearly linear monotone-path bound for *every* edge order by extracting **one** checkerboard-free \(K_{k,k}\) cannot succeed. A successful general argument must accommodate checkerboards and coordinate their effects.

## 5. A finite obstruction to four-local Hamilton completion

**Proposition 5.** There is an edge ordering of \(K_5\) for which every induced \(K_4\) admits an increasing Hamilton path but \(K_5\) admits none.

**Proof (exact certificate).** On vertices \(0,1,2,3,4\), rank the ten edges from 0 to 9 in the following increasing order:
\[
14,\quad12,\quad03,\quad04,\quad23,\quad34,\quad02,\quad13,\quad24,\quad01.
\tag{7}
\]
For each deleted vertex \(v=0,1,2,3,4\), the four-vertex sequences
\[
(1,2,3,4),\quad(0,3,2,4),\quad(0,4,3,1),\quad
(1,4,0,2),\quad(2,3,1,0),
\]
respectively, are increasing Hamilton paths in the remaining graph. Their edge-rank sequences are, respectively,
\[
(1,4,5),\quad(2,4,8),\quad(3,5,7),\quad(0,3,6),\quad(4,7,9).
\]
A complete finite enumeration of vertex-simple directed increasing paths of orders \(2,3,4,5\) gives counts \(20,30,12,0\). These counts can be reproduced without a solver by the following certificate:

```python
from itertools import permutations
edges = ["14","12","03","04","23","34","02","13","24","01"]
rank = {frozenset(map(int,e)):i for i,e in enumerate(edges)}
def increasing(p):
    e = [rank[frozenset((p[i],p[i+1]))] for i in range(len(p)-1)]
    return all(x < y for x,y in zip(e,e[1:]))
print([sum(increasing(p) for p in permutations(range(5),k))
       for k in (2,3,4,5)])
# [20, 30, 12, 0]
```

Therefore every four-vertex restriction has a positive spanning tight path under the associated global-edge-order boundary tournament, but the five-vertex tournament has no positive spanning tight path. Reverse orientation converts increasing paths to decreasing paths, so no negative spanning tight path exists either. \(\square\)

This invalidates the inference from Hamiltonicity of every induced four-vertex boundary chart to global Hamiltonicity. It does not limit the established long-path theorems.
