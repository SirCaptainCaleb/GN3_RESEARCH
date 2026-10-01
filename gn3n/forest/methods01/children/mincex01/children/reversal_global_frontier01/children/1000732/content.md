# A complete reverse fan yields a positioned Hamiltonian five-side with an inherited complementary two-cover

## Statement

Let H be a minimum counterexample and let T=(x,v,u) be a tight three-vertex path belonging to the complete reverse-fan branch of the bounded reversal frontier. Put L=H-V(T), and choose any displayed two-cover A|B of L.

Let E be the set of distinct displayed endpoints of A and B. Then there exist distinct e,f in E such that W=V(T) union {e,f} is Hamiltonian. Moreover deleting e and f from the displayed paths A,B leaves exactly two nonempty inherited tight-path fragments whose supports partition H-W. Thus W|P|Q is a spanning three-cover of H with |W|=5 and P|Q a displayed two-cover of H-W.

In particular the reverse-fan residue always enters the five-side transport machinery in a position tied to endpoints of a known complementary two-cover.

## Body

Because T is a proper Hamiltonian three-vertex support, H-V(T)=L cannot be Hamiltonian: otherwise T together with a Hamilton path of L would two-cover H. By minimality, L has path-cover number two, so choose a displayed two-cover A|B.

Since |V(H)|>10, |L|>=8. Hence A and B cannot both be singletons, and the set E of distinct displayed endpoints has order at least three.

Use the certified fixed-three-path extension consequence of smallset01: for a tight three-path T and any three distinct exterior vertices a,b,c, at least one of T union {a,b}, T union {a,c}, T union {b,c} is Hamiltonian. Apply this to any three distinct vertices of E. We obtain distinct endpoints e,f in E such that
W=V(T) union {e,f}
is Hamiltonian.

Delete e and f from the displayed paths A and B. Since e,f are displayed endpoints, every surviving nonempty piece is an inherited tight path, and there are at most two such pieces. Their supports partition H-W.

If fewer than two nonempty pieces survived, then H-W would itself be Hamiltonian (the empty-complement case is impossible here because |L|>=8). A Hamilton path on W together with a Hamilton path on H-W would then two-cover H, contradiction. Therefore exactly two nonempty inherited pieces survive. They form a displayed two-cover P|Q of H-W.

Equivalently, the Hamiltonian five-set is not merely a bare small-support witness: it is positioned by deleting two displayed endpoints of a known two-cover of its complement. No path reversal or cyclic permutation is used.
