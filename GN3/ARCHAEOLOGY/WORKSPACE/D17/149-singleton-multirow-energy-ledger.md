# Joint singleton-fiber replacements have an exact external/internal energy ledger

**Workspace:** D17
**State:** established
**Key:** `singleton-multirow-energy-ledger`

**Summary:** Exact coordinated K ledger plus support-level relaxation. Simultaneous replacements split into external energies and internal comparisons evaluated on both new rows. For fixed support partitions, path-order minimization factorizes globally, so after an R511 support copy every unchanged row can be reoptimized independently; the opposite source row automatically loses its reverse pair defect without needing a new support copy. A blocked bridge exports its full pair saving to third fibers, and K-neutral minority-to-majority bridge moves strictly decrease the fixed witness minority size until the singleton-minority floor.

### Exact multi-row ledger
Retain the singleton-cover family {C_x}, support partitions sigma_x, and ordered defects kappa(i<-j) from `codimension-one-coherence`. Let I be any nonempty set of deletion labels. For each i in I choose an actual replacement C'_i of H-i; rows outside I remain unchanged.

For i in I define the external energy against the unchanged rows I^c by

  E_i^{I^c}(C)= sum_{j notin I} kappa_C(i<-j) + sum_{j notin I} kappa_{C_j}(j<-i; sigma(C)).

The first sum uses the selected adjacencies of C against the fixed target partitions supplied by the unchanged rows. The second uses the fixed selected adjacencies of C_j against the target partition induced by sigma(C). Exactly as in `singleton-row-weighted-recombination`, each E_i^{I^c} is a selected-edge weight plus a labelled incoming-cut cost after simply omitting provenance labels in I.

