# Return-square complement failure re-enters the minimum universal-source parent

**Workspace:** D17
**State:** working
**Key:** `return-square-complement-reentry`

**Summary:** For the actual return path Q=(M,r,u,p,y), put C=(Y-y)+Z and P_a=(M,r,u,p). Besides the known completion targets C or C+a, the return geometry forces C-b non-Hamiltonian, where b is the retained predecessor of y in Y. Outside explicit R435 geometry, any actual successor of y in either return-square cover lies in Z; a T1-successor z then also forces C-z non-Hamiltonian. If both C and C+a are non-Hamiltonian, the literal source H-a=P_a|(Y+Z) is universally crossed at y and accepted R942 applies at the same minimum offending size 2k. In its disconnected branch C itself cannot be the recurrent Hamilton support, and only P_a plus the unique side of the y-cut having at least k vertices can support a minimum-or-larger recurrence.


### 1. Retained return coordinates and the two completion targets
Retain the genuine stationary return-square survivor of `stationary-sandwich-return-square` in the orientation

  X=(M,r,a,u),
  Y=(N,s,b,y),
  P_a=(M,r,u,p),
  Q=(M,r,u,p,y).

Thus P_a is the actual TTT puncture path on X+p-a, Q=P_a-y is a literal Hamilton path after appending y, and the return square contains exact covers

  T_0 of H-{u,p} with selected trimer (r,a,y),
  T_1 of H-{r,a} with selected trimer (u,p,y).

Put

  C=(Y-y) union Z.

The complement of Q in H is C union {a}. Therefore either Hamiltonicity of C gives the exact singleton cover Q|C of H-a with rail sizes k+1 and 2k-1, or Hamiltonicity of C+a gives the spanning two-cover Q|(C+a). The present section studies the genuine failure branch in which both supports are non-Hamiltonian.

### 2. The retained Y terminal forces one named bad deletion of C
The first sandwich already gives the graph-intrinsic reverse terminal turn

  (p,y,b)

tight, while Y retains the terminal segment (s,b,y). Hence

  Q_b=(M,r,u,p,y,b)

is a literal Hamilton path of order k+2. Its complement in H-a is exactly

  C-b=(Y-{y,b}) union Z,

of order 2k-2. If C-b were Hamiltonian, Q_b|(C-b) would be an exact two-cover of H-a whose two rail sizes k+2 and 2k-2 are both strictly below the global offending threshold 2k (k>=4). This contradicts `subminimum-source-saturation`. Consequently every genuine return-square survivor satisfies

  C-b non-Hamiltonian.

No Hamilton order on C-b is transported or assumed.

### 3. Quiet actual continuations after y are Z-continuations
Suppose y is not terminal on its T_1 rail and let z_1 be its actual successor. Then T_1 certifies (p,y,z_1) tight.

Outside explicit R435 geometry, z_1 must lie in Z. Indeed z_1 cannot lie in Y-y: in the retained order Y every such Y-vertex precedes y, while the T_1 rail has y before z_1, giving reversed common-contact order. Nor can z_1 lie in M: the retained puncture order P_a=(M,r,u,p) places every M-contact before u, while the T_1 rail contains u,p,y before z_1. The labels r,a are deleted in T_1 and u,p,y are already used. Hence the only remaining class is Z.

The same argument applies to T_0. If y has actual successor z_0 on its T_0 rail, then outside explicit R435 geometry z_0 cannot lie in Y-y, since it follows y, and cannot lie in M, since the current rail has r,a,y before z_0 whereas retained X=(M,r,a,u) places every M-contact before r. Thus z_0 lies in Z.

This is an order-valued localization of the actual return continuations, not a claim that the whole suffix is one Z block.

### 4. A T1 Z-successor gives a second named bad deletion of C
In the quiet continuation branch above, let z=z_1 in Z. Since T_1 certifies (p,y,z), appending z to Q introduces no uncertified turn:

  Q_z=(M,r,u,p,y,z)

is a Hamilton path of order k+2. Its complement in H-a is exactly C-z, of order 2k-2. Therefore the same threshold argument gives

  C-z non-Hamiltonian.

Thus when y is internal on the T_1 return rail, complement failure carries at least two named non-Hamiltonian deletions, b in Y-y and the actual successor z in Z. If y is terminal on that rail, no successor is invented and this second conclusion is omitted.

### 5. Failure of C+a makes y a new minimum universal pivot
Now assume both Director completion targets fail:

  C is non-Hamiltonian,
  C+a is non-Hamiltonian.

The fixed point supplies the literal singleton source

  C_a : (Y+Z) | P_a

of H-a: Y+Z is Hamiltonian by accepted R953 and P_a is the actual Hamilton puncture path above. Its large rail has size 2k, exactly the globally minimum offending size.

We claim y is universally crossing on the Y+Z rail of this source. If not, apply the accepted quiet deleted-label substitution from R927/P999 to source C_a and deleted vertex y. The alternative augmented small support P_a+a=X+p is non-Hamiltonian by the R953 saturated-petal conclusion. Therefore quiet substitution must Hamiltonize

  (Y+Z-y)+a=C+a,

contrary to the present failure hypothesis. Hence y is universal relative to C_a.

Since (Y+Z)-y=C is also non-Hamiltonian, accepted R942 applies legally to this new minimum source. Retain any actual Hamilton source order

  Y+Z = L-y-R,

where L,R are nonempty; non-Hamiltonicity of C itself guarantees y is not a source-order endpoint.

### 6. The disconnected R942 recurrence has only one possible long side
Apply R942 to W=H-{a,y} with source atoms L,R,P_a. In a disconnected interaction cover, the recurrent offending rail is the Hamilton union of the two nonisolated classes.

It cannot be L union R, because L union R=C is non-Hamiltonian by hypothesis. Thus any recurrent Hamilton support is one of

  P_a union L,
  P_a union R.

Write l=|L| and r'=|R|. Since |Y+Z|=2k and y is one vertex,

  l+r'=2k-1.

The two candidate recurrence sizes are k+l and k+r'. A universal recurrence smaller than 2k is forbidden by global minimality. Hence a surviving recurrence through P_a union L requires l>=k, and one through P_a union R requires r'>=k. Because l+r'=2k-1, these conditions cannot both hold. Therefore for each retained source order at most one side of the y-cut can carry a minimum-or-larger disconnected recurrence; the other disconnected orientation is automatically consumed by the R931/R942 closure/uniform alternatives.

This does not eliminate the unique long-side recurrence, the connected rainbow-hinge/split-star branch, explicit R435 exits, or the possibility that y is terminal in T_1. It does show that failure of both complement completions is a new minimum universal-source problem with an already Hamiltonian opposite pivot extension Q=P_a+y, not a featureless return square.

Status: complete internal working deduction from accepted R927, R942 and R953 plus the working return-square and subminimum-threshold units. It is not canonically reviewed and does not close Arm A.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R927"
    },
    {
        "relation": "dependency",
        "revision_id": "R942"
    },
    {
        "relation": "dependency",
        "revision_id": "R953"
    },
    {
        "relation": "related",
        "revision_id": "R435"
    }
]
```
