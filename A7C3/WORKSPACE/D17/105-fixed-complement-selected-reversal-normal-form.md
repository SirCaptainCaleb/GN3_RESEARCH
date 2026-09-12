# A fixed-complement selected reversal has monotone boundary transport or exact wrap shields

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-selected-reversal-normal-form`

**Summary:** Let two exact covers of one residue have the same support partition and the same literal Hamilton complement, while their active Hamilton orders select one physical dimer in opposite directions. Repeatedly use only the cyclic rotation that moves that same reversed dimer toward the R561 boundary. Every successful rotation preserves support, complement, and the named discrepancy while decreasing an explicit boundary-distance by one; every failed step gives the exact R548 reverse-wrap shield. Thus the process terminates either at a fixed-support R561 witness or at a pair in which every still-positive boundary distance is blocked by a named reverse-wrap trimer. In a singleton row the successful rotations have exact one-edge K-weight changes, giving either strict row improvement, neutral secondary distance descent, or a strict positive wrap-weight barrier at a lexicographic minimum. This consumes the selected-edge-reversal branch of same-support R435 without exporting a new anonymous order conflict.

### Setup and the named discrepancy
Let a proper residue have two literal exact covers

  P | B,     Q | B,

with the SAME unordered support partition X|V(B) and the SAME literal Hamilton complement B. Write

  P=(p_0,...,p_r),     Q=(q_0,...,q_r)

for Hamilton tight paths on the common support X. Suppose one physical dimer {u,v} is selected in opposite directions: for some a,b,

  (p_a,p_{a+1})=(u,v),     (q_b,q_{b+1})=(v,u).

Define the boundary distance of this labelled reversal by

  delta(P,Q;u,v)=a+(r-b-1).

Thus delta=0 exactly when P begins with (u,v) and Q ends with (v,u), the fixed-support configuration required by R561. The point of the following transport is that the physical discrepancy {u,v}, its two orientations, the support X, and the complement B never change.

### Left transport on P
Assume a>0. The tail rotation

  P_T=(p_1,...,p_r,p_0)

has only one new turn, beta_P=(p_{r-1},p_r,p_0). By accepted R548/P624, if beta_P is tight then P_T is a Hamilton tight path on X. Because a>0, the selected state (u,v) is not cut by the rotation; it remains selected, now one position closer to the left boundary. Hence

  delta(P_T,Q;u,v)=delta(P,Q;u,v)-1.

If beta_P is bad, boundary antisymmetry gives the exact reverse-wrap shield

  (p_0,p_r,p_{r-1})

tight. This shield is attached to the current P representative while the original directed state (u,v) remains selected. No new anonymous R435 event is introduced.

### Right transport on Q
Assume b<r-1. The head rotation

  Q_H=(q_r,q_0,...,q_{r-1})

has only one new turn, alpha_Q=(q_r,q_0,q_1). If alpha_Q is tight, R548 makes Q_H Hamiltonian on X. Since b<r-1, the selected reverse state (v,u) is not cut; it moves one position toward the right boundary, so

  delta(P,Q_H;u,v)=delta(P,Q;u,v)-1.

If alpha_Q is bad, R3 gives the exact reverse-wrap shield

  (q_1,q_0,q_r)

tight, again with the same physical reversal retained in Q.

### Finite normal form and R561
Apply the two directed rotations repeatedly whenever their relevant coordinate is positive and the required wrap seam is tight. Every successful step decreases the nonnegative integer delta by exactly one. Therefore the process terminates. In the terminal pair, independently on each side, either the corresponding distance coordinate is zero or its required wrap seam is bad and the displayed reverse-wrap shield is present.

If both coordinates reach zero, P starts (u,v) and Q ends (v,u). Accepted R561/P652 therefore says that EVERY exterior vertex Hamilton-extends X. In a singleton-deletion cover H-d=X|B this immediately gives a spanning two-cover of H by extending X with d and retaining B. In a deeper common residue, retain the fixed-support R561 absorber for the appropriate restoration step; no stronger automatic closure is asserted.

Thus a selected-edge reversal has an exact discrepancy-preserving normal form:

  R561 boundary reversal,
  or one/two named reverse-wrap shields at the still-positive ends,
  with every preceding successful step a strict decrease of delta.

### Exact singleton-row energy specialization
In the singleton-fiber setting of `singleton-row-weighted-recombination`, hold the support family fixed and let w_x(e) be the accepted selected-edge row weight for the deletion fiber x. A successful left tail rotation deletes only p_0p_1 and adds only p_rp_0, so its exact outgoing-row change is

  Delta R_x = w_x(p_rp_0)-w_x(p_0p_1).

A successful right head rotation deletes only q_{r-1}q_r and adds only q_rq_0, so

  Delta R_x = w_x(q_rq_0)-w_x(q_{r-1}q_r).

Consequently a successful transport step has one of three declared effects. If the displayed difference is negative and the current row is selected, it is a strict same-support K improvement. If the difference is zero, it is K-neutral but strictly decreases the well-founded discrepancy coordinate delta. If the difference is positive, the step records an exact positive wrap-energy barrier rather than pretending that the rotation is a K descent. In particular, at a representative chosen lexicographically to minimize row weight and then the relevant boundary distance among Hamilton orders retaining the named orientation, every positive boundary distance forces either the corresponding reverse-wrap shield or the strict inequality

  w_x(p_rp_0)>w_x(p_0p_1)

on the P side, respectively

  w_x(q_rq_0)>w_x(q_{r-1}q_r)

on the Q side.

### Interface with R435 and scope
For a same-support R435 comparison, every P-contact of Q is a vertex, so an adjacent reverse-order ear is literally one Q-selected state v_i v_{i-1}, the reversal of the P-selected state v_{i-1}v_i. The present lemma therefore consumes the SELECTED-EDGE-REVERSAL branch immediately, preserving the same physical dimer throughout.

This section deliberately does not claim that an R435 reverse trimer or proper tight cycle is already a Hamilton-order selected reversal. Those two branches remain separate. It also does not call an isolated wrap shield R561 or closure. The value of the normal form is currency retention: fixed support, fixed complement, the original reversed dimer, and every endpoint-role change caused by the actual rotations remain explicit.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R548"
    },
    {
        "relation": "dependency",
        "revision_id": "R561"
    }
]
```
