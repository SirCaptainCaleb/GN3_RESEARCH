# The one-split double-pivot branch is exactly a deletion-state cross-swap obstruction

## Statement

In the exactly-one-split compatibility branch, put A=R union {a} and B=S union {b}. Then A|B is the chosen deletion cover of H-c. After the first-type outcomes of compattogglepivot32 are excluded, c has a second-type failed-insertion pivot on each component. If either pivot is at the first or last gap, d26c575019cc reduces that side to a Hamiltonian four-window or an explicit non-Hamiltonian matching-block K4. If both pivots are interior, write Hamilton orders A=(u_0,...,u_m), B=(v_0,...,v_s), with pivots u_i|u_{i+1} and v_j|v_{j+1}. Then the certified pivot-pivot cross-swap theorem applies and forces both of the following clauses:

(C1) at least one of
(v_{j+1},c,u_i),
(u_{i+1},v_j,v_{j-1}),
(u_{i+2},u_{i+1},v_j)
is tight;

(C2) at least one of
(u_{i+1},c,v_j),
(v_{j+1},u_i,u_{i-1}),
(v_{j+2},v_{j+1},u_i)
is tight.

Thus the genuinely new one-split branch is reduced to two explicit constant-size cross-swap obstruction clauses on one deletion cover.

## Body

# Proof

In the normalized one-split branch, compatsupportham22 gives A=R union {a} Hamiltonian and B=S union {b} Hamiltonian. The sets A and B are disjoint and their union is V(H)-{c}. Hence

H-c = A | B

is a deletion two-cover.

By compattogglepivot32, after excluding the first-type four-kernel outcomes, the failed-insertion obstruction for c on each of the two chosen Hamilton orders is second-type.

If one pivot occurs at the first or last gap of its component, apply the certified boundary-pivot theorem d26c575019cc to the deletion cover H-c=A|B. It gives the stated Hamiltonian-four-window or explicit matching-block K4 alternative.

Assume therefore both pivots are interior. Write the displayed Hamilton orders as

A=(u_0,...,u_m),
B=(v_0,...,v_s),

with interior pivot gaps u_i|u_{i+1} and v_j|v_{j+1}. The hypotheses are now exactly those of the certified pivot-pivot cross-swap theorem in transport01, with omitted label x there replaced by c.

For the first cross-swap, a spanning two-cover would result if all three join triples

(u_i,c,v_{j+1}),
(v_{j-1},v_j,u_{i+1}),
(v_j,u_{i+1},u_{i+2})

were tight. Since H has no spanning two-cover, at least one is non-tight. Boundary antisymmetry therefore makes at least one of the reversed triples

(v_{j+1},c,u_i),
(u_{i+1},v_j,v_{j-1}),
(u_{i+2},u_{i+1},v_j)

tight. This is (C1).

For the opposite cross-swap, simultaneous tightness of

(v_j,c,u_{i+1}),
(u_{i-1},u_i,v_{j+1}),
(u_i,v_{j+1},v_{j+2})

would again give a spanning two-cover. Hence at least one of their reverses

(u_{i+1},c,v_j),
(v_{j+1},u_i,u_{i-1}),
(v_{j+2},v_{j+1},u_i)

is tight. This is (C2).

All triples lie in the two pivot neighborhoods together with c, so the arbitrary sizes of R,S disappear completely from the unresolved cross-swap obstruction.
