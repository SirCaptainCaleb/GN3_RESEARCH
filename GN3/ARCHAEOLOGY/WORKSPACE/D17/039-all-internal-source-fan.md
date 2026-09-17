# All-internal source-trimer seam amplification with a clean R920/R3/R523 route

**Workspace:** D17
**State:** established
**Key:** `all-internal-source-fan`

**Summary:** In the all-internal branch of current usable R920, fix H=J|U|V with J=(a,x,c). R920 gives |U|,|V|>=3 and the four reverse x-shields. For the literal U-to-V seam, the two new turns h1=(u_{r-1},u_r,v_1) and h2=(u_r,v_1,v_2) cannot both be tight. Writing A=reverse(h1)=(v_1,u_r,u_{r-1}) and B=reverse(h2)=(v_2,v_1,u_r), R3 gives at least one winner. If exactly A wins, h2 is tight and shifting u_r from U to the front of V leaves U^- nontrivial because |U|>=3; the all-internal outer-pair condition directly forces the shifted shield (v_1,u_r,x), so R523 gives same-polarity collisions both on (u_r,u_{r-1}) and on (v_1,u_r). The B-only case is dual. If both A and B are tight, they concatenate to the P4 (v_2,v_1,u_r,u_{r-1}), whose terminal dimers carry the two R523 collisions from the original R920 shields. The V-to-U direction is symmetric. This reconstructs the live source-coupled seam amplification with only clean R920,R3,R523; the older R458 remint is retained only as historical context and is not a current dependency.

### 1. Clean current source state
Fix the all-internal branch of current usable R920 for a proper tight trimer

  J=(a,x,c),

and retain one literal source currentization

  H=J | U | V,
  U=(u_1,...,u_r),
  V=(v_1,...,v_s).

R920 proves directly, without R168, R5, or R24, that

  |U|,|V| >= 3.                                           (AI.1)

It also gives the four graph-intrinsic reverse shields

  (u_2,u_1,x),   (x,u_r,u_{r-1}),
  (v_2,v_1,x),   (x,v_s,v_{s-1})                         (AI.2)

as tight turns. The all-internal hypothesis is a statement about every exact two-cover of H-{a,c}: the middle vertex x is never exposed at a rail endpoint. It is therefore independent of which literal J|U|V currentization is presently displayed.

The live goal of this section is the source-coupled seam amplification formerly routed through R467. The optional historical pair-remint layer of R458 is not needed for that goal and is not used below.

### 2. Direct U-to-V seam test
Keep J as the third rail and test the literal concatenation U followed by V. The only new turns are

  h_1=(u_{r-1},u_r,v_1),
  h_2=(u_r,v_1,v_2).                                      (AI.3)

If both were tight, (U,V)|J would be a spanning two-cover of H, impossible. Define their exact reversals

  A=(v_1,u_r,u_{r-1}),
  B=(v_2,v_1,u_r).                                        (AI.4)

By boundary antisymmetry R3, at least one of A,B is tight. We retain the complete tight/bad status, not merely this disjunction.

### 3. A wins uniquely: shift the cut and recover the cross-seam shield
Assume A is tight and B is bad. R3 applied to B gives

  h_2=(u_r,v_1,v_2) tight.                                (AI.5)

Hence

  U^-=(u_1,...,u_{r-1}),
  V^+=(u_r,v_1,...,v_s)                                   (AI.6)

are literal tight paths and

  H=J | U^- | V^+                                         (AI.7)

is a second literal spanning three-cover. By (AI.1), |U^-|>=2, so no short-rail premise is being imported from R168.

Now test the direct endpoint attachment of x to the left end of V^+:

  (x,u_r,v_1).                                            (AI.8)

If it were tight, (x,V^+)|U^- would be a two-cover of H-{a,c} exposing x at a rail endpoint. H-{a,c} cannot be Hamiltonian, since a Hamilton path there together with the dimer (a,c) would two-cover H; thus every displayed two-cover of H-{a,c} is exact. This contradicts the retained all-internal R920 regime. Therefore (AI.8) is bad and R3 gives the shifted shield

  (v_1,u_r,x) tight.                                      (AI.9)

There are now two exact same-oriented same-polarity collision packets.

On D_1=(u_r,u_{r-1}), the original shield (x,u_r,u_{r-1}) and A=(v_1,u_r,u_{r-1}) are two HEAD certificates with distinct witnesses x and v_1. Current R523 gives the HH collision on D_1.

On D_2=(v_1,u_r), the shifted shield (v_1,u_r,x) and A=(v_1,u_r,u_{r-1}) are two TAIL certificates with distinct witnesses x and u_{r-1}. R523 gives the TT collision on D_2.

Thus the A-only branch yields the old residual terminal collision and the new cross-seam collision with the literal one-vertex shift retained as provenance.

### 4. B wins uniquely: exact dual shift
Assume A is bad and B is tight. Then R3 gives

  h_1=(u_{r-1},u_r,v_1) tight.                            (AI.10)

Put

  U^+=(u_1,...,u_r,v_1),
  V^-=(v_2,...,v_s).                                      (AI.11)

Since |V|>=3, |V^-|>=2, and H=J|U^+|V^- is a literal spanning three-cover. Test x at the terminal end of U^+ in its certified order:

  (u_r,v_1,x).                                            (AI.12)

If (AI.12) were tight, (U^+,x)|V^- would be an exact H-{a,c} two-cover exposing x, contradicting all-internality. Hence (AI.12) is bad, and R3 gives

  (x,v_1,u_r) tight.                                      (AI.13)

Now D_3=(v_2,v_1) has two TAIL certificates, the original shield (v_2,v_1,x) and B=(v_2,v_1,u_r), so R523 gives a TT collision with witnesses x,u_r.

The cross-seam dimer D_4=(v_1,u_r) has two HEAD certificates, the shifted shield (x,v_1,u_r) and B=(v_2,v_1,u_r), so R523 gives an HH collision with witnesses x,v_2.

This is the exact ordered dual of Section 3, again with the shifted representative retained only as an alternative source certificate.

### 5. Double winner: a literal P4 with two terminal collisions
If both A and B are tight, then their shared turn order concatenates literally to

  K=(v_2,v_1,u_r,u_{r-1}),                               (AI.15)

which is a tight P4. Its left terminal dimer (v_2,v_1) has TAIL witnesses x and u_r from (AI.2) and B. Its right terminal dimer (u_r,u_{r-1}) has HEAD witnesses x and v_1 from (AI.2) and A. R523 therefore gives one same-polarity collision on each terminal dimer of K.

### 6. Clean live conclusion and historical fence
Every U-to-V seam of an all-internal R920 source state therefore yields two role-linked same-polarity collision supports whose x-signed polarities are opposite:

- in a unique-winner branch, one old residual terminal dimer and one cross-seam dimer created by the exact one-vertex cut shift;
- in the double-winner branch, the two terminal dimers of the literal P4 (AI.15).

Exchanging U and V gives the symmetric directional statement.

This is exactly the current source-coupled geometric content needed from the historical R467 chain. Its clean premises are R920, R3, and R523. In particular it does not use R168, R359, R453, R455, R458, R467, R5, or R24.

Historically, R458 additionally reminted a realized collision through a terminal dimer of J into repeated balanced-pair ancestry. That is a distinct optional spend. The historical claim and its provenance remain preserved in the old theorem/SV records, but this current section does not require that remint and does not list it as a dependency.
