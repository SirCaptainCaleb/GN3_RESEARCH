# Compatible deletion pairs reduce to endpoint reversal or a bounded singleton-swap residue

## Statement

Let H be a minimum counterexample, and let F_a,F_b be fully compatible exact two-covers of H-a and H-b. Use the compatible-pair localization of 1000694, so the two omitted labels insert into one common ordered class P and the other common class Q is unchanged.

If the insertion slots are adjacent, write P=(L,z,R) and, after naming the labels suitably,
F_b=(L,a,z,R)|Q,   F_a=(L,z,b,R)|Q.
Then H has the two spanning three-covers
(L,a)|(z,b,R)|Q
and
(L,a,z)|(b,R)|Q.
They differ only by transferring z between the first two components; z is a terminal endpoint in (L,a,z) and an initial endpoint in (z,b,R). Hence singleton_transfer_endpointization01 forces an explicit displayed component-end reversal. Moreover, if l=|L| and r=|R|, the quadratic-potential difference from the first cover to the second is 2(l-r).

If the insertion slots are identical, write P=(L,R) and
F_b=(L,a,R)|Q,   F_a=(L,b,R)|Q.
Then H has the Phi-neutral singleton-swap pair
(L,a)|(b,R)|Q
and
(L,b)|(a,R)|Q.
If |L|,|R|>=2, terminal_singleton_swap_k4_residue01 reduces this pair to a proper Hamiltonian four-support with non-Hamiltonian path-cover-two complement or to the explicit six-vertex paired matching-block endpoint residue. If exactly one flank has order at least two, the corresponding four-set on a,b and the two nearest flank vertices is either Hamiltonian or a single matching-block K4 by the common-pair four-set classification; if both flanks have order at most one, the entire insertion support P union {a,b} has order at most four.

Together with 1000694's direct two-cover conclusions for different insertion classes or slots separated by at least two, every fully compatible deletion pair is therefore consumed by a spanning two-cover, an explicit endpoint reversal, or a bounded same-slot singleton-swap/K4 residue.

## Body

By 1000694, fully compatible exact deletion covers of H-a and H-b have two common ordered support classes P,Q. Both omitted labels insert into P, and either their slots coincide or are adjacent unless H already has a spanning two-cover.

Adjacent slots. Write P=(L,z,R) and
F_b=(L,a,z,R)|Q,
F_a=(L,z,b,R)|Q.
Every displayed subpath of either cover is tight. Therefore
C_0=(L,a)|(z,b,R)|Q
and
C_1=(L,a,z)|(b,R)|Q
are spanning three-covers of H. Put X=V(L) union {a}, Y={b} union V(R), D=V(Q), and x=z. In C_1 the Hamilton path on X union {z} ends at z, while in C_0 the Hamilton path on Y union {z} begins at z. These are opposite endpoint realizations of the transferred singleton z. Since pc(H)>2, singleton_transfer_endpointization01 applies and produces an explicit tight triple reversing the terminal edge of a displayed Hamilton component.

The same construction records an exact potential identity. If l=|L| and r=|R|, then the two changing component-size pairs are
(l+1,r+2) and (l+2,r+1),
so
Phi(C_1)-Phi(C_0)
=(l+2)^2+(r+1)^2-(l+1)^2-(r+2)^2
=2(l-r).
Thus the adjacent-slot obstruction is simultaneously an endpoint-reversal producer and a one-vertex balancing move.

Identical slot. Write the common path as P=(L,R), where the common insertion gap lies between L and R, allowing either flank to be empty, and
F_b=(L,a,R)|Q,
F_a=(L,b,R)|Q.
Taking tight prefixes and suffixes gives spanning three-covers
C_a=(L,a)|(b,R)|Q,
C_b=(L,b)|(a,R)|Q.
The two changing component orders are the same in both covers, namely |L|+1 and |R|+1, so this is Phi-neutral. It is exactly the terminal singleton support swap with labels a,b and unchanged third path Q.

When |L|,|R|>=2, the displayed orders are the hard same-end orientation in terminal_singleton_swap_k4_residue01. Hence either one endpoint four-set is Hamiltonian, giving a proper Hamiltonian four-support with non-Hamiltonian path-cover-two complement by minimum-counterexample calculus, or both endpoint four-sets form the explicit paired six-vertex matching-block residue with {a,b} lowest at the left end and highest at the right end.

If only one flank has order at least two, use its two nearest vertices. For example, if R begins (c,d,...) then both (a,c,d) and (b,c,d) are tight. The common-pair four-set classification, applied after reversal if needed, says {a,b,c,d} is either Hamiltonian or an edge-orderable matching-block K4. The left-flank case is symmetric. If neither flank has order at least two, |P union {a,b}|<=4, so the obstruction is already bounded.

Thus the compatible-pair branch of the defect-span interface reduces completely to standard bridge inputs: direct two-cover, endpoint reversal, or a bounded same-slot kernel.
