# A hub-opposite coherent wheel either currentizes outside the P5 or collapses the critical block to order at most seven

**Workspace:** D17
**State:** established
**Key:** `portal-wheel-hub-opposite-outside-current-or-order7-collapse`

**Summary:** In the support-coherent fixed-complement cone shell of SV62430, take the rigid orientation x in the Hamilton independent class Q. Then all five P5 roots lie in the non-Hamiltonian block Omega and every Omega-d, d in K, is Hamiltonian. Pair each actual Hamilton puncture path P_d on Omega-d with the same literal Hamilton complement Q, giving an exact singleton row H-d=P_d|Q. Any K-d versus Omega-K transition in P_d is a selected root/exterior crossing. If its exterior endpoint y is internal, puncturing y gives a literal three-cover of H-{d,y}, while R429 gives an exact two-cover, so R159 produces a current same-pair component-drop portal; SV63332 also retains the alternative paid floor {d,y}. If no such exterior currentization occurs for any d, then in every P_d every Omega-K block must be a singleton path-end block. Therefore |Omega-K|<=2 and |Omega|<=7. If |Omega-K|=1, Omega is already deletion-Hamiltonian. If |Omega-K|=2={y,z}, then every P_d has endpoints exactly y,z and K-d is one contiguous four-vertex interior block. Thus the hub-opposite coherent wheel is either currently nonflat outside K or collapses to a six/seven-vertex critical residue with a rigid two-ended puncture necklace. This is a genuine kernel-size reduction, not full extinction of the order-seven residue.

### 1. Input: the hub lies in the Hamilton independent class
Retain the SUPPORT-COHERENT fixed-complement cone shell of SV62430. Thus

  V(H)=Omega disjoint_union Q,

where Q is a literal Hamilton block, Omega is non-Hamiltonian, K is the retained Hamilton P5, and the common wheel hub x lies in Q. Because Q is the independent color of the wheel cone and every spoke x-d is a cone edge, all five roots satisfy

  V(K) subseteq Omega.                                      (OC.1)

Moreover every spoke exact cover H-{x,d} has rails (Omega-d)|(Q-x), so

  Omega-d is Hamiltonian for every d in V(K).               (OC.2)

Since Q itself is Hamiltonian, for every d choose and retain an actual Hamilton puncture path P_d on Omega-d and form the literal exact singleton-deletion row

  T_d = P_d | Q   of H-d.                                  (OC.3)

Exactness follows from smallest-counterexample pc(H-d)=2: a Hamilton H-d would together with singleton d give an at-most-two cover of H after the usual minimal-counterexample reduction, while (OC.3) already supplies two nonempty rails. For the argument below only the literal two-path row is used.

Put

  E = Omega - V(K).                                        (OC.4)

E is nonempty, because Omega itself is non-Hamiltonian while K is a Hamilton path.

### 2. Every K/E transition is a wheel root crossing in one common-complement row
Fix d in K. The carrier K consists exactly of deleted vertex d plus the four-vertex block K-d in H-d. Accepted R508 therefore forces every literal two-cover T_d to contain a selected crossing between K-d and H-K. In the specific row P_d|Q, a selected adjacency having one endpoint in K-d lies on P_d, not on the disjoint Q rail. Hence its other endpoint cannot lie in Q and must lie in E. Thus P_d contains a selected adjacency

  k y,   k in K-{d}, y in E.                              (OC.5)

More generally, EVERY color change along the literal word P_d between K-d and E is itself a selected physical K/E crossing in this same source row.

By SV63332/R527 the same crossing (OC.5) may be actualized with either physical endpoint designated as the capture anchor. In particular the exterior endpoint y yields, as an alternative legal continuation, either closure or the ancestry-bearing floor {d,y}. Retain this source-labelled exterior-capture option, but do not count the paid floor itself as progress.

### 3. An internal exterior boundary vertex is immediately current on its own pair deletion
Suppose some K/E transition in P_d has exterior endpoint y in E which is INTERNAL on the path P_d. Puncture y from the SAME source row T_d. Since y is internal, P_d-y splits into two nonempty tight intervals, while the common complement Q survives unchanged. Therefore

  (P_d-y) | Q

is a literal three-cover of H-{d,y}. Accepted R429 supplies an exact two-cover F_{d,y} of the same pair-deletion residue. Hence accepted R159 applies to this literal 3-to-2 component drop; retain the actual three-cover, F_{d,y}, and a selected F_{d,y}-state crossing two source components as CURRENT same-pair geometry.                                         (OC.6)

This is exactly the exterior side of the forced-current fork SV63332, now inside the coherent fixed-complement shell.

Thus either (OC.6) occurs for some d in K and y in E, or every K/E transition in every chosen P_d has its E-endpoint at a PHYSICAL ENDPOINT of P_d. Assume the latter residue from now on.

### 4. Quiet exterior transitions force at most two exterior vertices
Fix d and read the Hamilton word P_d, coloring its vertices by

  K-color = K-{d},
  E-color = E.

Both colors occur. Consider a maximal E-colored block in this word.

If the E-block is internal in P_d, then at either boundary of that block there is a K/E selected transition whose E endpoint is an internal path vertex, contradicting the residue assumption. Therefore every E-block touches a physical endpoint of P_d.

If an endpoint E-block had length at least two, then its E-vertex adjacent to the neighboring K-block would again be internal in P_d, giving the same contradiction. Hence every E-block is a SINGLETON endpoint block. A path has only two physical endpoints, so there are at most two E-blocks and therefore

  |E| <= 2,
  |Omega| = 5+|E| <= 7.                                  (OC.7)

This is a true kernel-size collapse: a large hub-opposite coherent wheel cannot avoid a current exterior pair-deletion portal.

### 5. Exact shape of the bounded residue
If |E|=1, write E={y}. Then Omega-y=K is Hamiltonian, while (OC.2) says Omega-d is Hamiltonian for every d in K. Hence Omega is non-Hamiltonian but deletion-Hamiltonian at EVERY vertex: the partial wheel shell has promoted to a full fixed-complement critical block.

If |E|=2, write E={y,z}. For each d in K, Section 4 forces the two E vertices to occupy the two distinct physical endpoints of P_d. Consequently every retained puncture path has literal support/order shape

  y -- [Hamilton order on K-{d}] -- z,

or its complete endpoint-swapped version.                 (OC.8)

In particular K-d is one contiguous four-vertex interior block in every P_d. Thus the only quiet noncritical survivor is a seven-vertex non-Hamiltonian block Omega=K+{y,z} carrying five Hamilton punctures whose endpoint pair is the SAME physical pair {y,z}.

### 6. G23 consequence and fence
Combining SV62430 with this section, the coherent branch with the hub on the Hamilton-complement side has only three destinations:

1. a CURRENT exterior pair-deletion component-drop portal H-{d,y};
2. a full fixed-complement deletion-Hamiltonian critical block (the |E|=1 case);
3. the bounded order-seven two-ended puncture necklace (OC.8).

This is stronger than merely saying the legal capture family escapes the five P5 coordinates: outside current pair-deletion geometry the non-Hamiltonian support itself has order at most seven. No claim is made that the current component drop lowers Phi or epsilon_* by itself, and the order-seven necklace is not declared impossible here. The next legitimate consumer may attack (OC.8) directly or use its common endpoint pair to force one of y,z to become Hamilton-deletable, thereby promoting the residue to the full fixed-complement critical-block machinery.

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
    },
    {
        "relation": "dependency",
        "revision_id": "R508"
    },
    {
        "relation": "dependency",
        "revision_id": "R527"
    }
]
```