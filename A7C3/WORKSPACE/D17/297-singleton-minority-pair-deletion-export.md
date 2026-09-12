# A singleton-minority defect fan exports at least two current pair-deletion portals

**Workspace:** D17
**State:** established
**Key:** `singleton-minority-pair-deletion-export`

**Summary:** In a fixed-witness singleton disagreement fan whose minority class is one deletion label a, the unique minority cover C_a has at least two majority labels b as physical rail endpoints. An R511 bridge a<-b requires b internal, so each such endpoint defect is forced into the direct source-rail crossing species. Trimming b from C_a keeps an exact two-cover of H-{a,b} and preserves that selected crossing. Trimming a from C_b gives either another exact two-cover with a genuinely different support partition or a literal three-cover crossed by the first two-cover. Thus every singleton-minority K residue exports at least two distinct current pair-deletion disagreement/component-drop portals sharing the deleted label a and the same parent singleton row. This removes the singleton-minority case as a purely singleton-level rank-flat sink, without claiming the exported pair-deletion portals close.

### 1. Singleton-minority fixed-witness fan
Retain a hypothetical smallest counterexample H and a chosen singleton-deletion cover family as in `singleton-disagreement-fan`. Fix a physical witness pair {u,v}. Let the deletion labels outside {u,v} split into the two witness-status classes A,B, and assume the minority is the singleton

  A={a},    B=V(H)-{u,v,a}.

Thus |B|=n-3. For every b in B the support partitions sigma_a and sigma_b disagree on their common residue, so both ordered substitution defects are positive. We focus on a<-b.

Write C_a for the chosen exact two-nonempty-path cover of H-a. By the elementary singleton-rail fence in `codimension-one-coherence`, both rails of C_a have order at least two. Hence C_a has exactly four physical rail endpoints and n-5 internal vertices. The vertex set of C_a is exactly B union {u,v}. At most two of its four endpoints can be u,v. Therefore at least two distinct labels

  b_1,b_2 in B

are physical endpoints of C_a.

### 2. Endpoint majority labels cannot lie in the R511 bridge species
Fix such an endpoint b in B. Apply the exact positive-defect classification of `codimension-one-coherence` to the ordered defect a<-b. In its notation the source cover C_b has rails

  Q | T,    V(Q)={a} union S,    V(T)=T_0.

A positive defect has exactly two source species. Either C_a selects an actual S--T_0 adjacency, or, if no such adjacency exists, C_a has the unique nonclosing R511 word

  S-block -- b -- T_1  |  T_2

(or its reversal), with T_1,T_2 nonempty. In the R511 word the physical vertex b is internal: it has one selected neighbor in the S-block and one selected neighbor in T_1. Our b is an endpoint of C_a, so this second species is impossible. Consequently there is a selected directed state

  e_b=x_b -> y_b

in C_a with x_b in S and y_b in T_0, or the reverse orientation. In particular e_b avoids both deleted labels a,b.

Thus every majority label b that is an endpoint of the one minority row forces the DIRECT source-rail-crossing species. Since there are at least two such endpoints, the singleton-minority fan contains at least two distinct endpoint-rooted direct defects. The selected crossing states e_b need not be the same physical edge.

### 3. Trimming the endpoint currentizes the crossing one deletion lower
Delete b from C_a. Because b is a rail endpoint and both C_a rails were nontrivial, the b-containing rail remains nonempty and the other rail is untouched. Hence

  T_b := C_a-b

is a literal two-nonempty-path cover of H-{a,b}. Accepted pair-deletion rigidity R429 makes pc(H-{a,b})=2, so T_b is exact. The selected crossing e_b survives literally in T_b because e_b avoids b.

Now delete a from the source cover C_b. There are two cases.

**(ENDPOINT-a.)** If a is an endpoint of its C_b rail Q, then C_b-a is another literal two-nonempty-path cover of H-{a,b}, hence exact by R429. Its support partition is S|T_0. The surviving state e_b in T_b has one endpoint in S and one in T_0, so T_b has a different support partition. Thus H-{a,b} carries an actual same-residue exact partition disagreement with a named selected crossing e_b.

**(INTERNAL-a.)** If a is internal in Q, then C_b-a is the literal three-component cover obtained from the two nonempty fragments of Q-a together with T. Since e_b joins S to T_0, its endpoints lie in two distinct components of this three-cover. The exact two-cover T_b selects e_b. Hence H-{a,b} carries a literal 3-to-2 component drop with the named smaller-cover crossing e_b.

So every endpoint majority label b exports, on the exact pair-deletion residue H-{a,b}, either current exact partition disagreement or current component drop. No payment or historical currentization is needed to obtain this pair-deletion portal: it is produced by literal endpoint trimming of the original singleton covers.

### 4. Family-level consequence
There are at least two distinct endpoint labels b_1,b_2 in B. Therefore the singleton-minority fixed-witness residue exports at least two distinct exact pair-deletion fibers

  H-{a,b_1},   H-{a,b_2}

sharing the deleted label a and sharing the same parent minority cover C_a, each with a retained physical selected crossing e_{b_i} and with one of the two exact source types above.

This is the appropriate G22 interpretation of the singleton-minority floor in the neutral K-secondary descent. It is not a terminal singleton-level sink: the obstruction necessarily re-enters current pair-deletion disagreement/component-drop geometry in at least two directions. The theorem does not claim that the two pair-deletion portals have one common crossing, that their later paid descendants coexist, or that either portal by itself lowers global Phi/K. Its gain is a provenance-preserving current export before any payment reset.