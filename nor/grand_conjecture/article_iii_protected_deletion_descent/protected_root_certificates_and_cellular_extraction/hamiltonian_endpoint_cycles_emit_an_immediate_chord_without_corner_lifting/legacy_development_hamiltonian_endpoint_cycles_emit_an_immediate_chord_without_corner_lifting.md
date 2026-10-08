# Hamiltonian endpoint cycles emit an immediate chord without corner lifting — preserved pre-item development

## Composition

(none yet)

## Development

## Hamiltonian endpoint cycles emit an immediate chord without corner lifting

Work in the coboundary-flat alternating ternary endpoint regime. Let
x_0 -> x_1 -> ... -> x_{k-1} -> x_0
be an actual endpoint-root cycle whose physical support is Hamiltonian on the ambient coordinate set.

For one cycle edge write
x=x_i,qquad c=x_{i+1},
and choose its normalized endpoint witness
O_x=(a,b,c,d,ldots)
with one-change word 0^p1^q and p>=3. Prepending x gives the fully-curved endpoint barrier, so
alpha(x,a,c)=0.
Put
lambda_0=alpha(a,c,d).

The coordinates x,a,b,c,d are distinct.

### Case 1: lambda_0=0

By the audited endpoint-pivot theorem (§113), deleting b from the prepended endpoint state gives a genuine one-change deletion witness
O_b=(x,a,c,d,ldots)
omitting b, with the same phase profile.

Its endpoint root is
e_b-e_c,
i.e. the actual directed endpoint root
b -> c.

Because the old physical cycle is Hamiltonian, b is a vertex of that cycle. Its unique old edge entering c is x->c. Since b!=x, the new root b->c is not an old cycle edge. It is a directed chord.

The chord b->c together with the old directed segment from c back to b gives a strictly shorter positive cycle consisting entirely of actual endpoint roots.

### Case 2: lambda_0=1

Delete b from the prepended endpoint state. The first two statuses of
(x,a,c,d,ldots)
are
alpha(x,a,c)=0,qquad alpha(a,c,d)=1.
Therefore the ordered tetrahedron (x,a,c,d) carries an actual 0->1 transition with physical first-minus-last root
e_x-e_d,
i.e. x->d.

This transition may be flat or fully curved; either way the physical transition root is genuine. In the flat case it is the first root of the audited one-sided transport flag, while in the fully-curved case it is already protected.

Again Hamiltonicity puts d on the old physical cycle, and d!=c. Thus x->d is not the old outgoing edge x->c. It is a directed chord. The chord together with the old directed segment from d back to x gives a strictly shorter positive physical root cycle of actual endpoint/transport roots.

### Theorem

Every Hamiltonian endpoint-root cycle admits an immediate directed chord from the local endpoint-pivot packet, without any Johnson square/corner-lift assumption.

More precisely, at every endpoint edge x->c:
- lambda_0=0 yields a shorter endpoint-only cycle through the chord b->c;
- lambda_0=1 yields a shorter mixed endpoint/transport cycle through the chord x->d.

Hence a Hamiltonian endpoint cycle cannot be terminal merely because its rank-two partner cuts fail to align. The witness-preserving square-lift lemma is unnecessary for the first physical-cycle descent.

### Scope

This does not by itself contradict minimum ENDPOINT-cycle length in the lambda_0=1 branch, because the shorter cycle contains a transport root rather than only endpoint roots. The correct next minimal object is therefore a positive physical circuit taken across the union of realized endpoint roots and audited flat/full transport roots.

The new closure target is to exclude a minimum mixed circuit. A one-sided audited transport flag contains no positive dependence by itself, so any such minimum circuit must contain a genuine meeting/branching of provenance classes.
