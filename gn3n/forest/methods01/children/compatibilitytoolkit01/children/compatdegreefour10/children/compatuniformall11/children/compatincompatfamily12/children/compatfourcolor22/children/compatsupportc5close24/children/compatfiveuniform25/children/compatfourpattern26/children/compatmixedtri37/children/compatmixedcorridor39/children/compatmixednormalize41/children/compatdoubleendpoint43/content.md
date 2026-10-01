# Two same-endpoint replacements by one omitted label force a five-set or reverse cross triple

## Statement

Let H be a minimum counterexample and let H-b=P|Q be a deletion cover, with both components of order at least three. Let a be an endpoint of P and c an endpoint of Q. Suppose H-a has a deletion cover whose P-side is obtained by replacing a with b in the same endpoint position while leaving Q fixed, and H-c has a deletion cover whose Q-side is obtained by replacing c with b in the same endpoint position while leaving P fixed. Let u be the neighbor of a on P and v the neighbor of c on Q. Then the five-set {a,u,b,c,v} is Hamiltonian, or an explicit reverse cross triple through b is tight. More precisely, the four initial/terminal orientation cases reduce respectively to one of the reversal pairs (u,b,c)/(c,b,u), (c,b,u)/(u,b,c), (u,b,v)/(v,b,u), or (v,b,u)/(u,b,v); one orientation gives the Hamilton five-path formed by concatenating the two endpoint hooks, while the reverse orientation is the forced cross witness.

## Body

# Proof

The deletion cover H-b=P|Q forces the endpoint-hook triples from c38e8b5c48ee on both P and Q.

We inspect the four choices of whether a and c are initial or terminal endpoints in their displayed component orders. In each case, the same-endpoint replacement by b supplies the same local orientation as the inherited component, and the endpoint hooks provide two tight triples. One reversal pair remains undecided.

## Both terminal

Write

P=(...,u,a),  Q=(...,v,c),

with replacement paths (...,u,b) and (...,v,b).

The terminal endpoint hooks give (b,a,u) and (b,c,v) tight. By cyclic invariance, (a,u,b) is tight.

Exactly one of (u,b,c) and (c,b,u) is tight.

If (u,b,c) is tight, then

(a,u,b,c,v)

is a Hamilton tight path on the five-set. Otherwise (c,b,u) is the reverse cross witness.

## Both initial

Write

P=(a,u,...),  Q=(c,v,...),

with replacement paths (b,u,...) and (b,v,...).

The initial endpoint hooks give (u,a,b) and (v,c,b) tight. By cyclic invariance, (b,u,a) is tight.

Exactly one of (c,b,u) and (u,b,c) is tight.

If (c,b,u) is tight, then

(v,c,b,u,a)

is Hamiltonian. Otherwise (u,b,c) is the reverse cross witness.

## a terminal, c initial

The hooks give (a,u,b) and, from (v,c,b), its cyclic form (b,v,c).

Exactly one of (u,b,v) and (v,b,u) is tight.

If (u,b,v) is tight, then

(a,u,b,v,c)

is Hamiltonian. Otherwise (v,b,u) is the reverse cross witness.

## a initial, c terminal

The hooks give (b,u,a) and the cyclic form (c,v,b) of the terminal Q-hook.

Exactly one of (v,b,u) and (u,b,v) is tight.

If (v,b,u) is tight, then

(c,v,b,u,a)

is Hamiltonian. Otherwise (u,b,v) is the reverse cross witness.

Thus every orientation of two same-endpoint replacements by the same omitted label produces either a Hamiltonian five-set or one explicit reverse cross triple through b.

If the five-set is Hamiltonian, its complement in H is non-Hamiltonian and has path-cover number two by minimum-counterexample minimality; this additional complement statement is not needed for the local dichotomy.
