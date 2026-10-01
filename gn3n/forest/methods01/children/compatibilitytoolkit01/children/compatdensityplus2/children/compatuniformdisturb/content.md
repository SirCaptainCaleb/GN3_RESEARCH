# One deletion state carries linearly many uniform disagreement witnesses

## Statement

Let H be a boundary tournament with pc(H)>2, let D be a set of m>=7 deletion labels, and choose one deletion cover F_d of H-d for each d in D. Put I=binom(m,2)-floor(m^2/4)-2 and K=ceil(2I/m). Then some label d has at least K incompatible partners. Moreover at least ceil(K/2) of those partners can be chosen uniformly of one of the following two types: (i) support-incompatible with F_d, in which case the pair supplies a bounded mixed-support transition—either a direct ordinary crossing edge or a two-edge passage through the opposite omitted label with neighbors in the two support classes; or (ii) support-compatible but order-incompatible with F_d, in which case the relevant full path components exhibit a reversed common edge, a tight triple reversing an ordered edge at an intersection, or a vertex-simple tight cycle.

## Body

# One deletion state carries linearly many uniform disagreement witnesses

Take the chosen family {F_d:d in D}, |D|=m>=7, and its compatibility graph G.

By compatdensityplus2,

e(G) <= floor(m^2/4)+2.

Hence the number of incompatible pairs is at least

I = binom(m,2)-floor(m^2/4)-2.

The average incompatible degree is at least 2I/m, so some label d has at least

K = ceil(2I/m)

incompatible partners.

Fix such d. Partition its incompatible partners e into two classes.

## Type I: support-incompatible

On W=V(H)-{d,e}, the pair-state restrictions of F_d and F_e induce different two-class support partitions.

Therefore some two vertices x,y in W lie in the same path component of one full cover, say F_e, but in different support classes induced by F_d on W. Follow the F_e path segment from x to y. As the segment passes from one F_d-class to the other, one of two things happens:

1. some ordinary edge uv of F_e with u,v in W has its endpoints in the two different F_d support classes; or
2. the change of class occurs through d, so F_e contains a consecutive two-edge segment u,d,v with u and v in the two different F_d support classes.

Thus every support-incompatible partner supplies a bounded mixed-support transition relative to F_d: either a direct crossing edge or a two-edge passage through the opposite omitted label. If the witnessing same-component pair instead belongs to F_d and is separated by F_e, the symmetric statement holds with d,e interchanged.

## Type II: support-compatible but order-incompatible

The two restrictions have the same support partition but are not compatible. Therefore on at least one pair of corresponding full path components, two common vertices occur in different relative orders.

Apply pathcalc01, Section 4, to those two tight paths. It yields at least one of:

1. a common ordered edge used in opposite directions;
2. a tight triple reversing an ordered edge of one path at an intersection with the other;
3. a vertex-simple tight cycle in the union of the two paths.

Thus every Type-II partner supplies an explicit order-disagreement witness.

The K incompatible partners split into these two classes, so one class has size at least ceil(K/2).

Therefore one chosen deletion state participates in linearly many disturbances of one uniform broad kind: support-partition disagreement, each carrying a bounded mixed-support transition, or explicit relative-order disagreement.

No fixed-order classification is used.
