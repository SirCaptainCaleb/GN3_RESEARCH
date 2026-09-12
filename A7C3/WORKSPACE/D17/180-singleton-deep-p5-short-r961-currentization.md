# The short G1 overlap is a six-puncture common-complement R435 reservoir

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-p5-short-r961-currentization`

**Summary:** In the |M|=2 G1 overlap of SV15843, writing M=(v,u), the two passing endpoint alignments make C=(s,q,t,p,u) a tight 5-cycle on U-v where U={s,q,t,p,u,v}. U itself is non-Hamiltonian because B is a literal Hamilton complement. Counterexamplehood forces v to head- and tail-sign every reverse boundary dimer of C. Six explicit directed comparison cycles, one inside each U-x, then imply by accepted R887/R902 that every five-subset U-x is Hamiltonian. Hence for every x in U there is an exact singleton row H-x=P_x|B with the same literal complement B, and B+x is non-Hamiltonian. Applying the accepted source-anchored R961 fan to X=C,p=v, the only R435-quiet HHH form would require (v,t,p), contradicted by tight (p,t,v), while the only quiet TTT form would require (q,t,v), contradicted by tight (v,t,q). Thus the short G1 cell necessarily yields explicit source-visible cross-fiber R435 geometry inside an all-six-puncture common-complement family. This is a currentization, not closure or same-support R561.


### 1. Exact short-overlap setup
Retain `singleton-deep-p5-endpoint-aligned-recompletion` at exact section version SV15843. Work only in its surviving G1 overlap with

  M=(v,u),
  R=(s,v,u,p,q)|B

an exact two-cover of H-t, and with both G1 endpoint-alignment seams tight:

  (u,s,q),   (p,u,s).

The parent G1 path is

  C=(s,q,t,p,u),

and its five cyclic turns are all tight:

  (s,q,t), (q,t,p), (t,p,u), (p,u,s), (u,s,q).      (SC.1)

Put

  U={s,q,t,p,u,v}.

If U had a Hamilton path, that path together with the retained literal Hamilton rail B would be a spanning two-cover of H. Hence U is non-Hamiltonian.

### 2. The residual vertex signs both sides of every reverse cycle boundary
Take any cyclic rotation (a0,a1,a2,a3,a4) of C. If (v,a0,a1) were tight, then

  (v,a0,a1,a2,a3,a4)

would Hamiltonize U. Therefore (v,a0,a1) is bad and, by R3,

  (a1,a0,v)

is tight. Likewise, if (a3,a4,v) were tight then the corresponding rotation followed by v would Hamiltonize U, so

  (v,a4,a3)

is tight. Equivalently, for every directed boundary edge ai->a{i+1} of C, the reverse dimer a{i+1}->ai is both head- and tail-signed by v:

  (v,a{i+1},ai),   (a{i+1},ai,v) tight.              (SC.2)

In particular retain

  (v,q,s),(q,s,v),
  (v,t,q),(t,q,v),
  (v,p,t),(p,t,v),
  (v,u,p),(u,p,v),
  (v,s,u),(s,u,v).                                    (SC.3)

The old exact H-t rail also supplies

  (s,v,u), (v,u,p), (u,p,q).                          (SC.4)

### 3. Every five-subset of U is Hamiltonian
Use accepted R887 to read tight turns as directed comparisons between incident ordinary edges, and accepted R902 in contrapositive form: a five-set carrying a directed comparison cycle is Hamiltonian.

For each omitted label, the following tight turns give a directed comparison cycle entirely inside U-x:

- x=s: at middle p,
    (v,p,t), (t,p,u), (u,p,v),
  giving pv -> pt -> pu -> pv.

- x=q: at the three middles u,s,
    (s,u,v), (v,u,p), (p,u,s),
  giving su -> uv -> pu -> su.

- x=t: the same cycle su -> uv -> pu -> su.

- x=p:
    (u,s,q), (q,s,v), (v,s,u),
  giving su -> qs -> sv -> su.

- x=u: at middle q,
    (v,q,s), (s,q,t), (t,q,v),
  giving qv -> qs -> qt -> qv.

- x=v: the cycle supplied by C itself,
    (u,s,q), (s,q,t), (q,t,p), (t,p,u), (p,u,s),
  giving su -> qs -> qt -> pt -> pu -> su.

Thus

  U-x is Hamiltonian for every x in U.                (SC.5)

This does not assert that U is Hamiltonian; U is already known non-Hamiltonian.

### 4. Six exact singleton fibers share the literal complement B
For each x in U choose any Hamilton path P_x on U-x. Then

  P_x | B

is a literal two-cover of H-x. It is exact, since H-x cannot be Hamiltonian in a smallest counterexample. Therefore all six singleton fibers are current with the same literal Hamilton complement B.

Moreover

  B+x is non-Hamiltonian for every x in U,             (SC.6)

because otherwise a Hamilton path on B+x together with P_x would two-cover H.

If B=(b0,...,bk), then every literal endpoint insertion of x into B fails, so R3 gives the synchronized reverse-boundary stars

  (b1,b0,x),   (x,bk,b{k-1}) tight for every x in U.  (SC.7)

These six-witness stars are retained and are strictly stronger data than one anonymous R542 packet.

### 5. The source-anchored R961 quiet alternatives are impossible
Apply the accepted exact section `source-anchored-r961-fan` SV304 to

  Omega=U,   X=C=(s,q,t,p,u),   exterior label v.

That theorem says that, outside explicit X-relative R435 geometry, the R961 constant-role triangle must be one of two source-anchored quiet packets.

In the HHH packet the anchors are the first two vertices s,q of C. Its puncture path omitting s has the exact form

  P_s=(q,v,t,p,u).

This would require the turn (v,t,p) to be tight. But SC.3 contains (p,t,v) tight, its complete reverse. By R3, (v,t,p) is bad. Hence HHH is impossible.

In the TTT packet the anchors are the final two vertices p,u of C. Its puncture path omitting u has the exact form

  P_u=(s,q,t,v,p).

This would require (q,t,v) tight. But SC.3 contains (v,t,q) tight, its complete reverse. Hence TTT is impossible.

Therefore the short G1 overlap necessarily produces explicit R435 geometry among the puncture paths of the six singleton fibers P_x|B. The R435 event is source-visible, puncture-labelled, and common-literal-complement current.

### 6. Consequence and fence
The |M|=2 G1 overlap is no longer an isolated five-cycle exception. It is a six-vertex deletion-Hamiltonian critical universe U with:

1. every puncture U-x Hamiltonian;
2. six exact singleton rows P_x|B sharing one literal Hamilton complement B;
3. B+x non-Hamiltonian for all six x;
4. all six labels synchronously signing both reverse endpoint dimers of B; and
5. unavoidable explicit cross-fiber R435 geometry by the accepted source-anchored R961 theorem.

This is not yet a spanning two-cover, a same-support selected reversal, or an R561 witness. The next consumer must use the actual R435 comparison together with the common complement B and the synchronized puncture family. Generic R435 payment is deliberately not taken.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R887"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    },
    {
        "relation": "dependency",
        "revision_id": "R961"
    }
]
```
