# Fixed-target two-connector exchange switches the entrance in zero slack

## Statement

Work in the zero-slack critical-core model, and let
T_1,C_1,T_2,C_2,...,T_{c-1},C_{c-1},T_c=e
be a maximum alternating witness ending in the forest triple e through the port x=C_{c-1}∩e. Fix 1<=i<=c-2. Suppose there are DXX connectors f,g such that:
(1) f joins T_i to e at a port y∈e\{x};
(2) g joins T_{i+1} to T_1;
(3) at T_i the port of f is different from the port of C_{i-1} when i>1;
(4) at T_{i+1} the port of g is different from the port of C_{i+1} when i+1<c-1;
(5) at T_1 the port of g is different from the port of C_1;
(6) the colors of f and g are distinct and neither occurs among the retained connector colors
{col(C_1),...,col(C_{i-1}),col(C_{i+1}),...,col(C_{c-2})}.
Then there is a maximum alternating witness using all c forest triples and ending in e through y. In particular, if e is nonspecial with entrance x, no such pair f,g exists for either y∈e\{x} and any cut i.

## Body

The original witness uses the forest triples T_1,...,T_c and the connectors C_1,...,C_{c-1}, with all connector colors distinct and with distinct incident ports at every internal forest triple.

Delete the two connectors C_i and C_{c-1}. Keep the prefix connectors C_1,...,C_{i-1} and the middle/suffix connectors C_{i+1},...,C_{c-2}.

Now traverse the forest triples in the order
T_{c-1}, T_{c-2}, ..., T_{i+1}, T_1, T_2, ..., T_i, e.
Between consecutive triples use:
- the old connectors C_{c-2},C_{c-3},...,C_{i+1} along the reversed first block;
- the new connector g from T_{i+1} to T_1;
- the old connectors C_1,...,C_{i-1} along the forward second block;
- the new connector f from T_i to e.

This visits every forest triple exactly once and uses exactly c-1 connectors, so the lifted hypergraph sequence has 2c-1 edges, the same maximum length as the original witness.

Linearity follows from the stated port and color conditions. Distinct forest triples are disjoint. Every connector has its two X-endpoints in its designated adjacent forest triples. At internal triples inherited from the old witness, the two incident old connector ports remain distinct. At T_{i+1},T_1,T_i the explicit safe-port assumptions ensure the new connector is disjoint from the nonadjacent retained connector. Distinct connector colors mean their D-vertices are distinct, so nonconsecutive connectors do not meet in D. The two new connectors have distinct colors and distinct endpoint triples, hence are disjoint from one another.

Finally f meets e at y, so the resulting maximum witness ends in e through y. If y differs from the unique entrance x of a nonspecial e, this is impossible.

Therefore nonspeciality of a zero-slack forest triple is equivalent to the simultaneous failure of this entire family of fixed-target 2-opt moves.