# Sharp half-order endpoint probes force three crossings or disagreement

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, and let A=(a_0,...,a_m), m=lambda-1>=3, be globally longest with U=V(H)-V(A). Choose arbitrary exact two-covers G_0 of H-a_0 and G_m of H-a_m. Then either one of G_0,G_m has at least three ordinary edges crossing the cut between the surviving A-vertices and U, or the two endpoint probes expose explicit support/order disagreement: a differing common support partition, reversed common edge, reversing tight triple, or vertex-simple tight cycle.

## Body

# Sharp half-order endpoint probes force three crossings or disagreement

Let H be a minimum counterexample in the sharp half-order shell

|V(H)|=2 lambda+1,

and let

A=(a_0,...,a_m),  m=lambda-1>=3,

be a globally longest tight path. Put U=V(H)-V(A).

Choose arbitrary exact two-covers G_0 of H-a_0 and G_m of H-a_m. Let t_0,t_m be their numbers of ordinary edges crossing the corresponding surviving-A | U cuts.

By the certified endpoint-crossing theorem 7b2d1a6cf904, each t_i is at least one unless support/order disagreement has already been exposed, and if both t_i equal one the endpoint probes already disagree. We prove the stronger sharp-shell conclusion.

Assume that no explicit support/order disagreement has yet occurred and that

t_0,t_m <=2.

We derive a contradiction.

## 1. Neutral endpoint covers with one or two crossings have only two exact orders

Consider G_0.

If t_0=1, the proof of 7b2d1a6cf904 shows that G_0 has supports

(A-{a_0}) union {u}
and
U-{u}

for some u in U, with the first support Hamiltonian.

If its Hamilton path orders the common A-vertices differently from A, pathcalc01 gives explicit order disagreement. Thus assume the inherited A-order is preserved.

The unique crossing makes the surviving A-vertices one block. The mixed component cannot have order

(a_1,...,a_m,u),

because prepending a_0 would give the tight path

(a_0,a_1,...,a_m,u)

of order lambda+1. Hence the only neutral order is

(u,a_1,...,a_m).                         (L1)

If t_0=2, c8d4f2197a61 gives either the crosswise shape or the singleton internal-exchange shape. The crosswise shape is consumed by 4cd0c6fd1e31 and exposes explicit order disagreement. Hence in the neutral branch G_0 has a Hamilton path

(B_1,u,B_2)

on (A-{a_0}) union {u}, with B_1,B_2 nonempty.

Again absence of order disagreement means that the common A-vertices occur in their inherited order. Therefore B_1 is an initial segment of (a_1,...,a_m) and B_2 the complementary terminal segment.

If |B_1|>=2, prepending a_0 creates no new uncertain triple: the first new triple is (a_0,a_1,a_2), inherited from A, and every later triple is already in the exchange path. This would give a tight path of order lambda+1. Therefore |B_1|=1, and the neutral order is

(a_1,u,a_2,...,a_m).                     (L2)

The right endpoint is symmetric. Thus, for some v in U, absence of disagreement forces the mixed component of G_m to have one of the two orders

(a_0,...,a_{m-1},v)                      (R1)

when t_m=1, or

(a_0,...,a_{m-2},v,a_{m-1})              (R2)

when t_m=2.

In every case the other component is a Hamilton path on U with the displayed exterior label removed.

## 2. Compare the common two-deletion covers

Delete a_m from G_0 and a_0 from G_m. Since a_m is the terminal endpoint of both L1 and L2, and a_0 is the initial endpoint of both R1 and R2, this gives exact two-covers T_0,T_m of

H-{a_0,a_m}.

Let

I={a_1,...,a_{m-1}}.

The support partitions are

T_0 : (I union {u}) | (U-{u}),
T_m : (I union {v}) | (U-{v}).           (1)

The first parts have order lambda-1 and the second parts order lambda.

If u!=v, the unordered support partitions in (1) are different. The exact-cover disagreement theorem in deletion01 therefore gives reciprocal support-partition crossing edges. This is explicit disagreement, contrary to assumption.

Hence u=v.

Now the two covers have the same support partition. If the corresponding Hamilton orders on either common support differ, deletion01 and pathcalc01 give a reversed common edge, reversing tight triple, or vertex-simple tight cycle. Again this is explicit disagreement.

The only remaining possibility is that T_0 and T_m are identical as ordered two-path covers.

But restoring a_m to T_0 recovers G_0 by adjoining a_m at the right end of the component on I union {u}, whereas restoring a_0 to T_m recovers G_m by adjoining a_0 at the left end of that same common component.

Thus the two endpoint extensions use opposite ends of one component. The certified common endpoint-extension lemma in deletion01 says that in a tournament with path-cover number greater than two, two such extensions must use the same end of the same component. Equivalently, opposite-end extensions would adjoin both endpoints simultaneously and give a spanning two-cover.

This contradiction finishes the proof.

Therefore our assumption was impossible: for arbitrary endpoint covers of a globally longest path in the sharp half-order shell, either one endpoint cover has at least three cut crossings, or the endpoint probes expose explicit support/order disagreement. ∎

## Route consequence

In the sharp half-order equality shell, all one- and two-crossing endpoint states are consumed into ordered disagreement unless the opposite endpoint already supplies a three-or-more-crossing state. Thus the surviving endpoint-transport residue begins at crossing multiplicity three, not two.
