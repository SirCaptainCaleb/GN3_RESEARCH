# Repeated stationary sandwiches collapse to a terminal reversal or a two-fiber return square

**Workspace:** D17
**State:** working
**Key:** `stationary-sandwich-return-square`

**Summary:** In the corrected stationary R696 SANDWICH cell, the selected sandwich simultaneously shifts an R542 packet onto one petal final-gap dimer and reverses the retained terminal edge of the opposite petal. Reapplying R696 to the shifted packet has a finite transition graph: one sandwich branch reaches a labelled P4 after at most three sandwich steps; the other has exactly one recurrent branch, consisting of exact covers of H-{u,p} and H-{r,a} containing r-a-y and u-p-y. In that return branch the latter trimer appends to the actual TTT puncture path on X+p-a, producing a Hamilton (k+1)-path. Hence, unless H already two-covers, y is forbidden as a Hamilton endpoint of the pair union Y+Z. This is a boundary-exposure restriction, not yet Arm-A closure. Corrected complement accounting: the two paths cover H-a; the endpoint exclusion follows from rail sizes k+1 and 2k-1 below the global threshold, not a direct spanning two-cover.


### Setup and the terminal four-cell
Retain the corrected SANDWICH shift of `stationary-r696-sandwich-shift` in the orientation

  (u,p,y)

tight, where u=u_X and y=u_Y. Write the retained X-order as

  X=(M,r,a,u),

with r=a_{k-2}, a=a_{k-1}. The source-anchored quiet TTT packet supplies the three actual puncture paths

  P_p=(M,r,a,u),
  P_u=(M,r,p,a),
  P_a=(M,r,u,p)

on X, X+p-u, and X+p-a respectively. Since Omega_X=X+p is non-Hamiltonian, appending the omitted terminal to these three paths forces

  (p,u,a), (u,a,p), (a,p,u)

all tight by R3. Two further Hamiltonizing proposals give

  (p,a,r), (u,p,r)

tight: if (r,a,p) were tight then (M,r,a,p,u) would Hamiltonize Omega_X using (a,p,u), and if (r,p,u) were tight then (M,r,p,u,a) would Hamiltonize Omega_X using (p,u,a).

The corrected first SANDWICH shift therefore gives the R542 packet

  S_0=(u,p), carrier C_0=(p,u,a), witnesses {r,y}, complementary singleton a.

### The same sandwich simultaneously reverses the opposite petal terminal edge
Write the retained Y-order as

  Y=(N,s,b,y),

where b=b_{k-1}. Because Y+p is non-Hamiltonian, the retained path Y cannot be extended by p, so (b,y,p) is bad and R3 gives

  (p,y,b)

tight. Together with the selected sandwich (u,p,y), this gives the literal P4

  (u,p,y,b).

In particular the graph-intrinsic state y->b is the exact reversal of the retained terminal state b->y of Y. Thus SANDWICH is already a two-petal object: it shifts an R542 packet on the X side and simultaneously exports an ancestral terminal-edge reversal on the Y side. The orientation (y,p,u) is the exact X/Y dual.

### First reapplication of R696
Apply accepted R696 to the shifted packet S_0 in an actual exact cover of H-{u,p}. END is immediately an R785 selected-state-reversal/P4 output and FREE is the accepted witness-selectable same-frame capture output. Suppose instead that this new packet is again SANDWICH. Since the complementary singleton is a and the witnesses are r,y, the selected trimer is exactly one of

  (y,a,r),   (r,a,y).

#### Branch A: (y,a,r)
The fixed turn (p,a,r) and the sandwich turn (y,a,r) give two same-polarity witnesses p,y on the tested dimer (a,r), which is the reverse initial boundary dimer of the retained carrier (r,a,u). Hence R542 applies with complementary singleton u.

Apply R696 to this packet. If END or FREE occurs, retain it. In SANDWICH the selected trimer is either

  (y,u,p) or (p,u,y).

The first immediately concatenates with (u,p,r) to the labelled P4

  (y,u,p,r).

For the second, (p,u,y) and the fixed turn (p,u,a) give two same-polarity witnesses y,a on the tested dimer (p,u), the reverse terminal boundary dimer of the retained carrier (r,u,p). Thus R542 applies again, now with complementary singleton r.

