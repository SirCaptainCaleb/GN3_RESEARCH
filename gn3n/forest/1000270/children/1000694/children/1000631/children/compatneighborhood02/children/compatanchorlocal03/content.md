# Every incompatible pair inside a compatibility neighborhood is localized at the anchor label

## Statement

Let H be a boundary tournament with pc(H)>2, choose deletion covers F_x, and let G be their compatibility graph. Suppose a,d and b,d are edges of G but a,b is not. Put W=V(H)-{a,b,d}. Then the restrictions of F_a and F_b to W are compatible. Consequently every witness to the incompatibility of F_a and F_b on V(H)-{a,b} must involve d. More explicitly, either there is x in W such that d and x lie in the same path of exactly one of F_a,F_b, or the two covers agree on component membership for all common vertices and there is x in W such that d and x occur in the same path in both covers but in opposite relative orders.

## Body

# Proof

Because F_a is compatible with F_d, their restrictions to every smaller common domain are compatible; in particular F_a and F_d are compatible on W. Likewise F_b and F_d are compatible on W.

Compatibility on a fixed vertex set is transitive: for every pair of vertices of W, F_a and F_d agree on whether the pair lies in one path or in two different paths, and when the pair lies in one path they agree on its relative order; the same statements hold for F_b and F_d. Hence F_a and F_b agree on all such pair data on W. Thus their restrictions to W are compatible.

Now F_a and F_b are incompatible on their full common domain U=V(H)-{a,b}=W union {d}. Since every pair entirely inside W already agrees, any disagreement witness must involve d.

If the two covers disagree on support membership, then some x in W has different same-path status with d in the two covers: d and x lie in one path in one cover and in different paths in the other.

Otherwise the support relation agrees on all of U. Since the covers are still incompatible, the disagreement is in relative order inside a common path. All pairs contained in W have the same relative order, so some x in W sharing a path with d in both covers must occur on opposite sides of d in the two path orders.

Therefore an incompatible pair of deletion covers that are both compatible with one anchor cover has a single-label localization: deleting the anchor label d removes every support/order disagreement between the pair.

## Interaction with the neighborhood lemma

If d has k compatible partners, compatneighborhood02 shows that at least binom(k,2)-k pairs among those partners are incompatible. Every one of those incompatible pairs is therefore localized at the same anchor d. Thus high compatibility degree at one deletion state automatically creates a quadratic family of incompatibilities all carried by one common label.
