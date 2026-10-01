# Complete pair-extension over one core forces a triple enlargement or a Hamiltonian exterior four-set

## Statement

Let H be a boundary tournament, let K be a vertex set, and let E={a,b,c,d} be four vertices disjoint from K. Suppose that for every unordered pair {x,y} subset E there is a Hamilton path P_{xy} on K union {x,y}. Then at least one of the following holds:

(1) two of the six chosen paths P_{xy} induce different relative orders on their common vertices;

(2) for some three-set T subset E, H[K union T] is Hamiltonian;

(3) H[E] is Hamiltonian.

More precisely, if the six pair-extension paths are pairwise order-compatible on all intersections and every K union T with |T|=3 is non-Hamiltonian, then there is one common linear order C on K and one common insertion gap of C used by all four labels. Orient each pair x,y by x->y when P_{xy} places x before y in that gap. If e_1->e_2->e_3->e_4 is any directed Hamilton path of this precedence tournament, then
(e_4,e_3,e_2,e_1)
is a tight Hamilton path on E.

## Body

Assume outcome (1) does not occur. Then all six chosen paths induce one common relative order C on K.

Fix x in E. For any two distinct y,z in E-{x}, the paths P_{xy} and P_{xz} are compatible on K union {x}. Hence x has the same position relative to every vertex of K in both paths. Thus x determines a well-defined insertion gap g(x) of C, with endpoint gaps allowed.

Consider any triple T={x,y,z} subset E. Suppose the three gaps g(x),g(y),g(z) are not all equal. Construct an ordering W_T of K union T by starting from C and inserting x,y,z into their respective gaps; whenever two labels share one gap, order that pair as it appears in their pair path P_{xy}, P_{xz}, or P_{yz}.

Because the three labels do not all occupy one gap, no three consecutive vertices of W_T can consist entirely of x,y,z. Hence every consecutive triple of W_T omits at least one of the three special labels. If it omits z, its local order occurs in P_{xy}; if it omits y, it occurs in P_{xz}; if it omits x, it occurs in P_{yz}. Compatibility guarantees that these inherited local orders agree with W_T. Therefore every consecutive triple of W_T is tight, and H[K union T] is Hamiltonian.

Consequently, if outcome (2) also fails, then for every triple T subset E the three gaps of its labels are equal. Overlapping triples force
g(a)=g(b)=g(c)=g(d)=:g.

Now define a tournament T_E on E by orienting x->y exactly when P_{xy} places x before y in the common gap g. Every finite tournament has a directed Hamilton path; choose
e_1->e_2->e_3->e_4.

Consider the triple {e_1,e_2,e_3}. The pair paths P_{e_1e_2}, P_{e_1e_3}, P_{e_2e_3} all place their labels in the same gap and induce the pair precedence e_1->e_2->e_3 along a directed Hamilton path of T_E. If the ordered triple (e_1,e_2,e_3) were tight, inserting the block e_1,e_2,e_3 into the common gap of C would give a Hamilton path on K union {e_1,e_2,e_3}, contradicting failure of outcome (2). Hence (e_1,e_2,e_3) is non-tight, so boundary antisymmetry gives
(e_3,e_2,e_1)
tight.

The same argument for {e_2,e_3,e_4} gives
(e_4,e_3,e_2)
tight.

Therefore
(e_4,e_3,e_2,e_1)
is a tight Hamilton path on E. This is outcome (3).
