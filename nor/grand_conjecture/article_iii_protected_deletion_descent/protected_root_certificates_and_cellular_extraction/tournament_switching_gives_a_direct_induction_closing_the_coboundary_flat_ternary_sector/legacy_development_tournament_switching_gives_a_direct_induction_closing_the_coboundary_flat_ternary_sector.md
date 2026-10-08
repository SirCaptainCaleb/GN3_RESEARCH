# Tournament switching gives a direct induction closing the coboundary-flat ternary sector — preserved pre-item development

## Development

## Tournament switching gives a direct induction closing the coboundary-flat alternating ternary sector

Work with a coboundary-flat alternating ternary orientation alpha on V.

### 1. Tournament representation

Fix a reference vertex r. Define tournament edge bits t(a,b) in F_2, with t(a,b)=1 meaning a->b, as follows.

For a,b distinct from r, put
t(a,b)=1 xor alpha(r,a,b).

Put
t(r,a)=0
for every a distinct from r, and therefore t(a,r)=1.

Alternation of alpha gives t(b,a)=1 xor t(a,b), so this is a tournament.

For a triple containing r,
t(r,a) xor t(a,b) xor t(b,r)
=0 xor (1 xor alpha(r,a,b)) xor 1
=alpha(r,a,b).

For a,b,c distinct from r, flatness on {r,a,b,c} gives
alpha(a,b,c)
=alpha(r,a,b) xor alpha(r,a,c) xor alpha(r,b,c).

Also
t(c,a)=1 xor alpha(r,c,a)=alpha(r,a,c)
by alternation. Hence
t(a,b) xor t(b,c) xor t(c,a)
=alpha(a,b,c).

Therefore for every ordered triple,
alpha(a,b,c)=t(a,b) xor t(b,c) xor t(c,a).

So alpha is exactly the triangle-parity orientation of a tournament switching class.

### 2. Switching leaves alpha unchanged

For S subset V, switch every tournament edge crossing S | S^c. Algebraically,
t^S(a,b)=t(a,b) xor 1_S(a) xor 1_S(b).

On a triangle, each vertex indicator appears twice, so
t^S(a,b) xor t^S(b,c) xor t^S(c,a)
=t(a,b) xor t(b,c) xor t(c,a).

Thus tournament switching changes the representative t but leaves alpha unchanged.

### 3. Directed Hamiltonian paths read alpha as distance-two back-edge bits

Let
P=(v_1,...,v_m)
be a directed Hamiltonian path in a tournament representative t:
t(v_i,v_{i+1})=1 for every i.

Then
alpha(v_i,v_{i+1},v_{i+2})
=1 xor 1 xor t(v_{i+2},v_i)
=t(v_{i+2},v_i).

Thus the NOR status word along a directed Hamiltonian path is exactly the word of backward distance-two chords.

### 4. Strong induction

We prove by induction on |V|:

There exists a switching-equivalent tournament representative t' and a directed Hamiltonian path P in t' whose alpha-word has at most one change.

The statement is trivial for at most three vertices.

Fix x in V and put W=V\{x}. Start from any tournament representative of alpha. Switch a subset of W so that x becomes a sink: every vertex of W points to x. This is always possible: switch precisely those vertices v for which x originally points to v. Let the resulting representative be T_sink.

Apply induction to the subtournament T_sink[W]. We may perform further switching inside W and extend exactly the same switch to the full vertex set; x remains uniformly adjacent to W up to possibly choosing sink/source at the final step. Thus obtain a representative on W with a directed Hamiltonian path
P=(v_1,...,v_m)
whose alpha-word c has at most one change.

There are now two full representatives with the SAME subtournament on W:
- keep x as a sink;
- switch the singleton {x}, making x a source.

In the sink representative,
(v_1,...,v_m,x)
is a directed Hamiltonian path. Its only new ternary status is
alpha(v_{m-1},v_m,x)
=t(v_{m-1},v_m) xor t(v_m,x) xor t(x,v_{m-1})
=1 xor 1 xor 0
=0.
Hence its status word is c0.

In the source representative,
(x,v_1,...,v_m)
is a directed Hamiltonian path. Its only new status is
alpha(x,v_1,v_2)
=t(x,v_1) xor t(v_1,v_2) xor t(v_2,x)
=1 xor 1 xor 0
=0.
Hence its status word is 0c.

If c begins with 0, then 0c has at most one change.
If c ends with 0, then c0 has at most one change.
If c begins and ends with 1, then because c already has at most one change, c is all 1s; either 0c or c0 has exactly one change.
The empty/one-bit cases are immediate.

Therefore at least one of the source or sink extensions is NOR-good.

Since switching does not change alpha, the resulting coordinate order is a NOR-good spanning order for the ORIGINAL ternary orientation alpha.

### Theorem

Every coboundary-flat alternating ternary orientation admits a spanning coordinate order whose consecutive ternary-window word has at most one change.

Equivalently, the ternary NOR conjecture is true throughout the coboundary-flat sector.

### Article III consequence

All protected-root, threshold-band, width-two, and cellular-extraction machinery developed for this sector becomes auxiliary structure rather than a closure obligation. The direct switching induction closes the sector at the representation level.

The proof also explains why endpoint insertion repeatedly produced a forced zero phase: after choosing a switching representative, the omitted coordinate can always be made a global sink or source, and adjoining it to a directed Hamiltonian path contributes an exact zero status at the chosen endpoint.
