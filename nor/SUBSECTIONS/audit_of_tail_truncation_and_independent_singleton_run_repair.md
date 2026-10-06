# Audit of tail truncation and independent singleton-run repair

## Metadata

- ID: audit_of_tail_truncation_and_independent_singleton_run_repair
- Parent Section: higher_memory_norine_geodesics
- Position: 45
- Row version: 2
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Section 42's truncation argument does not justify first-post-switch polarization when q>1. The shortened ground set is a proper restriction of the minimum counterexample; it is not itself a counterexample. Thus neither endpoint blocking at the new endpoint nor rejection of a good cyclic cut is inherited.

Section 43's singleton-final-run conclusion is valid independently. On the full ground set, let T have word sigma^p(1-sigma) and residual deletion prefixes form a directed 3-cycle. Put w=t_m. If h(w,b,c)=1-sigma, the full order (w,b,c,a,t_1,...,t_{m-1}) has word (1-sigma)^2 sigma^{p+2}, closing the instance. Otherwise the cyclic rotations give h(w,a,b)=h(w,b,c)=h(w,c,a)=sigma. Then (w,a,b,t_1,...,t_{m-1}) is a constant-color deletion order, and prepending c closes the instance. No minimum-size hypothesis is needed.

Hence a counterexample's common-tail deletion cycle must have final run length at least two. This cannot be iterated by truncation. Development includes an arbitrarily long globally soluble family satisfying all local rigidity and endpoint identities while violating the claimed general switch polarization.

## Development

## Audit of tail truncation in section 42; independent repair of section 43

### Finding
Section 42 starts with a common-tail deletion cycle on the full counterexample ground set V, writes the tail word as sigma^p(1-sigma)^q, and truncates T at w=t_{p+3}. The three truncated deletion orders remain one-change. However the next use of endpoint blocking and the bad-cut assumption is not justified.

The truncated ground set V_*={a,b,c,t_1,...,t_{p+3}} is a proper subset of V when q>1. A minimum counterexample guarantees that its restriction has a spanning one-change order. It does not make that restriction a counterexample. Therefore:
- h(t_{p+2},w,b)=sigma is not supplied by endpoint blocking on the original ground set;
- a good cut on the smaller cyclic order (a,T_*,b,c) is not a contradiction to counterexamplehood on V.

Consequently the claimed first-post-switch polarization for arbitrary q is unsupported. This is a gap in the proof; no counterexample to the grand conjecture is asserted.

### A family separating the local rigidity from the asserted polarization
Let q>=2, m=q+3, and T=(t_1,...,t_m) have word 0 1^q. On residual vertices a,b,c use a->b->c->a. Prescribe:
h(z,t_1,t_2)=0 for z in {a,b,c};
h(s,t,t_1)=0 iff s->t for distinct residual s,t;
h(a,b,c)=h(b,c,a)=h(c,a,b)=1;
h(t_{m-1},t_m,z)=0 for each residual z.
Set reverse tuples to complementary colors.

These are all the head, residual, and terminal identities in section 40, including both endpoint blocking identities for each of (a,b,T),(b,c,T),(c,a,T). Set w=t_4 and additionally prescribe h(w,b,c)=1, contrary to section 42's polarization. There is no reversal-orbit conflict: this last prescription has two residual vertices and tail vertex t_4, whereas the head pair identities use t_1 and the terminal identities use two tail vertices.

One can also prescribe h(b,c,t_2)=h(c,t_2,t_3)=1. Then
(t_1,a,b,c,t_2,...,t_m)
has word 0 1^m and spans V. The first color follows from reversing h(b,a,t_1)=1; all subsequent colors follow from the displayed prescriptions and the tail word. Thus the local rigidity plus endpoint identities alone do not imply first-post-switch polarization. The family is globally soluble and does not refute the conditional claim for genuine minimum counterexamples.

### Independent theorem: the singleton final run is impossible
Section 43's conclusion can be proved on the full ground set without truncation.

Suppose a reversal-antisymmetric ternary coloring on V has no spanning one-change order. Suppose T=(t_1,...,t_m) has word sigma^p(1-sigma), p>=1, and V\V(T)={a,b,c}, with deletion orders
(a,b,T), (b,c,T), (c,a,T)
all one-change. We derive a contradiction.

Put w=t_m and eta=h(w,b,c). Counterexamplehood on V forces the identities from section 40:
h(a,t_1,t_2)=h(c,a,t_1)=sigma;
h(b,c,a)=1-sigma;
h(t_{m-1},w,b)=sigma.
The last identity follows by appending b to the actual full deletion order (c,a,T).

Consider the cyclic order C=(a,T,b,c). Its cyclic ternary color list is
sigma^{p+1}, (1-sigma), sigma, eta, (1-sigma), sigma.
If eta=1-sigma, omit the two consecutive cyclic windows with colors (1-sigma),sigma immediately after the initial sigma^{p+1} run. Concretely, the corresponding full linear order starts at t_m=w and is
(w,b,c,a,t_1,...,t_{m-1}).
Its color word is (1-sigma)^2 sigma^{p+2}, hence has one change. This contradiction gives eta=sigma. Cyclic rotation of the residual names similarly gives
h(w,a,b)=h(w,b,c)=h(w,c,a)=sigma.

Now
D=(w,a,b,t_1,...,t_{m-1})
is sigma-tight: its first three colors are h(w,a,b),h(a,b,t_1),h(b,t_1,t_2), all sigma, and the remaining windows lie in T with the final (1-sigma) window removed. D omits only c. Prepending c adds a single color to a constant word and therefore gives a spanning order with at most one change, contradiction.

Thus any common-tail deletion 3-cycle in a counterexample must have final run length at least two. This theorem uses no minimum-size assumption. It is a repair of section 43, not a proof of the general polarization claimed in section 42.

### Scope
All contradictions above use permutations of the full ambient set V. The valid singleton-run theorem does not permit repeated truncation of a longer final run. A universal tail-shortening exchange remains unproved.
