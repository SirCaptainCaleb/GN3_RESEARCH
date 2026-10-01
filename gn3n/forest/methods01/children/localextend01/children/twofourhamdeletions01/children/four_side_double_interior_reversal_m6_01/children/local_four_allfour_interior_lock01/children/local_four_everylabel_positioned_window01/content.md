# Every label of a locally minimal four-side has a positioned interior Hamiltonian window

## Statement

Let H be a minimum counterexample and let W|P|Q be a spanning three-cover minimizing quadratic potential within its connected pairwise-repartition component, with |W|=4 and |P|,|Q|>=6. Write P° and Q° for the displayed interior paths obtained by deleting both endpoints. Then for every w in W there exists a proper Hamiltonian induced set K_w of order four or five such that w is in K_w, at least three vertices of K_w lie in V(P°) union V(Q°), and H-K_w is non-Hamiltonian with path-cover number two.

## Body

Fix w in W. By local_four_allfour_interior_lock01, w is noninsertable into every position of both displayed paths P° and Q°. Choose failed-insertion normal forms for w on both interiors.

If either obstruction is first-type, say on P°, let a,b,c be its three consecutive interior vertices. By 0425e03e2aa3, X={w,a,b,c} is either Hamiltonian or the universal cyclic non-Hamiltonian four-set. In the first case take K_w=X. In the cyclic case choose any vertex d outside X; since H has order greater than ten such a vertex exists, and the cyclic-kernel extension conclusion makes X union {d} Hamiltonian. Taking K_w=X union {d} gives a Hamiltonian five-set containing w and the three interior vertices a,b,c.

Suppose both obstructions are second-type, at gaps p|p' in P° and q|q' in Q°. By 4efbe05b945a, either there is a mixed Hamiltonian four-path on {w,p,p',q} or on {w,q,q',p}, in which case its support is K_w, or the doubled-cross alternative occurs. In the latter case let F={w,p,p',q,q'}. If F is Hamiltonian, take K_w=F. If F is non-Hamiltonian, smallset01 says that at most one four-subset of F is non-Hamiltonian. Hence among the four subsets F-{v} with v!=w at least three are Hamiltonian; choose one as K_w. In every branch K_w contains w and at least three vertices from P° union Q°.

Because |P|,|Q|>=6, H has at least sixteen vertices, so K_w is proper. Minimum-counterexample calculus gives pc(H-K_w)<=2, and H-K_w cannot be Hamiltonian because then Hamilton paths on K_w and H-K_w would form a spanning two-cover. Thus H-K_w is non-Hamiltonian with path-cover number two. Since w was arbitrary, the conclusion holds for all four labels of W.