# Two-cover inseparability classes

## Statement

Let H be a boundary tournament admitting at least one two-cover. Define u~v when u and v lie in the same component of every two-cover of H. Then ~ is an equivalence relation. Every component support of every two-cover is a union of ~-classes, and two vertices can be separated by some two-cover if and only if they lie in distinct ~-classes.

## Body

Reflexivity and symmetry are immediate. For transitivity, suppose u~v and v~w. In every two-cover, u and v lie in one component and v and w lie in one component. Since the two component supports are disjoint, all three vertices lie in the same component, so u~w.

Now fix a ~-class C and any two-cover P|Q. Any two vertices of C must lie in the same one of P,Q, so the whole class C is contained in one component support. Hence both component supports are unions of whole ~-classes.

Finally, u and v are separable by some two-cover precisely when it is false that they lie together in every two-cover, which is precisely u not~v.

No boundary-tournament axiom is used beyond the existence of the family of two-covers; this is a general partition-family fact. It is the line-independent core of astra005criticalclass. The vertex-critical conclusion of that Astra node genuinely uses minimality of a prescribed-separation counterexample and therefore remains in the Astra-005 line.
