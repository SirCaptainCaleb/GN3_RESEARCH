# Every exact two-crossing endpoint cover forces order disagreement

## Statement

Under the sharp half-order hypotheses of c8d4f2197a61, every exact two-cover of H-a_0 with exactly two crossings across (A-{a_0})|U exposes explicit relative-order disagreement with the globally longest path A. Thus both shapes in the certified two-crossing classification are consumed: the crosswise shape by 4cd0c6fd1e31, and the singleton internal-exchange shape by a direct longest-path prefix argument.

## Body

# Every exact two-crossing endpoint cover forces order disagreement

Work in the sharp half-order setup of c8d4f2197a61:

|V(H)|=2 lambda+1,

A=(a_0,...,a_{lambda-1})

is globally longest, U=V(H)-V(A), and T is an exact two-cover of H-a_0 having exactly two ordinary edges across (A-{a_0})|U.

The certified classification c8d4f2197a61 has exactly two cases.

## Crosswise case

If T is crosswise, 4cd0c6fd1e31 proves that T exposes explicit order disagreement with A: either an A-block itself disagrees with the inherited relative order, or maximality forces a tight triple reversing an ordered edge of A.

## Singleton internal-exchange case

It remains to treat the shape

(B_1,u,B_2) | (U-{u}),

where u in U and B_1,B_2 are nonempty A-blocks partitioning A-{a_0}. Let

C=(B_1,u,B_2)

be the mixed component, which has order lambda.

First compare the relative order of all surviving A-vertices along C with their order along A. If these relative orders differ, pathcalc01 gives the standard reversed-edge, reversing-triple, or vertex-simple tight-cycle witness.

Assume therefore that the common A-vertices occur in the same relative order in C and A. Since B_1 occurs before B_2 in C and B_1 union B_2=A-{a_0}, the first vertex of B_1 must be a_1. Let z be the second vertex of C; if B_1 has at least two vertices, z is the next A-vertex of B_1, while if B_1 is a singleton, z=u.

If

(a_0,a_1,z)

were tight, then prepending a_0 to C would give the tight path

(a_0,B_1,u,B_2)

of order lambda+1: the displayed triple is the only new consecutive triple, and every later consecutive triple is inherited from C. This contradicts maximality of A. Hence boundary antisymmetry gives

(z,a_1,a_0)

tight, reversing the ordered edge (a_0,a_1) of A.

Thus the singleton internal-exchange case also necessarily exposes explicit order disagreement.

Both two-crossing shapes are therefore consumed. ∎

## Route consequence

At a longest-path endpoint in the sharp half-order shell, crossing multiplicity two is itself an ordered obstruction. No support-only equality residue remains at t=2.
