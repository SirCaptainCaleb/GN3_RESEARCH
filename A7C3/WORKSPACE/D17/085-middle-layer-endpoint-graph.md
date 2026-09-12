# Endpoint-deletion Johnson graph and local endpoint shields

**Workspace:** D17
**State:** working
**Key:** `middle-layer-endpoint-graph`

**Summary:** Foundational middle-layer reduction: endpoint deletion creates the Johnson incidence system, natural orientations and endpoint-rich cores, universal endpoint shields, the transferred local maximum-path packet, and the exact limitation motivating Hall structure.

### 1. Endpoint deletion turns the complete middle layer into a Johnson graph with excess

Assume the quiet alternative of `extremal-root-compression`: |V(H)|=2k+1, every k-subset supports a Hamilton tight path, and no (k+1)-subset supports one. Choose, once and for all, one actual Hamilton order

  P_S=(v_1,...,v_k)

for every k-set S. Put

  R_S^- = S-{v_1},   R_S^+ = S-{v_k}.

Both are (k-1)-sets. They differ by the one-for-one exchange v_k <-> v_1, so they are adjacent in the Johnson graph J(2k+1,k-1). Define F to have all (k-1)-sets as vertices and, for each k-set S, the single edge

  e_S = R_S^- R_S^+.

Different k-sets give different edges, because the union of the endpoints of e_S is exactly S. Hence

  |V(F)| = C(2k+1,k-1),
  |E(F)| = C(2k+1,k).

Therefore

  2|E(F)|/|V(F)| = 2(k+2)/k = 2+4/k.

In particular F is not a disjoint union of paths and cycles. It has a vertex of degree at least three and, quantitatively,

  sum_R (deg_F(R)-2) = 2|E(F)|-2|V(F)| = (4/k)|V(F)|.

Equivalently, after isolated/leaf contributions are included in the usual component identity, the total cyclomatic excess is positive; some connected component contains at least two independent cycles unless negative tree-component contributions absorb part of the displayed degree excess. The robust conclusion needed below is simply that branching endpoint-cores are unavoidable and F contains a cycle because |E(F)|>|V(F)|.

The edge e_S is not an abstract support relation. Its two exchanged physical vertices are exactly the two endpoints v_1,v_k of the chosen Hamilton path P_S. Thus F is an endpoint-certified Johnson subgraph.

### 2. Natural orientation and endpoint-rich cores

Orient e_S from R_S^- to R_S^+. Then

  outdeg_F(R)

counts completion vertices x outside R for which the chosen Hamilton path on R+x begins at x, while

  indeg_F(R)

counts completion vertices x for which that path ends at x. Since there is one oriented edge per k-set,

  average outdegree = average indegree = C(2k+1,k)/C(2k+1,k-1) = (k+2)/k = 1+2/k.

Consequently some core has outdegree at least two and some core has indegree at least two. Ignoring orientation, some core has at least three distinct endpoint completions. This recovers the direct double count

  2 C(2k+1,k) / C(2k+1,k-1) = 2+4/k > 2.

For such an incidence R --(x)-- S=R+x, deleting endpoint x from the chosen P_S leaves an actual Hamilton path on the same core R. Hence a degree-r core comes with r actual Hamilton orders of one fixed physical support R, each inherited from a different one-vertex completion. No internal-vertex trimming is being called Hamiltonian here; only literal endpoint deletion is used.

### 3. Every selected Johnson edge carries universal endpoint shields

Retain one selected k-set path

  P_S=(v_1,v_2,...,v_{k-1},v_k).

Let x be any exterior vertex, x notin S. Since no (k+1)-set is Hamiltonian, neither xP_S nor P_Sx can be tight. Their only new turns are respectively

  (x,v_1,v_2),
  (v_{k-1},v_k,x).

Both are therefore bad. Boundary antisymmetry R3 gives the exact reversals

  (v_2,v_1,x),
  (x,v_k,v_{k-1})

tight. These hold simultaneously for every one of the k+1 exterior vertices.

Thus the endpoint-certified Johnson edge e_S carries two universal physical shields: the reverse initial dimer (v_2,v_1) is tail-signed by every exterior vertex, and the reverse terminal dimer (v_k,v_{k-1}) is head-signed by every exterior vertex. This is the order data lost by the bare support-level middle-layer statement.

A useful immediate exclusion follows. If some Hamilton path of the same support S starts with (u,v), then no Hamilton path of S can end with (v,u). Indeed failed prepend of any exterior x to the first path forces (v,u,x) tight; appending x to a path ending (v,u) would then Hamilton-extend S to k+1 vertices. This is precisely the boundary-reversed Hamilton-dimer obstruction in the globally longest setting, but the argument above is self-contained.

### 4. The uploaded maximum-path argument yields a stronger local packet in boundary tournaments

Section 7 reconstructed the user's `lem:noDisjointMaxPaths` argument from `main-appendix.tex`. Its triangle-free (3,4)-tournament contradiction uses the fact that two specified cyclic rotations of one mixed triple cannot both be absent. In a boundary tournament they can both be absent, but R3 then gives more structured surviving data than a generic gap.

In the last-out-edge branch, after naming the failed seam as

  (w,u,v)

and the extremally forbidden cyclic rotation as

  (u,v,w),

the exact naming in section 7 may be cyclically shifted; what matters is that two cyclic rotations are bad. Reversing those two bad turns produces, after relabeling the oriented physical dimer as D=(p,q) and the third vertex as r,

  (r,p,q) tight,
  (p,q,r) tight.

The no-out alternating-word branch gives the identical form. Therefore every failed paper-style augmentation in a boundary tournament yields one oriented physical dimer D=(p,q) that is signed on BOTH sides by the SAME physical witness r.

If the same oriented dimer D receives two distinct witnesses r,s from two such packets, then both

  (r,p,q,s),
  (s,p,q,r)

are literal tight P4s. This is a strictly stronger interpretation of the transferred cyclic gap than merely recording two absent rotations. It still does not by itself provide a k+1-path because D can be an internal reverse state of one maximum rail and the outer junctions needed to reinstall that P4 into the full rail are not certified.

### 5. Exact limitation and next parent target

The endpoint graph F is genuinely global, but its most obvious local consumers are insufficient. A branching core of degree three merely gives three endpoint-realized one-vertex completions of one Hamilton (k-1)-support; local boundary-tournament models can realize such endpoint-rich cores without forcing a two-vertex Hamilton extension. Likewise a same-witness bidirectional dimer, even with a second witness and the two resulting P4s, need not by itself extend an arbitrary maximum rail by one vertex once the two outer junctions are audited.

Therefore the remaining middle-layer theorem should be formulated as synchronization across F, not as another one-core extension lemma. Each F-edge supplies:

* a one-for-one physical support exchange;
* an actual Hamilton order whose endpoints are exactly the exchanged labels;
* two terminal ordered dimers;
* universal reverse shields on those dimers indexed by all k+1 exterior vertices.

The next useful theorem would consume a cycle or branching subgraph of F by comparing these endpoint orders on overlapping cores. A successful statement must either produce a Hamilton (k+1)-support directly or produce a boundary-reversed Hamilton dimer on one fixed k-support, which then universally extends by the elementary R3 argument above. Merely extracting another isolated P4, signed packet, or support replacement does not discharge the branch.

Status: all combinatorial identities and endpoint-shield deductions above are complete internal arguments in this DR revision. The claimed local insufficiency is a strategy fence supported by exact computational diagnostics from the current research session but is not deposited here as a certificate theorem. No canonical review status is asserted.



## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
