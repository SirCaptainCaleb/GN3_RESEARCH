# A bad singleton cannot hide behind R511: every good fixed-complement row forces a direct cut crossing

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-bad-singleton-direct-crossing-currentization`

**Summary:** Let V(H)=Omega disjoint_union Q with Q Hamiltonian and Omega non-Hamiltonian. Call d good when Omega-d is Hamiltonian and y bad when Omega-y is non-Hamiltonian. For every good d choose the literal exact singleton row C_d=P_d|Q. Compare any exact bad row C_y with C_d through the accepted exact codimension-one coherence unit. In the ordered defect y<-d, the source classes are S=Omega-{y,d} and Q. The defect is positive because an aligned C_y rail on Omega-y would contradict badness. The only non-direct positive species would be the R511 word S-block-d-T1|T2 (or reverse), but its contiguous S-block-d subpath is a Hamilton path on Omega-y, again contradicting badness. Therefore for EVERY good d, C_y contains an actual selected S|Q crossing avoiding y,d. If at least five good labels are available, one is internal in the two-path row C_y; puncturing that good d gives a literal three-cover of H-{y,d} retaining its direct Omega|Q crossing, while R429 supplies an exact two-cover of the same residue, hence a current 3-to-2 component-drop interface by R159. Thus every bad singleton in a five-good fixed-complement shell exports a source-visible good-bad current pair deletion; the theorem does not by itself claim Phi/epsilon descent.

### 1. Fixed-complement good and bad singleton labels
Let H be a hypothetical smallest Strong Level-(1) counterexample and suppose

  V(H)=Omega disjoint_union V(Q),

where Q is a literal Hamilton tight path and Omega is non-Hamiltonian. Call d in Omega GOOD when Omega-d is Hamiltonian and y in Omega BAD when Omega-y is non-Hamiltonian.

Fix a nonempty set D of good labels and one bad label y notin D. For every d in D choose an actual Hamilton path P_d on Omega-d. Then

  C_d = P_d | Q

is a literal two-path cover of H-d. It is exact: H-d cannot be Hamiltonian, because a Hamilton path on H-d together with singleton d would give a spanning cover of H by at most two tight paths.

Let C_y be ANY literal exact two-cover of H-y. No support synchronization for C_y is assumed. The purpose of this section is to show that C_y cannot use the quiet R511 bridge species against any good row C_d.

### 2. The ordered defect y<-d has fixed source classes
Fix d in D. Apply the accepted exact section `codimension-one-coherence` to the ordered comparison

  y <- d.

In the source row C_d, the rail P_d contains y and has support Omega-d. In the notation of that section, write

  V(P_d) = {y} union S,       S = Omega-{y,d},
  T_0 = V(Q).

Thus the coherent target partition for C_y would be

  (S union {d}) | T_0 = (Omega-y) | Q.                    (BS.1)

The overlap partitions cannot agree. Indeed the accepted codimension-one gluing calculation says that overlap agreement in a counterexample forces exactly the placement (BS.1); its first rail would be a literal Hamilton path on Omega-y, contradicting that y is bad. Equivalently, the ordered substitution defect kappa(y<-d) is positive.

The exact normal form of `codimension-one-coherence` now leaves only two species:

  DIRECT: C_y selects an actual S--Q adjacency;
  BRIDGE: C_y has the R511 word
          S-block -- d -- T_1 | T_2
          or its reversal, with T_1,T_2 nonempty and partitioning Q.

### 3. Badness kills the R511 bridge species
The BRIDGE species is impossible. In the displayed word, `S-block` is a tight path using all of S. Hence the contiguous prefix

  S-block -- d

(or the corresponding suffix in the reversed word) is a tight Hamilton path on

  S union {d} = Omega-y.

That contradicts the definition of y as bad.

Therefore the ordered defect y<-d is DIRECT for every good d. Concretely:

> For every d in D, the fixed bad row C_y contains a selected physical adjacency e_d with one endpoint in Omega-{y,d} and the other endpoint in Q. In particular e_d avoids both deleted labels y,d.

This is simultaneous source-row information. The same C_y is retained for all d; only the guaranteed crossing e_d may vary with d. No paid descendants are being identified.

### 4. Five good labels force a current good-bad pair deletion
Assume now |D|>=5. The exact two-cover C_y has exactly four physical rail endpoints. Hence at least one good label

  d_* in D

is internal on its C_y rail.

Puncture d_* from that SAME bad row. Because d_* is internal, its rail splits into two nonempty tight intervals and the other C_y rail remains nonempty. Thus

  R_{y,d_*} = C_y-d_*

is a literal three-cover of H-{y,d_*}. The DIRECT crossing e_{d_*} from Section 3 avoids d_* and therefore survives literally as a selected Omega|Q cut state in this three-cover.

Accepted pair-deletion rigidity R429 supplies a literal exact two-cover

  F_{y,d_*}

of H-{y,d_*}. Since three source components are recompleted by two paths, some selected state of F_{y,d_*} crosses two components of R_{y,d_*}; accepted R159 records the corresponding graph-intrinsic component-drop pair. Retain BOTH pieces of current information:

1. the actual source three-cover R_{y,d_*}, including its surviving selected Omega|Q crossing e_{d_*};
2. the actual exact recompletion F_{y,d_*} and a selected component-crossing state.

Hence every bad singleton in a five-good fixed-complement shell emits a CURRENT good-bad pair-deletion interface on a pair {y,d_*}, with the original mixed singleton row still visible one deletion higher.

### 5. Consequences for the G24 kernel
In the coherent G24 shell the five distinguished P5 roots provide exactly such a set D whenever all five punctures Omega-d are Hamiltonian. Therefore any bad y in Omega-D cannot remain a purely support-level exception: one and the same bad singleton row is DIRECT against every good fixed-complement row and currentizes with at least one good root on H-{y,d_*}.

A useful conditional corollary is immediate. In any reconstruction subfamily whose retained current pair-deletion interfaces touching D are all required to have both deleted labels in D, no bad label y outside D can occur. Under that additional no-exterior-current condition, every label of Omega outside D is good, so the partial five-puncture shell promotes to a full deletion-Hamiltonian fixed-complement block.

This conditional statement must not be read backwards: G24 explicitly allows exterior current portals, and the existence of R_{y,d_*}|F_{y,d_*} alone is not strict Phi or epsilon_* descent. The gain is that the bad-singleton branch has no R511/seam-free hiding place. Its obstruction is forced into an actual mixed source row plus a current good-bad pair recompletion, exactly the currency required by BAD-SINGLETON / COMMON-COMPLEMENT EXTINCTION.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    }
]
```