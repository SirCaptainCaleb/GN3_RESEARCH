# Compatible one-label path extensions glue outside one common gap

## Statement

Let H be a boundary tournament. Let K be a vertex set and let x,y be distinct vertices outside K. Suppose P_x is a tight Hamilton path on K union {x} and P_y is a tight Hamilton path on K union {y}, and the vertices of K occur in the same relative order in P_x and P_y. Write that common order as
C=(c_1,...,c_m).
Then P_x and P_y are obtained by inserting x and y into two gaps g_x,g_y of C, with endpoint gaps allowed.

(1) If |g_x-g_y|>=2, then K union {x,y} is Hamiltonian: inserting both x and y into C at their respective gaps gives a tight Hamilton path.

(2) If g_x,g_y are adjacent, with common core vertex c between them, then the simultaneous merged order has every consecutive triple tight except possibly the unique triple containing x,c,y. Hence either K union {x,y} is Hamiltonian or the reverse triple through c is tight.

(3) If g_x=g_y is an internal gap u|v, then both (u,x,v) and (u,y,v) are tight, so {u,v,x,y} is Hamiltonian.

Thus if K union {x,y} is non-Hamiltonian and no reverse-cross or Hamiltonian-four witness occurs, x and y must occupy one common endpoint gap of the compatible core order; equivalently P_x and P_y are two same-end extensions of the same tight core path C.

## Body

Because P_x and P_y induce the same relative order on K and each has only one vertex outside K, each is obtained from the common word C by inserting its exceptional vertex in one gap.

Assume first that |g_x-g_y|>=2. Form the word W by inserting both x and y into C at those two gaps. No three consecutive vertices of W contain both x and y. Therefore every consecutive triple of W omits at least one of {x,y}. If it omits y, it is a consecutive triple of P_x; if it omits x, it is a consecutive triple of P_y. Hence every consecutive triple of W is tight, so W is a Hamilton path on K union {x,y}.

Now suppose the gaps are adjacent. After symmetry the local merged word has the form
...,x,c,y,...
for the unique common core vertex c between the two gaps. Every consecutive triple of the merged word except (x,c,y) omits x or y and is inherited from P_y or P_x as above. If (x,c,y) is tight, the merged word is Hamiltonian. Otherwise boundary antisymmetry gives the reverse tight triple (y,c,x).

Finally suppose the two gaps coincide at an internal core edge u|v. Then P_x contains (u,x,v) and P_y contains (u,y,v) as consecutive tight triples. The certified parallel-middle lemma in localextend01 implies that H[{u,v,x,y}] is Hamiltonian.

If the common gap is an endpoint gap, deleting x from P_x (equivalently y from P_y) leaves C as a contiguous suffix or prefix, so C itself is tight and P_x,P_y are two same-end extensions of that common tight path. This is exactly the only residual geometry not already consumed by (1)-(3).
