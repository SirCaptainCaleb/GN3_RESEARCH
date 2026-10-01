# Hamiltonian four-windows force common-top bounded square disturbances

## Statement


For every n-vertex boundary tournament J, at least (2/5) binom(n,4) of its four-vertex subsets are Hamiltonian. Consequently some three-set C in J has a Hamiltonian extension set
Y={y notin C : C union {y} is Hamiltonian}
with |Y| >= ceil(2(n-3)/5).

Now let H be a minimum counterexample of order n. Besides applying the preceding global construction to H, one has an anchored construction from any prescribed Hamiltonian four-set W: there exist C contained in W and Y disjoint from C, with W=C union {y_0} for some y_0 in Y,
|Y| >= 1+ceil((n-4)/4),
and C union {y} Hamiltonian for every y in Y.

For either construction in H, put G=H-C and define Gamma on Y by yz in E(Gamma) exactly when C union {y,z} is Hamiltonian. Then alpha(Gamma)<=2,
|E(Gamma)| >= floor((|Y|-1)^2/4),
and every edge yz gives a full path-cover-two square
G, G-y, G-z, G-{y,z}.

Hence either some edge yields simultaneous endpoint exposure in a two-cover of G, two two-covers of G have different support partitions, or two corresponding common-support Hamilton paths have an order disagreement; or there is I subseteq Y, |I|>=|Y|-2, whose vertices are internal in every two-cover of G.

In the last case, put s=|I| and assume s>=5. For every displayed two-cover P|Q of G there is an edge yz of Gamma with y,z internal on one displayed path and displayed distance at most
floor(2(|V(G)|-5)/(s-4)).
If y,z are nonadjacent, let M be the nonempty displayed subpath strictly between them. Then every two-cover T of G-{y,z} has an ordinary path edge crossing V(M) to its complement.

Writing the top path as P=(L,y,M,z,R), with M=(m_1,...,m_h), every such lower two-cover T satisfies at least one of:
(1) at least three T-edges join different members of V(L),V(M),V(R),V(Q);
(2) T has an order disagreement with one of the inherited paths L,M,R,Q;
(3) h=1;
(4) there is a proper Hamiltonian five-set whose complement in H is non-Hamiltonian with path-cover number two;
(5) at one end of M there are explicit doubled reverse endpoint triples: for a crossing neighbor a immediately before M, both (m_1,a,y) and (m_1,y,a) are tight, or for a crossing neighbor b immediately after M, both (b,z,m_h) and (z,b,m_h) are tight.

Thus dense Hamiltonian four-window structure reduces, in one theorem, to a common-top disturbance or to a bounded local lower-square obstruction. In the global construction on H, with N=|V(G)|, s>=ceil(2N/5)-2, so for N>=16 the displayed distance above is at most floor(2(N-5)/(ceil(2N/5)-6)).


## Body


Every five-set contains at least two Hamiltonian four-subsets: a Hamiltonian five-set has at least two Hamiltonian vertex deletions, while a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset. Double-counting incidences between Hamiltonian four-sets and containing five-sets gives
h_4(n-4) >= 2 binom(n,5),
hence h_4 >= (2/5)binom(n,4). Counting incidences between three-sets C and Hamiltonian four-sets C+y then gives average extension count at least 2(n-3)/5, proving route (A).

For route (B), fix a Hamiltonian four-set W. For each x outside W, apply the same five-set deletion facts to W+x. Some replacement (W-{d_x})+x is Hamiltonian. Pigeonholing d_x over the four vertices of W gives one d used for at least ceil((n-4)/4) labels. Put C=W-{d} and adjoin d itself to those labels to obtain Y.

Now use either route. For three distinct y,z,t in Y, the six-set C+{y,z,t} has at least four Hamiltonian five-subsets. Therefore not all of C+{y,z}, C+{y,t}, C+{z,t} can be non-Hamiltonian. Thus every three vertices of Y span an edge of Gamma, so alpha(Gamma)<=2. Mantel's theorem gives
|E(Gamma)| >= binom(|Y|,2)-floor(|Y|^2/4)=floor((|Y|-1)^2/4).

For yz in E(Gamma), the four sets C, C+y, C+z, C+{y,z} are Hamiltonian and proper. Minimum-counterexample calculus makes their complements G, G-y, G-z, G-{y,z} non-Hamiltonian with path-cover number two. Apply the certified two-label square normal form to every edge. If endpoint exposure, support-partition disagreement, or order disagreement occurs, we are done. Otherwise each edge has a universally internal endpoint. The set I of all universally internal labels is a vertex cover of Gamma; because alpha(Gamma)<=2, |I|>=|Y|-2.

Fix a two-cover P|Q of G. If a displayed path R of order m contains k>=3 labels of I at internal positions
2<=a_1<...<a_k<=m-1,
then
sum_{i=1}^{k-2}(a_{i+2}-a_i)
=a_{k-1}+a_k-a_1-a_2 <= 2(m-4).
Hence some three consecutive I-labels on R have span at most 2(m-4)/(k-2). Combining the two displayed paths when both contain at least three I-labels, or using that the other path contains at most two otherwise, yields three I-labels on one path in span at most
2(N-5)/(s-4),
where N=|V(G)| and s=|I|. Since alpha(Gamma)<=2, two of the three form an edge yz of Gamma. Their displayed distance satisfies the same bound.

If y,z are adjacent, this is already a same-path internal square edge. Otherwise write their displayed segment as (y,M,z). Let T be any two-cover of G-{y,z}. If no T-edge crossed V(M) to its complement, every T-component meeting M would lie wholly in M. Since T has two components, one would then have support exactly V(M), and replacing it by the inherited tight path (y,M,z) would give a two-cover of G with y,z displayed as endpoints, contradicting their universal internality. Thus every lower cover crosses the cut.

Write P=(L,y,M,z,R), M=(m_1,...,m_h), with L,M,R,Q all nonempty in the nonadjacent case under consideration. The transition-count inequality for the four inherited classes gives at least two cross-class T-edges. If there are at least three, outcome (1) holds. With exactly two, equality makes each inherited class one intact T-block. Any reversed inherited block gives outcome (2). Assume instead inherited order on all four blocks. If h=1, outcome (3) holds.

For h>=2, one of the two crossing edges is incident with an end of the M-block. Suppose a crossing enters M from a vertex a. Then (a,m_1,m_2) is tight in T and (y,m_1,m_2) is tight in the top path. Choose q=m_3 when h>=3 and q=z when h=2; then (m_1,m_2,q) is tight. The certified same-end-extender lemma applied to (m_1,m_2), left extenders a,y, and right extender q gives either a Hamiltonian five-set {a,y,m_1,m_2,q}, whose complement is path-cover-two by minimum-counterexample calculus, or both (m_1,a,y) and (m_1,y,a) tight. These are outcomes (4) and (5). A crossing leaving M is symmetric, using the right-end form of the same lemma and yielding either a Hamiltonian five-set or both (b,z,m_h) and (z,b,m_h).

Finally, in route (A), N=n-3 and |Y|>=ceil(2N/5), so s>=ceil(2N/5)-2, giving the displayed explicit global distance bound.
