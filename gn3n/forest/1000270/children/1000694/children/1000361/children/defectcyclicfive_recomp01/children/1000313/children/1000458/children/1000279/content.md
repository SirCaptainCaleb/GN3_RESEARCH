# Every deletion state has a central five-bridge or an outer reversed four-side

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion two-cover, with P=(p_0,...,p_m), Q=(q_0,...,q_s), m,s>=2. Then at least one of the following holds.

(1) Central five-bridge: (p_m,x,q_0) is non-tight, and C=(q_1,q_0,x,p_m,p_{m-1}) is a tight five-path. Thus P^{--}|C|Q^{++} is the canonical central five-bridge cover.

(2) Outer four-side: both cyclic wrap triples (q_{s-1},q_s,p_0) and (q_s,p_0,p_1) are non-tight, and S=(p_1,p_0,q_s,q_{s-1}) is a tight four-path with pc(H-S)=2.

In particular, if the canonical central bridge has order three, then the outer reversed four-side necessarily exists.

## Body

The triples (p_{m-1},p_m,x) and (x,q_0,q_1) are non-tight, since otherwise x could be appended to P or prepended to Q and the other deletion-cover component would give a spanning two-cover. If the middle join (p_m,x,q_0) is non-tight, boundary antisymmetry gives (q_0,x,p_m) tight; together with the reversal mates (q_1,q_0,x) and (x,p_m,p_{m-1}), this is exactly the central five-path of centralbridge35, proving (1).

Assume instead that (p_m,x,q_0) is tight. At least one cyclic wrap triple at Q|P is non-tight, for if both were tight then the concatenation QP would be a tight path and QP|{x} would two-cover H. Suppose exactly one wrap triple were non-tight. Every other cyclic triple lies wholly inside P or Q and is tight. Hence the cyclic defect graph of the singleton lift P|{x}|Q would consist precisely of the two isolated forced defects at (p_{m-1},p_m,x) and (x,q_0,q_1), together with one isolated wrap defect: run type {1,1,1}. This contradicts the certified deletion-singleton exit theorem 8ededbb50716. Therefore both wrap triples are non-tight. Their reversal mates (p_0,q_s,q_{s-1}) and (p_1,p_0,q_s) are tight, so S=(p_1,p_0,q_s,q_{s-1}) is a tight four-path. Since S is a nonempty proper Hamiltonian support in a minimum counterexample, pc(H-S)=2. This proves (2).
