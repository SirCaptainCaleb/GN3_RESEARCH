# Three compatible Hamiltonian deletions concentrate in one common gap

## Statement


Let H be a boundary tournament on a vertex set K union {a,b,c}, where a,b,c are distinct. Suppose there are Hamilton paths
P_a on K union {b,c},
P_b on K union {a,c},
P_c on K union {a,b},
and suppose these three paths are pairwise compatible on their common vertices: every pair induces the same relative order on its intersection.

Then there is a common linear order C of K such that each special label x in {a,b,c} has a well-defined insertion gap g(x) in C, independent of which of the two paths containing x is used. If the three gaps are not all equal, then H[K union {a,b,c}] is Hamiltonian.

Consequently, if the full set K union {a,b,c} is non-Hamiltonian, all three labels occupy one common insertion gap of the common K-order. The only residual obstruction is therefore localized to one gap and the three labels.


## Body


Pairwise compatibility implies that the restrictions of P_a,P_b,P_c to K have one common relative order; write it as C=(k_1,...,k_m).

Fix x in {a,b,c}. The label x appears in exactly two of the three paths. Those two paths are compatible on their common domain K union {x}, so x has the same position relative to every vertex of K in both paths. Hence x determines a well-defined gap g(x) of C, with endpoint gaps allowed.

Assume the three gaps are not all equal. Construct a word W on K union {a,b,c} by starting with C and inserting each special label into its gap. If two labels share a gap, order that pair as it appears in the unique deletion path containing both. Labels placed in distinct gaps have their relative position forced by the intervening K-vertices.

Because the three labels do not all occupy one gap, no three consecutive vertices of W can consist of all three special labels. Therefore every consecutive triple of W omits at least one of a,b,c. If it omits a, it occurs as a consecutive triple of P_a; if it omits b, it occurs in P_b; if it omits c, it occurs in P_c. Pairwise compatibility ensures the constructed local order agrees with the relevant deletion path whenever two labels share a gap. Hence every consecutive triple of W is tight.

Thus W is a Hamilton path on K union {a,b,c}. The contrapositive gives the one-common-gap conclusion in the non-Hamiltonian case.
