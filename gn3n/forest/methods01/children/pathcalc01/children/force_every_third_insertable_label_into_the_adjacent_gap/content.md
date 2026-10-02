# Two endpoint extenders force every third insertable label into the adjacent gap

## Statement

Let H be a boundary tournament and let R=(r_1,...,r_m), m>=2, be a tight path. Let a,b,c be distinct exterior vertices. Suppose both (a,R) and (b,R) are tight. If c is insertable into the displayed order of R at any gap other than the first two gaps (before r_1 or between r_1,r_2), then H[V(R) union {a,b,c}] is Hamiltonian. Equivalently, if that induced support is non-Hamiltonian and a,b both left-extend R, every insertion gap of c lies in {0,1}. Symmetrically, if a,b both right-extend R and the union is non-Hamiltonian, every insertion gap of c lies in the last two gaps {m-1,m}.

## Body

Index the gaps of R by 0,1,...,m, with gap 0 before r_1, gap j after r_j for 1<=j<=m-1, and gap m after r_m.

Assume a and b both left-extend R. Suppose c is insertable at a gap j>=2. Let R_c be the tight path obtained by inserting c at that gap. Because j>=2, the first two vertices of R_c are still r_1,r_2.

On the three-set {a,b,r_1}, after possibly interchanging a,b, boundary antisymmetry lets us choose the order so that
(a,b,r_1)
is tight.

Now consider
(a,b,R_c).
Its first triple (a,b,r_1) is tight by choice. Its next triple
(b,r_1,r_2)
is tight because (b,R) is tight. Every remaining consecutive triple lies inside R_c and is tight by the assumed insertion of c. Hence (a,b,R_c) is a Hamilton tight path on V(R) union {a,b,c}.

Therefore, if that support is non-Hamiltonian, c cannot be insertable at any gap j>=2; every insertion gap of c lies in {0,1}.

The right-end statement is symmetric. If a,b right-extend R and c is insertable at gap j<=m-2, let R_c be the corresponding inserted path. Its last two core vertices remain r_{m-1},r_m. Order a,b so that (r_m,a,b) is tight; whichever of a,b is placed first right-extends R. Then
(R_c,a,b)
is a Hamilton tight path. Hence, in a non-Hamiltonian union, every insertion gap of c lies in {m-1,m}. ∎