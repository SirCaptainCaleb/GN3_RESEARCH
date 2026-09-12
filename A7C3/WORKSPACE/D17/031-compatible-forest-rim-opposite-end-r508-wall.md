# Two-sided all-break trapping forces fixed opposite-end R508 crossings and rim-universal boundary quartets

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-rim-opposite-end-r508-wall`

**Summary:** Let Q be a shortest ordinary comparison rim and U=(u0,...,ua) a complementary rail of order at least three. If every Q-to-U source merge over every cyclic break is DOUBLE and every U-to-Q terminal merge is also DOUBLE, then the source wall makes every u0-spoke LOW and gives (u1,u0,qi), while the terminal wall makes every ua-spoke HIGH and gives (qi,ua,u_{a-1}). For each source-side reverse P4 K_i=(u1,u0,qi,q_{i-1}), these walls extend K_i to a P5 using the fixed terminal singleton ua when |U|=3, or to the P6 (u1,u0,qi,q_{i-1},ua,u_{a-1}) using the fixed terminal dimer when |U|>=4. R508 therefore forces EVERY exact cover of H-K_i to cross that same opposite-end block, uniformly in i. The terminal-side family dually forces every restored cover to cross the fixed source singleton/dimer. Moreover when |U|>=4 the fixed boundary quartet {u1,u0,ua,u_{a-1}} plus any rim vertex qi is Hamiltonian; with two trapped complement rails U,V, each cross-rail source/terminal boundary quartet likewise Hamilton-extends by every rim vertex. These are partial universal one-extension four-cores and provide a direct convergence bridge to the Director small-core target.

### 1. Two-sided all-break wall on one complementary rail
Let H be a hypothetical smallest counterexample, let Q=(q_0,...,q_{r-1}) be a shortest ordinary comparison rim with r>=5, and retain an exact complement cover

  H-V(Q)=U|V,
  U=(u_0,u_1,...,u_a),

with |U|=a+1>=3.

Assume BOTH cyclic merge families are trapped:

(SOURCE WALL) for every cyclic break ending at q_i, the seed q_i->u_0 is DOUBLE;

(TERMINAL WALL) for every cyclic break beginning at q_i, the seed u_a->q_i is DOUBLE.

By SV24086, SOURCE WALL implies every spoke u_0q_i is LOW and

  (u_1,u_0,q_i) tight for every i.                       (RW.1)

TERMINAL WALL implies every spoke u_aq_i is HIGH and

  (q_i,u_a,u_{a-1}) tight for every i.                   (RW.2)

The LOW/HIGH relations also give, for every i,

  (u_0,q_i,q_{i-1}) tight,
  (q_i,q_{i-1},u_a) tight.                               (RW.3)

### 2. Every source-side reverse P4 absorbs the same opposite-end block
The source-side DOUBLE at break i gives

  K_i=(u_1,u_0,q_i,q_{i-1})                              (RW.4)

as a literal tight P4.

If |U|=3, then u_a=u_2 is outside K_i, and (RW.3) extends (RW.4) to the literal P5

  A_i=(u_1,u_0,q_i,q_{i-1},u_2).                         (RW.5)

If |U|>=4, then u_a,u_{a-1} are both outside K_i. Equations (RW.2)-(RW.3) extend K_i to the literal P6

  A_i=(u_1,u_0,q_i,q_{i-1},u_a,u_{a-1}).                 (RW.6)

Put D_i=V(K_i), and define the fixed opposite-end block

  S_U={u_a}                         if |U|=3,
  S_U={u_{a-1},u_a}                 if |U|>=4.            (RW.7)

Then A_i is a tight path whose support is exactly D_i union S_U. By R4 the complement H-D_i has an exact two-cover. Apply accepted R508 to deletion D_i, absorbable block S_U, absorber A_i, and ANY exact two-cover T of H-D_i. It follows that T selects an actual state with exactly one endpoint in S_U and the other in

  V(H) \ (D_i union S_U).                               (RW.8)

Crucially S_U is independent of i. Thus every restored representative at every source-side rim portal crosses the SAME physical terminal singleton/dimer of U.

If a closed exchange family contains the relevant rim-break states and is closed under every DOUBLE recompletion, all of these crossing-bearing successors remain inside that family. No arbitrary choice of crossing type or crossing position is used.

### 3. Exact terminal-side dual
For the terminal-side DOUBLE at the break beginning q_i, retain

  K_i^T=(q_{i+1},q_i,u_a,u_{a-1}).                       (RW.9)

If |U|=3, the fixed source block is {u_0}, and

  (u_0,q_{i+1},q_i,u_a,u_1)                              (RW.10)

is a tight P5 by LOW at q_{i+1}, HIGH at q_i, and (RW.2).

If |U|>=4, the fixed source block is {u_0,u_1}, and

  (u_1,u_0,q_{i+1},q_i,u_a,u_{a-1})                      (RW.11)

contains K_i^T together with that fixed source dimer and is tight by (RW.1)-(RW.3).

Therefore R508 dually forces every exact two-cover of H-V(K_i^T) to cross the same fixed source singleton {u_0} when |U|=3, or source dimer {u_0,u_1} when |U|>=4. Thus two-sided all-break trapping creates TWO synchronized rim-indexed universal-crossing families, one anchored at each end of U.

### 4. LOW and HIGH endpoints force a rim-wide P5 family
At a rim vertex q_i, let s_i=u_0q_i and t_i=u_aq_i. LOW gives s_i->e_i while HIGH gives e_i->t_i for either incident rim edge e_i. Since the globally shortest comparison cycle has length r>=5, there is no directed star triangle at q_i. Hence t_i->s_i is impossible, and therefore

  s_i -> t_i,

i.e.

  (u_0,q_i,u_a) tight for every i.                       (RW.12)

When |U|>=4, put

  S_U^4={u_1,u_0,u_a,u_{a-1}}.                           (RW.13)

Equations (RW.1),(RW.2),(RW.12) show that for every rim vertex q_i

  (u_1,u_0,q_i,u_a,u_{a-1})                              (RW.14)

is a Hamilton P5 on S_U^4 union {q_i}. Therefore the fixed four-set S_U^4 Hamilton-extends by EVERY vertex of the shortest rim.

This is not yet a universal one-extension four-set in the Director sense because vertices in the complementary rails outside S_U^4 have not been absorbed.

### 5. Cross-rail partial universal cores
Suppose the second complement rail is

  V=(v_0,...,v_b)

and the all-break Q-to-U source family is DOUBLE while the all-break V-to-Q terminal family is DOUBLE. Then u_0q_i is LOW for every i, v_bq_i is HIGH for every i, and the wall turns give

  (u_1,u_0,q_i) tight,
  (q_i,v_b,v_{b-1}) tight.                               (RW.15)

As in Section 4, absence of a shorter star triangle at q_i forces

  (u_0,q_i,v_b) tight.                                   (RW.16)

Hence the fixed cross-rail four-set

  S_{U,V}={u_1,u_0,v_b,v_{b-1}}                          (RW.17)

satisfies

  (u_1,u_0,q_i,v_b,v_{b-1})                              (RW.18)

for every i. Thus S_{U,V}+q_i is Hamiltonian for every rim vertex. The exact source/terminal dual and the U/V-swapped forms also hold.

In the special case where U and V are both dimers, S_{U,V}=V(H)\V(Q), so every exterior vertex of S_{U,V} lies on Q and S_{U,V} is already a universal one-extension four-set. In larger complements (RW.18) is a partial universal-core shell, not full absorption.

### 6. Status
This section answers a concrete part of G9's representative-selection problem. Under two-sided all-break trapping, the fresh DOUBLE recompletions do not merely contain an unspecified cross-component edge: R508 forces a crossing from one FIXED opposite-end physical block across every break and every exact restored cover. Simultaneously the same walls manufacture fixed four-sets with Hamilton extensions over the entire shortest rim.

The remaining global step is to spend closed exchange-class recurrence to expose the vertices outside these boundary quartets, or else show that failure to expose them yields an actual two-cover or a smaller holonomy. No claim is made that two-sided all-break trapping is automatic in a terminal class.
