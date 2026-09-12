# The oversized one-p skeleton has a shared-hole source-reversal/R542 trichotomy

**Workspace:** D17
**State:** established
**Key:** `stationary-one-p-oversized-shared-hole`

**Summary:** In the unique direct quiet skeleton B-V-Z | U-p, let v be the first V vertex, c the final U vertex before p, and K_B=(b_1,...,b_{k-2},p,b_{k-1}). The common hole h=(p,b_{k-1},v) controls two subthreshold singleton-cover proposals. If h is bad, its reverse and the Y-terminal puncture turn give an R542 packet on (b_{k-1},p). If h is tight, K_B-V is Hamiltonian; for each omitted seam terminal u in {u_X,u_Y}, U-u-Z can fail only at (d,c,u) and (c,u,z). A bad right hole is an exact reversal of the historical source state u-z. If neither right hole is bad, both left holes must be bad and their reversals give a second R542 packet on (c,d). Thus the oversized skeleton has no featureless survivor: it yields a forbidden subthreshold cover, a source-edge reversal, or an ancestry-labelled R542 packet.


### Setup
Retain the unique quiet direct-repair skeleton from `stationary-one-p-zb-elimination`:

  B -> V -> Z  |  U -> p.

Here U and V partition A, with U nonempty because p has its unique selected A-incidence. Write

  s=|U|,  t=|V|,  s+t=k-1,

so s,t>=1. Let

  v=v_1

be the first vertex of the actual V block and let c be the final U vertex immediately before p. If s>=2, let d be the predecessor of c in the actual U order. Retain the quiet Y-terminal puncture

  K_B=(b_1,...,b_{k-2},p,b_{k-1})

and its forced reverse turn

  (u_Y,b_{k-1},p)

tight.

The current B->V seam certifies

  (b_{k-2},b_{k-1},v)

and, when t>=2, the next junction turn from b_{k-1} into the second V vertex. The stationary source orders also certify

  (u_X,z,z_2),  (u_Y,z,z_2)

with the obvious omission of z_2 only in a vacuous endpoint degeneration that does not occur here since k>=4.

### 1. One common B-entry hole
Consider

  P=(K_B followed by V).

Every turn is certified except possibly

  h=(p,b_{k-1},v).

Indeed K_B is tight, and after the first B->V junction turn all remaining turns are inherited from the actual current B-V block segment.

If h is bad, boundary antisymmetry gives

  (v,b_{k-1},p)

tight. Together with the terminal-puncture turn

  (u_Y,b_{k-1},p)

this gives two distinct same-polarity witnesses v,u_Y on the tested reverse terminal dimer

  S_B=(b_{k-1},p)

of the tight final-gap trimer

  K_B^tail=(b_{k-2},p,b_{k-1}).

Both witnesses lie outside K_B^tail. Hence accepted R542 applies, with complementary singleton b_{k-2}. Thus a surviving direct reconstruction may assume h tight.

### 2. Two synchronized subthreshold proposals when h is tight
Assume h tight, so P is Hamiltonian on B union {p} union V. For each

  q in {u_X,u_Y},

form the second literal proposal

  Q_q=(U,q,Z)

in the singleton fiber omitting the other seam terminal. Every old U turn and every Z turn is retained, and (q,z,z_2) is historical. Therefore the complete uncertified-turn set of Q_q is

  l_q=(d,c,q)   if s>=2,
  r_q=(c,q,z).

No other turn is new.

If all existing holes for one q were tight, then P|Q_q would be an exact singleton-deletion two-cover. Its rail orders are

  |P| = k+t,
  |Q_q| = k+s+1 = 2k-t.

Because 1<=t<=k-2, both orders are strictly below a=2k, contradicting `subminimum-source-saturation`. Consequently for each q at least one of its displayed holes is bad.

### 3. A bad right hole is an exact historical source-state reversal
Suppose r_q=(c,q,z) is bad. Then

  (z,q,c)

is tight. The historical stationary source containing q has the selected state q->z. The tight three-vertex path (z,q,c) contains the exact reversed state z->q. Comparing it with that historical source by accepted R435 therefore lands in the literal adjacent-state reversal branch: z and q are consecutive contacts in reverse source order.

Thus a bad right hole is not an anonymous seam certificate. It exports the exact reversed historical boundary state

  z -> q

for q=u_X or q=u_Y, with the source identity retained.

### 4. If neither historical source state reverses, the two left failures give R542
Assume neither r_{u_X} nor r_{u_Y} is bad. Then both are tight. Since each P|Q_q is nevertheless forbidden, the left hole l_q must exist and must be bad for both q. In particular s>=2. Boundary antisymmetry gives

  (u_X,c,d),
  (u_Y,c,d)

both tight.

But the final current U-p turn certifies the tight trimer

  K_U=(d,c,p).

Its reverse left boundary dimer is

  S_U=(c,d),

and u_X,u_Y are two distinct same-polarity witnesses on exactly this tested orientation. Accepted R542 therefore applies, now with complementary singleton p.

### Output
The exact oversized skeleton

  B -> V -> Z | U -> p

has no featureless direct survivor. One of the following holds:

1. the common B-entry hole is bad, giving the R542 packet (K_B^tail,S_B; witnesses v,u_Y);
2. after the common hole succeeds, one of the two U-to-seam right holes is bad, giving the exact historical source-state reversal z->u_X or z->u_Y;
3. neither source state reverses, in which case both left holes are bad and give the R542 packet (K_U,S_U; witnesses u_X,u_Y);
4. otherwise one of the displayed subthreshold singleton covers exists, contradicting the global threshold.

The two R542 outputs are ancestry-labelled and may be fed directly to accepted R696 before any generic payment: the first has complementary singleton b_{k-2}; the second has complementary singleton p. This section does not claim that R696 FREE/SANDWICH, a source-state reversal, or an R542 packet alone closes H.

Status: complete internal deduction, unreviewed exposition. Together with the preceding one-p sections it exhausts the direct quiet c=2,d=1,tau_Z=1 block topologies, but not their exported R435/R542 alternatives and not the separate exceptional fragmented-Z, tau_Z=2, c>2, or nonstationary recurrence branches.