Partition the ordered pairs (r,s), r!=s, according to whether zero, one, or two indices lie in I. Pairs with zero changed indices cancel. Pairs with exactly one changed index are exactly the external energies above. Hence the TOTAL defect change is the exact identity

  K(F')-K(F)
   = sum_{i in I} [E_i^{I^c}(C'_i)-E_i^{I^c}(C_i)]
     + sum_{i,j in I, i!=j} [kappa_{F'}(i<-j)-kappa_F(i<-j)].

The internal ordered comparisons are evaluated once, with BOTH new arguments: the selected path order from C'_i and the target support partition from C'_j. This is the correct ledger for coordinated support-changing repair. It avoids the double counting that results from summing one-row energies E_i computed against the old family.

For I={a,b}, this becomes

  Delta K = Delta E_a^{outside {a,b}} + Delta E_b^{outside {a,b}}
            + Delta kappa(a<-b)+Delta kappa(b<-a).

No pairwise optimality assumption is used.

### Fixed-support relaxation eliminates path-order collateral globally
It is useful to optimize path orders out of the problem after a support change. Call a support family Sigma={sigma_x} realizable when every sigma_x=A_x|B_x is carried by at least one actual exact two-cover of H-x. For fixed Sigma define

  m_x(Sigma)= min_C sum_{y!=x} kappa_C(x<-y),

where C ranges over actual exact two-covers of H-x with support partition sigma_x. Equivalently m_x is the minimum selected-edge w_x^Sigma weight in that support fiber. Since the target cuts are fixed once Sigma is fixed, the rows are independent and

  K^*(Sigma):=min_{representatives realizing Sigma} K = sum_x m_x(Sigma).

Thus after ANY realizable support-changing move one may reselect every row independently inside its unchanged support before judging profitability. This cannot increase K. A globally K-minimal family may in particular be assumed to realize m_x(Sigma) in every row.

Apply this to the R511 support copy below. Let Sigma' differ only in row a, with sigma'_a=(S+b)|T_0. The support sigma_b itself does not change. Under Sigma', the target partition for the ordered comparison b<-a is exactly sigma_b, namely (S+a)|T_0. Therefore every exact representative having support sigma_b has

  kappa_{Sigma'}(b<-a)=0.

If the original family is row-optimal, retaining its old C_b already gives

  m_b(Sigma') <= m_b(Sigma)-kappa_F(b<-a),

and an actual row-minimizing replacement C'_b with the same support sigma_b exists by finiteness. Hence the opposite row can always be coupled at the ORDER level without inventing a new support copy. The local support-copy fence `singleton-r511-opposite-row-local-fence` shows that a second support-changing alignment is not available from R511 data alone.

More generally every unchanged row c may be reoptimized inside sigma_c after the a-support change. Therefore if the fully relaxed K^*(Sigma') still does not decrease, the surviving collateral is genuinely support-level: it remains after all order-only repairs have been exhausted.

### R511 seam-free bridge exports all blocked savings to third fibers
Now retain the no-interior-crossing R511 bridge cell of `codimension-one-coherence` for an ordered defect a<-b. Thus

  C_b = Q | T,
  V(Q)={a} union S,
  V(T)=T_0,

and C_a has literal support/order form

  S-block -- b -- T_1  |  T_2

(or the reversal), where T_1,T_2 are nonempty and partition T_0. Relative to the substituted target (S union {b})|T_0, the unique selected crossing of C_a is the bridge from b into T_1. Therefore

  kappa_F(a<-b)=1.

For the reverse comparison b<-a, the Q rail lies wholly in the target block S union {a} union T_1, while the Hamilton T rail spans T_1 union T_2. Since T_1,T_2 are both nonempty, T contains at least one selected T_1|T_2 adjacency. Hence

  kappa_F(b<-a)>=1.

The seam-free replacement from `singleton-row-weighted-recombination` is

  C'_a = (contiguous S-through-b subpath) | T,

with support partition (S union {b})|T_0. This is exactly the deleted-label transport of sigma_b. Thus the two new fiber partitions agree on H-{a,b}; by `codimension-one-coherence`, in a counterexample both ordered defects vanish:

  kappa_{F'}(a<-b)=kappa_{F'}(b<-a)=0.

Take I={a,b} and leave C_b unchanged. The joint ledger therefore gives

  K(F')-K(F)
   = Delta E_a^{outside {a,b}}
     - [1+kappa_F(b<-a)].

(The b-external energy is unchanged.) Consequently, if F is globally K-minimal,

  Delta E_a^{outside {a,b}} >= 1+kappa_F(b<-a) >= 2.

Thus a blocked seam-free bridge repair cannot hide its cost in the repaired pair: it must export at least the full two-direction pair saving into comparisons with third deletion labels. In particular some c outside {a,b} has a strictly increased current comparison involving a after the hypothetical replacement, either outgoing a<-c or incoming c<-a. After fixed-support relaxation the analogous statement is stronger in interpretation: any remaining nondecrease is not removable by rechoosing path orders on the unchanged supports.

### Neutral bridge moves have a terminating fixed-witness secondary potential
Retain a physical witness pair {u,v} from `singleton-disagreement-fan`. Among deletion labels outside {u,v}, let A,B be the two status classes and suppose |A|<=|B|. Take a in A and b in B, and suppose the ordered defect a<-b is in the seam-free R511 bridge form above. The support replacement sigma_a -> sigma'_a copies sigma_b on the common residue, so the same-block status of {u,v} in row a flips from the A value to the B value; all other rows are unchanged. Thus

  (|A|,|B|) -> (|A|-1,|B|+1).

If the bridge move is K-neutral and |A|>=2, then the new family is also K-minimal and {u,v} remains an incoherence witness with strictly smaller minority size. Consequently, if one chooses among all K-minimal families and all of their incoherence witnesses a pair minimizing min(|A|,|B|), no K-neutral seam-free bridge can run from the minority class to the majority unless the minority size is exactly one.

Equivalently, away from the singleton-minority floor, a minority-to-majority bridge in such a minimal witness pair is either a strict K descent (closing the hypothetical K-minimal obstruction) or it must strictly increase K. This gives neutral moves a genuine terminating secondary coordinate rather than treating ties as progress. The size-one witness-star remains a separate residual and is not closed here.

### Scope
The multi-row identity, fixed-support relaxation, R511 collateral-export inequality, and neutral fixed-witness secondary potential are exact finite arguments. They do not prove that repeatedly adjoining collateral labels yields a profitable closed replacement family. The local fence shows that an opposite support-aligned row is not forced by R511 alone; only same-support row relaxation is automatic. The remaining parent problem is therefore a support-level coordinated repair, with direct-crossing defects and the singleton-minority witness-star as explicit unresolved exits.
