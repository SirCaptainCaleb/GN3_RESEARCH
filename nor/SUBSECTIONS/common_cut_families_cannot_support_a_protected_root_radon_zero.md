# Common-cut families cannot support a protected-root Radon zero

## Metadata

- ID: common_cut_families_cannot_support_a_protected_root_radon_zero
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 13
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Fix a normalized first-phase length p and a family of one-change deletion carriers whose first p physical coordinates form the same set L, though the carriers may differ to the right and may omit different coordinates. Every canonical switch root has the form e_a-e_c with a in L and c outside L. The common cut functional, equal to +1 on L and -1 on its complement, takes value 2 on every such root. Hence no positive protected-root dependence can be supported inside one common-cut family. Any genuine protected-root Radon zero must involve at least two distinct physical first-phase cuts. In particular same-cut exchange recurrences, including the ternary A2 recurrence, cannot by themselves furnish the positive cancellation needed for extraction.

## Development

Common-cut coorientation theorem. Let F be any family of normalized one-change deletion carriers with common first-phase length p such that the same physical set L occupies the first p coordinate positions in every carrier. The carriers may differ arbitrarily to the right of that cut and may omit different coordinates. For each carrier, insert its omitted coordinate at the canonical switch position and select any protected 10-descent. By the canonical switch-root theorem the resulting physical root is rho=e_a-e_c with a in that carrier's first p coordinates and c strictly to the right. Since the first-p set is the common set L, every such root has a in L. Put every other physical coordinate in R=V\L, including coordinates omitted in some members of the family. Then c lies in R for every chosen root. The common cut functional phi=+1 on L and -1 on R therefore gives phi(rho)=2 for every canonical protected root from every carrier in F. Hence no positive root dependence can be supported inside a common-cut family. Any compatible protected-root Radon zero must involve at least two genuinely distinct first-p physical sets. Equivalently, omission changes, same-profile exchanges, A2 recurrences, and other dynamics confined to one protected cut can create combinatorial recurrence but cannot create a physical protected-root zero. For global extraction, cut change is therefore a necessary event. A useful lexicographic bookkeeping state is consequently (root-span rank, protected-cut class): if root rank fails to increase and a signed circuit is forced, that circuit must traverse more than one protected cut.
