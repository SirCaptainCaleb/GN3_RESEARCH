# The n=2ell+2 additive case reduces to a two-bit carrier after at most five deletions

## Statement

Let A subset F_2^d\{0} have |A|=2ell+2. If H(A) is P_ell-free and |E(H(A))|/|A|>(ell-1)/3, then the almost-period reduction deletes exactly one vertex and yields an exact one-bit core over a quotient domain B of size ell. If R(B) denotes the number of unordered pairs {u,v} subset B with u+v notin B, then R(B)<=ell. Consequently B has a nonzero translation with boundary at most two; after deleting at most two further quotient vertices, B becomes an exact one-bit lift. Therefore A contains an exact two-bit Boolean carrier core after deleting at most 1+2*2=5 vertices.

## Body

Put n=2ell+2, so the excess in 1e6e60eb6c56 is t=1. That lemma gives x in A with boundary k<=1 and k==1 mod 2. Hence k=1. Delete the unique crossing point y. By 5a8f0a919864 the resulting induced domain A0=A\{y} is an exact one-bit lift of a quotient domain B and is non-Hamiltonian. Since |A0|=2ell+1, the quotient has |B|=ell.

For an exact one-bit lift,
  |E(H(A0))|=4|E(H(B))|+|B|=4m_B+ell.
The deleted vertex y has hypergraph degree at most floor((n-1)/2)=ell by linearity, so
  m_A <= 4m_B+2ell.
The density hypothesis gives
  m_A > ((ell-1)/3)(2ell+2)=2(ell^2-1)/3.
Therefore
  4m_B > (2ell^2-6ell-2)/3,
or equivalently
  3m_B > (ell^2-3ell-1)/2.

Let R(B) be the number of bad unordered pairs in B. Since
  3m_B=C(ell,2)-R(B),
we obtain
  R(B) < C(ell,2)-(ell^2-3ell-1)/2
       = (2ell+1)/2.
Thus R(B)<=ell.

Now put T=B union {0}. For z in B define
  b_T(z)=|{w in T:z+w notin T}|.
As before,
  sum_{z in B} b_T(z)=2R(B)<=2ell,
and
  b_T(z)==|T|=ell+1 mod 2.
Hence some z in B has b_T(z)<=2. More precisely:
- if ell is even, every b_T(z) is odd, so some z has b_T(z)=1;
- if ell is odd, every b_T(z) is even, so some z has b_T(z) in {0,2}.

Delete the unique T-point from each crossing z-pair. This removes b<=2 vertices, none equal to 0 or z, and leaves a z-invariant set T0. Therefore B0=T0\{0} is an exact one-bit lift of a smaller quotient C.

Since A0 itself is the exact one-bit lift of B, deleting from A0 both copies of each of the b deleted quotient vertices produces the exact two-bit lift of C. Starting from A, the total number of deleted vertices is
  1+2b <=5.

Thus any counterexample in the first noncritical layer is within five vertex deletions of an exact two-bit carrier. This structural reduction is independent of any Hamiltonicity theorem for two-bit lifts. The previously cited universal fourfold-lift claim is false (see the line-to-PG(3,2) counterexample), so the remaining task is to classify these exact two-bit cores with the correct set-sequential hypotheses. No computation is used.