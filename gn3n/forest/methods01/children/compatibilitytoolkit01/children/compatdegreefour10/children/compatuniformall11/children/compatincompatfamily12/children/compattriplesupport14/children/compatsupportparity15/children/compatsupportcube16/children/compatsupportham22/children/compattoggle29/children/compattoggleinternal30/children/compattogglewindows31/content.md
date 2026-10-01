# The one-split toggle compresses to four bounded insertion-obstruction windows

## Statement

In the one-split toggle of compattoggle29, choose arbitrary Hamilton paths P_R on R, P_S on S, P_{R+a} on R union {a}, and P_{S+b} on S union {b}. Then the failed-insertion normal form of insert01 applies simultaneously to b on P_R, a on P_S, c on P_{R+a}, and c on P_{S+b}. Hence the entire one-split residue is witnessed by four bounded local obstruction windows, each involving the failed label and at most four consecutive vertices of the relevant Hamilton path. In particular the same label c carries two bounded obstruction windows on disjoint Hamiltonian supports.

## Body

# Proof

By compattoggle29 and compattoggleinternal30,

R is Hamiltonian and R union {b} is non-Hamiltonian,
S is Hamiltonian and S union {a} is non-Hamiltonian,
R union {a} is Hamiltonian and R union {a,c} is non-Hamiltonian,
S union {b} is Hamiltonian and S union {b,c} is non-Hamiltonian.

Choose arbitrary Hamilton paths

P_R on R,
P_S on S,
P_{R+a} on R union {a},
P_{S+b} on S union {b}.

Since adjoining b to R gives a non-Hamiltonian induced subtournament, b cannot be inserted into any position of P_R. Likewise a cannot be inserted into P_S, and c cannot be inserted into either P_{R+a} or P_{S+b}.

Apply Section 3 of insert01 separately to these four path/label pairs. For each pair the theorem produces an index t and one of its two certified obstruction types:

1. a first-type comparison 3-cycle supported on the failed label and three consecutive path vertices; or
2. a second-type pivot pattern supported on the failed label and at most four consecutive path vertices.

Thus the one-split branch contains four bounded obstruction windows:

W_R(b),
W_S(a),
W_{R+a}(c),
W_{S+b}(c).

The final two share the same failed label c while lying on disjoint supports R union {a} and S union {b}. No assumption is made that their obstruction types or local indices coincide.

Therefore the arbitrary sizes of R and S disappear from the immediate obstruction data: all failure is compressed to four constant-size windows, with c synchronized across the two cores.