A third SANDWICH has selected trimer (a,r,y) or (y,r,a). These immediately concatenate respectively with the fixed turns (p,a,r) and (r,a,u), giving the labelled P4s

  (p,a,r,y),   (y,r,a,u).

Therefore Branch A cannot support an indefinitely repeated SANDWICH chain: after at most three consecutive SANDWICH applications it reaches a literal P4, unless END or FREE occurred earlier.

#### Branch B: (r,a,y)
The retained turn (r,a,u) and the sandwich turn (r,a,y) give two same-polarity witnesses u,y on the tested dimer (r,a), which is the reverse terminal boundary dimer of the fixed carrier (p,a,r). Hence R542 applies with complementary singleton p.

Apply R696 to this packet. Again END and FREE are retained outputs. In SANDWICH the selected trimer is either

  (y,p,u) or (u,p,y).

The first concatenates with (p,u,a) to the labelled P4

  (y,p,u,a).

The second is exactly the original sandwich trimer (u,p,y). Together with the fixed witness turn (u,p,r) and carrier (p,u,a), it recreates the original graph-intrinsic R542 packet S_0. However it occurs in a different exact deletion fiber. We have now retained simultaneously:

  T_0: an exact two-cover of H-{u,p} containing the selected trimer (r,a,y),
  T_1: an exact two-cover of H-{r,a} containing the selected trimer (u,p,y).

This is the unique SANDWICH recurrence. Repeating the same choices adds no new local trimer certificate; the recurrence is a two-fiber return square rather than an infinite packet descent.

### The return square forces a genuine (k+1)-path and pair-union endpoint exclusion
In the return branch, the actual TTT puncture path

  P_a=(M,r,u,p)

is Hamiltonian on X+p-a. The selected return trimer (u,p,y) shares its first two vertices with the terminal dimer of P_a, so appending y introduces no uncertified turn. Therefore

  Q=(M,r,u,p,y)

is a literal Hamilton path on

  (X+p-a) union {y},

which has order k+1.

The complementary vertex set in H is exactly

  {a} union (Y-y) union Z.

Correction to DR17.96-97: the earlier complement omitted a. If y were an endpoint of any Hamilton path on Y+Z, its deletion would certify (Y-y)+Z Hamiltonian. This path and Q partition H-a, NOT H. Their sizes are 2k-1 and k+1. Both are below the global offending threshold 2k for k>=4. Therefore subminimum-source-saturation contradicts this exact singleton cover. This use requires the stationary high-threshold hypothesis and the working threshold lemma; R953 alone does not supply the contradiction. Hence every genuine return-square survivor satisfies the graph-intrinsic terminal exclusion

  y is internal in every Hamilton path on Y+Z.

Thus the only recurrent SANDWICH cell has crossed from local packet geometry into pair-union boundary data. The next consumer should combine this new endpoint exclusion with the already retained source terminal/reversal geometry, rather than restart packet shifting or generic payment.

### Output and scope
Starting from the stationary selected sandwich (u,p,y), repeated use of accepted R696 on the exact shifted roles yields one of:

1. END, hence accepted R785 selected-state reversal or labelled P4;
2. FREE, hence witness-selectable same-frame capture;
3. a labelled P4 after finitely many SANDWICH shifts;
4. the unique two-fiber return square above, which produces an actual Hamilton (k+1)-path and forces y to be internal in every Hamilton order of Y+Z;
5. independently of the later branch, the first sandwich already gives the exact opposite-petal terminal-edge reversal y->b inside (u,p,y,b).

The dual orientation swaps X and Y. No claim is made that the labelled P4, FREE capture, terminal reversal, or endpoint exclusion alone closes H. No punctured pair-union is assumed Hamiltonian. This section is working exposition and does not alter the review status of the accepted exact D17 units.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R542"
    },
    {
        "relation": "dependency",
        "revision_id": "R696"
    },
    {
        "relation": "dependency",
        "revision_id": "R785"
    },
    {
        "relation": "dependency",
        "revision_id": "R953"
    },
    {
        "relation": "dependency",
        "revision_id": "R961"
    },
    {
        "relation": "related",
        "revision_id": "R435"
    },
    {
        "relation": "comparison",
        "revision_id": "R561"
    }
]
```
