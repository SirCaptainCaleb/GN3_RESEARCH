# The canonical R540 defect cut extinguishes both minimum-gap quiet G33 residues

**Workspace:** D17
**State:** established
**Key:** `g33-canonical-cut-xx-budget-extinguishes-quiet-residues`

**Summary:** For every one-hole R540-style LOW proposal of SV103129, choose the cut inside the sole bad turn on the spectator-side edge adjacent to the cut endpoint when the hole is spectator-side, and on the singleton-spoke edge when it is source-side. The resulting canonical defect forest J has one rail equal to the original spectator path B with exactly the opposite endpoint E deleted; its other two components partition X union {E}. Those five vertices lie in exactly two J-path components, so they contain exactly three selected edges, each either X-X or X-B. Therefore e_XX(J)+tau(J)=3. In either completely quiet minimum-gap residue of SV104738, tau(J)=2 and the old source has b_X(F)=2, so e_XX(J)=1 while e_XX(F)=4-b_X(F)=2. But SV104738 proves that every edge on which F and J differ in either quiet residue is one of the old/new seams and all such seams cross X|B; hence the selected X-X edge set is identical in F and J. Contradiction. Thus neither the one-transition seam-deletion residue nor the all-three-transition seam-tree residue can occur for an actual G33 R540 defect forest. Every direct packet therefore yields strict old-source descent or one of the bounded support-overlap/repeated-crossing/R435/local-R3 outputs of SV104738.

### 1. Canonical defect cut from the literal P616 construction
Retain SV103129 and the complete R540/P616 construction. Write the endpoint-favorable path as

  K=(k_0,k_1,k_2,k_3,k_4),

and let s be the omitted B-active source spoke, used as the singleton partner in the top-fiber R540 construction. Put

  B=(L=b_0,b_1,...,b_{m-1},R=b_m).

For every one-hole favorable position choose the following edge of the sole bad turn to cut.

LEFT cuts through L:
- If L=k_0, the sole hole is (s,k_1,k_2); cut s k_1. Then J=(s) | K[1,4] | B[0,m-1].
- If L=k_3, the sole hole is (k_2,L,b_1); cut k_2 L. Then J=K[0,2] | (s,k_4) | B[0,m-1].
- If L=k_4, the sole hole is (k_3,L,b_1); cut k_3 L. Then J=K[0,3] | (s) | B[0,m-1].

RIGHT cuts through R are the exact dual:
- If R=k_4, cut k_3 s in the source-side hole (k_2,k_3,s), giving J=K[0,3] | (s) | B[1,m].
- If R=k_1, cut R k_2 in the hole (b_{m-1},R,k_2), giving J=(k_0,s) | K[2,4] | B[1,m].
- If R=k_0, cut R k_1 in the hole (b_{m-1},R,k_1), giving J=(s) | K[1,4] | B[1,m].

Every displayed piece is tight because cutting creates no new turn. This is a proof-aware specialization of P616: only its literal words and complete seam ledger are used.

### 2. Exact X-edge budget
In the three left-cut rows, the pure spectator component is always

  B-E = B[0,m-1],  E=R.

In the three right-cut rows it is always

  B-E = B[1,m],  E=L.

The other two J-components partition exactly the five vertices

  X union {E}.

They are either a singleton plus a four-vertex path or a dimer plus a trimer. Hence they contain exactly three selected directed adjacencies in total. Since E is the only B-vertex among those five vertices, each of the three adjacencies is either X-X or X-B. Therefore, writing e_XX(J) for the number of selected J-edges with both endpoints in X,

  e_XX(J) + tau(J) = 3.                              (CB.1)

This identity is literal for the canonical defect forest and uses no minimum-gap assumption.

### 3. Apply the quiet-residue conclusions of SV104738
Suppose first that the ONE-TRANSITION SEAM-DELETION residue of SV104738 survives, or that the ALL-THREE-TRANSITION SEAM-TREE residue survives. In either completely quiet case SV104738 proves

  tau(F)=3,  tau(J)=2,
  b_X(F)=2,  d_F(v)=1,  b_B(F)=3.                    (CB.2)

By (CB.1),

  e_XX(J)=1.                                           (CB.3)

On the other hand the four vertices of X are partitioned into b_X(F)=2 maximal selected X-blocks in the old two-path forest F. Hence exactly

  e_XX(F)=4-b_X(F)=2.                                 (CB.4)

### 4. But quiet seam exchange cannot change an X-X edge
The synchronized-cell proof of SV104738 identifies every selected edge on which F and J differ with an old seam or a new seam between common cell words. In the one-transition seam-deletion residue the sole old seam crosses X|B. In the four-cell quiet residue both old seams and the new seam all cross X|B. Therefore in either quiet residue every selected X-X edge is common to F and J. In particular

  e_XX(F)=e_XX(J).                                    (CB.5)

Equations (CB.3)-(CB.5) give 2=1, contradiction.

Thus BOTH minimum-gap quiet residues of SV104738 are impossible for the actual canonical R540 defect forest supplied by G33.

### 5. Consequence
After the canonical cut, the direct G33 packet has only the nonquiet outcomes already isolated by SV104738:

1. a four-cell cyclic support-overlap nucleus;
2. a repeated-crossing seam pair;
3. an R435 adjacent reversal, reverse trimer, or proper cycle inside one cell;
4. a copy-competition or mixed-seam R3 trimer in a four-cell hybrid; or
5. an exact two-cover of the top fiber with transition count strictly below the old source F.

The fifth outcome is the desired strict old-source descent. The first four remain bounded physical consumers; this section does not relabel them as progress. Its gain is extinction of every completely quiet matching/seam-tree obstruction.

### 6. Scope
No R24, R5, payment, replay, finite search, or generic trimerized-R540 conclusion is used. The only accepted theorem mechanism imported is the literal P616 construction of R540, whose exact words and hole ledger are displayed above. The minimum-gap consequences are consumed exactly from SV104738.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R540"
    }
]
```
