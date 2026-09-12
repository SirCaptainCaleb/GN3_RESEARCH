# An all-zero source-label row forces fragmentation of the Hamilton deletion support

**Workspace:** D17
**State:** established
**Key:** `three-petal-allzero-fragmentation`

**Summary:** Conditional all-zero fragmentation theorem. Retain disjoint supports S,C in H-z with S Hamiltonian, C non-Hamiltonian deletion-Hamiltonian, and assume that for every c in C every exact H-z two-cover selects an S|(C-c) adjacency. Then no exact H-z cover can keep S in one maximal block. Hence b_S>=2, b_C>=2 and tau>=2. At tau=2 one has b_S=b_C=2 and exactly the three block forms S-C|S-C, S-C-S|C, or C-S-C|S. The two crossing C-endpoints are distinct; consequently the middle C-block in S-C-S|C is nontrivial. In the R953 Hamilton-deletion all-zero row these hypotheses are supplied by the source-label universal-crossing family.

Retain the Hamilton-deletion branch and notation of `three-petal-hamilton-deletion-row`: X=B union Z, C=L union {p}, z in X, S=X-{z} Hamiltonian, C non-Hamiltonian deletion-Hamiltonian, and the source-label exchange row E(y)=1 iff S+y is Hamiltonian. Assume the ALL-ZERO branch E(y)=0 for every y in C. Equivalently z is universally crossing relative to every literal singleton source

  H-y : X | (C-y),    y in C.

### 1. No exact H-z cover can keep S as one maximal block
Let T be any literal exact two-cover of H-z and suppose its restriction to S has exactly one maximal S-block U. By the all-zero row, T contains an S|C transition; indeed DR17.63 already shows at least two distinct C labels occur among the crossing endpoints.

Choose any selected transition at one boundary of U. In one orientation it is c-U, where c in C is the final vertex of the adjacent C-block; in the other it is U-c. Because U contains every vertex of S, the contiguous subpath

  c-U    or    U-c

is an actual Hamilton tight path on S union {c}. Since C is deletion-Hamiltonian, choose an arbitrary actual Hamilton path K_c on C-{c}. The two displayed supports are disjoint and partition V(H)-{z}, so

  (c-U) | K_c    or    (U-c) | K_c

is a literal exact two-cover of H-z.

But relative to the singleton source

  H-c : X | (C-c),

z is universally crossing. Its X-side deletion is S, so every exact H-z cover must select an adjacency between S and C-c. The reconstructed cover has no such adjacency: its only mixed rail contains S and the single C-label c, while K_c is pure C-c. Contradiction.

Therefore every exact H-z two-cover satisfies

  b_S(T) >= 2.

This is a cover-valued fragmentation theorem. It is stronger than the scalar transition lower bound.

### 2. Minimum transition two has an exact four-block normal form
For any exact H-z cover T let b_S,b_C be the numbers of maximal S- and C-blocks and tau the number of selected S|C transitions. Splitting the two rails at all cross transitions gives

  b_S+b_C=2+tau.

Because S is Hamiltonian, b_S>=1 a priori; because C is non-Hamiltonian but two-coverable, b_C>=2. Section 1 strengthens the first inequality to b_S>=2. Hence

  tau >= 2.

If tau=2, equality forces

  b_S=b_C=2.

Contracting maximal monochromatic blocks, the two-component path forest has four vertices and two cross-color edges. Up to exchanging the two rails and reading the displayed word in its actual orientation, exactly three block types occur:

  S-C | S-C,
  S-C-S | C,
  C-S-C | S.

The all-zero row also forces the two selected transitions to have distinct physical C endpoints, by DR17.63. Therefore in the S-C-S|C type the middle C-block cannot be a singleton: its two boundary transitions would otherwise both be incident with the same C-label. In the other two types the distinctness is automatic when the transition endpoints lie in disjoint C-blocks.

### 3. Retained next interface
Thus the all-zero Hamilton-deletion branch cannot terminate in a generic `tau>=2` statement. At transition minimum two it is already a two-cut fragmentation problem in which a Hamilton support S is split into exactly two current blocks and the two cuts hit distinct physical labels of the deletion-Hamiltonian block C. For larger tau the Hamilton support remains fragmented in every representative.

Any useful next consumer must preserve the literal Hamilton order of S, the two current S-blocks, both C crossing labels, and the Hamilton puncture paths C-c for those labels. A one-sided trim, anonymous P4, or bare balanced-pair birth discards the feature proved here.

Status: complete internal symbolic argument from the all-zero row and deletion-Hamiltonicity of C. No spanning two-cover is claimed.
