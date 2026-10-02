• [1000297] Brainstorms
    STATEMENT
    ‹none›

  • [1000075] Link-forest compression via the 2-shadow
      STATEMENT
      Exploit linearity to encode a 3-uniform linear hypergraph H by its 2-shadow graph G together with the unique hyperedge label on each shadow edge. Seek a theorem of the form: if H contains no loose path of length l, then after deleting o(n) exceptional vertices, G admits an orientation or forest decomposition in which each hyperedge contributes a labeled triangle and every sufficiently long ordinary graph path with pairwise compatible labels lifts to a loose hypergraph path. Prove a density bound on such labeled-triangle systems directly, aiming to force a liftable path at shadow average degree below the current hypergraph threshold.

    • [1001231] Linear paths are strong rainbow paths in the symmetric 2-shadow coloring
        STATEMENT
        Let H be a finite linear 3-uniform hypergraph. Form its 2-shadow G on V(H), and for every shadow edge xy color xy by the third vertex z of the unique hyperedge {x,y,z}. Then this edge-coloring is proper and satisfies the symmetric triangle rule c(xy)=z iff {x,y,z} is a hyperedge, equivalently the triangle xyz has colors z,y,x on xy,xz,yz. A graph path x_0x_1...x_k in G corresponds to a k-edge linear hypergraph path in H if and only if the 2k+1 vertices x_0,...,x_k,c(x_0x_1),...,c(x_{k-1}x_k) are all distinct. Moreover e(G)=3|E(H)|. Consequently H is P_ell-free exactly when this symmetric triangle-colored shadow contains no length-ell path whose path vertices and edge-colors are mutually distinct, and the target |E(H)|<=n ell/3 is equivalent to e(G)<=n ell for this special colored-graph class.

    • [1001234] Repeated hub colors obstruct extraction from an arbitrary long shadow path
        STATEMENT
        For every t there is a linear 3-graph H_t whose 2-shadow contains the graph path x_0x_1...x_t, while every linear hypergraph path in H_t has at most four edges. Namely, with two additional vertices z,w, take e_i={x_{i-1},x_i,z} for odd i and e_i={x_{i-1},x_i,w} for even i. Thus no argument for the 2-shadow route can rely only on extracting a positive fraction of an arbitrary ordinary shadow path; repeated color/hub structure must be used rather than discarded.

  • [1000151] High-degree hub / bounded-core dichotomy
      STATEMENT
      Prove a structural dichotomy for P_l-free linear triple systems: either a positive fraction of edges lie in stars centered at a small set S of high-degree vertices, in which case remove S and charge star edges sharply using linearity; or the remaining hypergraph has maximum degree O(l) and sufficiently large average degree to force a loose path by an expansion argument. Optimize the threshold defining S so that the two cases meet below the current 43/48 leading coefficient.

  • [1000578] Random endpoint exposure and entropy charging
      STATEMENT
      Randomly order the vertices and expose each hyperedge through its earliest vertex, producing a random assignment of every edge to one endpoint. For a longest loose path P, analyze the probability that an assigned off-path edge creates a legal extension or splice at the first exposed contact with P. Average over the random order to obtain a global inequality in which an edge that is locally 'bad' for one endpoint is unlikely to be bad for all three endpoints simultaneously. Seek an expectation bound that replaces deterministic minimum-rank assignment and yields a smaller average congestion constant.

  • [1000981] Clique-cover induced-path threshold
      STATEMENT
      Pass completely to the edge-intersection graph G of the linear 3-graph, with every adjacency colored by the unique shared hypergraph vertex. Thus E(G) is partitioned into color-cliques, every vertex of G lies in exactly three such cliques, and a linear hypergraph path corresponds to an induced graph path whose consecutive edge-colors are distinct. Conjecture that any such 3-clique-covered graph with average color-clique incidence above 3(l-c) for some absolute c>3/2 contains an induced l-vertex path with distinct consecutive colors. Prove this directly as a graph theorem, bypassing longest-hyperpath charging.

  • [1000312] Nonbacktracking incidence expansion
      STATEMENT
      Use the bipartite incidence graph B between hypergraph vertices and hyperedges. It is C4-free and every hyperedge-node has degree 3. Seek a pruning lemma giving a subgraph with minimum left-to-right branching whenever m/n exceeds (1-epsilon)l. Then grow nonbacktracking alternating walks from an edge-node. Conjecture that in a C4-free bipartite graph with right degree 3, sufficiently large average branching over l layers forces an alternating path whose right vertices correspond to pairwise nonintersecting nonconsecutive hyperedges, hence a linear P_l.

  • [1001129] Small-core or cheap-peeling dichotomy
      STATEMENT
      Conjecture a structural dichotomy for P_l^(3)-free linear 3-graphs: either there is a vertex of degree at most l-c for some fixed c>3/2, or there is a set S of O(l) vertices meeting a positive fraction of all edges in a way that leaves every component of H-S with bounded edge/vertex ratio strictly below l-3/2. Iterating the low-degree deletion outside the exceptional cores would give a global density bound with an improved leading coefficient.

• [1000846] Leading terms for 3-uniform linear path Turán numbers
    STATEMENT
    Improve the leading terms in the general-length bounds for ex_L(n,P_l^(3)), with the supplied source bound ex_L(n,P_l^(3)) <= (l-3/2)n as the current internal upper benchmark; pursue either upper- or lower-bound improvements for general l.

  • [1000192] Project guidance, literature, and proof-replacement program
      STATEMENT
      Organizational route for project-level guidance, literature state, and the program replacing computational evidence with durable human proofs.

    • [1000802] Current project guidance: general length, post-P4
        STATEMENT
        Treat the general-length 3-uniform problem as the live target. Keep the Devine–Milans bound (ell-3/2)n as the internal upper benchmark; treat P4 as solved literature, and P5 as an exact calibration point rather than the frontier.

    • [1000144] Literature state for linear hypergraph paths
        STATEMENT
        Current external results relevant to the general 3-uniform linear-path Turán problem, through 2026-09-21.

      • [1000033] Gyárfás–Ruszinkó–Sárközy (2022): acyclic triple systems
          STATEMENT
          For linear triple systems, ex_L(n,P_k) <= 1.5 k n for every k,n. Also ex_L(n,P_2)=floor(n/3), ex_L(n,P_3)<=n with equality iff the system is a disjoint union of Fano planes, and ex_L(n,P_4)<=4n/3 with equality iff it is a disjoint union of affine planes of order 3.

      • [1001063] Győri–Salia (2025): linear 3-graphs without long Berge paths
          STATEMENT
          If an n-vertex linear 3-graph contains no Berge path of length k>=4, then it has at most (k-1)n/6 hyperedges; the bound is sharp for infinitely many k,n.

      • [1000935] Zhou–Yuan (2025): general r-uniform path upper bound
          STATEMENT
          For r>=3 and ell>=4, ex_r^lin(n,P_ell^r) <= ((2r-3)ell/2)n.

      • [1000165] Ma–Hou–Gao (2020): minimum degree and long linear paths in general 3-graphs
          STATEMENT
          Yue Ma, Xinmin Hou and Jun Gao proved asymptotically sharp vertex-degree thresholds in general 3-uniform hypergraphs for forcing linear paths of prescribed length. For k>=0, sufficiently large n, δ_1(H)>=kn+6k^2-3k+3 forces P_{2k+1}, and δ_1(H)>=kn+6k^2+7k+6 forces P_{2k+2}.

      • [1000979] Tang–Wu–Zhang (2026): exact P5 and general conjectural scale
          STATEMENT
          Every n-vertex linear 3-graph with no P_5 has at most 15n/11 edges, with equality iff it is a disjoint union of the 11-vertex 15-edge graph G_0 (hence equality requires 11|n). They record the general conjecture ex_L(n,P_k) <= (k/3)n + c n for a universal constant c.

      • [1000519] Adak–Verma (2026 v2): uniform hypertrees and P4^r
          STATEMENT
          Under the stated design/divisibility assumptions, every k-edge linear r-uniform hypertree has a T_k^r-free construction with n(k-1)/r edges. For P_4^r, the source states the general value (r+1)n/r as a conjecture and proves the exact result for r=4; it also verifies connected cases under additional degree conditions.

      • [1001031] Ergemlidze–Győri–Methuku rainbow path Turán bound
          STATEMENT
          If P_t denotes a path of t edges, then every properly edge-colored n-vertex graph with no rainbow P_t has fewer than ((9(t-1))/7+2)n=((9t+5)/7)n edges.

      • [1000759] Ramani (2026): four-edge paths via incidence rank
          STATEMENT
          For every r>=2, every n-vertex linear r-uniform P_4^r-free hypergraph has at most (r+1)n/r edges, with equality precisely for vertex-disjoint unions of Steiner systems S(2,r,r^2).

    • [1000230] Human-proof replacement program for computational evidence
        STATEMENT
        Replace LINP's finite computational evidence, where mathematically worthwhile, by exact human arguments. Prioritize open structural conjectures and symmetric finite families; do not spend proof effort reproducing finite evidence whose intended conjecture has already been refuted.

      • [1000518] Human symmetry proof for the punctured cyclic STS(13) all-special calibration
          STATEMENT
          Deleting one point from the cyclic STS(13) gives a 12-vertex linear 3-graph in which every remaining edge has edge rank 5 and is special.

        • [1000585] The five-regular STS(13) puncture contains a linear five-cycle
            STATEMENT
            In the 12-vertex, 20-edge, 5-regular linear triple system obtained by deleting 0 from the cyclic STS(13) generated by {0,1,4} and {0,2,7}, the five blocks {1,2,5}, {2,3,6}, {3,4,7}, {4,10,12}, {10,11,1} form a linear cycle of length five. Consequently finite-field additive blow-ups of this P6-free calibration have paths of length 5q-O(1) and cannot improve the asymptotic one-third lower coefficient.

    • [1000112] Current conjecture, proposal, and numerical-evidence map
        STATEMENT
        Index of the live unproved mechanisms, conjectures, computational evidence, and explicit fences currently relevant to improving the general 3-uniform linear-path upper bound.

  • [1000953] General lower-bound construction program
      STATEMENT
      Organizational route collecting construction mechanisms and obstructions for improving the lower bound, including Steiner/projective systems, Boolean additive systems, Latin/transversal blow-ups, products, and construction fences.

    • [1000355] Latin, transversal, and blow-up construction route
        STATEMENT
        Organizational route for transversal designs, Latin-square lifts, cycle lifting, shared-color blow-ups, and related construction ceilings.

      • [1000019] Arbitrary Latin blow-ups lift base cycles to near-spanning route paths
          STATEMENT
          Let T be a fixed linear 3-graph containing a linear cycle C_s of length s>=3. Blow up each base vertex by q and replace every base triple independently by an arbitrary transversal design TD(3,q). Then the blow-up contains a linear path of length sq-o(q).
          
          More precisely, after cyclically labeling one joint cluster X_0={a_0,...,a_{q-1}}, for q-o(q) consecutive obligations t one can choose pairwise internally resource-disjoint lifted s-edge routes R_t from a_t to a_{t+1}; these concatenate to one path.
          
          Consequently, if T has v vertices and m edges, the full blow-up has qv vertices and q^2m edges and its normalized density at its first forbidden path length is at most
            m/(vs)+o(1).
          In particular, for the four-cycle in AG(2,3), every arbitrary-Latin affine-plane blow-up has a path of length 4q-o(q), so its normalized density is at most 1/3+o(1). Thus arbitrary local Latin fillings cannot amplify the affine-plane construction above the one-third asymptotic coefficient.

      • [1000041] Static transversals and fixed-multiplicity shared-color lifts cannot beat one third
          STATEMENT
          Three related lower-construction fences hold.
          
          (1) If a linear 3-graph H on n vertices has a vertex cover C of size t, then |E(H)|<=t(n-1)/2 and every linear path has at most 2t edges. Thus a path cap certified solely by a fixed t-vertex global transversal has normalized density below 1/4 at ell=2t+1.
          
          (2) This one-quarter ceiling is asymptotically attained by repeated one-factorization lifts: if a graph G has a proper d-edge-coloring in which every two colors occur on incident edges, and H_t is formed from t disjoint copies of G by adjoining one shared vertex for each color and lifting xy of color c to {x,y,c}, then for t>=d the lift contains a 2d-1 edge linear path. In particular repeated lifts of one-factorized K_{2^r} have asymptotic normalized coefficient at most 1/4.
          
          (3) More flexible fixed-multiplicity sharing still cannot beat the one-third benchmark. For fixed r>=3 and even N, let d=N-1 and take r disjoint copies of K_N, each arbitrarily one-factorized by the same d color labels; adjoining one common vertex for each color and lifting the graph edges gives H_{r,N}. Then H_{r,N} contains a linear path of length at least (3r/(2(r+1))-o(1))d. Since |E|/|V|=(r/(2(r+1))+o(1))d, its normalized density at its first forbidden path length is at most 1/3+o(1).

      • [1000329] Characteristic-two additive blow-ups lift every fixed base cycle to an almost q-fold path
          STATEMENT
          Let T contain a linear cycle of length s>=3 and let q=2^k be sufficiently large. Its coordinatewise additive F_q blow-up contains a linear path of length at least s(q-2). Hence its normalized density at the first forbidden path length is at most m/(vs)+o(1). For AG(2,3), a base four-cycle gives a 4q-8 path and asymptotic coefficient at most 1/3.

      • [1000382] Odd-order additive Latin blow-ups lift every base linear cycle
          STATEMENT
          Let T be a linear 3-graph containing a linear cycle of length s, and let q be odd. In the additive Z_q blow-up of T, that base cycle lifts to a linear cycle of length sq. Hence a fixed template with v vertices and m edges has normalized density at its first forbidden path length at most m/(vs). In particular the 11-vertex, 15-edge P5-extremal template G0 contains a base 5-cycle, so its additive blow-up contains a 5q-cycle and is bounded by 3/11<1/3.

        • [1000612] PG(3,2) contains a seven-edge linear cycle
            STATEMENT
            The Steiner triple system PG(3,2) contains a linear cycle of length 7. Consequently, for every odd q, its coordinatewise additive Z_q blow-up contains a linear cycle of length 7q and therefore a linear path of length 7q-1; since the blow-up has 15q vertices and 35q^2 edges, this construction cannot beat the asymptotic lower-bound coefficient 1/3.

        • [1000021] Additive affine-plane blow-ups have a 4q-cycle and cannot beat one third
            STATEMENT
            Let A be the affine-plane Steiner triple system AG(2,3). For every odd q, replace each of its nine points by a copy of Z_q and each of its twelve lines by the additive transversal design whose three coordinates sum to zero. The resulting linear 3-graph has 9q vertices and 12q^2 edges, but contains a linear cycle of length 4q and hence a path of length 4q-1. Therefore its normalized density at its first forbidden path length is at most 1/3.

      • [1000136] Arbitrary Latin lifts of the G0 five-cycle contain an almost-perfect packing of full laps
          STATEMENT
          Fix the rainbow 5-cycle of base edges in G0 and blow up its ten used base vertices by q, using an arbitrary Latin square on each of the five base triples. Label one joint cluster X_0={a_0,...,a_{q-1}} cyclically. For each t, let R_t be the family of five-edge lifted routes that start at a_t, traverse the five base-edge types once in cyclic order, and end at a_{t+1}. Then for q tending to infinity there is a set T of size q-o(q) and choices R_t in R_t for t in T such that the chosen routes are pairwise disjoint outside the prescribed X_0 endpoints. Equivalently, their four intermediate joint vertices and five private-symbol vertices are all distinct across chosen routes.

      • [1001154] Every order-four transversal design has a maximum-length linear path
          STATEMENT
          Every transversal design TD(3,4), equivalently every Latin square of order 4, contains a linear path of length 5. This is best possible because such a path uses 11 vertices and TD(3,4) has 12 vertices.

      • [1000335] Every order-five transversal design has a spanning seven-edge linear path
          STATEMENT
          Every transversal design TD(3,5), equivalently every Latin square of order 5, contains a spanning linear path P_7^(3).

      • [1000423] Every order-six Latin square has a full-color rainbow path
          STATEMENT
          Every proper edge-coloring of K_{6,6} with six colors contains a rainbow path of six edges. Equivalently, every transversal design TD(3,6), or every Latin square of order six, contains a six-edge linear path.

        • [1000245] Every properly six-colored K6,6 has a rainbow five-edge path
            STATEMENT
            Every proper edge-coloring of K_{6,6} with six colors contains a rainbow path of length at least five.

        • [1000584] The rainbow-six-cycle branch has one canonical chord matrix
            STATEMENT
            In the closing-chord normal form for a proper 6-coloring of K_{6,6} with no rainbow P_6, normalize the rainbow cycle
            a-A-b-B-c-C-a
            to have successive colors 1,2,3,4,5,6. Then, up to the half-turn symmetry of the cycle and relabeling colors by +3 modulo 6, the colors on the three remaining used-vertex chords are forced to be
            aB=2, bC=4, cA=6.
            Equivalently the used 3x3 color matrix is
            [ [1,2,6], [2,3,4], [6,4,5] ].

        • [1000622] Two endpoint-chord normal forms for an order-six rainbow-path counterexample
            STATEMENT
            Let K_{6,6} have a proper 6-edge-coloring and contain no rainbow P_6. If P=x_0y_0x_1y_1x_2y_2 is a rainbow P_5 whose five edge colors are distinct and alpha is the missing color, then exactly one of two configurations holds: (I) x_0y_2 has color alpha; or (II) both x_0y_1 and x_1y_2 have color alpha.

        • [1000800] Crossed missing-color chords force the opposite endpoint chord
            STATEMENT
            In the crossed-chord normal form for a hypothetical proper 6-coloring of K_{6,6} with no rainbow P_6, normalize a rainbow P_5 as x_0y_0x_1y_1x_2y_2 with colors 1,2,3,4,5 and suppose the missing color 6 occurs on x_0y_1 and x_1y_2. Then x_0y_2 has color 3.

        • [1000842] The crossed-chord order-six normal form forces a forbidden rainbow cycle
            STATEMENT
            The crossed-chord normal form of 8d4230198b1b is impossible. Therefore every proper 6-edge-coloring of K_{6,6} contains a rainbow P_6.

        • [1001115] The rainbow-six-cycle normal form forces a color collision
            STATEMENT
            The closing-chord (rainbow C_6) normal form of 8d4230198b1b is impossible. Hence any hypothetical proper 6-coloring of K_{6,6} with no rainbow P_6 must lie in the crossed-chord normal form.

      • [1000982] Schrijver rainbow paths give a one-third ceiling for full transversal designs
          STATEMENT
          Let T_q be any transversal design TD(3,q), equivalently the lift of a proper q-edge-coloring of K_{q,q} using q colors. Then T_q contains a linear path of length q-o(q) as q tends to infinity. Consequently, if ell(T_q) is one plus the maximum linear-path length of T_q, then (|E(T_q)|/|V(T_q)|)/ell(T_q) <= 1/3+o(1); in particular full transversal designs cannot yield an asymptotic lower-bound coefficient strictly larger than 1/3.

    • [1000893] Boolean additive and projective construction route
        STATEMENT
        Organizational route for induced Boolean Schur systems, binary carriers, projective exceptions, spanning-path obstructions, and the eventual closure of the critical Boolean family.

      • [1001136] Binary-projective diagonal tensor squares admit long coprime-orbit paths and stay below one third
          STATEMENT
          For every d>=3, let P_d=PG(d-1,2). Then P_d tensor P_d contains a linear path of length (2^d-1)(2^{d-1}-1)-1. If r=2^{d-1}-1 is the degree of P_d, the tensor square is 2r^2-regular and its normalized density at its first forbidden path length is less than 1/3. For d=4 this is the explicit 104-edge path in PG(3,2) tensor PG(3,2).

      • [1000137] Density improvement forces an almost-period and binary carrier reduction
          STATEMENT
          Let A subset F_2^d\{0}, let n=|A|=2ell+1+t with t>=0, and let H(A) consist of all triples {x,y,x+y} contained in A. If |E(H(A))|/n>(ell-1)/3, then there is x in A such that at most t translation pairs {y,y+x} cross S=A union {0}. Equivalently b_S(x)<=t, and d_H(x)>=(n-1-t)/2=ell. Deleting one S-vertex from each crossing pair produces S0 subset S with |S\S0|<=t and S0+x=S0. Thus, after at most t vertex deletions, A has an exact 2-point carrier decomposition over the quotient F_2^d/<x>.

        • [1000410] Every density-beating induced Boolean counterexample contains a non-Hamiltonian exact one-bit core
            STATEMENT
            Let A subset F_2^d\{0}, |A|=n=2ell+1+t, and suppose H(A) is P_ell-free while |E(H(A))|/n>(ell-1)/3. Then A contains an induced subdomain A0 of odd size n-k with k<=t such that A0 is an exact full one-bit Boolean lift of a quotient domain B, and H(A0) has no spanning linear path. Consequently the entire density-beating induced x+y construction problem reduces, without any defect-absorption loss, to classifying non-Hamiltonian exact one-bit lifts.

          • [1000770] Every nonpath additive triple is balanced over path-even bit colorings
              STATEMENT
              Let B be an additive domain of size 2r+1 and let P be a spanning P_r in H(B). Let Sigma(P) be the F_2-vector space of functions sigma:B->F_2 for which every edge e of P has sum_{v in e}sigma(v)=0. Then dim Sigma(P)=r+1. For every additive triple e in E(H(B))\E(P), exactly half of sigma in Sigma(P) satisfy sum_{v in e}sigma(v)=1. Consequently some P-even coloring has at least (|E(H(B))|-r)/2 odd triples, all edge-disjoint from P.

          • [1000331] Compatible two-rail criterion for Hamiltonicity of a one-bit Boolean lift
              STATEMENT
              Let B be a finite nonzero subset of an elementary abelian 2-group with |B|=2r+1. Suppose H(B) has two spanning P_r paths P and Q sharing a common endpoint vertex b. Let A=((B union {0}) x F_2)\{(0,0)} be the full one-bit lift. If every even subhypergraph of P union Q contains an even number of Q-edges, then H(A) has a spanning P_{2r+1}. In particular it is enough that the binary incidence vectors of the 2r edges in P union Q are linearly independent.

      • [1000618] Joint-residue normal form for spanning paths in Boolean Schur systems
          STATEMENT
          Let A be a finite subset of an elementary abelian 2-group with 0 notin A and |A|=2ell+1. Let H(A) consist of all triples {x,y,x+y} contained in A. Then H(A) has a spanning P_ell if and only if there are distinct joints j_1,...,j_{ell-1} in A such that the ell-2 consecutive sums s_i=j_i+j_{i+1} are distinct and lie in A\J, and the four residual points R=A\(J union {s_1,...,s_{ell-2}}) can be partitioned R={a,b,c,d} with a+b=j_1 and c+d=j_{ell-1}. Necessarily XOR(J)=XOR(A).

        • [1000135] Rank-nullity forces a small zero-sum block in the joint set
            STATEMENT
            In the joint-residue setting, suppose XOR(A)=0 and the joint set J has k=ell-1 elements spanning rank at most d. If k>=d+2, then J has a proper zero-sum subset S with 3<=|S|<=floor(k/2). For PG(3,2), k=6 and d=4, so |S|=3 and its complement also has size 3 and sum zero; hence the six joints split into two projective lines. This numerical collapse is specific to the six-joint rank-four case.

      • [1001143] Near-Steiner classification for induced Boolean Schur triple systems
          STATEMENT
          Let A be a finite subset of an elementary abelian 2-group G with 0 not in A and n=|A| odd. Let H(A) have edges {x,y,x+y} contained in A, and let M be the number of unordered pairs {x,y} in A with x+y not in A. If M<n, then for some subgroup W<=G either A=W\{0}, or A=W\{0,a,b} for two distinct nonzero a,b in W. Equivalently, among odd-order induced Boolean Schur systems, being within fewer than n missing pairs of a Steiner triple system forces a projective system or a two-point deletion of one.

        • [1000884] Critical Boolean additive constructions reduce to projective families, with only lengths 3 and 7 surviving through 15
            STATEMENT
            Let A⊂F_2^d\{0} have |A|=2ell+1, and let H(A) be the induced Boolean Schur triple system. If H(A) is P_ell-free and has density greater than (ell-1)/3, then A is either a punctured subspace or a punctured subspace with two additional points deleted; equivalently ell=2^{r-1}-1 or ell=2^{r-1}-2. For 2<=ell<=15, the only strict-density-improving P_ell-free cases in these two families are the Fano example at ell=3 and PG(3,2) at ell=7.

        • [1000002] Set-sequential paths close the critical induced-Boolean construction route
            STATEMENT
            Assume the near-Steiner classification fb1725da2cc8. For critical components |A|=2ell+1 in induced Boolean Schur hypergraphs H(A), strict improvement over the generic (ell-1)/3 density can occur only at ell=3 or ell=7. More precisely, all full projective candidates A=F_2^r\{0} are Hamiltonian for r>=5 by the Mehta--Vijayakumar set-sequential path theorem, and all two-point-deleted projective candidates A=F_2^r\{0,a,b} are Hamiltonian for r>=5 by deleting an endpoint vertex and its adjacent edge-label from such a set-sequential path and applying GL(r,2) 2-transitivity. The small two-point cases r=3,4 are also Hamiltonian; the full r=3,4 systems are the Fano P3-free and PG(3,2) P7-free exceptions.

      • [1000918] The n=2ell+2 additive case reduces to a two-bit carrier after at most five deletions
          STATEMENT
          Let A subset F_2^d\{0} have |A|=2ell+2. If H(A) is P_ell-free and |E(H(A))|/|A|>(ell-1)/3, then the almost-period reduction deletes exactly one vertex and yields an exact one-bit core over a quotient domain B of size ell. If R(B) denotes the number of unordered pairs {u,v} subset B with u+v notin B, then R(B)<=ell. Consequently B has a nonzero translation with boundary at most two; after deleting at most two further quotient vertices, B becomes an exact one-bit lift. Therefore A contains an exact two-bit Boolean carrier core after deleting at most 1+2*2=5 vertices.

        • [1000685] The claimed universal fourfold Boolean path lift fails on the 3-point line
            STATEMENT
            Object 7d7c5c253a86 is false as stated. Let B=F_2^2\{0}, so H(B) is one additive triple and has a spanning P_1 with r=1 odd. Its full two-bit lift ((B union {0}) x F_2^2)\{0} is F_2^4\{0}, i.e. PG(3,2). The repaired theorem d593f8024a92 proves PG(3,2) is P_7-free, whereas 7d7c5c253a86 asserts that this lift contains a spanning P_{4*1+3}=P_7. Hence 7d7c5c253a86, and downstream claims 7053f2ba50ad and the odd-L strengthening in e48ba67dae9c, require repair or rejection.

        • [1001027] Corrected two-bit carrier lift multiplies longest additive paths by four up to O(1)
            STATEMENT
            Let B be any finite nonzero domain in an elementary abelian 2-group, let L=L(H(B))>=1, and let A=((B union {0}) x F_2^2)\{0}. Then L(H(A))>=4L-1. If L is even, the stronger bound L(H(A))>=4L+3 holds. Moreover |A|=4|B|+3 and |E(H(A))|=16|E(H(B))|+6|B|+1. Consequently repeated exact two-bit carrier lifts cannot asymptotically improve the normalized density/path-length ratio of a construction family.

          • [1001065] Fourfold Boolean lift preserves even spanning additive paths
              STATEMENT
              Let B be a finite nonzero subset of an elementary abelian 2-group with |B|=2r+1 and r even. If H(B) contains a spanning P_r, then A=((B union {0}) x F_2^2)\{0} contains a spanning P_{4r+3}. The parity r even is essential to this four-copy construction: the corresponding ordinary path has two leaves in the same bipartition class, exactly the hypothesis in the corrected four-copy set-sequential lemma of Eckels--Gyori--Liu--Nasir (2024).

    • [1000067] STS(2ell+1) spanning-path obstruction route
        STATEMENT
        If there exists a Steiner triple system S on 2ell+1 vertices containing no spanning linear path P_ell, then disjoint copies of S give ex_L(n,P_ell^(3)) >= (ell/3)n - O(ell^2), and exactly (ell/3)n when 2ell+1 divides n. Thus any infinite family of such non-Hamiltonian Steiner triple systems improves the general lower benchmark (ell-1)n/3 by an additive n/3 on those lengths.

      • [1000576] PG(4,2) has a spanning 15-edge linear path
          STATEMENT
          The binary projective Steiner triple system PG(4,2) on the nonzero vectors of F_2^5 contains a spanning linear path with 15 edges. Hence the PG(3,2) non-Hamiltonicity phenomenon does not extend automatically to the next binary projective dimension.

      • [1000720] Human proof that every block of cyclic STS(13) is special of rank six
          STATEMENT
          In the cyclic Steiner triple system S on Z_13 generated by translates of B_1={0,1,4} and B_2={0,2,7}, every block has longest-path rank 6 and is special.

      • [1001095] Human proof that the cyclic STS(13) puncture is single-block extension-tight
          STATEMENT
          Let S be the cyclic Steiner triple system on Z_13 generated by the translates of {0,1,4} and {0,2,7}. Delete vertex 0 and its six incident blocks. If any one of those six blocks is restored, the resulting 21-edge system contains a spanning 6-edge linear path.

      • [1001096] Human proof of the exact six-block deletion threshold in cyclic STS(13)
          STATEMENT
          In the cyclic Steiner triple system STS(13) generated by the translates of B_1={0,1,4} and B_2={0,2,7}, at least six blocks must be deleted to destroy every spanning linear P_6, and six deletions suffice.

      • [1000025] Binary doubling reduces spanning paths to additive rainbow-forest accounting
          STATEMENT
          Consider the standard doubling of an STS on an odd set U by a one-factorization on a disjoint set W of size |U|+1. If a spanning linear path uses a old blocks from U, then its mixed edges select a spanning linear forest on W with exactly a+1 components; each component is rainbow in the one-factorization, every color is used at most twice, and repeated colors occur exactly at U-joints between consecutive mixed hyperedges.
          
          In the binary additive doubling W=F_2^d with color(pq)=p+q, let M be the unused nonzero colors and R the colors used twice. Then
          |M|-|R|=a,
          and the xor of all component endpoints equals xor(M) xor xor(R).
          
          In particular a=0 is impossible: it would give a rainbow Hamiltonian path in the additive one-factorization, but the xor of all nonzero colors is zero whereas the xor of the colors along a Hamiltonian path equals the xor of its two distinct endpoints and is nonzero. Thus every spanning path in the binary doubled STS uses at least one old block.

        • [1000119] STS doubling cannot beat the one-third leading coefficient
            STATEMENT
            Let D be any Steiner triple system obtained by doubling an STS on u vertices with an arbitrary one-factorization of K_{u+1}. For all sufficiently large u, D contains a linear path with at least u-1 edges using only mixed blocks. Consequently, if ell(D) is one plus the maximum linear-path length of D, then |E(D)|/(|V(D)| ell(D))<=1/3. Thus no asymptotic family of ordinary doubled STSs can improve the leading 1/3 lower-bound coefficient.

      • [1000840] A missing incidence-code weight forbids a linear path
          STATEMENT
          Let H be a 3-uniform hypergraph and let C be the binary linear code spanned by the incidence vectors of E(H). If H contains a linear path P_ell^(3), then C contains a codeword of Hamming weight exactly ell+2. Consequently, if C has no codeword of weight ell+2, then H is P_ell^(3)-free.

        • [1000548] Alternating incidence sums give a support-(ell+2) codeword over any field
            STATEMENT
            Let H be a 3-uniform hypergraph, let F be any field, and let C_F be the F-linear span of the edge-incidence vectors. If H contains a linear path P_ell^(3), then C_F contains a vector whose support has size exactly ell+2. Hence if every nonzero vector of C_F has support size different from ell+2, then H is P_ell^(3)-free.

        • [1000899] High-degree stars defeat the missing-weight certificate in two residue classes
            STATEMENT
            Let H be a linear 3-graph and C its binary incidence code. If ell is congruent to 2 mod 4 and Delta(H)>=(ell+2)/2, or if ell is congruent to 1 mod 4 and Delta(H)>=(ell+1)/2, then C contains a codeword of weight ell+2. Consequently no family with |E(H)|/|V(H)|>ell/3 can be certified P_ell-free solely by absence of weight ell+2 in its incidence code for ell congruent to 1 or 2 mod 4.

          • [1000752] Density above ell/3 forces the path weight in the binary incidence code
              STATEMENT
              Let ell>=3 and let H be a finite linear 3-graph with m edges and n vertices. If m/n>ell/3, then the binary linear code spanned by the edge-incidence vectors of H contains a codeword of Hamming weight exactly ell+2. Consequently, the sufficient certificate 'the binary incidence code has no word of weight ell+2' can never certify a P_ell-free construction whose edge density exceeds ell/3.

          • [1000472] Ternary incidence-code missing weights cannot certify a leading lower-bound improvement
              STATEMENT
              Let H be a linear 3-graph and let C_3 be the F_3-linear span of its edge-incidence vectors. If H contains P_ell then C_3 contains a codeword of Hamming weight ell+2. Conversely, if Delta(H)>=floor((ell+2)/2) and ell>=2, then C_3 already contains a codeword of weight ell+2. Hence any H with |E(H)|/|V(H)|>ell/3 necessarily has such a codeword, so absence of weight ell+2 in a ternary incidence code cannot certify a P_ell-free construction beating the 1/3 coefficient.

      • [1000955] PG(3,2) gives a 7/3 lower bound for P7
          STATEMENT
          The binary projective Steiner triple system PG(3,2) on 15 vertices and 35 edges contains no linear path with 7 edges. Consequently ex_L(n,P_7^(3)) >= 35 floor(n/15) = (7/3)n-O(1), with equality to (7/3)n for 15|n.

        • [1000707] Two-point split of a projective seven-cycle is Hamiltonian
            STATEMENT
            Let H be obtained from PG(3,2) by deleting the seven lines (1,8,9),(2,9,11),(4,11,15),(3,12,15),(6,10,12),(7,10,13),(5,8,13), adjoining two vertices a,b, and replacing each deleted line {x_i,x_{i+1},p_i} by {a,x_i,p_i} and {b,x_{i+1},p_i}. Then H has 17 vertices and 42 edges but contains a spanning P_8.

        • [1000270] Why the P7 two-subspace grid obstruction is dimension-four exceptional
            STATEMENT
            Let P be a hypothetical spanning linear path in the Boolean projective Steiner triple system PG(r-1,2) on F_2^r\{0}, and let J be its joint set. Then |J|=2^{r-1}-2 and XOR(J)=0. More generally, if |J|>=r+2, J contains a nonempty proper zero-sum subset S with 3<=|S|<=floor(|J|/2). For r=4, |J|=6, so necessarily |S|=3 and J\S is also a zero-sum triple; these are the two complementary 2-spaces used in the P7 grid proof. Moreover this exact architecture cannot recur for r!=4: if J=(U\{0}) union (W\{0}) for complementary nonzero subspaces U,W, then the spanning-path joint count forces r=4 and dim U=dim W=2.

      • [1000122] Hyperplane parity obstruction for spanning paths in binary projective STS
          STATEMENT
          Let d>=3 and let H be the Steiner triple system of lines of PG(d-1,2), on 2^d-1 points. If H has a spanning linear path, and J is the set of its joint vertices, then |J∩Pi| is even for every projective hyperplane Pi. Equivalently, representing points by nonzero vectors of F_2^d, the vector sum of J is 0.

      • [1000008] Edge-transitive Steiner systems have a sharp deletion barrier
          STATEMENT
          Let S be an edge-transitive Steiner triple system on v=2ell+1 vertices. If S contains one spanning linear path P_ell, then every block set meeting every spanning P_ell has size at least v/3. Consequently no deletion from a Hamiltonian edge-transitive STS can produce a P_ell-free component whose density exceeds the generic (ell-1)/3 benchmark.

      • [1000855] PG(4,2) has a spanning P15
          STATEMENT
          The binary projective Steiner triple system PG(4,2) on 31 points contains a spanning linear path with 15 edges. Hence the PG(3,2) non-Hamiltonicity phenomenon does not extend to the next binary projective dimension.

      • [1000942] One-factorization lifts are asymptotically inefficient for path lower bounds
          STATEMENT
          Let N be even and let phi be a 1-factorization of K_N. Form the linear 3-graph H_phi on V(K_N) union the N-1 colors by replacing each graph edge xy of color c with the triple {x,y,c}. Then |V(H_phi)|=2N-1 and |E(H_phi)|=N(N-1)/2. For all sufficiently large N, H_phi contains a linear path of length N-2. Consequently, if ell(H_phi) is one plus its maximum linear-path length, then |E(H_phi)|/(|V(H_phi)| ell(H_phi)) <= N/[2(2N-1)] = 1/4+o(1). Thus this natural generalization of the P5 extremal G0 cannot improve the asymptotic 1/3 lower coefficient.

        • [1000554] Cartesian products multiply available linear-path lengths
            STATEMENT
            Let H and K be finite linear 3-graphs containing linear paths of lengths a>=1 and b>=1. Then their Cartesian product H square K contains a linear path of length (a+1)(b+1)-1. Consequently, if H has n vertices, m edges, and maximum linear-path length L>=1, then its t-fold Cartesian power has edge/vertex ratio t(m/n) and maximum linear-path length at least (L+1)^t-1. Thus repeated Cartesian powering of a fixed component cannot yield a positive asymptotic coefficient in (|E|/|V|)/ell when ell is one plus the maximum path length.

        • [1000889] Repeated arbitrary proper-color lifts have a one-quarter asymptotic ceiling
            STATEMENT
            Let G be any finite properly edge-colored simple graph on u vertices with color set S. For r>=1 form H_r from r vertex-disjoint copies of G by adjoining one common hypergraph vertex for each color c in S and replacing every graph edge xy of color c by {x,y,c}. If H_r is P_ell-free for arbitrarily large r, then |E(G)|/u <= ceil(ell/2)/2. Consequently |E(H_r)|/|V(H_r)| <= ell/4+O(1)+o_r(1), so no repeated shared-color lift of this form can improve the one-third leading lower coefficient.

      • [1000917] Incidence-code constraint for a spanning linear path
          STATEMENT
          Let H be a 3-uniform hypergraph on 2ell+1 vertices and let C over F_2 be the binary span of its edge-incidence vectors. If H has a spanning linear path P_ell with joint set J of size ell-1, then 1_V + 1_J lies in C. Equivalently, for every vector y in C^perp one has |J intersect supp(y)| congruent to |supp(y)| mod 2.

      • [1000162] Carrier-label parity constraint for spanning paths in low-2-rank STS
          STATEMENT
          Let S be an STS(v) whose binary block-incidence code has rank v-m with m>=2. By the Assmus/Jungnickel--Tonchev carrier description, label the points by columns h(x) in F_2^m of a parity-check matrix: each nonzero label occurs w times and 0 occurs w-1 times, where v=w2^m-1. If S contains a spanning linear path and J is its joint set, then XOR_{x in J} h(x)=0. Equivalently, the set of carrier classes containing an odd number of joints is a zero-sum subset of F_2^m.

      • [1001156] Affine F3 joint-sum obstruction for spanning paths
          STATEMENT
          Let H be the affine Steiner triple system AG(d,3) on F_3^d, d>=2. If H has a spanning linear path, with joint set J, then sum_{x in J} x=0 in F_3^d. In particular AG(2,3) contains no spanning 4-edge linear path, giving a short algebraic proof of the affine-plane P4 obstruction.

      • [1000121] AG(3,3) has a spanning P13
          STATEMENT
          The affine Steiner triple system AG(3,3) on 27 points contains a spanning 13-edge linear path. Hence the affine-plane P4 obstruction and the joint-sum condition do not extend to a non-Hamiltonian affine family in dimension 3.

      • [1000500] Almost-spanning hypertrees give a 1/3 ceiling for Steiner-system lower constructions
          STATEMENT
          Im, Kim, Lee and Methuku proved that for every fixed mu>0 and all sufficiently large v, every Steiner triple system on v vertices contains every hypertree on at most (1-mu)v vertices. In particular it contains a linear path with at least ((1-mu)v-1)/2 edges. Consequently a sequence of Steiner triple systems, used as P_ell-free components at their first forbidden path lengths, has normalized density (|E|/|V|)/ell at most 1/3+o(1). Thus full Steiner triple systems cannot yield an asymptotic lower-bound coefficient strictly larger than 1/3.

      • [1000989] Signed projective normal form one rank above minimum
          STATEMENT
          For N=2^n-1, every STS(N) contained in the carrier code of binary rank at most N-n+1 (the t=1 carrier) has the following normal form. There is one distinguished point infinity and, for each nonzero x in F_2^{n-1}, a pair G_x={(x,0),(x,1)}. The block through infinity and G_x is {infinity,(x,0),(x,1)}. For every projective line {x,y,z} with x+y+z=0, the blocks on G_x union G_y union G_z form a TD(3,2); after choosing bit labels in each pair, this TD is described by b_x+b_y+b_z=sigma(x,y,z) for one sign sigma in F_2. Thus the family is encoded by a binary sign on each quotient line, modulo independent swaps of the two points in each G_x. The lower-bound problem asks whether sign patterns can force absence of a spanning linear path even when the all-projective pattern is Hamiltonian.

        • [1000056] Signed carrier-chain identity for a spanning path
            STATEMENT
            In the t=1 signed-projective normal form dd9129917320, suppose a spanning linear path exists. Let Q=PG(n-2,2) be the quotient on the carrier pairs G_x. Let y in F_2^{Lines(Q)} record, for each quotient line L, the parity of the number of selected cross blocks of the path supported on L. Let p in F_2^{Points(Q)} record, for each x, the parity of the number of path joints lying in G_x. Then A_Q y=p, where A_Q is the point-line incidence matrix of Q. If sigma is the line-signing and j_infinity is 1 when infinity is a path joint and 0 otherwise, then <sigma,y> = j_infinity + sum b over all path joints (x,b), modulo 2.

    • [1000114] Prize shelf: exceptional lower-bound constructions
        STATEMENT
        Curated shelf of especially strong, reusable, or potentially novel lower-bound results for linear-path Turán numbers. First prize: the PG(3,2) construction proving ex_L(n,P_7^(3)) >= (7/3)n-O(1).

    • [1000867] Residue-free (ell-1)/3 lower construction
        STATEMENT
        For every integer ell>=2, there is a P_ell^(3)-free linear triple system component T on t in {2ell-1,2ell} vertices with |E(T)|=((ell-1)/3)t. Hence ex_L(n,P_ell^(3)) >= ((ell-1)/3)n-O(ell^2) for every n; when n is divisible by the chosen t, ex_L(n,P_ell^(3)) >= ((ell-1)/3)n exactly.

      • [1000826] RETRACTED: incorrect MPTS lower-bound calculation
          STATEMENT
          Retracted. The claimed improvement used an incorrect maximum-packing formula for v≡4 (mod 6); in particular MPTS(10) has 13 edges, not 14. No lower-bound improvement follows from this calculation.

  • [1001233] Longest-path pair-capacity reduction with outside extremal defect
      STATEMENT
      Assume the target inequality 3m<=ell n is being proved inductively for P_ell-free linear 3-graphs. Let H be a minimal counterexample candidate, let P be a longest k-edge linear path, put X=V(P), Y=V(H)\X, m_Y=|E(H[Y])|, and e_X=|E(H)|-m_Y. Define the outside defect D_Y=ell|Y|-3m_Y, which is nonnegative by the inductive hypothesis. Then 3|E(H)|<=ell|V(H)| is equivalent to
      3e_X <= ell|X|+D_Y.
      Since |X|=2k+1,
      ell|X| = binom(|X|,2)+(ell-k)|X|.
      Hence it is enough, and under the inductive hypothesis equivalent, to prove
      3e_X <= binom(|X|,2)+(ell-k)|X|+D_Y.
      In the saturated case k=ell-1 this becomes
      3e_X <= binom(|X|,2)+|X|+D_Y.

  • [1001017] General-length attack: special-edge density and incidence rank
      STATEMENT
      For the 3-uniform general-length upper bound, pursue two complementary routes. Primary snake route: prove s>=epsilon*m-O(n) for some absolute epsilon>0, where s is the number of special edges; this already improves the leading coefficient below 1. Stronger b=O(n) is only the saturation target of that scheme and yields coefficient 2/3. Parallel graph/rank route: exploit the induced-P_ell-free intersection graph, its exact 3-fold clique cover, and rank(3I+A) to seek bounds capable of passing the 2/3 snake ceiling.

    • [1000272] Post-43/48 proof rehearsal: paid strict-gap local congestion
        STATEMENT
        Suppose the current 43/48 leading coefficient cannot be improved. Then there is a sequence with
          m_j >= (43/48-o(1))S_j.
        The exact rank-sensitive theorem a57007500001 forces n_j^+/S_j -> 0, hence S_j/n_j^+ -> infinity. The certified extraction 9fba15f1495c then yields a set Epp of distinct source-clean, doubly-terminal-single, paid-certified ascending nonspecial edges with
          |Epp| >= (1/16-o(1))S_j,
        such that every edge has edge rank strictly below both terminal vertex ranks.
        
        Assign each edge of Epp to a terminal of minimum vertex rank. The current end-to-end proof closes if there is a function g(p)=o(p) such that every rank-p vertex receives at most g(p) assigned edges from this class. Indeed 7e6abf77cbc5 then gives |Epp|<=sum_v g(phi(v))=o(S_j), a contradiction.
        
        Thus the first unsupported inference in the current proof organization is exactly the sublinear local congestion bound g(p)=o(p) for minimum-terminal assignments inside the paid-certified source-clean doubly-terminal-single strict-two-terminal-gap class.

    • [1000426] Intersection-graph and incidence-rank route
        STATEMENT
        Organizational route for the induced-path intersection-graph reformulation, exact clique-cover structure, and incidence-rank inequalities.

      • [1000511] Pathmaker lemma: linear paths are induced paths in the intersection graph
          STATEMENT
          Let G be a linear r-uniform hypergraph and L(G) its intersection graph on E(G). A sequence e_1,...,e_t is the edge sequence of a copy of P_t^(r) in G if and only if e_1...e_t is an induced path in L(G).

        • [1000960] Exact clique-cover reformulation of linear triple systems
            STATEMENT
            A graph F is the intersection graph of a linear 3-uniform hypergraph on an indexed ground set X if and only if F admits an indexed family (C_x)_{x∈X} of cliques, allowing empty and singleton cliques, such that every vertex of F belongs to exactly three C_x and every edge of F belongs to exactly one C_x. Under this correspondence, P_ell^(3)-freeness is exactly induced-P_ell-freeness of F.

          • [1001133] Weighted incidence-rank inequality
              STATEMENT
              Let H be a linear 3-uniform hypergraph with incidence matrix N. Assign weights 0<=w_e<=1 to its edges, let W=sum_e w_e, and let d_w(v)=sum_{e contains v} w_e. If d_w(v)<=D for every vertex v, then rank_R(N) >= 3W/(D+2). Consequently W <= (D+2)|V(H)|/3.

          • [1000586] Incidence-rank spectral identity
              STATEMENT
              Let G be a linear 3-uniform hypergraph with m edges, incidence matrix N, and intersection graph F with adjacency matrix A. Then N^T N=3I_m+A, so rank_R N=rank_R(3I_m+A)=m-mult_F(-3). In particular rank_R(3I_m+A)≤|V(G)|.

          • [1000512] Nonspecial edges are unique longest-path entrance vertices
              STATEMENT
              Let G be a linear 3-graph, F=L(G), and e∈E(G). For each longest induced path in F ending at the vertex e and having penultimate vertex f, call the unique vertex of f∩e its entrance label. If phi(e)=1 then e is special. If phi(e)≥2, then e is nonspecial exactly when all longest induced paths ending at e have the same entrance label. Equivalently, e is special exactly when at least two entrance labels occur.

            • [1000491] Every special globally top-rank edge is all-top
                STATEMENT
                Let L>=2 be the global maximum linear-path length. If an edge h={a,b,c} has rank phi(h)=L and is special, then phi(a)=phi(b)=phi(c)=L.

        • [1000071] Intersection-graph fences force cycle-rich leading-scale constructions
            STATEMENT
            For a finite linear 3-graph H, linear hypergraph paths are exactly induced paths in the hyperedge intersection graph I(H), whose edges admit the natural vertex-clique cover in which each vertex of I(H) belongs to three cliques and each graph edge belongs to exactly one.
            
            This representation sharply restricts chord-rich P_ell-free constructions. If E(H)=A∪B with every edge in A intersecting every edge in B, then each side has matching number at most three and vertex-cover number at most nine, so H has a vertex cover of size at most 18. More generally, if I(H) is chordal then |E(H)|<=3|V(H)|/2.
            
            Consequently, if H is P_ell-free with ell>=4 and has n vertices and m edges, then H contains at least (m-3n/2)/ell pairwise edge-disjoint linear cycles whenever this quantity is positive. In particular, m>(1/3+epsilon)ell n forces more than (1/3+epsilon-3/(2ell))n pairwise edge-disjoint linear cycles.

      • [1000531] Maximum-degree range of the incidence-rank path inequality
          STATEMENT
          Let H be a finite linear 3-uniform hypergraph with m edges, incidence matrix N, and maximum degree Delta. For every real L>=Delta+2, one has L rank_R(N)>=3m. Consequently m<=L|V(H)|/3. In particular, if H is P_ell^(3)-free and Delta(H)<=ell-2, then ell rank_R(N)>=3m and hence |E(H)|<=ell|V(H)|/3. Thus every counterexample to the conjectural sharp incidence-rank inequality at length ell must satisfy Delta(H)>=ell-1.

      • [1000514] Special-edge nullity conjecture
          STATEMENT
          For every finite linear 3-uniform hypergraph H with incidence matrix N and s special edges in the Devine–Milans snake digraph, nullity_R(N) <= s.

        • [1000081] Three-colored K3,3 family refutes the special-edge nullity conjecture
            STATEMENT
            The special-edge nullity conjecture 7305b7ec9d2a is false. In the certified family c3e95f4ce77d, all m=9t edges are ascending nonspecial and there are n=6t+3 vertices, while rank_R(N)=5t+2. Hence s=0 but nullity_R(N)=m-rank_R(N)=4t-2>0. Equivalently b=9t>6t+3=n for t>=2, contradicting the consequence b<=rank(N)<=n that nullity(N)<=s would imply.

        • [1000563] Constant-factor nullity control already improves the leading coefficient
            STATEMENT
            Let H be an n-vertex P_ell^(3)-free linear 3-graph with m edges, incidence matrix N, and s special edges. If nullity_R(N) <= C s + D n for constants C>0,D>=0 independent of ell, then m <= [C(2ell-3)+D+1]/(2C+1) * n. In particular the leading coefficient is 2C/(2C+1)<1.

        • [1000686] K3,3 nonspecial-column dependence obstruction
            STATEMENT
            The incidence columns corresponding to nonspecial edges of a linear 3-graph need not be linearly independent. There is an explicit six-edge nonspecial configuration whose intersection graph is K_{3,3} and whose six incidence columns satisfy a nontrivial signed dependence.

      • [1000488] Incidence-rank path conjecture
          STATEMENT
          For every ell>=4, if H is a linear 3-uniform P_ell-free hypergraph with m edges and incidence matrix N, then ell*rank_R N >= 3m.

        • [1000237] Bounded matching number gives only a one-quarter path lower coefficient
            STATEMENT
            Hou, Yu, Gao and Liu determined asymptotically/exactly for sufficiently large n the maximum number of edges in a 3-uniform hypergraph with bounded codegree and matching number. Specializing their theorem to codegree at most one: for fixed positive integer nu and sufficiently large n, every n-vertex linear 3-graph H with matching number at most nu satisfies |E(H)| <= (nu/2)n+O(nu^2), with the exact bound given by their function f(n,nu,1). Consequently, any P_ell-free construction certified solely by nu(H)<=ceil(ell/2)-1 has |E(H)| <= ((ceil(ell/2)-1)/2)n+O(ell^2) = (ell/4+O(1))n+O(ell^2), and therefore cannot improve the one-third leading lower coefficient.

        • [1000815] Regular path-length fence is a direct test case of the incidence-rank conjecture
            STATEMENT
            For a d-regular finite linear 3-graph H, the conjectural statement that H always contains a linear path of length at least d-1 follows immediately from the incidence-rank path conjecture. More sharply, any d-regular H with maximum path length at most d-2 would itself be a counterexample to that incidence-rank conjecture.

        • [1000825] Necessary anatomy of any lower construction above the one-third coefficient
            STATEMENT
            Let ell>=2 and let H be an n-vertex, m-edge linear 3-graph with no P_ell and m/n>ell/3. Then: (i) n>=2ell+2; (ii) the average vertex degree is >ell, hence Delta(H)>=ell+1; (iii) every vertex cover has size tau(H)>2ell n/[3(n-1)], and therefore the matching number nu(H)>2ell n/[9(n-1)]; (iv) H has an induced subhypergraph H0 with density at least m/n and minimum degree delta(H0)>ell/3; and (v) H violates the incidence-rank path conjecture, since ell rank_R N <3m. Thus any genuine leading-coefficient lower-bound improvement must be simultaneously large, high-degree, large-transversal, large-matching, and rank-exceptional.

    • [1000552] Snake and terminal-contact accounting route
        STATEMENT
        Organizational route for the snake-indegree, contact-multiplicity, terminal-localization, 0-1-1, paid-edge, and rotation refinements of the general upper bound.

      • [1001160] Snake indegree lemma
          STATEMENT
          Let G be a linear r-graph with snake digraph D. For every vertex v, d_D^-(v) <= (phi(v)-1)(r-1)+1. Moreover, if e contains v and phi(e,v) >= phi(f) for every other edge f containing v, then d_G(v) <= (phi(e,v)-1)(r-1)+1.

        • [1001161] Devine–Milans general linear-path upper bound
            STATEMENT
            For all r>=2 and ell>=2, ex_L(n,P_ell^(r)) <= (ell - 2 + 1/(r-1)) n. In particular, ex_L(n,P_ell^(3)) <= (ell - 3/2)n.

        • [1000405] Special-edge accounting criterion and the two-thirds ceiling of unweighted snake counting
            STATEMENT
            Let H be an n-vertex P_ell-free linear 3-graph with m edges and s special edges in the snake digraph. Then 2m+s <= (2ell-3)n. Hence if s>=epsilon m-Cn for fixed epsilon>0, then m <= ((2ell-3+C)/(2+epsilon))n. Any fixed positive special-edge density improves the leading coefficient below 1, while unchanged unweighted snake-incidence counting cannot cross the 2/3 leading coefficient.

        • [1000847] Weighted bad-load truncation by edge potential
            STATEMENT
            Let H be P_ell-free with incidence matrix N. For any nonincreasing weights 1>=g_1>=...>=g_{ell-1}>=0, define G=sum_e g_{phi(e)}, Q(v)=sum_{e nonspecial, entrance(e)=v} g_{phi(e)}, E_L^g=sum_v(Q(v)-L)_+, and S_g=g_1+2sum_{t=2}^{ell-1}g_t. Then
              G <= ((S_g+L+2)/3) rank_R(N)+E_L^g
                <= ((S_g+L+2)/3)n+E_L^g.
            The unweighted bad-load truncation inequality is the specialization g_t=1.

      • [1000872] Contact-multiplicity snake inequality
          STATEMENT
          Let H be a finite linear 3-graph. For each nonisolated vertex v choose a maximum p_v=phi(v) edge path P_v with last vertex v and last edge h_v. For e incident with v define mu_v(h_v)=1, and for e!=h_v put mu_v(e)=|(e\\{v}) intersect (V(P_v)\\h_v)|. Then sum_{e contains v} mu_v(e)<=2phi(v)-1. Moreover every incidence with phi(e)<=phi(v) has mu_v(e)>=1; the only incidences not forced to have positive multiplicity are ascending nonspecial entrance incidences with phi(e)=phi(v)+1. Consequently, if A is the number of ascending nonspecial edges and X is the total multiplicity excess beyond the baseline 3m-A, then 3m-A+X<=sum_{v:d_H(v)>0}(2phi(v)-1).

        • [1000356] Clean-minus-double identity for the contact snake
            STATEMENT
            Choose a maximum endpoint path P_v for every vertex v and define contact multiplicities mu_v(e) as in c312c26b7c1d. Let C be the number of incidences with mu_v(e)=0 and D the number with mu_v(e)=2. Then 3m-C+D=sum_{v,e contains v}mu_v(e)<=sum_v(2phi(v)-1). In a P_ell-free linear triple system, 3m-C+D<=(2ell-3)n. Every clean incidence is the unique entrance incidence of an ascending nonspecial edge.

          • [1000848] The 11/12 coefficient only requires a three-quarters bound after subtracting double-contact defect
              STATEMENT
              Choose for every vertex v a maximum endpoint path P_v as in the contact-snake framework. Let
                A = number of ascending nonspecial edges,
                S = sum_v phi(v),
                D = total number of double-contact incidences mu_v(e)=2
              with respect to the chosen paths.
              
              Then
                3m-A+D <= 2S-n.
              
              Consequently the global estimate
                A-D <= (3/4)S
              is sufficient to imply
                m <= (11/12)S - n/3.
              In particular, for a P_ell-free linear 3-graph it implies
                m <= ((11ell-15)/12)n.
              
              More locally, assign every ascending edge to a terminal of minimum endpoint potential, and let a(v) be the number assigned to v. If D_v is the number of double-contact incidences at v on P_v, then the pointwise inequalities
                a(v)-D_v <= (3/4)phi(v)
              for all v are sufficient. The same conclusion follows from any global charging proof of their sum, even if individual vertices violate the uncorrected charged-degree bound.

            • [1000271] A clean-only defect-corrected two-rank block suffices for the 11/12 bound
                STATEMENT
                Choose maximum endpoint paths P_x. Count only ascending nonspecial edges whose unique source incidence is genuinely clean, mu_x(e)=0, and assign each such edge to a minimum-potential terminal v. If for every v,q the number of assigned clean edges of ranks q,q+1 that are not double on P_v is at most three, then C-D<=3/4 sum_v phi(v). Hence 3m-C+D<=2 sum phi-n gives m<=11/12 sum phi-n/3, and m<=((11ell-15)/12)n in every P_ell-free system.

              • [1000108] In a source-clean one-low odd-boundary obstruction the rank-q witness is forced to C
                  STATEMENT
                  Let p=phi(v)=2q-3, q>=4. Choose maximum endpoint paths globally, and suppose four assigned source-clean ascending edges through v, of ranks in {q,q+1}, are all single-contact on P_v. Assume exactly one has rank q.
                  
                  Using the five surviving slots
                    A=g_{q-3}∩g_{q-2},
                    B=private(g_{q-2}),
                    C=g_{q-2}∩g_{q-1},
                    D=private(g_{q-1}),
                    E=g_{q-1}∩g_q,
                  the unique rank-q edge cannot have witness D or E.
                  
                  Hence its witness is necessarily C. If C is entrance-visible then phi(C)=q-1; otherwise C is the unique possible terminal-only rank-q witness.

                • [1001153] The visible-entrance C branch of the one-low odd-boundary obstruction is impossible
                    STATEMENT
                    Retain the source-clean one-low setting of 18cdb6e257aa at
                      p=phi(v)=2q-3, q>=4.
                    If the unique rank-q edge has its witness
                      C=g_{q-2}∩g_{q-1}
                    as its visible entrance, then the four-edge all-single configuration is impossible.
                    
                    Hence any surviving source-clean q,(q+1)^3 all-single state has the low edge
                      e={x,v,C}
                    with x absent from P_v and C its sole terminal contact on P_v.

                  • [1000305] Two high edges must meet the early part of the low clean source path
                      STATEMENT
                      In the surviving source-clean one-low odd-boundary state, let e={x,v,C} have edge rank q and let Q=(s_1,...,s_{q-1}) be the chosen maximum path with last vertex x. Let h_1,h_2,h_3 be the three edge-rank-(q+1) ascending edges through v. Then at least two of h_1,h_2,h_3 meet V(s_1 union ... union s_{q-3}). More precisely, any h_i avoiding the first q-3 edges of Q can meet Q only in the unique vertex of s_{q-1} that is neither x nor s_{q-2} cap s_{q-1}; hence at most one high edge can avoid the first q-3 edges.

                  • [1000315] A 0-1-1 low edge at the odd boundary is reciprocally central on its other terminal path
                      STATEMENT
                      Let e={x,v,u} be a 0-1-1 ascending edge of rank q>=4, assigned to terminal v with phi(v)=2q-3 and phi(u)>=phi(v). Then phi(u) is 2q-3 or 2q-2. On the chosen maximum u-ending path, if phi(u)=2q-2 the sole e-contact is necessarily x at the unique central joint. If phi(u)=2q-3, either the sole contact is v at joint r_{q-2}∩r_{q-1}, or it is x in one of the three central slots around r_{q-1}.

                    • [1000964] In the rising low-terminal branch the three high edges are disjoint two-sided chords
                        STATEMENT
                        Retain the surviving one-low odd-central 0-1-1 state, with low edge
                          e={x,v,C}
                        of rank q, where phi(v)=2q-3 and C is the sole P_v-contact. Suppose the opposite terminal rises:
                          phi(C)=2q-2.
                        
                        Let
                          R=(r_1,...,r_{2q-2})
                        be the globally chosen maximum C-ending path. By 436d55f14de2,
                          x=r_{q-1}∩r_q
                        is the sole e-contact on R, and v is absent from R.
                        
                        Let h_1,h_2,h_3 be the three rank-(q+1) 0-1-1 high edges through v. Then every h_i meets each of the two halves
                          R_L=(r_1,...,r_{q-1}),
                          R_R=(r_q,...,r_{2q-2}).
                        
                        Moreover h_i contains exactly one non-v vertex in R_L and exactly one non-v vertex in R_R. Thus the three high edges form three pairwise vertex-disjoint two-sided chords across the central cut of R.

                      • [1000233] The rising low-terminal branch has a pure four-slot cross-cut entrance gadget
                          STATEMENT
                          In the rising low-terminal branch of d734b1420b2f, let
                            R=(r_1,...,r_{2q-2})
                          be the chosen maximum C-ending path with
                            x=r_{q-1}∩r_q,
                          and let h_i={y_i,v,z_i}, i=1,2,3, be the three rank-(q+1) high edges. Then each entrance y_i belongs to exactly one of the four central slots
                            L=r_{q-2}∩r_{q-1},
                            A=private(r_{q-1}),
                            B=private(r_q),
                            R'=r_q∩r_{q+1}.
                          The central joint x itself is impossible.
                          
                          The three entrances are distinct, so they occupy three of these four slots. For each high edge, its opposite terminal z_i lies on the half of R opposite its entrance.

                        • [1000072] The rising four-slot gadget orders the two far terminals on its fully occupied side
                            STATEMENT
                            In the rising low-terminal four-slot gadget 33522a8389e9, suppose the two left slots
                              L=r_{q-2}∩r_{q-1},
                              A=private(r_{q-1})
                            are both occupied as entrances of high edges
                              h_L={L,v,z_L}, h_A={A,v,z_A}.
                            Let k_L,k_A be the first right-half path-edge indices containing z_L,z_A. Then
                              k_L<=k_A.
                            Moreover z_L does not lie on r_q, so k_L>=q+1.
                            
                            Dually, if both right slots
                              B=private(r_q),
                              R'=r_q∩r_{q+1}
                            are occupied, and i_B,i_R are the last left-half occurrence indices of their opposite terminals, then
                              i_R>=i_B,
                            with the terminal of the joint-side entrance R' strictly left of r_{q-1}.

                      • [1000424] The rising low-terminal odd-boundary branch is impossible
                          STATEMENT
                          In the surviving one-low p=2q-3 0-1-1 state, the low opposite terminal cannot have phi(C)=2q-2. On its chosen (2q-2)-edge C-path the three high edges are two-sided chords with sources in four central slots L,A,B,R around the low source x. Either joint source L or R directly splices with its opposite-half terminal to give a path of length at least q ending at x, contradicting phi(x)=q-1. Thus only private source slots A,B remain, insufficient for three distinct high sources.

                        • [1001075] The flat low-terminal branch is theta-or-terminal-central
                            STATEMENT
                            In the surviving one-low odd-boundary 0-1-1 state with flat opposite terminal phi(C)=phi(v)=2q-3, the reciprocal C-path has only two structural types. If its sole low-edge contact is the source x, then the C-path and the clean x-source rail share at least two vertices and hence contain a lens. Otherwise the sole contact is terminal v at the forced central joint r_{q-2}∩r_{q-1}. Thus the flat branch reduces to a theta branch and one symmetric terminal-terminal branch.

                      • [1001090] The rising one-low branch becomes a four-slot oriented-chord conflict system
                          STATEMENT
                          If the low opposite terminal C has phi(C)=2q-2, then on its chosen maximum path the three high rank-(q+1) sources occupy three distinct slots among L=joint(q-2,q-1), A=private(q-1), B=private(q), R=joint(q,q+1), around the central low entrance x. Each high edge is a two-sided chord. A left-joint source L paired with any right source forces either its own terminal into r_q or the right source terminal into the left prefix; symmetrically for R. In source patterns {L,B,R} or {L,A,R}, linearity removes the central escape and forces both opposite terminals across the cut.

                      • [1001147] The rising low-terminal branch recreates an all-visible four-slot crossed-chord gadget
                          STATEMENT
                          Retain the rising branch of d734b1420b2f. Thus
                            e={x,v,C}
                          has rank q,
                            phi(C)=2q-2,
                          and the chosen maximum C-ending path is
                            R=(r_1,...,r_{2q-2}),
                          with
                            x=r_{q-1}∩r_q
                          the sole e-contact and v absent.
                          
                          Let
                            h_i={y_i,v,z_i}, i=1,2,3,
                          be the three rank-(q+1) 0-1-1 high edges. Then their entrances y_i are three distinct vertices among the four slots
                            a=r_{q-2}∩r_{q-1},
                            b=private(r_{q-1}),
                            c=private(r_q),
                            d=r_q∩r_{q+1}.
                          Moreover:
                          - if y_i∈{a,b}, then z_i lies in the right half V(r_q∪...∪r_{2q-2});
                          - if y_i∈{c,d}, then z_i lies in the left half V(r_1∪...∪r_{q-1}).
                          
                          Thus the three high edges form an all-visible three-of-four central entrance gadget, and each is a two-contact chord crossing the central cut.

                  • [1001146] The surviving low C-terminal rotation forces the next joint to top potential
                      STATEMENT
                      In the surviving one-low odd-central 0-1-1 state, let p=phi(v)=2q-3 and let the unique rank-q edge be
                        e={x,v,C},
                      where x is the unique entrance, x∉V(P_v), and
                        C=g_{q-2}∩g_{q-1}
                      is the sole P_v-contact of e.
                      
                      Then the charged endpoint rotation along P_v forces
                        phi(E)>=p,
                      where
                        E=g_{q-1}∩g_q.
                      
                      Consequently, if E is occupied by one of the rank-(q+1) high single contacts, E cannot be that high edge's entrance (whose potential would be q); it must be its opposite terminal.

              • [1000286] Every source-clean rail in a two-rank 0-1-1 block crosses every foreign edge
                  STATEMENT
                  Let e_i={x_i,v,u_i} be 0-1-1 ascending nonspecial edges through common assigned terminal v, with ranks in {q,q+1}. For each i let Q_i be the chosen maximum clean source path ending at x_i. Then for every i!=j, e_j meets Q_i. Otherwise Q_i,e_i,e_j either exceeds phi(e_j) or is a longest e_j-path through the wrong terminal v. Hence a four-edge block creates twelve forced foreign contacts, each using x_j or u_j.

                • [1000198] Every foreign 0-1-1 contact manufactures an endpoint lens
                    STATEMENT
                    In a four-edge 0-1-1 consecutive-rank obstruction, every forced foreign contact of a source rail Q_i with e_j creates a two-vertex overlap with the chosen maximum endpoint path of the contacted vertex. An X-hit at x_j yields a source-source theta Q_i∩P_{x_j}; a U-hit at u_j yields a source-terminal theta Q_i∩P_{u_j}. Hence all twelve directed transversal incidences manufacture endpoint lenses.

                • [1000818] Source-clean rails in a two-rank 0-1-1 block are pairwise intersecting
                    STATEMENT
                    For any two 0-1-1 ascending edges through the same assigned terminal whose ranks lie in two consecutive levels, their chosen source-clean maximum endpoint paths intersect. If the first rail meets the second edge at its source, the source itself is common. If it meets only the opposite terminal, then disjoint rails would concatenate through that edge to a path ending at the first source longer than its endpoint potential. Hence a four-edge violation gives a K4 of pairwise-intersecting source rails, with some pair overlapping in at least two distinguished vertices.

                  • [1000579] Unique intersections remain aligned joints when maximum rail lengths differ by one
                      STATEMENT
                      Let Q be a maximum p-edge path ending at x and R a maximum (p+1)-edge path ending at y. If Q and R have exactly one common vertex w, then w is a joint on both paths at the same index: w=e_i∩e_{i+1}=f_i∩f_{i+1} for some i. Thus the aligned-joint rigidity of equal-length maximum rails extends exactly to the mixed consecutive-length case needed for two-rank 0-1-1 blocks.

                    • [1000393] A unique intersection of two maximum endpoint paths is an aligned joint
                        STATEMENT
                        Let Q=(e_1,...,e_a) and R=(f_1,...,f_b) be maximum endpoint paths ending at distinct vertices x and y, with phi(x)=a and phi(y)=b. If V(Q) intersect V(R)={w}, then w is a joint on both paths at the same index: there exists t with 1<=t<min(a,b) such that w=e_t intersect e_{t+1}=f_t intersect f_{t+1}. No hypothesis relating a and b is needed.

                      • [1000796] A contact with a maximum endpoint path manufactures a balanced endpoint lens
                          STATEMENT
                          Let Q be a maximum a-edge path ending at x, so phi(x)=a. Let y be a vertex of Q distinct from x, and let P be any maximum b-edge path ending at y, so phi(y)=b.
                          
                          Then Q and P have at least two common vertices. Moreover one can choose a common vertex z so that z,y are consecutive common vertices on the relevant y-side segments of Q and P, and the two z-to-y segments form a clean elementary lens with the same number of edges.
                          
                          Thus every occurrence of a vertex y on a maximum endpoint path Q canonically yields a balanced endpoint lens between Q and any chosen maximum y-path.

                        • [1000677] Every foreign contact in a four-edge 0-1-1 block is a balanced-lens certificate
                            STATEMENT
                            Let e_i={x_i,v,u_i}, i=1,2,3,4, be source-clean 0-1-1 ascending nonspecial edges through a common assigned terminal v, with ranks in two consecutive levels, and let Q_i be their chosen maximum source paths ending at x_i.
                            
                            For every ordered pair i!=j, choose any foreign contact
                            w in V(Q_i) intersect {x_j,u_j},
                            whose existence is guaranteed by complete foreign-edge transversality.
                            
                            Then Q_i and the chosen maximum endpoint path P_w share at least two vertices and contain a balanced elementary lens adjacent to w.
                            
                            In particular:
                            - if w=x_j, then P_w=Q_j may be used, so every directed source hit x_j in Q_i creates a balanced source-source lens between Q_i and Q_j;
                            - if w=u_j, the contact creates a balanced source-terminal lens between Q_i and P_{u_j}.
                            
                            Hence the twelve directed foreign-contact obligations in a four-edge 0-1-1 block are simultaneously twelve balanced-lens/no-piercing certificates.

                        • [1000166] A loose path refutes automatic production of a genuine endpoint lens
                            STATEMENT
                            Two maximum endpoint paths, one containing the other's last vertex, need not contain any genuine clean elementary lens. This remains false for arbitrarily long paths. The two-common-vertices conclusion of b35b0fd4e4cd is not refuted.

                      • [1001181] Reciprocal source-rail contacts force the balanced one-low terminal lens
                          STATEMENT
                          Let e_i={x_i,v,u_i} and e_j={x_j,v,u_j} be source-clean 0-1-1 edges through the same assigned terminal v, with maximum source paths Q_i,Q_j, and suppose each foreign edge meets the other source rail. If Q_i and Q_j have exactly one common vertex, then the cross-contacts are reciprocal-terminal: Q_i meets e_j at u_j and Q_j meets e_i at u_i.
                          
                          Consequently, in a one-low four-edge source-clean block with low edge e_0 and high edges e_1,e_2,e_3, if each Q_0,Q_i is uniquely intersecting, then u_0 lies on all three high rails and the high rails cannot all be pairwise uniquely intersecting. More precisely, if Q_i,Q_k and Q_j,Q_k are unique, then Q_i and Q_j share u_0 and u_k.
                          
                          In the minimal residue where Q_1,Q_3 and Q_2,Q_3 are unique and V(Q_1)∩V(Q_2)={u_0,u_3}, the vertices u_0,u_3 are internal on Q_1,Q_2, the two Q_1/Q_2 segments between them form a clean balanced lens, and u_0 occurs at the same joint index on Q_1,Q_2,Q_3.

                        • [1000263] Terminal-tail blocking pushes the flat terminal lens into the late high-rail zone
                            STATEMENT
                            In the minimal one-low high-rail lens state of 039d9d9cd8fd, on each high source rail Q_i of length q the low terminal u_0 lies in one of the final q-2 path edges, and every foreign high terminal u_j lying on Q_i lies in one of the final q-1 path edges. In particular the balanced terminal-terminal lens endpoints and the exterior high-terminal chord contacts are all excluded from the extreme early part of the high source rails.

                  • [1000916] A source hit forces a second source-rail intersection
                      STATEMENT
                      For two source-clean 0-1-1 edges through a common assigned terminal, if the source x_j of one edge lies on the other edge's chosen maximum source rail Q_i, then Q_i and Q_j share at least two vertices. Hence any pair of source rails with exactly one common vertex must contact each other's offending edges reciprocally through the opposite terminals u_i,u_j, never through the sources.

                    • [1000992] The simple source-rail graph has at most four edges
                        STATEMENT
                        For a four-edge 0-1-1 consecutive-rank violation, let G_s record source-rail pairs having exactly one common vertex. Then every edge of G_s lies in at most one triangle, so |E(G_s)|<=4. Hence at least two of the six rail pairs have at least two common vertices. If equality holds, G_s is either C4 or a triangle with one pendant edge, and the nonsimple pairs have explicitly shared opposite-terminal vertices forced by the simple U-U exchanges.

                      • [1000090] The extremal C4 rail skeleton carries two clean length-two bridges
                          STATEMENT
                          In the extremal C4 simple-rail skeleton, the two nonsimple rail pairs have explicit terminal boundaries and clean two-edge bridges: after relabeling, Q_1,Q_2 share u_3,u_4 and e_3,e_4 is a u_3-u_4 path through v otherwise disjoint from both rails; symmetrically Q_3,Q_4 share u_1,u_2 with bridge e_1,e_2. Hence any clean elementary lens bounded by those terminal pairs has balanced side length at least two.

                      • [1000956] The simple source-rail graph is triangle-free
                          STATEMENT
                          In a four-edge source-clean 0-1-1 consecutive-rank block, let G_s join two source rails exactly when they have a unique common vertex. Then G_s is triangle-free. Consequently |E(G_s)|<=4, and if |E(G_s)|=4 then G_s is necessarily a 4-cycle; the triangle-with-pendant extremal case is impossible.

                        • [1000638] The C4 source-rail residue forces a four-vertex diagonal overlap
                            STATEMENT
                            Assume the simple source-rail graph of a four-edge source-clean 0-1-1 consecutive-rank block is the 4-cycle 01,12,23,30, so the diagonal pairs are 02 and 13. Then one of the two diagonal pairs has source-only foreign contacts in both directions. Consequently that diagonal pair shares at least four distinct distinguished vertices: the two source endpoints of its own edges and the opposite terminals of the other two edges.

                • [1001125] Consecutive-rank source-clean common-terminal edges cross each other
                    STATEMENT
                    Let
                      e={x,v,u},  f={y,v,z}
                    be distinct ascending nonspecial edges sharing the terminal vertex v. Assume
                      phi(e)=q,
                      phi(f) in {q,q+1}.
                    Let R_e,R_f be chosen maximum paths with last vertices x,y respectively, of lengths phi(e)-1 and phi(f)-1, such that R_e avoids v,u and R_f avoids v,z.
                    
                    Then
                      f intersects V(R_e)
                    and
                      e intersects V(R_f).
                    
                    Thus each source-clean edge meets the chosen maximum source path of the other; no assignment or terminal contact-multiplicity hypothesis is required.

                • [1001128] Four 0-1-1 source rails force a two-vertex distinguished overlap
                    STATEMENT
                    For four source-clean 0-1-1 edges through one assigned terminal, with ranks in any two consecutive levels, choose their clean source rails Q_i. Then some pair Q_i,Q_j shares at least two distinct vertices among the eight non-v source/terminal vertices of the four edges. This follows purely by double counting: each rail contains its own source plus one vertex from each of the other three disjoint source-terminal pairs, giving four 4-subsets of an 8-set and total pair-intersection mass at least 8.

                  • [1000261] Clean lenses between maximum source rails are balanced
                      STATEMENT
                      Let Q,R be maximum endpoint paths ending at x,y. If two common vertices bound a clean lens whose two alternative segments are internal to both rails, then the two segments have equal edge length: replacing a shorter segment by the longer one would create a path ending at the same source longer than its endpoint potential. If a source endpoint lies on the lens, the corresponding endpoint-preserving replacement still gives the appropriate one-sided segment inequality.

                    • [1000805] A third cross-edge cannot pierce a balanced lens between maximum rails
                        STATEMENT
                        Let two maximum endpoint paths contain a clean internal lens whose two sides have equal length. No hyperedge can have one contact in the interior of each lens side and otherwise be disjoint from the two host rails. The two hybrid routes obtained by crossing through that edge have total length two more than the two original lens sides, so one hybrid is longer and gives an endpoint-preserving path longer than one of the maximum rails.

                      • [1001203] Lens non-piercing continuation
                          STATEMENT
                          Route bridge: the source-rail lens analysis continues after toolkit lemma 1000412.

                  • [1000398] Four source rails force two units of distinguished overlap
                      STATEMENT
                      In a four-edge source-clean 0-1-1 block, let Q_1,...,Q_4 be the four maximum source rails and let a_ij be the number of distinguished source-or-opposite-terminal vertices shared by Q_i and Q_j. Then either two distinct rail pairs satisfy a_ij>=2, or one rail pair satisfies a_ij>=3. Equivalently, the four-rail obstruction contains at least two units of overlap beyond a single two-vertex theta witness.

                    • [1000744] Source-hit imbalance exactly measures excess distinguished rail overlap
                        STATEMENT
                        For four source-clean 0-1-1 edges e_j={x_j,v,u_j} and their four maximum source rails Q_i, let s_j be the number of foreign rails Q_i, i!=j, that meet e_j at the source x_j. Let a_ik be the number of distinguished vertices among {x_j,u_j:1<=j<=4} shared by Q_i and Q_k. Then sum_{i<k} a_ik = 8 + sum_{j=1}^4 (s_j-1)^2. In particular the distinguished overlap mass is exactly 8 iff every source x_j lies on exactly one foreign rail.

                    • [1000957] Every four-edge two-rank source block has two lens cells and reciprocal simple pairs
                        STATEMENT
                        Consider four source-clean 0-1-1 edges through one assigned terminal, with ranks in two consecutive levels, and their four maximum source rails. The rail intersection graph is K_4. Counting elementary cells between consecutive common vertices with multiplicity over rail pairs, there are at least two lens cells. Moreover every rail pair having exactly one common vertex meets at an aligned same-index joint, and the two corresponding offending edges cross the opposite rail only at their opposite terminals. Thus after extracting two lens cells, every remaining simple rail-pair interaction is reciprocal-terminal.

                    • [1001165] Distinguished agreements and offending cross-edges are complementary
                        STATEMENT
                        Fix two source rails Q_i,Q_j in a four-edge source-clean 0-1-1 block. For each offending edge e_k={x_k,v,u_k}, each rail contains exactly one of x_k,u_k. If the two rails choose the same member, that vertex is a distinguished common vertex of Q_i,Q_j. If they choose different members, e_k itself has one non-v vertex on each rail and is an offending cross-edge between them. Consequently, if a_ij is the number of shared distinguished vertices, exactly 4-a_ij of the four offending edges cross Q_i and Q_j at two distinct distinguished contacts.

              • [1000620] The clean-minus-double defect is bounded by the number of 0-1-1 ascending edges
                  STATEMENT
                  Choose maximum endpoint paths P_v and let C,D be the clean- and double-incidence counts of the contact-snake identity. Let N_011 be the number of ascending nonspecial edges e={x,u,v} whose contact signature on the three chosen endpoint paths is
                     (mu_x(e),mu_u(e),mu_v(e))=(0,1,1),
                  where x is the unique entrance.
                  
                  Then
                     C-D <= N_011.
                  
                  Consequently, if
                     N_011 <= (3/4) sum_v phi(v),
                  then
                     m <= (11/12) sum_v phi(v)-n/3,
                  and every P_ell-free linear triple system satisfies
                     m <= ((11ell-15)/12)n.

              • [1000779] Four mutually blocking high entrance rails force a two-vertex overlap
                  STATEMENT
                  Let h_i={y_i,v,z_i}, i=1,2,3,4, be four rank-(q+1) ascending nonspecial edges through one common terminal v, with phi(y_i)=q, and let Q_i be canonical q-edge entrance rails. Then some pair Q_i,Q_j has at least two distinct common vertices. The proof uses foreign-edge transversality, a pigeonhole on one target edge, and repeated unique-intersection alignment.

            • [1000764] A defect-corrected consecutive-rank block is sufficient for the 11/12 bound
                STATEMENT
                Fix, for every vertex v with p=phi(v), a maximum endpoint path P_v. For a charged ascending edge e={x,v,u} assigned to v (so phi(u)>=p), call e double at v if both x and u lie on P_v.
                
                For each rank r let
                  n_r(v)=number of assigned charged edges of rank r,
                  d_r(v)=number of those edges that are double at v.
                
                Suppose that for every v and every consecutive rank pair {q,q+1},
                  [n_q(v)-d_q(v)] + [n_{q+1}(v)-d_{q+1}(v)] <= 3.   (*)
                
                Then the same consecutive-level pairing used in 2665d2c81d39 gives
                  a(v)-D_v <= (3/4)phi(v)
                after the same bottom-level residue corrections, where
                  a(v)=sum_r n_r(v)
                and D_v is the total double-contact incidence count at v.
                
                Consequently
                  A-D <= (3/4)sum_v phi(v),
                and hence
                  m <= (11/12)sum_v phi(v)-n/3
                by bed2a5868628.
                
                Even the corresponding +1 residue fallback suffices for leading coefficient 11/12.

              • [1000330] At the odd central boundary four single contacts cannot occupy both rightmost slots
                  STATEMENT
                  Let v have p=phi(v)=2q-3 with q>=4, and fix a maximum p-edge path P=(g_1,...,g_p) ending at v. Suppose four assigned potential-charged ascending edges of ranks in {q,q+1} are all single-contact relative to P.
                  
                  Write the seven rank-(q+1) central slots as
                   A=g_{q-3}∩g_{q-2},
                   B=private(g_{q-2}),
                   C=g_{q-2}∩g_{q-1},
                   D=private(g_{q-1}),
                   E=g_{q-1}∩g_q,
                   F=private(g_q),
                   G=g_q∩g_{q+1}.
                  
                  Then F and G cannot both be occupied by the four single contacts.

                • [1000521] The G-only odd-central four-single state is an exact loss-one normal form
                    STATEMENT
                    In the odd-central state p=phi(v)=2q-3, suppose four assigned charged edges of ranks {q,q+1} are all single-contact on a fixed maximum v-path P, and suppose the right joint
                      G=g_q∩g_{q+1}
                    is occupied while the right private slot F=private(g_q) is not.
                    
                    Then the four occupied slots are exactly
                      A=g_{q-3}∩g_{q-2},
                      B=private(g_{q-2}),
                      C=g_{q-2}∩g_{q-1},
                      G=g_q∩g_{q+1}.
                    Moreover:
                    (1) G is the visible entrance of a rank-(q+1) edge h_G and phi(G)=q;
                    (2) C is terminal-only;
                    (3) the A- and B-edges have rank q+1;
                    (4) writing e_C for the C-edge, the sequence
                        g_1,...,g_{q-2},e_C,h_G
                        is a q-edge path ending in h_G through the wrong terminal v, hence an exact loss-one wrong-entrance state for h_G.
                    
                    If either A or B is also terminal-only, its two-sided terminal-only spacing with C is attained at equality.

                • [1000621] At p=2q-3 a four-single rank-pair obstruction cannot occupy the right-joint slot
                    STATEMENT
                    Let phi(v)=2q-3 with q>=4 and let four assigned charged ascending edges of ranks in {q,q+1} all be single-contact on a fixed maximum v-path. In the seven-slot odd-central window A,...,G, the rightmost joint G=g_q∩g_{q+1} cannot be occupied. If G were occupied, the clean-joint hole rule and the F,G exclusion force the other contacts to A,B,C with C terminal-only; then g_1,...,g_{q-3},h_A,h_C,g_{q-1},g_q is a (q+1)-edge path ending at G, contradicting phi(G)=q.

                  • [1000365] At p=2q-3 a four-single rank-pair obstruction cannot occupy the right-private slot
                      STATEMENT
                      Under the p=2q-3 four-single rank-pair hypotheses with q>=4, the private right slot F=private(g_q) cannot be occupied. Since F is a clean rank-(q+1) entrance it empties B; splitting on the label/occupancy of E, the remaining star contacts always contain one of the bridge pairs {A,C}, {A,D}, or {C,E}, each producing a (q+1)-edge path ending at F and contradicting phi(F)=q. Together with the G-slot elimination, every four-single obstruction is confined to A,B,C,D,E.

                  • [1000625] At the odd central boundary a four-single obstruction cannot occupy the right-private slot
                      STATEMENT
                      Let v have phi(v)=2q-3, q>=4, and suppose four assigned potential-charged ascending edges of ranks in {q,q+1} are all single-contact on a fixed maximum v-path P. In the seven-slot notation
                       A,J_{q-3}; B,P_{q-2}; C,J_{q-2}; D,P_{q-1}; E,J_{q-1}; F,P_q; G,J_q,
                      the right-private slot F=private(g_q) cannot be occupied.
                      
                      Together with 8d1adea102fe, every four-single odd-central obstruction is confined to the five slots A,B,C,D,E.

                  • [1001035] Pure-high odd-boundary four-single states force terminal central joints and loss-one witnesses
                      STATEMENT
                      At p=2q-3, if four assigned 0-1-1 rank-(q+1) edges are all single-contact on one maximum v-path, their contacts occupy four of A,B,C,D,E. Whenever E is occupied it is terminal-only; whenever A and C are both occupied, C is terminal-only. Thus every state has a terminal-only central joint. If B or D is the omitted slot, then both C and E are terminal-only, and g_1,...,g_{q-2},h_C,h_E is an exact q-edge wrong-entrance path into a rank-(q+1) edge.

                    • [1000059] Every pure-high odd-boundary four-single state is an exact loss-one wrong-entrance state
                        STATEMENT
                        At p=2q-3, any four assigned 0-1-1 rank-(q+1) edges that are all single-contact on a maximum v-path necessarily yield a q-edge path ending in one of those rank-(q+1) edges through terminal v rather than its unique entrance. Thus every pure-high four-single obstruction is canonically a loss-one wrong-entrance state.

                      • [1000977] REFUTED: equal-rank competitor does not automatically block a loss-one wrong-entrance precursor
                          STATEMENT
                          Refuted. In a q-edge path R,h ending in h through the common terminal v, the last precursor edge of R contains v. Therefore another edge f through v is automatically not disjoint from R, and the proposed extension R,h,f has a nonconsecutive repeated v-contact between the last precursor edge and f. The argument cannot force f to have any additional precursor contact.

                  • [1001102] At p=2q-3 a four-single rank-pair obstruction cannot occupy the right-private slot
                      STATEMENT
                      Let p=phi(v)=2q-3 with q>=4, and fix a maximum path
                         P=(g_1,...,g_p)
                      ending physically at v. Use the seven-slot notation
                         A=g_{q-3}∩g_{q-2},
                         B=private(g_{q-2}),
                         C=g_{q-2}∩g_{q-1},
                         D=private(g_{q-1}),
                         E=g_{q-1}∩g_q,
                         F=private(g_q),
                         G=g_q∩g_{q+1}.
                      
                      Suppose four assigned potential-charged ascending edges of ranks in {q,q+1} are all single-contact relative to P.
                      
                      Then F cannot be occupied.
                      
                      Combined with 8d1adea102fe, neither F nor G can be occupied; hence every four-single obstruction at p=2q-3 is confined to the five slots A,B,C,D,E.

                    • [1000539] At the odd boundary a one-low four-single obstruction pins the low witness to C
                        STATEMENT
                        Let p=phi(v)=2q-3 with q>=4, and fix a maximum path
                           P=(g_1,...,g_p)
                        ending physically at v. Use
                           A=g_{q-3}∩g_{q-2},
                           B=private(g_{q-2}),
                           C=g_{q-2}∩g_{q-1},
                           D=private(g_{q-1}),
                           E=g_{q-1}∩g_q.
                        
                        Assume four assigned charged ascending nonspecial edges are all single-contact on P and have rank pattern
                           q,(q+1),(q+1),(q+1).
                        By 8d1adea102fe and f378e6022301 their witnesses all lie in A,B,C,D,E.
                        
                        Then the sole rank-q edge has witness C. In particular its witness cannot be D or E.
                        
                        Thus every remaining one-low all-single obstruction has a central low edge whose sole P-contact is C; C may be either its visible entrance or its opposite terminal.

              • [1000592] At p=2q-3 the unique low edge cannot use the private middle witness
                  STATEMENT
                  Let p=phi(v)=2q-3 with q>=4 and fix a maximum p-edge path P=(g_1,...,g_p) ending at v. Suppose four assigned charged ascending edges of ranks in {q,q+1} are all single-contact on P, with exactly one rank-q edge e.
                  
                  Use
                   A=g_{q-3}∩g_{q-2},
                   B=private(g_{q-2}),
                   C=g_{q-2}∩g_{q-1},
                   D=private(g_{q-1}),
                   E=g_{q-1}∩g_q.
                  
                  Then the rank-q edge cannot have witness D.

              • [1000665] At p=2q-3 terminal-only non-double witnesses are pushed to the left central slots
                  STATEMENT
                  Let phi(v)=2q-3 and fix a maximum v-ending path P. For a charged ascending edge through terminal v that is non-double on P: (i) if its rank is q and its entrance is absent, its opposite-terminal witness is forced to the unique joint g_{q-2}∩g_{q-1}; (ii) if its rank is q+1 and its entrance is absent, its opposite-terminal witness can occur only privately in g_{q-2} or g_{q-1}, or at one of the joints g_{q-3}∩g_{q-2}, g_{q-2}∩g_{q-1}, g_{q-1}∩g_q. In particular the private g_q slot and joint g_q∩g_{q+1} are entrance-only for non-double high edges.

              • [1000696] At the odd central boundary terminal-only single contacts lose the rightmost witness slots
                  STATEMENT
                  Let v have p=phi(v)=2q-3, q>=3, and let
                    P=(g_1,...,g_p)
                  be a maximum path ending at v.
                  
                  Let e={x,v,u} be a potential-charged ascending nonspecial edge assigned to v, assume e is not double on P, and suppose its unique P-contact outside the last edge is the opposite terminal u while its entrance x is absent.
                  
                  If phi(e)=q, then
                    u=g_{q-2}∩g_{q-1}.
                  
                  If phi(e)=q+1, then:
                  - if u is private to g_i, q-2<=i<=q-1;
                  - if u=g_i∩g_{i+1}, q-3<=i<=q-1.
                  
                  In particular a terminal-only rank-(q+1) single contact cannot occupy private(g_q) or the joint g_q∩g_{q+1}; those rightmost witness slots are entrance-only.

                • [1000244] Two non-double rank-q edges at p=2q-3 have a two-pattern middle-edge normal form
                    STATEMENT
                    Let v have phi(v)=2q-3 and fix a maximum path
                      P=(g_1,...,g_{2q-3})
                    ending physically at v.
                    
                    Suppose two distinct potential-charged ascending nonspecial rank-q edges through v are both non-double on P. Put
                      A=g_{q-2}∩g_{q-1},
                      B=private(g_{q-1}),
                      C=g_{q-1}∩g_q.
                    
                    Then their two distinct single-contact witnesses are exactly one of
                      {A,B} or {B,C}.
                    
                    Moreover B is necessarily the unique entrance of its rank-q edge, so
                      phi(B)=q-1.

                  • [1000050] The forced middle-private low entrance raises the outer right joint to full terminal potential
                      STATEMENT
                      Let v have p=phi(v)=2q-3 with q>=4, and let
                        P=(g_1,...,g_p)
                      be a maximum path ending physically at v.
                      
                      Suppose f={B,v,u} is an ascending nonspecial rank-q edge which is non-double on P and whose unique entrance
                        B=private(g_{q-1})
                      lies on P. Then u is absent from P and, putting
                        D=g_q∩g_{q+1},
                      one has
                        phi(D)>=p=2q-3.
                      
                      Consequently D cannot be the entrance of any rank-(q+1) ascending edge. In particular, in the two-rank-q saturation patterns of 35ee7b35de05, the outer right joint D is unavailable as a non-double charged witness of any rank in {q,q+1}.

                  • [1001216] Odd-boundary consecutive-rank four-edge normal form
                      STATEMENT
                      Let q>=4, p=2q-3, and let P be a maximum p-edge path ending at v. For four potential-charged ascending nonspecial edges at v with ranks in {q,q+1}: if at least two have rank q, then some edge is double on P. If exactly one has rank q and all four are single on P, then its sole contact is C=g_{q-2}∩g_{q-1}, C is its opposite terminal and its unique entrance is off P; E=g_{q-1}∩g_q is unoccupied; the three rank-(q+1) contacts are A=g_{q-3}∩g_{q-2}, B=private(g_{q-2}), D=private(g_{q-1}); and the D-edge is terminal-only with its entrance off P.

                    • [1000004] High 0-1-1 edges at the odd boundary have reciprocal central-gate normal forms
                        STATEMENT
                        Let h={y,v,z} be a 0-1-1 ascending edge of rank q+1 with q>=5, phi(v)=2q-3 and phi(z)>=phi(v). Then phi(z) is one of 2q-3,2q-2,2q-1,2q. On the chosen maximum z-path, the sole h-contact is forced into an explicit central window. At phi(z)=2q the source y is the unique central joint; at 2q-1 either y lies in the three central slots or v is the central joint; at 2q-2 and 2q-3 the contact lies in the corresponding five- or seven-slot central window.

                    • [1000217] The final one-low odd-boundary state creates a four-vertex high-potential central packet
                        STATEMENT
                        In the surviving p=2q-3 one-low 0-1-1 state, the occupied contacts are A,B,C,D, with both C and D terminal-only. Let
                          e_C={x_C,v,C}
                        have rank q and
                          e_D={x_D,v,D}
                        have rank q+1,
                        where x_C,x_D are their absent unique entrances.
                        
                        Then charged endpoint rotations of P_v give
                          phi(E)>=p,   E=g_{q-1}∩g_q,
                          phi(G)>=p,   G=g_q∩g_{q+1},
                        with p=2q-3.
                        
                        Since C and D are opposite terminals of edges assigned to v, also
                          phi(C)>=p, phi(D)>=p.
                        Hence the four vertices C,D,E,G, lying in the three consecutive central path edges g_{q-1},g_q,g_{q+1}, all have endpoint potential at least p.

                      • [1000775] High 0-1-1 terminal paths have a four-level reciprocal central normal form
                          STATEMENT
                          Let h={y,v,D} be a 0-1-1 ascending nonspecial edge of rank q+1 with q>=5, unique entrance y, and terminals v,D. Suppose
                            s=phi(D)>=2q-3.
                          Then s<=2q and, on the globally chosen maximum D-ending path
                            R=(r_1,...,r_s),
                          the unique h-contact has the following central localization.
                          
                          If the contact is the terminal v:
                          - s=2q: impossible;
                          - s=2q-1: v is necessarily the joint r_{q-1}∩r_q;
                          - s=2q-2: v is private in r_{q-1}, or a joint r_i∩r_{i+1} with i in {q-2,q-1};
                          - s=2q-3: v is private in r_i with i in {q-2,q-1}, or a joint with i in {q-3,q-2,q-1}.
                          
                          If the contact is the entrance y:
                          - s=2q: y is necessarily the central joint r_q∩r_{q+1};
                          - s=2q-1: y is private in r_q, or a joint with i in {q-1,q};
                          - s=2q-2: y is private in r_i with i in {q-1,q}, or a joint with i in {q-2,q-1,q};
                          - s=2q-3: y is private in r_i with i in {q-2,q-1,q}, or a joint with i in {q-3,q-2,q-1,q}.
                          
                          In particular every reciprocal D-path state is confined to O(1) central slots, and the maximal-potential case s=2q forces the entrance y at the exact central joint.

                    • [1000575] The terminal-only D contact forces the outer right joint to top potential
                        STATEMENT
                        Retain the sole surviving one-low odd-boundary state at
                          p=phi(v)=2q-3, q>=4,
                        with
                          P=(g_1,...,g_p)
                        maximum at v and occupied slots A,B,C,D. Let
                          h_D={y_D,v,D}
                        be the rank-(q+1) edge whose sole P-contact
                          D=private(g_{q-1})
                        is terminal-only, as in 512f6864eb96.
                        
                        Then the charged endpoint rotation at v yields a p-edge path ending at
                          G=g_q∩g_{q+1}.
                        Hence
                          phi(G)>=p=2q-3.
                        
                        Thus the residual state has two adjacent full-potential rotation endpoints
                          E=g_{q-1}∩g_q,
                          G=g_q∩g_{q+1},
                        with phi(E),phi(G)>=p.

                    • [1001207] The final odd-boundary residue forces a completely top-potential central edge
                        STATEMENT
                        In the final one-low odd-boundary 0-1-1 residue with p=2q-3, the terminal-only C- and D-rotations produce p-edge paths ending at the successive central joints E=g_{q-1}∩g_q and G=g_q∩g_{q+1}. Hence phi(E),phi(G)>=p. The same C-rotation also gives the private vertex F of g_q as a last vertex, so phi(F)>=p. Therefore every vertex of g_q has endpoint potential at least p, and the rotation ending in g_q shows phi(g_q)>=p.

              • [1000787] The defect-corrected two-rank block is automatic at the half-rank top boundary
                  STATEMENT
                  Let v have
                    p=phi(v)=2q-2,
                  and fix a maximum p-edge endpoint path P_v.
                  
                  Suppose four potential-charged ascending edges assigned to v have ranks in {q,q+1}. Let n_r be their rank counts and d_r the number among them that are double contacts on P_v.
                  
                  Then
                    (n_q-d_q)+(n_{q+1}-d_{q+1}) <= 1.
                  In particular the defect-corrected consecutive-rank block bound <=3 holds with two units to spare.

          • [1000922] The entire contact-snake defect reduces to 0-1-1 ascending edges
              STATEMENT
              With one maximum endpoint path P_v chosen at every vertex, call an ascending nonspecial edge e={x,y,z} a 0-1-1 edge when x is its unique entrance, mu_x(e)=0, and mu_y(e)=mu_z(e)=1. Let U be the number of such edges. Then 3m<=(2ell-3)n+U for every P_ell-free linear triple system. Consequently U=O(n) would imply ex_L(n,P_ell^(3))<=(2/3)ell n+O(n), while any bound U<=(1-epsilon)m+O(n) with fixed epsilon>0 already improves the leading coefficient below one.

            • [1000748] A three-per-two-ranks bound for 0-1-1 edges alone gives the 11/12 coefficient
                STATEMENT
                Assign every 0-1-1 ascending edge to a minimum-potential terminal v. If for every v and q at most three assigned 0-1-1 edges have ranks in {q,q+1}, then U<=3/4 sum_v phi(v). Combined with the certified defect inequality 3m<=2 sum_v phi(v)-n+U, this gives m<=11/12 sum_v phi(v)-n/3 and therefore m<=((11ell-15)/12)n for every P_ell-free linear triple system.

      • [1000062] Nonspecial terminal snake incidences have cumulative bound 2q-3
          STATEMENT
          Let H be a finite linear 3-graph, let v be a vertex, and let 2<=q<=phi(v). Among nonspecial edges e for which v is a terminal snake vertex and phi(e)<=q, there are at most 2q-3. In particular, the total number t(v) of nonspecial edges for which v is a terminal satisfies t(v)<=max{0,2phi(v)-3}.

        • [1000461] Terminal nonspecial saturation forces double-blocker excess
            STATEMENT
            Let H be a finite linear 3-graph, let v have p=phi(v), and choose a maximum p-edge path P=(g_1,...,g_p) with last vertex v and last edge h=g_p. Let t(v) be the number of nonspecial edges for which v is a terminal. Let D(v) count those such edges e!=h for which both vertices of e\\{v} lie in V(P)\\h. If p>=3, then t(v)-D(v)<=2p-4. (For p=2 one has t(v)<=1.)

          • [1000742] A nonspecial terminal of rank q reduces the entire incident low-rank capacity
              STATEMENT
              Let H be a finite linear 3-graph and let h be a nonspecial edge of rank q≥2 with v terminal at h. Put J_q(v)={f∈E(H): v∈f and φ(f)≤q}. Then |J_q(v)|≤2q-3. For q=3 the stronger bound |J_3(v)|≤2 holds; for q=2, J_2(v)={h}. The counted edges need not be nonspecial or terminal at v. In particular, if q=φ(v), then d_D^-(v)≤2φ(v)-3.

            • [1000022] Near the seven-sixths floor, full-rank nonspecial terminal vertices have density at most three eta
                STATEMENT
                Let H be a finite linear 3-graph with phi(v)>=3 for every vertex and write
                  sum_v phi(v)=m+(7/6+eta)n,
                with eta>=0.
                
                Let F be the set of vertices v for which there exists a nonspecial edge h terminal at v with
                  phi(h)=phi(v).
                Then
                  |F|<=3 eta n.
                
                Equivalently, outside at most 3 eta n vertices, every nonspecial terminal edge e at v satisfies
                  phi(e)<=phi(v)-1.

            • [1000735] An ascending last edge gives a three-halves incident rank bound and an eleven-twelfths Turan bound
                STATEMENT
                Let H be a finite linear 3-graph. If h is ascending of rank q and v is terminal at h, then #{f containing v: phi(f)<=q}<=floor((3q-1)/2), with the stronger bounds 1 for q=2 and 2 for q=3. Writing n_+ for the number of nonisolated vertices, S=sum_v phi(v), A for the number of ascending edges, and m=|E(H)|, one has A<=(3S-n_+)/4 and m<=(11S-5n_+)/12. Hence for ell>=2, ex_L(n,P_ell^(3))<=((11ell-16)/12)n.

              • [1000340] First-edge contacts sharpen the eleven-twelfths bound
                  STATEMENT
                  Let H be a finite linear 3-graph. If h is an ascending edge of rank q and v is terminal at h, then #{f containing v: phi(f)<=q}<=floor((3q-2)/2) for q>=4; for q=2,3 the sharper bounds are 1 and 2. Consequently, if n_+ is the number of nonisolated vertices, S=sum_v phi(v), A is the number of ascending edges, and m=|E(H)|, then A<=(3S-2n_+)/4 and m<=(11S-6n_+)/12. Hence every P_ell^(3)-free linear 3-graph satisfies m<=((11ell-17)/12)n for ell>=2.

                • [1000163] Full endpoint conflict matching sharpens the fixed-entrance incident-rank bound
                    STATEMENT
                    If h is an ascending edge of rank q in a finite linear 3-graph and v is terminal at h, then for q>=4
                    |J_q(v)| <= floor((3q-3)/2),
                    where J_q(v)={f: v in f and phi(f)<=q}. For q=2,3 the sharper bounds are 1 and 2. Consequently, with S=sum_v phi(v), n_+ the number of nonisolated vertices, E_even the number of nonisolated vertices of even rank, N_3 the number of vertices of rank 3, A the number of ascending edges, and m=|E(H)|,
                    A <= (3S-3n_+-E_even-2N_3)/4
                    and
                    m <= (11S-7n_+-E_even-2N_3)/12.
                    Hence every P_ell^(3)-free linear 3-graph satisfies m<=((11ell-18)/12)n.

                • [1000904] The full contact-conflict graph improves the leading coefficient to 43/48
                    STATEMENT
                    Let h be an ascending edge of rank q and v a terminal. Using the full singleton-contact conflict graph around a longest h-path, rather than only a disjoint matching of conflicts, one obtains |{f containing v: phi(f)<=q}| <= (11/8)q+3/2. Consequently A<=(11/16)sum_v phi(v)+(3/4)n_+, and the standard incidence inequality gives m<=(43/48)sum_v phi(v)-n_+/12. Hence every P_ell^(3)-free linear 3-graph satisfies m<=((43ell-47)/48)n.

                  • [1000012] Shortcut map and amplification program from Astra direct proof
                      STATEMENT
                      After Astra's recovered direct proof, the earliest natural shortcut is immediately after the old low-rank terminal-capacity lemma a570ca900001: strengthen its path-contact count using ascendingness, then sum globally. The later potential-charged/0-1-1 machinery is unnecessary for 11/12. Moreover Astra's splice supports a stronger full conflict graph, already yielding the pending 43/48 leading coefficient caeba14e4f6b. Further improvement requires exploiting ascending labels, multiple rotated path states, or rank-sensitive incidence accounting rather than only optimizing endpoint constants.

                  • [1000738] Run counting replaces the contact transfer and extends the coefficient improvement to every uniformity
                      STATEMENT
                      For each integer r>=3, put c_r=1-(2r-1)/(8r(r-1)) and d_r=(4r^2-10r+1)/(4r(r-1)). Every finite linear r-graph with m edges, n_+ nonisolated vertices, and S=sum_v phi(v) satisfies m<=c_r S-d_r n_+. Hence ex_L(n,P_ell^(r)) <= [c_r(ell-1)-d_r]n for ell>=2. The underlying local bound is |J_q(v)|<=(6r-7)q/8+(7-2r)/4 at a terminal of an ascending rank-q edge. An elementary run decomposition proves singleton density (2r-3)/4 and replaces the four-state transfer. Leading coefficients for r=3,4,5 are 43/48,89/96,151/160.

                    • [1000239] Ordered common-terminal edges force quadratic total entrance rank in every uniformity
                        STATEMENT
                        Let H be a finite linear r-graph with r>=3. Let v be a vertex of rank p, and let e_1,...,e_k be distinct ascending nonspecial edges terminal at v. Assume that, for every e_i, the vertex v has minimum vertex rank among the r-1 terminal vertices of e_i. Write q_i=phi(e_i), let x_i be the unique entrance of e_i, and relabel so that q_1<=...<=q_k.
                        
                        Then the sets e_i\{v} are pairwise disjoint and, for every i,
                          q_i >= ceil((8i+4r-14)/(6r-7)).
                        Consequently
                          sum_{i=1}^k phi(x_i)
                          >= sum_{i=1}^k [ceil((8i+4r-14)/(6r-7))-1]
                          >= [4k^2-(2r+3)k]/(6r-7).
                        
                        Moreover, besides x_i each edge e_i contains r-2 terminal vertices, all of rank at least p. These (r-2)k vertices are mutually distinct and disjoint from the entrances. Hence
                          sum_{z in union_i(e_i\{v})} phi(z)
                          >= (r-2)pk
                             + sum_{i=1}^k [ceil((8i+4r-14)/(6r-7))-1].
                        
                        In particular, a common-terminal family of size k=Theta(p) forces total vertex rank Theta(p^2) on pairwise distinct vertices outside v.

                    • [1000492] The contact-multiplicity snake and unpaid-edge reduction extend to arbitrary uniformity
                        STATEMENT
                        For every finite linear r-uniform hypergraph, choose one maximum endpoint path P_v at each nonisolated vertex and define contact multiplicities mu_v(e). Let C count clean incidences mu=0 and X=sum max(mu-1,0) be total excess contact multiplicity. Then rm-C+X <= (r-1)sum_v phi(v)-(r-2)n_+. Moreover C-X is bounded by the number of ascending nonspecial edges whose chosen-path signature is (0,1,...,1): clean at the unique entrance and single at all r-1 terminals. Hence rm <= (r-1)S-(r-2)n_+ + N_{0,1^{r-1}}.

                      • [1000484] Single-contact central windows give a two-envelope local bound in every uniformity
                          STATEMENT
                          Let H be a finite linear r-graph, r>=3. Fix a nonisolated vertex v of rank p and a maximum p-edge path
                            P=(g_1,...,g_p)
                          with last vertex v and last edge h=g_p. For an incident edge e!=h put
                            mu_v(e)=|(e\{v}) intersect (V(P)\h)|.
                          
                          Let e be an ascending nonspecial edge of rank s<p at which v is terminal, and suppose mu_v(e)=1. Let c be its unique contact with V(P)\h, and let a and b be the first and last indices of path edges containing c. Then
                            a<=s-1,
                            b>=p-s+2.
                          If c is a terminal vertex of e rather than its unique entrance, then in fact a<=s-2.
                          
                          Consequently, for q<p, if s_q(v;P) is the number of ascending nonspecial edges terminal at v, of edge rank at most q, and having mu_v(e)=1, then
                            s_q(v;P)
                            <= B_r(p,q)
                            := max{0,(r-1)(2q-p)-(2r-3)}.
                          
                          Now let t(v)>0 count all ascending nonspecial edges terminal at v, let q=q(v)<p be their maximum edge rank, and let
                            X_v=sum_{f contains v} max(mu_v(f)-1,0),
                          with mu_v(h)=1 as in the general contact-multiplicity inequality. Then
                            t(v)-X_v
                            <= min{
                                 ((6r-7)/8)q+(7-2r)/4,
                                 B_r(p,q)
                               }.
                          
                          Thus the two leading-order envelopes cross at
                            q/p = 8(r-1)/(10r-9).
                          More exactly, whenever B_r(p,q)>0 the central-window envelope is no larger than the fixed-entrance envelope if
                            q <= [8(r-1)p+2(6r-5)]/(10r-9).
                          For r=3, B_3(p,q)=max{0,4q-2p-3}, recovering the existing 3-uniform single-contact window.

                        • [1000373] Minimum-rank terminal assignment forces quadratic off-center rank in every uniformity
                            STATEMENT
                            Let H be a finite linear r-graph with r>=3. Fix a vertex v of rank p and a maximum p-edge path P ending at v. Let e_1,...,e_k be distinct ascending nonspecial edges terminal at v, all of edge rank less than p, and suppose every e_i has contact multiplicity one on P. Write q_i=phi(e_i), let x_i be the unique entrance of e_i, and relabel so that
                              q_1<=...<=q_k.
                            
                            Then for every i,
                              q_i >= ceil(((r-1)p+i+2r-3)/(2(r-1))),
                            and therefore
                              sum_{i=1}^k phi(x_i)
                              >= sum_{i=1}^k [
                                   ceil(((r-1)p+i+2r-3)/(2(r-1)))-1
                                 ]
                              >= kp/2 + k(k-1)/(4(r-1)).
                            
                            If, in addition, v has minimum vertex rank among the r-1 terminal vertices of every e_i, then all (r-1)k vertices in union_i(e_i\{v}) are distinct, and the r-2 terminal vertices of e_i other than v all have rank at least p. Hence
                              sum_{z in union_i(e_i\{v})} phi(z)
                              >= ((2r-3)/2)pk + k(k-1)/(4(r-1)).
                            
                            In particular this applies after assigning any family of globally unpaid signature-(0,1,...,1) ascending edges to a terminal of minimum vertex rank. For r=3 the entrance-rank conclusion becomes
                              sum_i phi(x_i) >= kp/2+k(k-1)/8,
                            the same numerical packet bound as the certified 3-uniform minimum-terminal lemma on the terminal-single subclass.

                          • [1001131] Terminal-single packets obey both central-window and fixed-capacity rank profiles
                              STATEMENT
                              Let H be a finite linear r-graph with r>=3. Fix a vertex v of rank p and a maximum p-edge path P ending at v. Let e_1,...,e_k be distinct ascending nonspecial edges terminal at v, each of edge rank less than p and each having contact multiplicity one on P. Write
                                q_i=phi(e_i)
                              and relabel so that q_1<=...<=q_k.
                              
                              Then for every i,
                                q_i >= max{
                                  ceil((8i+4r-14)/(6r-7)),
                                  ceil(((r-1)p+i+2r-3)/(2(r-1)))
                                }.
                              
                              Equivalently, the central-window lower profile controls the initial segment of the ordered packet, while the fixed-entrance capacity lower profile controls its dense upper tail. Their real-valued profiles cross at
                                i_*=
                                ((6r-7)(r-1)p+4r^2+4r-7)/(10r-9).
                              
                              If x_i is the unique entrance of e_i, then
                                sum_i phi(x_i)
                                >= sum_i [
                                  max{
                                    ceil((8i+4r-14)/(6r-7)),
                                    ceil(((r-1)p+i+2r-3)/(2(r-1)))
                                  }-1
                                ].
                              
                              If, moreover, v has minimum vertex rank among the r-1 terminal vertices of every e_i, then the r-2 other terminals on each e_i have rank at least p and all off-v vertices are pairwise distinct across the family. Hence their total off-v rank is at least
                                (r-2)pk
                              plus the displayed entrance-rank sum.
                              
                              This simultaneously strengthens the two separate packet bounds 34f8dc7df3f6 and 5198e921de4f on their common terminal-single domain.

                      • [1001191] Top-rank alignment continuation
                          STATEMENT
                          Route bridge: the coefficient-improvement analysis continues after toolkit theorem 1000274.

                        • [1000780] Aligned potential mass earns a second copy of the fixed-entrance coefficient gain
                            STATEMENT
                            Let S_0 be the total endpoint potential on vertices v whose maximum ascending-terminal edge rank equals phi(v). Then every linear r-uniform hypergraph satisfies m <= c_r S - ((2r-1)/(8r(r-1)))S_0 + O_r(n_+), where c_r=1-(2r-1)/(8r(r-1)) is the general fixed-entrance coefficient. Thus any asymptotic extremizer for c_r must have S_0=o(S): almost all potential mass lies at rank-misaligned vertices.

                          • [1001199] Rank-gap synthesis continuation
                              STATEMENT
                              Route bridge: the rank-gap synthesis continues after toolkit theorem 1000378.

                            • [1000574] Exact rank-sensitive master inequality for the three-uniform Astra-multiplicity synthesis
                                STATEMENT
                                Let H be a finite linear 3-graph. For each nonisolated vertex v put p(v)=phi(v), let t(v) count ascending nonspecial edges terminal at v, and if t(v)>0 let q(v) be their maximum rank. Choose P_v to end in a rank-p(v) ascending terminal edge whenever q(v)=p(v), and arbitrarily otherwise. Define
                                B(v)=0 if t(v)=0;
                                B(v)=ceil((3p(v)-4)/4) if q(v)=p(v);
                                B(v)=gamma(q(v)) if 0<q(v)<p(v),
                                where gamma(1)=0,gamma(2)=1,gamma(3)=2 and gamma(q)=floor((11q-5)/8) for q>=4.
                                Then
                                3m <= 2S-n_+ + (1/2)sum_v B(v),
                                where S=sum_v phi(v). Equivalently
                                m <= (2S-n_+)/3 + (1/6)sum_v B(v).
                                This retains the exact local rank q(v), exact low-rank corrections, and exact aligned multiplicity cancellation.

                              • [1000009] Singleton ascending-terminal contacts: terminal-only contacts lie in a stricter upper-half band
                                  STATEMENT
                                  Let H be a finite linear 3-graph, let v have p=phi(v), and let P=(g_1,...,g_p) be any maximum p-edge path ending at v. Let e={x,v,u} be an ascending nonspecial edge of rank q, with unique entrance x and v terminal. Suppose e has exactly one off-v contact w with P. Let a be the first path-edge index containing w and b the last; thus b is a or a+1. Then b>=p-q+2. If w=x, then a<=q-1, hence q>=ceil((p+2)/2). If w=u, then a<=q-2, hence q>=ceil((p+3)/2). In particular terminal-only singleton contacts are excluded from the bottom charged-rank boundary; at p=2q-2 any singleton contact must be the entrance.

                                • [1000713] Hybrid central-window and Astra bound for r=3 singleton terminal mass
                                    STATEMENT
                                    Let H be a finite linear 3-graph and fix a nonisolated vertex v with p=phi(v). Let t(v)>0 count ascending nonspecial edges terminal at v, let q=q(v) be their maximum rank, and let P_v be any maximum p-edge endpoint path at v. Let X_v be the excess contact multiplicity on P_v. If q<p, then
                                    t(v)-X_v <= min{ gamma(q), max(0,4q-2p-3) },
                                    where gamma(1)=0, gamma(2)=1, gamma(3)=2 and gamma(q)=floor((11q-5)/8) for q>=4.
                                    If q=p and P_v is chosen through a top-rank ascending terminal edge, then
                                    t(v)-X_v <= ceil((3p-4)/4).
                                    Thus for misaligned vertices the local cost is the minimum of the Astra fixed-entrance bound and the path-relative central-window packing bound. In the positive central-window regime, asymptotically that term is stronger for q/p<16/21, while Astra is stronger for q/p>16/21.

                                  • [1000812] Only doubly terminal-single ascending edges can contribute positively to A-X
                                      STATEMENT
                                      Fix arbitrary maximum endpoint paths P_v at all nonisolated vertices in a finite linear 3-graph, and let X be total excess contact multiplicity. Let U_11 be the number of ascending nonspecial edges e={x,u,v} for which both terminal incidences satisfy mu_u(e)=mu_v(e)=1. Then A-X<=U_11. Moreover, if e has rank q and belongs to U_11, then phi(u),phi(v)<=2q-2. If phi(v)=2q-2, the unique off-v contact of e on P_v must be the entrance x; the opposite terminal u is absent from P_v. The same holds symmetrically at u.

                              • [1000091] Gap-one top-rank edges either pay to alignment or move nondecreasingly in potential
                                  STATEMENT
                                  Let e={x,v,u} be ascending nonspecial of rank q with phi(v)=q+1 and v terminal. Then either phi(u)=q, in which case u is rank-aligned (its maximum ascending-terminal rank equals phi(u)); or phi(u)>=q+1=phi(v). Thus every top-rank edge at a gap-one vertex either lands on an aligned terminal one level lower or is nondecreasing in endpoint potential.

                                • [1000038] Every flat gap-one top edge manufactures a lens between maximum endpoint paths
                                    STATEMENT
                                    Let e={x,u,v} be an ascending nonspecial edge of rank p-1 in a finite linear 3-graph, with phi(u)=phi(v)=p and unique entrance x, so phi(x)=p-2. Let R be any maximum (p-2)-edge endpoint path ending at x for which R,e is a longest (p-1)-edge path ending in e, and let P_u,P_v be arbitrary maximum p-edge paths ending at u,v. Then at least one of the three path pairs (R,P_u), (R,P_v), (P_u,P_v) has at least two common vertices. More precisely: if x lies on P_v then R and P_v have a second common vertex; if x lies on P_u then R and P_u have a second common vertex; and if x lies on neither terminal path, then u lies on P_v and v lies on P_u, so P_u and P_v share both u and v.

                                  • [1000400] A flat gap-one top edge forces a balanced elementary lens
                                      STATEMENT
                                      In the setup of 0b1c38ec6184, one may choose the forced two-path overlap so that some elementary lens is balanced. If x lies on a terminal maximum path P_v (or P_u), then the elementary lens adjacent to x between the maximum entrance rail R and that terminal path has equal side lengths. If x lies on neither terminal path, then the two equal-length maximum terminal paths P_u,P_v share u and v and contain a balanced elementary lens. Hence every flat rank-(p-1) edge between potential-p terminals forces a balanced lens to which the no-piercing theorem applies.

                                • [1000619] Maximum ascending-terminal rank is nondecreasing across a maximum-rank terminal edge
                                    STATEMENT
                                    For a vertex v incident with at least one ascending edge at which v is terminal, let q(v) be the maximum edge rank among such edges. Let e={x,v,u} be an ascending edge of rank q(v), where x is its unique entrance and u is the other terminal vertex. Then q(u)>=q(v). Consequently, writing Delta(w)=phi(w)-q(w) at active vertices, if phi(u)<phi(v) then Delta(u)<Delta(v). In particular, in any directed graph obtained by choosing at each active vertex v one rank-q(v) ascending edge and directing v to one of its other terminal vertices, q is nondecreasing along every directed edge and is constant on every directed cycle.

                                  • [1000562] Maximum-rank terminal transfer reaches a charged step or alignment within the rank gap
                                      STATEMENT
                                      Let v_0 be active, with p_0=phi(v_0), q_0=q(v_0), and Delta_0=p_0-q_0. Starting at v_i, choose an ascending nonspecial edge e_i={x_i,v_i,v_{i+1}} of rank q(v_i), where v_i and v_{i+1} are its two terminals. If every chosen step strictly decreases endpoint potential, phi(v_{i+1})<phi(v_i), then Delta(v_{i+1})<=Delta(v_i)-1. Consequently after at most Delta_0 strict-decrease steps one reaches an aligned vertex Delta=0. Equivalently, before then either alignment occurs or some maximum-rank terminal edge is potential-charged at its current vertex, with phi(v_{i+1})>=phi(v_i). If p_0>=8, q_0>=4, q_0<p_0, and eta_{v_0} is the local defect from b032348c1a8a, then Delta_0<=1+(8/11)(eta_{v_0}+1).

                              • [1000617] A two-envelope local inequality isolates the near-top rank shell
                                  STATEMENT
                                  For a vertex v with p=phi(v) and maximum ascending-terminal rank q<p, one has t(v)-X_v <= min{gamma(q), max(0,4q-2p-3)}, where X_v is excess contact multiplicity on any chosen maximum p-path and gamma is the exact fixed-entrance bound. In particular q/p<=16/21 is controlled more strongly by the maximum-path window, and if p>=2q-1 then t(v)-X_v<=0. Thus the only asymptotically dangerous misaligned regime lies in the near-top band 16p/21<q<p.

                  • [1001055] Exact transfer solution gives a rank-sensitive 43/48 bound
                      STATEMENT
                      Let H be a finite linear 3-graph. If h is an ascending edge of rank q and v is terminal at h, then
                      |{f in E(H): v in f and phi(f)<=q}| <= floor((11q-5)/8)
                      for q>=4; for q=2,3 the sharper bounds are 1 and 2.
                      
                      Consequently, if t(v) counts ascending edges at which v is terminal and p=phi(v), then
                      t(v)<=gamma(p),
                      where gamma(1)=0, gamma(2)=1, gamma(3)=2, and gamma(p)=floor((11p-5)/8) for p>=4.
                      
                      Let S=sum_v phi(v), let n_+ be the number of nonisolated vertices, let rho(p) be the least nonnegative residue of 3p-5 modulo 8, put R=sum_v rho(phi(v)), and let N_2,N_3 count vertices of ranks 2,3. If A is the number of ascending edges and m=|E(H)|, then
                      A <= (11S-5n_+-R-8N_2-8N_3)/16
                      and
                      m <= (43S-21n_+-R-8N_2-8N_3)/48.
                      In particular every P_ell^(3)-free linear 3-graph satisfies
                      m <= ((43ell-64)/48)n.

                    • [1000342] Single ascending terminal contacts on a maximum path lie in one central rank window
                        STATEMENT
                        Let H be a finite linear 3-graph. Let v have p=phi(v), and let P=(g_1,...,g_p) be any maximum p-edge path with last vertex v, with last edge g_p. Let e={x,v,u} be an ascending nonspecial edge of rank q<p, with unique entrance x, and suppose e has contact multiplicity one on P:
                        |(e minus {v}) intersect (V(P) minus g_p)|=1.
                        Let c be that unique contact, and let a,b be the first and last indices of path edges containing c.
                        
                        Then
                        a<=q-1 and b>=p-q+2.
                        If c=u is the opposite terminal, the stronger a<=q-2 holds.
                        
                        Consequently p<=2q-2. More precisely all possible singleton-contact vertices for ascending terminal edges of rank at most q lie in a common central window of exactly
                        max(0,4q-2p-3)
                        vertices. Hence if s_q(v;P) is the number of ascending edges terminal at v, of rank at most q, that are single on P, then
                        s_q(v;P)<=max(0,4q-2p-3).
                        In particular, if p>=2q-1, every ascending terminal edge of rank at most q is double on every maximum path with last vertex v.

                      • [1000103] Maximum-path central windows sharpen the Astra multiplicity master inequality
                          STATEMENT
                          Let p(v)=phi(v), let t(v) count ascending nonspecial edges terminal at v, and let q(v) be their maximum rank when t(v)>0. Choose a maximum endpoint path P_v, choosing it to end in a rank-p(v) ascending terminal edge when q(v)=p(v). Let D_v count double contacts on P_v and D=sum_v D_v.
                          
                          Define B(v)=0 if t(v)=0; B(v)=ceil((3p(v)-4)/4) if q(v)=p(v); and if 0<q(v)<p(v), put
                          B(v)=min{gamma(q(v)), max(0,4q(v)-2p(v)-3)},
                          where gamma(2)=1, gamma(3)=2, and gamma(q)=floor((11q-5)/8) for q>=4.
                          
                          Then
                          2A-D <= sum_v B(v),
                          A-D <= (1/2)sum_v B(v),
                          and
                          3m <= 2S-n_+ +(1/2)sum_v B(v).

                    • [1000605] Near equality has a periodic four-cell contact normal form
                        STATEMENT
                        Use the fixed-entrance setup of eb40ddcc33ca, q>=4. Let s,d,u be the numbers of singleton contact sets, double contact sets, and unused vertices on W=V(P) minus h, and put
                        alpha=ceil((3q-8)/4),
                        M=floor((11q-5)/8).
                        If
                        |J_q(v)|=M-r,
                        then
                        (alpha-s)+u = 2r+(alpha mod 2).
                        In particular
                        s>=alpha-2r-1
                        and
                        u<=2r+1.
                        
                        Moreover, in the four-state representation of eb40ddcc33ca, all but at most 8r+18 interior state transitions are the critical cycle transitions
                        00->01, 01->11, 11->10, 10->00
                        with their full weights 2,1,0,0. Hence, after deleting O(r+1) exceptional cells and O(1) boundary cells, the singleton contact pattern is a union of intervals with the period-four normal form
                        0,0,2,1,0,0,2,1,...
                        up to cyclic phase.
                        
                        Thus exact or near equality simultaneously forces almost maximum singleton density, almost no unused vertices, linear double-contact mass, and an essentially periodic contact geometry.

                      • [1000543] Near-equality forces linearly many cross-period double contacts
                          STATEMENT
                          In the fixed-entrance setup of the periodic near-equality theorem 88db9b4e8337, suppose |J_q(v)|=M-r. After deleting O(r+1) exceptional cells and O(1) boundary cells, partition each remaining critical interval into disjoint full four-cell blocks following the period-four equality pattern. Let B be the number of such blocks. Then at least (B-u)/2 double contact sets have their two contact vertices in different blocks or have one endpoint outside the good-block union, where u is the number of unused contact vertices. Consequently there are at least q/8-O(r+1) such cross-period double contacts.
                          
                          In the gap-one switching setup, put delta=M-(t-X_v^T). By f6c9ded0ae63, at most |J|-t<=delta of these cross-period doubles belong to edges outside the ascending-terminal family T, and at most X_v^T<=delta members of T remain double on the maximum path. After discarding both classes, at least q/8-O(delta+1) cross-period switching edges remain.

                    • [1000987] The fixed-entrance conflict transfer extends to linear r-uniform paths
                        STATEMENT
                        Let r>=3 and let H be a finite linear r-uniform hypergraph. Define endpoint potentials and edge rank by longest linear paths. Suppose h has rank q>=4, has unique entrance x, satisfies phi(x)=q-1, and v is any other vertex of h. Put
                        J_q(v)={f in E(H): v in f and phi(f)<=q}.
                        
                        Set a=r-2 and L=q-3. Define alpha_r(L) by
                        alpha_r(1)=a,
                        alpha_r(4k+2)=a+1+k(2a+1) for k>=0,
                        alpha_r(4k+3)=(k+1)(2a+1) for k>=0,
                        alpha_r(4k)=3a+1+(k-1)(2a+1) for k>=1,
                        alpha_r(4k+1)=3a+1+(k-1)(2a+1) for k>=1.
                        Then
                        |J_q(v)| <= 1+floor(((r-1)(q-1)+alpha_r(q-3))/2).
                        In particular
                        |J_q(v)| <= ((6r-7)/8)q+O_r(1).
                        
                        For r=3 one has alpha_3(q-3)=ceil((3q-8)/4), and the bound becomes the exact inequality
                        |J_q(v)|<=floor((11q-5)/8).

                      • [1000588] Global r-uniform bound from ascending incidence and fixed-entrance transfer
                          STATEMENT
                          For every finite linear r-uniform hypergraph, r>=3, let S=sum_v phi(v), let n_+ count nonisolated vertices, let A count nonspecial ascending edges, and let m be the number of edges. Then
                          r m-A <= (r-1)S-(r-2)n_+.
                          The fixed-entrance transfer also gives
                          A <= ((6r-7)S-(6r-13)n_+)/(8(r-1)).
                          Hence
                          m <= ((8r^2-10r+1)S-(8r^2-18r+3)n_+)/(8r(r-1)).
                          Therefore every P_ell^(r)-free linear r-graph satisfies
                          m <= (((8r^2-10r+1)ell-(16r^2-28r+4))/(8r(r-1))) n.
                          At r=3 this is m<=((43ell-64)/48)n.

                      • [1000765] Near equality in the arbitrary-r fixed-entrance bound forces linear double-contact mass
                          STATEMENT
                          In the arbitrary-r fixed-entrance transfer, suppose |J_q(v)| is within t of the exact local maximum. Then the number of nonsingleton contact sets is at least floor(((r-1)(q-1)-alpha_r(q-3))/2)-t = ((2r-1)/8)q-O_r(1)-t. Moreover the total excess beyond doubles, u+sum_{j>=3}(j-2)n_j, is at most 2t+1. Hence all but O(t+1) of the forced nonsingleton contacts are genuine double contacts; quantitatively n_2>=((2r-1)/8)q-O_r(1)-3t.

                        • [1000580] Unpaid near-saturation forces linear anchor-to-maximum symmetric difference in every uniformity
                            STATEMENT
                            Let H be a finite linear r-graph with r>=3. Let h be an ascending nonspecial edge of rank q>=4, let v be terminal at h, and let
                              Q=(g_1,...,g_q=h)
                            be a longest h-path with last vertex v. Put
                              R=V(Q)\h,
                            so |R|=(r-1)(q-1).
                            
                            Let p=phi(v)>q, let P be a maximum p-edge path ending at v, and put
                              U=V(P)\last(P),
                            so |U|=(r-1)(p-1).
                            
                            Let T be a family of t distinct edges through v, containing h, such that every f in T has phi(f)<=q and every f in T\{h} has exactly one off-v contact with U. For f in T\{h}, put
                              C_Q(f)=(f\{v}) intersect R,
                            and let
                              D_Q(T)=#{f in T\{h}: |C_Q(f)|>=2}.
                            
                            Write s_r(q)=alpha_r(q-3), where alpha_r is the exact singleton-contact bound from dcf886f98a51. Then
                              D_Q(T) >= t-1-s_r(q),
                            and
                              |R\U| >= D_Q(T),
                              |U\R| >= D_Q(T)+(r-1)(p-q).
                            
                            Consequently, if
                              J_max(q)=1+floor(((r-1)(q-1)+s_r(q))/2)
                            and t>=J_max(q)-tau, then
                              D_Q(T)
                              >= floor(((r-1)(q-1)-s_r(q))/2)-tau
                              = ((2r-1)/8)q-O_r(1)-tau.
                            Thus any near-saturated terminal-single family forces linear two-sided symmetric difference between the rank-q anchor precursor and every chosen maximum p-path.
                            
                            In particular, the conclusion applies to a family of globally unpaid signature-(0,1,...,1) ascending edges from 6c9c2c5a0fcb, after restricting to one terminal v and a maximum-rank anchor h with q<phi(v).
                            
                            For r=3, every anchor-multiple edge is an anchor-double edge and its unique P-contact lies among the same two off-v vertices, so one obtains the stronger crossing matching of the existing gap-one theory. For r>3 that edgewise matching need not exist, but the symmetric-difference conclusion survives unchanged.

                          • [1000095] Near-saturated terminal-single families force linear balanced endpoint-lens packets in every uniformity
                              STATEMENT
                              Retain the setup of 80e2e6b25cab. Thus H is a finite linear r-graph, r>=3; P is a maximum p-edge endpoint path ending at v, with
                                U=V(P)\last(P);
                              Q is a rank-q ascending anchor path ending at v, q<p; and F is any family of D distinct edges through v such that each f in F has at least two contacts with the anchor precursor R=V(Q)\h but exactly one off-v contact
                                c_f in U
                              with P.
                              
                              Then the vertices c_f, f in F, are pairwise distinct. For each f, choose any maximum endpoint path P_f ending at c_f. The host path P and P_f contain a clean balanced elementary endpoint lens whose host-side endpoint is c_f.
                              
                              Hence P supports D balanced endpoint-lens states attached at D distinct host vertices.
                              
                              In particular, in the near-saturated terminal-single setting of 80e2e6b25cab, if
                                t>=J_max(q)-tau,
                              then one may take
                                D >= floor(((r-1)(q-1)-alpha_r(q-3))/2)-tau
                                  = ((2r-1)/8)q-O_r(1)-tau.
                              Thus near equality in the arbitrary-r fixed-entrance bound, together with terminal-singleness on a maximum p-path, forces a linear packet of distinct balanced endpoint lenses on that one host path in every uniformity.
                              
                              For globally unpaid signature-(0,1,...,1) ascending edges, terminal-singleness is automatic on the chosen endpoint path. This gives a uniformity-independent geometric replacement for the r=3 anchor-to-maximum crossing-matching step.

                          • [1000875] General-r switching hyperedges split into retained pairs or external three-vertex bridges
                              STATEMENT
                              Retain the setup of 80e2e6b25cab. Thus Q is a rank-q anchor path ending at v, R=V(Q)\h, P is a maximum p-edge path ending at v with U=V(P)\last(P), and every switching edge f in a family F through v satisfies
                                |C_Q(f)|>=2,
                                C_Q(f)=(f\{v}) intersect R,
                              while f has exactly one off-v contact c_f with U.
                              
                              Partition F into:
                                F_ret={f: c_f in C_Q(f)},
                                F_ext={f: c_f notin C_Q(f)}.
                              
                              Then:
                              
                              (1) For every f in F_ret one can choose
                                a_f in C_Q(f)\{c_f}
                              so that
                                a_f in R\U,
                                c_f in R intersect U.
                              The pairs {a_f,c_f}, f in F_ret, are pairwise vertex-disjoint. Hence F_ret canonically supplies a matching from anchor-only vertices to retained anchor vertices.
                              
                              (2) For every f in F_ext one can choose distinct
                                a_f,b_f in C_Q(f)
                              so that
                                a_f,b_f in R\U,
                                c_f in U\R.
                              The triples {a_f,b_f,c_f}, f in F_ext, are pairwise vertex-disjoint. Hence F_ext supplies a three-vertex bridge hypermatching with two anchor-only endpoints and one maximum-path-only endpoint.
                              
                              Consequently, if |F|=D, then either there is a retained crossing matching of size at least ceil(D/2), or there is an external bridge hypermatching of size at least ceil(D/2).
                              
                              For r=3 the external case is impossible: |C_Q(f)|>=2 already exhausts the two vertices of f\{v}. Thus the dichotomy collapses to the ordinary anchor-to-maximum crossing matching used in the 3-uniform gap-one theory.

                    • [1001083] The fixed-entrance conflict system has a five-fourths integrality gap over fractional packing
                        STATEMENT
                        In the fixed-entrance setup of eb40ddcc33ca with q>=4, let K_q be the conflict hypergraph on W whose hyperedges are the four forbidden singleton positions
                        {a_1},{b_1},{b_{q-2}},{z_{q-2}}
                        together with every two-vertex singleton-contact conflict supplied by the fixed-entrance splice between the forward part of g_i and the backward part of g_{i+2}, 1<=i<=q-3.
                        
                        Then the fractional matching number is exactly
                        nu^*(K_q)=q+1,
                        whereas the minimum vertex-cover number is
                        tau(K_q)=2q-2-ceil((3q-8)/4).
                        Thus tau(K_q)=(5/4+o(1)) nu^*(K_q). In particular, no fractional packing of the complete one-anchor singleton-contact constraints can improve the old q+1 marked-vertex lower bound; the improvement from local slope 3/2 to 11/8 is intrinsically an integral independence/cover phenomenon.

                      • [1000741] The eleven-eighths fixed-entrance incidence coefficient is asymptotically sharp
                          STATEMENT
                          For every k>=1 there is a finite linear 3-graph H_k with maximum linear-path length q=8k+4 and an ascending edge h of rank q, with terminal v, such that |{f containing v: phi(f)<=q}|=11k+1=(11/8)q-9/2. Hence the universal fixed-entrance bound on ALL low-rank incident edges cannot have leading coefficient below 11/8. This is not a lower bound of 43/48 for the Turan problem; the competing incident edges are not assumed ascending.

                    • [1001222] Near-saturated gap-one vertices force a five-eighths switching matching
                        STATEMENT
                        Let v have p=phi(v)=q+1 with q>=4, let T be the ascending nonspecial edges terminal at v with maximum rank q, and let delta=gamma(q)-(t(v)-X_v^T), gamma(q)=floor((11q-5)/8), where X_v^T is excess contact multiplicity of T on a chosen maximum p-path P. For every rank-q anchor path Q ending at v, at least gamma(q)-ceil((3q-4)/4)-delta=(5/8)q-O(1)-delta members of T are double on Q but single on P. Their disjoint non-v pairs form a matching in the anchor precursor crossing from vertices retained by P to vertices omitted by P; hence both sides of this cut have that size.

                      • [1000231] Deficiency-one path pairs have at most one unbalanced elementary lens
                          STATEMENT
                          Let Q and P be linear paths ending at the same vertex v, with |Q|=q and |P|=q+1=phi(v). Suppose a collection of pairwise edge-disjoint clean elementary lenses between Q and P is chosen, with Q-side lengths a_i and P-side lengths b_i. Then for every lens, 0<=b_i-a_i<=1, and at most one lens satisfies b_i-a_i=1. Consequently all but at most one elementary lens in any disjoint lens decomposition of the Q/P overlap are balanced.

                        • [1001120] Overlap-maximal gap-one path pairs have no balanced internal lens and at most one internal lens total
                            STATEMENT
                            Let Q be a q-edge path ending at v and let phi(v)=q+1. Among all maximum (q+1)-edge paths P ending at v, choose P to maximize the number of Q-edges it contains. Then Q and P admit no balanced clean internal elementary lens. Consequently, by the deficiency-one lens lemma 32ea928e6ffd, any pairwise edge-disjoint family of clean internal elementary Q/P lenses has size at most one; if such a lens exists, its P-side is exactly one edge longer than its Q-side.

                      • [1000429] A large gap-one switching family forces a linear packet of top-potential rotation endpoints
                          STATEMENT
                          Let P be a maximum p-path ending at v and F a family of distinct edges through v that are single blockers on P. Apart from O(1) boundary contacts, grouping precursor contacts into cells {private(g_i), g_i∩g_{i+1}} shows that each occupied cell yields a p-edge Posa rotation whose opposite endpoint can be the private vertex of g_{i+2}. Thus F forces at least |F|/2-O(1) distinct vertices of endpoint potential at least p. Applied to the gap-one switching family, local slack delta forces at least (5/16)q-O(1)-delta/2 high-potential rotation endpoints.

                        • [1000325] Single-blocker cells yield two top-potential rotation endpoints
                            STATEMENT
                            Let P=(g_1,...,g_p) be a maximum p-edge linear path ending at v, and let F be a family of distinct edges f through v such that each f has exactly one contact vertex with V(P)\V(g_p). Then, apart from O(1) boundary contacts, every occupied two-slot cell
                              C_i={b_i,z_i},   z_i=g_i∩g_{i+1},
                            forces two distinct vertices of endpoint potential at least p:
                              b_{i+2}  and  z_{i+1}=g_{i+1}∩g_{i+2}.
                            Consequently there are at least
                              |F|-O(1)
                            distinct vertices w with phi(w)>=p that occur as endpoints of p-edge rotations of P generated by members of F.
                            
                            Applied to the switching family of b032348c1a8a at an active misaligned vertex v of potential p, if eta_v=o(p), then the chosen maximum p-path supports at least
                              (5/8-o(1))p
                            distinct vertices of potential at least p arising from switching rotations. In the gap-one notation p=q+1 with local slack delta, the packet has size at least
                              (5/8)q-O(delta+1),
                            doubling the previous 5/16 coefficient from 5f8d96bf566a.

                          • [1000238] Doubled rotation packets halve the endpoint-congestion penalty
                              STATEMENT
                              Let (H_j) be a sequence of finite linear 3-graphs with
                                S_j=sum_v phi(v),
                                n_j^+=number of nonisolated vertices,
                              and S_j/n_j^+ tending to infinity.
                              
                              For every active misaligned vertex v, choose the switching family and the doubled rotation-endpoint packet R(v) supplied by b032348c1a8a and 465568d6d8dc. Let
                                M_j=max_w |{v:w in R(v)}|.
                              Then
                                |E(H_j)|
                                <= (19/24)S_j + (M_j/6)n_j^+ + o(S_j).
                              
                              More generally the pointwise maximum may be replaced by any aggregate bound
                                sum_v |R(v)| <= K_j n_j^+,
                              giving
                                |E(H_j)| <= (19/24)S_j + (K_j/6)n_j^+ + o(S_j).
                              
                              Thus any estimate
                                K_j < (5/8-o(1)) S_j/n_j^+
                              already yields a strict asymptotic improvement over 43/48; sublinear congestion K_j=o(S_j/n_j^+) recovers 19/24.

                          • [1000438] Every single-blocker rotation output pays by rank rise, specialness, flat orientation, or a high-potential joint
                              STATEMENT
                              Let P=(g_1,...,g_p) be a maximum p-edge path ending at v. Suppose a single blocker f through v has its unique precursor contact in an interior cell C_i={b_i,z_i}, and form the standard rotation
                                Q=(g_1,...,g_i,f,g_p,g_{p-1},...,g_{i+2}),
                              with i<=p-3.
                              Put h=g_{i+2} and let
                                z=g_{i+2} intersect g_{i+3}
                              be the forward joint of h on the original host path.
                              
                              Then phi(h)>=p. Moreover exactly one of the following holds:
                              (1) phi(h)>p;
                              (2) phi(h)=p and h is special;
                              (3) phi(h)=p, h is nonspecial ascending, z is its unique entrance, and phi(z)=p-1;
                              (4) phi(h)=p, h is nonspecial nonascending, z is its unique entrance, and phi(z)>=p.
                              
                              For distinct occupied cells the output edges h are distinct and their forward joints z are distinct.
                              
                              Thus every occupied switching cell makes monotone progress unless it lands in the flat ascending rank-p branch (3).

                            • [1000280] Consecutive flat rotation outputs are impossible at every potential level
                                STATEMENT
                                Let P=(g_1,...,g_p) be a maximum p-edge path ending at v. Suppose two consecutive host edges g_j,g_{j+1} both occur in the flat ascending branch (3) of the general rotation-output theorem 6205fe95ecf8, relative to occupied blocker cells on P. Then this is impossible.
                                
                                Equivalently, among all occupied cells whose output has rank exactly p and is nonspecial ascending through its forward joint, those cells form an independent set in the path-cell order.

                            • [1000443] Flat ascending rotation outputs with no endpoint rise land at aligned defect vertices
                                STATEMENT
                                Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, and let a single blocker through v have its unique precursor contact in an interior cell C_i, producing the standard rotation Q with last edge h=g_{i+2} and last vertex w=b_{i+2}. Then at least one of the following holds: (1) phi(h)>p; (2) phi(h)=p and h is special; (3) phi(h)=p and h is nonspecial nonascending; (4) phi(h)=p, h is ascending, and phi(w)>p; (5) phi(h)=p, h is ascending, phi(w)=p, and w is an active aligned vertex with q(w)=phi(w)=p. In case (5), for p>=8 the local defect eta_w of b032348c1a8a satisfies eta_w>=(5p-24)/8.

                              • [1000436] Distinct flat rotation terminal incidences are globally paid by local defect
                                  STATEMENT
                                  For each nonisolated vertex w let eta_w be the local defect from a57007500001. Let C be any set of distinct pairs (h,w) such that h is an ascending nonspecial edge terminal at w and phi(h)=phi(w)=p_w. Restrict first to p_w>=8. Then |C| <= 4 sum_w eta_w. Without the restriction p_w>=8, one has |C| <= 4 sum_w eta_w + O(n_+). Consequently, after the rotation outputs of 631ebe3d4728 are deduplicated by the ordered terminal incidence (h,w), all flat ascending no-endpoint-rise outputs cost only O(eta+n_+); the remaining issue is multiplicity with which one fixed pair (h,w) can be produced by different source vertices.

                            • [1000663] Every dangerous center pays one-eighth into progress or local obstruction
                                STATEMENT
                                Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, and let F be a family of single blockers through v. Restrict to the interior cells C_i={b_i,z_i}, 1<=i<=p-3, and let s_int be the number of blockers whose unique precursor contact lies in these cells.
                                
                                Let D be the number of cells containing two F-contacts. For every occupied cell C_i let h_i=g_{i+2} be its standard rotation output, and call C_i paid unless h_i is in branch (3) of 6205fe95ecf8, namely
                                  phi(h_i)=p,
                                  h_i is nonspecial ascending,
                                  its unique entrance is the forward joint g_{i+2}∩g_{i+3},
                                  and that joint has potential p-1.
                                Let Y be the number of paid occupied cells.
                                
                                Then
                                  D+Y >= s_int-ceil((p-3)/2).
                                
                                Each paid cell has at least one of:
                                (a) strict rank rise phi(h_i)>p;
                                (b) a special rank-p output edge;
                                (c) a nonspecial rank-p output whose forward joint has endpoint potential at least p.
                                
                                Each doubly occupied cell supports a linear switcher triangle.
                                
                                Consequently, for the switching family supplied by b032348c1a8a at any active misaligned vertex v of potential p>=8,
                                  D+Y >= p/8-eta_v-O(1).
                                Thus every low-defect dangerous center pays linearly into rank rise, specialness, high-potential forward joints, or switcher triangles; the unpaid flat rank-p branch cannot absorb the five-eighths switching density.

                              • [1000267] One-eighth payment is exactly internal superlevel edges or switcher triangles
                                  STATEMENT
                                  In the setting of 9586a4d2317f, put
                                    V_p={w:phi(w)>=p}.
                                  For each occupied interior cell C_i let h_i=g_{i+2} be its rotation-output edge, and let I_p be the number of occupied cells for which
                                    V(h_i) subset V_p.
                                  Let D be the number of doubly occupied cells.
                                  
                                  Then
                                    D+I_p >= s_int-ceil((p-3)/2).
                                  
                                  For the switching family at an active misaligned p-center,
                                    D+I_p >= p/8-eta_v-O(1).
                                  
                                  Thus the arbitrary-p one-eighth payment theorem has an exact potential-cut form: every dangerous center forces either a switcher triangle or a distinct output edge lying wholly inside its own potential superlevel H[V_p].

                              • [1000349] 43/48 near-extremizers carry one-eighth paid progress-or-obstruction mass
                                  STATEMENT
                                  Let (H_j) satisfy the near-extremal hypotheses of d287da5967d5: S_j=sum_v phi(v), S_j/n_j^+ -> infinity, and |E(H_j)| >= (43/48)S_j-o(S_j). For each active misaligned vertex v use the switching family and chosen maximum path from b032348c1a8a, and let D_v^cell be the number of doubly occupied interior blocker cells while Y_v is the number of paid occupied cells in the sense of 9586a4d2317f. Then sum_v(D_v^cell+Y_v) >= (1/8-o(1))S_j. Every Y_v event is one of: a strict output-rank rise above phi(v); a special output edge of rank phi(v); or a nonspecial rank-phi(v) output whose forward joint has endpoint potential at least phi(v). Every D_v^cell event contains a linear 3-cycle formed by the host edge and its two blocker edges.

                                • [1000894] One-eighth paid mass yields one-sixteenth distinct certified switcher edges
                                    STATEMENT
                                    Under the 43/48 near-extremal hypotheses of 4b7e6f0a912c, there is a set E_cert of distinct ascending nonspecial hyperedges with |E_cert| >= (1/16-o(1))S such that every f in E_cert is a switching edge in a paid-cell certificate at one of its terminal vertices. More precisely, one can inject all center-indexed units counted by sum_v(D_v^cell+Y_v) into center-switcher incidences (v,f); since an ascending nonspecial edge has exactly two terminal vertices, each underlying hyperedge receives at most two such incidences.

                                  • [1000551] Near 43/48 there are one-sixteenth many distinct paid-certified 0-1-1 edges
                                      STATEMENT
                                      Under the 43/48 near-extremal hypotheses, there are at least (1/16-o(1))S distinct ascending nonspecial edges that simultaneously (i) are source-clean on the chosen maximum path at their unique entrance, (ii) have contact multiplicity one on the chosen maximum endpoint path at each of their two terminals, and (iii) carry a paid-cell switching certificate at at least one terminal in the sense of c8d14f7306ab and 9586a4d2317f.

                                    • [1000201] Paid 0-1-1 edges are overwhelmingly canonical terminal-cycle chords
                                        STATEMENT
                                        Let (H_j) satisfy the 43/48 near-extremal hypotheses, with S_j=sum_v phi(v) and S_j/n_j^+ -> infinity. Let T_j be the terminal-pair graph of all nonspecial hyperedges, weighted by hyperedge rank, and choose a spanning forest F_j of T_j of maximum total rank.
                                        
                                        Then there is a set E_cyc of distinct ascending nonspecial hyperedges with
                                          |E_cyc| >= (1/16-o(1))S_j
                                        such that every e in E_cyc simultaneously:
                                        (1) is source-clean on the chosen maximum path at its unique entrance;
                                        (2) is terminal-single on the chosen maximum endpoint path at each terminal (hence lies in U_11);
                                        (3) carries a paid-cell switching certificate at at least one terminal;
                                        (4) its terminal-pair edge is not in F_j, so it is a minimum-rank edge on its canonical fundamental cycle C_e in T_j;
                                        (5) the two cycle-neighbor hyperedges at the two terminal endpoints of e have rank at least phi(e), and e satisfies the canonical two-sided blocker obligations supplied by the maximum-rank-forest theorem.
                                        
                                        Thus near 43/48, a linear-sized distinct family carries both the paid 0-1-1 local certificate and a canonical global terminal-cycle certificate.

                                      • [1000850] Paid edges have fundamental cycles inside the clean U_11 graph
                                          STATEMENT
                                          Under the 43/48 near-extremal hypotheses, let J be the terminal graph consisting only of ascending nonspecial hyperedges that are source-clean on the chosen source path and terminal-single on both chosen terminal endpoint paths. Weight each edge of J by its hyperedge rank and choose, in every component of J, a spanning tree of maximum total rank; let F be their union.
                                          
                                          Then there is a set E_clean-cyc of distinct paid-certified edges with
                                            |E_clean-cyc| >= (1/16-o(1))S
                                          such that every e in E_clean-cyc is a nonforest edge of F. Consequently its fundamental cycle C_e is entirely contained in the source-clean U_11 graph J, e has minimum rank on C_e, and at each terminal of e the adjacent cycle edge has rank at least phi(e) and forces e to make an additional blocker contact with every corresponding maximum-rank terminal witness.
                                          
                                          Thus a linear-sized family of paid-certified edges has canonical fundamental cycles all of whose edges remain inside the rigid source-clean, doubly-terminal-single ascending class.

                                    • [1001038] Almost all near-extremal potential mass has local one-eighth paid-certified 0-1-1 degree
                                        STATEMENT
                                        Let (H_j) satisfy the 43/48 near-extremal hypotheses of d287da5967d5. For each vertex v one may choose a family G_v of ascending nonspecial edges terminal at v such that every f in G_v is source-clean at its unique entrance, terminal-single on the chosen maximum endpoint paths at both terminals, and carries at v a paid-cell switching certificate from 9586a4d2317f. Writing p_v=phi(v), one has sum_v (p_v/8-|G_v|)_+=o(S_j). Consequently, for every fixed epsilon>0, the total endpoint-potential mass of vertices v with |G_v|<(1/8-epsilon)p_v is o(S_j).

                                      • [1000694] Near 43/48, linearly many paid-certified edges have strict rank gap at both terminals
                                          STATEMENT
                                          Let (H_j) satisfy the 43/48 near-extremal hypotheses, with S_j=sum_v phi(v) and S_j/n_j^+ -> infinity. Choose the families G_v from e6137a4bc902. Then all but o(S_j) of the center-edge incidences (v,f) with f in G_v have the following property: if u is the other terminal of f, then phi(f)<phi(v) and phi(f)<phi(u). Consequently there is a set Epp of distinct ascending nonspecial edges with |Epp| >= (1/16-o(1))S_j such that for every e={x,u,v} in Epp, both terminal vertex ranks strictly exceed the edge rank: min{phi(u),phi(v)} >= phi(e)+1. Every edge in Epp remains source-clean, terminal-single at both terminals, and paid-certified at at least one terminal.

                                        • [1000409] Local one-eighth strict-gap paid mass survives as clean fundamental-cycle chords
                                            STATEMENT
                                            Let (H_j) satisfy the 43/48 near-extremal hypotheses, write
                                              S_j = sum_v phi(v),
                                            and assume S_j/n_j^+ -> infinity. For each vertex v let G_v be the paid-certified source-clean, doubly-terminal-single family supplied by e6137a4bc902, and put p_v=phi(v).
                                            
                                            Let J_j be the terminal-pair graph consisting of all ascending nonspecial hyperedges that are source-clean on the chosen maximum path at their unique entrance and terminal-single on the chosen maximum endpoint path at both terminals. Weight each edge of J_j by its edge rank, and choose in every component a spanning tree of maximum total edge rank; let F_j be the union of these trees.
                                            
                                            Then there are subfamilies H_v subseteq G_v such that
                                              sum_v (p_v/8-|H_v|)_+ = o(S_j),
                                            and every center-edge incidence (v,e) with e={x,v,u} in H_v simultaneously satisfies:
                                            (1) e carries its paid-cell switching certificate at v and is source-clean and terminal-single at both terminals;
                                            (2) e has strict edge-rank gap at both terminals,
                                                phi(e)<min{phi(v),phi(u)};
                                            (3) the terminal-pair edge vu is not in F_j, so its fundamental cycle C_e lies entirely in J_j and e has minimum edge rank on C_e;
                                            (4) at each terminal of e, the cycle-neighbor hyperedge has edge rank at least phi(e), and e has an additional blocker contact with every corresponding maximum terminal witness for that neighbor.
                                            
                                            Consequently
                                              sum_v |H_v| >= S_j/8-o(S_j),
                                            and the union of the H_v contains at least
                                              (1/16-o(1))S_j
                                            distinct hyperedges. Thus almost all of the local one-eighth paid mass can simultaneously be required to have strict rank gap and a canonical clean fundamental-cycle certificate.

                                        • [1000570] Any sublinear local bound on the paid two-terminal-gap subclass breaks 43/48 saturation
                                            STATEMENT
                                            Assume there is a function g(p)=o(p) with the following property. For every relevant choice of maximum paths, at each vertex v of rank p, at most g(p) source-clean, doubly-terminal-single, paid-certified ascending nonspecial edges can be assigned to v as a minimum-rank terminal while having edge rank strictly below both terminal vertex ranks. Then no 43/48 near-extremal sequence with S/n_+ -> infinity exists. In particular, an O(log p) bound on this narrow local class is sufficient to force a strict asymptotic improvement below the 43/48 leading coefficient.

                                          • [1000406] Minimum-terminal rank-gap families force a disjoint two-tier rank packet
                                              STATEMENT
                                              Let v be a vertex with phi(v)=p, and let
                                                e_i={x_i,v,u_i},  i=1,...,k,
                                              be distinct ascending nonspecial edges through v, where x_i is the unique entrance, v is terminal at e_i, phi(u_i)>=p, and phi(e_i)<p. Order the edge ranks
                                                q_1<=...<=q_k,  q_i=phi(e_i).
                                              Then all 2k vertices x_1,...,x_k,u_1,...,u_k are distinct, and
                                                q_i >= ceil((2p+i+3)/4).
                                              Consequently
                                                sum_{i=1}^k phi(x_i) >= (p/2)k + k(k-1)/8,
                                              and
                                                sum_{i=1}^k [phi(x_i)+phi(u_i)]
                                                  >= (3p/2)k + k(k-1)/8.
                                              In particular the family forces k distinct vertices of vertex rank at least p outside v, together with a disjoint unique-entrance packet of the displayed total vertex rank.

                                          • [1001050] Separated mixed singleton contacts force rank sum at least host rank plus four
                                              STATEMENT
                                              Let P=(g_1,...,g_p) be a maximum p-edge path with last vertex v and last edge h=g_p. Let
                                                e={x,v,u},  f={y,v,z}
                                              be distinct ascending nonspecial edges, neither equal to h, that are terminal at v and each have exactly one off-v contact with V(P)\h.
                                              
                                              For a contact vertex c on P\h, let I(c)=[a(c),b(c)] be the interval of path-edge indices containing c. Suppose the two contact intervals are disjoint, with
                                                b(c_e) < a(c_f).
                                              If at least one of the two contacts is the opposite terminal of its edge rather than its unique entrance, then
                                                phi(e)+phi(f) >= p+4.
                                              
                                              Thus any pair of singleton ascending terminal edges with disjoint ordered contact intervals and rank sum at most p+3 must have both contacts equal to their unique entrances.

                                            • [1000200] Separated singleton contacts force rank sum at least host rank plus four without a contact-type hypothesis
                                                STATEMENT
                                                Let P=(g_1,...,g_p) be a maximum p-edge path with last vertex v and last edge h=g_p. Let
                                                  e={x,v,u},  f={y,v,z}
                                                be distinct ascending nonspecial edges, neither equal to h, that are terminal at v.
                                                
                                                Assume each edge has contact multiplicity one at v on P. Let c_e,c_f be their unique contacts in
                                                  V(P) minus h,
                                                and let
                                                  I(c)=[a(c),b(c)]
                                                be the interval of path-edge indices containing c.
                                                
                                                If
                                                  b(c_e)<a(c_f),
                                                then
                                                  phi(e)+phi(f)>=p+4.
                                                
                                                No assumption is required on whether either singleton contact is a unique entrance or the opposite terminal.

                                            • [1000489] Mixed overlapping singleton contacts have two exact boundary forms
                                                STATEMENT
                                                Let P=(g_1,...,g_p) be a maximum p-edge path with last vertex v and last edge g_p. Let
                                                  e_U={x,v,u},   phi(e_U)=r,
                                                  e_X={y,v,z},   phi(e_X)=s
                                                be distinct ascending nonspecial edges terminal at v, neither equal to g_p. Assume each has exactly one off-v contact with V(P)\g_p; the contact of e_U is its opposite terminal u, while the contact of e_X is its unique entrance y. Let I(u),I(y) be their path-edge occurrence intervals.
                                                
                                                If I(u) and I(y) overlap, then
                                                  r+s >= p+3.
                                                Moreover, if r+s=p+3, exactly one of the following two configurations occurs.
                                                
                                                (O) There is q with p=2q-3 and r=s=q, and on the central host edge g_{q-1},
                                                  u=g_{q-2}∩g_{q-1},
                                                  y=the private vertex of g_{q-1}.
                                                
                                                (E) There is q with p=2q-2, s=q, r=q+1, and on the central host edge g_{q-1},
                                                  u=the private vertex of g_{q-1},
                                                  y=g_{q-1}∩g_q.
                                                
                                                For the local switching-cell system of 9586a4d2317f, suppose additionally that e_U and e_X are both selected as distinct center-switcher witnesses by the D+Y cellwise injection of c8d14f7306ab. In case (O), at least one of the two adjacent occupied cells C_{q-2},C_{q-1} is paid. In case (E), the common cell C_{q-1} is doubly occupied and paid. Hence, by 39d0d99258db, every equality case forces a nearby switching output edge all of whose vertices have rank at least p.

                                              • [1000941] Opposite singleton-contact types have rank sum p plus three only with a superlevel output
                                                  STATEMENT
                                                  Let P=(g_1,...,g_p) be a maximum p-edge path with last vertex v. Let e and f be distinct selected ascending nonspecial edges terminal at v, neither equal to g_p, each having exactly one off-v contact with V(P)\g_p.
                                                  
                                                  Assume the contact of one edge is its unique entrance and the contact of the other edge is its opposite terminal. Then
                                                    phi(e)+phi(f) >= p+3.
                                                  
                                                  Moreover, if
                                                    phi(e)+phi(f)=p+3,
                                                  then one of the standard rotation-output edges associated with the two selected contacts has all three vertices of vertex rank at least p.
                                                  
                                                  Consequently, in any selected family in which no such superlevel rotation output is allowed, every opposite-type pair satisfies
                                                    phi(e)+phi(f) >= p+4.

                                            • [1001220] Terminal-single reciprocity forces repeated intersections below the rank-sum threshold
                                                STATEMENT
                                                Let e_i={x_i,v,u_i}, i=1,...,k, be distinct ascending nonspecial edges through a common terminal v. For each i choose a maximum path P_i ending at u_i on which e_i is terminal-single. If for every ordered pair i!=j one has phi(e_i)+phi(e_j)<=phi(u_i)+3, then P_i contains a non-v vertex of e_j. Partition owners according to whether the unique off-u_i contact of e_i on P_i is x_i or v. Every pair in the first class has at least two common vertices; in the second class the graph of pairs intersecting only at v is triangle-free. Hence at least binom(m,2)+binom(n,2)-floor(n^2/4) owner pairs have at least two common vertices, and for k>=4 some pair necessarily has a repeated intersection.

                                          • [1000361] Payment at one terminal does not yet supply payment at the minimum-rank terminal
                                              STATEMENT
                                              The certified extraction 9fba15f1495c provides payment at at least one terminal, not necessarily a minimum-rank terminal. Thus a sublinear bound requiring a paid certificate at the assigned minimum-rank terminal needs an additional transfer or mass estimate before applying 7e6abf77cbc5.

                                  • [1000851] Two selected contacts from one interior pair force a superlevel rotation output
                                      STATEMENT
                                      Let P=(g_1,...,g_p) be the chosen maximum p-edge path ending at v. For an interior index i, let
                                        C_i={b_i,z_i}
                                      be the two possible contact vertices used in the D+Y selection of c8d14f7306ab, and let
                                        h_i=g_{i+2}
                                      be the corresponding standard rotation output.
                                      
                                      Suppose two distinct selected center-edge incidences at v have their unique off-v contacts equal to b_i and z_i, respectively. Then every vertex of h_i has vertex rank at least p:
                                        V(h_i) subseteq {w: phi(w)>=p}.
                                      
                                      Equivalently, if h_i has a vertex of rank at most p-1, at most one selected incidence can have its unique off-v contact in C_i.

                                  • [1000945] One-sixteenth of near-extremal potential mass lies on distinct edges with strict rank-ascent certificates
                                      STATEMENT
                                      Under the 43/48 near-extremal hypotheses of c8d14f7306ab, there is a set E_asc of distinct ascending nonspecial edges with |E_asc| >= (1/16-o(1))S such that for every f in E_asc there exist a terminal center v, p=phi(v), an interior switching cell of the chosen maximum p-edge path P_v containing the unique off-v contact of f, and a host output edge h on P_v for which phi(f)<p<=phi(h). Moreover the standard single-blocker rotation is a p-edge linear path ending in h and containing f. Thus every f in E_asc comes with an explicit strict edge-rank ascent witness f -> h.

                              • [1000669] Cell dispersion forces a source-mass / switcher-triangle tradeoff
                                  STATEMENT
                                  Let P=(g_1,...,g_p) be a maximum p-edge path ending at v with last vertex v. Let F be a family of distinct ascending nonspecial edges terminal at v, each having exactly one off-v contact with P, and suppose all these contacts lie in the interior cells
                                    C_i={b_i,z_i},  1<=i<=p-3,
                                  where b_i is private to g_i and z_i=g_i∩g_{i+1}.
                                  Let s=|F|, let D be the number of cells containing two F-contacts, and hence let C=s-D be the number of occupied cells. For f∈F write x_f for its unique entrance.
                                  
                                  Then
                                    sum_{f∈F} phi(x_f)
                                    >= (p/2)s + floor(C^2/4)
                                    =  (p/2)s + floor((s-D)^2/4).
                                  
                                  Consequently, for any theta∈[0,1], either D>=theta s, or
                                    sum_{f∈F} phi(x_f)
                                    >= (p/2)s + ((1-theta)^2/4)s^2 - O(1).
                                  
                                  In particular, if F is the interior part of a low-defect switching family at a p-center, so s=(5/8-o(1))p, then either D>=theta(5/8-o(1))p or
                                    sum_{f∈F}phi(x_f)
                                    >= [5/16 + 25(1-theta)^2/256 - o(1)]p^2.

                                • [1000223] Top centers pay in triangles or simultaneous source mass and lenses
                                    STATEMENT
                                    Let v be an active misaligned global-top center with phi(v)=L and eta_v=o(L). Use the interior switching cells on a chosen maximum L-edge host path as in 9586a4d2317f. Let s be the number of interior switchers, D the number of doubly occupied cells, and Y the number of paid/nonflat occupied cells.
                                    
                                    Then at least one of the following holds:
                                    
                                    (T)  D >= (1/16-o(1))L. In particular the host supports at least (1/16-o(1))L distinct switcher triangles.
                                    
                                    (SL) D < (1/16-o(1))L, and simultaneously
                                      sum_{f in F_int} phi(x_f) >= (401/1024-o(1))L^2
                                    and
                                      Y >= (1/16-o(1))L.
                                    Hence, by 91f6c32ab805, the same host carries at least (1/16-o(1))L distinct top-potential balanced endpoint-lens attachments.
                                    
                                    Thus every low-defect global-top center has either a linear switcher-triangle packet, or both a strengthened quadratic source-potential packet and a linear equal-top lens packet.

                                • [1000307] Continuous triangle-lens-source frontier at top centers
                                    STATEMENT
                                    Let v be an active misaligned global-top center with phi(v)=L. Use the interior switching-cell notation on a chosen maximum L-edge host path. Let s be the number of interior switchers, D the number of doubly occupied cells, Y the number of paid/nonflat occupied cells, and
                                      M_v=sum_{f in F_int} phi(x_f)
                                    the total entrance-potential mass of the interior switchers.
                                    
                                    Then, up to the absolute O(1) boundary loss already present in the switching theorem,
                                      s >= (5/8)L-eta_v-O(1),
                                      D+Y >= (1/8)L-eta_v-O(1),
                                    and
                                      M_v >= (L/2)s + floor((s-D)^2/4).
                                    
                                    Consequently, if eta_v=o(L) and d_v=D/L, then
                                      Y/L >= max(0,1/8-d_v)-o(1)
                                    and
                                      M_v/L^2 >= 5/16 + (5/8-d_v)^2/4 - o(1)
                                    whenever d_v<=5/8+o(1).
                                    
                                    Thus a low-defect top center lies on a three-currency frontier: increasing switcher-triangle density D is the only way to reduce the cell-dispersion source mass, while until D reaches L/8 it simultaneously reduces but does not eliminate the forced paid-lens/output packet Y.

                              • [1000817] A dangerous global-top center pays one-eighth into switcher triangles or balanced-lens outputs
                                  STATEMENT
                                  Let L be the global maximum path length and let v be an active misaligned vertex with phi(v)=L and local defect eta_v as in b032348c1a8a. Use its switching family on a chosen maximum L-edge host path and the interior-cell notation of 9586a4d2317f. Let D be the number of doubly occupied interior cells and Y the number of paid occupied cells. Then D+Y >= L/8-eta_v-O(1). Every doubly occupied cell supports a linear switcher triangle. Every paid cell has a distinct rank-L all-top output edge, and hence manufactures a clean balanced elementary endpoint lens. Thus a low-defect global-top center carries Omega(L) center-indexed triangle/lens obstruction states.

                                • [1000642] Paid top-output cells give distinct top-potential lens attachments on one host path
                                    STATEMENT
                                    In the global-top setup of b7a21d8e4f90, let P_v=(g_1,...,g_L) be the chosen maximum host path and let Y be the paid occupied interior cells. For every paid cell with output edge g_j={z_{j-1},b_j,z_j}, the private host vertex b_j satisfies phi(b_j)=L. Choosing any maximum L-edge endpoint path P_{b_j}, the pair P_v,P_{b_j} contains a clean balanced elementary endpoint lens attached at b_j. Distinct paid cells give distinct attachment vertices b_j. Thus the Y paid cells yield Y distinct top-potential balanced-lens states on the single host path P_v.

                                  • [1001198] Balanced-lens continuation
                                      STATEMENT
                                      Route bridge: the balanced-lens analysis continues after toolkit lemma 1000369.

                                    • [1000915] Long nested balanced lenses must intersect off the host
                                        STATEMENT
                                        Let P be a globally longest L-edge linear path. Let two clean balanced endpoint lenses on P have nested host intervals
                                          [a,d] and [b,c]
                                        in the order a<b<c<d along P. Let A be the off-host side joining a to d and B the off-host side joining b to c. Assume A and B are internally vertex-disjoint. If T=|P[a,d]| is the outer host-side length, then
                                          2T <= L+1.
                                        Equivalently,
                                          T <= floor((L+1)/2).
                                        
                                        Consequently, if two balanced endpoint lenses on a globally longest host path have nested host intervals and the outer interval has length greater than (L+1)/2, then their off-host sides must intersect.

                                      • [1001109] Long balanced lenses have pairwise intersecting auxiliary sides
                                          STATEMENT
                                          Let P be a globally longest L-edge linear path. Let two genuine clean balanced endpoint lenses on P have host intervals I_1,I_2, each of host-side length greater than (L+1)/2. Then their off-host lens sides have an internal common vertex.
                                          
                                          Equivalently: a family of genuine balanced endpoint lenses on one globally longest host path whose host intervals all have length greater than (L+1)/2 has pairwise internally intersecting auxiliary sides.

                            • [1000675] Lens-free exact D+Y cell payment theorem
                                STATEMENT
                                Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, and let F be a family of distinct edges through v such that each has exactly one off-v contact with P. Restrict to the interior two-slot cells
                                  C_i={b_i,z_i}, 1<=i<=p-3,
                                and let s_int be the number of members of F whose unique contact lies in these cells.
                                
                                Let D be the number of doubly occupied interior cells. For each occupied C_i let h_i=g_{i+2} be its standard rotation output, and call C_i unpaid when h_i is the flat ascending branch (3) of 6205fe95ecf8; call it paid otherwise. Let Y be the number of paid occupied cells.
                                
                                Then
                                  D+Y >= s_int-ceil((p-3)/2).
                                
                                Every paid cell has at least one of:
                                (a) phi(h_i)>p;
                                (b) phi(h_i)=p and h_i is special;
                                (c) phi(h_i)=p, h_i is nonspecial nonascending, with its forward joint of vertex rank at least p.
                                Every doubly occupied cell supports a linear 3-cycle formed by its host edge and its two blocker edges.
                                
                                Thus this exact D+Y payment inequality is independent of any endpoint-lens assertion and of any dense-switching theorem.

                              • [1000235] Distinct doubly occupied switching cells give edge-disjoint local triangles
                                  STATEMENT
                                  Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, and let F be a family of distinct edges through v, each with exactly one off-v contact with P. Use the interior two-slot cells C_i={b_i,z_i}, 1<=i<=p-3, as in 9a6be27912e0.
                                  
                                  For every doubly occupied cell C_i, let f_i^1,f_i^2 be its two blocker edges. Then
                                    {g_i,f_i^1,f_i^2}
                                  is a linear 3-cycle, and the 3-cycles arising from distinct doubly occupied cells are pairwise edge-disjoint.
                                  
                                  Consequently, if D cells are doubly occupied, the hypergraph contains D pairwise edge-disjoint linear 3-cycles supported by those cells.

                              • [1000435] Lens-free one-eighth local payment at low-defect misaligned centers
                                  STATEMENT
                                  Let v be an active misaligned vertex with p=phi(v)>=8, local defect eta_v, chosen maximum p-edge path P_v, and a maximum-rank ascending terminal anchor with edge rank q<p. Let F_v be the anchor-double / host-single switching family supplied by the lens-free dense switching theorem f3588b3a3bc7.
                                  
                                  Restrict to switching contacts in the interior cells of P_v. Let D_v^cell be the number of doubly occupied interior cells and Y_v the number of paid occupied cells in the sense of the lens-free exact D+Y theorem 9a6be27912e0.
                                  
                                  Then
                                    D_v^cell+Y_v >= p/8-eta_v-O(1).
                                  
                                  More precisely,
                                    D_v^cell+Y_v
                                    >= beta(p)-eta_v-a(q)-ceil((p-3)/2)-O(1),
                                  where beta(p)=floor((11p-16)/8) and a(q)=ceil((3q-4)/4).
                                  
                                  Thus every low-defect active misaligned p-center carries at least p/8-o(p) selected local payment units, each represented by either a switcher triangle or a paid rotation-output cell.

                                • [1000873] One-eighth certificate payment splits into cycle packing or distinct progress outputs
                                    STATEMENT
                                    Let v be an active misaligned vertex with p=phi(v)>=8 and local defect eta_v. In the lens-free selected switching setup of 614c7d2d181a, let D be the number of doubly occupied interior cells and Y the number of paid occupied interior cells.
                                    
                                    Then at least one of the following holds:
                                    (1) D >= p/16-eta_v/2-O(1), and the hypergraph contains D pairwise edge-disjoint linear 3-cycles supported by the doubly occupied cells;
                                    (2) Y >= p/16-eta_v/2-O(1), and there are Y distinct host output edges h_i, one for each paid cell, each satisfying at least one of
                                        (a) phi(h_i)>p;
                                        (b) phi(h_i)=p and h_i is special;
                                        (c) phi(h_i)=p, h_i is nonspecial nonascending, and its forward joint has vertex rank at least p.
                                    
                                    In particular, eta_v=o(p) forces either (1/16-o(1))p pairwise edge-disjoint local triangles or (1/16-o(1))p distinct progress-output edges.

                          • [1000470] Switching rotations force a linear packet of high-rank host edges
                              STATEMENT
                              In the setting of 465568d6d8dc, every occupied interior blocker cell C_i forces the host edge g_{i+2} to satisfy phi(g_{i+2})>=p. Distinct occupied cells give distinct such edges. Hence if F is a single-blocker family on a maximum p-path, then at least
                                |F|/2-O(1)
                              distinct path edges have edge rank at least p.
                              
                              For a low-defect active misaligned center v with phi(v)=p and switching family F_v from b032348c1a8a,
                                #{g in E(P_v): phi(g)>=p}
                                >= (5/16)p-(1/2)eta_v-O(1).
                              Thus eta_v=o(p) forces (5/16-o(1))p rank-at-least-p edges on the chosen maximum path. If p is the global maximum path length, these are all globally top-rank edges.

                            • [1000036] Top-rank rotation outputs split into special, flat-oriented, or top-joint states
                                STATEMENT
                                Let L be the global maximum path length, let P=(g_1,...,g_L) be a maximum L-edge path, and suppose an occupied single-blocker cell C_i produces the rotation
                                  g_1,...,g_i,f,g_L,g_{L-1},...,g_{i+2}
                                with i<=L-3. Then phi(g_{i+2})=L. Put
                                  z_{i+2}=g_{i+2}∩g_{i+3},
                                the forward joint of g_{i+2} on the original host path.
                                
                                Exactly one of the following holds:
                                1. g_{i+2} is special;
                                2. g_{i+2} is nonspecial ascending, its unique entrance is z_{i+2}, and phi(z_{i+2})=L-1;
                                3. g_{i+2} is nonspecial nonascending, its unique entrance is z_{i+2}, and phi(z_{i+2})=L.
                                
                                Consequently, at a low-defect global-top center v with phi(v)=L, the linear packet of rank-L host edges from 68906f1d55c3 decomposes into special edges, forward-oriented flat ascending top-rank edges, and edges whose forward joints are distinct top-potential vertices.

                              • [1000391] Nonascending top-rank rotation outputs are all-top edges
                                  STATEMENT
                                  In the setup of 09e3d5b2bd6b, suppose the output edge g_j is nonspecial and nonascending. Then all three vertices of g_j have endpoint potential L.
                                  
                                  More explicitly, writing
                                    g_j={z_{j-1}, b_j, z_j},
                                  where z_{j-1}=g_{j-1}∩g_j, b_j is private on the host path, and z_j=g_j∩g_{j+1}, one has
                                    phi(z_{j-1})=phi(b_j)=phi(z_j)=L.
                                  
                                  Hence the nonascending branch of the top-rank rotation-output packet consists entirely of rank-L edges induced on the top-potential vertex set V_L={w:phi(w)=L}.

                                • [1000572] Every all-top edge manufactures a balanced endpoint lens
                                    STATEMENT
                                    Let L be the global maximum linear-path length and let h={a,b,c} be any edge with phi(a)=phi(b)=phi(c)=L. Fix any maximum L-edge endpoint path P_a ending at a. Then P_a contains at least one of b,c. Consequently, if y is such a contained vertex and P_y is any maximum L-edge path ending at y, the paths P_a and P_y contain a clean balanced elementary endpoint lens. In particular every nonascending top-rank rotation output from 57d5e4c71035 canonically forces a balanced-lens state among top-potential endpoint paths.

                                • [1001048] An all-top edge forces a multiple-overlap pair among its three maximum endpoint paths
                                    STATEMENT
                                    Let L be the global maximum linear-path length and let h={a,b,c} be an edge with phi(a)=phi(b)=phi(c)=L. Choose arbitrary maximum L-edge endpoint paths P_a,P_b,P_c ending physically at a,b,c respectively. Then every pair among P_a,P_b,P_c intersects. Moreover, at least one pair has at least two common vertices. More precisely, if P_a and P_b have a unique common vertex, that vertex must be c and is a same-index internal joint on both paths; cyclically for the other pairs.

                              • [1001212] Top-layer switching packets force one-eighth paid structure
                                  STATEMENT
                                  Along a global longest path, forward-flat ascending top-rank output edges form an independent set. For a dense family of interior single blockers at a top-layer switching center, this implies at least a one-eighth-scale payment into doubly occupied switcher cells or nonflat outputs. Refining by contact type, the same family satisfies s_int<=ceil((L-3)/2)+U+2Y, so U+2Y>=L/8-eta_v-O(1): linearly many switchers are terminal-retained or lie in cells whose output is special or all-top nonspecial nonascending.

                                • [1000933] A low-defect global-top center has either quadratic omitted-source mass or a linear top-lens packet
                                    STATEMENT
                                    Let v be an active misaligned global-top center with phi(v)=L, local defect eta_v, and use the switching family/interior-cell notation of 666bd06ca682. Put R_v=L/8-eta_v-O(1), with the same absolute boundary loss as in that theorem. Then at least one of the following holds: (U) there are k>=R_v/2 terminal-retained interior switchers, with distinct omitted entrances x_1,...,x_k satisfying sum_i phi(x_i)>=Lk/2+k(k+1)/8; or (Y) there are Y>=R_v/4 distinct paid/nonflat output cells whose private host vertices are distinct, have potential L, and each supports a clean balanced elementary endpoint lens on the common host maximum path. In particular, if eta_v=o(L), then either k>=(1/16-o(1))L and the omitted entrance-potential mass is at least (65/2048-o(1))L^2, or Y>=(1/32-o(1))L distinct top-potential balanced-lens attachments occur on one host.

                                • [1001061] Every low-defect misaligned center pays one-eighth into terminal retention or monotone output progress
                                    STATEMENT
                                    Let v be an active misaligned vertex with p=phi(v), and let F be a switching family from b032348c1a8a on the chosen maximum p-edge path P_v=(g_1,...,g_p). Restrict to interior blocker cells C_i={b_i,z_i}, 1<=i<=p-3, and let s_int be the number of F-edges whose unique P_v-contact lies in these cells.
                                    
                                    Call a switcher X-type if its retained contact is its entrance, and U-type if its retained contact is its opposite terminal. Let U be the number of interior U-type switchers.
                                    
                                    For each occupied cell C_i let h_i=g_{i+2} be the rotation-output edge. Call C_i flat if h_i is branch (3) of 6205fe95ecf8: phi(h_i)=p, h_i is nonspecial ascending, and its forward joint is the unique entrance of potential p-1. Let Y be the number of occupied cells that are not flat.
                                    
                                    Then
                                      s_int <= ceil((p-3)/2)+U+2Y,
                                    and hence
                                      U+2Y >= s_int-ceil((p-3)/2).
                                    
                                    Since
                                      s_int >= (5/8)p-eta_v-O(1),
                                    every low-defect misaligned center satisfies
                                      U+2Y >= (1/8)p-eta_v-O(1).
                                    
                                    Every cell counted by Y yields one of the following monotone outputs:
                                    (a) strict rank rise phi(h_i)>p;
                                    (b) a special edge h_i of rank p;
                                    (c) a nonspecial nonascending edge h_i of rank p whose three vertices all lie in the superlevel V_{>=p}={w:phi(w)>=p}.
                                    
                                    Thus the only asymptotically unpaid switching behavior is the forward-flat ascending branch, and clean entrance-retained switchers can occupy that branch with density at most one half along the host path.

                                • [1001215] Global monotone-payment charging would force a leading-coefficient gain
                                    STATEMENT
                                    Conjectural synthesis target. Let B be the active misaligned vertices and, for v in B with p_v=phi(v), let U_v and Y_v be the terminal-retained and nonflat-cell payments from 1001061. Seek an absolute-constant global charging inequality that bounds the total one-eighth payment sum_v(U_v+2Y_v) by bounded-congestion terminal resources: aligned-potential mass, rank-gap mass, special-edge mass, and monotone potential/rank-rise flow. Any such bound with no positive multiple of the full potential mass S on the right converts the local inequality U_v+2Y_v >= p_v/8-eta_v-O(1) into a strict improvement of the 43/48 leading coefficient.

                                  • [1001225] Near-43/48 obstructions force one globally linear enriched payment currency
                                      STATEMENT
                                      Assume a 43/48 near-extremal sequence with S=sum_v phi(v), S/n_+ -> infinity. Then, after discarding a set of centers of total endpoint-potential o(S), every remaining relevant center v of sufficiently large p=phi(v) admits a selected strict-gap paid family H_v of size at least (1/8-o(1))p such that every e in H_v is source-clean, terminal-single at both terminals, has edge rank strictly below both terminal vertex ranks, carries its selected common-anchor paid certificate at v, and is a minimum-rank chord of a clean fundamental cycle in the terminal-pair graph. For each such v, at least one of the following holds: (U) at least (1/16-o(1))p members of H_v are terminal-retained on the host path; (T) at least (1/128-o(1))p distinct early doubly occupied certificate cells occur, hence that many switcher triangles; (Z) at least (1/128-o(1))p distinct early paid cells have distinct standard output edges contained in V_{>=p}. Consequently, after partitioning centers by a witnessing case, at least one of U,T,Z has total center-indexed mass Omega(S) (indeed at least (1/384-o(1))S using the weakest coefficient).

                      • [1000773] Near-saturated gap-one vertices force linearly many balanced endpoint lenses on one maximum path
                          STATEMENT
                          Retain the gap-one switching setup of fecba48a3ffd. Thus phi(v)=q+1, q(v)=q, P is an arbitrary maximum (q+1)-edge path ending at v, and
                          delta=gamma(q)-(t(v)-X_v^T).
                          Then P supports at least
                          gamma(q)-ceil((3q-4)/4)-delta
                          distinct balanced endpoint-lens states.
                          
                          More precisely, there are that many distinct retained vertices c on P, each belonging to a switching edge f={v,c,d} that is double on a rank-q anchor path and single on P, such that for every chosen maximum endpoint path P_c ending at c, the pair P,P_c contains a balanced elementary lens adjacent to c.
                          
                          Consequently a near-saturated gap-one vertex forces
                          (5/8)q-O(1)-delta
                          pairwise distinct endpoint labels on one maximum path, each carrying a balanced-lens/no-piercing barrier.

                        • [1000465] Crossing balanced endpoint lenses on one maximum path must intersect off the host
                            STATEMENT
                            Let P be a maximum endpoint path ending at v. Let L_1 and L_2 be two clean balanced endpoint lenses attached to P, with host-side endpoint pairs (a,c) and (b,d) appearing in the order a<b<c<d along P. Let A_1,A_2 denote the corresponding off-P lens sides. Then A_1 and A_2 cannot be internally vertex-disjoint. Equivalently, any family of balanced endpoint lenses whose off-host sides are pairwise internally disjoint has a noncrossing (laminar/disjoint) family of host intervals.

                          • [1001163] A clean intersection of crossing balanced endpoint lenses yields two new maximum host-endpoint paths
                              STATEMENT
                              Let P be a maximum p-edge path ending at v. Let two balanced endpoint lenses have crossing host intervals [a,c] and [b,d] with a<b<c<d, and off-host sides A_1 from a to c and A_2 from b to d. Suppose w is a common vertex of A_1,A_2 such that, in each of the two displayed cross-splices, the chosen A_1- and A_2-subsegments meet only at w and are otherwise disjoint from the host pieces they are joined to. Then the two cross-splices
                              P[start,a] + A_1[a,w] + A_2[w,d] + P[d,v]
                              and
                              P[start,b] + A_2[b,w] + A_1[w,c] + P[c,v]
                              are both maximum p-edge paths ending at v.

                            • [1001184] Crossing-lens slack continuation
                                STATEMENT
                                Route bridge: the crossing endpoint-lens analysis continues after toolkit lemma 1000146.

                              • [1000594] Connected unique-intersection crossing components have constant rank-position difference
                                  STATEMENT
                                  Let P be a maximum p-edge path ending at v. For each vertex c in a finite set C, choose:
                                  (1) an occurrence of c on P, with kappa_P(c) equal to the number of P-edges in the prefix ending at that occurrence;
                                  (2) a maximum endpoint path P_c ending at c;
                                  (3) a common vertex a_c of P and P_c such that the P-segment P[a_c,c] and the corresponding P_c-segment have the same number of edges and have no common internal vertex.
                                  
                                  Define a graph G on C as follows. Join distinct c,d when their chosen P-intervals cross and the pair satisfies the hypotheses of 20606dbd4cd9 with P_c and P_d having exactly one common vertex.
                                  
                                  Then on every connected component K of G there is a constant sigma_K such that
                                    phi(c)-kappa_P(c)=sigma_K
                                  for every c in K.
                                  
                                  Consequently, if all vertex ranks phi(c), c in K, lie in an integer interval [A,B], then
                                    |K| <= B-A+1.
                                  In particular, no connected component contains two distinct vertices of the same vertex rank.

                                • [1001082] A narrow vertex-rank band bounds uniquely-intersecting crossing pairs
                                    STATEMENT
                                    Retain the setup and notation of 85d576d60e7e. Let X be any graph on the same vertex set C whose edges are crossing interval pairs for which the auxiliary maximum paths satisfy the cross-splice hypotheses of 20606dbd4cd9. Split
                                      E(X)=E_1 disjoint union E_2,
                                    where cd is in E_1 when P_c and P_d have exactly one common vertex, and cd is in E_2 when they have at least two common vertices.
                                    
                                    Assume every c in C has vertex rank in an integer interval [A,B], and put R=B-A+1. Then
                                      |E_1| <= (R-1)|C|/2.
                                    Consequently
                                      |E_2| >= |E(X)|-(R-1)|C|/2.
                                    
                                    Thus, whenever the crossing graph has more than (R-1)|C|/2 edges, at least one crossing pair has auxiliary maximum paths with at least two common vertices; any excess above that threshold counts distinct such crossing pairs.

                              • [1000782] Crossing balanced endpoint lenses at equal endpoint potential force a second auxiliary intersection
                                  STATEMENT
                                  Let P be a maximum host path. Let balanced endpoint lenses attached at distinct host vertices c<d have crossing host intervals. If phi(c)=phi(d), then the corresponding maximum endpoint paths P_c and P_d have at least two common vertices. Consequently they contain a balanced elementary lens of their own.

                        • [1000967] A terminal-retained switching endpoint recaptures its omitted entrance or the host endpoint on every maximum path
                            STATEMENT
                            Let f={v,x,u} be an ascending nonspecial edge of rank r with unique entrance x and terminals v,u. Suppose, in a gap-one switching state at host endpoint v, that u is the retained off-v vertex on the chosen maximum host path P while x is omitted. Then every maximum endpoint path P_u ending at u contains x or v. More precisely, if P_u uses f then phi(u)=r and P_u enters f through x, so x lies on P_u; if P_u does not use f, then avoidance of both x and v would allow f to be appended through terminal u, contradicting the rank/unique-entrance property of f.

                      • [1001114] Near-saturated gap-one states have linear symmetric difference and a dense switching matching
                          STATEMENT
                          In a near-saturated gap-one state p=q+1, the anchor-to-maximum switching matching has size s=(5/8)q-O(1)-delta and forces linear two-sided symmetric difference between the q-edge anchor Q and the maximum (q+1)-edge path P: each has at least s-O(1) vertices absent from the other. The s switching hyperedges form a matching through v pairing retained and omitted anchor vertices. Thus the hard shell is an ordered two-rail matching problem of density asymptotically 5/16 on the anchor precursor.

                        • [1000975] Every gap-one switching edge manufactures an endpoint lens on the maximum path
                            STATEMENT
                            Every switching edge in a gap-one anchor-to-maximum switching matching manufactures an endpoint lens on the maximum path P: if c is its unique retained off-v endpoint on P, then every maximum endpoint path P_c ending at c meets P in at least one additional vertex. Consequently a near-saturated gap-one vertex supports (5/8)q-O(1)-delta distinct endpoint-lens states attached to one maximum (q+1)-path.

                      • [1001118] Gap-one local slack splits exactly into anchor slack, foreign low-rank edges, and maximum-path doubles
                          STATEMENT
                          Let v lie in the gap-one shell phi(v)=q+1 with q(v)=q>=4. Let T be the family of ascending nonspecial edges terminal at v, t=|T|, and let P be any maximum (q+1)-edge path ending at v. Let X_v^T be the number of T-edges double on P. Put
                          J=J_q(v)={f containing v: phi(f)<=q},
                          M=gamma(q)=floor((11q-5)/8),
                          and
                          delta=M-(t-X_v^T).
                          
                          Then
                          delta=(M-|J|)+(|J|-t)+X_v^T.
                          All three summands are nonnegative. Consequently:
                          1. M-|J|<=delta;
                          2. |J|-t<=delta;
                          3. X_v^T<=delta.
                          
                          Thus a near-dangerous gap-one local state is simultaneously near-extremal for the fixed-entrance Astra system, contains at most delta low-rank incident edges outside the ascending-terminal family, and has at most delta ascending-terminal doubles on the maximum path.
                          
                          Combining with the periodic stability theorem, all but O(delta+1) cells of the anchor contact pattern lie on the critical period-four cycle, and all but O(delta) of the corresponding incident edges are ascending-terminal edges at v.

                        • [1000658] Near saturation leaves only O(delta) slots for one-rank-higher nonspecial terminal edges
                            STATEMENT
                            Let v lie in the gap-one shell phi(v)=q+1 with q(v)=q>=4. Choose a maximum-rank ascending nonspecial anchor
                                  e={x,v,u}
                                of rank q terminal at v, and let R be a canonical (q-1)-edge source rail ending physically at x, so R,e is a q-edge longest path and R avoids v,u. Put
                                  W=V(R) minus {x},
                                so |W|=2q-2.
                            
                            Let
                                  J=J_q(v)={f: v in f and phi(f)<=q},
                                  M=gamma(q)=floor((11q-5)/8),
                                  r=M-|J|,
                                and let U_R be the set of vertices of W unused by all contacts (f minus {v}) intersect W for f in J minus {e}.
                            
                            Let H_+(v) be the family of nonspecial edges h through v such that v is a terminal of h and phi(h)=q+1. Then
                                  |H_+(v)| <= |U_R| <= 2r+1.
                            
                            In the near-dangerous gap-one notation of f6c9ded0ae63, r<=delta, and therefore
                                  |H_+(v)| <= 2delta+1.
                            In particular, at exact local saturation delta=0 there is at most one nonspecial rank-(q+1) edge terminal at v.

                  • [1001230] Near-extremal singleton transfer is periodic away from few defects
                      STATEMENT
                      For the singleton-column transfer automaton used in the 43/48 contact-conflict bound, let an admissible state walk have N transitions, transition weights w_i, and total weight W. If W >= 3N/4-D, then at most 4D+6 transitions fail to lie on the four-cycle 00->01->11->10->00. Hence, after deleting those exceptional transition positions, every remaining interval has the period-four singleton-column weight pattern 2,1,0,0, up to phase.

            • [1000737] Near the seven-sixths floor, almost all vertices have a special subhypergraph confined to individual potential levels
                STATEMENT
                Let H be a finite linear 3-graph with φ(v)≥3 for all v. Define t_ns(v) as the number of nonspecial edges terminal at v, a(v)=2φ(v)-3-t_ns(v), and b(v)=2φ(v)-1-d_D^-(v). Call v Type A when (a(v),b(v))=(2,0). Every Type-A vertex v, writing p=φ(v), has exactly four incident special edges, all of rank p; every nonspecial edge terminal at v has rank at most p-1; and every nonspecial edge whose unique entrance is v is ascending. Thus every special edge whose vertices are Type A has equal vertex ranks, and every ascending arc entering a Type-A terminal raises vertex rank by at least two.
                
                More quantitatively, write Σ_v φ(v)=m+(7/6)n+ηn with η>=0. There is W⊆V(H), with |W|≥(1-66η)n, such that: (i) all vertices of W are Type A; (ii) the hypergraph consisting of the original special edges contained in W has minimum degree at least two and maximum degree at most four; (iii) every component of this special subhypergraph lies in one vertex-rank level; and (iv) every originally nonspecial edge contained in W is ascending, with both terminals of vertex rank at least two greater than its entrance. All ranks and classifications here are evaluated in H, not recomputed after deletion. Also, at most 30ηn special edges meet a non-Type-A vertex.

              • [1000134] Type-A terminal ranks either branch or form an exact ladder down to an exceptional entrance
                  STATEMENT
                  Let v be Type A with p=phi(v)>=5. For 2<=r<=p-1 let n_r(v) be the number of nonspecial edges of rank exactly r for which v is a terminal, and put
                    N_r(v)=sum_{j=2}^r n_j(v).
                  
                  Then:
                    N_r(v)<=2r-3
                  for every r, and
                    N_{p-1}(v)=2p-5=2(p-1)-3.
                  
                  Consequently exactly one of the following holds.
                  
                  (BRANCH) For some r with 3<=r<=p-1,
                    n_r(v)>=3.
                  
                  (LADDER) One has
                    n_2(v)=1
                  and
                    n_r(v)=2
                  for every 3<=r<=p-1.
                  
                  Moreover, in the LADDER case the unique rank-two nonspecial terminal edge through v has a non-Type-A unique entrance whenever all Type-A vertices in the ambient argument have potential at least three.

                • [1000350] A Type-A branching layer is either upper-half or exposes an exceptional entrance
                    STATEMENT
                    Let v be Type A with p=phi(v)>=5. Suppose for some rank r with 3<=r<=p-1 there are at least three nonspecial rank-r edges terminal at v.
                    
                    If
                      p>=2r-3,
                    then at least one of those rank-r edges has a non-Type-A unique entrance.
                    
                    Equivalently, if all entrances of a three-edge rank-r terminal subfamily are Type A, then
                      p<=2r-4,
                    so
                      r>=ceil((p+4)/2).

                • [1000797] One exceptional entrance supports at most four Type-A ladder vertices
                    STATEMENT
                    Assume every vertex has endpoint potential at least three. Let L be the set of Type-A vertices that fall in the LADDER alternative of 1e24a8fe7b2a.
                    
                    For each v∈L, let e_v be its unique rank-two nonspecial terminal edge and let x_v be the unique entrance of e_v. Then x_v is non-Type-A.
                    
                    For every fixed exceptional vertex x,
                      |{v∈L:x_v=x}|<=4.
                    Consequently, if E is the non-Type-A vertex set,
                      |L|<=4|E|.

              • [1000351] Type-A vertices force an exact saturated rank-minus-one terminal fan
                  STATEMENT
                  Let v be Type A with p=phi(v)>=5. Then v has exactly 2p-5 nonspecial terminal edges, all of rank at most p-1, and at least one has rank p-1.
                  
                  Fix a rank-(p-1) nonspecial terminal edge h through v and a longest
                    P=(g1,...,g_{p-1}=h)
                  ending in h with last vertex v. Put
                    W=V(P)\h
                  and
                    C=g_{p-3}\g_{p-4},
                  so |W|=2p-4 and |C|=2.
                  
                  For every other nonspecial terminal edge f through v:
                  1. f meets W\C;
                  2. the sets (f\{v})∩(W\C) are singletons and, as f varies, partition W\C;
                  3. f has at most one additional P-contact, necessarily in C.
                  
                  Consequently at most two of the 2p-6 edges f!=h are double-blocking on P, and at least 2p-8 are single-blocking.

                • [1000706] Type-A saturation forces rank-preserving propagation to a second terminal edge
                    STATEMENT
                    Continue in the saturated Type-A fan of 4c0a0105c825. Put q=p-1 and
                      P=(g1,...,g_q=h),
                    and write
                      C=g_{q-2}\g_{q-3}.
                    
                    Let
                      alpha=g_{q-3}∩g_{q-2},
                    and let beta be the private vertex of g_{q-1}, i.e. the vertex of g_{q-1} outside g_{q-2}∪h.
                    Let f_alpha,f_beta be the unique terminal edges whose W\C partition contacts are alpha,beta.
                    
                    Then:
                    1. f_alpha has no additional C-contact; its only P-contact outside v is the joint alpha.
                    2. f_beta has no additional C-contact either.
                    3. Consequently phi(f_beta)=q and beta is the unique entrance of f_beta.
                    
                    Thus every Type-A saturated fan around a rank-q=p-1 terminal edge h canonically produces a second rank-q nonspecial terminal edge through v, whose unique entrance is the private vertex beta of the penultimate edge of the chosen h-witness path.

                  • [1000724] Exactly two top terminal edges at a Type-A vertex force a universal two-entrance gate
                      STATEMENT
                      Let v be Type A with p=phi(v)>=5 and put q=p-1. Let T_q(v) be the set of nonspecial terminal edges through v having rank exactly q.
                      
                      Then |T_q(v)|>=2.
                      
                      If |T_q(v)|=2, write
                        T_q(v)={h1,h2}
                      and let x1,x2 be their unique entrances. Then there is a unique hyperedge g containing {x1,x2}, and g has the following universal-gate property:
                      
                      For i=1,2, every longest q-edge path ending in h_i with last vertex v has g as its penultimate edge. On such a path the penultimate edge g meets h_i at x_i, while the other entrance x_{3-i} is the private vertex of g relative to that path.

                • [1000763] A Type-A saturated rank-minus-one fan has at least p minus five genuine early private rotations
                    STATEMENT
                    In the setting of 4c0a0105c825, let v be Type A with p=phi(v)>=5, choose a rank-(p-1) nonspecial terminal edge h through v, and let
                      P=(g_1,...,g_{p-1}=h)
                    be a longest path ending in h at physical terminal v. Put
                      W=V(P)\h,
                      C=g_{p-3}\g_{p-4}.
                    
                    Among the other 2p-6 nonspecial terminal edges through v, at least p-4 are single-blocking on P whose unique W\C contact is a private/free vertex of its path edge. At most one of these has that contact on g_{p-2}; consequently at least
                      p-5
                    have a private/free unique precursor contact on one of
                      g_1,...,g_{p-4}.
                    
                    For each such early private-contact edge f, f meets P in exactly two path edges: its contact edge g_j and the last edge h, so the certified two-contact Posa rotation applies.

                  • [1001139] Type-A rotation expansion forces linearly many near-top-potential vertices on one witness path
                      STATEMENT
                      Let v be Type A with p=phi(v)>=7. In the saturated rank-(p-1) witness setting of a9ce4e3cd5da, there exists a longest
                        P=(g_1,...,g_{p-1}=h)
                      ending at v such that at least
                        2p-12
                      distinct vertices of V(P) have endpoint potential at least p-1.
                      
                      More precisely, there are at least p-6 distinct indices
                        j∈{1,...,p-4}
                      for which an early private-contact blocker yields a Posa rotation, and for every such j both vertices of
                        g_{j+2}\g_{j+3}
                      have endpoint potential at least p-1. These two-vertex sets are pairwise disjoint as j varies.

              • [1000632] Type-A potential levels have a two-level predecessor-capacity recurrence
                  STATEMENT
                  Assume every vertex has endpoint potential at least three. Let E be the set of non-Type-A vertices and, for each integer p, let
                    T_p={v: v is Type A and phi(v)=p}.
                  If T_p is nonempty, then
                    |E| + sum_{q<=p-2}|T_q| >= 2p-5.
                  
                  More precisely, for every v∈T_p the 2p-5 nonspecial terminal edges through v have pairwise distinct unique entrances, all lying in
                    E ∪ (union_{q<=p-2} T_q).

          • [1000480] General snake upper bound improved to (ell-2)n
              STATEMENT
              For every ell>=4, every n-vertex linear 3-uniform hypergraph with no linear path P_ell^(3) has at most (ell-2)n edges. Thus ex_L(n,P_ell^(3)) <= (ell-2)n. The proof combines the ordinary snake hinge with a second-order terminal blocker count; it improves the Devine--Milans (ell-3/2)n bound by n/2.

        • [1000651] General upper bound improved to (ell-11/6)n by terminal-snake localization
            STATEMENT
            For every ell>=3, every n-vertex linear 3-uniform hypergraph with no linear path P_ell^(3) has at most (ell-11/6)n edges. Equivalently ex_L(n,P_ell^(3)) <= (ell-11/6)n. This improves the Devine--Milans general bound (ell-3/2)n by n/3.

      • [1000616] A vertex on a linear path has half-path endpoint potential
          STATEMENT
          Let P=(e_1,...,e_p) be a p-edge linear path in a linear hypergraph, and let w be any vertex in V(P). Then φ(w)>=ceil(p/2). More precisely, if w lies in exactly one path edge e_i then φ(w)>=max{i,p-i+1}; if w=e_i∩e_{i+1} is a path joint then φ(w)>=max{i,p-i}.

        • [1000421] Low-vertex-rank labels occupy a bounded central window on a linear path
            STATEMENT
            Let P=(g_1,...,g_L) be an L-edge linear path in a linear 3-uniform hypergraph, and let R be an integer with 0<=R<L.
            
            Then the number of vertices z in V(P) with
              phi(z)<=R
            is at most
              max{0, 4R-2L+1}.
            
            More precisely, if such a vertex z is private to one path edge g_i, then
              L-R+1 <= i <= R.
            If z is the joint g_i intersect g_{i+1}, then
              L-R <= i <= R.
            
            Consequently, when R>=ceil(L/2), all vertices of P with vertex rank at most R consist of at most
              2R-L
            eligible private vertices and
              2R-L+1
            eligible joints.

          • [1000573] Shared entrances on one higher-rank source path force quadratic edge-rank mass
              STATEMENT
              Let
                e_1,...,e_M
              be distinct ascending nonspecial edges with unique entrances
                x_1,...,x_M
              and edge ranks
                r_1<=...<=r_M.
              Let A be a canonical maximum source path for another ascending edge of edge rank Q, so A has Q-1 edges. Assume every x_j lies on A and every r_j<=Q.
              
              Then for each j=1,...,M,
                r_j >= ceil((2Q+j+1)/4).
              
              Consequently
                sum_{j=1}^M r_j
                >= (MQ)/2 + M(M+3)/8.
              
              Equivalently, relative to the baseline Q/2 per edge, M distinct entrance labels lying on one Q-source path force a quadratic rank-mass bonus of at least M(M+3)/8.

        • [1000808] Potential-charged ascending edges: transversals, central packing, and deficit spacing
            STATEMENT
            Let v have p=φ(v). For every potential-charged ascending nonspecial edge e={x,v,u} with v terminal and φ(u)>=p, every p-edge path ending at v contains x or u; for distinct such edges the pairs {x,u} are pairwise disjoint.
            
            If C_Q(v) denotes the charged edges of rank at most Q, where ceil((p+2)/2)<=Q<=p, then
            |C_Q(v)|<=4Q-2p-1.
            Equivalently, if their ranks are q_1<=...<=q_k, then q_i>=ceil((2p+i+1)/4).
            
            Fix now a maximum p-edge path P=(g_1,...,g_{p-1},h) ending at v and restrict to charged edges e={x,v,u} distinct from h with E(P)∩e represented only by the entrance contact x and v. For two such edges e_1,e_2 whose entrance-contact blocks [a(e_i),b(e_i)] are separated by at least one path edge, one has
            b(e_2)-a(e_1) >= p-φ(e_2)+3
            after ordering the contacts from left to right. Consequently, for every D>=0, the number of clean entrance-only charged edges of rank at most p-D is O(p/(D+1)+1), with an absolute implied constant.

          • [1000473] Terminal-tail blockers recover the sharp central-window packing bound
              STATEMENT
              Let v have p=phi(v). For potential-charged ascending nonspecial edges e={x,v,u} with v terminal, phi(u)>=p and phi(e)<=Q, where ceil((p+2)/2)<=Q<=p, let C_Q(v) be their set. Then |C_Q(v)|<=4Q-2p-3. Hence, if their ranks are q_1<=...<=q_k, then q_i>=ceil((2p+i+3)/4).

            • [1000155] Path-relative central-window packing for common-terminal ascending edges
                STATEMENT
                Let P=(g_1,...,g_r) be an r-edge linear path ending at a vertex v. Let F_Q be any family of distinct ascending nonspecial edges e={x,v,u} for which v is a terminal vertex and phi(e)<=Q, where ceil((r+2)/2)<=Q<=r. Then |F_Q|<=4Q-2r-3. In particular, if q_1<=...<=q_k are the ranks of such edges, then q_i>=ceil((2r+i+3)/4) whenever P has length r at least q_i. No potential-charging assumption and no maximality of P at v are required.

          • [1000723] Four-edge spacing conjecture for potential-charged ascending edges
              STATEMENT
              Fix a vertex v and let e_i={x_i,v,u_i}, i=1,2,3,4, be four ascending nonspecial edges for which v is terminal and φ(u_i)>=φ(v). Order q_i=φ(e_i) so q_1<=q_2<=q_3<=q_4. Then 2q_2>=q_1+q_4+1.

            • [1000055] Canonical-entrance cross-blocker reduction for charged four-edge spacing
                STATEMENT
                Let e_1,e_2,e_4 be ascending nonspecial edges with common terminal v and ranks q_1<=q_2<=q_4. Let Q=(g_1,...,g_M), M=q_4-1, be the precursor of a longest q_4-edge path Q,e_4 ending at v, and let x_i be the unique entrance of e_i. Assume e_2∩V(Q)={x_2}, and let b be the last index of a Q-edge containing x_2. Assume e_1 is disjoint from V(g_b∪...∪g_M). Let R be a canonical (q_1-1)-edge entrance path for e_1 ending at x_1 and avoiding the two terminal vertices of e_1. If R is disjoint from e_4 and from V(g_b∪...∪g_M), then 2q_2>=q_1+q_4+2.

            • [1000721] Every charged four-edge spacing violation is tail-terminal or splice-blocked
                STATEMENT
                Let e_i={x_i,v,u_i}, i=1,2,3,4, be potential-charged ascending nonspecial edges through a common terminal v, with q_1<=q_2<=q_3<=q_4. Suppose 2q_2<q_1+q_4+1. Fix a q_4-edge path P_4 ending in e_4 with last vertex v, and a (q_1-1)-edge path Q_1 ending at x_1 such that Q_1,e_1 is a longest path ending in e_1. Then either (A) x_2 is absent from P_4 and u_2 occurs in one of the final q_2-2 precursor edges of P_4, or (B) x_2 lies on P_4 and the splice Q_1,e_1,e_4 followed by the reverse P_4-tail down to x_2 is not a linear path. Thus every spacing counterexample is forced into a terminal-tail state or an explicit cross-intersection obstruction.

            • [1001012] Pure rank-five at potential five forces a multi-precursor competitor
                STATEMENT
                Assume phi(v)=5 and four potential-charged ascending nonspecial rank-five edges are terminal at v. Fix one as e4 and a five-edge path
                  P=(g1,g2,g3,g4,e4)
                ending in e4 with physical terminal v.
                
                Let f be one of the other three competitors.
                
                If f meets exactly one precursor path edge among g1,g2,g3,g4, then that edge is either g2 or g4, and the contact vertex is the private vertex of that path edge. If the unique precursor edge is g4, that private vertex is the unique entrance of f.
                
                Consequently at most two of the three competitors can meet exactly one precursor path edge, and therefore at least one competitor meets at least two precursor path edges.

              • [1000760] Joint-only blockers in the p=5 pure rank-five obstruction are pushed away from the final joint
                  STATEMENT
                  In the p=5 pure rank-five setup, fix
                    P=(g1,g2,g3,g4,e4)
                  ending in the rank-five nonspecial edge e4 at terminal v. Put
                    r=g1∩g2,
                    a=g2∩g3,
                    c=g3∩g4,
                    d=g4∩e4.
                  
                  Let f be another rank-five charged edge through v whose only precursor vertex is a path joint.
                  
                  Then that joint cannot be c.
                  
                  If the joint is a, then phi(c)>=5.

            • [1000522] Clean doubly-terminal-single minimum-terminal edges violate spacing in two double cells
                STATEMENT
                For every integer R>=39 there is a finite linear 3-graph with four ascending nonspecial edges e_i={x_i,v,u_i}, edge ranks (R+1,R+1,R+7,R+7), and phi(v)=phi(u_i)=R+9. All four chosen source paths are clean and all four edges are terminal-single on the common maximum v-path and on their respective maximum u_i-paths. Their contacts form two doubly occupied cells. Thus conditions 1-4 of the paid target do not imply four-edge spacing. Both cells are unpaid apart from their single triangle contribution, and this is not a counterexample to the full selected paid-switching hypothesis.

              • [1000127] Strict-rise clean U11 edges still violate four-edge spacing
                  STATEMENT
                  For every integer R>=43 there is a finite linear 3-graph with four ascending nonspecial edges
                    e_i={x_i,v,u_i},  i=1,2,3,4,
                  having ordered edge ranks
                    (R+1,R+1,R+7,R+7),
                  such that
                    phi(v)=R+9,
                    phi(u_i)=R+10  for every i.
                  Moreover the four chosen source paths are clean and every e_i is terminal-single on the chosen maximum paths at both terminals.
                  
                  Thus all four edges have strict terminal-potential rise away from the common terminal v, yet
                    2q_2=2R+2 < 2R+9=q_1+q_4+1.
                  Hence four-edge deficit-doubling is false even for source-clean, doubly-terminal-single, strict-rise ascending edges.
                  
                  The construction still does not supply the genuine common-anchor selected-certificate hypothesis needed by the repaired post-43/48 target.

            • [1000013] Charged four-edge spacing implies logarithmic charged degree and the 2/3 leading coefficient
                STATEMENT
                Assume the charged four-edge spacing conjecture above. For every vertex v with p=φ(v)>=1, the number c_+(v) of ascending nonspecial edges e={x,v,u} with v terminal and φ(u)>=p is at most 3+ceil(log_2 p). Consequently every n-vertex P_ell^(3)-free linear 3-graph satisfies |E(H)| <= ((2ell + ceil(log_2(ell-1)))/3)n for ell>=2, and in particular has leading coefficient 2/3.

          • [1000804] Any rank-long terminal path has a terminal-tail blocker
              STATEMENT
              Let e={x,u,v} be a nonspecial edge with rank q=φ(e) and unique entrance x, with u,v its two terminal vertices. Let P=(g_1,...,g_r) be a linear path of length r>=q ending at u. Then either e is the last edge of P, necessarily r=q and the penultimate edge meets e at x, or P does not use e and one of x,v occurs in the final q-2 precursor edges g_{r-q+2},...,g_{r-1}. The analogous statement holds with u and v interchanged.

            • [1000207] A high-terminal witness gives a nondecreasing-potential endpoint rotation
                STATEMENT
                Let e={x,v,u} be an ascending nonspecial edge with rank q, let p=φ(v), and assume v is terminal and φ(u)>=p. Let P=(g_1,...,g_p) be a maximum p-edge path ending at v. If x∉V(P), then u∈V(P). Let j be the first index of a path edge containing u. Then j<=p-2, and the sequence (g_1,...,g_j,e,g_p,g_{p-1},...,g_{j+2}) is a p-edge linear path. Moreover it has a last vertex w=g_{j+1}∩g_{j+2} (with the evident interpretation w=g_{p-1}∩g_p when j=p-2), so φ(w)>=p. Thus every charged edge on a maximum v-ending path either contributes its low-potential entrance x as a path witness or yields a length-preserving rotation to an endpoint of potential at least φ(v).

              • [1000761] Endpoint-state Minty walk for potential-charged edges
                  STATEMENT
                  Use maximum paths with a distinguished last vertex as states. At state (P,v), every potential-charged ascending edge at v either places its low-potential entrance on P or, by the endpoint-rotation lemma, gives a move to a new state (P',w) with φ(w)>=φ(v). Analyze a walk that repeatedly takes such moves whenever too many charged edges are witnessed by their high terminals.

            • [1000485] Reciprocal-tail uncrossing for charged spacing
                STATEMENT
                For a potential-charged ascending edge e={x,v,u}, compare a maximum φ(v)-edge path ending at v with a maximum φ(u)-edge path ending at u. The terminal-tail lemma forces {x,u} into the final q-2 precursor edges of the first path and {x,v} into the final q-2 precursor edges of the second. Use this reciprocal pair of tail constraints as the basic state for proving charged four-edge spacing or a direct sublinear charged-degree bound.

      • [1000830] The fixed-target single-blocker rotation graph is K4-free
          STATEMENT
          In the boundary fixed-target endpoint-preserving single-blocker rotation graph of 68593c300c9c, no four distinct path states are pairwise rotation-adjacent. Equivalently, the rotation graph contains no K4.

      • [1000366] Reciprocal stretch bound for ascending edges
          STATEMENT
          Let H be a finite linear 3-graph on n vertices. For each ascending nonspecial edge e={x,u,v}, write q(e)=phi(e) and p(e)=min{phi(u),phi(v)}. Then q(e)>=2, q(e)<=p(e)<=2q(e)-2, and sum_e (1/(q(e)-1)-1/p(e)) <= 5n/4.

      • [1000216] Positive potential-gap terminal graphs are rainbow-path-free and have logarithmic reciprocal mass
          STATEMENT
          For t>=1, form the terminal-pair graph R_t^+ from nonspecial edges whose entrance x has phi(x)<t while both terminal potentials are at least t, coloring each terminal pair by x. The coloring is proper and R_t^+ has no rainbow t-edge path. Hence in any P_ell-free linear 3-graph,
            sum_e (1/a(e)-1/p(e)) = O(n log ell)
          over all nonspecial edges with entrance potential a(e)<p(e), with the certified bound (9/7)n(1+log(ell-1))+O(n).

      • [1000983] Longest-path terminal degree with exact double-blocker slack
          STATEMENT
          Let P=(e_1,...,e_L) be a globally longest linear 3-uniform path with last vertex z in e_L, and let B_P(z) count incident edges f≠e_L whose two non-z vertices both lie in V(P)\e_L. Then
            d_H(z)+B_P(z) <= 2L-1.
          In particular d_H(z)<=2L-1, so every linear 3-graph of minimum degree delta has a path of length at least ceil((delta+1)/2).

      • [1000692] Ascending-edge defect reduces to near-top clean chords and high-potential rotation endpoints
          STATEMENT
          Let H be a P_ell^(3)-free linear 3-graph with m edges and n vertices. Let A be the number of ascending edges. For every nonspecial nonascending edge f with unique entrance x define
            r(f)=ceil(phi(x)/(phi(f)-1))-2,
          and let R=sum_f r(f). Then
            3m-A+R <= sum_v(2phi(v)-1) <= (2ell-3)n.
          
          Choose for every vertex v a maximum p=phi(v) path P_v ending at v and assign every ascending nonspecial edge e={x,v,u} to a terminal v of minimum terminal potential. Apart from at most one assigned last edge per vertex, every assigned edge is of type D (both x,u on P_v), X (x on P_v,u off P_v), or U (u on P_v,x off P_v). If B is the chosen-path double-blocker compensation and S_X,S_U are the X,U counts, then
            A<=B+S_X+S_U+n
          and, with N=(2ell-3)n,
            5m+s+R <= 2N+S_X+S_U+n.
          For every fixed epsilon>0, the X-edges with phi(e)<=(1-epsilon)phi(v) contribute only O_epsilon(n).
          
          Moreover, for a fixed charged pair (P_v,v), the U-edges expand with multiplicity at most two into distinct canonical Pósa endpoints w of potential at least phi(v): if W(P_v,v) is the set of resulting endpoints then
            |U(P_v,v)| <= 2|W(P_v,v)|+1.
          Thus the leading ascending-edge obstruction is localized to near-top-rank clean entrance chords and large sets of nondecreasing-potential rotation endpoints.

      • [1000912] Rank-three incoming localization is sharp at rank four
          STATEMENT
          At any vertex z of a linear 3-graph, at most two nonspecial incoming snake edges of rank at most 3 can coexist. This threshold is sharp without additional hypotheses: there is a linear triple system with three distinct nonspecial incoming snake edges of rank exactly 4 at one vertex.

      • [1000032] Reconstruction of Astra 11/12 clean-contact route
          STATEMENT
          Astra interruption reconstruction: the certified inequality 3m-A<=2 sum_v phi(v)-n would combine with a local/global clean-contact packing bound A<=3/4 sum_v phi(v) to give m<=11/12 sum_v phi(v)-n/3, hence m<=((11ell-15)/12)n in a P_ell-free system. The likely local form is t_up(v)<=3phi(v)/2, obtained by pairing linearly many nearby path-contact slots and forbidding simultaneous clean occupancy. The exact splice remains unproved; naive consecutive single-blocker pairing is known false.

        • [1000031] A clean private entrance forbids every private single contact two positions earlier
            STATEMENT
            Let P=(g_1,...,g_p) be a maximum p-edge linear path ending at v with last vertex v, with last edge h=g_p. Let e and f be distinct ascending nonspecial edges through v, neither equal to h.
            
            Assume e meets V(P)\\h in exactly one vertex r, private to g_j (r may be either the entrance or the opposite terminal of e). Assume f meets V(P)\\h in exactly one vertex y, where y is the unique entrance of f and is private to g_{j+2}. Then this configuration is impossible.

        • [1000383] Three-quarters potential-oriented local bound gives Astra 11/12 coefficient
            STATEMENT
            For every vertex v with p=phi(v), at most floor(3p/4) ascending nonspecial edges e={x,v,u} have v terminal and phi(u)>=p. This implies A<=3/4 sum_v phi(v) by assigning each ascending terminal pair to its lower-potential endpoint, hence m<=11/12 sum_v phi(v)-n/3 and m<=((11ell-15)/12)n for P_ell-free systems. The target is already established at p=2,3 and p=4; p=5 is exactly the current four-charged-edge elimination problem.

          • [1000177] Two consecutive charged rank levels suffice for the 11/12 leading coefficient
              STATEMENT
              Suppose that for every vertex v and every q, at most three potential-charged ascending terminal edges at v have ranks in {q,q+1}. Then the certified charged-rank window implies c_+(v)<=floor(3phi(v)/4) in three residue classes and <=floor(3phi(v)/4)+1 in the fourth; using the current odd-central-window bound gives the exact floor bound in all residues. The +1 fallback already implies A<=3/4 sum phi+n and hence m<=11/12 sum phi<=11/12(ell-1)n for P_ell-free systems. This two-rank block statement is distinct from full four-edge spacing: the pattern q,(q+1),(q+1),(q+1) satisfies the spacing inequality at equality but is forbidden here.

            • [1000184] The top-boundary q,(q+1)^3 obstruction has a fixed four-slot witness normal form
                STATEMENT
                Let v have p=phi(v)=2q-2, q>=3. Suppose four potential-charged ascending nonspecial edges are terminal at v with ranks
                  q,q+1,q+1,q+1.
                Let e={x,v,u} be the rank-q edge. Fix any maximum p-edge path
                  P=(g_1,...,g_{2q-2})
                ending at v.
                
                Put
                  a=g_{q-2}∩g_{q-1},
                  b=private(g_{q-1}),
                  x=g_{q-1}∩g_q,
                  c=private(g_q),
                  d=g_q∩g_{q+1}.
                
                Then x is the universal entrance of e. The three rank-(q+1) competitors admit distinct path-relative witnesses occupying three of the four vertices {a,b,c,d}. Moreover any witness equal to c or d is necessarily the unique entrance of its rank-(q+1) edge. Terminal-only witnesses are possible only at a or b.
                
                In particular at least one rank-(q+1) competitor has a visible entrance in {c,d}, of potential q.

              • [1000018] At the half-rank top boundary every high competitor has a visible entrance
                  STATEMENT
                  Assume the top-boundary q,(q+1)^3 configuration of 28445330afcc:
                    phi(v)=2q-2,
                    P=(g_1,...,g_{2q-2})
                  is a maximum path ending physically at v,
                    e={x,v,u}
                  has rank q with universal entrance
                    x=g_{q-1}∩g_q,
                  and h is one of the rank-(q+1) charged competitors through v.
                  
                  Then the unique entrance of h lies on P. Consequently the three high-edge entrances are three distinct vertices among
                    a=g_{q-2}∩g_{q-1},
                    b=private(g_{q-1}),
                    c=private(g_q),
                    d=g_q∩g_{q+1}.
                  In particular each of these three selected witnesses has endpoint potential exactly q.

                • [1000593] A left-joint high entrance forces its high terminal across the central cut
                    STATEMENT
                    In the half-rank top-boundary q,(q+1)^3 configuration, if the left joint a=g_{q-2}∩g_{q-1} is a rank-(q+1) high entrance, then that high edge's opposite terminal must occur in the right suffix g_q,...,g_{2q-3}. Otherwise h_a,g_{2q-2},...,g_q is a q-edge path ending at the low entrance x, contradicting phi(x)=q-1.

                  • [1000348] A left-joint high entrance cannot close onto the central edge
                      STATEMENT
                      In the half-rank top-boundary q,(q+1)^3 gadget, if a=g_{q-2}∩g_{q-1} is a high entrance h_a={a,v,z_a}, then z_a cannot lie in g_q. Indeed g_1,...,g_{q-2},h_a,g_q is a q-edge path ending at x=g_{q-1}∩g_q, contradicting phi(x)=q-1. Hence z_a lies strictly in the right suffix g_{q+1},...,g_{2q-3}. In particular the proposed missing-slot closures z_a=d in abc and z_a=c in abd are impossible.

                    • [1000327] The d-free abc top-boundary pattern also has a crossed blocker moat
                        STATEMENT
                        Assume q>=4 and the all-visible top-boundary q,(q+1)^3 configuration with occupied high entrances
                          a=g_{q-2}∩g_{q-1},
                          b=private(g_{q-1}),
                          c=private(g_q),
                        while d=g_q∩g_{q+1} is unoccupied.
                        Write
                          h_a={a,v,z_a}, h_b={b,v,z_b}, h_c={c,v,z_c}.
                        
                        Then
                          z_a,z_b ∈ V(g_{q+1}∪...∪g_{2q-3}),
                        and
                          last_P(z_c)<=q-4.
                        
                        Thus abc also has a genuine two-right/one-left terminal split across the central block. In particular no opposite terminal of an occupied high edge lies in g_{q-1}∪g_q.

                    • [1001006] Every top-boundary pattern contains a far crossed pair
                        STATEMENT
                        Assume q>=4 and the all-visible top-boundary q,(q+1)^3 normal form
                           P=(g_1,...,g_{2q-2}),
                           a=g_{q-2}∩g_{q-1},
                           b=private(g_{q-1}),
                           x=g_{q-1}∩g_q,
                           c=private(g_q),
                           d=g_q∩g_{q+1},
                        with phi(x)=q-1. For every occupied slot y let
                           h_y={y,v,z_y}
                        be its rank-(q+1) high edge.
                        
                        For a path vertex w, write first_P(w) for the least index of a path edge containing w.
                        
                        Then:
                        
                        1. If c is occupied, z_c lies in the left prefix and
                              first_P(z_c) <= q-4.
                        
                        2. If d is occupied, z_d lies in the left prefix and
                              first_P(z_d) <= q-4.
                        
                        3. If a is occupied, z_a lies strictly in the right suffix
                              V(g_{q+1}∪...∪g_{2q-3}).
                        
                        4. If b and d are both occupied, z_b lies in the same strict right suffix.
                        
                        Consequently every one of the four occupied triples abc, abd, acd, bcd contains a far crossed pair
                           h_L={L,v,z_L}, h_R={R,v,z_R}
                        with
                           L∈{a,b}, R∈{c,d},
                           z_L∈V(g_{q+1}∪...∪g_{2q-3}),
                           first_P(z_R)<=q-4.

                • [1000596] The half-rank four-slot gadget has a three-edge conflict graph with forced cross-blockers
                    STATEMENT
                    In the top-boundary q,(q+1)^3 four-slot normal form, let
                     a=g_{q-2}∩g_{q-1},
                     b=private(g_{q-1}),
                     x=g_{q-1}∩g_q,
                     c=private(g_q),
                     d=g_q∩g_{q+1}.
                    Every occupied slot y is the unique entrance of a rank-(q+1) high edge h_y={y,v,z_y}.
                    
                    Then the slot pairs {a,c}, {a,d}, and {b,d} are conflict pairs in the following precise sense.
                    
                    (A) If a and r are occupied, where r∈{c,d}, then at least one of:
                      z_r ∈ V(g_1∪...∪g_{q-2}),
                      z_a ∈ V(g_1∪...∪g_{q-2}∪g_q)
                    must hold.
                    
                    (B) If b and d are occupied, then at least one of:
                      z_b ∈ V(g_{q+1}∪...∪g_{2q-3}),
                      z_d ∈ V(g_{q+1}∪...∪g_{2q-3}∪g_{q-1})
                    must hold.
                    
                    Consequently every three-of-four entrance pattern on {a,b,c,d} forces at least one explicit opposite-terminal cross-blocker, because every 3-subset contains one of the conflict pairs ac,ad,bd.

                  • [1000422] Corrected acd top-boundary blocker moat
                      STATEMENT
                      In the half-rank top-boundary q,(q+1)^3 configuration, suppose the occupied high-entrance slots are a,c,d (so b is omitted). Write
                       h_a={a,v,z_a}, h_c={c,v,z_c}, h_d={d,v,z_d}.
                      Then:
                      (1) z_d has a path occurrence in the left prefix, and its last occurrence index there is at most q-4;
                      (2) z_a has a path occurrence in the right suffix and does not lie in g_q, hence its first path-edge occurrence on the right is at least q+1;
                      (3) z_c has a path occurrence in the left prefix, with last occurrence at most q-3.
                      
                      Thus the two right-side high edges have distinct high-potential opposite terminals strictly left of the central cells, while the left-side high edge has its opposite terminal strictly right of g_q.

                  • [1000623] The four top-boundary missing-slot patterns reduce to crossed terminals plus two exact closures
                      STATEMENT
                      For q>=4, the all-visible top-boundary q,(q+1)^3 gadget has the following pattern structure. In abd, z_d is forced left and z_b right; z_a is right, with the only exact central closure z_a=c. In bcd, z_d is forced left and z_b right. In abc, either z_c is forced left or z_a=d, the missing slot. In acd, z_d,z_c are left and z_a right with the two-cell moat bounds. Thus every pattern contains an explicit left/right terminal crossing, and the only central escape states are the exact missing-slot closures z_a=c (abd) and z_a=d (abc).

                  • [1000857] The bcd top-boundary pattern forces a three-edge blocker moat
                      STATEMENT
                      Assume the half-rank top-boundary q,(q+1)^3 configuration with q>=4 and occupied high-entrance slots b,c,d. Write h_b={b,v,z_b}, h_c={c,v,z_c}, h_d={d,v,z_d}. Then last_P(z_c)<=q-4 and last_P(z_d)<=q-4, while z_b lies strictly to the right of g_q. Thus the two right-side entrance edges send their high opposite terminals at least three cells into the left prefix, while the left-private entrance sends its terminal across the central cut. No claim is made here that first_P(z_b)>=q+2; the exact g_{q+1} cross-block state remains to be analyzed.

                  • [1000883] Joint-pair conflict collapses to a left blocker or the missing right-private slot
                      STATEMENT
                      In the all-visible top-boundary q,(q+1)^3 gadget, if both joint slots a and d are occupied, then either the opposite terminal z_d of the d-edge lies in the strict left prefix g_1,...,g_{q-2}, or the opposite terminal z_a of the a-edge equals c, the right-private slot. Consequently in pattern acd one necessarily has z_d in the left prefix, while in pattern abd the only alternative is the exact missing-slot closure z_a=c.

                  • [1000939] Every d-containing top-boundary pattern has a common blocker moat
                      STATEMENT
                      In the half-rank top-boundary q,(q+1)^3 configuration with q>=4, suppose the occupied high-entrance slots include d=g_q∩g_{q+1}. Then the high opposite terminals split 1-versus-2 across the central block. Every terminal on the left side has last path-edge occurrence at most q-4, while every terminal on the right side lies strictly to the right of g_q. More precisely: abd has z_d left with last<=q-4 and z_a,z_b right of g_q; acd has z_d,z_c left with last<=q-4 and z_a right of g_q; bcd has z_d,z_c left with last<=q-4 and z_b right of g_q. No q+2 first-occurrence bound is asserted; g_{q+1} is an exact residual cross-block state.

                    • [1000451] Every top-boundary q,(q+1)^3 pattern contains a genuine crossed high-edge pair
                        STATEMENT
                        Assume q>=4 and the all-visible top-boundary q,(q+1)^3 configuration on a maximum
                          P=(g_1,...,g_{2q-2})
                        ending at v, with low entrance
                          x=g_{q-1}∩g_q
                        and high entrance slots
                          a=g_{q-2}∩g_{q-1},
                          b=private(g_{q-1}),
                          c=private(g_q),
                          d=g_q∩g_{q+1}.
                        
                        Then among the three occupied high edges there exist two,
                          h_L={y_L,v,z_L}, h_R={y_R,v,z_R},
                        such that
                          y_L∈V(g_{q-1})\{x},   z_L∈V(g_q∪...∪g_{2q-3}),
                        while
                          y_R∈V(g_q)\{x},       z_R∈V(g_1∪...∪g_{q-2}).
                        
                        Thus one high edge crosses the central cut left-to-right and another crosses it right-to-left.
                        
                        Moreover, if d is occupied then the right-to-left terminal may be chosen with last occurrence at most q-4 and the left-to-right terminal with first occurrence at least q+2, by d22fb281de15.

                      • [1000020] Strict-rise high terminals have reciprocal central entrance structure
                          STATEMENT
                          Let h={y,v,z} be ascending nonspecial of rank q+1 with phi(y)=q, phi(v)=2q-2, and phi(z)>=2q-2. Then phi(z)<=2q. If phi(z)=2q, every maximum 2q-edge path ending at z contains y, necessarily at its unique central joint. If phi(z)=2q-1, then on every maximum z-path either y lies in one of the three central slots, or y is absent and v is forced to be the unique central joint r_{q-1}∩r_q. Thus every strict-rise charged terminal has a reciprocal central-gate normal form.

                      • [1000258] Every top-boundary critical gadget contains a rank-q base with two rank-(q+1) entrance sides
                          STATEMENT
                          In the half-rank top-boundary q,(q+1)^3 configuration, q>=4, let
                            P=(g_1,...,g_{2q-2})
                          be maximum at v and
                            x=g_{q-1}∩g_q
                          the universal entrance of the low rank-q edge.
                          
                          Then
                            phi(g_{q-1})=phi(g_q)=q,
                          and both g_{q-1},g_q are ascending nonspecial edges with unique entrance x.
                          
                          Writing
                            g_{q-1}={x,a,b},
                            g_q={x,c,d},
                          the three high entrances occupy three of {a,b,c,d}. Therefore at least one of the pairs {a,b}, {c,d} is fully occupied.
                          
                          Consequently the critical gadget contains a linear 3-cycle
                            g_*, h_r, h_s
                          where g_* has rank q and unique entrance x, while h_r,h_s have rank q+1, share the common terminal v, and their respective entrances r,s are exactly the two terminal vertices of g_*.

                        • [1000906] A rank-mixed central triangle orders its two far high terminals
                            STATEMENT
                            In the top-boundary q,(q+1)^3 configuration, suppose the left central base
                              g_{q-1}={x,a,b}
                            has both terminals a,b occupied as high entrances:
                              h_a={a,v,z_a}, h_b={b,v,z_b}.
                            Then z_a,z_b lie to the right of g_q. Let k_a,k_b be their first path-edge occurrence indices. Then
                              k_a<=k_b.
                            
                            Dually, if the right central base
                              g_q={x,c,d}
                            has both c,d occupied, and i_c,i_d are the last path-edge occurrence indices of their opposite terminals on the left, then
                              i_d>=i_c.
                            
                            Thus on either fully occupied central base, the far terminal belonging to the joint entrance is weakly closer to the center in path order than the far terminal belonging to the private entrance.

                • [1001023] Every high entrance rail in the critical two-rank pattern crosses the low edge
                    STATEMENT
                    Let
                      e={x,v,u}
                    be an ascending nonspecial edge of rank q with unique entrance x. Let
                      h={y,v,z}
                    be a distinct ascending nonspecial edge of rank q+1 through the same terminal v.
                    
                    Let
                      R=(r_1,...,r_q)
                    be a canonical q-edge entrance path ending physically at y such that
                      R,h
                    is a longest (q+1)-edge path ending in h through its unique entrance y; in particular R avoids the terminals v,z.
                    
                    Then
                      V(R)∩{x,u} is nonempty.
                    
                    Consequently, in a q,(q+1)^3 configuration, the three canonical entrance rails of the high edges each cross the two-vertex gate {x,u}; hence two of the three rails cross the same gate vertex.

                • [1001070] Every left-central high entrance sends its opposite terminal across the cut
                    STATEMENT
                    In the half-rank top-boundary q,(q+1)^3 configuration, let
                     y∈{a,b}⊂V(g_{q-1})\{x}
                    be an occupied high entrance, and write h_y={y,v,z_y}. Then
                      z_y ∈ V(g_q∪g_{q+1}∪...∪g_{2q-3}).
                    Thus every high edge whose entrance lies on the left central edge g_{q-1} sends its charged opposite terminal across the central cut to the right.

              • [1000298] A right-joint high entrance pushes the low terminal to the first path edge
                  STATEMENT
                  In the top-boundary q,(q+1)^3 setup, suppose the right joint d=g_q∩g_{q+1} is a visible rank-(q+1) entrance, so phi(d)=q. If the low rank-q edge's opposite terminal u occurs in the left prefix, then u is forced to be private in g_1. More generally, if j is its last occurrence index, the rotation g_1,...,g_j,e,g_p,...,g_{q+1} gives phi(d)>=j+q-1, hence j<=1.

              • [1000508] Top-boundary q,(q+1)^3 obstructions have at least two visible high entrances
                  STATEMENT
                  In the top-boundary q,(q+1)^3 four-slot normal form, at least two of the three rank-(q+1) charged competitors have their unique entrances visible in the four central slots. Indeed c,d are always entrance slots when occupied, and the left pair a,b cannot both be terminal-only witnesses. Hence the obstruction contains at least two distinct visible vertices of potential q adjacent to the universal low entrance x of potential q-1.

                • [1000153] Every visible high entrance rail crosses the other three charged edges
                    STATEMENT
                    In a q,(q+1)^3 charged configuration at terminal v, let h_i be a rank-(q+1) high edge and R_i any canonical q-edge entrance rail for h_i. Then the low rank-q edge e meets one of the final q-2 edges of R_i, and each of the other two rank-(q+1) high edges meets R_i. Thus every visible high entrance yields a q-edge rail simultaneously transversal to all three other charged edges.

                  • [1000138] A low edge can meet a high entrance rail late only as a double blocker
                      STATEMENT
                      In the setup of 21dfd53c201f, let e={x,v,u} be the low rank-q edge and let Q_i=(r_1,...,r_q) be a canonical q-edge entrance rail for a rank-(q+1) high edge h_i={y_i,v,z_i}, with phi(y_i)=q.
                      
                      Then e meets Q_i. If e has exactly one contact vertex w on Q_i and k is the last path-edge index containing w, then
                        3<=k<=q-2.
                      Thus a one-contact low blocker lies in the interior rail band r_3,...,r_{q-2}; if e meets either of the final two rail edges r_{q-1},r_q, then e has two contacts on Q_i.

                  • [1000291] High entrance rails have exact clean interior bands and double-only terminal cells
                      STATEMENT
                      Let e={x,v,u} have rank q and let h_1,h_2,h_3 have rank q+1 in a q,(q+1)^3 charged configuration at the common terminal v. Fix i and a canonical q-edge entrance rail Q_i=(r_1,...,r_q) for h_i.
                      
                      Then every foreign charged edge meets Q_i, with the following exact one-contact bands:
                      
                      - for j!=i, if h_j has exactly one contact on Q_i, its contact occurs in r_2,...,r_{q-2};
                      - if e has exactly one contact on Q_i, its contact occurs in r_3,...,r_{q-2}.
                      
                      Consequently any foreign charged edge meeting r_{q-1} or r_q is necessarily a double blocker on Q_i.

                    • [1000795] In the 4555 rank-pair state the low edge double-blocks every high entrance rail
                        STATEMENT
                        In a charged rank pattern (4,5,5,5) at a common terminal v, let e={x,v,u} be the rank-four edge and let h_i be any rank-five high edge. For any canonical four-edge entrance rail Q_i for h_i, both x and u lie on Q_i. Equivalently, the low edge e is a double blocker on every high entrance rail.

                    • [1000908] Distance-two single blockers are incompatible on every canonical entrance rail
                        STATEMENT
                        Let h={y,v,z} be an ascending nonspecial edge of rank Q>=3 with unique entrance y, and let R=(r_1,...,r_{Q-1}) be a canonical entrance path ending at y and avoiding v,z, so R,h is a longest Q-edge path ending in h.
                        
                        Let f_1,f_2 be distinct edges through v, neither equal h. Suppose each f_i meets V(R) in exactly one vertex, private to r_{a_i}. Then |a_1-a_2|!=2.

                  • [1000703] A unique intersection of two equal-potential entrance rails is an aligned joint
                      STATEMENT
                      Let
                         Q=(e_1,...,e_q),   Q'=(f_1,...,f_q)
                      be q-edge linear paths ending physically at vertices y,y' with
                         phi(y)=phi(y')=q.
                      Assume
                         V(Q)∩V(Q')={w}.
                      
                      Then w is a path joint on both rails, and at the same index: there exists
                         1<=t<=q-1
                      such that
                         w=e_t∩e_{t+1}=f_t∩f_{t+1}.
                      
                      Apply this to two canonical high entrance rails Q_i,Q_j in a q,(q+1)^3 configuration. If their only common vertex is w, then their mandatory crossings of the opposite high edges are reciprocal terminal crossings:
                         z_j∈V(Q_i),   z_i∈V(Q_j).
                      Indeed Q_i cannot meet h_j at y_j, and Q_j cannot meet h_i at y_i, because y_j∈Q_j and y_i∈Q_i would give additional common vertices.

                    • [1000404] Three critical high entrance rails force a two-vertex overlap
                        STATEMENT
                        In a q,(q+1)^3 charged configuration at a common terminal v, let
                           h_i={y_i,v,z_i},  i=1,2,3,
                        be the three rank-(q+1) high edges, and let Q_i be arbitrary canonical q-edge entrance rails ending at y_i.
                        
                        Then some pair Q_i,Q_j has at least two distinct common vertices.

                  • [1001106] A competing high edge can meet a high entrance rail late only as a double blocker
                      STATEMENT
                      Let h_i={y_i,v,z_i} and h_j={y_j,v,z_j} be distinct ascending nonspecial edges of rank q+1 through the common terminal v, with phi(y_i)=phi(y_j)=q. Let Q_i=(r_1,...,r_q) be a canonical q-edge entrance path ending at y_i and avoiding v,z_i.
                      
                      Assume h_j meets V(Q_i) in exactly one vertex w, and let k be the last path-edge index containing w. Then k<=q-2. Equivalently, a one-contact competing high edge cannot meet either of the final two edges r_{q-1},r_q of Q_i.

              • [1000903] Right-side high entrances obey a conditional left-prefix recoil and unconditional low-rail crossing
                  STATEMENT
                  In the top-boundary q,(q+1)^3 setting of 28445330afcc, let P=(g_1,...,g_{2q-2}) end at v with last vertex v, let e={x,v,u} be the rank-q edge with x=g_{q-1}∩g_q, and let h={y,v,z} be a rank-(q+1) charged competitor whose selected witness is a right slot y∈{c,d}. Then y is the unique entrance of h and phi(y)=q.
                  
                  Moreover, if the low edge e has no second contact with the prefix P^-=(g_1,...,g_{q-1}) besides x, then z lies in V(P^-). Unconditionally, h meets every canonical (q-1)-edge entrance rail for e; on any such rail avoiding y, the forced contact is z.

              • [1001221] Top-boundary d-patterns have a forced crossed-terminal orientation
                  STATEMENT
                  Assume q>=4 in the all-visible top-boundary q,(q+1)^3 four-slot normal form, with low entrance x=g_{q-1}∩g_q and occupied high slots among a,b,c,d. If d=g_q∩g_{q+1} is occupied, then d is a high entrance, the low terminal u is absent from the entire left prefix, and the opposite terminal z_d lies on the left, by g_{q-3} whenever b is also occupied. Consequently every occupied triple containing d is crossed: in abd, z_d lies left while z_a,z_b lie right; in bcd, z_d lies left while z_b lies right; in acd, z_d and z_c lie strictly left while z_a lies strictly right.

            • [1000240] At the half-rank boundary a charged low-rank edge has a universal central-joint witness
                STATEMENT
                Let v have phi(v)=2q-2 and let e={x,v,u} be a potential-charged ascending nonspecial edge of rank q with v terminal. Then on every maximum (2q-2)-edge path P=(g_1,...,g_{2q-2}) ending at v, the path-relative witness for e is the unique central joint g_{q-1}∩g_q. Hence either the entrance x is that central joint (if x lies on P) or the opposite terminal u is that central joint (if x is absent).

              • [1000379] Half-rank charged edges are reciprocally central at both terminals
                  STATEMENT
                  If e={x,v,u} is ascending nonspecial of rank q, charged at terminal v with phi(v)=2q-2 and phi(u)>=phi(v), then phi(u)=phi(v)=2q-2. Consequently the central-joint localization of 351720508b02 applies symmetrically at both terminals: every maximum (2q-2)-edge path ending at v or u has the witness for e at its unique central joint.

                • [1000363] A half-rank charged edge has the same universal central entrance at both terminals
                    STATEMENT
                    Let e={x,u,v} be an ascending nonspecial edge of rank q, with unique entrance x. Suppose
                      phi(u)=phi(v)=2q-2.
                    Then for every maximum (2q-2)-edge path ending physically at either terminal u or v, the unique central joint is x.
                    
                    Equivalently, if
                      P_v=(g_1,...,g_{2q-2})
                    ends at v, then
                      x=g_{q-1}∩g_q,
                    and if
                      P_u=(h_1,...,h_{2q-2})
                    ends at u, then
                      x=h_{q-1}∩h_q.

              • [1000545] Half-rank boundary edges have reciprocal central-joint constraints at both terminals
                  STATEMENT
                  Let e={x,u,v} be ascending nonspecial of rank q, with unique entrance x. Suppose
                    phi(u)=phi(v)=2q-2.
                  Then for every maximum (2q-2)-edge path P_v ending at v, its unique central joint
                    c_v=g_{q-1}∩g_q
                  lies in {x,u}; and for every maximum (2q-2)-edge path P_u ending at u, its unique central joint lies in {x,v}.
                  
                  Equivalently, if a maximum v-ending path avoids the entrance x, then u is its central joint; if a maximum u-ending path avoids x, then v is its central joint.

              • [1000670] Clean contacts two positions apart cannot coexist on a canonical low-rank entrance rail
                  STATEMENT
                  Let e={x,v,u} be ascending nonspecial of rank q with unique entrance x, and let R=(r_1,...,r_{q-1}) be a canonical entrance path ending at x and avoiding v,u. If two distinct edges through terminal v each meet R in exactly one private contact, on path edges r_a and r_b respectively, then |a-b|≠2. Indeed contacts two positions apart splice through the two common-v edges to form a q-edge path ending at x, contradicting phi(x)=q-1. Adjacent positions are not covered because of the inherited r_a-r_{a+1} intersection.

                • [1000555] Every one-rank-higher terminal competitor crosses the low entrance rail
                    STATEMENT
                    Let e={x,v,u} be ascending nonspecial of rank q with unique entrance x and terminal v. For every canonical (q-1)-edge entrance path R ending at x with R,e a longest q-edge path, every nonspecial rank-(q+1) edge h through v for which v is terminal must meet R. Otherwise R,e,h is a longest (q+1)-edge path entering h through terminal v, contradicting the unique entrance of h.

                  • [1000128] Canonical source rails are downward-complete against common-terminal competitors
                      STATEMENT
                      Let e={x,v,u} be an ascending nonspecial edge of rank r>=2, with unique entrance x and terminal v. Let
                      R=(g_1,...,g_{r-1})
                      be any canonical maximum source rail ending at x such that R,e is a longest r-edge path ending in e through x; in particular R avoids v and u.
                      
                      Let f be any distinct nonspecial edge through v for which v is a terminal, and suppose phi(f)<=r+1. Then f meets V(R).
                      
                      Consequently, for any family e_1,...,e_k of ascending nonspecial edges terminal at the same vertex v, ordered by nondecreasing ranks r_1<=...<=r_k, every canonical source rail R_j of e_j meets every earlier edge e_i, i<j. More generally R_j meets every family edge of rank at most r_j+1.

                    • [1000051] Canonical source rails of arbitrary common-terminal ascending edges are pairwise intersecting
                        STATEMENT
                        Let e_i={x_i,v,u_i} and e_j={x_j,v,u_j} be distinct ascending nonspecial edges terminal at the same vertex v, with ranks r_i<=r_j. Let R_i,R_j be canonical maximum source rails ending at x_i,x_j, of lengths r_i-1,r_j-1, each avoiding the two terminals of its own edge. Then V(R_i)∩V(R_j) is nonempty. Thus the source rails of any finite family of ascending nonspecial edges sharing a terminal form a pairwise-intersecting family, with no restriction on the rank gaps.

                      • [1000419] The simple-intersection graph of arbitrary common-terminal source rails is triangle-free
                          STATEMENT
                          Let e_1,...,e_k be ascending nonspecial edges terminal at one vertex v, and choose a canonical maximum source rail R_i ending at the unique entrance x_i of each edge. Every two rails intersect. Form a graph S on {1,...,k} by joining i,j exactly when V(R_i) intersect V(R_j) consists of one vertex. Then S is triangle-free. Consequently at least binom(k,2)-floor(k^2/4) rail pairs have at least two common vertices.

                    • [1001134] Rank-ordered source rails force linear distinguished overlap
                        STATEMENT
                        Let e_1,...,e_k be distinct ascending nonspecial edges terminal at a common vertex v, ordered so that
                        r_1<=...<=r_k,
                        where r_i=phi(e_i). Write e_i={x_i,v,u_i}, with x_i the unique entrance, and choose a canonical maximum source rail R_j ending at x_j for every j.
                        
                        Fix integers h,m>=1 with h+m<=k, and choose any m indices
                        j_1,...,j_m > h.
                        For each chosen rail R_j and each coordinate i<=h, the rail meets {x_i,u_i}. Consequently some pair of the m chosen rails has at least
                        h * floor((m-1)^2/4) / C(m,2)
                        common distinguished vertices from the disjoint pairs {x_i,u_i}, i<=h.
                        In particular this is at least
                        h (m-2)/(2(m-1))
                        for m>=2, and is h/2-O(h/m).
                        
                        Taking the last m=k-h rails and h=floor(k/2), some two source rails share at least
                        k/4-O(1)
                        distinct distinguished vertices. Thus a common-terminal family of k ascending edges necessarily contains a pair of maximum source rails with linear overlap.

                      • [1000395] Near-dangerous gap-one states force two near-top source rails with eleven-sixteenths overlap
                          STATEMENT
                          Let v lie in the gap-one shell phi(v)=q+1, q(v)=q>=4. Let T be the family of ascending nonspecial edges terminal at v, let k=|T|, and let
                          delta=gamma(q)-(k-X_v^T),
                          where X_v^T>=0 is the number of T-edges double on a chosen maximum (q+1)-path and gamma is the exact fixed-entrance bound. Then k>=gamma(q)-delta.
                          
                          Fix an integer m with 3<=m<k. Let D be any integer with 0<=D<q-3 such that
                          gamma(q)-gamma(q-D)>delta+m.
                          Then at least m edges of T have rank greater than q-D.
                          
                          Choose canonical maximum source rails for any m such top-rank edges. Some pair of these rails shares at least
                          (k-m) floor((m-1)^2/4) / C(m,2)
                          distinct distinguished source-or-opposite-terminal vertices belonging to the other edges of T.
                          
                          Consequently, for any near-dangerous sequence with delta=o(q), one may choose m tending to infinity with
                          m=o(q) and delta=o(m), obtaining two ascending edges of ranks q-o(q) whose canonical maximum source rails share
                          (11/16-o(1))q
                          distinct distinguished vertices.

                        • [1001022] Near-dangerous gap-one states force a macroscopic lens-free overlap of near-top maximum paths
                            STATEMENT
                            First, let R be a maximum endpoint path ending at y. Among all maximum endpoint paths Q ending at x, choose Q to maximize |V(Q) intersect V(R)|. Then Q and R contain no genuine clean internal lens with distinct Q- and R-sides.
                            
                            Consequently, in the near-dangerous gap-one setting of 58659c428983 with delta=o(q), there exist two vertices x,y with
                            phi(x)=q-o(q),  phi(y)=q-o(q),
                            and maximum endpoint paths Q_x,Q_y ending at x,y such that
                            |V(Q_x) intersect V(Q_y)| >= (11/16-o(1))q,
                            while Q_x,Q_y contain no genuine clean internal lens.
                            
                            Thus every asymptotically dangerous gap-one state contains a canonical residual object: two almost-q-long maximum paths with macroscopic intersection but no switchable internal lens.

                          • [1000186] Overlap-maximal maximum path pairs admit no clean complementary switch
                              STATEMENT
                              Let R be a maximum endpoint path ending at y, and among all maximum endpoint paths ending at x choose Q to maximize |V(Q) intersect V(R)|. Let A be a nonempty union of pairwise internally vertex-disjoint internal subpaths of Q, and B a nonempty union of pairwise internally vertex-disjoint internal subpaths of R, with the same boundary attachment vertices.
                              
                              Assume:
                              (i) replacing A by B in Q produces a linear path Q* ending at x;
                              (ii) replacing B by A in R produces a linear path R* ending at y;
                              (iii) every interior vertex of A is outside R, and every interior vertex of B is outside Q.
                              
                              Then no such complementary switch exists.

                          • [1000385] Unlabeled lens-free overlap of maximum paths can be complete
                              STATEMENT
                              For every q>=5 with q not congruent to 1 modulo 3, there is a finite linear 3-uniform hypergraph on 2q+1 vertices containing two edge-disjoint q-edge maximum endpoint paths Q,R with
                                V(Q)=V(R),
                              and with no genuine clean internal lens between Q and R. In particular Q is overlap-maximal relative to R, yet the pair has no shared edge and cannot be simplified by a clean internal lens.
                              
                              Thus macroscopic overlap plus overlap-maximal lens-free normalization alone cannot force a shared-edge core or a longer-path contradiction. Any post-43/48 braid classification must use the distinguished ascending-edge labels or additional ambient structure.

                          • [1000985] Overlap-maximal maximum paths contain no clean four-point crossing braid cell
                              STATEMENT
                              Let R be a maximum endpoint path ending at y, and among all maximum endpoint paths ending at x let Q maximize |V(Q) intersect V(R)|. Suppose four common vertices a,b,c,d lie internally on both paths, in the order
                                a,b,c,d along Q
                              and
                                a,c,b,d along R.
                              Assume the six open path segments determined by these four vertices are clean: between a and d, the Q- and R-segment interiors meet the other path only at the displayed common vertices. Then this configuration is impossible.

                            • [1000333] Adjacent R-contacts either pay length deficit or saturate the Q-segment with common vertices
                                STATEMENT
                                Let R be a maximum endpoint path ending at y, and among all maximum endpoint paths ending at x let Q maximize |V(Q) intersect V(R)|. Let a,b be two internal common vertices that are consecutive on R in the strong sense that the R-subpath R[a,b] meets Q only at a and b. Put
                                  s=|R[a,b]|,  d=|Q[a,b]|.
                                Then d>=s. Moreover, if d=s, every vertex of Q[a,b] other than a,b belongs to R. Equivalently, the Q-side of every zero-length-deficit adjacent R-contact interval is completely saturated by common vertices.

                        • [1001218] Lens-free near-top rails retain a linear family of whole distinguished chords
                            STATEMENT
                            In the near-equality common-terminal ascending family of rank q, there exist two near-top maximum endpoint paths Q,R of endpoint rank q-o(q) such that Q and R have no genuine clean internal lens, |V(Q)∩V(R)| >= (5/4-o(1))q, and at least (25/88-o(1))q early distinguished source-terminal pairs {x_i,u_i} are wholly contained in V(Q)∩V(R). In addition, the underlying rail family has near-complete coverage of a common distinguished universe and contains a pair with (16/11-o(1))q common vertices.

                          • [1000156] RETRACTED: low-rank residue from the lens-free whole-pair braid
                              STATEMENT
                              Retracted. The claimed positive-density lower-rank subfamily does not follow from the cumulative fixed-entrance bound. That bound says the number of common-terminal ascending edges of rank at most s is at most gamma(s); therefore it gives a lower bound, not an upper bound, on the number of edges with rank greater than s. The proof of the previous version reversed this inequality. No low-rank residue follows from 3ef8a7c2d941 by this counting argument.

                          • [1000176] A whole ascending chord localizes its opposite terminal to the far end of every avoiding rail
                              STATEMENT
                              Let e={x,v,u} be an ascending nonspecial edge of rank r with unique entrance x, so phi(x)=r-1. Let Q=(g_1,...,g_L) be a linear path avoiding v and containing both x and u. Assume x and u do not lie on a common Q-edge (automatic when e is not an edge of Q by linearity).
                              
                              If x occurs before u along Q, let b be the last index of a Q-edge containing u. Then
                              L-b+1 <= r-2
                              in the convention that the reversed suffix g_L,...,g_b has L-b+1 edges and ends at u.
                              Symmetrically, if u occurs before x and a is the first index of a Q-edge containing u, then
                              a <= r-2.
                              
                              Equivalently: delete u from the path-order picture and take the Q-side from u toward the endpoint that does not contain x. That side has at most r-2 edges. Thus for every whole contact pair {x,u} of an external ascending edge on a canonical source rail, the opposite terminal u is forced into an (r-2)-edge end-zone on the side opposite its entrance x.

                            • [1000832] A paired terminal inside its source endpoint lens spends the remaining edge rank
                                STATEMENT
                                Let e={x,v,u} be an ascending nonspecial edge of rank r, with unique entrance x, so phi(x)=r-1. Let S be a maximum (r-1)-edge path ending at x that avoids u and v. Let Q be another maximum endpoint path containing x, and let z,x bound a clean balanced endpoint lens between S and Q, with both lens sides of length t.
                                
                                Assume u lies in the interior of the Q-side from z to x, and assume the Q-subpath from z to u avoids v. Let a be the number of Q-edges from z to u along that side (choosing the occurrence that precedes x). Then
                                  t+a+1 <= r.
                                Equivalently,
                                  a <= r-t-1.
                                
                                Thus if an endpoint lens at the entrance of an ascending edge uses almost all of the source rank, its paired terminal cannot lie deep inside a v-avoiding host side: it is forced into the first r-t-1 edges from the far lens boundary z.

                            • [1001067] A whole chord is endpoint-slack-shallow or its clean source rail reintersects the opposite side
                                STATEMENT
                                Let e={x,v,u} be an ascending nonspecial edge of rank r, with unique entrance x, and let
                                  S=(s_1,...,s_{r-1})
                                be a maximum source path ending at x such that S,e is a longest r-edge path ending in e through x and S avoids u,v.
                                
                                Let R be any linear path avoiding v and containing both x and u. Let a be the endpoint of R lying on the side of u opposite x in the path order, and let T be the R-segment from u to a. Write t=|T| for its number of edges.
                                
                                Then either
                                
                                (A) t <= phi(a)-r,
                                
                                or
                                
                                (B) S meets V(T).
                                
                                Every intersection in (B) is a common vertex of S and R distinct from x (and from u), so S and R have at least two distinct common vertices.
                                
                                In particular, if R=(g_1,...,g_L) is a maximum endpoint path ending at y with phi(y)=L, and x occurs before u toward y, then a=y and
                                  t <= L-r
                                unless the clean source rail reintersects the u-to-y suffix.
                                
                                For the precursor of a rank-q ascending anchor path this specializes to
                                  t <= q-r-1
                                in the unobstructed forward orientation.

                              • [1000609] Forward common-anchor chords pay quadratic deficit or source-rail reintersection
                                  STATEMENT
                                  Let h be an ascending nonspecial anchor of rank q terminal at v, and let
                                    Q=(g_1,...,g_{q-1},h)
                                  be a longest q-edge h-path ending at v. Put
                                    R=(g_1,...,g_{q-1}),
                                  and let y be the endpoint of R adjacent to the anchor entrance side, so phi(y)=q-1 and R ends at y.
                                  
                                  Let F be a family of distinct ascending nonspecial edges
                                    e={x_e,v,u_e}
                                  terminal at v, each of rank r_e<=q, such that both x_e,u_e lie on R and x_e occurs before u_e in the orientation of R toward y. For each e choose a clean maximum source path S_e ending at x_e.
                                  
                                  Call e simple-forward if S_e has no vertex on the R-side from u_e to y. Put
                                    delta_e=q-r_e.
                                  
                                  Then for every simple-forward e,
                                    the R-suffix from u_e to y has at most delta_e-1 edges.
                                  
                                  Consequently, if the simple-forward edges are ordered so that
                                    delta_1<=...<=delta_m,
                                  then
                                    delta_i >= ceil((i+1)/2)
                                  for every i, and hence
                                    sum_{i=1}^m delta_i >= sum_{i=1}^m ceil((i+1)/2) >= m^2/4.
                                  
                                  Equivalently: among forward-oriented whole chords on one common anchor, a family with small total anchor-rank deficit must contain many edges whose clean source rails reintersect the far anchor suffix. In particular every forward whole chord of rank q or q-1 necessarily has such a second source/anchor intersection.

                              • [1001058] A forward whole-chord reintersection pays a nonspecial cycle budget
                                  STATEMENT
                                  Retain the hypotheses and notation of ed412ed8e3b1 and suppose branch (B) occurs. Let z be the first vertex of S that lies on the far suffix of R from u toward y, when that suffix is traversed starting at u. Let
                                    a = number of R-edges from u to z along that suffix,
                                    b = number of S-edges from z to x along S toward its endpoint x.
                                  
                                  Then
                                    a+b <= r-1.
                                  
                                  Equivalently, the first reintersection that allows a forward whole chord to evade the deficit-shallow alternative cannot be simultaneously far from u on the host rail and far from x on the clean source rail.

                              • [1001001] High-rank unobstructed whole chords pack into two endpoint vertex-rank zones
                                  STATEMENT
                                  Let R be a linear path with endpoints a,b, avoiding a common vertex v. Let F be a family of distinct ascending nonspecial edges
                                    e={x,v,u}
                                  such that, for every e in F,
                                  - both x and u lie on R;
                                  - e has rank r=phi(e);
                                  - a clean maximum source path S_e ending at x is fixed.
                                  
                                  Call e unobstructed on R if S_e does not meet the R-side from u toward the endpoint lying opposite x.
                                  
                                  Fix an integer R0. Then the number of unobstructed members of F with rank at least R0 is at most
                                    max(0,2(phi(a)-R0)+1)
                                    + max(0,2(phi(b)-R0)+1).
                                  
                                  Consequently, every additional rank-at-least-R0 whole chord beyond this endpoint-zone capacity has a clean source rail with a second intersection with R on the side beyond its opposite terminal.

                                • [1000161] Top-band common-anchor chords are controlled by opposite-end excess plus return cycles
                                    STATEMENT
                                    Let h be an ascending nonspecial anchor of rank q terminal at v, and let
                                      Q=(R,h)
                                    be a longest q-edge h-path ending at v, where the precursor R has q-1 edges and avoids v. Let its endpoints be a and y, with y the anchor entrance endpoint, so
                                      phi(y)=q-1.
                                    Put
                                      E=phi(a)-(q-1)>=0.
                                    
                                    Let F be any family of distinct source-clean whole chords
                                      e={x,v,u}
                                    on R: each e is ascending nonspecial terminal at v, both x,u lie on R, and a clean maximum source path S_e ending at x is fixed.
                                    
                                    For an integer D>=0, let F_D consist of the members with
                                      phi(e)>=q-D.
                                    Call e unobstructed if S_e does not meet the R-side beyond u toward the endpoint opposite x.
                                    
                                    Then
                                      |{e in F_D : e unobstructed}|
                                      <= 2E+4D+2.
                                    Consequently
                                      |{e in F_D : S_e has a second intersection with R beyond u}|
                                      >= |F_D|-(2E+4D+2).
                                    
                                    Thus, in a common-anchor selected family, any top-D rank band larger than the sum of the opposite-end excess E and the band width D necessarily creates proportionally many distinguished source/anchor return cycles.

                          • [1000345] Every retained whole chord spans another common vertex in the lens-free braid
                              STATEMENT
                              In the setup of 3ef8a7c2d941, let Q,R be the two lens-free near-top maximum endpoint paths and let e_i={x_i,v,u_i} be one of the retained early distinguished edges whose whole pair {x_i,u_i} lies in V(Q)∩V(R). Then x_i and u_i are not consecutive common vertices on both rails simultaneously. Equivalently, at least one of the two Q- or R-segments between x_i and u_i contains a third vertex of V(Q)∩V(R) in its interior. Hence all (25/88-o(1))q retained whole distinguished pairs span nontrivial common-vertex structure in the normalized braid.

                          • [1000888] Earlier first contact of two common-hub double chords is bounded by the later chord rank
                              STATEMENT
                              Let P=(g_1,...,g_L) be a linear path avoiding a vertex v. Let f and h be distinct nonspecial edges through v, each having exactly two vertices on P, and assume v is terminal at h (equivalently, v is not the unique entrance of h). Let i_f and i_h be the first path-edge indices meeting f and h, respectively. If i_f<i_h and r=phi(h), then i_f<=r-3.
                              
                              In particular, for any family of pairwise distinct nonspecial edges through an external hub v that each double-contact P and at which v is terminal, ordering the edges by strictly increasing first-contact indices forces every earlier first-contact index to be at most the rank of every later edge minus three.

                          • [1000901] Two separated endpoint lenses from one source rail are at most half-rank
                              STATEMENT
                              Let S be a maximum (r-1)-edge path ending at x, so phi(x)=r-1. Let Q and R be maximum endpoint paths containing x. Suppose z_Q,x and z_R,x bound clean balanced endpoint lenses between S,Q and S,R respectively, chosen on the x-side of S, with side lengths t_Q and t_R.
                              
                              Assume the two host-side lens paths Q[z_Q,x] and R[z_R,x] meet each other only at x. Then
                                max{t_Q,t_R} <= r/2.
                              Equivalently, if either source endpoint lens has length greater than r/2, the Q- and R-host sides must have a second common vertex away from x.
                              
                              In the whole-pair braid, where S is a canonical source rail for an ascending rank-r edge with entrance x, every source lens longer than half the parent rank therefore forces additional local overlap between the two lens-free host rails.

                      • [1000722] Same-type distinguished overlap yields two balanced endpoint lenses per label
                          STATEMENT
                          Let H be a finite linear 3-graph. Let v be a vertex with \(\phi(v)=p\), and let
                          \[
                          e_i=\{x_i,v,u_i\},\qquad i=1,\dots,k,
                          \]
                          be distinct ascending nonspecial edges terminal at \(v\), where \(x_i\) is the unique entrance of \(e_i\). Assume that \(v\) has minimum vertex rank among the two terminal vertices of every \(e_i\), so \(\phi(u_i)\ge p\). Order the edges so that \(q_1\le\cdots\le q_k\), where \(q_i=\phi(e_i)\), and choose a canonical maximum source rail \(R_i\) of length \(q_i-1\) ending at \(x_i\).
                          
                          Put \(h=\lfloor k/2\rfloor\) and \(m=k-h\). If \(k\ge4\), then there are two indices \(a,b>h\) and a set \(I\subseteq\{1,\dots,h\}\) with
                          \[
                          |I|\ \ge\ \frac{h\,\lfloor (m-1)^2/4\rfloor}{2\binom m2}
                          \ =\ \frac{k}{8}-O(1)
                          \]
                          such that one of the following holds throughout \(I\):
                          
                          (i) \(x_i\in V(R_a)\cap V(R_b)\) for every \(i\in I\), and \(\phi(x_i)\ge\lceil p/2\rceil\);
                          
                          (ii) \(u_i\in V(R_a)\cap V(R_b)\) for every \(i\in I\), and \(\phi(u_i)\ge p\). In this case
                          \[
                          e_i\cap V(R_a)=e_i\cap V(R_b)=\{u_i\}.
                          \]
                          Consequently, on each of \(R_a,R_b\), the first path edge containing \(u_i\) has index at most \(q_i-2\).
                          
                          Moreover, writing \(y_i=x_i\) in case (i) and \(y_i=u_i\) in case (ii), for any maximum endpoint path \(P_i\) ending at \(y_i\), each pair \(R_a,P_i\) and \(R_b,P_i\) contains a clean balanced elementary endpoint lens ending at \(y_i\). In case (i) one may take \(P_i=R_i\).

                      • [1001127] Same-type distinguished overlap gives two lens-free repeated-intersection certificates per label
                          STATEMENT
                          Let H be a finite linear 3-graph. Let v be a vertex with phi(v)=p, and let
                            e_i={x_i,v,u_i}, i=1,...,k,
                          be distinct ascending nonspecial edges terminal at v, where x_i is the unique entrance of e_i. Assume v has minimum vertex rank among the two terminal vertices of every e_i, so phi(u_i)>=p. Order the edges by
                            q_1<=...<=q_k,   q_i=phi(e_i),
                          and choose a canonical maximum source rail R_i of length q_i-1 ending at x_i.
                          
                          Put h=floor(k/2) and m=k-h. If k>=4, then there exist a,b>h and a set I subset {1,...,h} with
                            |I| >= h*floor((m-1)^2/4)/(2*C(m,2)) = k/8-O(1)
                          such that one of the following holds throughout I:
                          
                          (X) x_i belongs to V(R_a) intersect V(R_b) for every i in I, and phi(x_i)=q_i-1>=ceil(p/2);
                          
                          (U) u_i belongs to V(R_a) intersect V(R_b) for every i in I, phi(u_i)>=p, and x_i is absent from V(R_a) union V(R_b). Hence
                            e_i intersect V(R_a)=e_i intersect V(R_b)={u_i},
                          and the first path-edge of each of R_a,R_b containing u_i has index at most q_i-2.
                          
                          Moreover, write y_i=x_i in case (X) and y_i=u_i in case (U). For every i in I and every maximum endpoint path P_i ending at y_i,
                            |V(P_i) intersect V(R_a)|>=2
                          and
                            |V(P_i) intersect V(R_b)|>=2.
                          In case (X) one may take P_i=R_i.
                          
                          Thus a common-minimum-terminal family of k ascending edges forces two higher-rank source rails and k/8-O(1) same-type labels, each label carrying two lens-free repeated-intersection certificates.

                        • [1000064] A clean joint-to-joint detour cannot shortcut a maximum host path
                            STATEMENT
                            Let A=(g_1,...,g_L) be a maximum endpoint path ending at a. Let z and u be distinct internal joints of A, with
                              z=g_s intersect g_{s+1},
                              u=g_t intersect g_{t+1}.
                            Let B be a linear path from z to u such that
                              V(B) intersect V(A)={z,u}.
                            Then
                              |E(B)|<=|s-t|.
                            Thus a clean detour between two host joints cannot use fewer edges than the corresponding interval of a maximum host path.

                        • [1000147] A same-type overlap packet forces many cycle-bearing labels or many common last edges
                            STATEMENT
                            Retain f84b001e0a61. Thus there are indices a,b and a set I of size M, together with one fixed type X or U, such that for every i in I a label y_i lies on both maximum source paths R_a,R_b, where
                              y_i=x_i in type X,
                              y_i=u_i in type U,
                            and every maximum endpoint path P_i ending at y_i has at least two common vertices with each of R_a,R_b.
                            
                            Choose one such maximum endpoint path P_i for every i, and let h_i be its last edge. Then for every i in I at least one of the following holds:
                            
                            (1) P_i union R_a contains a linear cycle;
                            
                            (2) P_i union R_b contains a linear cycle;
                            
                            (3) h_i belongs to E(R_a) intersect E(R_b).
                            
                            If C is the number of indices i for which (1) or (2) holds, then
                              |E(R_a) intersect E(R_b)| >= (M-C)/3.
                            
                            Hence either at least M/2 labels are cycle-bearing with one of the two hosts, or
                              |E(R_a) intersect E(R_b)| >= M/6.
                            
                            In type U, every edge h_i arising from alternative (3) has edge rank at least p. Consequently the second outcome strengthens to: R_a and R_b share at least M/6 distinct hyperedges of edge rank at least p.

                          • [1000000] A higher-rank internal edge on a maximum endpoint path forces a suffix return unless the path leaves through its unique entrance
                              STATEMENT
                              Let
                                R=(g_1,...,g_L)
                              be a maximum endpoint path with last vertex x, so phi(x)=L. Let h=g_j be an internal edge of R, with j<L and edge rank
                                r=phi(h)>L.
                              Put
                                z=g_j intersect g_{j+1},
                              the path joint through which R leaves h toward x.
                              
                              If z is terminal at h, then every maximum r-edge path Q with last edge h and last vertex z has a common vertex with the suffix
                                g_{j+1},...,g_L
                              other than z.
                              
                              Consequently:
                              
                              (a) if h is special, this suffix return is forced;
                              
                              (b) if h is nonspecial with unique entrance y, the suffix return is forced unless z=y.
                              
                              Thus a higher-rank internal edge can avoid a forced return into the remaining suffix only when it is nonspecial and the host path leaves h through its unique entrance.

                            • [1000463] An internal edge above the endpoint-path rank propagates forward with loss at most one or creates a cycle
                                STATEMENT
                                Let
                                  A=(g_1,...,g_L)
                                be a maximum endpoint path with last vertex a, so phi(a)=L. Let h=g_j be an internal edge, j<L, with edge rank
                                  r=phi(h)>L.
                                
                                Then at least one of the following holds:
                                
                                (C) the union of A with a suitable maximum endpoint path contains a linear cycle;
                                
                                (P) there is an index t>j such that
                                  phi(g_t)>=r-1.
                                
                                Consequently, if no linear cycle occurs in the successive applications of this alternative starting from h, then
                                  j <= 2L+1-r.
                                
                                Equivalently, every internal path edge with
                                  j>2L+1-phi(g_j)
                                forces a linear cycle through the propagation process.

                              • [1001091] Shared edges above the host-path rank are confined to an initial prefix unless a cycle occurs
                                  STATEMENT
                                  Let
                                    A=(a_1,...,a_{q-1})
                                  be a maximum endpoint path with last vertex x, where q<p. Let H be a set of T distinct hyperedges belonging to A, each of edge rank at least p.
                                  
                                  Then at least one of the following holds:
                                  
                                  (1) in the propagation process of 678901b48360 for some h in H, the union of A with a suitable maximum endpoint path contains a linear cycle;
                                  
                                  (2) every h in H occurs among
                                    a_1,...,a_{2q-p-1},
                                  and consequently
                                    T <= max{0,2q-p-1}.
                                  
                                  In particular, if no such cycle occurs and T>0, then
                                    q >= ceil((p+T+1)/2).
                                  
                                  Applied to the type-U common-edge outcome of 20cdd04e92ca, if one of the two higher-rank source paths has edge rank q, then either a cycle is produced or the number T of distinct common hyperedges of edge rank at least p satisfies
                                    T<=2q-p-1.

                            • [1000997] Many common higher-rank edges force cycle-bearing edges or common unique-entrance traversal
                                STATEMENT
                                Let A and B be maximum endpoint paths of lengths L_A,L_B, and let p>max{L_A,L_B}. Let H be a set of T distinct hyperedges such that every h in H belongs to both A and B and has edge rank at least p.
                                
                                Discard the at most two members of H that are the last edge of A or the last edge of B. For every remaining h, at least one of the following holds:
                                
                                (C) h lies on a linear cycle;
                                
                                (E) h is nonspecial and both A and B leave h toward their respective last vertices through the unique entrance of h.
                                
                                Consequently at least one of the following holds:
                                
                                (1) at least (T-2)/2 distinct edges of H lie on linear cycles;
                                
                                (2) at least (T-2)/2 distinct edges of H satisfy (E).
                                
                                Applied to the type-U non-cycle outcome of 20cdd04e92ca, where T>=M/6, this gives either at least M/12-1 distinct common edges lying on linear cycles, or at least M/12-1 common nonspecial edges that both higher-rank source paths leave through their unique entrances.

                              • [1001033] Cycle-free common unique-entrance edges form one consistently oriented block
                                  STATEMENT
                                  Let
                                    A=(a_1,...,a_L),  B=(b_1,...,b_M)
                                  be linear paths in a linear 3-graph, oriented toward their last vertices. Assume A union B contains no linear cycle.
                                  
                                  Then the full common-edge set
                                    E(A) intersect E(B)
                                  is a contiguous edge block in each path.
                                  
                                  Suppose this common block contains an edge h that is internal to both A and B, is nonspecial, and has the following property: if y is the unique entrance of h, then the edge immediately after h on A meets h at y, and the edge immediately after h on B also meets h at y.
                                  
                                  Then, provided the common block has at least two edges, the common block occurs in the same order in the two oriented paths.

                        • [1000076] A shared-entrance packet forces the lower-half edge ranks upward
                            STATEMENT
                            Retain the X-branch of f84b001e0a61. Thus
                              e_i={x_i,v,u_i}, i=1,...,k,
                            have edge ranks
                              q_1<=...<=q_k,
                            put h=floor(k/2), and there are indices a,b>h and a set
                              I subset {1,...,h}
                            of size M such that every x_i, i in I, belongs to both canonical source paths R_a,R_b.
                            
                            Fix one host index a. If q_h<q_a, then
                              M <= 4q_h-2q_a-1.
                            Equivalently,
                              q_h >= ceil((2q_a+M+1)/4).
                            
                            In particular, since q_a>=q_{h+1}, any strict median rank jump q_h<q_{h+1} satisfies
                              M <= 4q_h-2q_{h+1}-1.
                            Thus a linear shared-entrance packet is incompatible with a large rank gap between the lower half of the family and its higher host paths.

                      • [1000301] A repeated endpoint-on-path intersection gives a linear cycle or a shared last edge
                          STATEMENT
                          Let A and P be linear paths in a linear hypergraph, and let u be the last vertex of P. Assume u belongs to V(A), and P and A have at least one common vertex besides u.
                          
                          Then at least one of the following holds:
                          
                          (1) the last edge of P is also an edge of A;
                          
                          (2) A union P contains a linear cycle.
                          
                          More precisely, let z be the last common vertex encountered before u when P is oriented toward its last vertex u. If the last edge of P is not an edge of A, then the P-segment from z to u and the A-segment between z and u are internally vertex-disjoint and edge-disjoint, and their union is a linear cycle.

                        • [1000364] Endpoint-retaining repeated intersections force a cycle or adjacent source-path last-edge containment
                            STATEMENT
                            Let x_i=v_j be an interior color-terminal collision on a simple rainbow terminal-pair path, and let R_i,R_j,R_{j+1} be the chosen maximum source paths ending at x_i,x_j,x_{j+1}. Assume
                              x_j in V(R_i),
                              x_{j+1} in V(R_i),
                            and
                              |V(R_i) intersect V(R_j)|>=2,
                              |V(R_i) intersect V(R_{j+1})|>=2.
                            Let h_j and h_{j+1} be the last edges of R_j and R_{j+1}.
                            
                            For each s in {j,j+1}, either R_i union R_s contains a linear cycle, or h_s belongs to E(R_i).
                            
                            Consequently, if neither union contains a linear cycle, then R_i contains both h_j and h_{j+1}. If in addition there is no linear 3-cycle consisting of E_j,E_{j+1} and one edge of R_i, then h_j!=h_{j+1}.

                      • [1000843] A non-endpoint vertex on a maximum endpoint path forces a second intersection with its own maximum endpoint path
                          STATEMENT
                          Let Q be a maximum endpoint path with last vertex x, and let y be a vertex of Q with y!=x. Let P_y be any maximum endpoint path with last vertex y.
                          
                          Then
                            |V(Q) intersect V(P_y)|>=2.

                        • [1001100] Interior U_11 color-terminal collisions force a linear-size matching of repeated endpoint-path intersections
                            STATEMENT
                            Let v_0v_1...v_k be a simple rainbow terminal-pair path whose parent hyperedges E_s={x_s,v_{s-1},v_s} belong to U_11. Let P_w denote the globally chosen maximum endpoint path with last vertex w, and write R_i=P_{x_i}.
                            
                            Let M be any family of interior color-terminal collisions x_i=v_j. For each collision, choose one adjacent parent edge F_i in {E_j,E_{j+1}} that is not the last edge of R_i; such a choice always exists. Let c_i be its unique off-x_i contact with R_i. Then
                              F_i intersect V(R_i)={x_i,c_i},
                            and
                              |V(P_{x_i}) intersect V(P_{c_i})|>=2.
                            
                            The M pairs {x_i,c_i} form a loopless multigraph of maximum degree at most seven. Consequently there is a subfamily of at least
                              ceil(M/13)
                            collisions for which the endpoint pairs {x_i,c_i} are pairwise disjoint.
                            
                            Hence M interior U_11 color-terminal collisions force at least ceil(M/13) endpoint-disjoint pairs of chosen maximum endpoint paths, each pair having at least two common vertices. No edge-rank monotonicity is required.

                  • [1000774] The q,(q+1)^3 equality pattern forces tail-terminal or cross-splice obstructions
                      STATEMENT
                      Let e_1 have rank q and e_2,e_4 rank q+1, all potential-charged ascending nonspecial edges at common terminal v. Relative to any longest e_4-path and canonical entrance rail for e_1, either the entrance x_2 is absent and the opposite terminal u_2 lies in the final q-1 precursor tail, or x_2 is present and the natural low-rail/high-tail splice is necessarily cross-blocked. In particular, in a q,(q+1)^3 obstruction, each of the two nonchosen high competitors satisfies one of these two explicit obstruction modes against any chosen high edge.

                    • [1000792] Every high competitor in the q,(q+1)^3 pattern has a private-singleton, joint, or two-vertex contact with the low entrance rail
                        STATEMENT
                        Let e={x,v,u} be ascending nonspecial of rank q, with unique entrance x and terminal v, and let R=(r_1,...,r_{q-1}) be a canonical entrance path ending at x and avoiding v,u. Let h={y,v,z} be a distinct ascending nonspecial edge of rank q+1 through the same terminal v. Then h meets R and cannot contain x or u. Writing mu_R(h) for the number of rail edges met by h, exactly one of the following holds:
                        - mu_R(h)=1, and the unique contact is private in r_j for j in {2,...,q-3} union {q-1};
                        - h has exactly one vertex on R, that vertex is a joint r_i∩r_{i+1}, and hence mu_R(h)>=2;
                        - both non-v vertices y,z lie on R, and no rail edge contains both.
                        The final-edge private-singleton residue j=q-1 remains open.

                    • [1000879] Clean single contacts avoid the first and penultimate rail edges
                        STATEMENT
                        Let e={x,v,u} be ascending nonspecial of rank q with canonical entrance rail R=(r_1,...,r_{q-1}). If a distinct edge through the same terminal meets R in exactly one private contact on r_j, then j≠1 and j≠q-2; moreover no two such occupied positions differ by two. The previously claimed exclusion of j=q-1 is not justified by the available splice, so that last-edge case remains open.

                      • [1001088] A later terminal-only contact is bounded from the right by the earlier edge rank
                          STATEMENT
                          Let P=(g_1,...,g_p) be a maximum path ending at v. Let e,f be ascending nonspecial terminal-only single-contact edges through v with entrances absent from P. If the last occurrence index of e's terminal contact is smaller than that of f's, then the later contact satisfies l_f>=p-phi(e)+3. This is the reversed-coordinate companion to df8ad4c65be0.

              • [1000924] At the half-rank boundary the low-rank entrance is universally the central joint
                  STATEMENT
                  Let v have phi(v)=2q-2 and let
                    e={x,v,u}
                  be a potential-charged ascending nonspecial edge of rank q with v terminal. Then for every maximum (2q-2)-edge path
                    P=(g_1,...,g_{2q-2})
                  ending physically at v,
                    x=g_{q-1}∩g_q.
                  
                  In particular the opposite-terminal witness alternative in 351720508b02 never occurs.

            • [1000284] REFUTED route: top-boundary mutual-blocking rails
                STATEMENT
                Refuted as a general-q lemma. The construction incorrectly assumed that a rank-(q+1) edge f_j can terminate a maximum phi(v)=2q-2 edge path at v. For q>3, q+1<2q-2, so such a path cannot exist. The argument is valid only in the base case q=3 and must not be used in the general two-rank block.

            • [1000430] Every one-rank-higher charged competitor blocks the low entrance rail
                STATEMENT
                Let e={x,v,u} be an ascending nonspecial edge of rank q with unique entrance x and terminal v. Let
                  R=(r_1,...,r_{q-1})
                be a canonical entrance path ending physically at x and avoiding v,u.
                
                Let h={y,v,z} be a distinct ascending nonspecial edge of rank q+1 for which v is a terminal. Then
                  h∩V(R) is nonempty.
                
                More precisely, h cannot contain x, so every R-contact of h lies in {y,z}. Hence h has either one or two R-contact vertices.

            • [1000450] Any four-edge counterexample with occupied upper consecutive rank lies below the odd central threshold
                STATEMENT
                Fix v with p=phi(v), and suppose four potential-charged ascending nonspecial edges are terminal at v, all with ranks in {q,q+1}, and at least one has rank q+1. Then
                  q+1 <= p <= 2q-2.
                Moreover:
                (i) if p=2q-2, at most one of the four edges has rank q, and every rank-q edge among them has opposite terminal u with phi(u)=p;
                (ii) if p=2q-3, at most two of the four edges have rank q.
                Thus at p=2q-2 the only possible ordered rank patterns are
                  (q,q+1,q+1,q+1) and (q+1,q+1,q+1,q+1),
                while at p=2q-3 at least two edges have rank q+1.
                The all-rank-q case is handled only after reindexing q as the occupied upper level; it is not covered by the displayed hypothesis with the original q.

          • [1000290] Recovered Astra 11/12 architecture: charged three-quarters bound via consecutive rank pairs
              STATEMENT
              The interrupted Astra route is best reconstructed as follows.
              
              For v put p=phi(v), and let c_+(v) count ascending nonspecial edges e={x,v,u} for which v is terminal and phi(u)>=p.
              
              TARGET LOCAL BOUND:
                c_+(v) <= floor(3p/4).
              
              Every ascending edge can be assigned to a terminal of minimum endpoint potential, so it is counted by c_+ at its assigned terminal. Hence
                A <= sum_v c_+(v) <= (3/4) sum_v phi(v).
              
              Combining with certified ascending accounting
                3m-A <= 2 sum_v phi(v)-n
              gives
                m <= (11/12) sum_v phi(v)-n/3.
              For a P_ell-free system:
                m <= ((11ell-15)/12)n.
              
              A sufficient local lemma is the consecutive-rank block:
                for every v and q, at most three charged ascending terminal edges at v have ranks in {q,q+1}.
              The charged rank floor and rank-pair arithmetic then give the exact floor(3p/4) bound, with odd-central-window capacities supplying the residue corrections.
              
              The screenshots' clean-nearby-contact mechanism is rigorously represented by 990186a1aaa6, 08f894b8cb5e, and eac2e3da3eea: appropriate clean contacts in nearby rail/path positions splice to a path too long for an ascending entrance. This mechanism crucially uses clean/entrance structure and does not invoke the false arbitrary consecutive-single-blocker claim.
              
              The remaining gap is to prove the consecutive-rank block or an equivalent global charge. A four-edge counterexample is already confined to q+1<=p<=2q-2. At p=2q-2 in the mixed q,(q+1)^3 pattern, the rank-q entrance is universally the central joint on every maximum p-path. Relative to its canonical entrance rail, every high competitor is either a strict-interior clean singleton chord or a two-contact chord; singleton contacts two positions apart are forbidden. Relative to a chosen high-edge witness, every other high competitor is additionally tail-terminal or cross-splice-blocked.

        • [1000454] Quantitative separation between an earlier single blocker and a later clean entrance
            STATEMENT
            Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, with last edge h=g_p. Let e and f be distinct ascending nonspecial edges through v, neither equal h. Assume e has exactly one contact vertex r in V(P)\h, and let j be the first path-edge index containing r.
            
            Assume f also has exactly one contact vertex on P, namely its unique entrance y.
            
            (a) If y is private to g_k and k>=j+2, then
              k-j >= p-phi(f)+3.
            
            (b) If y=g_k∩g_{k+1} is a joint and k>=j+1, then
              k-j >= p-phi(f)+2.

        • [1000864] Distance-two private clean entrance contacts are incompatible
            STATEMENT
            Let P=(g_1,...,g_p) be a maximum p-edge linear path ending at v, with last edge h=g_p. Let e={x,v,u} and f={y,v,z} be distinct ascending nonspecial edges, neither equal to h. Assume:
            - e meets V(P)\h in exactly one vertex, namely its entrance x;
            - f meets V(P)\h in exactly one vertex, namely its entrance y;
            - x is private to g_j and y is private to g_{j+2}, for some 1<=j<=p-3.
            
            Then this configuration is impossible.

          • [1000053] Clean entrance-only ascending terminal chords satisfy three-halves packing
              STATEMENT
              Let P=(g_1,...,g_p) be a maximum p-edge linear path ending at v, with h=g_p. Let X(P,v) be the family of ascending nonspecial edges e={x,v,u}, e!=h, such that e meets V(P)\V(h) in exactly one vertex and that vertex is its unique entrance x.
              
              Let alpha_p be the maximum weight of an independent set in the distance-two graph on indices {1,...,p-1}, with weight 2 at index 1 and weight 1 elsewhere; for p=1 this graph is empty and alpha_1=0. Then
                |X(P,v)| <= p-2 + alpha_p <= floor(3p/2)
              for p>=2, while X(P,v)=emptyset for p=1.
              
              For p>=2,
                alpha_p =
                  p/2+1       if p≡0 mod4,
                  (p+1)/2     if p≡1 mod4,
                  p/2+1       if p≡2 mod4,
                  (p+3)/2     if p≡3 mod4.
              In particular |X(P,v)|<=floor(3p/2), with a one-unit stronger bound when p is even.

            • [1001003] An earlier terminal-only contact is bounded by the later edge rank
                STATEMENT
                Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, with h=g_p. Let e={x,v,u} and f={y,v,z} be distinct ascending nonspecial edges, neither equal h, such that relative to V(P)\V(h), e has exactly one contact u (its opposite terminal) with x absent, and f has exactly one contact z with y absent. Let j be the first path-edge index containing u and k the first path-edge index containing z, with j<k. If q_f=phi(f), then
                  j <= q_f-3.
                
                The reversed-path analogue is valid when formulated using the last occurrence index of the earlier/later terminal contact; no unconditional first-index reciprocal inequality is asserted.

              • [1000833] Consecutive terminal-only singleton ranks sum to at least the host potential plus four
                  STATEMENT
                  Let P=(g_1,...,g_p) be a maximum p-edge path ending at v. Let e,f be distinct ascending nonspecial edges terminal at v, each having exactly one off-v contact with P, and suppose in both cases that contact is the opposite terminal while the unique entrance is absent from P. If the contact of e occurs before the contact of f along P, and r_e=phi(e), r_f=phi(f), then r_e+r_f>=p+4. Consequently, among terminal-only singleton edges of rank at most q, at most one can occur whenever p>=2q-3.

                • [1000195] Terminal-only singleton ranks two positions apart sum to at least the host potential plus five
                    STATEMENT
                    Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, and let e_1,e_2,e_3 be three ascending nonspecial terminal-only singleton edges through v whose unique contacts occur in this order along P. Write r_i=phi(e_i). Then r_1+r_3>=p+5. Consequently, if all three ranks are at most q, three terminal-only singleton contacts require p<=2q-5.

              • [1000878] Separated terminal-only contact intervals are squeezed from both ends
                  STATEMENT
                  In the setting of df8ad4c65be0, let I_e and I_f be the sets of path-edge indices containing the sole terminal contacts u and z, respectively. Thus each I is either {j} or {j,j+1}. Assume
                    max I_e < min I_f.
                  Write
                    a=min I_e,  b=max I_f,
                  and q_e=phi(e), q_f=phi(f).
                  Then
                    a <= q_f-3
                  and
                    b >= p-q_e+3.

          • [1000190] Clean entrance-only ascending terminal chords satisfy the three-halves path-slot bound
              STATEMENT
              Let P=(g_1,...,g_p) be a maximum p-edge linear path ending physically at v, with last edge h=g_p. Let X(P,v) be the set of ascending nonspecial edges e={x,v,u}, e!=h, for which v is a terminal and
                e∩(V(P)\h)={x},
              where x is the unique entrance of e.
              
              Then
                |X(P,v)| <= floor(3p/2).
              
              More precisely, at most p-2 members of X(P,v) have entrance at a path joint outside h, while at most ceil(p/2)+1 have entrance in a path-private slot.

        • [1001054] A clean joint entrance forbids the immediately preceding first-contact cell
            STATEMENT
            Let P=(g_1,...,g_p) be a maximum p-edge path ending at v with last vertex v, with h=g_p. Let e and f be distinct ascending nonspecial edges through v, neither equal h.
            
            Assume e has exactly one contact vertex r in V(P)\\h, and let j be the first path-edge index containing r. Assume f has exactly one contact vertex y in V(P)\\h, that y is the unique entrance of f, and that y is the joint g_{j+1}∩g_{j+2}. Then this configuration is impossible.

      • [1000269] Chosen maximum endpoint paths give global double-blocker compensation
          STATEMENT
          Let H be an n-vertex P_ell^(3)-free linear 3-graph with m edges, snake digraph D, and s special edges. For each vertex v choose a maximum phi(v)-edge path P_v ending at v, and let h_v be its last edge. Let B_v be the number of snake-incoming incidences (f,v) with f!=h_v such that both vertices of f minus {v} lie in V(P_v) minus h_v. Put B=sum_v B_v. Then d_D^-(v)+B_v<=2phi(v)-1 for every v, and consequently 2m+s+B <= (2ell-3)n.

      • [1000952] Cumulative snake-rank indegree bound
          STATEMENT
          Let G be a linear r-uniform hypergraph with snake digraph D. Fix v and q>=1, and let I_q(v)={e : (e,v) is an incoming snake incidence and phi(e,v)<=q}. Then |I_q(v)| <= (q-1)(r-1)+1. In particular, for r=3, |I_q(v)|<=2q-1.

      • [1000322] Defect-stability route to the two-thirds Turan upper bound
          STATEMENT
          For a globally longest L-edge path P ending in a maximum-rank nonspecial edge e={x,y,z}, terminal blocker defects measure exactly the deviation from the saturated punctured-Steiner regime: for each terminal v in {y,z},
          U_v-S_v=2(L-d_H(v)),
          where S_v is the number of single blockers and U_v the number of precursor vertices unused by the v-star. Consequently, in a minimum-degree-delta graph,
          U_v-S_v<=2(L-delta).
          This suggests a general 2/3 strategy: a nonspecial edge above the threshold 3delta>2L+2 must lie either in a rotation-rich regime with many open blocker defects, or in a near-saturated regime close to the punctured-Steiner one/two-chain topology.

        • [1000120] Lexicographically maximal fixed-edge paths push rotations onto maximum-potential private vertices
            STATEMENT
            Let H have global maximum path length L and let e be a nonspecial edge of rank L with unique entrance x. Among all globally longest L-edge paths ending in e through x, choose P lexicographically maximizing the sorted multiset of endpoint potentials of the private vertices of its path edges. Suppose a safe opposite-end single-blocker rotation replaces one path edge g_j by an external edge f and thereby imports an outside vertex o while ejecting the private vertex p_j of g_j. Then phi(o)=phi(p_j)=L.

        • [1000133] Threshold-degree vertices cover every off-witness edge in an edge-minimal counterexample
            STATEMENT
            Fix ell>=4 and put k=floor(2ell/3)+1, the least integer strictly larger than 2ell/3. Suppose H is a P_ell-free linear 3-graph with minimum degree at least k and containing a nonspecial edge, chosen edge-minimal among such counterexamples (after any desired vertex-minimal choice). Then delta(H)=k. Moreover, for every nonspecial edge e and every phi(e)-edge witness path P ending in e, every edge f not belonging to P contains a vertex of degree exactly k. Equivalently, the set D={v:d_H(v)=k} is a vertex cover of E(H)\E(P) for every nonspecial witness path P.

          • [1000566] High-degree-only edges form a universal core of all nonspecial witness paths
              STATEMENT
              In the setting of 1e01357bf9c3, let D={v:d_H(v)=k}, where k=floor(2ell/3)+1, and let C={f in E(H): f∩D=∅}. Then for every nonspecial edge e and every longest witness path P ending in e, one has C⊆E(P). Hence every edge of C lies in the intersection of all longest witness paths for every nonspecial edge. In particular, if P and P' are two longest witness paths for the same nonspecial edge and a rotation or splice passes from P to P' by omitting an edge g of P, then g meets D.

            • [1001190] Threshold-deletion continuation
                STATEMENT
                Route bridge: the threshold-degree deletion analysis continues after toolkit lemma 1000228.

              • [1000411] At least one third of a minimal counterexample lies at threshold degree
                  STATEMENT
                  In the setting of 324fa959c567, write X=V(H)\D. Then (k-1)|X|<=2k|D|. Consequently |D|>=(k-1)|V(H)|/(3k-1). Thus at least an asymptotic one-third fraction of the vertices of any edge-minimal dense-core counterexample have degree exactly k=floor(2ell/3)+1.

              • [1000529] Conditional threshold-set deletion endgame under simultaneous Turan excess
                  STATEMENT
                  Let ell>=4, put k=floor(2ell/3)+1, and let H be a P_ell-free linear 3-graph which simultaneously satisfies: (i) the threshold-core conclusions of 1e01357bf9c3 for D={v:d_H(v)=k}, and (ii) the sharp Turan excess |E(H)|>(k-1)|V(H)|. For i=1,2,3 let m_i be the number of edges containing exactly i vertices of D. If m_2+2m_3>=|D|, then deleting D is compatible with the sharp Turan induction at coefficient k-1. Hence under these simultaneous hypotheses one must have m_2+2m_3<=|D|-1.

              • [1001072] A nonregular minimal counterexample has at least k threshold-degree vertices
                  STATEMENT
                  In an edge-minimal counterexample at threshold k=floor(2ell/3)+1, let D be the degree-k vertices. If V(H)\D is nonempty, then |D|>=k. Indeed every higher-degree vertex has at least k-1 cross-edges into D, which hit distinct D-vertices by linearity; equality |D|=k-1 would force every vertex of the path forest H-D to have degree two, impossible. If |D|=k, then H-D has no isolated vertices, every path endpoint has degree k+1 and its k cross-edges hit every vertex of D.

                • [1000862] Extremal threshold-set size yields a color-complete path-forest lift
                    STATEMENT
                    Assume the setting of ee2c9575cf8f with |D|=k, and put X=V(H)\D. Let P be the set of vertices of forest-degree one in H[X]. For every x∈P, d_H(x)=k+1 and for every d∈D there is a unique hyperedge {x,d,y_d} with y_d∈X. These k edges are all the edges through x meeting D, each contains exactly one D-vertex, and the vertices y_d are pairwise distinct. Consequently, if G is the simple graph on X in which xy is colored d whenever {d,x,y}∈E(H), then G is properly edge-colored by D and every x∈P has degree and color-degree exactly k, seeing every color once. Equivalently, for each d∈D the d-colored edges form a matching on X that saturates P.

                  • [1000094] Color-complete critical cores satisfy m plus 2c at most 2k
                      STATEMENT
                      In the extremal |D|=k color-complete path-forest normal form, if H-D has m edges and c nonempty path components, then m+2c<=2k. If m+2c=2k, every edge incident with every d in D is a DXX connector pairing two forest-private vertices. If m+2c=2k-1, every d-edge is again DXX, with exactly one joint endpoint among the k matching edges.

                    • [1000082] Zero-slack critical cores collapse to a one-factorized graph plus disjoint triples
                        STATEMENT
                        In the extremal |D|=k color-complete critical-core normal form, the zero-slack case m+2c=2k forces H-D to be a matching of single hyperedges. In particular every forest component has length one, m=c, and 3c=2k. Moreover the DXX color graph G on X has |X|=2k vertices, is k-regular, and its k colors are perfect matchings (a 1-factorization of G).

                      • [1000183] Rainbow connector paths through contracted forest triples double their length
                          STATEMENT
                          In the zero-slack critical-core model 13500728c22f, let F_1,...,F_c be the disjoint forest triples, c=2k/3, and let G be the k-regular properly k-edge-colored graph on X whose colored edge uv of color d represents the hyperedge {d,u,v}. Suppose there are distinct triple-indices i_1,...,i_s and G-edges C_j=u_jv_j, j=1,...,s-1, such that C_j joins F_{i_j} to F_{i_{j+1}}, the colors of the C_j are distinct, and for each internal triple F_{i_j} the two incident connector endpoints in that triple are distinct. Then
                          F_{i_1}, C_1^H, F_{i_2}, C_2^H,...,C_{s-1}^H,F_{i_s}
                          is a linear hypergraph path of length 2s-1, where C_j^H is the corresponding DXX hyperedge.

                      • [1000299] Zero-slack critical cores are at absolute near-spanning order
                          STATEMENT
                          In the zero-slack |D|=k critical-core model one has |V(H)|=3k. With k=floor(2ell/3)+1, this equals 2ell+3, 2ell+1, or 2ell+2 according as ell is 0,1,2 mod3. Thus the forbidden P_ell would omit exactly 2,0,1 vertices respectively. Zero slack is therefore a spanning/all-but-one/all-but-two path problem, not a diffuse asymptotic configuration.

                      • [1000323] The zero-slack contracted triple graph has a Hamilton path
                          STATEMENT
                          In the zero-slack critical-core model 13500728c22f, contract each forest triple F_i to one node and join two nodes in a simple graph R whenever at least one DXX connector joins their triples. Then every node of R has degree at least c/2, where c=2k/3 is the number of forest triples. Consequently R always has a Hamilton path. If c>=3, then R has a Hamilton cycle by Dirac's theorem.

                      • [1000346] Every pair of zero-slack triples has many same-color double jumps
                          STATEMENT
                          In the zero-slack |D|=k critical-core model, for every two distinct forest triples A,B, all but at most 12 threshold colors d admit two distinct d-colored matching edges e_A,e_B such that e_A leaves A away from B and e_B leaves B away from A. The lifted sequence A,h_A,h_B,B is then a four-edge linear path. Thus every pair of forest triples has at least k-12 legal same-color two-edge connector jumps.

                      • [1000824] Zero-slack nonspecial witnesses alternate exactly and all colored connectors are special
                          STATEMENT
                          In the zero-slack critical-core model 13500728c22f, every nonspecial witness path contains all c=2k/3 forest triples and therefore alternates exactly between forest triples and DXX connectors. Consequently every nonspecial edge is a forest triple, every DXX edge is special, and every nonspecial edge has rank exactly
                          q=2c-1=4k/3-1.

                        • [1000319] Failure of an uncolored entrance switch forces an exact half-neighborhood partition
                            STATEMENT
                            In the zero-slack alternating witness
                            T_1,C_1,...,C_{c-1},T_c=e,
                            fix an alternate terminal port y∈e. Let
                            A_y={j∈{1,...,c-1}: some DXX connector joins y to T_j}
                            and
                            B={j∈{2,...,c-1}: some DXX connector joins T_{j-1} to T_{c-1}}.
                            Then |A_y|>=c/2 and |B|>=c/2-1. Hence either A_y∩B is nonempty, supplying the two contracted adjacencies required by the entrance-switch lemma 767380617163, or else:
                            |A_y|=c/2, |B|=c/2-1,
                            A_y and B partition {1,...,c-1},
                            every triple T_j with j∈A_y contains exactly three neighbors of y in the DXX graph,
                            and the contracted degree of T_{c-1} is exactly c/2.

                          • [1001201] Rigid zero-slack half-neighborhoods expose a usable fixed-target cut
                              STATEMENT
                              In the zero-slack alternating witness T_1,C_1,...,C_{c-1},T_c=e={x,y,z}, suppose both alternate ports y,z fail the initial uncolored two-switch. Then they have the same complete half-neighborhood A of size c/2 among the forest triples, and no neighbors in the complementary index set B.
                              
                              In this rigid branch, an alternate port such as y has an unused-color safe connector into some T_i with i in A. Moreover there exists i in A, 1<=i<=c-2, such that the contracted graph also contains an edge T_1T_{i+1}. Thus some cut simultaneously has the target adjacency y-T_i and the return adjacency T_{i+1}-T_1 needed for the fixed-target 2-opt exchange; only color compatibility and the bounded unsafe ports remain.

                          • [1001213] Odd zero-slack rigidity forces a transverse connector or a common target neighborhood
                              STATEMENT
                              If both alternate terminal ports fail the zero-slack two-switch, they share one exact half-neighborhood S and induce a fixed-point-free color derangement there. Each threshold-color perfect matching has a cut-parity law across (S,X\S): the number of crossing matching edges is congruent to k modulo two and at least two. When k is odd, every color supplies a third crossing beyond the y- and z-edges. Therefore either some DXX edge joins S to the B-side, or every color matches x into S, forcing N_G(x)=N_G(y)=N_G(z)=S.

                            • [1000073] Odd-k rigid zero-slack no-switch state must contain an A-to-B connector
                                STATEMENT
                                In the rigid zero-slack no-switch normal form fb4fc1ee4179 with odd k, let A,B partition {1,...,c-1} as in 4468081d47b0 and let S be the union of the triples T_j with j∈A. Then the DXX graph contains an edge joining S to the union B_X of the triples indexed by B.

                            • [1000179] Odd-k rigid zero-slack branch must contain an S-to-B connector
                                STATEMENT
                                In the odd-k rigid zero-slack no-switch setting of 6894769a092f, alternative (B) is impossible. Hence alternative (A) must hold: there is a DXX edge joining S to B_X.

                              • [1000208] Rigid zero-slack cross-half edges match the entrance half-deficit
                                  STATEMENT
                                  In the rigid zero-slack half-neighborhood setting with S=N_G(y)=N_G(z), let e={x,y,z}, |S|=k, X=S disjoint-union B_X disjoint-union e, and put t=|N_G(x)∩S|. Then x has exactly k-t neighbors in B_X, and the number of DXX graph edges joining S to B_X is at least k-t.

                        • [1000528] A two-chord block reversal switches the entrance of a zero-slack witness
                            STATEMENT
                            Let
                            T_1,C_1,T_2,C_2,...,C_{c-1},T_c
                            be an alternating zero-slack witness as in b93769ee6fab, with T_c=e and final entrance port x∈e. Fix another port y∈e. Suppose for some 2<=j<=c-1 there are DXX connectors h joining y to a vertex of T_j and g joining T_{j-1} to T_{c-1} such that:
                            (i) the connector colors in the sequence below are all distinct;
                            (ii) at T_j the h-port differs from the port used by C_j;
                            (iii) at T_{j-1} the g-port differs from the port used by C_{j-2} when j>2;
                            (iv) at T_{c-1} the g-port differs from the port used by C_{c-2}.
                            Then there is a maximum alternating witness ending in e through y.

                        • [1000766] Unused colors at a reachable endpoint avoid every outgoing forest port
                            STATEMENT
                            In a zero-slack maximum witness for a nonspecial forest triple, fix either opposite endpoint a and an unused connector color d. Unless the d-mate of a is one of the three vertices of the terminal triple e, that mate must be an incoming or private port of an internal forest triple; it cannot be an outgoing port. Consequently each opposite endpoint has at least c/2-2 distinct unused-color mates on incoming/private ports and none on outgoing ports.

                        • [1000962] Color-run accounting is the natural zero-slack near-spanning target
                            STATEMENT
                            In a zero-slack critical core, let a linear path P use:
                            - a forest-triple edges;
                            - b_1 threshold colors on exactly one DXX edge each;
                            - b_2 threshold colors on exactly two consecutive DXX edges each.
                            Assume no threshold color occurs in two separated places of P, as required by linearity. Then
                            |E(P)|=a+b_1+2b_2,
                            the number of D-vertices used by P is b_1+b_2,
                            and the number of X-vertices used is
                            2|E(P)|+1-(b_1+b_2).
                            In particular, if P uses all k threshold colors exactly once as color-runs, then
                            |E(P)|=k+a+b_2.
                            Thus constructing a forbidden P_ell with all colors used reduces to finding a color-run path with
                            a+b_2=ell-k.
                            For k=floor(2ell/3)+1, the required surplus ell-k is about k/2.

                        • [1000996] Fixed-target two-connector exchange switches the entrance in zero slack
                            STATEMENT
                            Work in the zero-slack critical-core model, and let
                            T_1,C_1,T_2,C_2,...,T_{c-1},C_{c-1},T_c=e
                            be a maximum alternating witness ending in the forest triple e through the port x=C_{c-1}∩e. Fix 1<=i<=c-2. Suppose there are DXX connectors f,g such that:
                            (1) f joins T_i to e at a port y∈e\{x};
                            (2) g joins T_{i+1} to T_1;
                            (3) at T_i the port of f is different from the port of C_{i-1} when i>1;
                            (4) at T_{i+1} the port of g is different from the port of C_{i+1} when i+1<c-1;
                            (5) at T_1 the port of g is different from the port of C_1;
                            (6) the colors of f and g are distinct and neither occurs among the retained connector colors
                            {col(C_1),...,col(C_{i-1}),col(C_{i+1}),...,col(C_{c-2})}.
                            Then there is a maximum alternating witness using all c forest triples and ending in e through y. In particular, if e is nonspecial with entrance x, no such pair f,g exists for either y∈e\{x} and any cut i.

                        • [1001103] Unused terminal colors are repelled from the penultimate triple of a zero-slack witness
                            STATEMENT
                            Let
                            T_1,C_1,...,T_{c-1},T_c=e
                            be a zero-slack maximum witness for a nonspecial forest triple e, entered through x, and let y be another vertex of e. Let p_in be the port of T_{c-1} used by C_{c-2}, p_out the port used by C_{c-1}, and p_free the third port. If d is a connector color unused by the witness and the d-colored edge from y has its other X-endpoint w in T_{c-1}, then nonspeciality forces w=p_in. In particular at most one unused-color y-edge can meet T_{c-1}. The same holds for the other terminal z.

                          • [1000590] Unused terminal colors are repelled from both ends of a zero-slack witness
                              STATEMENT
                              In the zero-slack witness of f3a692e51efb, let y be a terminal port different from the entrance x and let d be an unused connector color. If the d-colored edge {y,d,w} has w in the first forest triple T_1, then nonspeciality forces w to be the port of T_1 used by C_1. Hence at most one unused-color y-edge meets T_1. Together with f3a692e51efb, at most two unused-color y-edges meet T_1∪T_{c-1}; therefore at least k/3-1 of the k/3+1 unused-color y-edges have X-contact in the interior triples T_2,...,T_{c-2}.

                    • [1000251] One-slack critical cores have at most one forest joint
                        STATEMENT
                        Assume the extremal |D|=k color-complete critical-core normal form with one unit of slack,
                        m+2c=2k-1.
                        Let j=m-c be the number of forest joints. Then
                        j(k-2)<=k.
                        In particular, for k>=5 one has j<=1. Hence H-D consists of single-edge components, with at most one two-edge path component. More precisely 3c+j=2k-1 with j∈{0,1}.

                    • [1000254] Zero slack forces the universal path forest to be a matching
                        STATEMENT
                        In the |D|=k critical-core normal form, if m+2c=2k then H-D has no forest joints. Hence every component of H-D is a single edge, m=c, and 3c=2k. Thus zero slack can occur only when 3 divides k, and the core reduces to c=2k/3 disjoint X-triples together with k pairwise edge-disjoint perfect D-colored matchings on the 2k vertices of X.

                    • [1000302] Slack controls forest joints in the extremal critical core
                        STATEMENT
                        In the extremal |D|=k color-complete critical-core normal form, let
                        sigma=2k-(m+2c)>=0,
                        where m=|E(H-D)| and c is the number of nonempty forest components. For each color d∈D let J_d be the number of forest-joint endpoints among the d-colored DXX edges, and let T_d be the number of edges through d that are not DXX. Then
                        J_d+2T_d=sigma
                        for every d. Consequently, if j=m-c is the total number of forest joints, then
                        j(k-2)<=k sigma,
                        so
                        j<=k sigma/(k-2).
                        Thus for fixed small sigma and large k, all but O(sigma) components of H-D are single hyperedges.

                      • [1000229] Only constant effective slack can obstruct Hamiltonicity of the critical color graph
                          STATEMENT
                          In the extremal |D|=k critical-core normal form, let sigma=2k-(m+2c) and j=m-c be the private slack and number of forest joints. Then
                          |X|=2k-sigma+j.
                          The DXX color graph G on X satisfies delta(G)>=k-2. Consequently, if sigma-j>=4, then delta(G)>=|X|/2, so the underlying simple graph G is Hamiltonian by Dirac. Hence the only critical-core regime in which ordinary Hamiltonicity is not automatic satisfies sigma-j<=3.

                      • [1000988] Critical-core slack fixes forest-joint count modulo three
                          STATEMENT
                          In the extremal |D|=k critical core, with private slack sigma=2k-(m+2c) and joint count j=m-c, one has 3c+j=2k-sigma and hence j congruent to 2k-sigma mod 3. For sigma<=k-2, also 0<=j<=sigma. Thus every fixed small-slack layer has only finitely many forest templates; in particular sigma=0 requires 3|k and j=0, while sigma=1 is impossible for k=0 mod3 and otherwise forces j=1 or 0 according as k=1 or 2 mod3.

                    • [1000354] Zero-slack component partitions have rainbow cut expansion
                        STATEMENT
                        In the zero-slack |D|=k critical-core normal form, let a union A of forest components contain R forest-private vertices. The number of distinct D-colors on connectors crossing A to its complement is at least max{0,k-min(R,2k-R)+1}. Consequently every partition of the c forest components into t>=2 nonempty groups has at least k-floor(2k/t)+1>=t-1 distinct colors represented across the partition.

                    • [1000786] Zero-slack critical cores with at most two forest components are impossible in the good residues
                        STATEMENT
                        Assume the extremal |D|=k color-complete normal form and the zero-slack case m+2c=2k. If c=1, then H contains P_ell for every ell>=4. If c=2 and ell is congruent to 0 or 2 modulo 3, then H also contains P_ell. Hence no P_ell-free minimal counterexample in either good residue class can have |D|=k, zero slack, and at most two components in H-D.

                      • [1000152] Zero-slack two-component critical cores always have a free-end cross connector
                          STATEMENT
                          Assume the extremal |D|=k color-complete normal form and zero slack m+2c=2k. If c=2, then some colored connector joins a free end of one forest component to a private vertex of the other. Consequently, for ell congruent to 0 or 2 modulo 3, the c=2 zero-slack case is impossible in a P_ell-free counterexample.

                      • [1000314] Zero-slack two-component critical cores are impossible in the good residues
                          STATEMENT
                          In the zero-slack |D|=k critical-core setting m+2c=2k with c=2, some physical forest endpoint must have a colored connector into the other component. Consequently, for ell congruent to 0 or 2 modulo 3, the physical-bridge lemma yields P_ell and the case is impossible.

                    • [1001007] One unit of critical-core slack permits at most one forest joint
                        STATEMENT
                        In the |D|=k critical-core normal form, if m+2c=2k-1 then every threshold star is entirely DXX and has exactly one forest-joint endpoint. Hence the total D-to-joint incidence is k. Since every forest joint needs at least k-1 such incidences, there is at most one joint. Therefore H-D is either a matching, or a matching with exactly one two-edge path component.

                  • [1000482] The extremal critical-core color graph has minimum degree k minus two
                      STATEMENT
                      In the |D|=k critical-core normal form, let G on X=V(H)\D consist of all DXX edges, colored by their D-vertex. Then G is properly edge-colored, every forest-private vertex has color-degree k, and every forest joint has degree k, k-1, or k-2. Hence delta(G)>=k-2. Degree k-2 occurs only when a joint of total degree k+1 lies in exactly one DDX edge; otherwise a joint misses at most one D-color.

                  • [1000881] Every threshold color supplies many private-to-private forest connectors
                      STATEMENT
                      Assume the color-complete path-forest normal form c15cf7354428. Let F=H[X] have m edges and c nonempty path components. Then F has r=m+2c vertices of forest-degree one and j=m-c joint vertices of forest-degree two. For each color d in D, the d-colored matching on X saturates all r forest-degree-one vertices, and therefore contains at least ceil(3c/2) edges whose two endpoints both have forest-degree one.

                  • [1001025] Private-vertex slack bounds the number of forest joints
                      STATEMENT
                      In the |D|=k critical-core normal form, let sigma=2k-(m+2c), where m,c are the edge and component counts of the universal path forest F=H-D, and let J be its forest joints. Then (k-1)|J|<=k sigma. In particular, for 0<=sigma<=k-2 one has |J|<=sigma. Hence small private slack forces H-D to be a matching with only O(sigma) joints.

                  • [1001060] Free-end connector is either an inter-component bridge or a cycle-closing chord
                      STATEMENT
                      Assume the color-complete path-forest normal form c15cf7354428. Let C=(e_1,...,e_a) be a component of F=H[X], let x be a free last vertex of e_1, and let f={x,d,y} be the unique connector of color d through x. If y lies in a different forest component C' of length b, then H contains a linear path of length at least a+1+ceil(b/2). Hence P_ell-freeness forces a+ceil(b/2)<=ell-2. If y lies in C itself and j is the first path-edge index containing y, then j>=2 and e_1,...,e_j,f is a linear cycle of length j+1. Thus every threshold-color connector at a free forest end is either an inter-component bridge giving the displayed path lower bound, or a cycle-closing chord in its own component.

        • [1000990] Equality-layer induction reconciles Turan and critical-core minimality
            STATEMENT
            Fix ell>=4 and d=floor(2ell/3). Consider the strengthened equality-layer assertion S_ell: every P_ell-free linear 3-graph H with |E(H)|>=d|V(H)| that contains a nonspecial edge has a vertex of degree at most d. If S_ell holds, then ex_L(n,P_ell^(3))<=dn. Moreover, whenever H is an edge-minimal counterexample to S_ell with |E(H)|>=d|V(H)|+1, then for every nonspecial edge e with witness path P, every edge f outside P contains a vertex of degree exactly d+1 in H.

          • [1000092] The sharp Turan equality layer forces residue-dependent ascending mass
              STATEMENT
              Let d=floor(2ell/3). If a P_ell-free linear 3-graph satisfies |E(H)|=d|V(H)| and A is its number of ascending nonspecial edges, then A>=3n, n, or 2n according as ell is congruent to 0,1, or 2 mod3. Thus the equality layer itself forces a large structured ascending defect, especially in residues 0 and 2.

          • [1000265] The sharp Turan bound reduces to the exact-density equality layer
              STATEMENT
              Fix ell>=5, put d=floor(2ell/3) and k=d+1. Assume the following equality-layer assertion E_ell:
              
              Every P_ell-free linear 3-graph J with |E(J)|=d|V(J)| that contains a nonspecial edge has a vertex of degree at most d.
              
              Then
              ex_L(n,P_ell^(3))<=dn
              for every n.
              
              More strongly, under E_ell there is no edge-minimal strict counterexample, because its DXX color graph simultaneously has more than k(k-3/2)|X| edges and fewer than ((9ell+5)/7)|X| edges.

            • [1000549] Cheap outside packets force a low-degree survivor
                STATEMENT
                Let H be a vertex-minimal counterexample to the strengthened equality-layer assertion S_ell at density d=floor(2ell/3), and let O be the vertices outside a fixed nonspecial witness path. If a nonempty packet S⊆O satisfies |N(S)|<=d|S|, then H-S still has density at least d and retains the nonspecial witness, so H-S contains a vertex of degree at most d. No Hall-type packet expansion follows without an additional minimum-degree-preservation or lift-back argument.

              • [1000972] Vertex-minimal equality does not by itself give outside packet expansion
                  STATEMENT
                  The packet-expansion conclusion in 7a55fc8cb587 is not justified by vertex-minimality of an equality-layer counterexample alone. From a nonempty S outside a preserved nonspecial witness and |N(S)|<=d|S|, one may infer that H-S has density at least d and retains the nonspecial edge, but H-S can have minimum degree at most d because deleting S may lower degrees of surviving vertices. In that case H-S satisfies, rather than violates, the equality-layer assertion. Thus no contradiction to minimality follows without a separate minimum-degree-preservation or strengthened inductive hypothesis.

            • [1000838] Exact density forces a potential-deficiency surplus of upward 0-1-1 transitions
                STATEMENT
                Let H be a \(P_\ell\)-free linear 3-graph with \(m=dn\), where \(d=\lfloor 2\ell/3\rfloor\). Choose maximum endpoint paths as in the contact-multiplicity snake wherever defined, let \(U\) be the number of unpaid 0-1-1 ascending edges, and define
                \[
                A_\phi=\sum_{v\in V(H)}((\ell-1)-\phi(v)),\qquad
                N_i=|\{v\in V(H):\phi(v)=i\}|\quad(i=0,1).
                \]
                Then
                \[
                U\ge \gamma_\ell n+2A_\phi,
                \qquad
                \gamma_\ell=3d-(2\ell-3),
                \]
                where \(\gamma_\ell=3,1,2\) according as \(\ell\equiv0,1,2\pmod3\).
                
                Orient every 0-1-1 edge from its unique entrance \(x\) to its two terminals \(y,z\). This produces an acyclic directed two-branch transition system because \(\phi(y),\phi(z)\ge\phi(x)+1\). If \(t_U(v)\) counts transitions for which \(v\) is a terminal, then
                \[
                t_U(v)\le\max\{0,2\phi(v)-3\},
                \]
                and hence
                \[
                2U\le (2\ell-5)n-2A_\phi+N_1+3N_0.
                \]
                In particular, if \(\phi(v)\ge1\) for every vertex, then
                \[
                2U\le (2\ell-5)n-2A_\phi+N_1,
                \]
                and if \(\phi(v)\ge2\) for every vertex, then
                \[
                2U\le (2\ell-5)n-2A_\phi.
                \]

              • [1000474] Exact-density nonspecial obstructions have average endpoint potential d plus five-sixths
                  STATEMENT
                  Let H be a P_ell-free linear 3-graph with exact density |E(H)|=d|V(H)|, where d=floor(2ell/3), and suppose the contact-snake setup yields the unpaid 0-1-1 transition count U as in bbcfa1f0ff1d. Then the average endpoint potential satisfies
                  (1/n) sum_v phi(v) >= d+5/6.
                  Equivalently,
                  A_phi=sum_v((ell-1)-phi(v)) <= (ell-1-d-5/6)n.
                  This bound is residue-independent despite the residue-dependent transition surplus gamma_ell.

              • [1000497] Ascending potential flow forces a quadratic degree-potential constraint
                  STATEMENT
                  Let H be a finite linear 3-graph in which phi(v)>=2 for every vertex. Write p_v=phi(v), d_v=d_H(v), m=|E(H)|, and let A be the number of ascending nonspecial edges. Then
                  2A <= sum_v p_v(6p_v-5-2d_v).
                  Moreover A>=3m-2sum_v p_v+n. Consequently
                  sum_v [6p_v^2-p_v-2(p_v+1)d_v-2] >=0.
                  In particular every exact-density equality obstruction m=d n must satisfy this quadratic degree-potential constraint.

            • [1001123] Ascending terminal density would reduce equality to the single critical residue
                STATEMENT
                Let H be a P_ell-free linear 3-graph on n vertices with m=d n edges, where d=floor(2ell/3), and let A be the number of ascending nonspecial edges. Then the certified ascending-edge accounting inequality forces
                A >= (3d-2ell+3)n.
                Equivalently:
                if ell≡0 mod3, A>=3n;
                if ell≡1 mod3, A>=n;
                if ell≡2 mod3, A>=2n.
                
                Consequently, if the ascending terminal-pair graph T_up satisfies mad(T_up)<=3, hence A<=3n/2, then no exact-density equality-layer counterexample can exist for ell≡0 or 2 mod3. Under that terminal-graph bound, the grand equality-layer induction is reduced entirely to ell≡1 mod3.

              • [1001099] Potential-oriented local degree would close the zero residue equality layer
                  STATEMENT
                  Assume the potential-oriented local bound 50b6278b9537: for every vertex v, at most three ascending nonspecial edges e={x,v,u} with v terminal satisfy phi(u)>=phi(v). Then the ascending terminal-pair graph T_up is 3-degenerate. Consequently |E(T_up)|<3|V(T_up)|<=3|V(H)|. In particular, combined with exact-density accounting, this alone eliminates every equality-layer counterexample for ell≡0 mod3.

          • [1000282] Every equality-layer bad witness omits a vertex of degree at least d plus two
              STATEMENT
              Let ell>=5 and d=floor(2ell/3). If a linear 3-graph H satisfies |E(H)|=d|V(H)| and P is any q-edge path with q<=ell-1, then not all vertices outside P can have degree d+1. In fact some vertex outside P has degree at least d+2. Thus in an equality-layer obstruction every nonspecial witness omits a genuinely higher-degree vertex, and the all-threshold outside-reservoir branch is impossible.

            • [1000699] Every equality-layer witness omits many above-threshold vertices
                STATEMENT
                Let ell>=5 and d=floor(2ell/3). In an n-vertex linear 3-graph with |E(H)|=dn and minimum degree at least d+1, every path P of length at most ell-1 omits at least 4d-2ell vertices of degree at least d+2. More precisely, the total outside excess E_O=sum_{v outside P}(d(v)-(d+1)) satisfies E_O>=n(2d-1-|V(P)|/2)+|V(P)|(d+3/2). Thus a nonspecial equality-layer witness omits at least d, d-2, or d-1 genuinely above-threshold vertices according as ell is 0,1,2 mod3.

          • [1000467] Equality-layer strict counterexamples are overwhelmingly threshold-degree
              STATEMENT
              Let d=floor(2ell/3), k=d+1, and let H be an edge-minimal counterexample to S_ell with |E(H)|>=d|V(H)|+1. For D={v:d(v)=k} and X=V(H)\\D, one has d|X|<=|D|+ell-2. If X is nonempty then |D|>=k. Thus the strict equality-layer counterexample consists overwhelmingly of exact-threshold vertices; the higher-degree exceptional set has size at most (|D|+ell-2)/d and induces only the universal path forest.

          • [1000490] Exact minimal equality obstructions admit a balanced d-outregular incidence orientation
              STATEMENT
              In the simultaneous strengthened S_ell induction, after the strict layer is excluded, let H be a vertex-minimal exact-density counterexample with |E(H)|=d|V(H)|. Then every proper nonempty induced H[W] has at most d|W|-1 edges. Equivalently every nonempty proper S meets at least d|S|+1 hyperedges. Hall therefore assigns every hyperedge to one incident vertex so that each vertex is assigned exactly d hyperedges.

            • [1000747] Balanced equality orientation is an almost-regular self-colored matching graph
                STATEMENT
                The balanced d-outregular orientation of an exact equality obstruction induces a simple properly edge-colored graph G on the same vertex set: every color x is a d-edge matching avoiding vertex x, every color occurs exactly d times, and d_G(v)=d_H(v)-d=2d-k_v. Every strong-rainbow graph path lifts to a linear hypergraph path. Hence the equality target k_v>=2d is exactly an isolated vertex in G; in the stalled branch G has average degree 2d and minimum degree at least 2d-kappa-3.

          • [1000719] Exact-density equality obstructions have a huge outside reservoir
              STATEMENT
              Let ell>=4 and d=floor(2ell/3). If a linear 3-graph H satisfies |E(H)|=d|V(H)|, then |V(H)|>=6d+1. Consequently any P_ell-free equality-layer graph has at least
              6d-2ell+2
              vertices outside every linear path of length at most ell-1. Explicitly, this outside-vertex lower bound is 2ell+2 when ell≡0 mod3, 2ell-2 when ell≡1 mod3, and 2ell when ell≡2 mod3.

          • [1000730] Two two-contact chords through one outside owner give an exact bridge splice
              STATEMENT
              Let P=(p_1,...,p_s) be a linear path and o outside P. Suppose f={o,r,r_prime} and g={o,t,t_prime} are distinct edges through o, with four distinct P-contacts. If r is last seen in p_i, t is first seen in p_k, i<k, and all occurrences of r_prime,t_prime lie strictly between i and k, then p_1,...,p_i,f,g,p_k,...,p_s is a linear path of length s+3-(k-i). Thus gap two extends the path and gap three gives a length-preserving rotation.

          • [1001104] Exact Turan density has Steiner order at least 6d plus one
              STATEMENT
              Every n-vertex linear triple system with |E(H)|=dn satisfies n>=6d+1. Equality n=6d+1 holds iff H is a Steiner triple system. More generally, if n=6d+1+s, then the uncovered-pair leave graph has exactly ns/2 edges and average degree s.

            • [1000396] Leave deviations form a zero-sum charge field whose negative mass forces ascending flow
                STATEMENT
                For an exact-density system with n=6d+1+s, define k_v=(d_U(v)-s)/2. Then k_v is integral, sum_v k_v=0, and d_H(v)=3d-k_v. If H is P_ell-free, max k_v>=kappa=3d-2ell+3, equal to 3,1,2 by residue. Every vertex with k_v=-r<0 has phi(v)<=ell-2 and sources at least kappa+r+2 ascending nonspecial edges. Thus negative leave charge is quantitatively converted into upward potential flow.

              • [1000069] The equality-layer conjecture is exactly a leave-charge amplification to 2d
                  STATEMENT
                  In the exact-density charge coordinates k_v=(d_U(v)-s)/2, one has d_H(v)=3d-k_v. Hence the equality-layer conclusion d_H(v)<=d is exactly k_v>=2d. A counterexample has k_v<=2d-1 for every vertex, sum k_v=0, a forced positive spike kappa=3d-2ell+3 in {3,1,2}, and every negative charge -r sources at least kappa+r+2 ascending edges. Thus the grand equality step is precisely a charge-amplification problem from kappa to 2d, with ascending flow as the amplification mechanism.

                • [1000236] Ascending flow gives a levelwise charge-to-superlevel growth inequality
                    STATEMENT
                    For L_p={v:phi(v)=p} and V_{p+1}={u:phi(u)>=p+1}, one has 2 sum_{v in L_p} max(0,d_H(v)-2p+1) <= (2p-1)|V_{p+1}|. At exact density d_H(v)=3d-k_v, this becomes 2 sum_{L_p} max(0,3d-k_v-2p+1) <= (2p-1)|V_{p+1}|. Thus low-potential negative charge forces quantitative growth of higher potential superlevels.

                  • [1000203] Negative charge at level p pays a fixed branching surcharge
                      STATEMENT
                      Let N_p={v:phi(v)=p,k_v<0} and R_p=sum_{N_p}(-k_v). Then (2p-1)|V_{p+1}| >= 2[(3d-2p+1)|N_p|+R_p]. Thus each negative-charge vertex at level p pays both its charge mass and a fixed surcharge 3d-2p+1 in next-superlevel terminal capacity; the surcharge is large at low potential and falls to kappa+2 at p=ell-2.

                • [1000252] Opposite endpoints amplify the forced equality charge by two
                    STATEMENT
                    Let k_v=3d-d_H(v) in a P_ell-free exact-density equality obstruction and kappa=3d-2ell+3. Then max_v k_v>=kappa+2. Indeed zero-sum charge gives a negative-charge vertex v; its degree exceeds 3d, so phi(v)<=ell-2. The opposite endpoint z of a maximum phi(v)-path has degree at most 2phi(v)-1<=2ell-5, hence k_z>=3d-2ell+5=kappa+2. Thus max charge is at least 5,3,4 in residues 0,1,2.

                  • [1000534] Either charge amplifies by four or all negative charge is trapped one level below the top
                      STATEMENT
                      In an exact-density P_ell-free equality obstruction, either max_v k_v>=kappa+4, or every negative-charge vertex has endpoint potential exactly ell-2. In the exceptional case, each negative vertex v with k_v=-r sources at least kappa+r+2 rank-(ell-1) ascending edges whose terminal pairs lie in the top layer T={phi=ell-1}; these form a strong-rainbow properly colored matching graph on T, and every u in T has positive charge k_u>=kappa.

                    • [1000193] A stalled charge amplification obstruction has only two potential levels
                        STATEMENT
                        If max charge is below kappa+4 in an exact-density P_ell-free equality obstruction, then every vertex has endpoint potential ell-2 or ell-1. All negative charge lies in S=L_{ell-2}; every top-layer vertex in T=L_{ell-1} has charge at least kappa; and every ascending edge is an S-to-TT rank-(ell-1) edge.

                      • [1000725] In the stalled two-level state every longest path is top-potential except for a constant defect
                          STATEMENT
                          Let L=ell-1 in the stalled state max k<=kappa+3. If u is top-potential with k_u=kappa+h, 0<=h<=3, then every globally longest L-edge path ending at u contains at least 2L-4h-6 top-potential vertices, hence at most 4h+7 low-level vertices. In particular every such path contains at most 19 vertices of potential ell-2.

                    • [1001187] Trapped-negative charge forces a high-degree top star with many single blockers
                        STATEMENT
                        In the exceptional trapped-negative two-layer charge state, put a=kappa+2, N={v:k_v<0}, R=sum_{v in N}(-k_v), and let G be the properly edge-colored top-layer terminal graph with support S.
                        
                        (i) Every u in S has k_u>=a, hence R>=a|S|.
                        (ii) For each v in N of negative mass r=-k_v, r<=R/(2a)-a; consequently |N|>=2a+1=2kappa+5.
                        (iii) The graph G has average degree greater than 2a, so some top-layer vertex u has d_G(u)>=2a+1=2kappa+5. Its incident G-edges come from distinct negative source colors and rank-(ell-1) ascending nonspecial hyperedges.
                        (iv) If additionally max_w k_w<=kappa+3, then for any G-edge h at such a vertex u and any longest p=(ell-1)-edge path P ending in h with last vertex u, the number B_P(u) of other incident terminal edges double-blocking P is at most 3. Hence at least 2kappa+1 other incident G-edges are full-rank equal-potential single blockers of P.

                • [1000803] Quadratic potential flow becomes an exact charge-potential covariance lower bound
                    STATEMENT
                    With leave charges k_v=(d_U(v)-s)/2 and centered endpoint potentials a_v=phi(v)-d, every exact-density equality obstruction satisfies
                      2 sum_v a_v k_v >= n(7d+2)-(6d-1)sum_v a_v-6sum_v a_v^2.
                    Hence whenever the right side is positive, the obstruction has quantitatively positive covariance between leave charge and endpoint potential.

                • [1000810] Vertex charge and density deficit obey an exact deletion recurrence
                    STATEMENT
                    If |E(H)|=d|V(H)|-r and q_v:=3d-d_H(v), then sum_v q_v=3r. Deleting a vertex w produces new deficit r_prime=r+2d-q_w. Thus at equality, deleting charge K creates deficit 2d-K, and the target charge 2d is exactly the threshold for deletion not to worsen the deficit.

                  • [1000308] Packet deletion has an exact effective-charge formula
                      STATEMENT
                      At exact density, for any vertex set S with charge K(S)=sum_{v in S}k_v and m_i(S) edges meeting S in exactly i vertices, the deficit after deleting S is r(H-S)=2d|S|-K(S)-m_2(S)-2m_3(S). Hence S is deficit-nonincreasing exactly when K(S)+m_2(S)+2m_3(S)>=2d|S|. Shared edges therefore act as packet charge.

            • [1000452] Equality obstructions have Steiner deficiency at least two
                STATEMENT
                Let d=floor(2ell/3). An exact-density P_ell-free linear triple system with |E(H)|=d|V(H)| cannot have order 6d+1 or 6d+2. Equivalently the leave-deficiency parameter s=n-(6d+1) is at least 2. At s=0 the system is an STS and is 3d-regular; at s=1 parity forces the leave to be a perfect matching, again making H 3d-regular. In both cases the minimum-degree endpoint-potential bound forces a P_ell.

              • [1000140] Steiner deficiency two forces pair-universal vertices
                  STATEMENT
                  In an exact-density P_ell-free equality obstruction with n=6d+3 (Steiner deficiency s=2), the leave graph has even degrees and average degree 2 but cannot be 2-regular. Hence it has a degree-zero vertex, corresponding to a pair-universal vertex of H of degree 3d+1. If ell=0 mod3, the leave spike Delta>=6 forces at least two such pair-universal vertices; in residues 1 and 2 at least one is forced.

                • [1000339] At Steiner deficiency two, universal vertices exactly pay for leave branching
                    STATEMENT
                    In the s=2 equality layer the leave U is even of average degree two. If z is the number of leave-isolated vertices and n_{2j} the number of leave-degree 2j vertices, then z=sum_{j>=2}(j-1)n_{2j}. Thus pair-universal vertices of H exactly equal the total branching excess of the Eulerian leave. In particular z=1 forces one degree-4 branch vertex and all other nonisolated vertices degree 2; the exceptional leave component suppresses to a bouquet of two cycles.

                  • [1000984] At deficiency two, P_l-freeness forces many leave branches and universal vertices
                      STATEMENT
                      In the s=2 equality layer let B be the leave vertices of degree at least 4, b=|B|, and z the number of leave-isolated/pair-universal vertices. Then P_ell-freeness forces b>=3d-2ell+3, and the defect identity gives z>=b. Thus b,z are at least 3,1,2 according as ell is 0,1,2 mod3.

                • [1000969] A pair-universal star converts degree-potential defect exactly into clean ascending sources
                    STATEMENT
                    Let v be pair-universal and P a maximum p=phi(v)-edge path ending at v. If B_j counts star pairs through v with exactly j contacts in V(P)\{v}, then B_0-B_2=d_H(v)-2p. Every B_0 edge is necessarily an ascending nonspecial edge of rank p+1 with unique entrance v. Hence every maximum v-ending path exposes at least d_H(v)-2phi(v) clean ascending source edges, with exact surplus B_2.

                  • [1000869] Every universal-star maximum path omits a large higher-potential terminal packet
                      STATEMENT
                      Let v be pair-universal and P a maximum p=phi(v)-edge path ending at v. Then the clean-star count satisfies B_0>=d_H(v)-2p+1, because the final path edge itself contributes to B_2. Every B_0 edge is an ascending nonspecial source edge at v whose two terminals lie outside P. Hence P omits at least 2(d_H(v)-2p+1) vertices of potential at least p+1. In the s=2 equality layer with p=ell-2 this gives 12, 8, or 10 omitted top-potential vertices by residue.

            • [1000604] Equality obstructions force a leave-degree spike in residues zero and two
                STATEMENT
                Let d=floor(2ell/3), n=6d+1+s, and U be the leave graph of an exact-density P_ell-free linear triple system. Then Delta(U)>=6d+s-4ell+4. Hence Delta(U)>=s+4 when ell=0 mod3, Delta(U)>=s when ell=1 mod3, and Delta(U)>=s+2 when ell=2 mod3. Thus residues 0 and 2 force the leave to be genuinely more irregular than its average degree s.

              • [1001020] Sharp endpoint threshold strengthens the equality leave spike
                  STATEMENT
                  For an exact-density P_ell-free system with n=6d+1+s and leave U, one has Delta(U)>=6d+s-4ell+6. Thus the leave maximum degree is at least s+6, s+2, or s+4 according as ell is 0,1,2 mod3. At s=2 this means degrees at least 8,4,6.

            • [1001149] Equality forces a high-degree low-potential ascending source
                STATEMENT
                Every exact-density P_ell-free equality obstruction contains a vertex v with d_H(v)>=3d+1 and phi(v)<=ell-2, where d=floor(2ell/3). Consequently v is the entrance of at least 3d-2ell+6 ascending nonspecial edges: at least 6, 4, or 5 in residues ell=0,1,2 mod3 respectively. Their terminal pairs are disjoint, giving at least twice as many distinct higher-potential outneighbors.

          • [1001150] Threshold-cover plus sharp deletion kills the strict Turan layer for ell at least six
              STATEMENT
              Let ell>=6, d=floor(2ell/3), and H be P_ell-free with |E(H)|>=d|V(H)|+1. Suppose H has the equality-layer threshold-cover structure for D={v:d(v)=d+1}, and suppose the sharp deletion step gives m_2+2m_3<=|D|-1. Then H cannot contain a nonspecial edge. Equivalently, under the simultaneous equality-layer/Turan induction, every strict counterexample is eliminated for ell>=6; the remaining substantive obstruction is the equality layer |E(H)|=d|V(H)|.

        • [1000063] Minimum-degree-first convention for the 2/3 route
            STATEMENT
            For the main route toward ex_L(n,P_ell^(3))<=floor(2ell/3)n, impose δ(H)>=floor(2ell/3)+1 at the outset by the minimal-counterexample reduction before applying snake, ascending-edge, rank, blocker, or computational attacks.

          • [1000005] Dense-core all-special conjecture
              STATEMENT
              For every ell>=4, if H is a P_ell^(3)-free linear 3-uniform hypergraph with minimum degree delta(H)>2ell/3, equivalently delta(H)>=floor(2ell/3)+1, then every edge of H is special in the Devine–Milans snake digraph.

            • [1000044] The n<=12 strict two-thirds search reduces to three structural classes
                STATEMENT
                Let H be a positive-minimum-degree linear triple system on 6<=n<=12, with maximum path length L and minimum degree delta. If H has a nonspecial edge and 3delta>2L+2, then H belongs to one of three classes: (I) L=3 and delta=3; (II) n=12, L=4 and H is 4-regular with 16 edges; or (III) n=12, L=5 and H is 5-regular, equivalently a one-point puncture of an STS(13).

              • [1000311] Every P4-free linear triple system of minimum degree three is all-special
                  STATEMENT
                  If H is a linear 3-uniform hypergraph with no P_4^(3) and minimum degree at least 3, then every edge of H is special in the snake digraph.

              • [1000853] Strict two-thirds all-special threshold for n<=12
                  STATEMENT
                  Let H be a positive-minimum-degree linear triple system on 6<=n<=12, with minimum degree delta and maximum linear-path length L. If 3delta>2L+2, then every edge of H is special. Equivalently, if H has a nonspecial edge then 3delta<=2L+2.

                • [1000035] Class-III systems have no rank-four nonspecial edge
                    STATEMENT
                    A 12-vertex 5-regular linear triple system has no nonspecial edge of rank four.

                • [1000057] Correct terminal-blocker localization in Class III
                    STATEMENT
                    In the Class-III maximum-rank setup P=(g_1,g_2,g_3,g_4,e), e={x,y,z}, put W=V(P)\e and E=W∩V(g_1∪g_2). For any edge h≠e through a terminal y or z, either h has a contact in E, or h is the unique single blocker using the outside vertex o and its sole W-contact lies in g_4\e. In particular no terminal edge can have its first precursor contact in g_3, and a terminal with four double blockers has no L-L blocker pair except possibly a pair whose earlier contact is already in E; the only completely late exceptional contact is the penultimate single blocker.

                • [1000141] Class-II rank-four nonspeciality forces a crossed terminal rectangle
                    STATEMENT
                    Let H be a 4-regular linear 3-graph with no five-edge linear path. Suppose e={x,y,z} is a nonspecial edge of rank four with unique entrance x, and let P=(g_1,g_2,g_3,e) be a longest path ending in e through x. Write g_1={r,a,b} and g_2={r,c,d}. Then, after swapping c,d, H contains the four forced edges
                    {y,a,c}, {y,b,d}, {z,a,d}, {z,b,c}.
                    In particular these four edges are pairwise intersecting and form a K_4 in the intersection graph.

                • [1000150] Class-III rank-five nonspeciality reduces to a nine-vertex residual matching obstruction
                    STATEMENT
                    Let H be a 12-vertex 5-regular linear triple system and let e={x,y,z} be a nonspecial edge of global maximum rank five with unique entrance x. Put R=H-{x,y,z}. Then R has 9 vertices, 7 edges, and degree multiset (3,3,3,2,2,2,2,2,2); its three degree-three vertices are exactly the uncovered mates x*,y*,z* of x,y,z. The four edges through y other than e induce a perfect matching F_y on V(R)\{y*}, and the four edges through z other than e induce a perfect matching F_z on V(R)\{z*}. For every pair {u,v} in F_y, R contains no three-edge linear path ending at u with u as a last vertex while avoiding v, and none ending at v with v as a last vertex while avoiding u. The analogous statement holds for every pair of F_z.

                  • [1000690] At least one Class-III terminal matching has two high-low pairs
                      STATEMENT
                      In the nine-vertex residual obstruction 213f75e9692a, the two terminal matchings F_y and F_z cannot both pair their two available degree-three vertices together. Consequently at least one of F_y,F_z contains two high-low pairs.

                  • [1001086] Triangle-type classification of the Class-III nine-vertex residual obstruction
                      STATEMENT
                      In the residual obstruction R of 213f75e9692a, let A,B,C be the three degree-three vertices and let F_x,F_y,F_z be the off-star matchings induced by the three vertices x,y,z of e (so F_x omits A, F_y omits B, F_z omits C). At most one of F_x,F_y,F_z contains its available high-high pair. More precisely:
                      
                      (i) If exactly one matching is high-high, then R has triangle-type counts (n_0,n_1,n_2,n_3)=(0,5,2,0), where n_i is the number of R-edges containing exactly i high vertices. Exactly four lows are external high-low mates, each has exactly two high neighbors in R, and the other two lows are adjacent in R to all three highs.
                      
                      (ii) If no matching is high-high, then R has triangle-type counts either (0,6,0,1) or (1,3,3,0). Every low is the external mate of exactly one high and is adjacent in R to exactly the other two highs.

                • [1000188] Every vertex deletion of a 12-vertex 5-regular linear triple system has a spanning P5
                    STATEMENT
                    Let H be a 12-vertex 5-regular linear 3-uniform hypergraph. Then for every vertex z, the deletion H-z contains a spanning five-edge linear path.

                • [1000420] Class-III rank-four terminal stars force an alternating five-vertex matching
                    STATEMENT
                    Let H be a 12-vertex 5-regular linear triple system. Suppose e={x,y,z} is a nonspecial edge of rank four with unique entrance x, and let
                      P=(g_1,g_2,g_3,e)
                    be a longest path ending in e through x. Write
                      g_1={r,a,b},  g_2={r,c,d},
                    and relabel c,d so that
                      g_3={c,x,t}.
                    Let u,v,w be the three vertices outside V(P), and put
                      R={r,t,u,v,w}.
                    
                    After possibly swapping c,d, the terminal stars contain the crossed rectangle
                      {y,a,c}, {y,b,d}, {z,a,d}, {z,b,c}.
                    
                    The two remaining edges through y other than e determine a 2-edge matching M_y on R, and the two remaining edges through z determine an edge-disjoint 2-edge matching M_z on R. Every vertex of R lies in M_y∪M_z; hence M_y∪M_z is an alternating five-vertex path. Moreover r is an internal vertex of this path, so r has degree two in M_y∪M_z.
                    
                    Finally, among the eight edges of H not yet listed, every edge contains exactly one vertex of
                      A={r,a,b,c,d}
                    and two vertices of
                      B={x,t,u,v,w}.

                • [1000633] Class-II systems have no rank-four nonspecial edge
                    STATEMENT
                    A 4-regular P_5^(3)-free linear triple system has no nonspecial edge of rank four.

                • [1000634] Every Class-II system is all-special
                    STATEMENT
                    Every 12-vertex 4-regular linear triple system with no five-edge linear path is all-special.

                • [1000823] Class-III nonspecial edges have rank at least four
                    STATEMENT
                    In a 12-vertex 5-regular linear triple system, every nonspecial edge has edge rank at least four. Consequently, in Class III of the n<=12 strict-threshold reduction, a hypothetical nonspecial edge has rank exactly 4 or 5.

                • [1000880] Contact-gap restrictions for a rank-four nonspecial edge against a P5
                    STATEMENT
                    Let Q=(g_1,...,g_5) be a five-edge linear path and let e={x,y,z} be an edge outside Q such that z is absent from Q while x,y lie on Q. Suppose e is nonspecial of rank four with unique entrance x. Record at each path edge whether it contains x (X), contains y (Y), or is disjoint from e (0). Then the X-positions and Y-positions are disjoint blocks of length one or two; every 0-run adjacent to a contact has length at most two; and every 0-run adjacent to a Y-position has length at most one.

                • [1000931] Class-II rank-three nonspeciality forces an alternating terminal C6
                    STATEMENT
                    Let H be a 4-regular P_5^(3)-free linear triple system. Suppose e={x,y,z} is nonspecial of rank three with unique entrance x, and let P=(g_1,g_2,e) be a longest path ending in e through x. Then the six edges through the terminal vertices y,z other than e induce two edge-disjoint perfect matchings on the same six-vertex set, whose union is a single alternating 6-cycle.

                • [1000974] Failed high-low terminal pair forces both other high vertices onto the low mate
                    STATEMENT
                    Let R be a 9-vertex 7-edge linear triple system with degree multiset (3,3,3,2,2,2,2,2,2). Let t have degree 3 and o have degree 2, and suppose no edge of R contains {t,o}. If R contains no three-edge linear path ending physically at t and avoiding o, then o is adjacent in R to both of the other degree-three vertices.

                • [1001164] Class-III systems have no rank-five nonspecial edge
                    STATEMENT
                    Every 12-vertex 5-regular linear triple system has no nonspecial edge of rank five. Consequently, together with the rank-at-least-four reduction and the rank-four exclusion, every Class-III system in the n<=12 strict two-thirds reduction is all-special.

                • [1001204] Class-III blocker defects reduce to one or two explicit alternating chains
                    STATEMENT
                    In a 12-vertex 5-regular linear triple system, let P=(g_1,g_2,g_3,g_4,e) be a maximum five-edge path ending in a rank-five nonspecial edge e={x,y,z}. For the terminal blocker matchings on W=V(P)\e, the union has only one or two open alternating chain defects. Their endpoints are exactly the uncovered-mate and single-blocker data. Moreover, whenever a terminal single blocker has no early contact in g_1∪g_2, its path contact is forced to the private vertex of g_4.

            • [1000142] Minimum-degree rank floor and layer recurrence have disjoint support
                STATEMENT
                Let H be a finite linear 3-graph of minimum degree delta. If an ascending nonspecial edge lies in layer J_k, then k>=ceil((delta+1)/2). Therefore the positive-coefficient range delta>2k-1 of the ascending-layer recurrence contains no nonempty ascending layer.

            • [1000249] Rank-band decomposition for the grand two-thirds conjecture
                STATEMENT
                Let H be a P_ell-free linear 3-graph with minimum degree delta>2ell/3 and global maximum path length L<=ell-1. To prove every edge special, it is enough to eliminate ascending nonspecial edges rank-by-rank. The existing machinery suggests three bands.
                
                LOW BAND: q<=delta-1. Certified rotation expansion gives every fixed-entrance state degree at least 4(delta-q)-2. Thus the farther q lies below delta, the more violently its entrance-path state space branches. Any proof in this band should convert branching into either a terminal-label switch, a repeated blocker/cycle contradiction, or a longer path.
                
                BOUNDARY BAND: q=delta. Every state still rotates, but local branching may collapse. Certified boundary normal forms show the only sink-like configurations are exact or almost exact blocker partitions of the entrance path, with only two or three exceptional single blockers. This is the natural finite-width transition layer.
                
                TOP BAND: delta<q<=L. Since delta>2L/3 follows from delta>2ell/3 and L<=ell-1 only up to additive slack, in any putative sharp counterexample this band has width at most roughly L/3. Here entrance paths are long enough that terminal blocker systems become highly saturated. At q=L the punctured-Steiner analysis gives alternating matching systems, exact defect accounting, and low-deficiency strong-rainbow residual shadows. More generally the identity U_v-S_v=2(q-1? / path-relative analogue to be developed) should measure distance from saturation.
                
                Additionally, whenever q<=(L+1)/2, the certified long-terminal-path capture lemma forces every longest L-path ending at either terminal to contain all three vertices of the rank-q edge. Thus the low half of the spectrum is globally visible to longest paths, whereas only ranks above L/2 can evade complete capture.
                
                This yields a four-way proof agenda:
                (A) q<=min(delta-1,(L+1)/2): combine high rotation degree with complete capture by longest terminal paths;
                (B) (L+1)/2<q<=delta-1: use high fixed-entrance rotation degree without complete capture;
                (C) q=delta: eliminate the exact saturated-fan boundary states;
                (D) delta<q<=L: prove a stability theorem showing that small rotation defect forces a punctured-Steiner-like alternating-blocker/strong-rainbow residual structure, then eliminate it.
                
                The missing global bridge is no longer 'propagate nonspeciality to maximum rank' in one jump. It is enough to prove that every nonspecial edge in one of these bands either contradicts the corresponding local structure or transfers to a nonspecial edge/state in a strictly higher band.

            • [1000287] Punctured-Steiner boundary all-special conjecture
                STATEMENT
                For every d>=3, every d-regular linear 3-uniform hypergraph H on 2d+2 vertices with global maximum linear-path length d is all-special. Equivalently, every one-point puncture of an STS(2d+3) whose longest linear path has d edges has every edge special.

              • [1000015] Deficiency-s residual decomposition around a nonspecial edge
                  STATEMENT
                  Let H be a d-regular linear 3-uniform hypergraph on n=2d+1+s vertices, where s>=0, and let J be its uncovered-pair graph. Then J is s-regular.
                  
                  Fix an edge e={x,y,z}, put U=V(H)\e, and let R=H[U]. For q∈{x,y,z}, let D_q=N_J(q)⊂U and let F_q be the set of off-q pairs from the d-1 edges through q other than e. Then:
                  
                  (1) |D_q|=s and F_q is a matching of size d-1 covering exactly U\D_q.
                  
                  (2) For u∈U, if c(u)=|N_J(u)∩{x,y,z}|, then
                      d_R(u)=d-3+c(u).
                  
                  (3) Every unordered pair from U lies in exactly one of four types: the 2-shadow of R, F_x, F_y, F_z, or J[U]. Thus
                      E(K_U)=shadow_2(R) ⊔ F_x ⊔ F_y ⊔ F_z ⊔ E(J[U]).
                  
                  If moreover e is nonspecial of rank q with unique entrance x and y,z terminal at e, then for every {a,b}∈F_y, R contains no (q-2)-edge linear path ending physically at a while avoiding b, nor one ending at b while avoiding a; likewise for F_z.

                • [1000131] Outside-vertex deficiency equals open blocker-chain deficiency
                    STATEMENT
                    Let H be d-regular on 2d+1+s vertices and let e be a nonspecial edge of global maximum rank d. Relative to any globally longest d-edge path ending in e, if S_y,S_z are the numbers of terminal single blockers and p is the number of path components in the union of the two terminal double-blocker matchings, then U_v=S_v for each terminal v and p=S_y+S_z<=2s. Thus s=0 gives only alternating cycles, s=1 gives one or two open chains, and fixed s gives at most 2s open defects.

              • [1001052] Strong-rainbow shadow formulation of the punctured-Steiner residual obstruction
                  STATEMENT
                  Let R be any linear 3-uniform hypergraph, and let S be its 2-shadow, coloring each covered pair uv by the unique third vertex c(uv) such that {u,v,c(uv)}∈E(R). Let
                    Q=v_0v_1...v_k
                  be a simple graph path in S. Then the corresponding hyperedges
                    E_i={v_{i-1},v_i,c(v_{i-1}v_i)}
                  form a k-edge linear hypergraph path in this order if and only if the k colors c(v_{i-1}v_i) are pairwise distinct and none belongs to {v_0,...,v_k}.
                  
                  Call such a graph path strongly rainbow.
                  
                  Consequently, in the punctured-Steiner residual R of efe44a01f2dc on 2d-1 vertices, a hypothetical nonspecial maximum-rank edge forces the following: for every pair {a,b} in either terminal matching F_y or F_z, the colored shadow S contains no strongly-rainbow path of length d-2 ending at a and avoiding b, and none ending at b and avoiding a. Meanwhile the uncolored shadow is K_{2d-1} minus the four matching classes F_x,F_y,F_z,L_R of e6c8f5225c3f; its complement has degree two at the three high vertices and degree four at every low vertex.

              • [1001081] Universal residual and blocker normal form for punctured-Steiner regular systems
                  STATEMENT
                  Let d>=2 and let H be a d-regular linear 3-uniform hypergraph on 2d+2 vertices. Then the uncovered-pair graph of H is a perfect matching, so H is a one-point puncture of a Steiner triple system on 2d+3 vertices. Suppose moreover that H has global maximum path length d and e={x,y,z} is a nonspecial edge of rank d with unique entrance x. Put R=H-{x,y,z}, and let x*,y*,z* be the uncovered mates of x,y,z. Then:
                  (1) |V(R)|=2d-1 and |E(R)|=(2d-3)(d-2)/3;
                  (2) d_R(x*)=d_R(y*)=d_R(z*)=d-2, while every other vertex of R has degree d-3;
                  (3) for each v in {y,z}, the d-1 edges through v other than e induce a perfect matching F_v on V(R)\{v*};
                  (4) for every pair {a,b} in F_v, R contains no (d-2)-edge linear path ending at a with a as a last vertex while avoiding b, nor vice versa;
                  (5) relative to any maximum d-edge path P ending in e, the two terminal double-blocker matchings on W=V(P)\e have union consisting of even alternating cycles together with exactly one or two alternating path components.

                • [1000281] Extremal-deletion transfer for punctured-Steiner regular systems
                    STATEMENT
                    Let d>=2 and let H be a d-regular linear 3-uniform hypergraph on 2d+2 vertices. Fix a vertex z. Then H-z has 2d+1 vertices, exactly d(2d-1)/3 edges, one vertex of degree d and all other 2d vertices of degree d-1. Consequently, if every P_d-free linear triple system on 2d+1 vertices has at most d(2d-1)/3 edges and every equality example has degree sequence different from (d,(d-1)^{2d}), then H-z contains a spanning P_d. If the equality-profile condition holds for every d in some family, then every one-vertex deletion of every corresponding punctured Steiner system contains a spanning P_d.

                • [1000496] General early-or-penultimate localization of punctured-Steiner terminal defects
                    STATEMENT
                    In the setting of efe44a01f2dc, let P=(g_1,...,g_{d-1},e) be a maximum d-edge path ending in a nonspecial edge e={x,y,z} through entrance x. Fix a terminal v∈{y,z} and an edge h≠e through v. Then either h meets one of g_1,...,g_{d-3}, or h is the unique single blocker through v and has the form {v,o,p}, where o is the unique vertex outside P and p is the private vertex of the penultimate precursor edge g_{d-1}.

                • [1000827] Punctured-Steiner maximum-rank obstructions have one of two saturated defect topologies
                    STATEMENT
                    Under the hypotheses of efe44a01f2dc, a hypothetical maximum-rank nonspecial edge e has exactly one of two saturated defect topologies.
                    
                    (A) One-chain case: one terminal has a perfect double-blocker matching on W, while the other terminal has exactly one single blocker {v,o,w} and exactly one unused precursor vertex u; the unique alternating path component of M_y∪M_z joins w to u.
                    
                    (B) Two-chain case: each terminal v∈{y,z} has exactly one single blocker {v,o,w_v} using the unique outside vertex o and exactly one unused precursor vertex u_v. The two single blockers intersect at o, so together with e they form a linear 3-cycle. The union M_y∪M_z has exactly two alternating path components, whose endpoint defects are drawn from {w_y,u_y,w_z,u_z}.

                • [1001041] Colored-complement decomposition of the general punctured-Steiner residual
                    STATEMENT
                    In the residual system R from efe44a01f2dc, every unordered pair of residual vertices belongs to exactly one of five disjoint classes: it is covered by a triple of R; it belongs to exactly one of the three off-star matchings F_x,F_y,F_z induced by the deleted vertices x,y,z; or it belongs to the surviving leave matching L_R of size d-2. Equivalently, the complement of the 2-shadow of R is the edge-disjoint union F_x∪F_y∪F_z∪L_R, where |F_x|=|F_y|=|F_z|=d-1 and |L_R|=d-2.

                • [1001166] Punctured-Steiner terminal defects are exactly saturated
                    STATEMENT
                    In the setting of efe44a01f2dc, let P be a maximum d-edge path ending in a nonspecial maximum-rank edge e, let p be the number of alternating path components in the union of the two terminal double-blocker matchings, and for v in {y,z} let S_v,U_v denote respectively the numbers of single blockers and unused precursor vertices in the terminal defect accounting. Then p∈{1,2} and
                    S_y+S_z=p,
                    U_y+U_z=p.
                    More precisely:
                    - if p=1, one terminal has (B,S,U)=(d-1,0,0) and the other has (d-2,1,1);
                    - if p=2, both terminals have (B,S,U)=(d-2,1,1).

            • [1000288] Lexicographic path-state induction for the grand two-thirds conjecture
                STATEMENT
                A proposed induction for 3delta<=2L+2 tracks a nonspecial target edge together with an entrance path. Order states by increasing target rank, then decreasing path loss, then the span of the unique loss-one fixed-hole obstruction. Certified rotation, transfer, and sink lemmas show that all persistent recurrence is forced into two atoms: flat equal-rank transfer cycles and canonical loss-one fixed-hole/theta states. Closing those two atoms at the 3q/2 scale would prove the boundary step and plausibly the grand conjecture.

              • [1000807] Mod-three strengthened induction with an equality-structure layer
                  STATEMENT
                  A viable induction for the dense-core all-special conjecture should carry two statements: STRICT(r), all-specialness above 2r/3 for every r, and an EQUALITY(r) structural classification when 3 divides r. All one-degree induction failures occur exactly at smaller parameters divisible by three. The order-11 equality blocker cycle at r=6 and the order-12 open-defect analysis are the prototype equality structures that the strengthened induction should propagate.

            • [1000442] Inductive path-hull reduction for lower-rank nonspecial edges
                STATEMENT
                Assume the dense-core all-special conjecture is true for every forbidden length r with 4<=r<ell. Let H be a P_ell^(3)-free linear 3-graph of minimum degree delta, and let e be a nonspecial edge of rank q<=ell-2. For every q-edge path P ending in e, put U=V(P) and G=H[U]. Then:
                
                (1) |U|=2q+1, so G is automatically P_{q+1}^(3)-free.
                
                (2) e has rank exactly q in G and is nonspecial in G with the same unique entrance as in H.
                
                (3) Consequently
                    delta(G) <= floor(2(q+1)/3).
                
                Hence every such witness path P contains a vertex v with at least
                    d_H(v)-floor(2(q+1)/3)
                and in particular at least
                    delta-floor(2(q+1)/3)
                incident edges not wholly contained in V(P).
                
                Every such external incident edge meets V(P) in either exactly v or exactly two vertices including v; equivalently, relative to the spanning path hull it is a clean ear or a one-contact chord. Thus, under induction on ell, every lower-rank nonspecial edge q<=ell-2 forces an ear-rich vertex on each maximum q-edge witness path.

              • [1000105] Inductive path-hull ears are threshold-supported in an edge-minimal counterexample
                  STATEMENT
                  Let ell>=4 and k=floor(2ell/3)+1. Assume the dense-core all-special conjecture for all smaller forbidden lengths, and let H be an edge-minimal P_ell-free counterexample with minimum degree k. Let D={v:d_H(v)=k}. Let e be a nonspecial edge of rank q<=ell-2 and P a q-edge witness path ending in e. Put G=H[V(P)].
                  
                  Then there exists v∈V(P) with
                    d_H(v)-d_G(v) >= k-floor(2(q+1)/3).
                  Every edge through v counted on the left meets D.
                  
                  If v∉D, these external edges meet pairwise distinct vertices of D. Hence v has at least
                    k-floor(2(q+1)/3)
                  distinct neighbors in D, each lying with v in a different external hyperedge.

              • [1001042] Minimal-counterexample induction reduces every bad path hull to ears or a spanning top-rank core
                  STATEMENT
                  Assume the dense-core all-special conjecture is true for every forbidden length r<ell. Let H be a counterexample for ell with minimum degree delta>2ell/3, chosen with |V(H)| minimum. Let e be any nonspecial edge of rank q and let P be any q-edge path ending in e. Put U=V(P) and G=H[U].
                  
                  Then exactly one of the following holds:
                  
                  (A) G has a vertex v with
                      d_G(v)<=floor(2(q+1)/3),
                  so v is incident in H with at least
                      delta-floor(2(q+1)/3)
                  edges not contained in U; every such edge is a clean ear or one-contact chord relative to U.
                  
                  (B) q=ell-1 and U=V(H). In particular P is a spanning top-rank path and |V(H)|=2ell-1.
                  
                  Thus every nonspecial edge in a minimal counterexample either exposes a quantitatively ear-rich vertex on each maximum witness path, or is top-rank and has a spanning witness.

            • [1000587] Two-lemma induction scheme for the dense-core all-special conjecture
                STATEMENT
                For ell>=4 define k_ell=floor(2ell/3)+1.
                
                Suppose the following two statements hold for every ell.
                
                EAR-TO-PROGRESS(ell):
                Let H be P_ell-free with delta(H)>=k_ell. Let e be nonspecial of rank q<=ell-1 and P a q-edge path ending in e. If some v in V(P) has at least
                  k_ell-floor(2(q+1)/3)
                incident edges not contained in V(P),
                then either
                (i) e is actually special; or
                (ii) H contains a nonspecial edge f with phi(f)>q; or
                (iii) q=ell-1 and V(P)=V(H).
                
                SPANNING-TOP(ell):
                Every P_ell-free linear 3-graph H on exactly 2ell-1 vertices with delta(H)>=k_ell is all-special.
                
                Then the dense-core all-special conjecture holds for every ell.
                
                Moreover, by e6d318739fde, EAR-TO-PROGRESS is invoked only with exactly the amount of external attachment guaranteed inductively; no stronger ambient density statement is needed. Thus the grand conjecture reduces inductively to converting a quantitatively forced family of clean ears/one-contact chords into rank progress, plus the spanning top-rank base geometry.

              • [1000268] Spanning top-rank induction works after one vertex deletion in two residue classes
                  STATEMENT
                  Assume the dense-core all-special conjecture is true for forbidden length ell-1. Let H be a P_ell-free linear 3-graph on exactly 2ell-1 vertices with
                    delta(H)>=k_ell:=floor(2ell/3)+1.
                  Then for every vertex w,
                    H-w
                  is automatically P_{ell-1}-free and has minimum degree at least k_ell-1=floor(2ell/3).
                  
                  If ell is congruent to 0 or 2 modulo 3, then
                    floor(2ell/3) >= floor(2(ell-1)/3)+1,
                  so H-w lies above the dense-core threshold for ell-1. Consequently every edge of H-w is special.
                  
                  If ell is congruent to 1 modulo 3, this implication misses by exactly one:
                    floor(2ell/3)=floor(2(ell-1)/3),
                  whereas the strict ell-1 threshold is one larger.
                  
                  Thus, under induction, a spanning top-rank counterexample can only retain genuinely nontrivial deletion structure in the residue class ell≡1 mod 3; in the other two residue classes every single-vertex deletion is all-special.

                • [1000464] Two-hole alternate paths have an exact alternating blocker-matching defect identity
                    STATEMENT
                    Let H be a linear 3-uniform hypergraph on 2ell-1 vertices, and let Q be an (ell-2)-edge linear path. Write V(H)\V(Q)={a,b}. For h in {a,b}, let epsilon be 1 if there is an edge {a,b,w} for some w in V(Q), and 0 otherwise. Then epsilon is well-defined and common to both holes.
                    
                    For each h in {a,b}, every edge through h other than the possible common edge {a,b,w} has its other two vertices in V(Q). These blocker pairs form a matching M_h on V(Q), with
                      |M_h|=d_H(h)-epsilon.
                    Moreover M_a and M_b are edge-disjoint.
                    
                    Let N=|V(Q)|=2ell-3, let U_h be the number of vertices of V(Q) unmatched by M_h, and let p be the number of path components of M_a union M_b, counting isolated vertices as path components. Then
                      U_h = N-2d_H(h)+2epsilon
                    and
                      U_a+U_b=2p.
                    Equivalently,
                      p = N-d_H(a)-d_H(b)+2epsilon
                        = 2ell-3-d_H(a)-d_H(b)+2epsilon.
                    
                    In particular, if delta(H)>=floor(2ell/3)+1, then
                      p <= 2ell-5-2floor(2ell/3)+2epsilon
                    and hence p<=2ell-3-2floor(2ell/3).

                • [1000705] Critical residue deletions either give two-hole witnesses or fall exactly onto equality
                    STATEMENT
                    Assume the dense-core all-special conjecture is true for forbidden length ell-1, and let ell=3m+1. Let H be a P_ell-free linear 3-graph on 2ell-1=6m+1 vertices with minimum degree at least 2m+1. Let
                      P=(g_1,...,g_{ell-2},e)
                    be a spanning (ell-1)-edge path ending in a nonspecial edge e, and let a be either free vertex of g_1.
                    
                    Then H-a is P_{ell-1}-free, e has rank ell-2 in H-a, and exactly one of the following holds:
                    
                    (A) e is special in H-a. Then H-a supplies an alternate wrong-entrance (ell-2)-edge path Q_a ending in e, hence the same two-hole witness structure as in the good residue classes.
                    
                    (B) e is nonspecial in H-a. Then
                      delta(H-a)=2m.
                    Consequently delta(H)=2m+1, and there exists a vertex v_a!=a with
                      d_H(v_a)=2m+1,
                      d_{H-a}(v_a)=2m,
                    such that a and v_a lie together in an edge of H.
                    
                    Thus the residue ell≡1 mod3 has no diffuse extra case: every failed deletion step lands exactly on the equality threshold and exposes a minimum-degree neighbor of the deleted hole.

              • [1001214] Good-residue two-hole witnesses force four large blocker matchings
                  STATEMENT
                  In the good residue classes, deleting either free first-edge vertex of a spanning top-rank core yields an alternate near-spanning wrong-entrance witness with exactly two holes. Its opposite endpoints have exact alternating blocker defects. For any such witness, the two endpoint blocker systems and the two hole blocker systems give four pairwise edge-disjoint matchings on the common interior set W, of sizes at least delta-3,delta-3,delta-4,delta-4. Hence their union has at least 4delta-14 edges; above the threshold equality cases this forces a vertex incident with blocker pairs from at least three distinct centers.

                • [1000564] Good-residue two-hole witnesses force linearly many three-center collisions
                    STATEMENT
                    In the setting of 7383e241bcce, let F be the union of the four pairwise edge-disjoint blocker matchings on W, and let T be the number of vertices w in W with d_F(w)>=3. Then
                      T >= |E(F)|-|W|.
                    
                    Consequently, at the dense-core threshold:
                    - if ell=3m, then T>=2m-4;
                    - if ell=3m+2, then T>=2m-4.
                    
                    Thus outside the small equality cases ell=6,8, every good-residue alternate witness contains not merely one but linearly many interior vertices incident with blocker pairs from at least three distinct centers among the two holes and two opposite endpoints.

                  • [1000820] An early endpoint blocker forces opposite-endpoint prefix escape
                      STATEMENT
                      Let Q=(p_1,...,p_s) be a linear path with first edge p_1={u,v,c}, where u,v are the two free opposite endpoints. Let f={u,r,w} be an edge different from p_1 whose two non-u vertices lie in V(Q)\p_1. Let i be the first index >=2 of a path edge containing either r or w. Then
                        C=(p_1,p_2,...,p_i,f)
                      is a linear cycle of length i+1.
                      
                      Assume moreover that H has minimum degree at least delta. At the private cycle vertex v of p_1, classify edges h!=p_1 by the number 0,1,2 of vertices of h\{v} lying in V(C), and call the counts C_0,C_1,C_2. Then
                        2C_0+C_1 >= 2delta-2i-1.
                      
                      In particular, if i<=delta-2, at least three weighted units of the v-star escape the prefix cycle. In a two-hole wrong-entrance witness, every such escaping v-edge is a single/double blocker on the full path Q whose blocker set is not wholly contained in V(C); thus an early u-blocker quantitatively forces the opposite endpoint matching to send contacts beyond the same prefix.

                  • [1001219] Gap-three two-hole rotations force high-potential omitted vertices
                      STATEMENT
                      Let Q=(p_1,...,p_s) be an s-edge wrong-entrance path omitting exactly two vertices a,b, chosen so that sort(phi(a),phi(b)) is lexicographically maximal among such states. A two-hole collision spanning one omitted cell gives an (s+1)-edge wrong-entrance lift and is impossible. A gap-three collision instead rotates Q to another s-edge wrong-entrance two-hole state. If its cut is between p_i and p_{i+3}, then both current holes satisfy phi(a),phi(b)>=max{i,s-i-2}; in particular a cut within r cells of either end forces both hole potentials at least s-r-2.

                • [1000628] Good-residue witnesses contain linearly many genuine two-hole collisions
                    STATEMENT
                    In the two-hole wrong-entrance setting, the two hole-centered matchings N_a,N_b have at least 4delta-2ell-10 common covered vertices. At the dense-core threshold this is at least 2m-6 for ell=3m and also for ell=3m+2. Every such vertex w supports distinct hyperedges {a,w,r} and {b,w,t} with r!=t, i.e. exactly a genuine two-hole collision of the splice type.

            • [1000639] Low-degree endpoint in the fixed-edge rotation closure
                STATEMENT
                Let H be a finite linear 3-graph with global maximum path length L. Let e be a nonspecial edge with phi(e)=L and unique entrance x. Fix a globally longest path P ending in e through x, and let R(P,e,x) be the set of vertices that occur as an opposite last vertex of some globally longest path obtained from P by a sequence of length-preserving rotations that keep e as the last edge and keep x as its entrance. Then min_{v in R(P,e,x)} d_H(v) <= floor(2(L+1)/3).

            • [1000771] Matching deletions are exactly the minimum-degree-five deletions of STS(13)
                STATEMENT
                Let S be any Steiner triple system on 13 vertices, hence 6-regular. For a set M of deleted blocks, S\M has minimum degree at least 5 if and only if M is a matching. Moreover every such deletion is automatically P_7^(3)-free.

              • [1001013] Every matching deletion of cyclic STS(13) is all-special
                  STATEMENT
                  Let S be the cyclic STS(13) generated by the translates of {0,1,4} and {0,2,7}. For every matching M of blocks, S\M has minimum degree at least 5, is P_7^(3)-free, and every surviving edge is special of edge rank 6.

                • [1000054] Each cyclic STS(13) block orbit has matching number three
                    STATEMENT
                    Let O_1={A_i:i in Z_13} and O_2={B_i:i in Z_13}, where A_i={i,i+1,i+4} and B_i={i,i+2,i+7}. Then the largest matching contained in either O_1 or O_2 has size exactly 3.

                  • [1000170] Three-block matchings in each cyclic STS(13) orbit have two affine types
                      STATEMENT
                      Up to translation and the order-three multiplier automorphism stabilizing a block orbit, a three-block matching inside O_1 has exactly two types, represented by {A_0,A_2,A_7} and {A_0,A_2,A_8}. Likewise a three-block matching inside O_2 has exactly two types, represented by {B_0,B_1,B_4} and {B_0,B_1,B_10}.

                • [1000210] Three affine endpoint paths do not survive arbitrary matching deletions
                    STATEMENT
                    The three affine-stabilizer spanning paths used to prove specialness of A_0={0,1,4} in the full cyclic STS(13) are not robust enough by themselves to prove specialness under matching deletions: the disjoint blocks A_6 and A_11 hit all three.

                • [1001142] Matching deletions of cyclic STS(13) preserve rank six at every surviving block
                    STATEMENT
                    Let S be the cyclic STS(13) generated by the translates of {0,1,4} and {0,2,7}. If M is any matching of blocks, then every block e of S\M has edge rank φ(e)=6.

                  • [1000980] Matching-deletion specialness reduces to two exceptional blocker-pair types per block orbit
                      STATEMENT
                      For a surviving block e in a matching deletion of cyclic STS(13), the six explicit rank-six endpoint paths from fb007f7c4b89 already exhibit two distinct entrance labels unless the deleted matching contains one of two stabilizer-orbits of exceptional disjoint same-orbit block pairs.

            • [1000535] Global nonspecial-edge path-length inequality
                STATEMENT
                Let H be a finite linear 3-graph with minimum degree δ and global maximum linear-path length L. If H contains a nonspecial edge, then 3δ<=2L+2. Equivalently L>=ceil((3δ-2)/2).

              • [1000963] High terminal degree forces outside single-blocker expansion
                  STATEMENT
                  Let P be a globally longest L-edge path ending in a maximum-rank nonspecial edge e, and let v be a terminal vertex of e. If S_v is the number of incident terminal edges that meet the precursor in exactly one vertex, then S_v>=2d(v)-2L and S_v<=|V(H)\\V(P)|. Hence d(v)<=L+|V(H)\\V(P)|/2. For the two terminals y,z, S_y+S_z>=2d(y)+2d(z)-4L>=4delta(H)-4L.

            • [1000973] Star obstruction to unrestricted all-specialness
                STATEMENT
                A linear 3-uniform star with at least two edges has no special edges.

            • [1001152] Minimal-counterexample minimum-degree reduction
                STATEMENT
                Let d>=0 and let P be any hereditary property of finite hypergraphs. To prove |E(H)|<=d|V(H)| for all H with property P, it is enough to prove it for H with minimum degree δ(H)>d. Equivalently, every smallest counterexample to the inequality has δ(H)>d.

            • [1000318] Local degree bound on a nonspecial edge is false
                STATEMENT
                It is false that every nonspecial edge e must contain a vertex of degree at most floor(2(phi(e)+1)/3).

              • [1000829] Human counterexample at the 2/3 equality threshold
                  STATEMENT
                  There is an 11-vertex linear 3-graph H with minimum degree 4 and no P_6^(3) containing a globally maximum-rank nonspecial edge e of rank 5 whose three vertices all have degree 5. Thus the maximum-rank local degree conjecture is false, and equality delta=2ell/3 cannot suffice in the dense-core all-special conjecture at ell=6.

            • [1000550] Minimum-degree all-special transfer by peeling
                STATEMENT
                Fix ell>=2 and an integer k>=0. Suppose every P_ell^(3)-free linear 3-graph with minimum degree at least k+1 has all edges special. Then ex_L(n,P_ell^(3)) <= max{k,(2ell-3)/3} n. In particular, the dense-core all-special conjecture with k=floor(2ell/3) implies ex_L(n,P_ell^(3))<=floor(2ell/3)n.

            • [1000353] Generalize the P4 special-edge lemma to dense cores
                STATEMENT
                Try to prove the dense-core all-special conjecture by generalizing the source P4 special-edge mechanism: a nonspecial edge together with minimum degree >2ell/3 should force enough distinct path attachments to create an alternative longest-path entrance label, hence make the edge special or create P_ell.

            • [1000109] Two-terminal rank ascent from a low-rank nonspecial edge
                STATEMENT
                Let e be a nonspecial edge of rank t in a linear 3-uniform hypergraph, with terminal vertices y,z. If d(y)>2t-1, then some edge f_y containing y has phi(f_y)>t; likewise for z. Hence if the minimum degree is delta and t<(delta+1)/2, then e has two distinct higher-rank neighbors, one through each terminal.

            • [1000516] Refuted: maximum-rank nonspecial edge degree conjecture
                STATEMENT
                Refuted. A globally maximum-rank nonspecial edge need not contain a vertex of degree at most floor(2(L+1)/3). The certified counterexample bab307b92caa has maximum path length L=5 and maximum-rank nonspecial edges all of whose vertices have degree 5>4.

              • [1000247] Clean entrance replacements stay at maximum rank
                  STATEMENT
                  Let H be a linear 3-graph, let e be a nonspecial edge of globally maximum rank L with unique entrance x, and let P=(e_1,...,e_{L-1},e) be a globally longest path entering e through x=e_{L-1}∩e. Let f≠e contain x and suppose f meets V(P) only at x. Then φ(f)=L. Moreover, if f is nonspecial, its unique entrance is also x.

              • [1000437] Nonspeciality need not propagate to maximum path rank
                  STATEMENT
                  A linear 3-graph may contain nonspecial edges even though every globally maximum-rank edge is special.

            • [1000525] Refuted: opposite-end 2/3 degree bound for longest paths ending in a nonspecial edge
                STATEMENT
                Refuted, even after weakening 'every longest path' to 'there exists a longest path'. The explicit counterexample 1d151c5db254 has global maximum path length L=6 and a maximum-rank nonspecial edge with exactly one longest path ending at it; both free opposite-end vertices have degree 5>4=floor(2(L+1)/3).

              • [1001148] Every opposite-end single blocker is a safe rotation of the fixed nonspecial last edge
                  STATEMENT
                  Let P=(g_1,...,g_L) be a globally longest linear path whose last edge e=g_L is nonspecial with unique entrance x=g_{L-1}∩e. Let a be either vertex of g_1\g_2. If f≠g_1 is an edge through a with exactly one blocker vertex w∈V(P)\g_1, then there is another globally longest L-edge path P' whose last edge is still e. Moreover P' enters e through x. In particular w cannot be either terminal vertex of e.

              • [1000920] Opposite-end degree bound proves the maximum-rank-nonspecial branch of 3δ≤2L+2
                  STATEMENT
                  Assume the opposite-end degree conjecture. If H has minimum degree δ, global maximum path length L, and contains a nonspecial edge e with φ(e)=L, then 3δ<=2L+2.

              • [1000003] Maximum-rank nonspecial edge can have no low-degree opposite endpoint
                  STATEMENT
                  The opposite-end degree conjecture 75e5875cac45 is false. There is a 9-vertex, 8-edge linear 3-graph of global maximum path length L=3 with a globally maximum-rank nonspecial edge e such that, for every longest path ending in e, both last vertices at the opposite end have degree 3>floor(2(L+1)/3)=2.

              • [1000129] Opposite-end degree bound fails even existentially
                  STATEMENT
                  The opposite-end degree conjecture 75e5875cac45 is false even in the existential sense. There is a 13-vertex linear 3-graph with global maximum path length L=6 and a globally maximum-rank nonspecial edge e={0,3,8} having exactly one longest path ending at e; the two free vertices at the opposite end of that path both have degree 5, whereas floor(2(L+1)/3)=4.

          • [1000357] Minimum-degree local ascending-neighbor bound
              STATEMENT
              Let H be a P_ell^(3)-free linear 3-graph with minimum degree δ(H)>=floor(2ell/3)+1. Fix v∈V(H). Then there are at most three ascending nonspecial edges e={x,v,u} for which v is a last vertex and φ(u)>=φ(v).

            • [1001030] Minimum degree forces ascending edges to have large φ
                STATEMENT
                Let H be a finite linear 3-graph with minimum degree δ. If e is an ascending nonspecial edge, then φ(e)>=ceil((δ+3)/2).

            • [1000959] Refuted: minimum degree four does not eliminate ascending nonspecial edges
                STATEMENT
                Refuted. Minimum degree 4 does not force ascending nonspecial edges to disappear. The family 7564e287447b has δ=4 and contains an ascending nonspecial edge for every L>=2.

              • [1000524] Affine-plane boosters preserve an ascending edge at minimum degree four
                  STATEMENT
                  For every L>=2 there is a finite linear 3-graph H_L with minimum degree 4 containing an ascending nonspecial edge. In fact H_L has a distinguished edge e with φ(e)=L+3 and unique entrance x satisfying φ(x)=L+2.

            • [1001105] Minimum degree forces ascending edges to have large φ
                STATEMENT
                Let H be a finite linear 3-graph with minimum degree δ. If e is an ascending nonspecial edge, then φ(e)>=ceil((δ+3)/2).

            • [1000681] Minimum-degree local bound implies the 2/3 upper bound
                STATEMENT
                Assume the minimum-degree local ascending-neighbor bound 4e1c498f922a holds for a fixed ell. Then every P_ell^(3)-free linear 3-graph H satisfies |E(H)|<=(2ell/3)|V(H)|.

          • [1000336] Sharp minimum-degree lower bound conjecture for ascending edges
              STATEMENT
              Let H be a finite linear 3-graph with minimum degree δ. If e is an ascending nonspecial edge, then φ(e)>=δ+1.

            • [1000047] Saturated boundary fans are degree-two cell graphs with rigid adjacent-cell blockers
                STATEMENT
                In a saturated boundary fan, the two-vertex cells C_i=g_i minus g_{i-1} support a degree-two multigraph: double blockers join distinct cells, singleton blockers are labeled half-edges, and in the S=3 case the unique unused blocker is an extra half-edge. Thus the fan is cycles plus one or two open paths pairing the defects. Under the no-safe-rotation hypothesis, an adjacent-cell double blocker joining C_i to C_{i+1} is impossible at the final pair, and otherwise must use the forward joint g_{i+1}∩g_{i+2} in its later cell.

            • [1000060] Switch cycles force rank-q common-entrance escape structure
                STATEMENT
                In the boundary fixed-target entrance rotation graph, a terminal-label switch occurs exactly when the rotating edge blocks at the opposite terminal sigma(P). Such a switch closes the current entrance path into a linear q-cycle C=(g_1,...,g_{q-2},f,h) in which the fixed target edge f={x,y,z} has cycle joints y,z and private entrance x.
                
                For any edge a!=f through x with at most one additional vertex on C, if a is cycle-clean or its unique extra contact is the private vertex of either cycle neighbor of f, then phi(a)>=q. Since phi(x)=q-1 forces every edge through x to have rank at most q, every such favorable ear has rank exactly q and is either special or ascending nonspecial with unique entrance x.
                
                Moreover, among edges through x other than f, if C_0,S,D count those with respectively 0,1,2 non-x contacts on the q-1 edge path C-h, then 2C_0+S>=2. Hence every switch cycle exposes either a clean favorable rank-q ear or at least two distinct one-contact ears; neighboring-private one-contact ears are favorable in the same sense.

            • [1000101] Single blockers give endpoint-preserving rotations, safe below the boundary
                STATEMENT
                A single-blocking edge whose blocker w is not the fixed last vertex x gives a length-preserving rotation of a path that still ends at x. Consequently, if e={x,y,z} is ascending nonspecial of rank q and q<=delta-1, then every (q-1)-edge x-ending entrance path avoiding y,z admits a nontrivial single-blocker rotation to another (q-1)-edge x-ending path still avoiding y,z.

              • [1000431] Rank deficiency forces high degree in the fixed-entrance rotation graph
                  STATEMENT
                  Let H have minimum degree delta, and let e={x,y,z} be an ascending nonspecial edge of rank q=phi(e) with q<=delta-1. Fix a (q-1)-edge path Q ending at x and avoiding y,z. In the graph whose states are such (q-1)-edge x-ending paths avoiding y,z and whose edges are endpoint-preserving safe single-blocker rotations, Q has at least 4(delta-q)-2 distinct neighbors.

              • [1001036] Saturated blocker fan at the boundary q=δ
                  STATEMENT
                  Let H have minimum degree δ and let e={x,y,z} be an ascending nonspecial edge with q=φ(e)=δ. Let Q be a (q-1)-edge path ending at x and avoiding y,z, and let a be its opposite last vertex. If Q has no safe single-blocker rotation avoiding y,z, then d_H(a)=q. Moreover the number S of single-blocking edges through a besides the first edge of Q is 2 or 3, every such edge is exceptional (its blocker is x or it contains y or z), the number of double-blocking edges is D=q-1-S, and the blocker vertices used by these edges leave exactly S-2 vertices of V(Q)\g_1 unused.

                • [1000132] Index-graph normal form for a saturated boundary fan
                    STATEMENT
                    In the exact saturated-fan setting of 29164b69be06, put t=q-1 and for each i=2,...,t let A_i=g_i\V(g_1∪...∪g_{i-1}); then |A_i|=2 and the A_i partition V(Q)\g_1. Form a loopless multigraph J on indices {2,...,t} by adding, for each double-blocking edge through a, an edge ij when its two blocker vertices lie in A_i and A_j. Then Δ(J)<=2. If S=2, J has q-2 vertices and q-3 edges and therefore exactly one path component, all other components being cycles. If S=3, J has q-2 vertices and q-4 edges and therefore exactly two path components (isolated vertices counted as path components), all other components being cycles.

                • [1001185] Saturated-fan continuation
                    STATEMENT
                    Route bridge: the boundary saturated-fan analysis continues after toolkit lemma 1000187.

                  • [1000784] Exceptional Y/Z single blockers cannot occupy the final cell
                      STATEMENT
                      In the saturated boundary setting q=δ with ascending nonspecial e={x,y,z}, maximum entrance path Q=(g_1,...,g_{q-1}), and no safe rotation, a Y-type or Z-type exceptional single blocker cannot use a blocker vertex in the final cell C_{q-1}=g_{q-1}\g_{q-2}.

            • [1000232] Fixed-hole one-contact chords either bridge or collapse to one two-edge window
                STATEMENT
                For a path P ending at x and an outside fixed hole b with at least three one-contact external b-chords, either two chords satisfy the corrected bridge criterion, or all contacts other than x lie in two consecutive path edges. Consequently, in the canonical loss-one two-cycle the fixed-hole escape problem reduces to: an edge disjoint from the rotated path, a corrected two-chord bridge, or a single two-edge contact window containing all non-x one-contact chords.

              • [1000218] An external fixed-hole edge through the alternate hole restores full length
                  STATEMENT
                  In the canonical loss-one two-cycle notation, let Q=(g_1,...,g_t), t=q-1, with g_1={a,a',c_1}, let the loss-one blocker be h={a,u,b_{i+2}}, and let b=b_{i+1} be the fixed hole of P_0,P_1. Let f be an edge through b which is disjoint from V(P_1) and suppose f contains a', the second vertex omitted from P_1. Then H contains a (q-1)-edge path ending at x and avoiding y,z, namely g_t,g_{t-1},...,g_{i+2},g_{i+1},f,g_1,g_2,...,g_{i-1}.

              • [1000716] Fixed-hole window state for the final loss-one obstruction
                  STATEMENT
                  For a loss-one x-ending state P in the boundary q=delta analysis, retain the fixed omitted vertex b together with the minimal two-edge interval I(P,b) containing all non-x one-contact external chords through b whenever no corrected two-chord bridge exists. Seek a canonical move that either increases the path length, changes the fixed hole, or moves I(P,b) monotonically toward an endpoint. A closed state walk with unchanged hole and window should force repeated use of the same path vertices by distinct b-edges or by the omitted two-contact edge, contradicting linearity.

            • [1000316] Terminal defect accounting and opposite-terminal splice dichotomy
                STATEMENT
                In the setting of the two-terminal alternating blocker system of 765d552ff81d, for each terminal v in {y,z}, 2L-2-2B_v=S_v+U_v and 2d_H(v)=2L+S_v-U_v; hence S_y+S_z+U_y+U_z=2p and d_H(y)+d_H(z)=2L+S_y+S_z-p, where p is the number of alternating path components. Moreover, for opposite-terminal single blockers f_y,f_z with first/last blocker positions j<k<=L-2: if they intersect then f_y,e,f_z form a linear 3-cycle; if disjoint and k>=j+2 there is an exact bridge splice of length L+2-(k-j); if disjoint and k=j+1 then at least one blocker is the joint g_j∩g_{j+1}.

            • [1000362] Maximum-rank nonspecial edges have a three-color blocker system with terminal-pair control on clean replacements
                STATEMENT
                Let P=(g_1,...,g_{L-1},e) be globally longest with nonspecial e={x,y,z} entered through x, and W=V(P) minus e. The double blockers through x,y,z form three pairwise edge-disjoint matchings on W. At terminal vertices y,z every other incident edge is blocking on W. At entrance x, clean replacements may occur; every such clean edge has rank L, and if it is special then every alternate-entrance longest witness for it meets the fixed terminal pair {y,z}.

            • [1000401] Type-B alternate break forces a nonlocal blocker or terminal theta
                STATEMENT
                In loss-one sink case (B), let P=(p_1,...,p_s), s=q-2, end at x with opposite last vertex a, and let h_x be the mandatory x-type singleton blocker. Then C=(p_1,...,p_s,h_x) is a linear cycle of length q-1. Deleting p_s yields a canonical second x-ending path P^*=(p_{s-1},...,p_1,h_x).
                
                Write A_s={b_s,x} and A_{s-1}={b_{s-1},c_{s-1}} with c_{s-1}=p_{s-1}∩p_s. If neither last vertex of A_{s-1} admits a safe single-blocker rotation on P^*, then the unique double blocker through a containing b_s pairs b_s with a blocker in some cell A_j with j<=s-2.
                
                Moreover, at c=c_{s-1}, the deleted edge p_s={c,b_s,x} is itself an x-type single blocker relative to P^*. Hence if c is a safe sink, its deficiency-two normal form cannot be the perfect-double-matching type. In that case c has a clean edge f through one of the terminals y,z of e={x,y,z}, and P^*, p_s, and f,e form three internally disjoint c-to-x branches of lengths q-2,1,2. Thus their union is a theta containing linear cycles of lengths q-1, q, and 3.

            • [1000460] Far-end deletion forces motion, rank progress, or a flat terminal adjacency
                STATEMENT
                For a boundary ascending nonspecial edge e={x,y,z} of rank q=delta, delete the far first edge of a canonical (q-1)-edge x-ending entrance path. At the new opposite endpoint either a safe clean extension exists, a safe single-blocker rotation exists, or there is a terminal-clean edge f through y or z that is special or has rank at least q. If the latter f is nonspecial, ascending, and has rank exactly q, then its shared terminal v in {y,z} is also a terminal of f; hence every rank-flat ascending transfer is an adjacency in the ascending terminal-pair graph.

              • [1000469] A terminal-clean boundary transfer closes a q-cycle
                  STATEMENT
                  In the setting of 5ca3b62fde96, suppose the transfer alternative occurs through terminal y: the deficiency-two path is R=(g_2,...,g_{q-1}) and f is an edge through b_2 and y that is clean relative to R. Then g_2,g_3,...,g_{q-1},e,f is a linear cycle of length q. If moreover f is nonspecial ascending of rank q, then e and f are equal-rank terminal-adjacent ascending edges, and on the (q-1)-edge path g_2,...,g_{q-1},e the edge f has exactly two contacts, b_2 in the first edge and y in the last edge. Thus f realizes equality in the terminal successive-contact separation bound.

                • [1000597] Every private vertex of a minimum-degree cycle has a mobile ear
                    STATEMENT
                    Let C=(e_1,...,e_q) be a linear q-cycle in a linear 3-graph H with minimum degree at least q. For each i let p_i be the private vertex of e_i, i.e. the unique vertex of e_i not used in the two cycle intersections. Then there is an edge f_i != e_i through p_i having at most one additional vertex on V(C). More quantitatively, if C_0(i),C_1(i),C_2(i) count the noncycle edges through p_i having respectively 0,1,2 other vertices on V(C), then 2C_0(i)+C_1(i)>=1.

                • [1001111] Flat-transfer cycle chain as the residual boundary obstruction
                    STATEMENT
                    Iterate the transfer alternative from 5ca3b62fde96 on boundary ascending nonspecial edges. Order states lexicographically by edge rank and then entrance-vertex potential. Any transfer to larger rank is strict progress; at fixed rank q, any nonascending transfer has entrance potential at least q and therefore rises above the source ascending entrance potential q-1. Hence a closed transfer chain can consist only of ascending nonspecial rank-q edges. By 321866bdcbef each such transfer is a terminal adjacency, and by 68606ec8e860 each step lies on a linear q-cycle and realizes equality in terminal contact spacing. The remaining hard case is therefore a chain or cycle of equal-rank ascending terminal edges glued by these extremal q-cycles.

              • [1000504] Flat transfers carry a one-edge blocker memory into the next longest witness
                  STATEMENT
                  Let e={x,y,z} and f be equal-rank q nonspecial edges arising in a flat transfer e to f through their common terminal y, with e ascending and unique entrance x. Then every q-edge longest path P ending in f with last vertex y has, among the final q-2 precursor edges before f, a vertex from {x,z}. Equivalently the previous edge e must reappear in the tail of every such next-state witness through one of its two nonshared vertices.

            • [1000481] Minimum degree gives an endpoint-potential floor and a stronger ascending-edge rank floor
                STATEMENT
                Let H be a finite linear 3-graph of minimum degree delta. Every vertex v satisfies
                  phi(v)>=ceil((delta+1)/2).
                Consequently every ascending nonspecial edge e with unique entrance x satisfies
                  phi(e)>=ceil((delta+3)/2).

            • [1000520] Loss-one sinks have saturated index graphs forcing a nonlocal blocker or lossless rotation
                STATEMENT
                In the boundary setting q=delta, suppose a loss-one x-ending path P' of length q-2 avoiding y,z has opposite endpoint a' with neither a safe clean extension nor a safe single-blocker rotation.
                
                Then d_H(a')=q and the endpoint fan is exactly saturated. In Type A with no singleton blocker, the double blockers use every blocker vertex; in Type A with one singleton, that singleton is x-type and exactly one blocker vertex is uncovered; in Type B, the two singleton blockers and the double blockers partition all blocker vertices.
                
                Partition V(P')p_1 into the standard two-vertex cells A_i and form the double-blocker index graph J on the cells. Then Delta(J)<=2. In Type A with no singleton, J is a union of cycles; in the other two cases J is a union of cycles plus one path component, with endpoint defects exactly the singleton/uncovered blocker incidences.
                
                If no double blocker gives a length-preserving splice, then J must contain a nonlocal edge joining A_i,A_j with |i-j|>=2. Equivalently, every loss-one sink exposes either a lossless double-blocker rotation or a nonlocal double blocker.

            • [1000667] Open-chain defects and their ordered locations in saturated boundary fans
                STATEMENT
                In the saturated boundary-fan index graph J, the deficit 2-d_J(i) of a cell A_i is exactly the number of its vertices not used by double blockers. Hence open path-component endpoints are precisely the singleton-blocker defects together with the unique uncovered blocker when present. Moreover an X-type singleton defect lies in the final cell A_{q-1}, whereas Y- and Z-type singleton defects lie strictly earlier.

            • [1000673] A loss-one two-cycle has a fixed hole with unavoidable external attachment surplus
                STATEMENT
                In the canonical loss-one double-blocker two-cycle, both rotated states omit the same path vertex b_{i+1}; their second omitted vertices differ. This fixed hole b has at least two neighbor incidences outside the original path. Hence either one edge through b is otherwise disjoint from the original path, or at least two distinct b-edges are one-contact external chords.

              • [1001208] Fixed-hole continuation
                  STATEMENT
                  Route bridge: the fixed-hole analysis continues after toolkit lemma 1000432.

                • [1000644] Exact deficiency equation at the fixed hole
                    STATEMENT
                    In the canonical loss-one two-cycle setting, let P be the rotated x-ending path of length q-2, let b be the fixed omitted vertex, and let g be the original path edge through b, whose other two vertices both lie on P. Among edges through b other than g, let C,R,D count those having respectively 0,1,2 non-b vertices on V(P). Then C+R+D=d_H(b)-1>=q-1, R+2D<=2q-5, and hence 2C+R>=3. If equality 2C+R=3 holds, then d_H(b)=q, every path vertex allowed by linearity is used by exactly one b-edge, and exactly one of the following occurs: (i) C=0,R=3,D=q-4; (ii) C=1,R=1,D=q-3.

              • [1001121] Two fixed-hole one-contact chords give an exact bridge splice
                  STATEMENT
                  Let P=(p_1,...,p_s) be a linear 3-uniform path ending at x, and let b notin V(P). Let f_1,f_2 be distinct edges through b such that f_r meets V(P) in exactly one vertex w_r, and its third vertex lies outside V(P)∪{b}. Assume w_2≠x. Let j be the first index of a path edge containing w_1, and let k be the last index of a path edge containing w_2. If j+2<=k, then (p_1,...,p_j,f_1,f_2,p_k,...,p_s) is a linear path ending at x of length s+3-(k-j). In particular, if s=q-2 and k-j=2, this produces a (q-1)-edge path ending at x.

                • [1000943] Corrected fixed-hole two-chord bridge
                    STATEMENT
                    Let P=(p_1,...,p_s) be a linear 3-graph path with last vertex x, and let b notin V(P). Let f_1,f_2 be distinct edges through b such that each f_r meets V(P) in exactly one vertex w_r and its third vertex lies outside V(P) union {b}. Let j be the first index of a path edge containing w_1 and k the last index of a path edge containing w_2. Assume j+2<=k and w_2!=x. Then (p_1,...,p_j,f_1,f_2,p_k,...,p_s) is a linear path with last vertex x and length s+3-(k-j). In particular, if s=q-2 and k-j=2, this is a (q-1)-edge path ending at x.

            • [1000749] A flat transfer cycle has no clean second-private ear and forces a target-preserving maximum rotation
                STATEMENT
                In an entrance-joint equal-rank flat-transfer q-cycle C=(h_1,...,h_{q-2},e,f), let x=f∩h_1 be the unique entrance of target f and let p be the private vertex of h_2. No noncycle edge through p is clean relative to C. In minimum degree q, p therefore has a one-contact ear; relative to P=(h_2,...,h_{q-2},e,f), it in fact has at least two single blockers, one with blocker different from x. Such a blocker gives a nontrivial (q-1)-edge maximum x-ending rotation that still ends with f.

              • [1000468] Boundary entrance-path rotation graph has no sinks
                  STATEMENT
                  Let H be a finite linear 3-graph with minimum degree at least q, and let f be an ascending nonspecial edge of rank q with unique entrance x, so phi(x)=q-1. Let S(f,x) be the finite set of (q-1)-edge linear paths P that have last vertex x and have f as their last edge. For every P in S(f,x), there is a distinct P_prime in S(f,x) obtained by a single-blocker endpoint-preserving rotation. Consequently the directed rotation graph on S(f,x), with all such rotations as arcs, has positive outdegree at every state and therefore contains a directed cycle.

            • [1000785] Local structure and escape in the boundary fixed-target rotation graph
                STATEMENT
                In the setting of 68593c300c9c, let G(f,x) be the undirected graph whose vertices are the (q-1)-edge paths ending at x with last edge f, with two states adjacent when one is obtained from the other by an endpoint-preserving single-blocker rotation.
                
                (1) Every rotation has a canonical inverse. Every state has degree at least two, and after traversing any rotation edge there is a noninverse rotation available from the other free opposite endpoint.
                
                (2) Every triangle in G(f,x) has one common exchanged path edge, necessarily g_2. Writing g_1={a,b,c} with c=g_1∩g_2, d=g_2∩g_3, and p for the private vertex of g_3, its two alternative states have the form (g_1,h_a,g_3,...,g_t) and (g_1,h_b,g_3,...,g_t), where h_a contains a and one of {d,p}, h_b contains b and one of {d,p}, and each new edge has its third vertex outside the original path. Conversely such a linear configuration gives the corresponding rotation triangle. No such triangle is a connected component: it has a noninverse exit outside the triangle, with the analogous exit forced on each endpoint side.
                
                (3) Every chordless 4-cycle is supported in the first four path positions. From any base state P_0=(g_1,...,g_t), if its two incident square rotations delete g_i and g_j with i<j, then (i,j) is one of (1,2),(1,3),(2,3),(2,4); hence all four states share the tail g_5,...,g_t when t>=5. No such square is a connected component: at least one state has a non-x single-blocker rotation outside the square, and in pivot types (2,3) and (2,4) the blocker-universe argument forces the corresponding exit on each endpoint side.

            • [1001068] Deficiency-two sink fans form alternating blocker systems with defects pinned at x
                STATEMENT
                Let H be a linear 3-graph of minimum degree q, let P=(p_1,...,p_{q-2}) be a linear path ending at x, let u,v be the two opposite last vertices of p_1, and let y,z lie outside V(P). Suppose both u and v are safe sinks: neither admits a safe clean extension avoiding y,z nor a safe single-blocker rotation avoiding y,z.
                
                For each sink r in {u,v}, its endpoint fan has degree exactly q and exactly one of three forms:
                (i) C=1,S=2,D=q-4, with one X-type singleton and one singleton through the other terminal;
                (ii) C=2,S=0,D=q-3, with clean y- and z-edges;
                (iii) C=2,S=1,D=q-4, with clean y- and z-edges and one X-type singleton.
                
                Let W=V(P)\p_1 and let M_r be the matching on W whose edges are the blocker pairs of double-blocking edges through r. Then M_u and M_v are edge-disjoint. Each M_r is either perfect, or has exactly two unmatched vertices, one of which is x. Hence M_u union M_v is a disjoint union of alternating cycles together with at most one nontrivial alternating path after the common x-defect is accounted for:
                - if both matchings are perfect, only cycles occur;
                - if exactly one is imperfect, there is one alternating path from x to its secondary defect;
                - if both are imperfect, x is isolated and there is at most one alternating path joining the two secondary defects.

            • [1001080] Saturated boundary fans force a nonlocal blocker
                STATEMENT
                Let H have minimum degree delta=q>=5, let e={x,y,z} be an ascending nonspecial edge of rank q, and let Q=(g_1,...,g_t), t=q-1, be a canonical maximum x-ending path avoiding y,z. For a double blocker through an opposite endpoint a with blockers in A_i,A_j, the exact splice loss is j-i-1 when the later blocker is private and j-i when it is the forward joint; length is preserved exactly for consecutive private-private blockers {a,b_i,b_{i+1}}. If a saturated endpoint fan has only consecutive double blockers and no safe single rotation or length-preserving double splice, then S=2 is impossible and S=3 has one rigid ladder with only the final adjacency missing. Consequently, if both opposite endpoints a,a' are sinks of this kind, at least one fan contains a nonlocal double blocker.

            • [1001130] Flat-transfer joint classification and entrance-to-entrance path
                STATEMENT
                Let e->f be an equal-rank ascending terminal-clean transfer of rank q. Let y=e∩f be the source-shared joint on the transfer q-cycle and let b be the other cycle joint of f.
                
                Then y is terminal for f. The joint b is the unique entrance x_f of f if and only if phi(b)=q-1; if b is instead the other terminal of f, then phi(b)>=q.
                
                In the entrance-joint case b=x_f, the deficiency-two precursor R=(g_2,...,g_{q-1}) is a (q-2)-edge linear path whose two last vertices can be chosen as x_f and the entrance x_e of e. Moreover R avoids both terminals of e and both terminals of f.

              • [1000947] All-entrance flat chains require labeled overlap, not generic two-path overlap
                  STATEMENT
                  In an all-entrance flat transfer chain, every step e_i->e_{i+1} supplies a (q-2)-edge path R_i between the consecutive entrance vertices x_i,x_{i+1}, with phi(x_i)=phi(x_{i+1})=q-1 and with R_i avoiding both terminal pairs. If R_i and R_{i+1} have no cross-intersections beyond their common entrance, they concatenate to a (2q-4)-edge linear path. However no generic bounded-cross-degree theorem can force a 3q/2-scale induced path when cross-intersections are present. A successful argument must use the additional blocker-memory: the preceding transfer edge is forced into the final q-2 tail of every longest witness for the next edge, together with entrance/terminal potential labels.

              • [1001122] First repetition in a flat transfer walk lifts to a labeled linear cycle
                  STATEMENT
                  Fix q>=2 and consider a walk in the threshold terminal graph R_q using rank-q ascending nonspecial hyperedges E_i={x_i,v_{i-1},v_i}, where x_i is the entrance color and phi(x_i)=q-1 while phi(v_j)>=q. Suppose we stop at the first repetition among the terminal vertices v_j and entrance colors x_i. Then the corresponding hyperedges contain a linear cycle. If the first repetition is a terminal vertex, the cycle is a rainbow cycle in R_q and every entrance x_i is private on the lifted hypergraph cycle. If the first repetition is an entrance color, the terminal-pair edges form a simple path and the first and last hyperedges close through the repeated entrance; that repeated entrance is the unique low-potential cycle joint and all other cycle joints are terminal vertices.

                • [1000014] Flat transfer triangles force all three entrances onto every rail
                    STATEMENT
                    Let e_1,e_2,e_3 be rank-q ascending nonspecial edges forming a flat terminal-transfer triangle: write e_i={x_i,v_{i-1},v_i} with indices modulo 3, and suppose each transfer e_i->e_{i+1} is of entrance-joint type. Let R_i be the associated (q-2)-edge entrance-to-entrance rail from x_i to x_{i+1} given by 932e2a9de86d. Then every rail R_i contains all three entrance vertices x_1,x_2,x_3.

                • [1000117] Every q-step flat transfer walk contains a labeled linear cycle
                    STATEMENT
                    Let H be a linear 3-graph and fix q. Any walk of q consecutive flat equal-rank-q ascending transfers contains, among its transfer hyperedges, a linear cycle of length at most q. The cycle is of one of the two types in f7c3ab40c059: either a terminal-cycle whose entrance labels are pairwise distinct private vertices, or a color-closure cycle with one low-potential entrance joint and all remaining joints terminal.

                • [1000445] Private-vertex ear surplus on a short linear cycle
                    STATEMENT
                    Let C be a linear cycle of c edges in a linear 3-graph H with minimum degree at least q. Let p be the private vertex of one cycle edge. Among edges f distinct from that cycle edge and containing p, let C_0,C_1,C_2 count those for which f minus {p} contains respectively 0,1,2 vertices of V(C). Then 2C_0+C_1 >= 2q-2c+1. In particular, if c<=q-1 then 2C_0+C_1>=3, and if c<=q-s then 2C_0+C_1>=2s+1.

            • [1000113] Single-blocker surplus below the conjectured ascending threshold
                STATEMENT
                Let H be a linear 3-graph of minimum degree δ, let x be a vertex, and let Q=(g_1,...,g_t) be a path of length t=φ(x) with last vertex x. Let z be a last vertex of g_1 at the opposite end. For f≠g_1 containing z, call f single-blocking if exactly one vertex of f\{z} lies in V(Q)\g_1, and double-blocking if both do. If S and D are their numbers, then S+D=d_H(z)-1 and S+2D<=2t-2. Hence S>=2(δ-t). In particular, if t<=δ-1 then S>=2.

              • [1000332] Refuted: consecutive private single blockers need not force an extension
                  STATEMENT
                  Refuted. Consecutive private single blockers can occur on a longest endpoint path; the explicit counterexample 2712f65b5d5e has a longest 3-edge x-ending path with such blockers in consecutive private slots p_2,p_3.

                • [1000462] Unsupported: proposed 4/7 minimum-degree floor for ascending edge rank
                    STATEMENT
                    Unsupported. The displayed 4/7 rank floor was derived using 47c17993cf60, which is false by the explicit counterexample 2712f65b5d5e. No independent proof of this 4/7 bound is currently supplied.

                • [1000180] Consecutive private single blockers can occur on a longest endpoint path
                    STATEMENT
                    The claim 47c17993cf60 is false. There is a linear 3-graph with a longest 3-edge path Q ending at x whose opposite endpoint a supports two single-blocking edges with blockers in consecutive private slots p_2,p_3.

              • [1000427] Endpoint deficiency pays for clean extensions and single rotations
                  STATEMENT
                  Let H be a linear 3-graph of minimum degree δ, and let P=(g_1,...,g_s) be any linear path with last vertex x. Let a be a last vertex of g_1 at the opposite end. Among edges f≠g_1 through a, let C be the number with no vertex of f\{a} in V(P)\g_1, let S be the number with exactly one such blocker vertex, and let D be the number with two. Then C+S+D=d_H(a)-1, S+2D<=2s-2, and consequently 2C+S>=2(d_H(a)-s)>=2(δ-s).

                • [1001202] Safe-sink continuation
                    STATEMENT
                    Route bridge: the boundary-rotation analysis continues after toolkit lemma 1000394.

                  • [1001177] Loss-one two-cycle continuation
                      STATEMENT
                      Route bridge: the boundary loss-one analysis continues using toolkit lemma 1000016.

                    • [1001039] Exact normal form for a deficiency-two safe sink
                        STATEMENT
                        Let H be a linear 3-graph of minimum degree δ, let P be an x-ending path of length s=δ-2, let a be an opposite last vertex, and let y,z lie outside P. Suppose there is neither a safe clean extension nor a safe single-blocker rotation at a. Then d_H(a)=δ. Writing C for clean edges through a other than the first path edge and S for single blockers, exactly one of the following holds: (i) C=1 and S=2, consisting of one clean Y- or Z-edge together with the X-single and the single of the opposite terminal type; (ii) C=2 and S=0, with one clean Y-edge and one clean Z-edge; (iii) C=2 and S=1, with clean Y and Z edges and the unique single blocker of type X. In cases (i) and (ii) the blocker sets saturate V(P) minus the first edge; in case (iii) exactly one blocker vertex is unused.

                • [1000928] A terminal-safe rotation state has endpoint deficiency at most three
                    STATEMENT
                    In the setting above, fix two vertices y,z not on P. Call a clean edge safe if it avoids y,z, so prepending it gives an (s+1)-edge path still ending at x and avoiding y,z. Call a single blocker safe if its blocker is not x and the edge avoids y,z, so the single-blocker rotation gives another s-edge path ending at x and avoiding y,z. If there is no safe clean edge and no safe single blocker at a, then δ-s<=3.

            • [1000527] Two-terminal double blockers form an alternating path-cycle system
                STATEMENT
                Let P=(g_1,...,g_{L-1},e) be a globally longest linear path in a linear 3-graph, where e={x,y,z} is nonspecial and g_{L-1}∩e={x}, so y,z are the two terminal vertices of e. Put W=V(P)\e, |W|=2L-2. For v∈{y,z}, let M_v consist of the unordered blocker pairs (f\{v})⊂W arising from edges f≠e through v whose two non-v vertices both lie in W. Then M_y and M_z are matchings on W, they are edge-disjoint, and M_y∪M_z is a simple graph of maximum degree at most two whose nontrivial components are alternating paths and even cycles. Moreover |M_v|=B_P(v). If p is the number of path components of M_y∪M_z, isolated vertices included, then p=(2L-2)-(B_P(y)+B_P(z)).

            • [1001117] Loss-one case A forms a terminal theta
                STATEMENT
                In loss-one sink case (A) of 87a6758ddc73, let P'=(p_1,...,p_{q-2}) be the x-ending path avoiding y,z with opposite last vertex a'. Let f_y and f_z be the two clean edges through a' containing y and z respectively, and let e={x,y,z}. Then P'∪{e,f_y} and P'∪{e,f_z} are linear cycles of length q, while {e,f_y,f_z} is a linear 3-cycle. Thus the union is a theta configuration consisting of the common long a'-to-e arc P' together with the two terminal branches f_y and f_z.

              • [1000374] Flat Type-A boundary sinks either branch through a common entrance or form a rainbow terminal triangle
                  STATEMENT
                  In loss-one sink case A at the boundary q=delta, let e={x,y,z} be the source ascending nonspecial edge of rank q, let a be the opposite endpoint of the deficiency-two path, and let f_y,f_z be the two clean terminal branches through {a,y} and {a,z}. Assume neither branch is special, both have rank q, and both are ascending. Then exactly one of the following holds. (i) phi(a)=q-1, and a is the common unique entrance of both f_y and f_z. (ii) phi(a)>=q, and a is terminal for both f_y and f_z; hence the terminal-pair edges of e,f_y,f_z form the triangle yz,ya,za. In case (ii) this triangle is rainbow in the threshold graph R_q: the three entrance colors are pairwise distinct and all have potential q-1.

              • [1000457] Unsafe clean terminal branches are special or do not drop rank
                  STATEMENT
                  Let e={x,y,z} be an ascending nonspecial edge of rank q, and let P=(p_1,...,p_{q-2}) be an x-ending path avoiding y,z. Let a be an opposite last vertex of p_1. Suppose f_y is an edge through a and y that is clean relative to P, meaning f_y meets V(P) only at a. Then phi(f_y)>=q-1. Moreover there are (q-1)-edge paths ending in f_y with two distinct entrance labels a and y. Consequently either f_y is special or phi(f_y)>=q. The analogous statement holds for a clean z-edge.

            • [1000204] Short-loss boundary sinks: loss two always escapes and loss one has exactly two exceptional forms
                STATEMENT
                In the boundary case q=delta, suppose a lossy double-blocker splice from a canonical entrance path produces an x-ending path avoiding y,z and the new opposite endpoint has no safe clean extension and no safe single-blocker rotation. Loss two is impossible. For loss one, exactly one of two forms remains: (A) two clean edges, one through y and one through z, with at most one single blocker, necessarily x-type; or (B) one clean edge through one terminal and exactly two single blockers, one x-type and one through the other terminal.

    • [1000446] Rainbow-shadow formulations for 3-uniform linear paths
        STATEMENT
        A dedicated research document for translating the 3-uniform linear-path problem into properly edge-colored graph problems. It records both the global A/B shadow reduction and the rank-layer ascending-edge formulation, together with two distinct minimum-degree normalizations: one in the original 3-uniform hypergraph and one in the derived properly edge-colored shadow graph.

      • [1000079] Longest directed paths force complementary source/rainbow endpoint degrees
          STATEMENT
          In the source-oriented setup above, suppose d_F(x)≥d for all x and let P=v_0v_1...v_p be a longest directed path in D. Then
          h(v_0)≤p,   s(v_0)≥d-p,
          s(v_p)≤p/2, h(v_p)≥d-p/2.

      • [1000381] Source-oriented triples force a 7/27-scale directed-or-rainbow path
          STATEMENT
          In the source-oriented setup on n vertices, assume every vertex lies in at least m/n triples. Then the associated properly edge-colored graph H contains a rainbow path of length q with
          q > 7m/(27n) - 14/9.
          Consequently the maximum of the longest directed path in the forced digraph D and the longest rainbow path in H exceeds the same bound.

      • [1000793] Ascending-edge directed paths lift through endpoint-potential growth
          STATEMENT
          Let H be a finite linear 3-graph with endpoint potential phi. For every ascending nonspecial edge e={x,u,v} with unique entrance x, orient two auxiliary arcs x->u and x->v. Then every auxiliary directed path x_0->x_1->...->x_p forces phi(x_p)>=phi(x_0)+p, and hence H contains a linear hypergraph path of length at least p. Thus the longest directed path in the ascending-edge orientation is a lower bound for the longest linear path in H.

        • [1000225] Potential superlevel cuts isolate ascending edges while retaining all special edges
            STATEMENT
            Let H be a finite linear 3-graph with endpoint potential phi. For t>=1 put
              V_t={v:phi(v)>=t}.
            Consider an edge e with rank q=phi(e)>=t.
            
            If q>t, then every vertex of e lies in V_t.
            
            If q=t, then exactly one of the following holds:
            (i) e is ascending nonspecial, with unique entrance x satisfying phi(x)=t-1; then e has exactly one vertex outside V_t (namely x) and its two terminal vertices lie in V_t;
            (ii) e is special or nonspecial nonascending; then all three vertices of e lie in V_t.
            
            Consequently, among all edges of rank at least t, the edges crossing the cut (V_t,V(H)\V_t) are exactly the ascending nonspecial edges of rank t, and every such crossing edge has type 1-outside/2-inside.

          • [1000698] Potential superlevel cuts are controlled by the exact induced-core density defect
              STATEMENT
              For every potential threshold t, let E_t=|E(H[V_t])| and xi_t=E_t-d|V_t|. Then
                A_t >= M_{>=t}-E_t
                    = M_{>=t}-d|V_t|-xi_t.
              If H is vertex-minimal for S_ell and V_t is proper, a nonnegative xi_t cannot be excluded by minimality alone: when H[V_t] contains a nonspecial edge, minimality instead guarantees a vertex of degree at most d inside that core; when the core is all-special, xi_t<0. Thus the earlier universal +1 boundary-flow term requires an additional induced-core deficit hypothesis.

            • [1000172] Potential cuts have an exact three-minus-one incidence count
                STATEMENT
                Let H be a finite linear 3-graph and, for t>=1, put V_t={v:phi(v)>=t}. Let M_{>=t} be the number of edges of rank at least t and A_t the number of ascending nonspecial edges of rank exactly t. Then the number I_t of incidences (v,e) with v in V_t and phi(e)>=t is exactly\nI_t=3M_{>=t}-A_t.\n\nIf t>=2, then for every v in V_t,\n#{e contains v: phi(e)>=t} >= d_H(v)-(2t-3),\nwith the right side interpreted as zero if negative. Hence, for t>=2,\nsum_{v in V_t} max{0,d_H(v)-2t+3}\n<=3M_{>=t}-A_t.

            • [1000197] Weighted potential-cut inequality for the exact-density layer
                STATEMENT
                Let ell>=4, d=floor(2ell/3), and let H be a vertex-minimal exact-density obstruction to S_ell as in a05c50b3ab96. Let w_1,...,w_{ell-1} be arbitrary nonnegative weights and put W(r)=sum_{t=1}^r w_t. Then
                sum_{e in E(H)} W(phi(e)) - sum_{e ascending} w_{phi(e)}
                <= d sum_{v in V(H)} W(phi(v))
                   - sum_{t: emptyset != V_t != V(H)} w_t,
                where V_t={v:phi(v)>=t}.

            • [1000929] Summed potential cuts retain the exact induced-core density defects
                STATEMENT
                Let xi_t=|E(H[V_t])|-d|V_t|. For arbitrary nonnegative weights w_t supported on h<t<=L,
                  sum_t w_t A_t
                  >= sum_t w_t M_{>=t}
                     -d sum_t w_t|V_t|
                     -sum_t w_t xi_t.
                In particular,
                  A_{>h}
                  >= sum_e(phi(e)-h)_+
                     -d sum_v(phi(v)-h)
                     -sum_{t=h+1}^L xi_t.
                The previously claimed +(L-h) bonus is recovered only under the additional hypothesis xi_t<=-1 at every proper threshold.

        • [1000428] Ascending sources are exactly the one-step incidence rank defects
            STATEMENT
            Let H be a finite linear 3-graph and let v be a vertex with endpoint potential phi(v)=p. For every incident hyperedge e,
              phi(e)<=p+1.
            Furthermore,
              phi(e)=p+1
            if and only if e is nonspecial ascending and v is its unique entrance.
            
            Equivalently, every special incidence and every nonspecial terminal or nonascending-entrance incidence satisfies phi(e)<=phi(v); the only incidence with phi(e)>phi(v) is an ascending entrance, and then the gap is exactly one.

        • [1000921] Special/nonspecial incidence compatibility gives the d plus five-sixths potential bound and rigid equality
            STATEMENT
            Let H be a finite linear 3-graph on n vertices with m edges, and assume phi(v)>=2 for every vertex. Let s be the number of special edges. Then
              m-sum_v phi(v)+(3/2)n <= s
              <= 2sum_v phi(v)-n-2m.
            
            Consequently
              (1/n)sum_v phi(v) >= m/n + 5/6.
            
            In particular, at exact density m=d n,
              average(phi) >= d+5/6.
            
            Moreover, equality average(phi)=m/n+5/6 holds if and only if both displayed special-edge bounds are equalities; in that case
              s=2n/3.
            Thus an equality-layer obstruction attaining the minimum possible average endpoint potential has exactly two-thirds as many special edges as vertices and simultaneously saturates both the nonspecial-terminal capacity and the total snake-indegree capacity.

          • [1001032] Near-minimum average potential forces simultaneous near-saturation of special and nonspecial incidence capacities
              STATEMENT
              Let H satisfy the hypotheses of ce94930a22e0, and write rho=m/n. Suppose
                (1/n)sum_v phi(v)=rho+5/6+epsilon
              with epsilon>=0.
              
              Let
                Delta_ns = sum_v(2phi(v)-3)-2(m-s),
              the slack in the cumulative nonspecial-terminal capacity, and
                Delta_sn = sum_v(2phi(v)-1)-(2m+s),
              the slack in the total snake-indegree capacity.
              
              Then
                (1/2)Delta_ns + Delta_sn = 3epsilon n.
              
              Also
                (2/3-epsilon)n <= s <= (2/3+2epsilon)n.
              
              In particular, epsilon=0 iff Delta_ns=Delta_sn=0, and then s=2n/3. More generally, if epsilon=o(1), then both capacity systems have total slack o(n), so all but o(n) vertices have locally near-saturated terminal/snake budgets in the averaged sense.

            • [1000023] A vertex cannot simultaneously saturate nonspecial-terminal and total snake capacities
                STATEMENT
                Let H be a finite linear 3-graph and let v have p=phi(v)>=2. Put
                  delta_ns(v)=(2p-3)-t_ns(v),
                  delta_sn(v)=(2p-1)-d_D^-(v),
                where t_ns(v) is the number of nonspecial edges for which v is a terminal and d_D^-(v) is total snake indegree.
                
                Then delta_ns(v) and delta_sn(v) cannot both be zero.
                
                Equivalently, for every vertex with phi(v)>=2,
                  [(2phi(v)-3)-t_ns(v)] + [(2phi(v)-1)-d_D^-(v)] >= 1.

              • [1000695] For endpoint potential at least three, the weighted local snake defect is at least one
                  STATEMENT
                  Let H be a finite linear 3-graph and let v satisfy p=phi(v)>=3. Define
                    a(v)=(2p-3)-t_ns(v),
                    b(v)=(2p-1)-d_D^-(v).
                  Then
                    (1/2)a(v)+b(v)>=1.
                  
                  Equivalently, the two smallest possible local slack patterns (0,0) and (1,0) are both impossible.

                • [1000558] Dense equality cores have average endpoint potential at least density plus seven-sixths
                    STATEMENT
                    Let H be a finite linear 3-graph on n vertices with m edges and assume phi(v)>=3 for every vertex. Then
                      (1/n)sum_v phi(v) >= m/n + 7/6.
                    
                    In particular, every exact-density equality-layer candidate with minimum degree high enough to force phi(v)>=3 satisfies
                      average(phi)>=d+7/6
                    when m=d n.
                    
                    If equality holds, then at every vertex v exactly one of the following local slack patterns occurs:
                      Type A: a(v)=2, b(v)=0;
                      Type B: a(v)=0, b(v)=1.
                    Accordingly, Type A vertices lie in exactly four special edges and Type B vertices lie in exactly one special edge.

                  • [1000209] The density-plus-seven-sixths potential bound is never attained in the dense regime
                      STATEMENT
                      Let H be a finite linear 3-graph with phi(v)>=3 for every vertex. Then equality cannot hold in
                        average(phi)>=m/n+7/6.
                      
                      Equivalently,
                        sum_v phi(v) > m + (7/6)n.
                      
                      More structurally, any hypothetical equality configuration would force every nonspecial edge to be ascending and would give the strict-potential auxiliary DAG positive indegree at every vertex, impossible.

                    • [1000569] Strict integer form of the ell minus thirteen-sixths upper bound
                        STATEMENT
                        For every ell>=6 and every n, every n-vertex linear 3-uniform hypergraph with no linear P_ell satisfies
                          6|E(H)| <= (6ell-13)n-1.
                        Equivalently,
                          |E(H)| <= floor(((6ell-13)n-1)/6).
                        
                        In particular
                          |E(H)| < (ell-13/6)n.

                    • [1000646] Near the seven-sixths floor, almost every vertex is Type A and almost every nonspecial edge is ascending
                        STATEMENT
                        Let H be a finite linear 3-graph with phi(v)>=3 for every vertex, and suppose
                          sum_v phi(v)=m+(7/6+eta)n
                        for eta>=0.
                        
                        Let R be the set of vertices that are not Type A, i.e. do not satisfy
                          a(v)=2, b(v)=0.
                        Let s be the number of special edges, and let N^- be the number of nonspecial nonascending edges.
                        
                        Then
                          |R|<=6 eta n,
                          (4/3-4eta)n <= s <= (4/3+2eta)n,
                        and
                          N^-<=6 eta n.
                        
                        Moreover every nonspecial nonascending edge has its unique entrance in R.

                      • [1000715] The lowest Type-A potential level forces a large exceptional entrance set
                          STATEMENT
                          Assume the near-floor setting of 92cce33dd917. Let R be the non-Type-A vertices. Suppose Type-A vertices exist, let
                            p0=min{phi(v): v notin R},
                          and let
                            X={v notin R: phi(v)=p0}.
                          Then
                            |R|>=2p0-5.
                          
                          Consequently, if
                            sum_v phi(v)=m+(7/6+eta)n,
                          then
                            eta n >= (2p0-5)/6.
                          
                          If in addition H has minimum degree delta, then p0>=ceil((delta+1)/2), so
                            eta n >= [2ceil((delta+1)/2)-5]/6.

                    • [1001141] Near the density-plus-seven-sixths floor, only O(eta n) vertices and edges are exceptional
                        STATEMENT
                        Let H be a finite linear 3-graph with phi(v)>=3 for every vertex. Write
                          S=sum_v phi(v)=m+(7/6)n+eta n,
                        with eta>=0. For each vertex put
                          delta_ns(v)=(2phi(v)-3)-t_ns(v),
                          b(v)=(2phi(v)-1)-d_D^-(v),
                        and call v Type A when (delta_ns(v),b(v))=(2,0).
                        
                        Then:
                        (1) the number of non-Type-A vertices is at most 6 eta n;
                        (2) B:=sum_v b(v) <= 6 eta n;
                        (3) the number N_na of nonascending nonspecial edges is at most B, hence N_na<=6 eta n.
                        
                        Thus if eta=o(1), all but o(n) vertices are Type A and all but o(n) nonspecial edges are ascending.

                      • [1000834] The bottom potential layer forces distance from the seven-sixths floor
                          STATEMENT
                          In the setting of fa7e5e79b905, let h=min_v phi(v) and let L_h={v:phi(v)=h}, r=|L_h|. Then
                            eta >= [r(2h-5)]/[6n(2h-3)].
                          In particular eta >= (r/n)/18 for h>=3, and asymptotically the coefficient tends to (r/n)/6 as h grows.
                          
                          Thus any sequence of dense cores with eta=o(1) must have a bottom potential layer of size o(n).

                  • [1000320] The one-special local equality type is impossible
                      STATEMENT
                      Let v have p=phi(v)>=3 and local slack pattern
                        a(v)=0, b(v)=1.
                      Then this configuration is impossible.
                      
                      Consequently, if equality holds in 7cae1cb001ac, every vertex must be Type A:
                        a(v)=2, b(v)=0,
                      and hence every vertex lies in exactly four special edges. Therefore the special-edge subhypergraph is 4-regular on vertices and
                        3s=4n.

                    • [1000624] Type-A equality vertices have at most one deficient special incidence
                        STATEMENT
                        Assume a vertex v with p=phi(v)>=3 has Type-A local slack
                          a(v)=2, b(v)=0.
                        Then v lies in exactly four special edges.
                        
                        For every maximum p-edge path P ending at v:
                        - if the last edge h is nonspecial, the four special edges through v meet P outside v exactly at the two free vertices of g_1 and the two critical vertices
                          C=g_{p-2}\g_{p-3};
                          the two far-contact special edges have rank p, and the two critical-contact special edges have rank at least p-1;
                        - if the last edge h is special, then h and the two special edges using the far free vertices all have rank p.
                        
                        Consequently at least three of the four special edges through v have rank p. Equivalently, at most one special edge e through v can satisfy phi(e)<phi(v), and any such deficient incidence has phi(e)=phi(v)-1.

                  • [1000495] General upper bound improved to (ell-13/6)n
                      STATEMENT
                      For every ell>=6, every n-vertex linear 3-uniform hypergraph with no linear P_ell satisfies
                        |E(H)| <= (ell-13/6)|V(H)|.
                      Equivalently,
                        ex_L(n,P_ell^(3)) <= (ell-13/6)n.
                      This improves the certified (ell-2)n general bound by n/6.

                    • [1001000] The (ell-13/6)n upper bound has an additional additive Theta(ell) improvement
                        STATEMENT
                        For every integer ell>=6 and every n-vertex linear 3-uniform P_ell-free hypergraph H,
                          |E(H)| <= (ell-13/6)n - c_ell,
                        where
                          c_ell = [2 ceil((ell-1)/2)-5]/6.
                        Equivalently,
                          c_ell=(ell-5)/6 for even ell,
                          c_ell=(ell-6)/6 for odd ell.
                        
                        Thus the new (ell-13/6)n bound admits an additional additive improvement of order ell.

              • [1000887] Special/ascending compatibility improves the universal average endpoint potential floor to density plus one
                  STATEMENT
                  Let H be a finite linear 3-graph on n vertices with m edges, and assume phi(v)>=2 for every vertex. Then
                    (1/n)sum_v phi(v) >= m/n + 1.
                  
                  In particular, if |E(H)|=d|V(H)|, then
                    average(phi)>=d+1.

                • [1000068] Equality at density plus one gives an exact three-special-edge blocker normal form
                    STATEMENT
                    Assume equality in c77c818cf1e9:
                      average(phi)=m/n+1.
                    Fix a vertex v with p=phi(v), and let
                      P=(g_1,...,g_p)
                    be any maximum p-edge path ending at v, with h=g_p.
                    
                    Then:
                    (1) v lies in exactly three special edges;
                    (2) if h is nonspecial, then among the 2p-4 tail vertices
                        T=(V(g_2 union ... union g_{p-1}))\V(h),
                        exactly one is not used as the blocker witness of a nonspecial terminal edge through v; the three special edges through v meet P outside v exactly once each, at the two free vertices of g_1 and at that unique unused tail vertex;
                    (3) if h is special, then every vertex of T is used by a nonspecial terminal edge through v, and the other two special edges through v meet P outside v exactly once each, at the two free vertices of g_1.
                    
                    In either case at least two special edges through v have rank p. Consequently all three special edges through v have rank exactly p.

              • [1001077] Local capacity incompatibility improves average endpoint potential to density plus one
                  STATEMENT
                  Let H be a finite linear 3-graph in which phi(v)>=2 for every vertex, with n vertices and m edges. Then
                    (1/n) sum_v phi(v) >= m/n + 1.
                  Equivalently,
                    sum_v phi(v) >= m+n.
                  
                  More precisely, with
                    delta_ns(v)=(2phi(v)-3)-t_ns(v),
                    delta_sn(v)=(2phi(v)-1)-d_D^-(v),
                  one has delta_ns(v),delta_sn(v)>=0 and delta_ns(v)+delta_sn(v)>=1 for every v, while
                    (1/2)sum_v delta_ns(v)+sum_v delta_sn(v)
                     =3[sum_v phi(v)-m-(5/6)n].
                  Therefore the right-hand side is at least n/2.

                • [1000306] Minimum-potential equality is a 3-regular special core plus an all-ascending remainder
                    STATEMENT
                    Assume H satisfies phi(v)>=2 for every vertex and equality in eeb9576892:
                      sum_v phi(v)=m+n.
                    Then every vertex lies in exactly three special hyperedges. Consequently the special-edge subhypergraph is 3-uniform and 3-regular, and the number s of special edges equals n.
                    
                    Moreover every nonspecial edge is ascending. In particular, if m=dn then H has exactly n special edges and (d-1)n nonspecial edges, all of the latter ascending.

            • [1000087] Minimum-potential equality forces the special-edge subhypergraph to be a cubic-graph dual
                STATEMENT
                Under the hypotheses of ce94930a22e0, suppose
                  (1/n)sum_v phi(v)=m/n+5/6.
                Then for every vertex v,
                  t_ns(v)=2phi(v)-3
                and
                  d_D^-(v)=2phi(v)-1,
                where t_ns(v) is the number of nonspecial edges for which v is a terminal and d_D^-(v) is the total snake indegree.
                
                Consequently every vertex of H lies in exactly two special hyperedges.
                
                Let H_sp be the subhypergraph consisting of the special edges. Then H_sp is a linear 3-uniform 2-regular hypergraph. Equivalently, the intersection graph L(H_sp) is a simple cubic graph: its vertices are the special hyperedges, and every original vertex of H corresponds to the unique graph edge joining the two special hyperedges that contain it. In particular
                  3s=2n
                and s=2n/3.

              • [1000328] In minimum-potential equality, every special edge lies strictly below all three endpoint potentials
                  STATEMENT
                  Assume the minimum-potential equality setting of 148ebd1d1809. Then for every vertex v with p=phi(v), every maximum p-edge path ending at v has a nonspecial last edge for which v is a terminal.
                  
                  Consequently, if e is special and v∈e, then
                    phi(e)<=phi(v)-1.
                  Thus every special edge e={a,b,c} satisfies
                    phi(a),phi(b),phi(c)>=phi(e)+1.

      • [1001064] Source/non-source decomposition couples a forced digraph to a proper colored graph
          STATEMENT
          Let V be a finite set and let F be a linear family of triples. In every T∈F choose a source σ(T)∈T. Form a digraph D by replacing T={u,v,w} with source u by the arcs u→v,u→w, and form a graph H by adding the edge vw colored u. For x∈V let s(x) be the number of triples sourced at x and h(x)=d_H(x). Then H is simple and properly edge-colored, and
          s(x)+h(x)=d_F(x),
          d_D^+(x)=2s(x),
          d_D^-(x)=h(x).
          Hence
          (1/2)d_D^+(x)+d_D^-(x)=d_F(x)
          for every x.

      • [1001094] Shadow-rainbow reduction and its black-box 2/3 ceiling
          STATEMENT
          Let H be a linear 3-graph. Color each pair xy in its 2-shadow by the unique third vertex z with xyz in E(H). This is a proper edge-coloring. For any bipartition V(H)=A∪B, retain on A exactly the shadow edges whose color lies in B; every rainbow t-edge path in the retained graph lifts to P_t^(3) in H. Consequently, if every properly edge-colored graph of average degree d has a rainbow path of length at least alpha*d-C, then every P_ell^(3)-free H satisfies |E(H)| <= (2/(3alpha))(ell+C)|V(H)|. Thus even an ideal alpha=1 black-box theorem stops at leading coefficient 2/3.

      • [1001062] Original-hypergraph density-core minimum-degree reduction
          STATEMENT
          Let H be a nonempty finite 3-uniform hypergraph with n vertices and m>0 edges. There is a nonempty vertex-induced subhypergraph H0 such that |E(H0)|/|V(H0)| >= m/n and delta(H0) >= |E(H0)|/|V(H0)|. In particular, for a linear P_ell-free H, H0 remains linear and P_ell-free.

      • [1000822] Two-stage minimum-degree normalization for the rainbow shadow
          STATEMENT
          Let H be a nonempty linear 3-graph with density rho=|E(H)|/|V(H)|. There is a linear subhypergraph H0 with delta(H0)>=rho0:=|E(H0)|/|V(H0)|>=rho. From H0 one can choose an A/B shadow graph J and then a graph subgraph J0 such that J0 is properly edge-colored, every rainbow path in J0 lifts to a linear path in H0, and delta(J0)>=3rho0/4>=3rho/4.

      • [1000295] Full shadow doubles hypergraph degree
          STATEMENT
          Let H be a linear 3-uniform hypergraph and S its 2-shadow, with each shadow edge yz colored by the unique third vertex x such that xyz is in E(H). Then S is properly edge-colored and d_S(v)=2d_H(v) for every vertex v. Hence delta(S)=2delta(H). A minimum-degree theorem for properly edge-colored graphs applied to the full shadow must use delta(S), not delta(H).

      • [1000304] Ascending-edge rainbow-layer formulation
          STATEMENT
          Let H be a P_ell^(3)-free linear 3-graph. For each nonspecial edge e of edge rank t with unique entrance x, call e ascending when φ(x)=t-1. Let A be the number of ascending edges. Then 3|E(H)|-A ≤ Σ_v(2φ(v)-1) ≤ (2ell-3)|V(H)|. Moreover, for each k≥1, the ascending edges with entrance level φ(x)=k form a properly edge-colored graph J_k on their terminal pairs, colored by x, and J_k contains no rainbow path of length k+1.

        • [1000966] Ordered shadow graph for chaining ascending edges
            STATEMENT
            For each ascending nonspecial hyperedge e={x,u,v} of rank q with unique entrance x, form an auxiliary edge-ordered graph Z on V(H) by adding the two entrance-terminal edges xu,xv with order label q-1 and the terminal-pair edge uv with order label q; color all three auxiliary edges by the parent hyperedge e. Investigate whether sufficiently many ascending hyperedges force a long strictly increasing rainbow path in Z of a liftable form, and whether such a path yields a long linear path in H.

          • [1000085] Increasing ordered-shadow paths have nondecreasing parent ranks and lift unless they close a linear cycle
              STATEMENT
              Let Z be the ordered shadow from d7bc6f5ad804. Let z_0z_1,...,z_{t-1}z_t be a simple rainbow path in Z with strictly increasing order labels lambda_1<...<lambda_t, and let E_i be the distinct parent hyperedge of z_{i-1}z_i, with q_i=phi(E_i). Then q_1<=...<=q_t. Moreover either E_1,...,E_t is a linear hypergraph path, or there exist i<j-1 such that E_i,...,E_j is a linear cycle.

            • [1001097] Nonspecial edges on a linear cycle have rank at least the cycle length
                STATEMENT
                Let C=(E_1,...,E_c) be a linear cycle of length c>=3 in a linear 3-graph. If E_i is nonspecial, then phi(E_i)>=c. Consequently, if every edge of C is nonspecial, min_i phi(E_i)>=c.

              • [1001186] Ordered-shadow growth continuation
                  STATEMENT
                  Route bridge: the ordered-shadow analysis continues after toolkit lemma 1000221.

                • [1000637] Hidden ordered-shadow cycles force a near-doubling rank spread
                    STATEMENT
                    In the obstruction alternative of 1412d7e749b8, suppose the minimal hidden cycle is E_i,...,E_j and has c=j-i+1 edges. Let q_min=q_i and q_max=q_j; these are respectively the minimum and maximum parent ranks on the cycle. Then c<=q_min and q_max-q_min>=c-2. Consequently q_max>=q_min+c-2>=2c-2, so c<=floor((q_max+2)/2).

        • [1000143] Potential-threshold terminal graphs are rainbow-path-free
            STATEMENT
            Let H be a finite linear 3-graph with endpoint potential phi. For an integer t>=1, form a graph R_t on the vertices v with phi(v)>=t by adding, for each ascending nonspecial hyperedge e={x,u,v} whose unique entrance is x and satisfies phi(x)<t<=min{phi(u),phi(v)}, the terminal-pair edge uv colored by x. Then this coloring is proper and R_t contains no rainbow path of t edges.

        • [1000946] Minty-type potential on the directed graph obtained from nonspecial edges
            STATEMENT
            Let R be the digraph on V(H) obtained by replacing every nonspecial edge e={x,y,z}, with unique entrance x, by the arcs x→y and x→z. For an arc x→y arising from e, put q=φ(e). Assign score log(1+1/φ(x)) if e is ascending; assign -log 2 if e is nonascending and φ(x)<=2(q-1); otherwise assign -log 3. Then every directed closed walk in R has total score at most zero.

          • [1000399] Vertex-level cyclic-transient Minty strategy
              STATEMENT
              Use the directed graph R formed by orienting each nonspecial edge from its unique entrance toward its two snake vertices as the primary Minty object. Treat arcs in recurrent strongly connected structure by the closed-walk potential inequality, and control the remaining ascending arcs by repeated-blocker and path-rotation arguments. This retains the transient sharp examples while putting the cyclic argument directly on the physical vertex set of H.

            • [1000182] Location-sensitive lift of the Minty walk
                STATEMENT
                If the scalar potential φ on the vertex-level nonspecial-edge digraph is too coarse to control the transient part, lift the walk state to remember a path together with the location of the first blocking contact. A clean extension is the positive step; a two-contact Pósa rotation or truncation at the first blocker is the backward step. Seek a step score for which every closed state-walk has nonpositive total score.

        • [1001046] Ascending-layer degree recurrence
            STATEMENT
            Let H be a linear 3-graph, let φ(v) be the maximum length of a linear path ending at v, and let J_k be the ascending-edge layer from 419519f0efa5. If φ(x)=k, then every edge incident with x has rank at most k+1, at most 2k-1 incident edges have rank at most k, and therefore the color class of x in J_k has size at least d_H(x)-(2k-1). On the terminal side, every vertex y of J_k has d_{J_k}(y)<=2k+1. Consequently, if δ(H)>=δ and n_k=|{v:φ(v)>=k}|, then for every k with δ>2k-1, 2(δ-2k+1)(n_k-n_{k+1}) <= (2k+1)n_{k+1}.

        • [1000971] Entrance-rank distortion by blockers
            STATEMENT
            Let H be a linear 3-graph. Let e={x,y,z} be a nonspecial edge of rank t=phi(e) with unique entrance x, and let a(x) be the maximum length of a linear path ending physically at x. For any a(x)-edge path P ending at x, let r be the number of edges of P that meet e. Then 1<=r<=3 and a(x)<=r(t-1). In particular a(x)<=3(t-1). If e is nonascending, then r>=2; if a(x)>2(t-1), then r=3, so both terminal vertices y,z occur on P as blockers.

          • [1000874] Nonascending bad-load blocker bound
              STATEMENT
              Let H be a linear 3-graph and x a vertex with endpoint rank a=a(x). Among nonspecial edges e whose unique entrance is x and which are nonascending, there are at most 2a-2. More sharply, among those satisfying a>2(phi(e)-1), there are at most a-1.

          • [1001078] Entrance-value distortion with consecutive-contact correction
              STATEMENT
              Let f be a nonspecial edge with φ(f)=q and unique entrance x. Let P be a path of length φ(x) with last vertex x. If r vertices of f occur on P, then φ(x)<=r(q-1)<=3(q-1). If f is not ascending, then r>=2; if φ(x)>2(q-1), then r=3.

            • [1000643] Maximum-path characterization of ascending and nonascending edges
                STATEMENT
                Let f={x,y,z} be a nonspecial edge with unique entrance x and q=φ(f). Then f is ascending if and only if there exists a path of length φ(x) with last vertex x that contains neither y nor z. If f is nonascending, every path of length φ(x) with last vertex x contains at least one of y,z. If moreover φ(x)>2(q-1), then every such path contains both y and z.

            • [1000900] Joint snake-incidence and blocker budget
                STATEMENT
                Fix a vertex x and let I(x) be the incident edges e with φ(e,x)=φ(e). Let B^-(x) be the nonspecial nonascending edges with unique entrance x. For f∈B^-(x), put w_x(f)=ceil(φ(x)/(φ(f)-1))-1. Then |I(x)|+Σ_{f∈B^-(x)}w_x(f)<=2φ(x)-1.

              • [1001192] Ascending-accounting continuation
                  STATEMENT
                  Route bridge: the ascending-edge accounting analysis continues after toolkit lemma 1000278.

                • [1001002] Global compensated ascending-defect bound
                    STATEMENT
                    It is enough for the general 2/3-leading-coefficient route to prove A-H_2=O(n), where A is the number of ascending edges and H_2 is the number of nonspecial nonascending edges e with unique entrance x satisfying φ(x)>2(φ(e)-1).

            • [1001124] Minty-type potential on the transfer digraph of nonspecial edges
                STATEMENT
                Define a digraph M on the nonspecial edges of H by e→f when e∩f={v}, φ(e,v)=φ(e), and v is the unique entrance of f. For e→f put p=φ(e), q=φ(f). If f is ascending, assign score log(1+1/p); if f is nonascending and φ(v)<=2(q-1), assign score -log 2; otherwise assign score -log 3. Every directed closed walk in M has total score at most zero.

              • [1000813] Cyclic-transient decomposition for the transfer digraph
                  STATEMENT
                  Split the nonspecial-edge transfer digraph into its vertices lying on directed cycles and the remaining transient vertices. Use the Minty-type closed-walk inequality on the cyclic part and blocker/rotation arguments on the transient part. It would suffice to prove A_cyclic<=H_2+O(n) and A_transient=O(n); together with the refined ascending-edge accounting this gives m<=(2ell/3+O(1))n.

        • [1000397] Refuted: ascending terminal-degree conjecture
            STATEMENT
            Refuted. It is not true that every vertex is a last vertex for at most three ascending nonspecial edges. The explicit counterexample 830b0775567f has four such edges at one vertex.

          • [1000856] Terminal tail-blocker lemma
              STATEMENT
              Let e and f be distinct edges of a linear 3-uniform hypergraph sharing a vertex v. Assume e is nonspecial of rank q=phi(e), that v is a terminal vertex of e, and that f is a snake-incoming edge at v with phi(f)>=q-1. Then for every longest path P ending in f at v, the edge e meets at least one of the q-2 edges immediately preceding f in the final (q-1)-edge suffix of P. Equivalently, e cannot be disjoint from the precursor part of any (q-1)-edge suffix ending in f at v.

          • [1000998] Rank-gap forces the terminal blocker for ascending edges
              STATEMENT
              Let e={x,v,y} be an ascending nonspecial edge of rank q, with unique entrance x, so a(x)=q-1 and v,y are terminal vertices. Let f be a snake-incoming edge at v of rank p>=q-1. For any longest path ending in f at v, the terminal tail-blocker lemma forces e to meet the final q-2 precursor edges. If p>=2q-1, that forced intersection cannot occur at x; hence it must occur at y.

          • [1000448] High-rank competitor captures all vertices of a lower ascending edge
              STATEMENT
              Let e={x,v,y} be an ascending nonspecial edge of rank q, with unique entrance x and terminals v,y. Let f be a snake-incoming edge at v of rank p>=2q-1, and let P be any longest p-edge path ending in f at v. Then P contains both x and y in its precursor before f; together with v in f, the path P meets all three vertices of e.

          • [1000799] Repeated-blocker splice obligation for four ascending terminal edges
              STATEMENT
              To prove the ascending terminal-degree conjecture, it suffices to rule out four ascending nonspecial edges through one common terminal vertex. Ordering their ranks t1>=t2>=t3>=t4, each lower-ranked edge e_j must intersect the precursor paths of all higher-ranked edges e_i (i<j). Hence e_4, which has only two noncommon vertices, meets three precursor paths through only two blocker vertices, forcing one blocker vertex to lie on two precursor paths. A path-splicing/uncrossing lemma at such a repeated blocker would close the degree-3 conjecture.

            • [1000583] First-contact localization for a nonspecial edge
                STATEMENT
                Let f be a nonspecial edge of rank q with unique entrance x. Let R=(r_1,...,r_p) be any linear path not using f, and let i be the first index for which r_i meets f. If r_i∩f={x}, then i<=q-1. If r_i meets f in one of the two terminal vertices of f, then i<=q-2.

            • [1001045] Separation of successive contacts with a nonspecial edge
                STATEMENT
                Let f be a nonspecial edge of a linear 3-graph with φ(f)=q and unique entrance vertex x. Let P=(e_1,...,e_p) be a path not using f. Suppose u,w are distinct vertices of f such that u occurs on P before w, and no vertex of f occurs on the intervening part of P. Let i be the last index of an edge of P containing u before the first later occurrence of w, and let j>i be the first index of an edge containing w. If w=x, then j-i<=q-1. If w is one of the other two vertices of f, then j-i<=q-2.

          • [1000296] Refuted: compensated terminal-degree conjecture
              STATEMENT
              Refuted. The inequality a(v)<=3+h(v) is false. In counterexample 830b0775567f, one vertex satisfies a(v)=4 and h(v)=0.

          • [1001049] High-rank competitors contain the whole ascending edge
              STATEMENT
              Let e={x,v,y} be an ascending nonspecial edge of rank q with unique entrance x, so a(x)=q-1 and v,y are terminal. Let f be a snake-incoming edge at v of rank p>=2q-1, and let P be any longest p-edge path ending in f at physical terminal v. Then P contains all three vertices x,y,v of e. More precisely, y occurs among the final q-2 precursor edges before f, and x occurs earlier on P.

          • [1001043] Ascending edges at one last vertex can have unbounded φ-gap
              STATEMENT
              For every integer q>=5 there is a linear 3-graph containing two ascending nonspecial edges e and f that share a last vertex v and satisfy φ(e)=2q-3 and φ(f)=q. In particular, the difference φ(e)-φ(f)=q-3 is unbounded.

          • [1000591] Four ascending edges can share one last vertex
              STATEMENT
              There exists a linear 3-graph with four ascending nonspecial edges having the same last vertex. Hence both the conjecture Δ(T^up)<=3 and the compensated inequality a(v)<=3+h(v) are false.

        • [1000845] Ascending terminal graph need not be a pseudoforest
            STATEMENT
            The terminal-pair graph formed only from ascending edges can have cycle rank greater than one in a connected component; in particular the pseudoforest strengthening is false.

        • [1000157] Directed graph of ascending edges and a level-cut inequality
            STATEMENT
            For each ascending edge e={x,y,z} with unique entrance x, orient two arcs x→y and x→z on V(H). Then φ strictly increases along every arc. If c(v) is the number of ascending edges with entrance v, then d^+(v)=2c(v), d^-(v)<=2φ(v)-1, and d_H(v)-c(v)<=2φ(v)-1. Consequently, for S={v:φ(v)<K}, 2Σ_{v∈S}d_H(v)-3Σ_{v∈S}(2φ(v)-1) <= Σ_{v∉S}(2φ(v)-1).

        • [1000417] Low-φ nonspecial edges force larger-φ adjacency
            STATEMENT
            Let H be a linear 3-graph with minimum degree δ. For t>=1 let B_t be the nonspecial edges e with φ(e)=t, and let M_{>t}=|{f:φ(f)>t}|. Then 2(δ-2t+1)_+ |B_t| <= 3(2t-1) M_{>t}.

        • [1000478] Global bound for ascending edges
            STATEMENT
            Let H be a finite linear 3-graph and let A be the number of ascending edges. Then A<=3|V(H)|/2.

          • [1000293] Refuted: incidence-rank bound for ascending edges
              STATEMENT
              Refuted. It is not true in general that rank_R(N_↑)>=2A/3 for the incidence matrix restricted to ascending edges. The family c3e95f4ce77d has A=9t and rank_R(N_↑)=5t+2, which violates the bound for every t>=3.

            • [1000876] Three-colored K3,3 copies refute the ascending-incidence rank bound
                STATEMENT
                For every t>=2 there is a finite linear 3-graph H_t with A=9t ascending edges on n=6t+3 vertices such that rank_R(N_↑)=5t+2. In particular, for t=3 one has rank_R(N_↑)=17<18=2A/3, so the conjectured bound rank_R(N_↑)>=2A/3 is false. Moreover A/n=9t/(6t+3) tends to 3/2.

          • [1000648] Maximum average degree three for the ascending terminal graph
              STATEMENT
              Let H be a finite linear 3-graph. Form the simple graph T_↑ whose edges are the terminal pairs of the ascending nonspecial hyperedges of H. Then every nonempty subgraph J of T_↑ satisfies 2|E(J)|<=3|V(J)|; equivalently mad(T_↑)<=3.

            • [1000368] Potential-oriented local bound for ascending terminal edges
                STATEMENT
                Let H be a finite linear 3-graph and let a(v) be the maximum length of a linear path ending at v. Fix v∈V(H). Then there are at most three ascending nonspecial edges e={x,v,u} for which v is a terminal vertex and a(u)>=a(v).

              • [1000028] The mixed p=4 charged obstruction is impossible
                  STATEMENT
                  If phi(v)=4, four potential-charged ascending nonspecial edges through v cannot have ordered ranks (3,4,4,4).

              • [1000065] Middle entrance slots force opposite terminals into the first edge
                  STATEMENT
                  In the pure p=4 obstruction, fix P=(g_1,g_2,g_3,f_4) as in f9e64ea63be0. If another charged rank-four edge f={a,v,b} has visible entrance a equal either the private vertex of g_2 or the middle joint g_2∩g_3, then b is a private vertex of g_1.

              • [1000202] Rank-three charged edges at potential four have a unique universal middle entrance
                  STATEMENT
                  Let v satisfy phi(v)=4. Among potential-charged ascending nonspecial edges e={x,v,u} with v terminal and phi(u)>=4, at most one can have edge rank 3. Moreover, if such an edge exists, then for every maximum four-edge path P=(g_1,g_2,g_3,g_4) ending at v, its unique entrance is x=g_2∩g_3.

              • [1000344] Three-pattern normal form for the pure p=4 obstruction
                  STATEMENT
                  Assume phi(v)=4 and four potential-charged ascending nonspecial edges through v all have rank four. Fix a longest path P=(g_1,g_2,g_3,f_4) ending in f_4 at v, and write
                  g_1={L,M,R}, g_2={R,S,T}, g_3={T,U,V},
                  with V=g_3∩f_4 the entrance of f_4. Then T is necessarily the entrance of one of the other charged edges. Up to swapping L,M, exactly one of the following three patterns holds:
                  (A) S,T,V are visible entrances; the fourth entrance is absent from P and its opposite terminal is R; U is unused as a charged witness.
                  (B) R,T,U,V are the four entrances; S is unused as a charged witness.
                  (C) T,U,V are visible entrances; the fourth entrance is absent from P and its opposite terminal is R; S is unused as a charged witness.
                  Moreover in every case the T-entrance edge has opposite terminal one of L,M.

              • [1000440] Potential-five charged obstructions have four rank patterns
                  STATEMENT
                  Let phi(v)=5 and suppose four potential-charged ascending nonspecial edges through v exist. Then every such edge has rank 4 or 5, at most three have rank 4, and the ordered rank pattern is one of (4,4,4,5), (4,4,5,5), (4,5,5,5), (5,5,5,5). Moreover, in pattern (4,4,4,5), for any maximum five-edge path P=(g_1,g_2,g_3,g_4,e_5) ending in a rank-five charged edge e_5 at v, the three rank-four path-relative witnesses are exactly the three vertices of g_3: the joints g_2∩g_3, g_3∩g_4 and the private vertex of g_3.

                • [1000676] In the p=5 pattern 4445, two middle-edge witnesses are forced entrances
                    STATEMENT
                    Let phi(v)=5 and suppose four potential-charged ascending nonspecial edges through v have ordered ranks (4,4,4,5). Fix a maximum five-edge path
                      P=(g1,g2,g3,g4,e5)
                    ending in the rank-five charged edge e5 at v. Write
                      a=g2∩g3,
                      b=the private vertex of g3,
                      c=g3∩g4.
                    
                    Then among the three rank-four charged edges, the witnesses b and c are necessarily their unique entrances. In particular
                      phi(b)=phi(c)=3.
                    Only the left joint a can possibly be realized as an opposite-terminal witness of a rank-four charged edge whose entrance is absent from P.

                  • [1000043] The p=5 pattern 4445 contains a canonical low-high terminal triangle
                      STATEMENT
                      In the p=5 charged pattern (4,4,4,5), with notation from 9a7eac176b49, let
                        f_b={b,v,u_b},
                        f_c={c,v,u_c}
                      be the two rank-four charged edges whose forced entrances are
                        b=private(g3),
                        c=g3∩g4.
                      Then
                        (f_b,g3,f_c)
                      is a linear 3-cycle with joints b,c,v.
                      
                      Moreover
                        phi(b)=phi(c)=3,
                      while the opposite terminals satisfy
                        phi(u_b)>=5,
                        phi(u_c)>=5.
                      Thus every 4445 obstruction contains a canonical triangle with two low-potential entrance joints and two high-potential outer terminals.

                    • [1000093] The low joints in a 4445 triangle are universally pinned on high-terminal five-paths
                        STATEMENT
                        In the p=5 charged 4445 setting of 0b8e51bfe396, let
                          f_b={b,v,u_b}, f_c={c,v,u_c},
                        with phi(f_b)=phi(f_c)=4, phi(b)=phi(c)=3, and phi(u_b),phi(u_c)>=5.
                        
                        Let R=(r_1,...,r_5) be any five-edge linear path ending physically at u_b. Then f_b is not the last edge of R, and one of b,v occurs in r_3 union r_4. Moreover, if b occurs in r_3 union r_4, then b must be exactly the joint
                          b=r_3∩r_4.
                        In particular b cannot be private to r_3 or r_4 and cannot be the joint r_4∩r_5.
                        
                        The symmetric statement holds for c on every five-edge path ending physically at u_c.

                    • [1000560] In the p=5 pattern 4445, both high terminals are forced into the first two path edges
                        STATEMENT
                        In the p=5 charged pattern (4,4,4,5), use the notation of 0b8e51bfe396 and let
                          P=(g1,g2,g3,g4,e5)
                        be the fixed rank-five path ending in the rank-five charged nonspecial edge e5 at terminal v. Let
                          f_b={b,v,u_b},
                          f_c={c,v,u_c}
                        be the two rank-four charged edges with forced entrances b,c in g3.
                        
                        Then
                          u_b,u_c ∈ V(g1∪g2).
                        Moreover neither lies in g3, and u_b≠u_c.

                      • [1001119] Canonical entrance paths in the p=5 4445 pattern must cross the far end of the five-path
                          STATEMENT
                          In the p=5 charged pattern (4,4,4,5), retain the notation of 7d676959b033. Let R_b be any canonical three-edge entrance path for the ascending rank-four edge
                            f_b={b,v,u_b},
                          so R_b ends at b and avoids both terminals v,u_b.
                          
                          Then R_b must meet V(e5∪g4). Equivalently, no canonical b-ending entrance path for f_b is disjoint from both the rank-five terminal edge e5 and its predecessor g4.

                    • [1000870] Every five-path to a high terminal of the 4445 triangle is suffix-blocked by the middle edge
                        STATEMENT
                        In the 4445 triangle setting of 0b8e51bfe396, let
                          f_b={b,v,u_b}
                        and let g_3 contain b,c with phi(c)=3.
                        
                        For every five-edge path
                          R=(r_1,r_2,r_3,r_4,r_5)
                        ending at u_b, at least one of the following holds:
                        (i) r_4 meets f_b;
                        (ii) r_4 meets g_3;
                        (iii) r_5 meets g_3.
                        
                        Equivalently, the four-edge sequence
                          r_4,r_5,f_b,g_3
                        can never be a linear path.
                        
                        Symmetrically, for every five-edge path ending at u_c, the analogous suffix through f_c and g_3 is blocked; otherwise it would give a four-edge path ending at b.

                      • [1000125] High-terminal five-paths in the 4445 triangle satisfy a three-way late-contact alternative
                          STATEMENT
                          In the 4445 triangle setting, write
                            g_3={a,b,c},
                            f_b={b,v,u_b},
                          with phi(b)=phi(c)=3.
                          
                          For every five-edge path
                            R=(r_1,...,r_5)
                          ending physically at u_b, at least one of the following holds:
                          (A) v∈r_4;
                          (B) b=r_3∩r_4;
                          (C) a∈r_4∪r_5.
                          
                          Moreover b,c are absent from r_5, and any occurrence of b or c in r_4 is necessarily the joint r_3∩r_4.
                          
                          Symmetrically, every five-edge path ending at u_c satisfies
                            v∈r_4, or c=r_3∩r_4, or a∈r_4∪r_5.

                      • [1000178] A late common-terminal blocker on a 4445 high-terminal path forces the low entrance into the center
                          STATEMENT
                          In the 4445 triangle setting, let f_b={b,v,u_b} with phi(f_b)=4 and phi(b)=3. Let
                            R=(r_1,...,r_5)
                          be a five-edge path ending at u_b.
                          
                          If v∈r_4, then b∈V(R). More precisely,
                            b is either the private vertex of r_3 or the joint r_2∩r_3.
                          In particular b∉r_4.

                        • [1000683] The v-late branch of a 4445 high-terminal path forces the third middle vertex to an end side
                            STATEMENT
                            In the 4445 triangle setting, let g_3={a,b,c}, phi(b)=phi(c)=3, and let
                              R=(r_1,...,r_5)
                            be a five-edge path ending at u_b with v∈r_4.
                            
                            By 26b4d33bfabe, b is either private in r_3 or b=r_2∩r_3.
                            
                            Assume g_3 is not itself an edge of R.
                            
                            (i) If b is private in r_3, then a∈V(r_1∪r_2).
                            
                            (ii) If b=r_2∩r_3, then a∈V(r_4∪r_5).
                            
                            Thus, outside the exact coincidence g_3∈E(R), the v-late branch forces the third vertex a of the canonical triangle to a prescribed side of the path according to the central position of b.

                  • [1000736] A five-edge path chord excludes the potential-five pattern 4445
                      STATEMENT
                      Let H be a finite linear 3-graph and P=(g1,g2,g3,g4,g5) a five-edge linear path with last vertex v. Put a=g2∩g3 and c=g3∩g4. If H contains an edge f containing a and v, then φ(c)≥4. Consequently, at a vertex v with φ(v)=5, four potential-charged ascending nonspecial edges cannot have ordered ranks (4,4,4,5). The remaining four-edge rank patterns are (4,4,5,5), (4,5,5,5), and (5,5,5,5).

                    • [1000740] An endpoint chord raises the next joint's vertex rank
                        STATEMENT
                        Let P=(g1,...,gp) be a linear path in a finite linear 3-graph, with p≥3 and last vertex v. For 1≤i≤p-2 put a=g_i∩g_{i+1} and c=g_{i+1}∩g_{i+2}. If an edge f contains a and v, then φ(c)≥min{i+2,p-i+1}.

              • [1000568] The mixed p=4 obstruction consists of common-endpoint two-rail paths
                  STATEMENT
                  Assume phi(v)=4 and four potential-charged ascending nonspecial edges through v have ranks (3,4,4,4). Let e={x,v,u} be the unique rank-three edge, so phi(x)=2. For any rank-four charged edge f={a,v,b} and any longest four-edge path P_f=(h_1,h_2,h_3,f) ending in f with last vertex v, one has x=h_2∩h_3 and u is a private vertex of h_1. Hence P_f is a four-edge path with last vertices u and v and middle joint x.

              • [1000709] Potential four satisfies the potential-oriented local bound
                  STATEMENT
                  If phi(v)=4, then v is terminal for at most three potential-charged ascending nonspecial edges e={x,v,u} with phi(u)>=4.

              • [1000767] The S-entrance pattern in the pure p=4 obstruction is impossible
                  STATEMENT
                  Pattern (A) in the three-pattern normal form 49c24605109f is impossible. Hence any pure p=4 obstruction must be of pattern (B) or (C), with S unused and T,U,V visible entrances.

              • [1001079] Certified low-potential case of the potential-oriented local bound
                  STATEMENT
                  If v has endpoint potential p=phi(v)<=3, then v is terminal for at most three potential-charged ascending nonspecial edges e={x,v,u} with phi(u)>=p.

              • [1001137] Absent entrances in the pure p=4 obstruction are pinned to the first joint
                  STATEMENT
                  Let phi(v)=4 and let f_1,f_2,f_3,f_4 be four rank-four potential-charged ascending nonspecial edges through v. Fix a longest path P=(g_1,g_2,g_3,f_4) ending in f_4 with last vertex v. For i∈{1,2,3}, if the unique entrance a_i of f_i is absent from P, then the opposite terminal b_i equals the first joint g_1∩g_2. Consequently at most one of f_1,f_2,f_3 can have its entrance absent from P.

              • [1001217] Universal middle-joint entrance in the first potential-four obstruction
                  STATEMENT
                  Let v satisfy phi(v)=4 and suppose four potential-charged ascending nonspecial edges through v exist. Then their ranks are either (3,4,4,4) or (4,4,4,4). In the (3,4,4,4) case, if e={x,v,u} is the unique rank-three edge, then for every maximum four-edge path P=(g_1,g_2,g_3,g_4) ending at v one has x=g_2∩g_3 and phi(x)=2. In particular each rank-four charged edge admits a longest four-edge path ending through v whose middle joint is the same vertex x.

              • [1000098] Any long terminal path captures a lower-rank ascending edge
                  STATEMENT
                  Let e={x,v,u} be an ascending nonspecial edge of rank q, with unique entrance x and terminal vertices v,u. Let P be any linear path of length p>=2q-1 ending at v. Then P contains all three vertices x,v,u of e. More precisely, u occurs among the final q-2 precursor edges before the last edge of P, and x occurs within the final q-1 edges of a prefix of P ending at u.

                • [1000743] Terminal potentials of an ascending edge are at most three times its rank
                    STATEMENT
                    Let e={x,u,v} be an ascending nonspecial edge of a finite linear 3-graph, with unique entrance x and rank q=φ(e). Then φ(u),φ(v)<=3q-3. Equivalently q>=ceil((max{φ(u),φ(v)}+3)/3). In particular, for a potential-oriented charged edge at v, q>=ceil((φ(v)+3)/3).

                • [1000756] Terminal potentials of an ascending edge are at most twice its rank minus two
                    STATEMENT
                    Let e={x,u,v} be an ascending nonspecial edge of a finite linear 3-graph, with unique entrance x and edge rank q=φ(e). Then φ(u),φ(v)<=2q-2. Equivalently q>=ceil((φ(u)+2)/2) and q>=ceil((φ(v)+2)/2). This is sharp: the six-edge example 0e0b0a3c7b04 has q=3 and φ(u)=φ(v)=4=2q-2.

                  • [1000726] Strict terminal-potential rise forces a narrower upper-half rank band
                      STATEMENT
                      Let e={x,v,u} be an ascending nonspecial edge with rank q=φ(e), and suppose p=φ(v)<φ(u). Then q>=ceil((p+3)/2).

              • [1000919] Potential-oriented local bound implies the 2/3 upper bound
                  STATEMENT
                  Assume 50b6278b9537. Then every finite linear 3-graph has at most 3n ascending nonspecial edges. Consequently every n-vertex P_ell^(3)-free linear 3-graph satisfies |E(H)|<=(2ell/3)n.

              • [1000459] Finite falsification search for the potential-oriented local bound
                  STATEMENT
                  Exact induced-path enumeration on 2,250 generated small linear triple systems found no vertex incident as a terminal with four ascending nonspecial edges whose opposite terminals all have endpoint potential at least that vertex's potential. The maximum observed oriented count was three.

              • [1000061] A potential-oriented charged ascending edge can have rank below both terminal potentials
                  STATEMENT
                  There is a six-edge linear 3-graph containing an ascending nonspecial edge e={1,5,6} with φ(e)=3, unique entrance 1, and vertex ranks φ(5)=φ(6)=4. Thus the potential-oriented condition φ(u)≥φ(v) does not force φ(e)=φ(v), even when the two terminal vertex ranks are equal.

              • [1000501] Strict-rise plus equal-level control suffices for the 2/3 leading coefficient
                  STATEMENT
                  Let H be a finite linear 3-graph and T_up its simple terminal-pair graph on the ascending nonspecial edges. Partition E(T_up)=E_< disjoint-union E_= according as the endpoint potentials φ(.) are unequal or equal, and orient each edge of E_< from its lower-potential endpoint to its higher-potential endpoint. Suppose every vertex has strict-rise outdegree at most C and the equal-potential graph T_= has maximum average degree at most D. Then the number A of ascending edges satisfies A<=(C+D/2)|V(H)|. Consequently every n-vertex P_ell^(3)-free linear 3-graph satisfying these two bounds obeys |E(H)|<=((2ell-3+C+D/2)/3)n. In particular any absolute constants C,D give the leading coefficient 2/3; the targets C=2,D=3 give |E(H)|<=(2ell/3+1/6)n.

                • [1000402] Strict potential-rise terminal degree is at most two
                    STATEMENT
                    Let H be a finite linear 3-graph and fix a vertex v. There are at most two ascending nonspecial edges e={x,v,u} for which v is a terminal vertex and the opposite terminal satisfies φ(u)>φ(v).

                  • [1000029] Strict potential rise can occur above the edge rank at both terminals
                      STATEMENT
                      There is a 13-vertex, 10-edge linear 3-graph containing an ascending nonspecial edge e with edge rank φ(e)=4 and terminal vertex potentials 5 and 6. Hence a strict potential rise φ(u)>φ(v) does not force the lower terminal potential φ(v) to equal φ(e).

                • [1000499] Equal-potential ascending terminal graph has maximum average degree three
                    STATEMENT
                    Let H be a finite linear 3-graph. Form the simple graph T_= whose edges are the terminal pairs {u,v} of ascending nonspecial hyperedges satisfying φ(u)=φ(v). Then every nonempty subgraph J of T_= satisfies 2|E(J)|<=3|V(J)|; equivalently mad(T_=)<=3.

                  • [1000164] A dense equal-potential terminal component forces two incident minimum-rank bicircular chords
                      STATEMENT
                      Let J be a connected subgraph of the equal-potential ascending terminal graph T_= on n vertices, and suppose |E(J)|>3n/2. Give each terminal-pair edge the rank of its corresponding ascending hyperedge. Choose, among spanning connected unicyclic subgraphs B of J, one of maximum total rank. Then E(J)\E(B) contains two edges f,g sharing a vertex v. Moreover each excluded edge h is minimum-rank on its fundamental bicircular circuit in B+h. In particular, for each of f and g, the B-edge adjacent to h at the common endpoint v on the fundamental circuit has rank at least phi(h), so h must block every longest terminal-v witness for that adjacent B-edge.

                    • [1000923] Dense equal-potential obstruction reduces to a double-blocked fork or a four-edge charged configuration
                        STATEMENT
                        In the setting of 237ecc9a25b6, let f,g be excluded edges sharing v, and let e_f,e_g be basis edges adjacent at v on their respective fundamental bicircular circuits. Then all of f,g,e_f,e_g are ascending nonspecial edges terminal at v whose opposite terminals have the same vertex rank phi(v), and phi(f)<=phi(e_f), phi(g)<=phi(e_g). Hence exactly one of the following holds: (i) e_f=e_g, in which case one basis edge has two distinct excluded terminal blockers f,g at v on every longest terminal-v witness; or (ii) e_f!=e_g, in which case f,g,e_f,e_g are four distinct potential-charged ascending edges at v, with two distinguished rank inequalities phi(f)<=phi(e_f) and phi(g)<=phi(e_g).

                  • [1000788] Equal-potential ascending terminal graph can contain a rainbow four-edge path
                      STATEMENT
                      The rainbow four-edge path in bdb1eac5484d already lies entirely in the equal-potential ascending terminal graph T_=; its five terminal vertices 9,2,11,10,5 all satisfy φ=5. Hence T_= need not be rainbow-P4-free.

          • [1000958] Unbounded common-last-vertex degree for ascending edges
              STATEMENT
              For every r>=1 there is a finite linear 3-graph containing r+1 ascending edges with a common last vertex. Consequently no absolute bound of the form a(v)<=C+h(v) can hold pointwise, even with h(v)=0.

          • [1001116] Logarithmic common-last-vertex bound for ascending edges
              STATEMENT
              There is an absolute constant C such that, for every finite linear 3-graph H and every vertex v, the number a(v) of ascending edges for which v is a last vertex satisfies a(v)<=C log(φ(v)+2).

            • [1001206] Prefix-excess spacing converts large local switching families into early structural payment
                STATEMENT
                For distinct single entrance contacts on one host path, bounded entrance-prefix excess permits only logarithmically many contacts; quantitatively, #{f:sigma_f<=s}<=4s+7+4 floor(log_2(p+2)). In a selected D+Y switching family, contacts with excess sigma_f>s occupy at least half as many distinct early cells, each yielding either a switcher triangle or a paid output edge in V_{>=p}. Thus a linear selected local family forces one of three macroscopic currencies: terminal-retained contacts, early switcher triangles, or early superlevel output edges.

              • [1000836] A linear selected local family forces U-mass, early triangles, or early superlevel outputs
                  STATEMENT
                  Let P=(g_1,...,g_p) be a maximum p-edge path with last vertex v, and let F be a family of k distinct selected strict-gap switching edges through v from the local D+Y certificate system, each single on P. Split
                    F = X disjoint_union U,
                  where X consists of edges whose unique off-v contact on P is their entrance, and U consists of edges whose unique contact is the opposite terminal.
                  
                  Put
                    C_p = 7+4 floor(log_2(p+2)).
                  Then at least one of the following holds:
                  (1) |U| >= k/2;
                  (2) there are at least k/16-C_p/4-O(1) distinct early doubly occupied certificate cells, hence that many linear switcher triangles;
                  (3) there are at least k/16-C_p/4-O(1) distinct early paid certificate cells with distinct standard output edges contained in V_{>=p}.
                  
                  In (2) and (3), all counted cells have standard output index at most
                    p-floor(k/16).
                  Consequently, whenever k=Omega(p), one of the three displayed currencies is Omega(p).

            • [1000145] Four-edge spacing conjecture at a common last vertex
                STATEMENT
                Let e_1,e_2,e_3,e_4 be four ascending nonspecial edges having a common last vertex v, ordered so that q_i=φ(e_i) satisfies q_1<=q_2<=q_3<=q_4. Then 2q_2>=q_1+q_4+1. A stronger form with +3 is suggested by the clean common-path model and by the known extremal constructions.

              • [1000066] Slack-corrected spacing for clean entrance contacts
                  STATEMENT
                  Let e_1,e_2,e_4 be ascending nonspecial edges with common last vertex v and q_i=φ(e_i), where q_1<=q_2<=q_4. Let Q=(g_1,...,g_M) be the precursor of a q_4-edge path ending with e_4 at v, so M=q_4-1 and e_4 meets Q only at its entrance in g_M. Suppose for i=1,2 that e_i meets Q only at its entrance x_i, that x_i lies in exactly one edge g_{j_i}, and j_1+2<=j_2. Put s_i=(q_i-1)-j_i. Then 2q_2>=q_1+q_4+3+s_2-s_1.

              • [1000104] Cross-blocker reduction for four-edge spacing
                  STATEMENT
                  Let e_1,e_2,e_4 be ascending nonspecial edges with common last vertex v and q_1<=q_2<=q_4. Let Q=(g_1,...,g_M) be the precursor of a q_4-edge path ending with e_4 at v, where M=q_4-1. Let x_i be the entrance of e_i. Suppose e_2∩V(Q)={x_2}; let b be the last index of an edge of Q containing x_2. Suppose also that e_1 is disjoint from V(g_b∪...∪g_M), and that there exists a (q_1-1)-edge path R with last vertex x_1, not using e_1, such that V(R)∩e_1={x_1}, and R is disjoint from e_4 and from V(g_b∪...∪g_M). Then 2q_2>=q_1+q_4+2.

              • [1000950] Four-edge spacing implies logarithmic common-last-vertex degree
                  STATEMENT
                  Assume the four-edge spacing inequality 2q_2>=q_1+q_4+1 holds whenever four ascending nonspecial edges share a last vertex. Then if k ascending edges share a last vertex v and p is the largest of their φ-values, k<=3+ceil(log_2(p+1)).

              • [1000403] Uncrossed splice gives four-edge spacing
                  STATEMENT
                  Let e_1,e_2,e_4 be ascending nonspecial edges of a linear 3-graph sharing a common last vertex v, with q_i=φ(e_i) and q_1<=q_2<=q_4. Let x_i be the unique entrance of e_i. Let P_4 be a q_4-edge path ending in e_4 with last vertex v, and suppose x_2 lies on P_4. Let Q_1 be a (q_1-1)-edge path ending at x_1 such that Q_1,e_1 is a longest path ending in e_1. If Q_1,e_1,e_4 followed by the reverse tail of P_4 from the edge preceding e_4 down to x_2 is a linear path, then 2q_2>=q_1+q_4+2. If x_2 is private to a single edge of P_4, the stronger bound 2q_2>=q_1+q_4+3 holds.

              • [1000540] Two-contact counterexample to four-edge spacing
                  STATEMENT
                  The four-edge spacing conjecture 1ff3a09b18b7 is false. There is a linear 3-graph with four ascending nonspecial edges sharing one last vertex and having φ-values 12,16,20,20, so 2q_2=32<33=q_1+q_4+1.

              • [1001034] Four common-last ascending edges can have values 11,11,17,17
                  STATEMENT
                  There is a finite linear 3-graph with four ascending nonspecial edges having a common last vertex and ordered φ-values (11,11,17,17). Hence even the weakened four-edge midpoint inequality 2q_2>=q_1+q_4 is false.

                • [1000455] Human counterexample to the 368-extension search around the 11,11,17,17 gadget
                    STATEMENT
                    The finite-search statement bce2e76b5733 is false. In the base configuration e56c6d0fce1a, adjoining G={v,a_13,c_4} with c_4 new gives five ascending nonspecial edges E_17,F_1,F_2,F_3,G with common last vertex v and ordered ranks (11,11,14,17,17).

                • [1000754] Human classification of one-private-contact fifth edges around the 11,11,17,17 gadget
                    STATEMENT
                    In the 11,11,17,17 base configuration e56c6d0fce1a, no legal fifth edge G={v,b_j,c} with c new and b_j a single private precursor vertex can make G together with E_17,F_1,F_2,F_3 all ascending nonspecial with common last vertex v.

            • [1000380] Terminal φ-values of an ascending edge are comparable
                STATEMENT
                Let e={x,u,v} be an ascending nonspecial edge of a linear 3-graph, with unique entrance x and q=φ(e). Then |φ(u)-φ(v)|<=q-1. In particular max{φ(u),φ(v)}<2 min{φ(u),φ(v)}.

            • [1000494] Five-edge deficit-doubling conjecture
                STATEMENT
                Let e_1,...,e_5 be five ascending nonspecial edges having a common last vertex v, ordered so that q_i=φ(e_i) satisfies q_1<=...<=q_5. Then 2q_4>=q_1+q_5+1.

              • [1000680] Five-edge deficit doubling implies logarithmic common-last-vertex degree
                  STATEMENT
                  Assume the five-edge deficit-doubling inequality 2q_4>=q_1+q_5+1 for every five ascending nonspecial edges with a common last vertex. If k such edges share a last vertex and p is the largest of their φ-values, then k<=3 floor(log_2 p)+4 for p>=1.

        • [1000541] Sublinear common-last-vertex control suffices for the 2/3 leading coefficient
            STATEMENT
            Let H be an n-vertex P_ell^(3)-free linear 3-graph, let A be the number of ascending edges, and for each vertex v let c(v) be the number of ascending edges for which v is a last vertex. Suppose g is nondecreasing and c(v)<=g(φ(v)) for every v. Then A<=n g(ell-1)/2 and |E(H)|<=((2ell-3)/3+g(ell-1)/6)n. In particular, any uniform bound c(v)=O(φ(v)^alpha) with fixed alpha<1 implies ex_L(n,P_ell^(3))<=(2ell/3+O(ell^alpha))n, and any c(v)=o(φ(v)) gives leading coefficient 2/3.

        • [1000844] Ascending terminal graph can contain a rainbow four-edge path
            STATEMENT
            There is a finite linear 3-graph whose terminal-pair graph restricted to ascending edges, colored by the unique entrance vertex of each edge, contains a rainbow path of four edges. Thus the global ascending-edge bound cannot be reduced to forbidding rainbow four-edge paths in that terminal graph.

      • [1000611] Degree-scope fence for rainbow arguments
          STATEMENT
          Keep the original-hypergraph minimum degree and the properly edge-colored shadow-graph minimum degree as separate, simultaneously useful hypotheses. A rainbow-path theorem stated for minimum degree applies to the derived graph degree delta(J), not to the hypergraph degree delta(H). Do not discard delta(H): it remains available for hypergraph-side dense-core, peeling, attachment, and special-edge arguments.

    • [1000671] Rotation-expansion route for forcing special-edge density
        STATEMENT
        Use Pósa-style rotations of longest linear paths to turn the snake digraph's terminal incidences into an endpoint-expansion argument. The target is a quantitative dichotomy: after discarding O(n) low-rank or star-like mass, a positive fraction of hyperedges should admit longest paths entering through at least two labels, hence be special.

      • [1000341] P-scale rotation-closure via deletable blocker endpoints
          STATEMENT
          Let H be a finite linear 3-graph and let P be a globally longest p-edge path. Conjecturally, the rotation component of P satisfies a Pósa-type p-scale expansion principle: if reachable terminal vertices repeatedly have degree above p, then repeated length-preserving rotations force either many distinct reachable terminal pairs or many distinct original private path vertices that are absent from some reachable maximum path. In particular, persistent failure of such closure should force terminal degree back to p+O(1), rather than the 2p scale of fixed-path contact counting.

        • [1000712] Amortized distinct-deletion rotation closure
            STATEMENT
            Let H be a finite linear 3-graph and let P be a globally longest p-edge path. Suppose a reachable maximum-path state has a terminal vertex v with d(v)>=p+t. Then, unless the rotation component already contains Omega(t) distinct reachable terminal pairs, there is a sequence of length-preserving one-edge rotations that omits Omega(t) distinct original private vertices of P without immediately restoring more than a bounded fraction of earlier omissions. Each newly omitted private vertex that was used by a double off-v contact destroys one distinct blocker contact, converting that edge into a latent singleton exchange for any later reachable state in which its surviving contact is terminal. In particular, persistent degree excess above p should force rotation-component expansion at p-scale rather than 2p-scale.

      • [1000629] Terminal-pair cycle-rank reduction
          STATEMENT
          Let H be an n-vertex P_ell^(3)-free linear 3-graph with m edges, s special edges, and b=m-s nonspecial edges. For each nonspecial edge e with unique entrance u(e), put the terminal pair e\{u(e)} as an edge of a simple graph T. If the cycle rank beta(T)=|E(T)|-|V(T)|+c(T) satisfies beta(T)<=C s+D n for constants C,D>=0 independent of ell, then m <= [2(C+1)ell-3(C+1)+D+1]/(2C+3) * n. Hence every fixed C,D gives leading coefficient 2(C+1)/(2C+3)<1.

      • [1000266] Refuted: terminal-pair cycle rank is controlled by special edges
          STATEMENT
          Refuted. It is not true that beta(T)<=s for the terminal-pair graph T of nonspecial edges and the number s of special hyperedges. The family c3e95f4ce77d has s=0 while its terminal-pair graph is t disjoint copies of K_{3,3}, so beta(T)=4t.

        • [1000657] Terminal adjacency forces rank rise or a blocker
            STATEMENT
            Let e,f be distinct nonspecial edges of a linear 3-graph, sharing a vertex v that is terminal for e and also terminal for f. Let t=phi(e), and choose a t-edge path P ending in e with physical terminal v. If f meets P only in v, then appending f gives a (t+1)-edge linear path ending in f through the entrance label v; hence phi(f)>=t+1. Consequently, if phi(f)<=phi(e), every longest path witnessing v as a terminal of e must meet f in a second vertex. In particular, on any cycle of the terminal-pair graph, every edge of minimum rank blocks both neighboring terminal witnesses in the corresponding incoming directions.

          • [1001021] Terminal blocker contact-count bound
              STATEMENT
              Let e,f be distinct nonspecial edges of a linear 3-graph sharing a vertex v that is terminal for both. Put p=φ(e), q=φ(f), assume q<=p, and let P be a p-edge path ending in e with last vertex v. If r is the number of distinct vertices of f that occur on P, then 2<=r<=3 and p<=r(q-1). In particular, if p>=2q-1 then all three vertices of f occur on P.

          • [1000086] Unblocked shared-last-vertex extension raises φ by two
              STATEMENT
              Let e and f be distinct nonspecial edges of a linear 3-graph sharing a vertex v. Assume φ(e,v)=φ(e) and φ(f,v)=φ(f), and that v is not the unique entrance vertex of either edge. Let P be a longest path with last edge e and last vertex v. If f meets P only at v, then φ(f)>=φ(e)+2.

        • [1000781] Maximum-rank forest gives canonical blocker chords
            STATEMENT
            Let T be the terminal-pair graph of the nonspecial edges of a linear 3-graph, weighted by hyperedge rank φ(e). Choose a spanning forest F of T with maximum total rank. Then every nonforest edge f is a minimum-rank edge on its fundamental cycle C_f, and the number of nonforest edges is β(T). Hence each unit of cycle rank has a canonical representative f whose two fundamental-cycle neighbors have rank at least φ(f) and must block longest-path witnesses for those neighbors through the corresponding shared terminal vertices.

      • [1000728] Two-contact rotation of a linear path
          STATEMENT
          Let P=(e_1,...,e_p) be a linear path and let f be an edge outside P meeting P exactly in e_j and e_p, with 1<=j<p. If j<=p-2, then (e_1,...,e_j,f,e_p,e_{p-1},...,e_{j+2}) is a p-edge linear path. If j=p-1, then (e_1,...,e_{p-1},f) is a p-edge linear path.

        • [1000037] A two-contact competitor either meets the penultimate edge or meets early
            STATEMENT
            Let e be a nonspecial edge with φ(e)=p and unique entrance vertex x. Let P=(e_1,...,e_p) be a longest path with last edge e and last vertex v, where v≠x. Let f be an edge not in P that contains v and meets exactly two edges of P, namely e_j and e_p=e. Then either j=p-1 or j≤p-3.

        • [1000360] Single-blocker rotation and forbidden penultimate-predecessor slot
            STATEMENT
            Let P=(e_1,...,e_L) be a linear path with last vertex z in e_L, and let f∉P contain z. Suppose f has exactly one further vertex w on V(P)\e_L. Let j be the first index of a path edge containing w. Then if j<=L-2, the sequence (e_1,...,e_j,f,e_L,e_{L-1},...,e_{j+2}) is an L-edge linear path; if j=L-1, then (e_1,...,e_{L-1},f) is an L-edge linear path. If moreover P is globally longest, e_L is nonspecial with unique entrance x, and z≠x is a terminal vertex of e_L, then j≠L-2.

      • [1000046] Terminal-cycle rank controls nonspecial incidence nullity up to entrance rank
          STATEMENT
          Let H be a finite linear 3-graph, let E_ns be its nonspecial edges, and let T be the terminal-pair graph of E_ns. Let N_ns be the vertex-edge incidence matrix restricted to E_ns, and let h be the number of distinct entrance vertices among E_ns. Then nullity_R(N_ns)<=β(T)+h. Consequently, if H has s special edges and full incidence matrix N, then nullity_R(N)<=β(T)+h+s<=β(T)+n+s.

• [archive01] Archive
    STATEMENT
    ‹none›

  • [proof_rehearsals] Proof Rehearsals
      STATEMENT
      ‹none›

    • [1001169] Proof rehearsal 6 — 2026-09-25 02:19 UTC
        STATEMENT
        Under 43/48 near-extremality, 7ac951de82f4 and bee5f8c756bb give Omega(S) DISTINCT paid-certified source-clean U_11 edges that are minimum-rank nonforest chords of clean fundamental terminal cycles. For each such chord, 42f99fb3835e forces adjacent source-rail theta/multiple-overlap, outer-rail intersection, or two late aligned gates; in the fully flat gap-one cycle subcase f435dfa310db further forces a balanced entrance-rail lens. The current certified state does not globalize these local certificates: there is no bounded-reuse/telescoping theorem showing that the aggregate number of these theta/intersection/lens/late-gate certificates is O(eta+n_+) (or otherwise o(S) when eta=o(S)). This global clean-cycle certificate packing is now the first unsupported inference. It is later and more specific than raw endpoint reuse or center-indexed paid-object congestion, because the paid family is already distinct at the hyperedge level.

    • [1001170] Proof rehearsal 7 — 2026-09-25 11:21 UTC
        STATEMENT
        From the certified lower bound sum_v(D_v^cell+I_v) >= (1/8-o(1))S in every 43/48 near-extremal sequence, prove a global reuse/congestion inequality for the center-indexed switcher triangles and distinct output edges internal to each center superlevel, for example sum_v(D_v^cell+I_v)=O(eta+n_+), or any bound ruling out positive-linear mass when eta=o(S) and n_+=o(S). The certified result 619d7583671c only charges distinct flat no-rise terminal incidences after deduplication and does not control center multiplicity of these paid objects.

    • [1001171] Proof rehearsal 8 — 2026-09-25 19:06 UTC
        STATEMENT
        There exists a universal g(p)=o(p) such that every rank-p vertex is the minimum-rank terminal of at most g(p) source-clean, doubly-terminal-single, paid-certified ascending nonspecial edges whose edge rank is strictly below both terminal vertex ranks.

    • [1001172] Proof rehearsal 9 — 2026-09-25 19:40 UTC
        STATEMENT
        For a rank-p center v with k source-clean, doubly-terminal-single, paid-certified strict-two-terminal-gap edges assigned to v as a minimum-rank terminal, the certified local consequences do not yet imply k=o(p). 59c5795520ff forces k distinct opposite terminals of rank at least p and a disjoint entrance packet with total rank at least (p/2)k+k(k-1)/8; a47f1ec7709f further forces Omega(k) same-label vertices lying simultaneously on two source rails and hence two balanced endpoint lenses per label; 5a5ceede5e3f adds clean fundamental-cycle blockers. The unsupported step is to bound global reuse/congestion of these high-rank vertices, lens states, or forest-branch blocker certificates strongly enough to convert those local packets into k=o(p). Without such a packing theorem the same off-center high-rank structure may be reused across many centers, so summing local Omega(p k+k^2) rank mass is unjustified.

    • [1001173] Proof rehearsal 12 — 2026-09-25 22:27 UTC
        STATEMENT
        To invoke a54a1a6159e1 and contradict 43/48, one must prove a function g(p)=o(p) bounding, at every rank-p minimum terminal, the number of assigned source-clean doubly-terminal-single strict-gap ascending edges that carry a selected common-anchor D+Y certificate at either terminal. The certified split 9e490cc47ca8 reduces this to separate o(p) bounds for class S (certificate at a minimum-rank terminal) and class H (certificate only at the strictly higher-rank terminal). Current certified fundamental-cycle, repeated-intersection, U_11 collision, and fixed-cut cycle-packing lemmas do not yet imply either sublinear degree bound.

    • [1001174] Proof rehearsal 13 — 2026-09-26 04:03 UTC
        STATEMENT
        For every rank-p vertex w, the number of strict-gap source-clean terminal-single ascending edges assigned to w as a minimum-rank terminal and carrying a selected common-anchor D+Y certificate at either terminal is o(p), uniformly over the relevant chosen maximum endpoint paths. Equivalently, both the same-terminal certified class and the uphill-certified class from 9e490cc47ca8 require sublinear assigned local congestion bounds. The certified uphill structural split 25b5948e8d37 does not yet supply such a bound.

    • [proof_rehearsal_g000000000014] Proof rehearsal 14 — 2026-10-01 19:57 UTC
        STATEMENT
        ‹none›

    • [proof_rehearsal_g000000000015] Proof rehearsal 15 — 2026-10-01 21:36 UTC
        STATEMENT
        ‹none›

• [project_policy] Project-specific policy
    STATEMENT
    ‹none›

• [proof_rehearsals01] Comprehensive Proof Rehearsals
    STATEMENT
    Organizational home for one comprehensive synthesis rehearsal per major conceptual LINP proof route.

  • [linp_route01] Route 1 — Snake/contact-defect and post-43/48 stability
      STATEMENT
      Comprehensive synthesis of the direct snake/contact-accounting route from the rank-sensitive 43/48 theorem through near-extremal switching, paid strict-gap structure, and the current global-reuse closure gap.

  • [linp_route02] Route 2 — Dense-core all-special / ascending-edge rank flow
      STATEMENT
      Comprehensive synthesis of the two-thirds upper-bound program based on dense-core normalization, elimination of nonspecial ascending edges by rank layers, and all-special closure.

  • [linp_route03] Route 3 — Rotation-expansion and terminal-pair cycle rank
      STATEMENT
      Comprehensive synthesis of the Pósa-style rotation and terminal-pair graph route for forcing special-edge density or bounded cycle complexity.

  • [linp_route04] Route 4 — Incidence rank / induced-path clique-cover
      STATEMENT
      Comprehensive synthesis of the algebraic upper-bound route through the incidence matrix, induced-path-free intersection graph, exact clique-cover realizability, and weighted/nullity rank inequalities.

  • [linp_route05] Route 5 — Inductive longest-path pair capacity with outside defect
      STATEMENT
      Comprehensive synthesis of the one-third induction route that removes a longest path and pays all incident edges from internal pair capacity, path slack, and the outside extremal defect.

  • [linp_route06] Route 6 — Algebraic/Steiner lower constructions and spanning-path obstructions
      STATEMENT
      Comprehensive synthesis of the algebraic lower-bound program using Steiner/projective/affine/additive systems, path-sum invariants, carrier reductions, and the major Hamiltonicity fences.

  • [linp_route07] Route 7 — Transversal/Latin/blow-up/product lower constructions
      STATEMENT
      Comprehensive synthesis of the lower-bound route through transversal designs, properly colored lifts, fixed-template Latin blow-ups, shared-color constructions, and products.

  • [linp_route08] Route 8 — Global/symmetric 2-shadow and strong-rainbow translation
      STATEMENT
      Comprehensive synthesis of the representation-level upper route through the properly edge-colored 2-shadow, source-oriented directed/rainbow coupling, and the full symmetric strong-rainbow formulation.

• [research_nudges] Research nudges
    STATEMENT
    Strongly encouraged project-local research heuristics. Researchers must seriously consider the applicable nudges as default methodological priors, but may depart from them when mathematical judgment gives a reason.

• [research_retrospectives] Research retrospectives
    STATEMENT
    Asynchronous retrospective epochs for mining general research lessons from major results, failures, and periodic review.

  • [1000042] Major-result retrospective epoch 4
      STATEMENT
      Major-result retrospective for the lens-free repair cascade and the fixed-cut collision packing result. The episode reinforces existing research nudges on isolating failed auxiliary premises, preserving witness provenance, globalizing local certificates, and auditing high-fanout premises; no new nudge is added.

  • [1000130] Major-result retrospective epoch 5
      STATEMENT
      The latest lens-free and collision progress reinforces exact-equality and route-salvage methodology, and adds one new general nudge: boundary conventions must not be mistaken for the geometric witnesses required by downstream arguments.

  • [1000317] Major-result retrospective epoch 3
      STATEMENT
      Major-result retrospective for the arbitrary-uniformity single-contact central-window theorem and its immediate descendants; existing research nudges already capture the general lessons, so no new nudge is added.

  • [1000600] Periodic retrospective epoch 1
      STATEMENT
      Periodic retrospective epoch 1 synthesized and closed.

  • [1000886] Periodic retrospective epoch 2
      STATEMENT
      Periodic retrospective epoch 2 synthesized and closed.

• [scheduler_guidance] Scheduler guidance
    STATEMENT
    ‹none›

• [standardization_dictionary] Standardization dictionary
    STATEMENT
    ‹none›

• [methods01] Toolkit
    STATEMENT
    Reserved top-level home for project-level reusable mathematics, definitions, methods, fences, abstractions, and imported toolkits. It is organizational rather than a proof inference.

  • [1000750] External toolkit for structured lower-bound constructions
      STATEMENT
      A curated toolkit for the LINP lower-bound program: edge-ordered path-suppressing constructions, antipodal cube obstructions, hypergraph Hall/Ryser matching machinery, and combinatorial fixed-point equivalences. Each child records an exact reusable statement, proof or proof architecture, source, and a LINP translation.

    • [1000689] Combinatorial-topology and matching toolkit
        STATEMENT
        A compact reusable package of certified fixed-point, antipodal-state-space, and hypergraph matching tools used by LINP: the Sperner--Connector--Hex--Pouzet--Brouwer cycle, Tucker/Borsuk--Ulam, the Norine antipodal-coloring toolkit and its local reductions, and the Aharoni--Haxell/Ryser matching package.

      • [1000115] Sperner--Connector--Hex--Pouzet--Brouwer equivalence toolkit
          STATEMENT
          Sperner's lemma, the Hochberg--McDiarmid--Saks Connector Theorem, multidimensional Hex, Pouzet's lattice-direction lemma, and Brouwer's fixed-point theorem form a short implication cycle. The discrete middle of the cycle is especially reusable for finite path-state spaces.

      • [1000890] Tucker lemma and the Borsuk--Ulam bridge
          STATEMENT
          Tucker's combinatorial lemma is the antipodal analogue of Sperner: an antipodally labeled triangulated ball must contain a complementary edge. It is equivalent to the no-antipodal-extension form of Borsuk--Ulam and supplies a finite sign-label obstruction well suited to combinatorial state spaces.

      • [1001015] Norine antipodal-coloring toolkit
          STATEMENT
          Norine's conjecture is now a theorem: every antipodal red--blue edge-coloring of Q_n, n>=2, has a monochromatic path joining a vertex to its antipode. For LINP the reusable pieces are the component-to-rook-labeling reduction, low-dimensional square/cube forcing, and the general antipodal obstruction.

        • [1000704] Counterexample to Norine gives a rook labeling
            STATEMENT
            If an antipodal red--blue coloring of Q_n has no monochromatic antipodal path, then after enlarging dimension if necessary it yields an antipodally symmetric rook labeling q:V(Q_K)->Omega_K: antipodes swap the two label coordinates, and adjacent cube vertices agree in at least one coordinate.

        • [1000581] Low-dimensional cube forcing before the general Norine proof
            STATEMENT
            Before the 2026 general proof, simple square constraints and explicit Q_4--Q_6 analyses already forced monochromatic antipodal paths. These local cube mechanisms are retained because they are more likely than the final chain construction to port directly to finite LINP state spaces.

      • [1000407] Aharoni--Haxell hypergraph Hall toolkit
          STATEMENT
          A family of hypergraphs has disjoint representatives if every subfamily has matching width at least its cardinality. A deficiency form gives a large partial system of disjoint representatives when the inequality is allowed a fixed deficit.

      • [1000052] Ryser for 3-partite 3-graphs from Aharoni--Haxell and Konig
          STATEMENT
          Every 3-partite 3-uniform hypergraph H satisfies tau(H)<=2 nu(H). A short derivation follows from the Aharoni--Haxell deficiency theorem applied to bipartite link graphs, together with Konig's theorem.

    • [1000835] Calderbank--Chung--Sturtevant monotone-path suppression
        STATEMENT
        There are edge orderings of K_n for which every increasing simple path has length at most (1/2+o(1))n. For n=2^k the construction is algebraic over F_2^k and converts simple increasing paths into increasing vector sequences with no zero consecutive block sum.

    • [1000849] Porting map from the external toolkit into LINP constructions
        STATEMENT
        The imported tools suggest four concrete construction/obstruction interfaces for improving the lower bound: algebraic ordered transitions, antipodal state complexes, disjoint-representative connector packing, and fixed-point direction labels. These are proposals for experiments, not established LINP implications.

      • [1000871] Diagonal products as a possible amplifier of the P5 lower construction
          STATEMENT
          For linear 3-graphs H,K define the diagonal product H tensor K on V(H)xV(K) by taking, for every e in E(H), f in E(K), and every bijection sigma:e->f, the triple {(u,sigma(u)):u in e}. This product is linear and has |V|=|V(H)||V(K)| and |E|=6|E(H)||E(K)|. For the 11-vertex 15-edge P5-extremal component G0, its t-fold diagonal power has edge/vertex ratio (1/6)(90/11)^t. Determine the growth of its maximum linear-path length L_t. If (|E|/|V|)/(L_t+1)>1/3+epsilon for infinitely many t, this gives a genuine leading-coefficient lower-bound improvement.

        • [1000814] The diagonal square of G0 already contains P33
            STATEMENT
            Let G0 be the 11-vertex 15-edge P5-extremal linear triple system represented by a 1-factorization of K6 with five centers. Then the diagonal product G0 tensor G0 contains a 33-edge linear path. Consequently its first forbidden path length is at least 34, and since it has 121 vertices and 1350 edges, its normalized density at its first forbidden length is at most 1350/(121*34)=675/2057<1/3. Thus the diagonal square does not improve the asymptotic 1/3 benchmark.

        • [1000961] The diagonal product C7 tensor C7 has maximum path length at most 81
            STATEMENT
            Let C7 be the 3-uniform linear seven-cycle. In the diagonal product C7 tensor C7, every linear path has at most 81 edges. More generally, if C_s is a linear s-cycle and a path in C_s tensor C_s has L edges, then a simple type count gives 3L <= 5s^2-1, hence L <= floor((5s^2-1)/3). For s=7 this gives L<=81. Thus the natural C7 tensor C7 subproduct cannot supply the 97-edge path needed to fence PG(3,2) tensor PG(3,2); instead it exhibits substantial path suppression under diagonal product.

    • [1000498] Any set of pair-universal vertices generates a dense strong-rainbow matching graph
        STATEMENT
        Let Z be pair-universal vertices in a linear triple system. For every A subseteq Z of size a<=(n-1)/2, the hyperedges with one vertex in A and two in B=V\A define a properly edge-colored graph G_A on B, colored by A, with |E(G_A)|>=a(n-2a+1)/2. Every rainbow path in G_A lifts to a linear hypergraph path because the color set A is disjoint from the graph vertex set.

    • [1000241] The new projective proof explains exactly the d=3 and d=4 exceptional dimensions
        STATEMENT
        For the full projective additive system H_d on F_2^d\{0}, any spanning path has joint XOR zero. For d=3 this is already impossible because a spanning P_3 would have two distinct joints. For d=4 rank-nullity forces the six joints to split into two complementary lines, and the 3-by-3 residue grid gives the endpoint contradiction. Beginning at d=5 this proof mechanism cannot yield a universal obstruction: PG(4,2) has a spanning P_15, and in the displayed witness its 14-joint set even contains a zero-sum triple {2,31,29}; the remaining 11 joints also sum to zero, showing precisely why the two-line collapse disappears.

  • [1001175] Maximum-path structural toolkit
      STATEMENT
      Reusable lemmas about maximum endpoint paths: endpoint-preserving rotations, terminal-contact packing, and rigid intersection geometry.

    • [1000016] A loss-one double-blocker splice creates a canonical two-cycle
        STATEMENT
        In the boundary setting q=δ, let Q=(g_1,...,g_t), t=q-1, be an x-ending path avoiding y,z, with cells A_i={b_i,c_i}. Suppose a double blocker h through an opposite last vertex a has blockers u∈A_i and b_{i+2}∈A_{i+2}, so the exact splice loss is one. Then the resulting (t-1)-edge x-ending path P_0 admits a forced safe single-blocker rotation using the omitted edge g_i, producing a second (t-1)-edge x-ending path P_1; in P_1 the omitted edge g_1 is a forced safe single blocker and rotating by g_1 returns to P_0. Thus the obvious safe repair of a loss-one chord is a canonical two-state rotation cycle, and any proof of further progress must use another endpoint or another incident edge.

    • [1000058] Flat shared-last-edge states have half-density in the terminal-contact window
        STATEMENT
        Let P=(g_1,...,g_p) be a maximum endpoint path with last vertex v. Let F be a family of distinct ascending nonspecial edges
          e_i={x_i,v,u_i}
        such that:
        - v is terminal at e_i;
        - phi(e_i)=q_i<p<=phi(u_i);
        - the unique off-v contact of e_i with P is u_i;
        - for each i there is a maximum p-edge path Q_i ending at u_i whose last edge is an internal host edge g_{j_i}, and Q_i enters g_{j_i} through the forward joint
            z_{j_i}=g_{j_i} intersect g_{j_i+1};
        - g_{j_i} is nonspecial ascending of edge rank p with unique entrance z_{j_i}.
        
        For Q<p let
          F_{<=Q}={e_i in F:q_i<=Q}.
        Then
          |F_{<=Q}| <= max(0,2Q-p-1).
        
        Consequently, if q_1<=...<=q_k are the edge ranks in F, then
          q_i >= ceil((p+i+1)/2)
        for every i.
        
        In particular, the host edges g_{j_i} supporting these flat states occupy pairwise nonconsecutive indices.

    • [1000106] Four equal-length maximum paths cannot form a chordless cycle of unique intersections
        STATEMENT
        Let A,B,C,D be maximum endpoint paths of the same length L. Suppose
          |V(A) intersect V(B)|=|V(B) intersect V(C)|=|V(C) intersect V(D)|=|V(D) intersect V(A)|=1,
        while
          V(A) intersect V(C)=V(B) intersect V(D)=emptyset.
        Then no such four paths exist.

    • [1000146] Unique auxiliary intersections of crossing endpoint lenses preserve potential-minus-position slack
        STATEMENT
        Let P be a maximum p-edge path ending at v. Let balanced endpoint lenses for retained vertices c,d have crossing host intervals [a,c] and [b,d] with a<b<c<d, and let P_c,P_d be the corresponding maximum endpoint paths ending at c,d. Let kappa_P(c),kappa_P(d) denote the host-prefix edge counts to the chosen occurrences of c,d on P. Suppose the two off-host lens sides have a clean intersection w and that w is the unique common vertex of the full maximum paths P_c and P_d. Then
        phi(c)-kappa_P(c)=phi(d)-kappa_P(d).
        Consequently, for a crossing pair of balanced endpoint lenses, either P_c and P_d have at least two common vertices, or their endpoint slack phi(.)-kappa_P(.) is equal.

    • [1000174] Uphill 0-1-1 edges are repeated-intersection or aligned X-X
        STATEMENT
        Let e={x,v,u} be an ascending nonspecial edge of rank q with unique entrance x and terminals v,u. Assume
          q<phi(v)=p<phi(u)=s.
        Let P_v and P_u be chosen maximum endpoint paths ending at v and u, respectively, and assume e is terminal-single on both paths.
        
        On P_v, exactly one of {x,u} occurs off v; call the lower-terminal contact type X if x occurs and U if u occurs.
        On P_u, exactly one of {x,v} occurs off u; call the higher-terminal contact type X if x occurs and V if v occurs.
        
        Then:
        
        (1) If the type is U-X, U-V, or X-V, the two maximum paths P_v and P_u have at least two common vertices.
        
        (2) The only type for which P_v and P_u can have a unique common vertex is X-X. In that case, if
          V(P_v) intersect V(P_u)={x},
        then x is a joint on both paths at the same path index.
        
        Thus every uphill strict-gap doubly-terminal-single edge either carries an explicit repeated-intersection certificate between its two terminal maximum paths, or is in the rigid X-X aligned-joint state.

    • [1000187] Exact saturated-fan normal form at the boundary q=δ
        STATEMENT
        In the setting of e5859985e51b, let e={x,y,z} be ascending nonspecial with q=φ(e)=δ, let Q=(g_1,...,g_{q-1}) be a maximum path ending at x and avoiding y,z, let a be the opposite last vertex, and assume Q has no safe single-blocker rotation avoiding y,z. Then the blocker sets of the q-1 edges through a other than g_1 are pairwise disjoint subsets of V(Q)\g_1 of sizes one or two. If S=2, they partition V(Q)\g_1 exactly; the two single blockers occupy exactly two of the three exceptional types {blocker x, contains y, contains z}. If S=3, they cover all but one vertex of V(Q)\g_1, and the three single blockers are exactly one of each exceptional type.

    • [1000285] A saturated terminal star nearly realizes the period-four singleton extremizer on the opposite source rail
        STATEMENT
        Let e={x,u,v} be an ascending nonspecial edge of rank q>=4 and let R be a canonical (q-1)-edge source rail of e. Fix one terminal w in {u,v}, and assume q is the maximum rank of an ascending nonspecial edge terminal at w.
        
        Let t(w) be the number of ascending nonspecial edges terminal at w and put delta_w=gamma(q)-t(w)>=0, where gamma(q)=floor((11q-5)/8).
        
        Relative to R, classify the t(w)-1 ascending terminal competitors f!=e as single-contact or double-contact edges, with counts S_w,B_w, and let U_w count vertices of W=V(R) minus {x} unused by all these competitors. Put alpha(q)=ceil((3q-8)/4) and kappa_q=alpha(q)-2gamma(q)+2q. Then kappa_q belongs to {0,1}, and
        alpha(q)-kappa_q-2delta_w <= S_w <= alpha(q),
        0 <= U_w <= kappa_q+2delta_w <= 2delta_w+1.
        
        Thus if delta_w=o(q), the terminal star has S_w=(3/4+o(1))q single blockers on R and leaves only o(q) rail vertices unused. If e is maximum-rank at both terminals u,v and both deficits are o(q), the same source rail simultaneously supports two near-extremal period-four singleton patterns, one from each terminal star.

    • [1000369] A genuine balanced lens has length at least two
        STATEMENT
        Let H be a simple linear hypergraph. Let Q and R be linear paths having a genuine clean balanced lens between distinct boundary vertices a,b, with Q-side and R-side internally vertex-disjoint and distinct. If the common side length is t, then t>=2.
        
        Consequently, every balanced endpoint lens supplied by b35b0fd4e4cd that has genuinely distinct host and auxiliary sides uses at least two host edges and at least two auxiliary edges.

    • [1000394] Terminal-safe sinks have endpoint deficiency at most two
        STATEMENT
        Let H be a linear 3-graph of minimum degree δ, let P=(g_1,...,g_s) be a linear path ending at x, let a be a last vertex of g_1 at the opposite end, and fix y,z outside V(P). If at a there is neither a safe clean extension avoiding y,z nor a safe single-blocker rotation avoiding y,z, then δ-s≤2. Consequently, if a double-blocker splice produces an x-ending path avoiding y,z with loss d from a (δ-1)-edge entrance path in the boundary case q=δ, then every loss d≥2 state admits another safe clean extension or safe single rotation; only loss d=1 can be a local sink.

    • [1000412] No third path can pierce a balanced lens between maximum rails
        STATEMENT
        Let two maximum endpoint paths contain a clean internal lens with equal-length sides. No nontrivial third path can have a clean subpath joining an interior vertex of one lens side to an interior vertex of the other. The two complementary hybrid replacements have total length larger than the two original lens sides by twice the third-segment length, so one replacement beats a maximum endpoint path.

      • [1000493] No third path can cleanly pierce any clean lens between maximum endpoint paths
          STATEMENT
          Let Q,R be maximum endpoint paths and let two common vertices bound any clean lens between them, with arbitrary side lengths A,B. No third path can cleanly pierce from the interior of one lens side to the interior of the other. The two complementary hybrids have total length A+B+2l; if one does not beat the Q-side length A, the other necessarily beats the R-side length B. Thus the earlier no-piercing theorem does not require a balanced lens.

    • [1000530] Every whole chord on a canonical common anchor has a second source-rail intersection
        STATEMENT
        Let
          h={y,v,w}
        be an ascending nonspecial edge of rank q with unique entrance y and terminal v, and let
          R=(g_1,...,g_{q-1})
        be a canonical maximum source rail ending at y, so R,h is a longest q-edge h-path and R avoids v,w.
        
        Let
          e={x,v,u}
        be any distinct ascending nonspecial edge terminal at the same vertex v, and suppose both non-v vertices x,u lie on R. Let S be any canonical maximum source rail ending at the unique entrance x of e.
        
        Then
          |V(S) intersect V(R)| >= 2.
        In particular, besides the distinguished common vertex x, the source rail S has another intersection with the common anchor precursor R.
        
        Thus every source-clean whole chord on one canonical common anchor automatically carries a second source/anchor intersection; the remaining issue is only where that second intersection lies relative to x and u.

      • [1000439] A middle source-anchor return closes a rank-budgeted chord cycle
          STATEMENT
          Let
            h={y,v,w}
          be an ascending nonspecial anchor of rank q with canonical source rail R ending at y, and let
            e={x,v,u}
          be a distinct ascending nonspecial whole chord on R of rank r, with canonical clean source rail S ending at x. Thus R avoids v, both x,u lie on R, and S avoids u,v.
          
          Orient R so that x occurs before u. Suppose there is a common vertex
            z in V(S) intersect V(R)
          lying strictly on the R-segment between x and u. Choose z closest to u along that segment. Let
            a = number of R-edges from z to u,
            b = number of S-edges from z to x along the S-subpath ending at x.
          
          Then the three pieces
            e, R[u,z], S[z,x]
          form a linear cycle of length 1+a+b. Consequently
            a+b <= r-1.
          
          Thus any second source/anchor intersection lying between the entrance x and opposite terminal u carries the same nonspecial rank budget as a return lying beyond u.

      • [1000837] A whole edge yields a rank-bounded cycle or an equal-length entrance-side exchange
          STATEMENT
          Let
            h={y,v,w}
          be an ascending nonspecial edge of edge rank q with unique entrance y, and let
            R=(g_1,...,g_{q-1})
          be a maximum endpoint path with last vertex y such that R,h is a longest q-edge path with last edge h and R avoids v,w.
          
          Let
            e={x,v,u}
          be a distinct ascending nonspecial edge of edge rank r terminal at e at v. Assume both x and u lie on R. Let S be a maximum endpoint path with last vertex x such that S,e is a longest r-edge path with last edge e and S avoids u,v.
          
          Orient R so that x occurs before u. Then exactly one of the following alternatives is available:
          
          (A) S has a common vertex z with R on the u-side of x. Choosing such z to minimize the S-distance to x, the union of e, the R-segment between u and z, and the S-segment between z and x is a linear cycle of length at most r.
          
          (B) Every common vertex of S and R other than x lies strictly on the side of x opposite u. Let z be the common vertex closest to x on that side in the R-order. Then the R-segment R[z,x] and the S-segment S[z,x] are internally vertex-disjoint, distinct, and have the same number of edges. Replacing either segment by the other preserves maximum path length at the corresponding last vertex.
          
          Thus every whole edge on the common q-1-edge precursor yields either a rank-bounded cycle through e or an explicit equal-length two-path exchange entirely on the entrance side of x.

        • [1000040] Crossing equal-length source-path exchanges have constant rank-position slack unless two source paths meet twice
            STATEMENT
            Let R be a maximum endpoint path. For i=1,...,m let e_i={x_i,v,u_i} be distinct ascending nonspecial edges terminal at the common vertex v, with edge ranks r_i. Let S_i be canonical maximum source paths for e_i ending at x_i.
            
            For each i suppose there is a common vertex z_i of R and S_i such that the R-segment I_i=R[z_i,x_i] and the S_i-segment S_i[z_i,x_i] are distinct, internally vertex-disjoint, and have equal edge length. Suppose the intervals I_i are pairwise crossing on R. For every pair i!=j assume that, when S_i and S_j have exactly one common vertex, the pair satisfies the crossing-exchange hypotheses of 20606dbd4cd9. Let kappa_R(x_i) be the host-prefix coordinate of the chosen occurrence of x_i.
            
            Then either some pair S_i,S_j has at least two common vertices, or the quantities
              phi(x_i)-kappa_R(x_i)
            are all equal.
            
            Consequently, if all r_i lie in an integer interval [Q-D,Q] and the coordinates kappa_R(x_i) are pairwise distinct, then either m<=D+1 or some pair S_i,S_j has at least two common vertices.
            
            The coordinate-injectivity hypothesis in the counting consequence is essential; distinct host vertices alone do not imply distinct prefix-edge coordinates in a 3-uniform linear path.

        • [1000859] A common exchange return vertex has narrow-band capacity unless source paths overlap twice
            STATEMENT
            Let R be a linear path and let z be a fixed vertex of R. For i=1,...,m let
              e_i={x_i,v,u_i}
            be distinct ascending nonspecial edges terminal at v, with edge ranks r_i, and let S_i be maximum endpoint paths with last vertices x_i, so phi(x_i)=r_i-1.
            
            Assume:
            (1) z and x_i are common vertices of R and S_i;
            (2) the R-segment R[z,x_i] and the S_i-segment S_i[z,x_i] are internally vertex-disjoint and have the same number of edges;
            (3) the x_i are distinct.
            
            If all edge ranks r_i lie in an integer interval [Q-D,Q], then either
              m<=D+1,
            or there exist i!=j such that
              |V(S_i) intersect V(S_j)|>=2.
            
            Equivalently, D+2 equal-length path exchanges sharing one return vertex z in an edge-rank band of width D force a pair of the corresponding maximum source paths to have at least two common vertices.

          • [1001113] Large narrow-rank exchange families reduce to repeated source overlap or laminar host intervals
              STATEMENT
              Let R be a linear path and let F be a family of N equal-length path exchanges of the form
                I_i=R[z_i,x_i],
                A_i=S_i[z_i,x_i],
              where each S_i is a maximum endpoint path with last vertex x_i, I_i and A_i are internally vertex-disjoint and have the same number of edges, and the x_i are distinct unique entrances of distinct ascending nonspecial edges terminal at one common vertex. Assume all corresponding edge ranks lie in an integer interval of width D.
              
              Assume further that every pair S_i,S_j has exactly one common vertex. Then there is a subfamily of size at least
                K=floor(N/(6(D+1)))
              whose host intervals have pairwise distinct endpoints, and this subfamily contains at least one of:
              
              (1) ceil(sqrt(K)) pairwise disjoint host intervals;
              (2) ceil(K^(1/4)) pairwise nested host intervals;
              (3) ceil(K^(1/4)) pairwise crossing host intervals.
              
              Moreover every pairwise crossing subfamily has size at most D+1. Hence if
                K^(1/4)>D+1,
              outcome (3) is impossible and a quantitatively large pairwise disjoint or pairwise nested subfamily is forced.
              
              Thus, unless two maximum source paths already have at least two common vertices, sufficiently large narrow-rank exchange families reduce to a laminar host-interval family.

      • [1000861] Whole common-anchor chords give a cycle, a clean equal exchange, or a return-order inversion
          STATEMENT
          Let
            h={y,v,w}
          be an ascending nonspecial edge of rank q with canonical maximum source rail
            R=(g_1,...,g_{q-1})
          ending at y, so R,h is a longest q-edge h-path and R avoids v,w.
          
          Let
            e={x,v,u}
          be a distinct ascending nonspecial whole chord on R, of rank r, with canonical clean maximum source rail S ending at x. Thus x,u lie on R and S avoids u,v. Orient R so that x occurs before u.
          
          Then at least one of the following holds.
          
          (A) TERMINAL-SIDE CYCLE. Some common vertex of S and R other than x lies on the u-side of x. Then one can choose such a vertex z so that
            e union R[u,z] union S[z,x]
          is a linear cycle containing e, hence
            |R[u,z]|+|S[z,x]|+1 <= r.
          
          (B) CLEAN EQUAL EXCHANGE. Every common vertex other than x lies on the side of x opposite u, and the common vertex z nearest x in the R-order is also the common vertex nearest x in the S-order. Then
            R[z,x] and S[z,x]
          form a genuine clean two-path exchange, and
            |R[z,x]|=|S[z,x]|.
          
          (C) ORDER INVERSION. Every common vertex other than x lies on the side of x opposite u, but the R-nearest return z_R and the S-nearest return z_S are distinct. Then their order is reversed:
            z_R lies strictly between z_S and x on R,
          while
            z_S lies strictly between z_R and x on S.
          Thus R and S contain an explicit two-common-vertex braid inversion.
          
          This trichotomy is valid without assuming compatible order of all common vertices.

        • [1000582] Overlap-maximal source-clean paths make entrance-side inversions pay deficit or saturation
            STATEMENT
            Let e={x,v,u} be an ascending nonspecial edge of edge rank r with unique entrance x. Let R be a linear path avoiding v and containing x,u, oriented so that x occurs before u.
            
            Among all maximum endpoint paths S with last vertex x that avoid u,v, choose S maximizing
              |V(S) intersect V(R)|.
            Let a,b be common vertices of S and R such that the R-segment R[a,b]:
            (1) lies entirely on the side of x opposite u, and
            (2) meets S only at a,b.
            
            Put
              s=|R[a,b]|,  d=|S[a,b]|
            for the corresponding S-segment between a,b.
            
            Then d>=s. If d=s, every internal vertex of S[a,b] belongs to V(R).
            
            In particular, in the return-order inversion branch of c10cb2dd049c, let z_R be the common vertex nearest x in the R-order. Then
              |S[z_R,x]| >= |R[z_R,x]|.
            If equality holds, every internal vertex of S[z_R,x] lies somewhere on R. Thus an order inversion at an overlap-maximal clean source path either pays a positive integer length deficit or lies inside a source segment completely saturated by common-precursor vertices.

          • [1000932] Every overlap-maximal return-order inversion pays one edge of metric deficit
              STATEMENT
              Retain the return-order inversion branch (C) of c10cb2dd049c. Choose the maximum endpoint path S with last vertex x, among those avoiding u,v, to maximize |V(S) intersect V(R)| as in 813525f7f639. Let z_R be the common vertex nearest x in the R-order, and let z_S be the common vertex nearest x in the S-order. Then
                z_R != z_S,
              with z_R between z_S and x on R and z_S between z_R and x on S.
              
              Put
                s=|R[z_R,x]|,
                d=|S[z_R,x]|.
              Then
                d >= s+1.
              
              Thus every return-order inversion on an overlap-maximal source-clean maximum path carries a strict integer metric deficit; the zero-deficit saturation alternative of 813525f7f639 cannot occur in branch (C).

        • [1001223] Single-contact path rotations bound total contact-potential drop
            STATEMENT
            Let H be a finite linear 3-graph, phi its endpoint potential, and P=(g_1,...,g_p) a maximum path ending at v. Let E_v be a family of distinct edges e through v, different from the last edge of P, each meeting V(P) exactly in {v,z_e}. Then
            sum_{e in E_v} (p-phi(z_e))_+ <= 12p.
            In particular, for ascending edges e={x,v,u} of rank r<p that are terminal-single on P: entrance contacts contribute p-r <= p-phi(x), and opposite-terminal contacts contribute (p-phi(u))_+. The bound holds for any subfamily of these contacts.

        • [1001224] One-sided common-anchor source contacts force quadratic rank spread
            STATEMENT
            Let R=(g_1,...,g_L) avoid v. Let F be m distinct ascending nonspecial edges e={x,v,u}, with x,u on R, rank r_e<=q, and a clean maximum source path S_e of length r_e-1 ending at x. Orient R once, and set a_e to the first index containing x. Partition F according to whether u is after or before x. Assume the following weak one-sided source-contact property:
            if u is after x, V(S_e) intersect V(R) is contained in V(g_1 union ... union g_{min(L,a_e+1)});
            if u is before x, that intersection is contained in V(g_{a_e} union ... union g_L).
            Then, with Delta=sum_{e in F}(q-r_e),
            Delta >= m^2/24-m/2.
            Also, for every integer D>=0, at most 12(D+1) members have r_e>=q-D.
            The entrance-side equal-exchange and order-inversion branches on a common anchor satisfy this weak property.

          • [1001227] Entrance-side returns with an entrance terminal-path contact have sublinear total mass
              STATEMENT
              Let H be a finite linear 3-graph, S=sum_v phi(v), n_+=|{v:phi(v)>0}|, with fixed maximum endpoint paths P_v. At each center v let F_v be a distinct-edge family of ascending nonspecial edges e={x,v,u}, of rank r<min(phi(v),phi(u)), terminal-single on both P_v and P_u. Assume F_v has one common anchor of rank q_v<=phi(v), containing both x,u for every member, with r<=q_v and clean maximum sources.
              
              Let B_v consist of members satisfying the one-sided host-block condition of the rank-spread lemma at this anchor and for which at least one of P_v,P_u has entrance contact x (rather than opposite-terminal contact). Put M=sum_v |B_v|. Then
              M <= 6 n_+ + sqrt(36 n_+^2 + 864 n_+ S).
              Consequently M=o(S) whenever S/n_+ tends to infinity.
              
              Applied to the selected strict-gap families, this eliminates o(S)-scale entrance-side equal-exchange/order-inversion incidences with at least one entrance contact. Any surviving Omega(S) selected incidence mass must have a terminal-side return or opposite-terminal contacts on both terminal paths. No better leading coefficient is asserted.

            • [1001228] Two-opposite-terminal contacts have an aggregate terminal-potential balance budget
                STATEMENT
                In the fixed maximum-path setting, let E be a set of distinct ascending nonspecial strict-gap edges e={x,u,v}, terminal-single at both terminals, with the contact at u equal to v and the contact at v equal to u. Then
                sum_{e in E}|phi(u)-phi(v)|<=12S.
                For certificate-centered incidences supported on E, each edge occurring at at most two centers, the number having |phi(u)-phi(v)|>=epsilon phi(center) is o(S) for every fixed epsilon>0, whenever S/n_+ tends to infinity. Thus the two-opposite-terminal-contact residual is asymptotically balanced in terminal potentials in the incidence-count sense.

        • [1001226] A clean high-rank terminal source gives a central contact capacity bound
            STATEMENT
            Let e={x,v,u} be ascending nonspecial of rank q, and S a clean maximum source path of length q-1 ending at x. Let F_R be any family of distinct other ascending nonspecial edges through terminal v, all of rank at most R<=q. Then
            |F_R| <= max(0,4R-2q-1).
            In particular no such edge has rank below (q+1)/2, and at the integer equality boundary there is at most one. This replaces the proposed repeated-halving mechanism, which does not yield a substantial low-rank family.

        • [1000547] Return-order inversion has an exact two-splice loss identity
            STATEMENT
            Let R be a maximum endpoint path ending at y and S a maximum endpoint path ending at x, with x a vertex of R distinct from y. Suppose z_R,z_S are two further common vertices with the following nearest-return order:
            - the open R-segment R(z_R,x) contains no vertex of S, and along R the order is z_S,z_R,x;
            - the open S-segment S(z_S,x) contains no vertex of R, and along S the order is z_R,z_S,x.
            
            Put
              A=|R[z_S,z_R]|,  B=|R[z_R,x]|,
              C=|S[z_R,z_S]|,  D=|S[z_S,x]|.
            
            Then the two paths obtained by the clean tail switches
              S[start,z_R] followed by R[z_R,x],
            and
              R[start,z_S] followed by S[z_S,x] followed by R[x,y]
            are linear paths ending at x and y respectively.
            
            Define their losses relative to S and R by
              delta_x=(C+D)-B,
              delta_y=(A+B)-D.
            Then
              delta_x>=0,  delta_y>=0,
            and exactly
              delta_x+delta_y=A+C.
            
            Consequently
              max{delta_x,delta_y} >= (A+C)/2.
            Thus a return-order inversion with a long reversed middle core necessarily incurs a comparably large loss in at least one of the two canonical endpoint-preserving switches.

          • [1001229] Disjoint crossing source tails pay quadratic anchor-switch loss
              STATEMENT
              Let R be a maximum linear 3-uniform path ending at y. Let T_1,...,T_m be pairwise vertex-disjoint paths, each meeting R exactly at its endpoints a_i,b_i. All attachment vertices are distinct internal junctions of R, and their order is a_1<...<a_m<b_1<...<b_m. Set delta_i=|R[a_i,b_i]|-|T_i|. For m>=2, delta_i>=0 and sum_i delta_i >=(m-1)^2. For i<j, delta_i+delta_j>=2|R[a_j,b_i]|.

      • [1000914] A whole ascending chord spans at most rank minus one path edges
          STATEMENT
          Let e={x,v,u} be an ascending nonspecial edge of rank r, and let R be any linear path avoiding v that contains both x and u. Let R[x,u] denote the unique path segment between x and u, with d(e;R) edges.
          
          Then
            e union R[x,u]
          is a linear cycle of length d(e;R)+1. Consequently
            d(e;R) <= r-1.
          
          In particular, if e is a whole chord on a canonical common-anchor precursor R, its two distinguished endpoints x,u lie at anchor distance at most phi(e)-1.

        • [1000542] Strict-gap U11 whole chords carry a three-cycle packet
            STATEMENT
            Let e={x,u,v} be an ascending nonspecial edge of rank r. Let t be either terminal u or v, and let P_t be a maximum endpoint path ending at t with phi(t)>r. Assume e is terminal-single on P_t. Let c_t be the unique vertex of e\{t} occurring on the precursor of P_t, and let b_t be the last path-edge index containing c_t.
            
            Then e together with the suffix of P_t from that last occurrence of c_t to the endpoint t is a linear cycle C_t containing e, and
              |C_t|<=r.
            
            Consequently every strict-gap doubly-terminal-single edge carries two canonical rank-budgeted terminal cycles C_u,C_v.
            
            If, in addition, e is a whole chord on a path R avoiding the third/common terminal and containing its entrance x and the opposite terminal, then e also carries the anchor cycle
              C_R=e union R[x,opposite terminal],
            again of length at most r.
            
            Hence a same-terminal selected whole-chord edge in the strict-gap U11 class naturally carries a three-cycle packet, all three cycles containing the same nonspecial edge e and each having length at most phi(e).

      • [1001056] Every whole chord on a canonical common anchor has source and terminal returns
          STATEMENT
          Let h={y,v,w} be an ascending nonspecial anchor of rank q and let
            R=(g_1,...,g_{q-1})
          be a canonical maximum source rail ending at y, so R,h is a longest q-edge h-path and R avoids v,w.
          
          Let e={x,v,u} be a distinct ascending nonspecial edge terminal at v such that both x and u lie on R. Let S_x be a canonical maximum source rail ending at x, and let P_u be any maximum endpoint path ending at u.
          
          Then both
            |V(S_x) intersect V(R)| >= 2
          and
            |V(P_u) intersect V(R)| >= 2.
          
          If moreover e is terminal-single on P_u, exactly one of x,v lies on P_u away from u. Hence:
          - in reciprocal type X, x lies on P_u, so x and u are two explicit common vertices of P_u and R;
          - in reciprocal type V, x is absent from P_u and v is absent from R, so the second common vertex of P_u and R is external to e.
          
          Thus every whole chord on a canonical common anchor carries two independent maximum-path return certificates to the anchor: one from its clean source rail at x and one from its opposite-terminal path at u.

        • [1000242] Reciprocal V-type terminal-single edges close a canonical terminal cycle
            STATEMENT
            Let e={x,v,u} be an ascending nonspecial edge of rank r with terminals v,u. Let
              P=(g_1,...,g_s)
            be a maximum endpoint path ending at u, with s=phi(u)>r. Assume e is terminal-single on P and its unique off-u contact with the precursor is the other terminal v (reciprocal type V).
            
            Let b be the last path-edge index for which v lies in g_b. Then
              e,g_b,g_{b+1},...,g_s
            is a linear cycle of length
              s-b+2.
            Consequently
              s-b+2 <= r,
            or equivalently
              b >= s-r+2.
            
            Thus every reciprocal V-type strict-gap edge carries a canonical terminal cycle containing e, cut from the final segment of its opposite-terminal maximum path.

        • [1000746] Reciprocal X-type whole chords create a three-way multiple-overlap state
            STATEMENT
            Retain the common-anchor setup of eb7f3a1e87e0. Let
              e={x,v,u}
            be terminal-single on the chosen maximum path P_u ending at u, and suppose its reciprocal contact type at u is X, i.e. x lies on P_u and v does not.
            
            Let S_x be a canonical maximum source rail ending at x and R the canonical common anchor precursor containing x and u.
            
            Then every pair among the three maximum endpoint paths
              R, S_x, P_u
            has at least two common vertices:
              |R intersect S_x|>=2,
              |R intersect P_u|>=2,
              |S_x intersect P_u|>=2.
            
            More specifically R∩P_u contains both x and u. Thus reciprocal X-type whole chords manufacture a three-way multiple-overlap state on maximum endpoint paths, with one side carrying the distinguished pair {x,u}.

        • [1000828] Reciprocal type X is a short nonspecial chord cycle
            STATEMENT
            Let e={x,v,u} be an ascending nonspecial edge of rank r, with unique entrance x and terminals v,u. Assume r<phi(u), and let P_u be a maximum endpoint path ending at u on which e is terminal-single. Suppose the unique off-u contact of e on P_u is x rather than v.
            
            Then e is not an edge of P_u, and if d is the number of P_u-edges on the segment between x and u, then
              d <= r-1.
            
            Equivalently, every reciprocal terminal-single type-X state closes a linear cycle of length d+1 through e, and this cycle has length at most r.

      • [1000107] Any source return on the terminal side of a whole chord pays the nonspecial cycle budget
          STATEMENT
          Let h={y,v,w} be an ascending nonspecial anchor and let R be a canonical source precursor for h, so R avoids v. Let e={x,v,u} be a distinct ascending nonspecial edge of rank r terminal at v, with both x,u on R, and let S be a canonical clean source rail ending at x.
          
          Orient R so that x occurs before u. Suppose S has a common vertex with R strictly on the u-side of x. Among all such common vertices choose z minimizing the S-distance from x. Let
            a = |R[u,z]|
          be the number of R-edges on the segment between u and z, and
            b = |S[z,x]|.
          Then
            a+b <= r-1.
          
          Here R[u,z] is the unique R-segment between u and z, regardless of whether z lies between x and u or beyond u. Consequently, the only source-return pattern not carrying this cycle budget is one in which every common vertex of S and R other than x lies strictly on the R-side of x opposite u.

    • [1000432] The fixed hole has three external incidences relative to the rotated state
        STATEMENT
        In the canonical loss-one two-cycle setting of 0501d7730fd2 and bf82e5f39180, let P_1 be the rotated x-ending path of length q-2 and let b=b_{i+1} be the vertex omitted from P_1. Then among the edges through b other than g_{i+1}, the total number of non-b vertices lying outside V(P_1) is at least three. Consequently either some edge through b is disjoint from P_1, or at least three distinct edges through b meet P_1 in exactly one vertex and have their third vertex outside P_1.

    • [1000666] Entrance rails on a flat gap-one terminal cycle are blocked on both sides within distance two
        STATEMENT
        Let C=(e_0,...,e_{c-1}) be a linear terminal-cycle consisting of flat ascending nonspecial edges of common rank p-1, whose terminal vertices all have potential p and whose entrance labels x_i have potential p-2 and are private on their cycle edges. For each i let R_i be a maximum (p-2)-edge entrance path ending at x_i with R_i,e_i a longest (p-1)-edge path ending in e_i. Then R_i meets e_{i+1} union e_{i+2} and also meets e_{i-1} union e_{i-2}, with indices modulo c. If c>=6 these two cycle arcs are vertex-disjoint, so R_i has at least two distinct foreign-cycle contacts, one on each side of e_i. For c=5 the two arcs meet at the terminal joint e_{i+2} intersect e_{i-2}, so a single contact at that joint may satisfy both requirements and no two-contact conclusion is asserted.

      • [1000264] Flat gap-one terminal cycles have length at most p minus one
          STATEMENT
          A flat terminal cycle of rank-(p-1) ascending edges with terminal potential p and private entrances of potential p-2 has length at most p-1. Indeed deleting the cycle edge immediately after e_i leaves a (c-1)-edge path ending physically at the private entrance x_i, so c-1<=phi(x_i)=p-2.

      • [1000868] Entrance-label blockers on a flat gap-one cycle immediately create balanced rail lenses
          STATEMENT
          In a flat rank-(p-1) terminal cycle with private entrance labels x_i of potential p-2 and maximum entrance rails R_i ending at x_i, suppose R_i contains x_j for some j!=i. Then R_i and R_j have at least two common vertices and therefore contain a balanced elementary lens. Consequently, in any flat-cycle state with no balanced lens between distinct entrance rails, every forced foreign-cycle contact of every R_i must occur at a terminal vertex of the contacted cycle edge, hence at a vertex of potential p.

        • [1000220] Lens-free flat cycles force the two adjacent edges to be exact opposite-terminal single blockers on every entrance rail
            STATEMENT
            Let
              C=(e_0,...,e_{c-1}),  c>=4,
            be a flat gap-one terminal cycle with
              e_i={x_i,t_i,t_{i+1}},
            indices modulo c, where every e_i is ascending nonspecial of rank p-1, every terminal t_i has phi(t_i)=p, and every private entrance x_i has phi(x_i)=p-2.
            
            For each i let
              R_i=(r_1,...,r_{p-2})
            be a canonical maximum entrance rail ending physically at x_i such that R_i,e_i is a longest (p-1)-edge path ending in e_i. Assume the residual is entrance-rail lens-free in the sense that no two distinct rails R_i,R_j contain a balanced elementary lens.
            
            Then, for every i,
              e_{i-1} intersect V(R_i) = {t_{i-1}},
              e_{i+1} intersect V(R_i) = {t_{i+2}}.
            In particular e_{i-1} and e_{i+1} are exact one-contact blockers on R_i, through the two opposite terminal colors of e_i, and neither neighboring entrance x_{i-1},x_{i+1} lies on R_i.
            
            Moreover the first R_i-edge containing t_{i-1} and the first R_i-edge containing t_{i+2} each has index at most p-4.
            
            Thus every lens-free flat gap-one cycle canonically embeds, on each entrance rail, the two opposite-terminal single blockers needed by the two-terminal shared-rail system.

          • [1000599] Distance-three entrance rails meet at the intervening cycle terminal
              STATEMENT
              Retain the entrance-rail lens-free flat gap-one terminal cycle
                e_i={x_i,t_i,t_{i+1}}
              and canonical entrance rails R_i from 315871ed0c8b.
              
              Then for every i,
                t_{i+2} belongs to V(R_i) intersect V(R_{i+3}).
              
              Moreover, in the lens-free residual this is the unique common vertex:
                V(R_i) intersect V(R_{i+3})={t_{i+2}}.
              Consequently t_{i+2} is an internal aligned joint of R_i and R_{i+3} at one common index h_i, and
                h_i <= p-4.
              
              In particular, if the flat terminal cycle has length five, all five entrance rails are pairwise intersecting and every pair intersects uniquely: adjacent pairs meet at the anonymous aligned joints y_i from 960a5153b900, while nonadjacent pairs meet at the labeled cycle terminals supplied above.

          • [1000664] Lens-free flat cycles induce a cycle of unique aligned entrance-rail joints
              STATEMENT
              In the setting of 315871ed0c8b, assume the flat terminal cycle is entrance-rail lens-free. Then for every i the adjacent canonical entrance rails R_i and R_{i+1} have exactly one common vertex y_i.
              
              Moreover y_i is an internal joint of both rails at the same index: there is a unique integer
                k_i in {1,...,p-3}
              such that
                y_i=r^{(i)}_{k_i} intersect r^{(i)}_{k_i+1}
                   =r^{(i+1)}_{k_i} intersect r^{(i+1)}_{k_i+1}.
              
              The joint y_i is not any of
                x_i,x_{i+1},t_i,t_{i+1},t_{i+2}.
              Thus the lens-free flat cycle carries a second cyclic datum
                (R_0 --y_0-- R_1 --y_1-- ... -- R_{c-1} --y_{c-1}-- R_0)
              whose adjacent intersections are anonymous aligned internal joints with well-defined levels k_i.

            • [1000602] Disjoint outer rails force consecutive aligned joints into the late half
                STATEMENT
                Let A=(a_1,...,a_l), B=(b_1,...,b_l), C=(c_1,...,c_l) be maximum endpoint paths of the same length l, ending physically at x_A,x_B,x_C respectively.
                
                Assume
                  V(A) intersect V(B)={y},
                  V(B) intersect V(C)={z},
                and
                  V(A) intersect V(C)=emptyset.
                By unique-intersection alignment, write
                  y=a_r intersect a_{r+1}=b_r intersect b_{r+1},
                  z=b_s intersect b_{s+1}=c_s intersect c_{s+1}.
                
                Then
                  min{r,s} >= ceil(l/2).
                
                Applied to the lens-free flat-cycle rail system of 960a5153b900, if R_{i-1} and R_{i+1} are disjoint, then
                  min{k_{i-1},k_i} >= ceil((p-2)/2).
                Equivalently, whenever one of the two adjacent aligned levels k_{i-1},k_i is earlier than the midpoint, the outer rails R_{i-1},R_{i+1} must intersect.

              • [1000447] A clean cross-edge of uniquely intersecting maximum rails must cross the aligned joint
                  STATEMENT
                  Let A and B be maximum endpoint paths of the same length l, ending physically at x_A and x_B, and assume
                    V(A) intersect V(B)={y}.
                  Thus y is an aligned internal joint of the two paths.
                  
                  Let f be a hyperedge not belonging to A or B such that
                    f intersect V(A)={a},
                    f intersect V(B)={b},
                  with a,b distinct from y, and the third vertex of f outside V(A) union V(B).
                  
                  Then a and b must lie on opposite sides of y in their respective path orders.
                  
                  Consequently, in the lens-free flat-cycle system of 960a5153b900 and 315871ed0c8b, suppose the outer rails R_{i-1},R_{i+1} intersect. Their intersection is unique; call it z_i. The central cycle edge
                    e_i={x_i,t_i,t_{i+1}}
                  meets R_{i-1} exactly at t_{i+1} and R_{i+1} exactly at t_i. Therefore t_{i+1} and t_i lie on opposite sides of the aligned joint z_i on those two outer rails.

              • [1001200] Lens-free flat cycles have late aligned rails and no distance-two intersections
                  STATEMENT
                  Let R_i be the equal-length maximum entrance rails in a lens-free flat gap-one terminal cycle.
                  
                  If three such rails are pairwise uniquely intersecting, their three pairwise intersections coincide at one common aligned joint. Consequently the cyclic rail system has only two possible global forms: either every adjacent rail joint lies at level at least ceil((p-2)/2), or all rails share one common early aligned joint. The common-early-joint alternative is impossible in the flat terminal cycle, so every adjacent rail joint lies in the late half.
                  
                  Moreover every distance-two pair R_i,R_{i+2} is vertex-disjoint. If V(R_i)∩V(R_{i+3})={t_{i+2}} has aligned level h_i, then ceil((p-2)/2)<=h_i<=p-4. In particular a lens-free flat terminal cycle cannot have length five.

                • [1001074] Lens-free flat terminal cycles have no lengths six, seven, or nine
                    STATEMENT
                    In the entrance-rail lens-free flat gap-one terminal-cycle setting of 315871ed0c8b, the cycle length c is not 6, 7, or 9. Together with 14bb137811b4, it is therefore not 5,6,7, or9.

                  • [1001179] Four-path obstruction continuation
                      STATEMENT
                      Route bridge: flat-cycle elimination continues using toolkit lemma 1000106.

                    • [1001108] Every flat gap-one terminal cycle forces a balanced lens between entrance rails
                        STATEMENT
                        Let
                          C=(e_0,...,e_{c-1}), c>=4,
                        be a flat gap-one terminal cycle with
                          e_i={x_i,t_i,t_{i+1}},
                        where every e_i is ascending nonspecial of rank p-1, every t_i has vertex rank p, and every private entrance x_i has vertex rank p-2. For canonical maximum entrance rails R_i ending at x_i, some two distinct rails contain a balanced elementary lens. Equivalently, the entrance-rail lens-free residual is impossible.

        • [1000479] Terminal blockers on a flat-cycle entrance rail are pushed early by their cycle distance
            STATEMENT
            Let C=(e_0,...,e_{c-1}) be a flat rank-(p-1) terminal cycle with private entrances x_i, and let R_i=(r_1,...,r_{p-2}) be a maximum entrance rail ending at x_i. Assume R_i has no entrance-label contact with the relevant short cycle arc. Suppose a terminal vertex y of e_{i+d}, d in {1,2}, lies on R_i and the short forward arc e_{i+d},e_{i+d-1},...,e_i meets R_i only at y and x_i. If a is the first rail-edge index containing y, then a<=p-d-3. The symmetric backward statement holds for d in {1,2}. Thus an adjacent terminal blocker has first occurrence at most p-4, while a distance-two terminal blocker has first occurrence at most p-5.

    • [1000515] A terminal-retained strict-gap edge forces a cycle, a forward return, or a flat shared last edge
        STATEMENT
        Let e={x,v,u} be an ascending nonspecial edge with unique entrance x and edge rank q. Let
          P=(g_1,...,g_p)
        be a maximum endpoint path with last vertex v such that u belongs to V(P) and x does not. Assume
          q<p<=phi(u).
        
        Choose a maximum endpoint path
          Q=(f_1,...,f_s)
        with last vertex u, where s=phi(u). Suppose e is single-contact at u on Q.
        
        Then at least one of the following holds.
        
        (C) P union Q contains a linear cycle.
        
        (R) The last edge h=f_s of Q is an internal edge g_j of P, and Q has a common vertex with the forward suffix
          g_{j+1},...,g_p
        outside V(h).
        
        (H) The last edge h=f_s equals an internal edge g_j of P, Q enters h through the forward joint
          z=g_j intersect g_{j+1},
        and either
          phi(h)>p
        or
          V(h) subseteq {w:phi(w)>=p}.
        
        (F) One has s=p, h=g_j is nonspecial ascending of edge rank p, its unique entrance is
          z=g_j intersect g_{j+1},
        and phi(z)=p-1.
        
        Thus, after excluding cycles, further forward intersections, edge-rank rise, and host edges contained in V_{>=p}, the only remaining shared-last-edge state is the flat rank-p ascending orientation.

    • [1000745] Canonical p=5 entrance paths must cross the rank-five terminal edge itself
        STATEMENT
        In the p=5 charged pattern (4,4,4,5), retain the notation of 7d676959b033. Write the rank-five charged edge
          e5={d,v,w},
        where d=g4∩e5 is its unique entrance and v is the common charged terminal.
        
        For the rank-four edge
          f_b={b,v,u_b},
        let R_b be any canonical three-edge entrance path ending at b and avoiding v,u_b.
        
        Then R_b must meet e5. Since R_b avoids v, it contains at least one of d,w.
        
        Moreover phi(d)=4 and phi(w)>=5.

      • [1000175] Canonical p=5 entrance paths satisfy two simultaneous two-point transversals
          STATEMENT
          In the p=5 charged pattern (4,4,4,5), retain the notation
            f_b={b,v,u_b},  f_c={c,v,u_c},  e5={d,v,w}.
          Let R_b be any canonical three-edge entrance path for f_b, so R_b ends at b and avoids v,u_b. Then R_b meets both
            e5 and f_c.
          Consequently
            V(R_b)∩{d,w} != empty
          and
            V(R_b)∩{c,u_c} != empty.
          
          Symmetrically, every canonical entrance path R_c for f_c satisfies
            V(R_c)∩{d,w} != empty
          and
            V(R_c)∩{b,u_b} != empty.

      • [1001057] A single far-edge contact cannot occur in the middle of a canonical 4445 entrance rail
          STATEMENT
          In the 4445 setting, let
            R_b=(h_1,h_2,h_3)
          be a canonical three-edge entrance path for
            f_b={b,v,u_b},
          so R_b ends at b and avoids v,u_b, and R_b,f_b is a four-edge path ending in f_b through its unique entrance b.
          
          Suppose the rank-five edge e5 meets R_b in exactly one vertex. Then that contact does not lie in h_2.

        • [1000913] Double far-edge contact on a canonical 4445 entrance rail is confined to its first two edges
            STATEMENT
            In the 4445 setting let R_b=(h_1,h_2,h_3) be a canonical three-edge entrance path for f_b={b,v,u_b}. Suppose the rank-five edge e5 meets R_b in both of its non-v vertices d,w. Then one of d,w lies in h_1 and the other lies in h_2.
            
            Equivalently, the contact-position sets {h_1,h_3} and {h_2,h_3} are impossible. Hence every double-contact canonical rail has the normal form in which h_1,h_2,e5 form a linear 3-cycle, with h_3 as the stem from h_2 to the low entrance b.

    • [1000831] A double triple-gate C4 braid forces a cross-gate blocker
        STATEMENT
        Retain the double triple-gate branch of b6bdb78029f5. Let A be the common same-index joint of Q_0,Q_1,Q_3 at index a, and B the common same-index joint of Q_2,Q_1,Q_3 at index b. Then a≠b. If a<b, the other diagonal Q_0,Q_2 has a common vertex lying on the Q_0 suffix strictly after A and on the Q_2 prefix at or before B. If b<a, symmetrically Q_0,Q_2 has a common vertex lying on the Q_0 prefix at or before A and on the Q_2 suffix strictly after B. Thus the other diagonal must cross the interval between the two triple gates.

    • [1000811] The C4 residue is overlap-rich or a double triple-gate braid
        STATEMENT
        Assume the simple source-rail graph is the 4-cycle 01,12,23,30. After relabeling so that the four-overlap diagonal supplied by 905b4dff6b4c is 13, either the other diagonal pair Q_0,Q_2 has at least three distinguished common vertices, or there are two distinct vertices u_2,u_0 such that Q_0∩Q_1=Q_0∩Q_3={u_2} and Q_2∩Q_1=Q_2∩Q_3={u_0}; moreover u_2 is a same-index joint on Q_0,Q_1,Q_3 and u_0 is a same-index joint on Q_2,Q_1,Q_3. Thus the only non-overlap-rich C4 residue is a double triple-gate braid.

    • [1000965] Half-rank q,(q+1)^3 obstructions have a visible high entrance
        STATEMENT
        At phi(v)=2q-2, fix a maximum v-path and a charged rank-q edge e. Its entrance is the universal central joint. Each rank-(q+1) charged competitor has a selected witness in four surrounding slots L,A,B,R. If two competitors have entrances absent, their opposite-terminal witness slots are necessarily {L,B} or {L,R}. Hence among three rank-(q+1) competitors at least one entrance is visible on the path; that visible entrance has potential q.

    • [1001024] A first-joint-only rank-five competitor forces both far-left free vertices to potential at least five
        STATEMENT
        In the p=5 pure rank-five setup
          P=(g1,g2,g3,g4,e4),
        put r=g1∩g2. Let f be another rank-five charged edge through v whose only precursor vertex is r.
        
        Then both vertices of g1\\{r} have endpoint potential at least five.

    • [1001029] Disjoint outer maximum rails force aligned gates past half the shorter rail
        STATEMENT
        Let
          A=(a_1,...,a_m), B=(b_1,...,b_n), C=(c_1,...,c_\ell)
        be maximum endpoint paths ending at vertices x_A,x_B,x_C with
          phi(x_A)=m, phi(x_B)=n, phi(x_C)=ell.
        Assume
          V(A)∩V(B)={y},  V(B)∩V(C)={z},  V(A)∩V(C)=emptyset,
        and assume the unique intersections are aligned joints:
          y=a_r∩a_{r+1}=b_r∩b_{r+1},
          z=b_s∩b_{s+1}=c_s∩c_{s+1}.
        
        Then:
        - if r<=s, r>=ceil(m/2);
        - if s<=r, s>=ceil(ell/2).
        Consequently
          min{r,s} >= ceil(min{m,ell}/2).
        
        In particular this applies automatically whenever each adjacent rail pair has lengths differing by at most one, by the existing unique-intersection alignment lemmas.

      • [1000048] Both-prefix reciprocal terminals force a unique rail gate into the late half
          STATEMENT
          Let
            e_i={x_i,v,u_i}, e_j={x_j,v,u_j}
          be distinct source-clean ascending nonspecial edges through the common terminal v, with canonical maximum source rails
            Q_i=(a_1,...,a_m), Q_j=(b_1,...,b_n)
          ending at x_i,x_j, where m=phi(x_i)=phi(e_i)-1 and n=phi(x_j)=phi(e_j)-1.
          
          Assume:
          (1) V(Q_i)∩V(Q_j)={y}, and y is the aligned joint
              y=a_t∩a_{t+1}=b_t∩b_{t+1};
          (2) the foreign-edge contacts are reciprocal-terminal:
              Q_i∩e_j={u_j}, Q_j∩e_i={u_i};
          (3) both u_j on Q_i and u_i on Q_j occur strictly on the prefix side of y.
          
          Then
            2t >= m+1
          and
            2t >= n+1.
          Equivalently
            t >= ceil((max{m,n}+1)/2).
          
          Consequently, for a uniquely intersecting pair of source-clean U_11 edges in the consecutive-rank setting, if the aligned gate lies earlier than ceil((max{m,n}+1)/2), at least one of the two forced reciprocal terminal contacts must lie on the suffix side of the gate.

      • [1000313] Every paid clean-cycle chord yields theta, outer intersection, or two late source gates
          STATEMENT
          Let e be one of the paid-certified nonforest edges supplied by bee5f8c756bb, lying on its clean U_11 fundamental cycle C_e. Write r=phi(e), and let f,g be the two cycle neighbors of e. Then
            phi(f),phi(g) >= r.
          Choose canonical maximum source rails R_e,R_f,R_g, of lengths
            r-1, phi(f)-1, phi(g)-1.
          
          Then at least one of the following holds:
          (1) |V(R_e)∩V(R_f)|>=2;
          (2) |V(R_e)∩V(R_g)|>=2;
          (3) V(R_f)∩V(R_g) is nonempty;
          (4) both adjacent intersections are unique aligned joints, the outer rails R_f,R_g are disjoint, and if their gate indices on R_e are t_f,t_g, then
              min{t_f,t_g} >= ceil((r-1)/2).
          
          Thus every paid clean-cycle chord either immediately creates theta/multiple-overlap structure, closes a three-rail intersection triangle, or forces both adjacent simple gates into the late half of its source rail.

    • [1001076] Overlap-maximal same-endpoint deficiency-d path pairs have at most d internal lenses
        STATEMENT
        Let Q be an a-edge path ending at v, let phi(v)=a+d, and let P be a maximum (a+d)-edge path ending at v. Choose P, among maximum v-paths, to maximize the number of Q-edges it contains. For any family of clean internal elementary Q/P lenses that is simultaneously switchable (in particular, their replacement interiors are pairwise vertex-disjoint), with Q-side lengths A_i and P-side lengths B_i, one has A_i<=B_i and sum_i(B_i-A_i)<=d. Moreover no balanced lens B_i=A_i can occur. Hence such a family contains at most d internal elementary lenses.

    • [1001084] Overlap-maximal gap-one pairs have at most one nontrivial switchable cell, regardless of intersection order
        STATEMENT
        Let Q be a q-edge path and P a maximum (q+1)-edge path, both ending at v, with P chosen to maximize the number of Q-edges it contains. Consider any simultaneously switchable family of nontrivial two-common-vertex cells, where each cell consists of a Q-subpath and P-subpath joining the same boundary vertices and the replacement interiors are pairwise vertex-disjoint; the two subpaths may traverse the boundary vertices in the same or opposite order. If their lengths are A_i,B_i on Q,P respectively, then A_i<=B_i, sum_i(B_i-A_i)<=1, and no balanced cell A_i=B_i can occur. Hence such a family contains at most one nontrivial switchable cell.

  • [1001176] Terminal-shadow collision toolkit
      STATEMENT
      Reusable lemmas for backward color-terminal collisions on rank-monotone terminal-pair paths, including shortcut cycles and collision-packing mechanisms.

    • [1000126] Two crossing backward collisions either shortcut to a linear cycle or expose a further collision
        STATEMENT
        Let v_0v_1...v_k be a rainbow terminal-pair path of ascending nonspecial edges
        E_s={x_s,v_{s-1},v_s}
        with nondecreasing edge ranks. Suppose
        x_i=v_j and x_h=v_l
        are crossing backward collisions with
        j<l<i<h.
        
        Consider the edge sequence
        C=
        E_{j+1},E_{j+2},...,E_l,
        E_h,E_{h-1},...,E_i.
        
        Then one of the following holds.
        
        (A) C is a linear cycle of length
        L=(l-j)+(h-i+1).
        Every edge of C has rank at least L, and r_i>=L+1.
        
        (B) There is an additional backward collision x_b=v_a, distinct from the two displayed collisions, with either
        j<=a<b<=l,
        or
        i<=a<b<=h,
        or
        j<=a<l<i<b<=h.
        Thus failure of the crossing shortcut is witnessed in one of the two flanks or by another collision lying inside the crossing rectangle between the displayed chords.

    • [1000224] Collision count is bounded by rank spread times squared cycle-packing number
        STATEMENT
        Let v_0v_1...v_k be a rainbow terminal-pair path of ascending nonspecial edges
        E_1,...,E_k
        with nondecreasing ranks r_1<=...<=r_k. Let C be the number of color-terminal collision chords on this path, let
        D=r_k-r_1,
        and let nu be the maximum number of pairwise edge-disjoint linear cycles whose edges all belong to {E_1,...,E_k}.
        
        Then
        C <= D(2nu+1)^2.
        In particular, if D=0 then C=0, and more generally a path with small rank spread and bounded cycle-packing number is close to strong-rainbow.

    • [1000483] Every inclusion-minimal backward collision is a nonspecial cycle with one unit of rank slack
        STATEMENT
        Let v_0v_1...v_k be a rainbow terminal-pair path of ascending nonspecial edges
        E_s={x_s,v_{s-1},v_s}
        with nondecreasing edge ranks r_s.
        
        Call a backward color-terminal collision interval [j,i], meaning x_i=v_j, inclusion-minimal if there is no other collision x_h=v_l with j<=l<h<=i such that [l,h] is a proper subinterval of [j,i].
        
        If [j,i] is inclusion-minimal and c=i-j, then:
        (1) c>=3;
        (2) E_{j+1},...,E_{i-1} is strong-rainbow;
        (3) E_{j+1},...,E_i is a linear cycle of length c;
        (4) every edge on this cycle has rank at least c;
        (5) r_i>=c+1.

  • [1001183] Potential and rank-growth toolkit
      STATEMENT
      Reusable lemmas governing endpoint-potential equality, rank growth, and monotone rank propagation.

    • [1000196] Minimum-potential equality forces two-step ascent on every nonspecial edge
        STATEMENT
        Assume the minimum-potential equality setting of 41d502ff7771: sum_v phi(v)=m+n. Then:
        
        1. For every vertex v with p=phi(v), every maximum p-edge path ending at v has a special last edge.
        
        2. Every nonspecial edge e is ascending, and if q=phi(e) with unique entrance x and terminals u,v, then
           phi(x)=q-1,
           phi(u)>=q+1,
           phi(v)>=q+1.
        Equivalently every entrance-to-terminal arc in the auxiliary DAG raises endpoint potential by at least two.
        
        In particular no nonspecial edge has rank equal to the endpoint potential of either terminal.

    • [1000221] Strict ordered-shadow growth forces near-unit parent-rank growth
        STATEMENT
        Let z_0z_1,...,z_{t-1}z_t be a strictly increasing path in the ordered shadow Z, with labels lambda_i and parent ascending hyperedges E_i of ranks q_i. Write epsilon_i=q_i-lambda_i in {0,1}, so epsilon_i=1 exactly when the chosen auxiliary edge is entrance-terminal and epsilon_i=0 exactly when it is terminal-terminal. Then q_{i+1}-q_i >= 1+epsilon_{i+1}-epsilon_i. In particular parent ranks are nondecreasing; equality q_{i+1}=q_i can occur only when epsilon_i=1 and epsilon_{i+1}=0, i.e. only across an entrance-terminal step followed by a terminal-terminal step. More generally q_j-q_i >= (j-i)+epsilon_j-epsilon_i >= j-i-1.

    • [1000274] Top-rank alignment converts Astra double-contact mass directly into multiplicity credit
        STATEMENT
        Let q(v) be the maximum rank of an ascending nonspecial edge terminal at v. If q(v)=phi(v)=p, then choosing the global endpoint path P_v to end in such a top-rank ascending edge gives t(v)-X_v <= ((2r-3)/4)p+O_r(1), where X_v is excess contact multiplicity. Consequently, if every vertex supporting ascending terminal edges is top-rank aligned, the global leading coefficient improves to 1-(2r-1)/(4r(r-1)); for r=3 this is 19/24.

    • [1000278] Refined ascending-edge accounting
        STATEMENT
        Let A be the number of ascending nonspecial edges and let H_2 be the number of nonascending nonspecial edges e with unique entrance x satisfying φ(x)>2(φ(e)-1). Then 3m-A+H_2 <= Σ_v(2φ(v)-1) <= (2ell-3)n.

    • [1000378] Rank-gap mass and aligned potential simultaneously improve the Astra coefficient
        STATEMENT
        Let H be a finite linear r-uniform hypergraph, r>=3. For each nonisolated vertex v let p_v=phi(v), let t(v) count ascending nonspecial edges terminal at v, and when t(v)>0 let q(v) be their maximum rank. Let V_0={v:t(v)>0 and q(v)=p_v}, S_0=sum_{v in V_0}p_v, and G=sum_{v:t(v)>0,q(v)<p_v}(p_v-q(v)). Put S=sum_v p_v and c_r=1-(2r-1)/(8r(r-1)). Then
        m <= c_r S - (2r-1)/(8r(r-1)) S_0 - (6r-7)/(8r(r-1)) G + O_r(n_+).
        For r=3 this is m <= (43/48)S-(5/48)S_0-(11/48)G+O(n_+). Hence any asymptotic extremizer for the Astra coefficient with S/n_+ tending to infinity must satisfy both S_0=o(S) and G=o(S).

    • [1000414] A long terminal-only singleton family forces large total potential on its absent entrances
        STATEMENT
        Let P be a maximum p-edge path ending at v, and let e_1,...,e_k be terminal-only singleton ascending edges through v ordered by their contact positions on P. Let x_i be the absent unique entrance of e_i. Then
        sum_{i=1}^k phi(x_i) >= [k(p+3)-2p-10]/2.
        In particular, for k=Omega(p), the distinct off-path entrances carry Omega(kp) total endpoint potential.

    • [1000559] Two Type-A top-terminal entrances force a special universal gate two levels below
        STATEMENT
        Let v be Type A with p=phi(v)>=5, put q=p-1, and suppose exactly two rank-q nonspecial terminal edges h1,h2 occur through v. Let x1,x2 be their unique entrances, and let g be the universal two-entrance gate from a4df41ae3d99.
        
        Assume x1 and x2 are both Type A.
        
        Then:
        1. phi(x1)=phi(x2)=q-1=p-2;
        2. phi(g)=q-1;
        3. g is special.
        
        Hence g is one of the full-rank special edges in the common Type-A potential level p-2. In particular its third vertex also has potential q-1 whenever that third vertex is Type A.

    • [1000732] The aligned-or-lower-rank dichotomy sharpens the global bound to (43ell-75)n/48
        STATEMENT
        Let H be a finite linear 3-uniform hypergraph, let p(v)=phi(v) for each nonisolated vertex, and let m=|E(H)|. Define
        beta(1)=0, beta(2)=1, beta(3)=2, beta(4)=2, beta(5)=3, beta(6)=5,
        and beta(p)=floor((11p-16)/8) for p>=7.
        Then
        6m <= sum_{v nonisolated}(4p(v)-2+beta(p(v))).
        
        Consequently, for every integer ell>=8, every n-vertex P_ell^(3)-free linear 3-graph satisfies
        m <= [4ell-6+floor((11ell-27)/8)] n /6
          = [(43ell-75-rho_ell)/48] n,
        where rho_ell is the least nonnegative residue of 11ell-27 modulo 8. In particular
        m <= ((43ell-75)/48)n.
        The same argument gives m<=2n, (8/3)n, (7/2)n, and (9/2)n for ell=4,5,6,7 respectively.
        
        More precisely choose maximum endpoint paths as described in the proof. Let A count ascending edges, C count clean incidences, D count double incidences, U be total unused contact capacity, and eta=sum_v[beta(p(v))-t(v)+D_v]. Then eta>=0 and the exact identity is
        6m = sum_v(4p(v)-2+beta(p(v))) - D - eta - 2(A-C) - 2U.
        All four subtracted terms are nonnegative.

      • [1000371] The exact global deficit controls gap-one switching and lens mass
          STATEMENT
          Let v have p=φ(v)>=8, let T(v) be the ascending nonspecial edges terminal at v, let t=|T(v)|, let q be their maximum edge rank when t>0, and let D_v and
            eta_v=beta(p)-t+D_v,
            beta(p)=floor((11p-16)/8),
          be as in the exact identity of a57007500001.
          
          Then:
          (1) if q=p, eta_v>=beta(p)-ceil((3p-4)/4)>=(5p-24)/8;
          (2) if q<p, eta_v>=beta(p)-gamma(q), where gamma is the exact fixed-entrance bound.
          
          Hence eta_v=0 forces q=p-1, t=gamma(p-1)=beta(p), and D_v=0.
          
          Moreover, in the gap-one case q=p-1, the gap-one switching slack delta_v satisfies delta_v<=eta_v. Therefore every rank-q anchor and the chosen maximum p-edge path produce at least
            floor(5q/8)-eta_v
          switching edges that are double on the anchor and single on the maximum path; their retained endpoints give the same number of distinct balanced endpoint lenses on the maximum path.

        • [1000789] Low global defect forces near-top rank and dense switching lenses
            STATEMENT
            Let v have p=φ(v)>=8. Let T(v) be the ascending nonspecial edges terminal at v, let t=|T(v)|, and when t>0 let q be their maximum edge rank. Choose the maximum p-edge path P_v as in a57007500001. Let D_v count incident double contacts on P_v and put
              beta(p)=floor((11p-16)/8),
              eta_v=beta(p)-t+D_v.
            Then eta_v>=0.
            
            If q=p, then
              eta_v>=beta(p)-ceil((3p-4)/4)>=(5p-24)/8.
            
            If q<p, write gamma for the exact fixed-entrance bound and a(q)=ceil((3q-4)/4). Then
              eta_v>=beta(p)-gamma(q).
            Moreover, for every rank-q ascending terminal anchor h and every q-edge longest h-path Q ending at v, at least
              beta(p)-eta_v-a(q)
            members of T(v) are double on Q but single on P_v. Their non-v pairs form a matching between vertices of the anchor precursor retained by P_v and vertices omitted by P_v. Hence P_v supports at least the same number of distinct balanced endpoint-lens states.
            
            Since all these switching edges are single ascending terminal edges of rank at most q on P_v,
              beta(p)-eta_v-a(q) <= max(0,4q-2p-3).
            
            In particular, eta_v=o(p) forces q=p-o(p) and produces (5/8-o(1))p switching edges and balanced endpoint lenses.

          • [1000303] Lens-free low-defect centers still force near-top rank and five-eighths switching
              STATEMENT
              Let v be a nonisolated vertex with p=phi(v)>=8. Let T(v) be the ascending nonspecial edges terminal at v, let t=|T(v)|, and when t>0 let q be their maximum edge rank. Choose the maximum p-edge path P_v used in the exact defect identity a57007500001. Let D_v be the number of incident double contacts on P_v and put
                beta(p)=floor((11p-16)/8),
                eta_v=beta(p)-t+D_v.
              Then eta_v>=0.
              
              If q=p, then
                eta_v>=beta(p)-ceil((3p-4)/4)>=(5p-24)/8.
              
              If q<p, let gamma be the exact fixed-entrance bound and a(q)=ceil((3q-4)/4). Then
                eta_v>=beta(p)-gamma(q).
              Moreover, for every rank-q ascending terminal anchor h and every q-edge longest h-path Q ending at v, at least
                beta(p)-eta_v-a(q)
              members of T(v) are double on Q but single on P_v. Their non-v pairs form a matching between vertices of the anchor precursor retained by P_v and vertices omitted by P_v.
              
              Since these switching edges are single ascending terminal edges of rank at most q on P_v,
                beta(p)-eta_v-a(q) <= max(0,4q-2p-3).
              
              Consequently eta_v=o(p) forces q=p-o(p) and, at every active misaligned v, produces (5/8-o(1))p anchor-double / maximum-path-single switching edges. No endpoint-lens conclusion is asserted.

            • [1000755] Near 43/48, five-eighths switching mass survives without endpoint lenses
                STATEMENT
                Let (H_j) be a sequence of finite linear 3-uniform hypergraphs. For H_j write
                  S_j=sum_v phi(v),  m_j=|E(H_j)|,  n_j^+=|{v:d(v)>0}|.
                Assume
                  S_j/n_j^+ -> infinity
                and
                  m_j >= (43/48)S_j-o(S_j).
                
                Choose the maximum endpoint paths and local deficits eta_v from a57007500001. Then
                  sum_v eta_v=o(S_j).
                Moreover all but o(S_j) vertex-rank mass lies on active misaligned vertices v for which the maximum edge rank q(v) of an ascending nonspecial edge terminal at v satisfies q(v)<phi(v).
                
                For each such vertex choose one maximum-rank ascending terminal anchor and a longest anchor path. Let s(v) be the number of anchor-double / maximum-path-single switching edges supplied by 411fc64479d2. Then
                  sum_v s(v) >= (5/8-o(1))S_j.
                
                Thus every asymptotic 43/48 near-extremizer carries center-indexed switching-edge mass of order 5S/8. No endpoint-lens conclusion is asserted or needed.

          • [1000653] Switching edges inject into the half-potential superlevel
              STATEMENT
              Let H be a finite linear 3-graph and let v be an active misaligned vertex with p=phi(v)>=8. In the setup of b032348c1a8a, choose a maximum-rank ascending terminal anchor and let F_v be the resulting family of anchor-double / maximum-path-single switching edges. Then the unique entrance vertices of the edges in F_v are pairwise distinct and all have endpoint potential at least ceil(p/2). Consequently
                |V_{>=ceil(p/2)}| >= |F_v|
                >= beta(p)-eta_v-ceil((3q(v)-4)/4).
              In particular,
                |V_{>=ceil(p/2)}| >= (5/8)p-eta_v-O(1).
              
              Thus if eta_v=o(p), the half-potential superlevel contains at least (5/8-o(1))p vertices.

          • [1000655] Switching families force quadratic entrance-potential mass
              STATEMENT
              Let v be an active misaligned vertex with p=phi(v)>=8, let P_v be the chosen maximum p-edge path, and let F_v be any switching family from b032348c1a8a. For f in F_v write x_f for its unique entrance. Then
                sum_{f in F_v} phi(x_f) >= (p/2)|F_v|-p-5.
              Consequently
                sum_{f in F_v} phi(x_f)
                >= (p/2)[beta(p)-eta_v-ceil((3q(v)-4)/4)]-p-5.
              In particular, if eta_v=o(p), then
                sum_{f in F_v} phi(x_f) >= (5/16-o(1))p^2.
              
              Moreover, if switching families F_v are chosen simultaneously at several centers, then
                2 sum_{e ascending} phi(x_e)
                >= sum_v sum_{f in F_v} phi(x_f),
              because an ascending hyperedge has only two terminal vertices and hence can belong to at most two center-indexed switching families.

            • [1000211] Ascending source potential has a quadratic terminal-capacity budget
                STATEMENT
                Let H be a finite linear 3-graph. For each ascending nonspecial edge e={x,u,v}, let x be its unique entrance. Then
                  2 sum_{e ascending} phi(x)
                  <= sum_{y in V(H)} (phi(y)-1) max(0,2phi(y)-3).
                In particular, if phi(y)>=2 on every nonisolated vertex, then
                  2 sum_{e ascending} phi(x)
                  <= sum_y (phi(y)-1)(2phi(y)-3).
                
                Consequently, for any simultaneously chosen center-indexed switching families F_v,
                  sum_v sum_{f in F_v} phi(x_f)
                  <= sum_y (phi(y)-1) max(0,2phi(y)-3).

            • [1000526] Common-terminal rank windows add a quadratic source-rank bonus
                STATEMENT
                Let v be an active misaligned vertex with phi(v)=p>=8, and let F_v be any switching family from b032348c1a8a. Write k=|F_v| and x_f for the unique entrance of f. Then
                  sum_{f in F_v} phi(x_f) >= kp/2 + k(k-1)/8.
                More generally the same inequality holds for any k distinct ascending nonspecial edges terminal at a common vertex v of rank p, provided every edge has rank at most p.
                
                Consequently, if eta_v=o(p), then k>=(5/8-o(1))p and
                  sum_{f in F_v} phi(x_f) >= (185/512-o(1))p^2.
                For simultaneously chosen switching families,
                  sum_v [p_v|F_v|/2 + |F_v|(|F_v|-1)/8]
                  <= 2 sum_{e ascending} phi(x_e).

              • [1000006] Rank windows remove the high-triangle collapse in the source-mass frontier
                  STATEMENT
                  In the setup of 98152151c212, with s interior switchers and D doubly occupied cells,
                    sum_{f in F} phi(x_f)
                    >= (p/2)s + max{ floor((s-D)^2/4), s(s-1)/8 }.
                  Hence triangle concentration cannot reduce the quadratic source term below s(s-1)/8. For a low-defect switching family with s=(5/8-o(1))p,
                    sum_{f in F} phi(x_f) >= (185/512-o(1))p^2,
                  uniformly in D.
                  More precisely the cell-dispersion term dominates while D <= (1-1/sqrt(2))s+O(1), and the rank-window term dominates beyond that threshold.

            • [1000727] Central-window ordering boosts switching source mass to 185/512
                STATEMENT
                Let v be an active misaligned vertex with p=phi(v)>=8, and let F_v be a switching family from b032348c1a8a relative to the chosen maximum p-edge path P_v. Put s=|F_v|, and order the switcher edge ranks
                  r_1<=...<=r_s.
                Then for every i=1,...,s,
                  r_i >= ceil((2p+i+3)/4).
                Hence, writing x_i for the unique entrance of the i-th switcher,
                  sum_{i=1}^s phi(x_i)
                  >= sum_{i=1}^s (ceil((2p+i+3)/4)-1)
                  >= (p/2)s + s^2/8 - s/8.
                
                Since b032348c1a8a gives
                  s>=beta(p)-eta_v-ceil((3q(v)-4)/4),
                a low-defect center eta_v=o(p) satisfies
                  sum_{f in F_v}phi(x_f) >= (185/512-o(1))p^2.
                
                For simultaneous switching families at several centers,
                  sum_v [ (p_v/2)s_v+s_v^2/8-s_v/8 ]
                  <= sum_y (phi(y)-1)max(0,2phi(y)-3),
                where s_v=|F_v|.

              • [1001138] Clean-retained switchers gain a one-sixth quadratic source term
                  STATEMENT
                  Let v be an active misaligned vertex with p=phi(v)>=8, let P_v be the chosen maximum p-edge path, and let F_v be a switching family from b032348c1a8a. Split
                    F_v = X_v disjoint_union U_v,
                  where X_v consists of switchers whose unique retained off-v contact on P_v is their entrance, and U_v consists of switchers whose retained contact is the opposite terminal. Put
                    a=|X_v|, k=|U_v|, s=a+k.
                  
                  Order the ranks of X_v as
                    rho_1<=...<=rho_a.
                  Then for every i,
                    rho_i >= p/2 + (i+1)/3,
                  and therefore
                    sum_{f in X_v} phi(x_f) >= (p/2)a + (a^2-a)/6.
                  
                  Every f in U_v has
                    phi(x_f) >= (p+1)/2.
                  Consequently
                    sum_{f in F_v} phi(x_f)
                    >= (p/2)s + (a^2-a)/6 + k/2.                 (*)
                  
                  Combining (*) with the all-switcher central-window bound a5066873364f gives
                    sum_{f in F_v} phi(x_f)
                    >= max{
                         (p/2)s+s^2/8-s/8,
                         (p/2)s+(a^2-a)/6+k/2
                       }.
                  
                  In particular, if eta_v=o(p), then s=(5/8-o(1))p. Hence either |U_v|=Omega(p), or, whenever |U_v|=o(p),
                    sum_{f in F_v}phi(x_f) >= (145/384-o(1))p^2.
                  Thus a low-defect center either carries a linear terminal-retained switching family or pays the stronger 145/384 clean-retained source-mass coefficient.

                • [1000567] Clean-retained switchers satisfy four-fifths cell packing
                    STATEMENT
                    Let P=(g_1,...,g_p) be a maximum p-edge path ending at v with last vertex v. Let X be a family of ascending nonspecial edges e={x,v,u}, e!=g_p, such that each edge has exactly one off-v contact with P and that contact is its unique entrance x.
                    
                    For R<p let X_{\\le R}={e in X: phi(e)<=R}. Then, whenever X_{\\le R} is nonempty,
                      |X_{\\le R}| <= (4/5)(2R-p-1)+7/5.
                    In particular, if the ranks of X are ordered
                      rho_1<=...<=rho_a,
                    then
                      rho_i >= ceil((4p+5i-3)/8)
                    for every i.
                    
                    Consequently, writing x_i for the entrance of the edge of rank rho_i,
                      sum_{i=1}^a phi(x_i)
                      >= (p/2)a + (5a^2-17a)/16.
                    
                    Applied to the clean-retained part X_v of a low-defect switching family at a p-center, if the terminal-retained part U_v has size o(p), then a=(5/8-o(1))p and
                      sum_{f in X_v} phi(x_f) >= (445/1024-o(1))p^2.

                  • [1000124] Near-minimal source mass forces three-sevenths terminal retention
                      STATEMENT
                      Let v be an active misaligned p-center and let a low-defect switching family F_v split as
                        F_v=X_v disjoint_union U_v,
                      with a=|X_v|, k=|U_v|, s=a+k.
                      Then, up to an additive O(p) boundary term,
                        sum_{f in F_v} phi(x_f)
                        >= (p/2)s + s^2/8
                            + max{0, a(7a-4s)/16}.                         (*)
                      
                      Consequently, if eta_v=o(p), so s=(5/8-o(1))p, then either the forced source-potential mass is larger than the generic 185/512 p^2 floor by a fixed positive multiple of p^2, or
                        k >= (3/7-o(1))s
                          = (15/56-o(1))p.
                      
                      More quantitatively, if k <= (3/7-epsilon)s for fixed epsilon>0, then
                        sum_{f in F_v} phi(x_f)
                        >= (185/512 + c_epsilon-o(1))p^2
                      for some explicit c_epsilon>0 (for example one may take c_epsilon asymptotic to 25 epsilon/512 for small epsilon).

                    • [1000905] Terminal-retained cheap states force disjoint inside-outside packets
                        STATEMENT
                        Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, and let U be a family of k terminal-retained switching edges
                          e_i={x_i,v,u_i},
                        so u_i is the unique off-v contact of e_i with P and x_i is the omitted unique entrance.
                        
                        Then U forces two disjoint packets.
                        
                        (1) Off-path source packet. The vertices x_1,...,x_k are distinct and lie outside V(P), and
                          sum_{i=1}^k phi(x_i) >= (p/2)k + k(k+1)/8.
                        
                        (2) On-path rotation packet. The U-contacts occupy at least ceil(k/2) interior two-slot blocker cells apart from O(1) boundary contacts. Every occupied interior cell yields two distinct vertices of V(P) with endpoint potential at least p, and the output pairs from distinct cells are disjoint. Hence U yields at least
                          k-O(1)
                        distinct vertices w in V(P) with phi(w)>=p that arise as endpoints of p-edge rotations generated by U.
                        
                        The two packets are vertex-disjoint because every x_i lies outside P.
                        
                        Consequently, at any low-defect p-center whose source-potential mass remains within o(p^2) of the generic 185/512 p^2 floor, 1bab77ec4e49 gives
                          k >= (15/56-o(1))p.
                        Such a center therefore simultaneously carries:
                        - at least (15/56-o(1))p distinct omitted entrance vertices outside P, with total endpoint potential at least
                            (3585/25088-o(1))p^2;
                        - at least (15/56-o(1))p distinct vertices on P of endpoint potential at least p arising as U-rotations.

                  • [1000149] Near equality in clean-retained packing has a unique period-five normal form
                      STATEMENT
                      Use the clean-retained central-window setup of 7e047fd40dd7 at a rank cutoff R<p, with N=2R-p-1 eligible joint cells, and let m=|X_{\le R}|. Put
                        Delta = 4N/5 + 7/5 - m >= 0.
                      
                      Then all but at most 5Delta of the eligible cell transitions are on the unique critical five-cycle of the cell automaton. Consequently the eligible window can be partitioned into at most 5Delta+1 consecutive intervals such that, on each interval away from its boundary, the clean-retained occupancy pattern is periodic of period five:
                        (private+joint), private, empty, joint, empty,
                      up to cyclic phase.
                      
                      In particular, if m=4N/5-o(N), then after deleting o(N) cells the clean-retained contact pattern is a union of period-five intervals of the displayed form.

                  • [1000753] Clean-retained switchers satisfy three-quarters cell packing
                      STATEMENT
                      Let P=(g_1,...,g_p) be a maximum p-edge path ending at v. Let X be a family of ascending nonspecial terminal edges e={x,v,u}, e!=g_p, such that each e has exactly one off-v contact with P and that contact is its unique entrance x.
                      
                      For R<p let X_{\le R}={e in X: phi(e)<=R}. Then, whenever X_{\le R} is nonempty,
                        |X_{\le R}| <= (3/4)(2R-p-1)+3/2.                    (1)
                      
                      Hence, if the X-ranks are ordered rho_1<=...<=rho_a,
                        rho_i >= ceil((3p+4i-3)/6),                          (2)
                      and therefore
                        sum_{i=1}^a phi(x_i)
                        >= (p/2)a + a^2/3 - 7a/6.                           (3)
                      
                      In particular, if X comprises (5/8-o(1))p switchers, then
                        sum_{f in X}phi(x_f) >= (85/192-o(1))p^2.
                      
                      Moreover, near equality in (1) has the unique period-four cell pattern
                        (private+joint), private, empty, empty
                      up to cyclic phase: if
                        Delta = (3/4)(2R-p-1)+3/2-|X_{\le R}|,
                      then all but at most 4Delta cell transitions lie on the corresponding critical four-cycle.

                    • [1000185] Near-minimal source mass forces five-elevenths terminal retention
                        STATEMENT
                        Let v be an active misaligned p-center and split a switching family
                          F_v=X_v disjoint_union U_v
                        with
                          a=|X_v|, k=|U_v|, s=a+k.
                        Then, up to an additive O(p) term,
                          sum_{f in F_v}phi(x_f)
                          >= (p/2)s + s^2/8
                              + max{0, a(11a-6s)/24}.                         (*)
                        
                        Consequently, suppose eta_v=o(p) and the switching-source mass remains within o(p^2) of the generic 185/512 p^2 floor. Then necessarily
                          s=(5/8+o(1))p
                        and
                          k >= (5/11-o(1))s
                            = (25/88-o(1))p.
                        
                        If instead eta_v=o(p) and
                          k <= (5/11-epsilon)s
                        for a fixed epsilon>0, then the source-potential mass exceeds the generic 185/512 p^2 floor by a fixed positive multiple of p^2.

                      • [1000949] Near-minimal switching states require order at least 201 over 88 times the host rank
                          STATEMENT
                          Let H be a finite linear 3-graph on n vertices and let v be an active misaligned vertex with p=phi(v). Suppose eta_v=o(p) and the switching-family source-rank mass is within o(p^2) of the generic 185/512 p^2 floor. Then
                            n >= (201/88-o(1))p.
                          Indeed, if U_v is the terminal-retained part of the switching family, then |U_v| >= (25/88-o(1))p and its distinct omitted entrances lie outside the chosen maximum p-edge host path.

                      • [1001107] Near-minimal source mass forces improved terminal retention on both host halves
                          STATEMENT
                          Let v be an active misaligned p-center with low-defect switching family F_v=X_v disjoint_union U_v. Write a=|X_v|, k=|U_v|, s=a+k. Let k_-,k_+ count U_v contacts whose first host-path occurrence lies strictly left and strictly right of the midpoint (p-1)/2, and put d=(k_--k_+)/s, t=k/s. Then, up to O(p), the switching-source mass M_v satisfies M_v >= (p/2)s+s^2/8 + max{0, s^2[(1-t)(5-11t)+3d^2]/24}. Consequently, if eta_v=o(p), so s=(5/8-o(1))p, and M_v differs from the generic floor (p/2)s+s^2/8 by o(p^2), then t>=5/11-o(1) and min{k_-,k_+} >= [4/11-sqrt(42)/22-o(1)]s >= [5(8-sqrt(42))/176-o(1)]p.

                        • [1000347] Cheap vertices carry balanced endpoint-lens packets on both host halves
                            STATEMENT
                            Let v be a low-defect active misaligned vertex of rank p whose switching-source mass is within o(p^2) of the generic 185/512 p^2 floor. On the chosen maximum p-edge host path P_v, there are at least
                              [5(8-sqrt(42))/176-o(1)]p
                            distinct terminal-retained attachment vertices strictly on each side of the host midpoint. Every such attachment vertex u supports a clean balanced elementary endpoint lens between P_v and a maximum u-ending path.
                            
                            Thus a locally cheap vertex carries two macroscopic, spatially separated endpoint-lens packets, one on each host half.

                      • [1001132] Five-elevenths retention upgrades the disjoint inside-outside packets
                          STATEMENT
                          Let P=(g_1,...,g_p) be the chosen maximum p-edge path at a low-defect active misaligned vertex v, and suppose the switching-source mass is within o(p^2) of the generic 185/512 p^2 floor. Then the terminal-retained subfamily U_v contains
                            k >= (25/88-o(1))p
                          edges e_i={x_i,v,u_i}. Consequently:
                          (1) the x_i are distinct vertices outside P and
                            sum_i phi(x_i) >= (9425/61952-o(1))p^2;
                          (2) U_v yields at least (25/88-o(1))p distinct vertices of P of vertex rank at least p arising as last vertices of p-edge switching rotations.
                          The outside source packet and on-path rotation packet are vertex-disjoint.

                    • [1000731] Retaining the strict rank gap gives three-fifths entrance-contact packing
                        STATEMENT
                        Let P=(g_1,...,g_p) be a maximum linear path ending at v in a finite linear 3-graph. Let X be ascending nonspecial edges terminal at v, each of rank at most R<p and each having exactly one off-v contact with P, namely its unique entrance. If X is nonempty, then |X| <= (3/5)(2R-p-1)+9/5. In particular, taking R=p-1 gives |X|<=3p/5. The same bound holds for any subfamily, including the entire entrance-contact family at a misaligned vertex.

                • [1000631] Ascending edges are reciprocal two-point transversals of terminal maximum paths
                    STATEMENT
                    Let e={x,u,v} be any ascending nonspecial edge of rank r, with unique entrance x and terminals u,v. Then every maximum endpoint path ending at u contains x or v. Symmetrically, every maximum endpoint path ending at v contains x or u.
                    
                    More precisely, if a maximum u-ending path P_u uses e, then phi(u)=r, e is the last edge of P_u, and P_u enters e through x, so x belongs to P_u. If P_u does not use e, then P_u cannot avoid both x and v.

                  • [1000502] Every terminal-retained switcher yields a source-terminal lens or a two-terminal overlap
                      STATEMENT
                      Let e={x,v,u} be an ascending nonspecial edge with unique entrance x. Let P_v be a maximum endpoint path ending physically at v such that u lies on P_v and x does not. Let P_u and P_x be arbitrary maximum endpoint paths ending physically at u and x. Then P_v and P_u contain a balanced elementary endpoint lens attached at u. Moreover at least one of the following holds: (X) x lies on P_u, in which case P_u and P_x contain a balanced elementary endpoint lens attached at x; (V) v lies on P_u, in which case P_u and P_v contain a balanced elementary endpoint lens attached at v. Thus every terminal-retained switching state carries, in addition to its host attachment at u, either a source-terminal lens certificate or reciprocal terminal-terminal overlap through both terminal labels.

                    • [1000762] Terminal-retained edges force repeated maximum-path intersections without lens conversion
                        STATEMENT
                        Let e={x,v,u} be an ascending nonspecial edge with unique entrance x and terminals v,u. Let P_v be a maximum endpoint path ending at v such that u belongs to V(P_v) and x does not. Let P_u and P_x be arbitrary maximum endpoint paths ending at u and x respectively.
                        
                        Then:
                        
                        (1) P_v and P_u have at least two common vertices.
                        
                        (2) At least one of x,v lies on P_u.
                        
                        (3) If x lies on P_u, then P_u and P_x have at least two common vertices.
                        
                        (4) If v lies on P_u, then P_v and P_u contain the two distinct common vertices u and v.
                        
                        Hence every terminal-retained ascending edge produces either a source-recapture repeated-intersection pair P_u,P_x or an explicit reciprocal terminal-terminal overlap P_v,P_u through {u,v}; in all cases P_v,P_u already have at least two common vertices.
                        
                        If in addition phi(u)>phi(e) and e is terminal-single on P_u, then exactly one of x,v lies on P_u, so the two alternatives in (3),(4) are exclusive.

                      • [1001210] Terminal-retained continuation
                          STATEMENT
                          Route bridge: the reciprocal-transversal analysis continues after toolkit lemma 1000515.

                        • [1001178] Flat host-packing continuation
                            STATEMENT
                            Route bridge: the flat terminal-retained analysis continues after toolkit lemma 1000058.

                          • [1000234] A cycle-free flat terminal-retained state forces a rank-p edge common to both host paths
                              STATEMENT
                              Retain a flat state from 7312b3378d20. Thus e={x,v,u} has edge rank below p, its unique contact on the maximum p-edge path P ending at v is u, and a maximum p-edge path Q ending at u has last edge h, where h is an internal edge of P, h is nonspecial ascending of edge rank p, and Q enters h through the forward joint of P.
                              
                              Assume additionally that e belongs to a selected common-precursor family: there is a maximum endpoint path R of length L<p that avoids v and contains both x and u.
                              
                              Then either
                                Q union R
                              contains a linear cycle, or
                                h belongs to E(P) intersect E(R).
                              
                              In the second case, either h is the last edge of R, or h is internal on R. If h is internal and the propagation process of 678901b48360 starting from h produces no linear cycle, the position of h on R is at most
                                2L+1-p.
                              
                              For a family of such flat states using one fixed precursor R, the boundary alternative h=last(R) can occur for at most two target edges.

                • [1000882] Terminal-only singleton ranks have a cumulative four-slot bound
                    STATEMENT
                    Let P=(g_1,...,g_p) be a maximum p-edge path ending at v. Let U be a family of ascending nonspecial edges e={x,v,u} terminal at v such that each e has exactly one off-v contact with P, that contact is the opposite terminal u, and the unique entrance x is absent from P.
                    
                    For an integer R<p, let U_{<=R}={e in U: phi(e)<=R}. Then
                      |U_{<=R}| <= max{0,4R-2p-4}.
                    
                    Consequently, if the ranks in U are ordered
                      rho_1<=...<=rho_k,
                    then
                      rho_i >= ceil((2p+i+4)/4).
                    Writing x_i for the absent entrance of the edge of rank rho_i,
                      sum_{i=1}^k phi(x_i)
                      >= (p/2)k + k(k+1)/8.
                    
                    Thus a long terminal-retained singleton family forces quadratic, not merely linear, total endpoint potential on its distinct omitted entrances.

                  • [1001047] Terminal-retained source mass pays quadratically for left-right contact imbalance
                      STATEMENT
                      Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, and let U be a family of ascending nonspecial terminal-only singleton edges
                            e_i={x_i,v,u_i},
                          where x_i is the unique entrance, x_i is absent from P, and u_i is the unique off-v contact with P.
                      
                      For each i let a_i be the first path-edge index containing u_i. Define
                            k_- = |{i: a_i < (p-1)/2}|,
                            k_+ = |{i: a_i > (p-1)/2}|,
                            k=|U|,
                          with contacts exactly at the midpoint (possible only when p is odd) placed in neither side.
                      
                      Then
                            sum_i phi(x_i)
                            >= (p/2)k + k^2/8 + (k_- - k_+)^2/8.
                      
                      Combining with c48823eea604, one may sharpen this to
                            sum_i phi(x_i)
                            >= (p/2)k + k^2/8
                               + max{k/8,(k_- - k_+)^2/8}.
                      
                      Consequently, for any sequence with k=Theta(p), if the terminal-retained entrance-potential mass is within o(p^2) of the quadratic minimum (p/2)k+k^2/8, then
                            k_- - k_+ = o(p).
                      Thus a near-minimal terminal-retained packet must be asymptotically balanced across the two halves of its host path.

                    • [1000951] Near-minimal switcher source mass forces linear terminal retention on both host halves
                        STATEMENT
                        Let v be an active misaligned p-center with switching family
                              F_v=X_v disjoint_union U_v.
                            Write
                              a=|X_v|,  k=|U_v|,  s=a+k,
                            and let k_-,k_+ be the numbers of U_v contacts whose first host-path occurrence lies respectively strictly left and strictly right of the midpoint (p-1)/2 of the chosen maximum host path P_v.
                        
                        Put
                              M_v=sum_{f in F_v} phi(x_f),
                            where x_f is the unique entrance of f. Then, up to an additive O(p) term,
                              M_v >= (p/2)s + s^2/8
                                     + max{0, [(s-k)(3s-7k)+2(k_--k_+)^2]/16}.      (*)
                        
                        Consequently, suppose eta_v=o(p), so s=(5/8-o(1))p, and suppose
                              M_v <= (p/2)s+s^2/8+o(p^2).
                        Then
                              k >= (3/7-o(1))s
                        and, more strongly,
                              min{k_-,k_+}
                              >= ((5-3sqrt(2))/14-o(1)) s.
                        
                        Hence
                              min{k_-,k_+}
                              >= [5(5-3sqrt(2))/112-o(1)] p
                              = (0.03379...-o(1))p.
                        
                        Thus every low-defect center that avoids a fixed quadratic source-mass gain carries a fixed linear family of terminal-retained switchers on each side of its maximum host path.

          • [1000940] 43/48 near-extremizers carry five-eighths switching and lens mass
              STATEMENT
              Let (H_j) be a sequence of finite linear 3-uniform hypergraphs. For H_j write
                S_j=sum_v φ(v),  m_j=|E(H_j)|,  n_j^+=|{v:d(v)>0}|.
              Assume
                S_j/n_j^+ -> infinity
              and
                m_j >= (43/48)S_j-o(S_j).
              
              Choose the maximum endpoint paths and local deficits eta_v from a57007500001. Then
                sum_v eta_v=o(S_j).
              Moreover, all but o(S_j) endpoint-potential mass lies on active misaligned vertices v for which the maximum rank q(v) of an ascending nonspecial edge terminal at v satisfies q(v)<φ(v).
              
              For each such vertex choose one maximum-rank ascending terminal anchor and its canonical longest anchor path. Let s(v) be the number of anchor-double / maximum-path-single switching edges supplied by b032348c1a8a. Then
                sum_v s(v) >= (5/8-o(1))S_j.
              Consequently the chosen maximum endpoint paths collectively support at least (5/8-o(1))S_j distinct center-indexed balanced endpoint-lens states.
              
              Thus every asymptotic 43/48 near-extremizer carries switching/lens mass of order 5S/8; any global argument forcing a fixed positive proportional loss in this mass improves the 43/48 leading coefficient.

            • [1000310] 43/48 near-extremizers reduce to a dense doubly-terminal-single rainbow graph
                STATEMENT
                Let (H_j) be a sequence of finite linear 3-graphs satisfying the 43/48 near-extremal hypotheses of d287da5967d5:
                  S_j=sum_v phi(v),  S_j/n_j^+ -> infinity,
                  |E(H_j)| >= (43/48)S_j-o(S_j).
                Choose the maximum endpoint paths used in a57007500001.
                
                Let U_11 be the set of ascending nonspecial edges e={x,u,v} whose contact multiplicity is one at both terminal endpoint paths P_u and P_v. Form the terminal graph G_11 with vertex set V(H), one graph edge uv for every e={x,u,v} in U_11, colored by its entrance x.
                
                Then:
                (1) |U_11|=(11/16-o(1))S_j.
                (2) If d_11(v) is the degree of v in G_11, then
                    sum_v (beta(phi(v))-d_11(v))_+ = o(S_j).
                Consequently, for every fixed epsilon>0, all but o(S_j) endpoint-potential mass lies on vertices v satisfying
                    d_11(v) >= (11/8-epsilon)phi(v).
                (3) The coloring of G_11 by entrances is proper. A simple graph path lifts to a linear hypergraph path whenever it is strong-rainbow: its edge colors are pairwise distinct and none of those entrance colors is a vertex of the graph path.
                
                Thus any asymptotic 43/48 extremizer contains, after discarding o(S) weighted defect, a properly edge-colored terminal graph whose local degree is asymptotically 11/8 times endpoint potential. Ordinary rainbowness alone is not asserted to guarantee a linear lift.

              • [1000608] Correction: terminal-shadow lifting requires strong-rainbow, not ordinary rainbow
                  STATEMENT
                  Let G be the terminal-pair graph of a linear 3-uniform hypergraph, with an edge uv colored by the entrance x of its parent hyperedge {x,u,v}. A simple graph path
                  v_0v_1...v_k
                  with edge colors x_1,...,x_k lifts in the displayed order to a linear hypergraph path
                  {x_i,v_{i-1},v_i}, i=1,...,k,
                  if and only if:
                  (1) the colors x_i are pairwise distinct; and
                  (2) no color x_i belongs to the graph-path vertex set {v_0,...,v_k} except in the impossible incident cases excluded by linearity.
                  
                  Thus ordinary rainbow is insufficient in a self-colored terminal graph. The correct lifting condition is strong-rainbow: pairwise distinct colors, all avoiding the graph-path vertices.
                  
                  Consequently the counting and degree-stability conclusions (1),(2) of 420e9aea15cc remain unaffected, but its lifting assertion (3) must be replaced by the strong-rainbow statement above; in particular G_11 is not thereby proved rainbow-P_ell-free.

                • [1000606] A clean common entrance consumes two distinct strict-superlevel vertices per edge
                    STATEMENT
                    Fix the globally chosen maximum endpoint path P_x at a vertex x. Let F_x be any family of ascending nonspecial edges
                      e={x,u_e,v_e}
                    whose unique entrance is x and whose source incidence is clean relative to P_x, that is mu_x(e)=0.
                    
                    Then the terminal pairs {u_e,v_e}, e in F_x, are pairwise disjoint, are disjoint from V(P_x), and lie in the strict potential superlevel
                      V_{>phi(x)}={w:phi(w)>phi(x)}.
                    Consequently
                      2|F_x| <= |V_{>phi(x)} minus V(P_x)|.
                    
                    In particular, if c_11(x) counts U_11 edges colored by entrance x in the near-extremal terminal graph, then
                      2c_11(x) <= |V_{>phi(x)} minus V(P_x)|.

                  • [1000259] A source rail couples its two terminal stars into one alternating blocker system
                      STATEMENT
                      Let e={x,u,v} be an ascending nonspecial edge of rank q>=2, with unique entrance x and terminals u,v. Let
                        R=(g_1,...,g_{q-1})
                      be a canonical maximum source rail ending physically at x, so R,e is a q-edge path and R avoids u,v. Put
                        W=V(R) minus {x},
                      so |W|=2q-2.
                      
                      For w in {u,v}, let T_w be any family of distinct nonspecial edges f!=e through w such that w is a terminal of f and phi(f)<=q+1. Then every f in T_w meets W in one or two vertices. Let S_w and B_w count the one-contact and two-contact members of T_w, and let M_w be the set of two-vertex contact pairs of the B_w members.
                      
                      Then:
                      (1) M_u and M_v are matchings on W and are edge-disjoint.
                      (2) M_u union M_v is a simple maximum-degree-two graph whose nontrivial components are alternating paths and even alternating cycles.
                      (3) If p is the number of path components, isolated vertices included, then
                          p=(2q-2)-(B_u+B_v).
                      (4) If U_w is the number of vertices of W unused by all contacts from T_w, then
                          S_u+S_v+U_u+U_v=2p.
                      (5) Writing d_w^*=1+|T_w|=1+S_w+B_w for the truncated star count including e,
                          2d_w^*=2q+S_w-U_w,
                      and hence
                          d_u^*+d_v^*=2q+S_u+S_v-p.
                      
                      Thus the two terminal stars of one ascending edge are not independent: on the common source rail their double contacts form a single alternating path-cycle system, and its open-chain defects are exactly the single/unused contact defects of the two stars.

                    • [1001232] Two truncated terminal stars force many bounded-reuse linear triangles
                        STATEMENT
                        Let e={x,u,v} be an ascending nonspecial edge of edge rank q, and let R be a canonical source rail ending at its unique entrance x. For w in {u,v}, restrict to ascending edges terminal at w of edge rank at most q, including e, let t_w be their number, and write delta_w=gamma(q)-t_w>=0. Put Delta=delta_u+delta_v. Then the two truncated terminal stars around the common source rail force at least q/8-3Delta-O(1) distinct linear 3-cycles. More exactly, with alpha(q)=ceil((3q-8)/4), kappa_q=alpha(q)-2gamma(q)+2q in {0,1}, the number is at least one half of 3alpha(q)-2q+2-6kappa_q-6Delta. The resulting triangles have multiplicity at most three when counted over choices of the base edge e.

                • [1000897] Color-terminal collisions on a rank-monotone terminal path point only backward
                    STATEMENT
                    Let
                    v_0v_1...v_k
                    be a simple path in the terminal-pair graph of ascending nonspecial edges. Let
                    E_i={x_i,v_{i-1},v_i}
                    be the parent hyperedge of graph edge v_{i-1}v_i, with rank r_i=phi(E_i), and assume
                    r_1<=r_2<=...<=r_k.
                    
                    Suppose the graph path is rainbow, and some entrance color x_i equals a nonincident path vertex v_j. Then necessarily
                    j<=i-2.
                    Moreover
                    phi(v_j)=r_i-1,
                    and every terminal-path edge incident with v_j has rank at most r_i-1.
                    
                    Thus every obstruction to strong-rainbowness on a nondecreasing-rank rainbow terminal path is a strictly backward color-terminal chord. In particular no entrance color can hit a later nonincident terminal vertex.

                  • [1000222] Backward color-terminal collisions are stabbed by strict rank jumps
                      STATEMENT
                      Let v_0v_1...v_k be a rainbow terminal-pair path of ascending nonspecial edges
                      E_i={x_i,v_{i-1},v_i}, with nondecreasing edge ranks r_1<=...<=r_k.
                      For every color-terminal collision x_i=v_j, put I_i={j+1,...,i-1}.
                      
                      Then I_i contains an index t with r_t<r_{t+1}. Equivalently, every backward collision chord crosses a strict parent-rank jump.
                      
                      Consequently:
                      (1) every contiguous constant-rank block of the terminal path is strong-rainbow;
                      (2) if r_k-r_1=D, all collision chords are stabbed by at most D cuts between consecutive path edges;
                      (3) if there are C collision chords and D>0, some strict-rank cut is crossed by at least ceil(C/D) collision chords;
                      (4) some strong-rainbow contiguous subpath has at least ceil(k/(D+1)) edges.

                    • [1000532] Many backward collisions through one cut contain a large crossing or nested family
                        STATEMENT
                        Let v_0v_1...v_k be a rainbow terminal-pair path, and suppose M color-terminal collision chords x_i=v_j all cross one fixed cut between path edges E_t and E_{t+1}; thus j<t<i for every such chord.
                        
                        Then these M chords contain a subfamily of size at least ceil(sqrt(M)) that is pairwise crossing, or a subfamily of size at least ceil(sqrt(M)) that is pairwise nested.
                        
                        More explicitly, after ordering the chords by increasing left endpoint
                        j_1<...<j_M,
                        their right edge indices i_1,...,i_M are distinct. An increasing subsequence of the i_s gives pairwise crossing chords, while a decreasing subsequence gives pairwise nested chords.

                      • [1000930] A shortest backward collision closes a genuine linear cycle
                          STATEMENT
                          Let v_0v_1...v_k be a rainbow terminal-pair path of ascending nonspecial edges
                          E_s={x_s,v_{s-1},v_s}
                          with nondecreasing edge ranks. Suppose at least one color-terminal collision occurs, and choose x_i=v_j with minimum span i-j.
                          
                          Then i-j>=3, the terminal subpath
                          E_{j+1},E_{j+2},...,E_{i-1}
                          is strong-rainbow and lifts to a linear hypergraph path, and
                          E_{j+1},E_{j+2},...,E_{i-1},E_i
                          is a linear cycle of length i-j.
                          
                          Consequently, if r_i=phi(E_i), then
                          i-j <= r_i.

                        • [1001209] Primitive-collision continuation
                            STATEMENT
                            Route bridge: the nested-collision analysis continues after toolkit lemma 1000483.

                          • [1000652] Two nested backward collisions either shortcut to a linear cycle or contain a further collision
                              STATEMENT
                              Let v_0v_1...v_k be a rainbow terminal-pair path of ascending nonspecial edges
                              E_s={x_s,v_{s-1},v_s}
                              with nondecreasing edge ranks. Suppose
                              x_i=v_j and x_h=v_l
                              are nested backward collisions with
                              j<l<h<i.
                              
                              Consider the shortcut edge sequence
                              C =
                              E_{j+1},E_{j+2},...,E_l,
                              E_h,
                              E_{h+1},E_{h+2},...,E_i.
                              
                              Then exactly one of the following holds.
                              
                              (A) C is a linear cycle, of length
                              L=(l-j)+1+(i-h)=i-j-(h-l)+1.
                              In this case every edge of C has rank at least L, and in particular r_i>=L+1.
                              
                              (B) There is an additional backward color-terminal collision x_b=v_a, distinct from the two displayed collisions, whose interval [a,b] is contained in [j,l], or contained in [h,i], or satisfies
                              j<=a<l<h<b<=i.
                              In the last case [l,h] is properly contained in [a,b], which is properly contained in [j,i] unless an endpoint agrees with the outer collision.
                              
                              Thus a nested pair that does not yield the shortcut cycle necessarily exposes a further collision in one of the two flanks or between the two nesting levels.

                            • [1000453] A saturated nested collision chain yields shortcut cycles or edge-disjoint primitive flank cycles
                                STATEMENT
                                Let
                                I_a=[j_a,i_a],  a=1,...,m,
                                be a saturated strictly nested chain of backward color-terminal collision intervals on a rainbow nondecreasing-rank terminal path:
                                j_1<j_2<...<j_m<i_m<...<i_2<i_1,
                                and there is no collision interval J with
                                I_a strictly containing J strictly containing I_{a+1}
                                for any a.
                                
                                For each adjacent pair I_a superset I_{a+1}, one of the following holds.
                                
                                (S_a) The nested shortcut from 94579ab0aabc is a linear cycle of length
                                L_a=(j_{a+1}-j_a)+1+(i_a-i_{a+1}),
                                and the outer colliding rank satisfies
                                r_{i_a}>=L_a+1.
                                
                                (F_a) One of the two flanks
                                [j_a,j_{a+1}] or [i_{a+1},i_a]
                                contains a backward collision interval. Consequently that flank contains an inclusion-minimal collision interval, which by 6aba8c1331b7 closes a genuine linear cycle.
                                
                                Moreover, primitive cycles chosen from the flanks for distinct indices a are edge-disjoint. Thus if f of the m-1 adjacent pairs fail to shortcut, the terminal path contains at least f pairwise edge-disjoint primitive nonspecial cycles, each of length at least three.

                              • [1000778] A saturated nested collision chain packs linearly many edge-disjoint linear cycles
                                  STATEMENT
                                  Under the hypotheses of 65825e12de66, let
                                  I_1 strictly contain I_2 strictly contain ... strictly contain I_m
                                  be a saturated nested chain of backward collision intervals.
                                  
                                  Then the hypergraph contains at least
                                  ceil((m-1)/2)
                                  pairwise edge-disjoint linear cycles, each consisting entirely of ascending nonspecial edges and each having length at least three.

                                • [1000416] Fixed-cut collision congestion gives a large crossing family or many edge-disjoint cycles
                                    STATEMENT
                                    Let M backward color-terminal collision chords of a rainbow nondecreasing-rank terminal path all cross one fixed cut.
                                    
                                    Then at least one of the following holds:
                                    (1) there are at least ceil(sqrt(M)) pairwise crossing collision chords;
                                    (2) the hypergraph contains at least
                                    ceil((ceil(sqrt(M))-1)/2)
                                    pairwise edge-disjoint linear cycles consisting entirely of ascending nonspecial edges.
                                    
                                    Thus fixed-cut collision congestion reduces, with square-root loss, to the genuinely crossing case or to linear cycle packing.

                                  • [1001180] Crossing-collision continuation
                                      STATEMENT
                                      Route bridge: fixed-cut collision packing continues using toolkit lemma 1000126.

                                    • [1000769] A saturated crossing collision family packs linearly many edge-disjoint cycles
                                        STATEMENT
                                        Let
                                        I_a=[j_a,i_a], a=1,...,m,
                                        be a pairwise crossing family of backward collision intervals on a rainbow nondecreasing-rank terminal path, ordered so that
                                        j_1<...<j_m<t<i_1<...<i_m
                                        for some fixed cut t.
                                        
                                        Assume the family is saturated: for each a<m there is no additional collision interval [u,w] with
                                        j_a<u<j_{a+1}
                                        and
                                        i_a<w<i_{a+1}.
                                        
                                        Then the hypergraph contains at least
                                        ceil((m-1)/2)
                                        pairwise edge-disjoint linear cycles, each consisting entirely of ascending nonspecial edges and each having length at least three.

                                      • [1001028] Fixed-cut backward collisions force square-root many edge-disjoint nonspecial cycles
                                          STATEMENT
                                          Let M backward color-terminal collision chords of a rainbow terminal-pair path of ascending nonspecial edges with nondecreasing edge ranks all cross one fixed cut.
                                          
                                          Then the hypergraph contains at least
                                          ceil((ceil(sqrt(M))-1)/2)
                                          pairwise edge-disjoint linear cycles, each consisting entirely of ascending nonspecial edges and each having length at least three.

                    • [1000938] Rank spread bounds nondecreasing rainbow terminal paths in a path-free hypergraph
                        STATEMENT
                        Let H be a P_ell^(3)-free linear 3-graph. Let v_0v_1...v_k be a rainbow terminal-pair path of ascending nonspecial parent edges E_i={x_i,v_{i-1},v_i} with nondecreasing edge ranks r_1<=...<=r_k. If D=r_k-r_1, then
                        k <= (D+1)(ell-1).
                        Equivalently, any such rainbow terminal path with k>(D+1)(ell-1) forces an ell-edge linear path in H.

                  • [1000413] U_11 color-terminal collisions are confined to one factor-two edge-rank scale
                      STATEMENT
                      Let v_0v_1...v_k be a rainbow terminal-pair path of ascending nonspecial edges with nondecreasing edge ranks r_1<=...<=r_k. Suppose x_i=v_j is a color-terminal collision. If F is either parent edge incident with v_j (that is, F=E_{j+1}, and also F=E_j when j>=1), then
                      
                      ceil((r_i+1)/2) <= phi(F) <= r_i-1.
                      
                      Equivalently, r_i <= 2phi(F)-1. Thus a color-terminal collision cannot jump backward to a path location whose incident parent-edge rank is less than half the colliding edge rank.

                    • [1000986] A factor-two edge-rank jump is a barrier to U_11 color-terminal collisions
                        STATEMENT
                        Let
                        v_0v_1...v_k
                        be a rainbow path in the terminal-pair graph whose parent hyperedges are ascending nonspecial edges in U_11, with nondecreasing edge ranks
                        r_1<=...<=r_k.
                        
                        If for some t
                        r_{t+1}>=2r_t,
                        then no color-terminal collision x_i=v_j satisfies
                        j<t<i.
                        Equivalently, no collision interval crosses the cut between E_t and E_{t+1}.

                  • [1001168] A backward color-terminal collision forces double blocking of the colliding source rail
                      STATEMENT
                      Retain the setting of c9a012c1b82e. Let
                      v_0v_1...v_k
                      be a rainbow terminal-pair path with nondecreasing parent ranks r_1<=...<=r_k, and suppose
                      E_i={x_i,v_{i-1},v_i}
                      has a color-terminal collision x_i=v_j with j<=i-2.
                      
                      Let R_i be any canonical source rail of E_i: an (r_i-1)-edge path ending at x_i such that R_i,E_i is a longest r_i-edge path, so R_i avoids the terminals v_{i-1},v_i.
                      
                      Then E_{j+1} has at least two distinct vertices on R_i. If j>=1, E_j also has at least two distinct vertices on R_i. Moreover the additional R_i-contact vertices supplied by E_j and E_{j+1} are distinct.
                      
                      Thus every interior backward collision forces the two terminal-path edges adjacent to the hit vertex to be double blockers of the colliding edge's maximum source rail.

                    • [1000024] Collision-adjacent double blockers are localized on the source-rail tail
                        STATEMENT
                        Retain the setting of fff2955f7084. Thus x_i=v_j is a backward collision for the rank-r_i edge E_i, and R_i is a canonical (r_i-1)-edge source rail ending at x_i.
                        
                        Let F be either E_{j+1}, or E_j when j>=1, and put s=phi(F). Then F is not an edge of R_i. Among the vertices of F∩V(R_i) distinct from x_i, choose z closest to x_i along R_i, and let d be the number of R_i-edges in the segment from z to x_i.
                        
                        Then
                        1 <= d <= s-1 <= r_i-2.
                        
                        For F=E_j and F=E_{j+1}, the chosen vertices z are distinct. Hence an interior backward collision forces two distinct lower-rank blocker contacts into rank-controlled terminal segments of its source rail.

                    • [1000433] A U_11 color-terminal collision has exact blockers except at explicit boundary cases
                        STATEMENT
                        Let v_0v_1...v_k be a rainbow terminal-pair path whose parent hyperedges E_s={x_s,v_{s-1},v_s} are ascending nonspecial edges in U_11, with nondecreasing edge ranks r_s=phi(E_s). Suppose x_i=v_j is a color-terminal collision, and let P_{x_i}=(g_1,...,g_p) be the chosen maximum path ending at x_i used for the source incidence of E_i, where p=phi(x_i)=r_i-1 and h=g_p.
                        
                        For either parent edge F incident with v_j (F=E_{j+1}, and also F=E_j when j>=1), put s=phi(F). Then
                        
                        (1) ceil((r_i+1)/2) <= s <= r_i-1.
                        
                        (2) If F!=h, then there is a unique vertex c_F!=x_i with
                            F intersect V(P_{x_i})={x_i,c_F}.
                        
                        (3) If moreover s<p, and a_F,b_F are the first and last path-edge indices containing c_F, then
                            a_F<=s-1,
                            b_F>=r_i-s+1,
                        with the stronger a_F<=s-2 when c_F is the opposite terminal of F rather than its unique entrance.
                        
                        At most one of the two adjacent parent edges can equal h. Hence every interior color-terminal collision has at least one genuine exact off-x_i contact on P_{x_i}; if neither adjacent parent edge is h, both exact contacts exist and are distinct.

                      • [1000226] Every interior U_11 color-terminal collision closes a local linear cycle, including the last-edge boundary
                          STATEMENT
                          Let v_0v_1...v_k be a rainbow terminal-pair path whose parent hyperedges E_s={x_s,v_{s-1},v_s} belong to U_11 and have nondecreasing edge ranks r_s=phi(E_s). Let x_i=v_j be an interior color-terminal collision. Let R_i=(g_1,...,g_p) be the chosen maximum source path ending at x_i, where p=r_i-1, and put h=g_p.
                          
                          For every F in {E_j,E_{j+1}} with F!=h, let c_F be the exact off-x_i contact supplied by 608468bb403b.
                          
                          If neither adjacent parent equals h, then E_j together with the R_i-segment between c_{E_j},c_{E_{j+1}} and E_{j+1} is a linear cycle; if that host segment has d edges, then d+2<=r_j.
                          
                          If E_{j+1}=h, let b be the last index of an R_i-edge containing c_{E_j}. Then E_j,g_b,...,g_p is a linear cycle of length p-b+2<=r_j. If E_j=h, the symmetric statement holds with E_{j+1}.
                          
                          Thus every interior U_11 color-terminal collision closes a local linear cycle; at the host-last-edge boundary the cycle is closed by the single adjacent parent having a genuine off-x_i contact.

                        • [1000148] Every interior U_11 color-terminal collision has rank-sum surplus, a local 3-cycle, or an explicit last-edge boundary cycle
                            STATEMENT
                            Retain the setting of 3216d2e9afcd. For an interior color-terminal collision x_i=v_j, let R_i=(g_1,...,g_p), p=r_i-1, be the chosen maximum source path and h=g_p its last edge. At least one of the following holds:
                            
                            (1) r_j+r_{j+1}>=r_i+3;
                            
                            (2) some edge g of R_i together with E_j,E_{j+1} forms a linear 3-cycle;
                            
                            (3) one of E_j,E_{j+1} equals h. The other adjacent parent F has a genuine exact off-x_i contact and, together with the terminal host segment from that contact to x_i, forms the boundary cycle of 3216d2e9afcd.
                            
                            If neither adjacent parent equals h, only (1) and (2) are possible. Hence away from the explicit last-edge boundary, the universal lower bound r_j+r_{j+1}>=r_i+2 can be tight only in the local-3-cycle case.

                          • [1000123] Every interior U_11 color-terminal collision pays plus three or forces owner-to-hit source-path overlap
                              STATEMENT
                              Let
                              v_0v_1...v_k
                              be a rainbow terminal-pair path whose parent hyperedges
                              E_s={x_s,v_{s-1},v_s}
                              belong to U_11 and have nondecreasing edge ranks r_s. Let R_s be the chosen maximum source path ending at x_s.
                              
                              For every interior color-terminal collision
                                x_i=v_j,
                              at least one of the following holds:
                              
                              (1) r_j+r_{j+1} >= r_i+3;
                              
                              (2) x_j belongs to V(R_i), and consequently
                                  |V(R_i) intersect V(R_j)|>=2.
                              
                              Thus the sole failure of the plus-three adjacent edge-rank-sum inequality is never geometrically free: it forces a multiple intersection between the colliding source path and the source path of the left parent edge adjacent to the hit terminal vertex.

                            • [1000598] Tight U_11 color-terminal collisions contain a half-size matching of multiple-overlap source-path pairs
                                STATEMENT
                                Let T be a family of interior U_11 color-terminal collisions
                                  x_i=v_j
                                on one simple rainbow terminal-pair path, all satisfying the tight equality
                                  r_j+r_{j+1}=r_i+2.
                                
                                For each collision draw the directed index edge
                                  i -> j.
                                Then these directed edges form a vertex-disjoint union of directed paths. In particular T contains a subfamily T' of size at least
                                  ceil(|T|/2)
                                such that all indices occurring in the pairs {i,j} are distinct.
                                
                                For every collision i->j in T',
                                  |V(R_i) intersect V(R_j)|>=2.
                                
                                Hence |T| tight collisions force at least ceil(|T|/2) index-disjoint pairs of chosen maximum source paths having at least two common vertices.

                          • [1000173] Every interior U_11 collision pays rank-sum surplus, a rotation packet, or a low-rank boundary triangle
                              STATEMENT
                              Let
                              v_0v_1...v_k
                              be a rainbow path in the terminal-pair graph whose parent hyperedges
                              E_s={x_s,v_{s-1},v_s}
                              belong to U_11 and have nondecreasing edge ranks r_s.
                              
                              For every interior color-terminal collision x_i=v_j, 1<=j<=i-2, let
                              R_i=(g_1,...,g_{r_i-1})
                              be the chosen maximum source path ending at x_i and let h=g_{r_i-1}. At least one of the following holds.
                              
                              (A) Rank-sum surplus:
                                r_j+r_{j+1}>=r_i+3.
                              
                              (B) Nonboundary exact-half-rank rotation:
                                r_j+r_{j+1}=r_i+2,
                              and either
                                (B-even) r_i=2m with m>=3 and r_j=r_{j+1}=m+1,
                              or
                                (B-odd) r_i=2m+1 with m>=2, r_j=m+1, r_{j+1}=m+2, and E_{j+1}!=h.
                              In either case one adjacent parent edge has its unique entrance at a private vertex of a middle edge of R_i and meets R_i otherwise only at x_i. Rotating through that parent gives an (r_i-1)-edge linear path whose last edge has edge rank at least r_i-1 and which has two distinct possible last vertices of vertex rank at least r_i-1.
                              
                              (C) Low-rank boundary triangle:
                              either
                                r_i=4 and r_j=r_{j+1}=3,
                              or
                                r_i=5, r_j=3, r_{j+1}=4, and E_{j+1}=h.
                              In either case the collision closes a local linear 3-cycle.
                              
                              Thus failure of the plus-three edge-rank-sum inequality is confined to exact half-rank states: all nonboundary states emit the near-owner-rank rotation packet, while the only omitted states are two explicit low-rank triangle boundaries.

                            • [1001009] Tight-collision rotation outputs split into rank rise, rank-p special/nonascending, or one exact ascending entrance
                                STATEMENT
                                Retain outcome (B) of 259bdff45872 and put
                                  p=r_i-1.
                                Let h be the last edge of the p-edge rotated path, and let y,z be the two distinct vertices of h that can be chosen as last vertices of that rotation. Then
                                  phi(h)>=p,
                                  phi(y)>=p,
                                  phi(z)>=p.
                                
                                Consequently exactly one of the following holds:
                                
                                (1) phi(h)>p;
                                
                                (2) phi(h)=p and h is special;
                                
                                (3) phi(h)=p, h is nonspecial and nonascending;
                                
                                (4) phi(h)=p and h is ascending nonspecial. In this case neither y nor z is the unique entrance of h. The third vertex w of h is the unique entrance and
                                    phi(w)=p-1.
                                
                                In alternatives (2) and (3), every vertex of h has vertex rank at least p. In alternative (4), h has exactly two vertices of vertex rank at least p, namely y,z, and one unique entrance w of vertex rank p-1.
                                
                                For the smallest parity-boundary cases in which h is also the last edge of the original path R_i, the third vertex is x_i and already has vertex rank p; hence alternative (4) cannot occur there.

                          • [1000294] Local 3-cycle collisions have bounded host-edge reuse
                              STATEMENT
                              Let T be a family of interior color-terminal collisions x_i=v_j on one simple rainbow terminal-pair path. Suppose every collision in T is of the local 3-cycle type from 20ee63fa1617: for each hit index j choose an edge g_j of the colliding chosen maximum path such that
                                g_j,E_j,E_{j+1}
                              form a linear 3-cycle.
                              
                              Then there is a subfamily T' with
                                |T'|>=ceil(|T|/2)
                              whose distinguished parent-edge pairs {E_j,E_{j+1}} are pairwise edge-disjoint.
                              
                              Within T', any fixed hyperedge g occurs as g_j for at most four collisions. Consequently the family {g_j : j in T'} contains at least
                                ceil(|T'|/4)
                                >= ceil(ceil(|T|/2)/4)
                              distinct hyperedges.

                            • [1000260] Triangle collisions force distinct host edges at half the owner edge rank
                                STATEMENT
                                Retain the family T and host edges g_j from 3f165c52a1a6. Suppose every colliding owner E_i in T has edge rank at least R.
                                
                                Then T contains a subfamily T' of size at least ceil(|T|/2) such that:
                                (1) the distinguished parent-edge pairs are pairwise disjoint;
                                (2) every fixed host hyperedge occurs for at most four members of T';
                                (3) every host hyperedge g_j has edge rank at least ceil(R/2).
                                
                                Consequently T produces at least
                                  ceil(ceil(|T|/2)/4)
                                distinct hyperedges of edge rank at least ceil(R/2).

                            • [1000334] Local 3-cycle collisions force a linear packing of edge-disjoint 3-cycles
                                STATEMENT
                                Let T be a family of interior U_11 color-terminal collisions on one simple rainbow terminal-pair path, and suppose every member is of the local linear 3-cycle type from 20ee63fa1617.
                                
                                Then the hypergraph contains at least
                                  ceil(|T|/32)
                                pairwise edge-disjoint linear 3-cycles arising from members of T.

                            • [1001092] Fourfold triangle-host reuse forces two further color-terminal collisions
                                STATEMENT
                                Retain the parity-selected family T' from 3f165c52a1a6, so the distinguished parent-edge pairs {E_j,E_{j+1}} are pairwise disjoint. Fix a hyperedge g.
                                
                                If g is the third edge of four distinguished linear 3-cycles
                                  g,E_j,E_{j+1},
                                then at least two vertices of g are simultaneously:
                                (1) terminal-path vertices v_s of the rainbow terminal-pair path, and
                                (2) unique entrance labels x_t of parent hyperedges.
                                
                                Hence fourfold reuse of one triangle host forces at least two additional color-terminal collisions x_t=v_s on the same rainbow terminal-pair path.

                          • [1000377] Equality in the U_11 collision rank-sum bound has an exact central normal form
                              STATEMENT
                              Retain an interior U_11 color-terminal collision x_i=v_j on a rainbow terminal-pair path with nondecreasing parent edge ranks. Let
                                R_i=(g_1,...,g_{r_i-1})
                              be the chosen maximum path with last vertex x_i, and let c_j,c_{j+1} be the exact contacts of E_j,E_{j+1} with R_i.
                              
                              Assume the minimum possible adjacent rank sum occurs:
                                r_j+r_{j+1}=r_i+2.
                              
                              Then the collision is of the local linear 3-cycle type, and the following more precise alternatives hold.
                              
                              (Even owner rank.) If r_i=2q, then
                                r_j=r_{j+1}=q+1.
                              The only possible contact vertices for either edge are
                                g_{q-1} intersect g_q,
                                the private vertex of g_q,
                                g_q intersect g_{q+1}.
                              Thus c_j and c_{j+1} are two distinct vertices of g_q, and
                                g_q,E_j,E_{j+1}
                              is the local linear 3-cycle.
                              
                              (Odd owner rank.) If r_i=2q+1, then
                                r_j=q+1,   r_{j+1}=q+2.
                              Moreover
                                c_j=g_q intersect g_{q+1}.
                              The other exact contact c_{j+1} is one of
                                g_{q-1} intersect g_q,
                                the private vertex of g_q,
                                the private vertex of g_{q+1},
                                g_{q+1} intersect g_{q+2}.
                              Accordingly the local linear 3-cycle uses host edge g_q or g_{q+1}.

                            • [1000544] Nonspecial middle edges have strict half-path edge rank
                                STATEMENT
                                Let P=(g_1,...,g_L) be a linear path.
                                
                                (1) If L=2q-1 and the middle edge g_q is nonspecial, then
                                  phi(g_q)>=q+1.
                                
                                (2) If L=2q, then each of the two middle edges g_q,g_{q+1} has edge rank at least q+1. Moreover, if g_q is nonspecial with phi(g_q)=q+1, its unique entrance is the central joint
                                  g_q intersect g_{q+1};
                                and if g_{q+1} is nonspecial with phi(g_{q+1})=q+1, its unique entrance is the same central joint.

                          • [1000679] Tight U_11 collisions have half-rank central form outside two explicit low-rank boundary cases
                              STATEMENT
                              Retain an interior U_11 color-terminal collision x_i=v_j on a nondecreasing-rank rainbow terminal-pair path and suppose
                                r_j+r_{j+1}<=r_i+2.
                              Let R_i=(g_1,...,g_{r_i-1}) be the chosen maximum source path ending at x_i, with last edge h.
                              
                              Then equality holds:
                                r_j+r_{j+1}=r_i+2.
                              Moreover r_i>=4, and exactly the following possibilities remain.
                              
                              (1) Low-rank even case: r_i=4 and r_j=r_{j+1}=3. The collision closes a local linear 3-cycle. No assertion of two genuine exact off-x_i contacts is made.
                              
                              (2) Even central case: r_i=2m with m>=3. Then r_j=r_{j+1}=m+1, neither adjacent parent equals h, and both genuine exact contacts c_j,c_{j+1} lie on g_m. Each is one of the backward joint, private vertex, or forward joint of g_m, and the two are distinct. Hence g_m,E_j,E_{j+1} is a linear 3-cycle.
                              
                              (3) Odd central case: r_i=2m+1 with m>=2, r_j=m+1 and r_{j+1}=m+2. The contact c_j is the joint g_m∩g_{m+1}. If E_{j+1}!=h, its exact contact c_{j+1} lies on g_m or g_{m+1}, and one of those host edges with E_j,E_{j+1} forms a linear 3-cycle. The only possible last-edge boundary is m=2 (r_i=5), E_{j+1}=h; in that case g_3,E_j,h is a linear 3-cycle.
                              
                              Thus every failure of the plus-three inequality lies at the exact half-rank boundary and still closes a local 3-cycle; the previous two-exact-contact normal form requires the explicit low-rank boundary qualification above.

                            • [1000678] The nonboundary odd half-rank tight collision is one-sided at the middle joint
                                STATEMENT
                                Retain the odd central case of 9b023ed3d700:
                                  r_i=2m+1 with m>=2,
                                  r_j=m+1,
                                  r_{j+1}=m+2,
                                  R_i=(g_1,...,g_{2m}).
                                Assume the nonboundary case E_{j+1}!=h, where h=g_{2m} is the host last edge.
                                
                                Then:
                                (1) the exact contact of E_j is its unique entrance
                                    x_j=g_m∩g_{m+1};
                                (2) the genuine exact contact c_{j+1} of E_{j+1} lies on g_m and is distinct from x_j, hence it is either
                                    g_{m-1}∩g_m
                                    or the private vertex of g_m;
                                (3) consequently
                                    g_m,E_j,E_{j+1}
                                    is the unique local 3-cycle host among the two middle edges g_m,g_{m+1}.
                                
                                Thus every nonboundary tight odd collision is oriented: the rank-(m+1) parent enters at the middle joint, while the rank-(m+2) parent returns on the left middle edge. The sole boundary case m=2, E_{j+1}=h is handled separately in 9b023ed3d700.

                              • [1000776] The odd tight U_11 collision reduces to a cycle, multiple source-path overlap, or reciprocal terminal exchange
                                  STATEMENT
                                  Retain the odd tight color-terminal collision of 9b00516e2965. Thus
                                    r_i=2m+1,
                                    r_j=m+1,
                                    r_{j+1}=m+2,
                                  the chosen maximum path
                                    R_i=(g_1,...,g_{2m})
                                  ends at x_i=v_j,
                                    x_j=g_m intersect g_{m+1},
                                  and the exact contact c_{j+1} of E_{j+1} with R_i lies on g_m.
                                  
                                  Let
                                    Q=(g_1,...,g_m),
                                  so Q is a maximum m-edge path with last vertex x_j.
                                  Let R_j and R_{j+1} be the chosen maximum source paths of E_j and E_{j+1}, ending at x_j and x_{j+1} respectively.
                                  
                                  Then at least one of the following holds:
                                  
                                  (1) Q union R_j contains a linear cycle;
                                  
                                  (2) R_j and R_{j+1} have at least two common vertices;
                                  
                                  (3) all of the following hold:
                                      (a) g_m is the last edge of R_j;
                                      (b) c_{j+1}=v_{j+1};
                                      (c) E_{j+1} intersect V(R_j)={v_{j+1}};
                                      (d) E_j intersect V(R_{j+1})={v_{j-1}};
                                      (e) R_j and R_{j+1} have exactly one common vertex, which is an internal joint at the same path-edge index on both paths.
                                  
                                  Thus the hard residue of the odd half-rank collision is a reciprocal terminal-terminal exchange between the two adjacent source paths.

                                • [1000030] In the odd tight reciprocal-exchange residue the two cross-terminal contacts lie on the same side of the aligned joint
                                    STATEMENT
                                    Retain alternative (3) of ac73dd583c10. Let
                                      A=R_j
                                    be the m-edge chosen maximum source path ending at x_j, and let
                                      B=R_{j+1}
                                    be the (m+1)-edge chosen maximum source path ending at x_{j+1}.
                                    
                                    The paths A and B have exactly one common vertex z, which is an internal joint at the same path-edge index k on both paths. Thus write
                                      A=A^- union A^+,
                                      B=B^- union B^+,
                                    where A^-,B^- are the k-edge prefixes ending at z and A^+,B^+ are the complementary suffixes from z to x_j,x_{j+1}.
                                    
                                    The exact cross-contacts are
                                      E_{j+1} intersect V(A)={v_{j+1}},
                                      E_j intersect V(B)={v_{j-1}}.
                                    
                                    Then v_{j+1} and v_{j-1} lie on the same side of z:
                                    either
                                      v_{j+1} in V(A^- ) minus {z}
                                    and
                                      v_{j-1} in V(B^- ) minus {z},
                                    or
                                      v_{j+1} in V(A^+ ) minus {z}
                                    and
                                      v_{j-1} in V(B^+ ) minus {z}.
                                    
                                    The two mixed orders are impossible.

                                  • [1000449] The reciprocal terminal-exchange residue of an odd tight U_11 collision is impossible
                                      STATEMENT
                                      Retain the odd tight U_11 color-terminal collision of ac73dd583c10:
                                        r_i=2m+1,
                                        r_j=m+1,
                                        r_{j+1}=m+2.
                                      Let
                                        A=R_j=(a_1,...,a_m)
                                      and
                                        B=R_{j+1}=(b_1,...,b_{m+1})
                                      be the chosen maximum source paths.
                                      
                                      Then alternative (3) of ac73dd583c10 cannot occur.
                                      
                                      Consequently every odd tight collision has at least one of the following additional structures beyond its forced central linear 3-cycle:
                                      (1) the maximum m-edge prefix Q=(g_1,...,g_m) of the colliding source path and R_j contain a linear cycle;
                                      (2) R_j and R_{j+1} have at least two common vertices.

                              • [1000909] A nonboundary odd tight U_11 collision forces a full-length rotation and near-owner-rank output
                                  STATEMENT
                                  Retain the nonboundary odd tight collision of 9b00516e2965:
                                    r_i=2m+1 with m>=2,
                                    r_j=m+1,
                                    r_{j+1}=m+2,
                                    R_i=(g_1,...,g_{2m}),
                                    x_j=g_m intersect g_{m+1},
                                  and assume E_{j+1}!=h=g_{2m}.
                                  
                                  Then the exact contact of E_{j+1} on the precursor of R_i is the private vertex b_m of g_m. Consequently E_{j+1} intersect V(R_i)={b_m,x_i}, and
                                    g_1,...,g_m,E_{j+1},g_{2m},g_{2m-1},...,g_{m+2}
                                  is a 2m-edge linear path.
                                  
                                  In particular phi(g_{m+2})>=2m=r_i-1; and if z_{m+1}=g_{m+1} intersect g_{m+2} and b_{m+2} is the private vertex of g_{m+2}, then phi(z_{m+1}),phi(b_{m+2})>=2m.
                                  
                                  No assertion is made here for the isolated boundary case m=2,E_{j+1}=h.

                            • [1001089] The even half-rank central collision has one surviving two-entrance pattern and a full-length rotation
                                STATEMENT
                                Retain the even central case of 9b023ed3d700:
                                  r_i=2m with m>=3,
                                  r_j=r_{j+1}=m+1,
                                  R_i=(g_1,...,g_{2m-1}),
                                and neither adjacent parent is the host last edge.
                                
                                Let
                                  L=g_{m-1}∩g_m,
                                  B=the private vertex of g_m,
                                  R=g_m∩g_{m+1}.
                                Then the two genuine exact contacts of E_j,E_{j+1} are exactly B and R, in some order, and both contacts are the unique entrances of their parent edges.
                                
                                Let F be the parent edge whose exact contact is B. Then F meets R_i exactly at B and the last vertex x_i, and
                                  g_1,...,g_m,F,g_{2m-1},g_{2m-2},...,g_{m+2}
                                is a (2m-1)-edge linear path.
                                
                                Consequently
                                  phi(g_{m+2})>=2m-1=r_i-1,
                                and both g_{m+1}∩g_{m+2} and the private vertex of g_{m+2} have vertex rank at least 2m-1.

                          • [1001085] Many local triangle collisions force linearly many edge-disjoint 3-cycles
                              STATEMENT
                              Let
                                v_0v_1...v_k
                              be a rainbow path in the terminal-pair graph with parent hyperedges
                                E_s={x_s,v_{s-1},v_s}.
                              Let M be a set of interior color-terminal collisions x_i=v_j for which there is a hyperedge g_i such that
                                g_i,E_j,E_{j+1}
                              form a linear 3-cycle, as in alternative (2) of 20ee63fa1617.
                              
                              Then the hypergraph contains at least floor(|M|/32) pairwise edge-disjoint linear 3-cycles of this form.
                              
                              More explicitly:
                              (1) one parity class of hit indices j has size at least |M|/2 and its distinguished parent-edge pairs {E_j,E_{j+1}} are pairwise disjoint;
                              (2) within such a parity class, any fixed hyperedge g can be the third edge of at most four distinguished 3-cycles;
                              (3) after choosing one cycle for each distinct third edge, the remaining cycle family has an edge-intersection graph of maximum degree at most three.

                        • [1000595] An interior U_11 color-terminal collision forces adjacent edge-rank sum at least the colliding rank plus two
                            STATEMENT
                            In the setting of 3216d2e9afcd, every interior color-terminal collision x_i=v_j satisfies
                              r_j >= ceil((r_i+1)/2),
                              r_{j+1} >= ceil((2r_i+3)/4),
                            and therefore
                              r_j+r_{j+1} >= r_i+2.
                            
                            Equivalently,
                              r_i-r_{j+1} <= r_j-2.

                          • [1000171] The sharp 2q-1 cut barrier; the 2q-2 boundary gives overlap except for the rank-4 triangle
                              STATEMENT
                              Let
                              v_0v_1...v_k
                              be a rainbow terminal-pair path whose parent hyperedges
                              E_s={x_s,v_{s-1},v_s}
                              belong to U_11 and have nondecreasing edge ranks
                              r_1<=...<=r_k.
                              
                              Fix a cut between E_t and E_{t+1}, and put
                                q=r_t,  s=r_{t+1}.
                              
                              For every interior color-terminal collision x_i=v_j crossing this cut, so j<t<i, one has
                                s<=2q-2.
                              
                              Consequently:
                              
                              (1) If s>=2q-1, no color-terminal collision crosses the cut.
                              
                              (2) If s=2q-2, every crossing collision has
                                r_i=2q-2,
                                r_j=r_{j+1}=q.
                              If q=3, then r_i=4 and the collision closes a local linear 3-cycle.
                              If q>=4, the collision is in the even central case with m=q-1>=3; the exact contact of E_j with the chosen maximum source path R_i is its unique entrance x_j, and therefore
                                |V(R_i) intersect V(R_j)|>=2.
                              
                              (3) If q>=4 and M collisions cross a cut with s=2q-2, then at least ceil(M/2) can be chosen so that their source-path pairs (R_i,R_j) are index-disjoint and every selected pair has at least two common vertices. At q=3, every crossing collision is instead one of the rank-4 local-triangle cases from (2).

                            • [1000896] A 2q-3 cut has three rank patterns, with only explicit low-rank boundary cycles obstructing the normal forms
                                STATEMENT
                                Let
                                v_0v_1...v_k
                                be a rainbow terminal-pair path whose parent hyperedges belong to U_11 and have nondecreasing edge ranks. Fix a cut with
                                  r_t=q,
                                  r_{t+1}=2q-3,
                                and let x_i=v_j be an interior color-terminal collision crossing the cut.
                                
                                Then exactly one of the following rank patterns occurs.
                                
                                (T_even)
                                  r_i=2q-2,
                                  r_j=r_{j+1}=q.
                                If q=3, this is the rank-4 low boundary and the collision closes a local linear 3-cycle. If q>=4, it is a nonboundary tight even collision and
                                  |V(R_i) intersect V(R_j)|>=2.
                                
                                (T_odd)
                                  r_i=2q-3,
                                  r_j=q-1,
                                  r_{j+1}=q.
                                Necessarily q>=4. If q=4 and E_{j+1} is the host last edge h of R_i, the collision closes the explicit rank-5 boundary triangle. Otherwise
                                  |V(R_i) intersect V(R_j)|>=2.
                                
                                (P_3)
                                  r_i=2q-3,
                                  r_j=r_{j+1}=q,
                                so
                                  r_j+r_{j+1}=r_i+3.
                                Necessarily q>=4. Put
                                  R_i=(g_1,...,g_{2q-4})
                                and h=g_{2q-4}.
                                If one of E_j,E_{j+1} equals h, then q=4 and the boundary-cycle alternative of 20ee63fa1617 holds.
                                If neither adjacent parent equals h, both have genuine exact contacts c_j,c_{j+1} on R_i. Either their occurrence intervals overlap, in which case some edge of R_i together with E_j,E_{j+1} forms a linear 3-cycle, or the intervals are disjoint. In the disjoint case, after naming c_- the earlier contact and c_+ the later contact,
                                  c_-=g_{q-3} intersect g_{q-2},
                                while c_+ is either the private vertex of g_{q-1} or
                                  g_{q-1} intersect g_q.
                                
                                Thus all crossing states at a 2q-3 cut are finite-state after two explicit low-rank boundary-cycle exceptions are separated.

                              • [1001188] Near-factor-two collision cuts reduce to overlap, triangles, or one terminal-only residue
                                  STATEMENT
                                  Let v_0v_1...v_k be a rainbow terminal-pair path whose parent hyperedges lie in U_11 and have nondecreasing ranks, with chosen maximum source paths R_i.
                                  
                                  At a cut r_t=q, r_{t+1}=2q-3:
                                  1. In the separated plus-three case r_i=2q-3 and r_j=r_{j+1}=q, the later exact contact on R_i is the unique entrance x_s of one adjacent parent edge E_s, and |V(R_i)∩V(R_s)|>=2.
                                  2. Consequently, if M interior color-terminal collisions cross the cut, then either there are at least ceil(M/6) pairwise index-disjoint source-path pairs with at least two common vertices, or at least ceil(M/64) pairwise edge-disjoint linear 3-cycles.
                                  
                                  At the next cut r_t=q, r_{t+1}=2q-4, every interior collision again yields adjacent source-path multiple overlap or a local linear 3-cycle, except possibly the single residual rank pattern
                                  r_i=2q-4, r_j=r_{j+1}=q,
                                  where both exact contacts are opposite terminals with disjoint intervals. In that residue the earlier contact lies in {g_{q-4}∩g_{q-3}, private(g_{q-3})} and the later contact lies in {private(g_{q-2}), g_{q-2}∩g_{q-1}} on R_i=(g_1,...,g_{2q-5}).

                                • [1000718] At a 2q-4 cut the only new collision residue is a four-pattern terminal-only central pair
                                    STATEMENT
                                    Let
                                    v_0v_1...v_k
                                    be a rainbow terminal-pair path whose parent hyperedges belong to U_11 and have nondecreasing edge ranks.
                                    Fix a cut with
                                      r_t=q,
                                      r_{t+1}=2q-4,
                                    and let x_i=v_j be an interior color-terminal collision crossing the cut.
                                    
                                    Then at least one of the following holds:
                                    
                                    (1) there is an adjacent index s in {j,j+1} such that
                                        |V(R_i) intersect V(R_s)|>=2;
                                    
                                    (2) some edge of R_i together with E_j,E_{j+1} forms a linear 3-cycle;
                                    
                                    (3) the ranks are exactly
                                        r_i=2q-4,
                                        r_j=r_{j+1}=q,
                                    and both exact contacts of E_j,E_{j+1} with
                                        R_i=(g_1,...,g_{2q-5})
                                    are opposite terminals, with disjoint contact intervals. Writing c_- for the earlier contact and c_+ for the later one,
                                        c_- belongs to {
                                          g_{q-4} intersect g_{q-3},
                                          private(g_{q-3})
                                        },
                                    and
                                        c_+ belongs to {
                                          private(g_{q-2}),
                                          g_{q-2} intersect g_{q-1}
                                        }.
                                    
                                    Thus the first genuinely new state one rank below the 2q-3 cut is a four-pattern terminal-only central configuration.

                      • [1000866] A U_11 collision gives adjacent rank sum, a host 3-cycle, or two repeated source-path intersections
                          STATEMENT
                          Let
                          v_0v_1...v_k
                          be a rainbow path in the terminal-pair graph whose parent hyperedges
                          E_s={x_s,v_{s-1},v_s}
                          belong to U_11 and have nondecreasing edge ranks r_s.
                          Let x_i=v_j be an interior color-terminal collision, so 1<=j<=i-2.
                          
                          Let R_s denote the chosen maximum path with last vertex x_s used for the source incidence of E_s. Then at least one of the following holds:
                          
                          (1) r_j+r_{j+1} >= r_i+3;
                          
                          (2) there is an edge g of R_i such that g,E_j,E_{j+1} form a linear 3-cycle;
                          
                          (3) both adjacent source paths meet R_i at least twice:
                              |V(R_j) intersect V(R_i)|>=2
                          and
                              |V(R_{j+1}) intersect V(R_i)|>=2.
                          
                          Thus, below the adjacent-rank-sum threshold and in the absence of a host 3-cycle, a U_11 color-terminal collision forces repeated intersections of the colliding source path with both source paths adjacent to the hit terminal vertex.

                        • [1000577] Repeated-intersection collisions contain a linear-size matching of source-path pairs
                            STATEMENT
                            Let M be a family of interior color-terminal collisions x_i=v_j on one rainbow terminal-pair path. Assume that every collision in M has the repeated-intersection outcome
                              |V(R_i) intersect V(R_j)|>=2
                            and
                              |V(R_i) intersect V(R_{j+1})|>=2,
                            where R_s is the chosen maximum path with last vertex x_s.
                            
                            Form a simple graph Q on the parent-edge indices by adding, for every collision x_i=v_j in M, the two edges
                              {i,j}, {i,j+1}.
                            
                            Then Q has exactly 2|M| edges and maximum degree at most four. Consequently Q contains a matching of size at least
                              ceil(2|M|/7).
                            
                            Hence M forces at least ceil(2|M|/7) index-disjoint pairs of chosen maximum source paths, each pair having at least two common vertices.

            • [1001159] 43/48 near-extremizers carry five-sixteenths top-potential rotation mass
                STATEMENT
                Let (H_j) be a sequence of finite linear 3-uniform hypergraphs. Write
                S_j=sum_v phi(v), m_j=|E(H_j)|, and n_j^+=|{v:d(v)>0}|.
                Assume S_j/n_j^+ tends to infinity and
                m_j >= (43/48)S_j-o(S_j).
                
                Choose the maximum endpoint paths and switching families from d287da5967d5. For every active misaligned center v, let R(v) be a set of distinct vertices produced by single-blocker rotations of its chosen maximum phi(v)-edge path, each vertex in R(v) having endpoint potential at least phi(v). Then the choices may be made so that
                sum_v |R(v)| >= (5/16-o(1))S_j.
                
                Thus every asymptotic 43/48 near-extremizer carries center-indexed top-potential rotation-endpoint mass of asymptotic size at least 5S/16.

              • [1000358] Low defect forces thick potential superlevels
                  STATEMENT
                  Let H be a finite linear 3-graph, let v be an active misaligned vertex with p=phi(v)>=8 and q=q(v)<p, and let eta_v be the local defect from b032348c1a8a. Put
                    V_{\ge p}={w:phi(w)>=p}.
                  Then
                    |V_{\ge p}| >= (1/2)[beta(p)-eta_v-ceil((3q-4)/4)]-O(1)
                  and therefore, since q<=p-1,
                    |V_{\ge p}| >= (5/16)p-(1/2)eta_v-O(1).
                  
                  Equivalently,
                    eta_v >= (5/8)p-2|V_{\ge p}|-O(1).
                  
                  Consequently, for any sequence satisfying the 43/48 near-extremal hypotheses of d287da5967d5, for every fixed epsilon>0 all but o(S) endpoint-potential mass lies on vertices v with
                    |V_{\ge phi(v)}| >= (5/16-epsilon)phi(v).
                  Thus asymptotic 43/48 sharpness cannot be supported by sparse high-potential spikes; almost all potential mass must lie in quantitatively thick superlevel sets.

              • [1001014] Sublinear rotation-endpoint reuse would lower the r=3 coefficient to 19/24
                  STATEMENT
                  Let (H_j) be a sequence of finite linear 3-uniform hypergraphs, with
                  S_j=sum_v phi(v) and n_j^+ the number of nonisolated vertices, and assume S_j/n_j^+ tends to infinity.
                  
                  For each active misaligned vertex v choose the maximum path, switching family, and rotation-endpoint set R(v) supplied by b032348c1a8a and 5f8d96bf566a. Suppose the maximum reuse multiplicity
                  M_j=max_w |{v:w in R(v)}|
                  satisfies
                  M_j n_j^+=o(S_j).
                  
                  Then
                  |E(H_j)| <= (19/24+o(1)) S_j.
                  
                  In particular, an absolute bound on rotation-endpoint reuse would improve the present 43/48 leading coefficient to 19/24 in the large-potential regime.

          • [1001101] Lens-free dense switching theorem
              STATEMENT
              Let v have p=phi(v)>=8. Let T(v) be the ascending nonspecial edges terminal at v, let t=|T(v)|, and when t>0 let q be their maximum edge rank. Choose the maximum p-edge path P_v as in a57007500001. Let D_v count incident double contacts on P_v and put
                beta(p)=floor((11p-16)/8),
                eta_v=beta(p)-t+D_v.
              
              Then eta_v>=0. If q=p, then
                eta_v>=beta(p)-ceil((3p-4)/4)>=(5p-24)/8.
              
              If q<p, write gamma for the exact fixed-entrance bound and a(q)=ceil((3q-4)/4). Then
                eta_v>=beta(p)-gamma(q).
              Moreover, for every rank-q ascending terminal anchor h and every q-edge longest h-path Q ending at v, at least
                beta(p)-eta_v-a(q)
              members of T(v) are double on Q but single on P_v.
              
              For each such switching edge e={x,v,u}, both x,u lie in the anchor precursor V(Q)\h, while exactly one lies in V(P_v)\last(P_v). Distinct switching edges have disjoint non-v pairs. Hence they form a matching between anchor vertices retained by P_v and anchor vertices omitted by P_v.
              
              Since all these switching edges are single ascending terminal edges of rank at most q on P_v,
                beta(p)-eta_v-a(q) <= max(0,4q-2p-3).
              
              In particular, eta_v=o(p) forces q=p-o(p) and produces (5/8-o(1))p anchor-double / host-single switching edges, with a disjoint retained/omitted matching on the anchor precursor.

            • [1000158] Lens-free 43/48 switching stability
                STATEMENT
                Let (H_j) be a sequence of finite linear 3-uniform hypergraphs. For H_j write
                  S_j=sum_v phi(v),  m_j=|E(H_j)|,  n_j^+=|{v:d(v)>0}|.
                Assume
                  S_j/n_j^+ -> infinity
                and
                  m_j >= (43/48)S_j-o(S_j).
                
                Choose the maximum endpoint paths and local deficits eta_v from a57007500001. Then
                  sum_v eta_v=o(S_j).
                Moreover, all but o(S_j) endpoint-potential mass lies on active misaligned vertices v for which the maximum edge rank q(v) of an ascending nonspecial edge terminal at v satisfies q(v)<phi(v).
                
                For each such vertex choose one maximum-rank ascending terminal anchor and a longest anchor path. Let s(v) be the number of anchor-double / maximum-path-single switching edges supplied by the lens-free dense switching theorem f3588b3a3bc7. Then
                  sum_v s(v) >= (5/8-o(1))S_j.
                
                Thus every asymptotic 43/48 near-extremizer carries center-indexed switching mass of order 5S/8, with each local switching family a disjoint matching between retained and omitted vertices of one common anchor precursor.

              • [1000116] Lens-free global one-eighth paid switching mass
                  STATEMENT
                  Let (H_j) satisfy
                    S_j=sum_v phi(v),  S_j/n_j^+ -> infinity,
                    |E(H_j)| >= (43/48)S_j-o(S_j).
                  For every active misaligned vertex v use the lens-free common-anchor switching family from f3588b3a3bc7 and let D_v^cell,Y_v be the corresponding local certificate counts from 614c7d2d181a.
                  
                  Then
                    sum_v (D_v^cell+Y_v) >= (1/8-o(1))S_j.
                  
                  Every D-unit is represented by a doubly occupied switching cell and hence a linear switcher triangle. Every Y-unit is represented by a paid switching cell whose output is in one of the nonflat progress branches of 6205fe95ecf8.
                  
                  Thus the global one-eighth paid progress-or-obstruction mass survives on a lens-free dependency chain.

            • [1000613] Lens-free flat terminal incidences are paid by local defect
                STATEMENT
                For each nonisolated vertex w let eta_w be the local defect from a57007500001. Let C be any set of distinct ordered terminal incidences (h,w) such that h is an ascending nonspecial edge terminal at w and
                  phi(h)=phi(w)=p_w.
                
                Then
                  |C| <= 4 sum_w eta_w + O(n_+).
                
                More precisely, restricting to p_w>=8,
                  |C| <= 4 sum_w eta_w.
                
                Thus in a 43/48 near-extremal sequence, the total number of rank-tight ascending terminal incidences is o(S).

      • [1000733] The one-rank saving improves the global bound for every uniformity
          STATEMENT
          For integers r>=3 and ell>=5, every n-vertex linear r-uniform hypergraph containing no linear path of ell edges satisfies
          |E(H)| <= [((8r^2-10r+1)ell-(16r^2-22r-3))/(8r(r-1))] n.
          This improves the preceding general-r bound by (6r-7)n/(8r(r-1)), without changing its leading coefficient.
          
          For the maximum endpoint paths selected in the proof, let X be total excess contact multiplicity. The stronger estimate subtracts the additional term (r-2)X/[r(r-1)] from the right-hand side.
          In particular the displayed coefficients are (43ell-75)/48 for r=3, (89ell-165)/96 for r=4, and (151ell-287)/160 for r=5.

    • [1000739] At most two ascending terminal edges occupy the odd central rank window
        STATEMENT
        Let q≥3 be an integer, H a finite linear 3-graph, and v a vertex with φ(v)≥2q-3. Then at most two ascending nonspecial edges e containing v have v terminal at e and φ(e)≤q. No comparison with their opposite terminal vertex ranks is required. More precisely the respective upper bounds are 2, 1, and 0 when φ(v)=2q-3, φ(v)=2q-2, and φ(v)≥2q-1. In particular, if φ(v)=5, at most two rank-four ascending edges are terminal at v, even without potential charging.

      • [1001044] Potential-five pattern 4455 has only two rank-four witness geometries
          STATEMENT
          Let phi(v)=5 and suppose four potential-charged ascending nonspecial edges through v have ordered ranks (4,4,5,5). Fix a maximum five-edge path
            P=(g1,g2,g3,g4,e5)
          ending in one rank-five charged edge e5 at v, and write
            a=g2∩g3,
            b=the private vertex of g3,
            c=g3∩g4.
          
          For the two rank-four charged edges, their path-relative witnesses are two distinct vertices of {a,b,c}. The witness pair {a,c} is impossible. Hence, up to ordering, the only possible rank-four witness sets are
            {a,b} or {b,c}.
          
          Moreover b is necessarily an entrance witness in either case; in the {b,c} case both b and c are entrances and phi(b)=phi(c)=3.

        • [1000444] The low-low witness geometry is impossible in the p=5 pattern 4455
            STATEMENT
            In the p=5 charged pattern (4,4,5,5), the {b,c} rank-four witness geometry is impossible. Consequently every surviving 4455 obstruction must have rank-four witness set {a,b}, with a=g2∩g3 and b the private vertex of g3.

        • [1000668] In the 4455 low-low witness geometry the second rank-five edge either enters privately through g4 or has two precursor contacts
            STATEMENT
            Assume the p=5 charged pattern (4,4,5,5) and the {b,c} witness geometry of e6eec0f670ed. Thus
              P=(g1,g2,g3,g4,e5)
            ends at v,
              g3={a,b,c},
            where b,c are the unique entrances of the two rank-four charged edges and phi(b)=phi(c)=3.
            
            Let
              h={x,v,u}
            be the other rank-five charged edge, with unique entrance x and phi(x)=4.
            
            Then h is disjoint from g3. Moreover h meets g2∪g4. If h has exactly one contact with g2∪g3∪g4, then that contact lies in g4, is x, and x is the private vertex of g4.
            
            Equivalently, every other case forces h to have contacts with both g2 and g4.

          • [1000283] The two-contact 4455 low-low branch is a rigid four-cycle plus rank-five triangle
              STATEMENT
              Continue in the {b,c} witness geometry of the p=5 pattern (4,4,5,5), and let h={x,v,u} be the second rank-five charged edge.
              
              Assume h meets both g2 and g4. Then:
              1. h∩g4 is the private vertex of g4;
              2. h∩g2 is the joint g1∩g2.
              
              Consequently
                h,g2,g3,g4
              form a linear 4-cycle, while
                h,g4,e5
              form a linear 3-cycle. Thus the whole two-contact obstruction is a rigid theta consisting of a 4-cycle and a 3-cycle sharing the edge-pair h,g4.

            • [1000253] The two-contact p=5 4455 low-low state is impossible
                STATEMENT
                In the p=5 charged pattern (4,4,5,5), the {b,c} witness geometry cannot occur in the two-contact state of 3d216d397f78. Hence, within the {b,c} geometry, the second rank-five charged edge must be in the unique clean state of 96ce63c6b236: its sole contact with g2∪g3∪g4 is its entrance at the private vertex of g4.

        • [1000968] The low-low witness geometry in the potential-five 4455 pattern is impossible
            STATEMENT
            In the p=5 charged pattern (4,4,5,5), use the notation of e6eec0f670ed:
              P=(g1,g2,g3,g4,e5)
            ends in a rank-five charged nonspecial edge e5 at terminal v, and
              g3={a,b,c}
            with a=g2∩g3, b private in g3, c=g3∩g4.
            
            The rank-four witness set cannot be {b,c}. Therefore the only remaining witness geometry for 4455 is {a,b}.

          • [1000553] The surviving 4455 witness geometry forces the right middle joint to potential at least four
              STATEMENT
              Assume the p=5 charged pattern (4,4,5,5) in its only surviving witness geometry {a,b}, with
                P=(g1,g2,g3,g4,e5),
                a=g2∩g3,
                b private in g3,
                c=g3∩g4.
              Let f_b={b,v,u_b} be the rank-four charged edge whose witness b is necessarily its unique entrance.
              
              Then:
              1. phi(b)=3;
              2. u_b∈V(g1∪g2);
              3. phi(c)>=4.
              
              The lower bound phi(c)>=4 is witnessed both by the endpoint chord through a and v and by an explicit four-edge path through f_b and e5.

            • [1000262] If the left 4455 witness is an entrance, every canonical entrance rail must recross the middle edge
                STATEMENT
                Assume the surviving p=5 4455 witness geometry {a,b} from 7b36d8822911, with
                  g3={a,b,c},
                  phi(b)=3.
                Suppose a is the unique entrance of its rank-four charged edge f_a. Then phi(a)=3.
                
                Let
                  R_a=(h1,h2,h3)
                be any canonical three-edge entrance path ending physically at a such that R_a,f_a is a four-edge path ending in f_a through a and R_a avoids the two terminals of f_a.
                
                Then R_a meets g3 at some vertex other than a. Equivalently, at least one of b,c belongs to V(h1∪h2).

              • [1001059] Every canonical left-entrance rail in 4455 crosses both the middle edge and the far rank-five edge
                  STATEMENT
                  Continue in the surviving 4455 geometry {a,b}, and suppose a is the entrance of its rank-four charged edge
                    f_a={a,v,u_a}.
                  Let
                    e5={d,v,w}
                  be the fixed rank-five charged last edge, with d its unique entrance.
                  
                  For every canonical three-edge entrance path
                    R_a=(h1,h2,h3)
                  ending at a and avoiding v,u_a:
                  1. R_a meets g3={a,b,c} at a second vertex, hence contains b or c in h1∪h2;
                  2. R_a meets e5, hence contains d or w.
                  
                  Thus every canonical a-ending entrance rail simultaneously crosses the middle edge away from a and the far rank-five edge away from v.

                • [1000243] Every canonical left-entrance rail in the surviving 4455 branch also crosses the opposite rank-four edge
                    STATEMENT
                    Continue in the surviving p=5 pattern 4455, entrance-a branch. Thus
                      g_3={a,b,c},
                      f_a={a,v,u_a},
                      f_b={b,v,u_b},
                    where f_a,f_b are rank-four charged ascending nonspecial edges with unique entrances a,b and
                      phi(a)=phi(b)=3.
                    
                    Let
                      R_a=(h_1,h_2,h_3)
                    be any canonical three-edge entrance path ending at a such that R_a,f_a is a four-edge path ending in f_a through a and R_a avoids v,u_a.
                    
                    Then R_a meets f_b. Since R_a avoids v, it contains b or u_b.
                    
                    Together with 3925baec6cf9 and ebd9e72015cd, every canonical R_a therefore simultaneously:
                    - contains b or c, as a second contact with g_3;
                    - contains d or w, as a contact with e_5;
                    - contains b or u_b, as a contact with f_b.
                    
                    In particular, if R_a avoids b (so its extra g_3-contact is c), then R_a necessarily contains u_b.

                • [1000809] Canonical entrance-a rails in 4455 have only two far-middle overlap normal forms
                    STATEMENT
                    In the entrance-a subcase of the surviving p=5 pattern 4455, let
                      R_a=(h1,h2,h3)
                    be a canonical three-edge a-ending entrance rail for f_a, and let e5={d,v,w}.
                    
                    Then exactly the following possibilities remain relative to e5:
                    
                    (I) e5 has a unique contact with R_a, and it lies in h3;
                    
                    (II) e5 meets R_a twice, once in h1 and once in h2. In this case the mandatory extra contact of g3={a,b,c} with R_a is forced to the first rail joint
                      h1∩h2.
                    In particular h1∩h2 is b or c.
                    
                    Thus all other single/double far-contact placements are impossible.

            • [1001182] Terminal-left 4455 rigidity collapses the no-c rank-five branch
                STATEMENT
                Assume the surviving p=5 terminal-left 4455 geometry with
                P=(g1,g2,g3,g4,e5),
                a=g2∩g3, b the private vertex of g3, c=g3∩g4,
                and suppose the rank-four charged edge at a is
                f_a={x,v,a}
                with a terminal and x its unique entrance. Then phi(a),phi(c)>=5, phi(x)=3, and x∉V(P).
                
                Let f_b be the charged edge with entrance b, and let h be the second rank-five charged edge through v. Then h contains neither a nor b, so h∩g3 is either empty or {c}. If c∉h, then h is disjoint from g2∪g3 and meets g4 at its private vertex z. In fact this no-c branch is uniquely clean:
                h={z,v,u},
                where z is the unique entrance of h and u∉V(P); hence h meets P only at z and v.

              • [1000791] The clean terminal-left 4455 state forces every low entrance rail to hit three separated edges
                  STATEMENT
                  Continue in the clean no-c terminal-a state of 14c89ddd9ef1:
                    f_a={x,v,a}
                  is rank four with unique entrance x, phi(x)=3, and x∉V(P);
                    h={z,v,u}
                  is the second rank-five edge with entrance z=private(g4) and u∉V(P);
                  and e5 is the fixed rank-five edge.
                  
                  Let
                    Q=(q1,q2,q3)
                  be any canonical three-edge entrance path ending physically at x and avoiding the terminals v,a, so Q,f_a is a four-edge path ending in f_a through x.
                  
                  Then Q meets each of the three edges
                    g3, e5, h.
                  Because Q avoids a and v, these contacts lie respectively in:
                    {b,c}, {d,w}, {z,u}.

                • [1000375] Clean terminal-left 4455 entrance rails are fourfold transversals
                    STATEMENT
                    Continue in the clean terminal-a state of b0de0851e2b0. Thus
                      f_a={x,v,a}
                    is rank four with unique entrance x and x∉V(P),
                      f_b={b,v,u_b}
                    is the other rank-four charged edge with unique entrance b,
                      h={z,v,u}
                    is the second rank-five edge in the clean state,
                    and e5 is the fixed rank-five edge.
                    
                    Let
                      Q=(q1,q2,q3)
                    be any canonical three-edge entrance path ending physically at x and avoiding the terminals v,a, so Q,f_a is a four-edge path ending in f_a through x.
                    
                    Then Q meets each of
                      g3, e5, h, f_b.
                    The contacts lie respectively in
                      {b,c}, {d,w}, {z,u}, {b,u_b}.
                    
                    In particular, if Q avoids b, then it contains four distinct forced vertices
                      c, u_b, one of {d,w}, and one of {z,u}.

            • [1001205] The entrance-a 4455 branch forces a saturated three-edge rail under a unique far contact
                STATEMENT
                In the surviving p=5 pattern (4,4,5,5), if the witness a is the entrance of its rank-four edge f_a, every canonical three-edge a-ending entrance rail R_a=(h_1,h_2,h_3) must meet g_3 again besides a. If the fixed rank-five edge e_5 meets R_a exactly once, that contact is the private vertex of h_3, and g_3 meets both h_1 and h_2 as well as h_3. Thus g_3 intersects every edge of R_a.

      • [1001211] Potential-five 4555 reduces to a late/joint/crossed rail normal form
          STATEMENT
          At potential five, four charged ascending terminal edges have ranks only 4 or 5 and at most two can have rank four. In the 4555 pattern, fixing the unique rank-four edge and a canonical three-edge entrance rail, each of the three rank-five competitors is either late on the final rail edge or early on both first rail edges. At most one competitor is late and at most one early competitor can use only the common joint, so at least one rank-five competitor is crossed across the first two rail edges.

        • [1000507] Crossed p=5 rank-five competitors force a reciprocal rank-four tail blocker
            STATEMENT
            In the p=5 pattern 4555, use the setup of 5ef77fe98dff. Let
              f={x,v,u}
            be the unique rank-four charged edge, with unique entrance x and phi(x)=3.
            
            Let
              h={y,v,z}
            be any crossed rank-five charged competitor, where y is the unique entrance of h and z its opposite terminal. Let
              Q=(q1,q2,q3,q4)
            be any canonical four-edge entrance path with last vertex y and avoiding the two terminals v,z, so Q,h is a rank-five path ending in h through y.
            
            Then
              V(q3∪q4)∩{x,u} != empty.
            In particular every canonical entrance rail for h has a terminal-tail contact with the rank-four edge f in one of its last two precursor edges.

        • [1000821] Potential-five pattern 4555 reduces to exactly two crossed edges and one joint edge
            STATEMENT
            In the p=5 charged pattern (4,5,5,5), retain the canonical rank-four entrance rail
              R=(r1,r2,r3)
            from 5ef77fe98dff, with
              f={x,v,u},
              phi(x)=3,
            and s=r1∩r2.
            
            Then none of the three rank-five charged competitors can be late. Consequently all three are early, exactly two are crossed, and exactly one is joint type.
            
            More precisely:
            - the joint-type edge contains v and s;
            - the two crossed edges are
                h_i={v,a_i,b_i}, i=1,2,
              where {a_1,a_2}=r1\{s} and {b_1,b_2}=r2\{s}.
            Thus the two crossed edges saturate all four non-joint vertices of r1∪r2.

          • [1001069] The exact 4555 normal form is a crossed two-pole incidence rectangle
              STATEMENT
              In the p=5 charged pattern 4555, assume the exact normal form of b8d0dfa0af07. Let
                R=(r_1,r_2,r_3)
              be the canonical rank-four entrance rail, with
                s=r_1∩r_2,
              and let the two crossed rank-five edges be
                h_i={v,a_i,b_i}, i=1,2,
              where
                {a_1,a_2}=r_1\{s},
                {b_1,b_2}=r_2\{s}.
              Let j be the unique joint-type rank-five competitor, so {v,s}⊂j.
              
              Then:
              1. h_1,h_2 induce a perfect matching between r_1\{s} and r_2\{s};
              2. j meets both rail edges r_1,r_2 at the common pole s;
              3. j meets both crossed edges h_1,h_2 at the common pole v.
              
              Thus the five-edge incidence pattern on
                {r_1,r_2,h_1,h_2,j}
              is a rigid crossed rectangle with poles s and v. It is not a linear 4-cycle, because the nonconsecutive rail edges r_1,r_2 already meet at s.

            • [1000865] The joint edge in the exact 4555 rectangle is either rail-clean or hits only the private vertex of the third rail edge
                STATEMENT
                In the exact p=5 pattern 4555 of edc545e3d1e7, let
                  f={x,v,u}
                be the unique rank-four charged edge with canonical entrance rail
                  R=(r_1,r_2,r_3),
                let
                  s=r_1∩r_2,
                  q=r_2∩r_3,
                and let
                  j={v,s,t}
                be the unique joint-type rank-five charged competitor.
                
                Then
                  t∉{x,u,q}.
                Consequently either j is disjoint from r_3, or t is the private vertex of r_3 (the unique vertex of r_3\{x,q}).

    • [1000790] Minimum degree gives an additive gap above the seven-sixths potential floor
        STATEMENT
        Let H be a finite linear 3-graph on n vertices with m edges and minimum degree delta>=4. Then
          sum_v phi(v)
          >= m + (7/6)n
             + [2ceil((delta+1)/2)-5]/6.
        
        Consequently, if H is P_ell-free, then
          m
          <= (ell-13/6)n
             - [2ceil((delta+1)/2)-5]/6.

    • [1000934] Type-A vertices source only ascending nonspecial edges and have an exact degree decomposition
        STATEMENT
        Let v have p=phi(v)>=3 and Type-A local slack
          a(v)=2, b(v)=0.
        Let c(v) be the number of ascending nonspecial edges whose unique entrance is v. Then every nonspecial edge whose unique entrance is v is ascending, and
          d_H(v)=2p-1+c(v).
        
        Equivalently, the incident edges at v split exactly into:
        - 2p-1 snake-incoming edges (four special and 2p-5 nonspecial terminal edges);
        - c(v) ascending nonspecial source edges.
        There are no additional nonascending nonspecial source edges.

    • [1001008] A consistently oriented shared block has descending rank at every ascending edge
        STATEMENT
        Let
          h_1,...,h_t
        be a consistently oriented common block as in e552a55fe162. For 1<=s<t, put
          y_s=h_s intersect h_{s+1}.
        Assume y_s is the unique entrance of h_s and is terminal at h_{s+1}. Write
          r_s=phi(h_s).
        
        Then:
        
        (1) if h_s is ascending, then
          r_{s+1} <= r_s-1;
        
        (2) if r_1,...,r_t all lie in an integer interval of width D, and B is the number of indices s<t for which h_s is nonascending, then
          t-1 <= (D+1)B + D.
        
        Equivalently,
          B >= (t-1-D)/(D+1).
        
        Thus a long consistently oriented common block confined to a narrow edge-rank band contains many nonspecial nonascending edges.

  • [1001189] Critical-core and deletion toolkit
      STATEMENT
      Reusable lemmas about threshold-degree deletion, universal witness cores, and path-forest structure in minimal obstructions.

    • [1000228] Deleting threshold-degree vertices leaves a universal path forest
        STATEMENT
        In the setting of 7de985881169, the induced subhypergraph H-D has edge set C and is a subhypergraph of every nonspecial witness path. Consequently H-D is a linear path forest: every nontrivial component is a subpath of a linear path, every vertex has degree at most two in H-D, and if c is the number of nonempty components then |E(H-D)|=(|V(E(H-D))|-c)/2<=|V(H)\D|/2. In particular every vertex v outside D has at least d_H(v)-2>=k-1 incident edges meeting D.

    • [1000276] Minimal equality obstructions are connected and top cycles have a two-contact first ear
        STATEMENT
        Let ell>=4, d=floor(2ell/3), and let H be a vertex-minimal counterexample to the exact-density equality assertion E_ell: |E(H)|=d|V(H)|, delta(H)>=d+1, and H contains a nonspecial edge. Then H is connected.
        
        Moreover, in the minimum-potential equality branch, if C is one of the canonical linear ell-cycles supplied by 56fe77d0057c, there exists an edge f not in C meeting both V(C) and V(H)\V(C). Every such crossing edge meets C in exactly two vertices; in particular the first connection from C to the outside reservoir is a two-contact chord with one outside vertex.

    • [1000389] Minimum-potential equality paths have two canonical special cycle closures
        STATEMENT
        Assume the minimum-potential equality configuration average(phi)=m/n+1, so the conclusions of f9df80bd57f2 hold. Let v have p=phi(v), and let P=(g_1,...,g_p) be any maximum p-edge path ending at v, with last edge h=g_p. Then h is special, and the other two special edges f_1,f_2 through v each close P to a linear cycle of length p+1:
        (g_1,g_2,...,g_p,f_i).
        Consequently, if p=ell-1 in a P_ell-free equality obstruction, every maximum p-edge endpoint path lies in at least two distinct linear ell-cycles sharing the same p-edge path.

    • [1000757] Cheap witness-avoiding singleton deletion forces an exact threshold bridge
        STATEMENT
        For a witness-avoiding set S, the density deficit updates exactly by r(H-S)=r(H)+|N(S)|-d|S|. In a vertex-minimal equality obstruction, a cheap singleton deletion w that preserves density at least d and a nonspecial witness need not contradict minimality; instead H-w has a degree-at-most-d vertex u. Linearity then forces d_H(u)=d+1, d_{H-w}(u)=d, and a unique hyperedge through {u,w}.

    • [1001135] At density-plus-one equality every maximum endpoint path has a special last edge
        STATEMENT
        Assume equality in c77c818cf1e9. Then for every vertex v with p=phi(v), every maximum p-edge path ending at v has a special last edge.
        
        Moreover, relative to every such maximum path P=(g_1,...,g_p) with special last edge h=g_p:
        - all 2p-4 nonspecial terminal edges through v are single-blockers on P and their blocker witnesses biject exactly onto
          (V(g_2 union ... union g_{p-1}))\V(h);
        - the two special edges through v other than h meet P outside v exactly at the two free vertices of g_1, one each.

    • [1001155] Exact density forces at least 4d minus one above-threshold vertices
        STATEMENT
        If a linear 3-graph H satisfies |E(H)|=d|V(H)| and minimum degree at least d+1, then at least 4d-1 vertices have degree at least d+2. Consequently every q-edge path omits at least 4d-2q-2 such vertices; for q<=ell-1 this recovers the lower bound 4d-2ell from a05f009dfcef.

  • [1000565] Lens-free local one-eighth paid clean 0-1-1 extraction
      STATEMENT
      Let (H_j) satisfy
        S_j=sum_v phi(v),  S_j/n_j^+ -> infinity,
        |E(H_j)| >= (43/48)S_j-o(S_j),
      and choose maximum endpoint paths as in a57007500001.
      
      Then for each vertex v one may choose a family G_v of ascending nonspecial edges terminal at v such that every f in G_v:
      (1) belongs to the common-anchor / maximum-path switching family at v supplied by f3588b3a3bc7;
      (2) carries at v one selected D+Y certificate from the lens-free cell payment theorem;
      (3) is source-clean at its unique entrance;
      (4) is terminal-single on the chosen maximum endpoint paths at both terminals.
      
      Writing p_v=phi(v),
        sum_v (p_v/8-|G_v|)_+ = o(S_j).
      
      Consequently, for every fixed epsilon>0, the total endpoint-potential mass of vertices satisfying
        |G_v| < (1/8-epsilon)p_v
      is o(S_j).
      
      Thus the local one-eighth paid-certified clean 0-1-1 degree survives without any endpoint-lens premise, and every retained edge also carries the genuine common-anchor switching structure.

    • [1001018] Lens-free strict two-terminal-gap paid family with certificate terminal retained
        STATEMENT
        Let (H_j) satisfy
          S_j=sum_v phi(v),  S_j/n_j^+ -> infinity,
          |E(H_j)| >= (43/48)S_j-o(S_j).
        Choose the lens-free local families G_v from 7ddb7afd3083.
        
        Then all but o(S_j) of the center-edge incidences (v,f), f in G_v, satisfy strict edge-rank gap at both terminals: if u is the other terminal and q=phi(f), then
          q<phi(v) and q<phi(u).
        
        Consequently there is a set Epp of distinct ascending nonspecial edges with
          |Epp| >= (1/16-o(1))S_j
        such that every e={x,u,v} in Epp:
        (1) is source-clean on the chosen maximum path at its unique entrance;
        (2) is terminal-single on the chosen maximum endpoint paths at both terminals;
        (3) satisfies q=phi(e)<min{phi(u),phi(v)};
        (4) carries a selected D+Y common-anchor switching certificate at at least one of its terminals.
        
        The certificate terminal in (4) is retained as part of the data and is not asserted to be a minimum-rank terminal of e.

      • [1000160] Sublinear congestion in the original certificate-centered families alone closes 43/48
          STATEMENT
          Assume there is a function g(p)=o(p) with the following property. For every relevant choice of maximum endpoint paths and every vertex v of rank p, any family F_v of distinct ascending nonspecial edges terminal at v in which every e={x,v,u}:
          (1) is source-clean at its unique entrance x;
          (2) is terminal-single on the chosen maximum endpoint paths at both terminals;
          (3) satisfies phi(e)<min{phi(v),phi(u)};
          (4) carries at v a selected common-anchor D+Y switching certificate,
          has |F_v|<=g(p).
          
          Then no 43/48 near-extremal sequence with S/n_+ tending to infinity exists.
          
          Thus it is enough to prove sublinear congestion directly in the original certificate-centered local families. No quotient to distinct underlying edges, minimum-rank terminal assignment, certificate transfer, or same-terminal/uphill split is needed for this reduction.

      • [1000503] Lens-free selected strict-gap mass survives as clean fundamental-cycle chords
          STATEMENT
          Let (H_j) satisfy
            S_j=sum_v phi(v),  S_j/n_j^+ -> infinity,
            |E(H_j)| >= (43/48)S_j-o(S_j),
          and let G_v be the lens-free selected common-anchor families from 7ddb7afd3083.
          
          Form the terminal-pair graph J_j consisting of all ascending nonspecial hyperedges that are source-clean on the chosen maximum path at their unique entrance and terminal-single on the chosen maximum endpoint paths at both terminals. Weight each graph edge by the rank of its parent hyperedge, and in every component choose a spanning tree of maximum total rank; let F_j be the resulting forest.
          
          Then there are subfamilies H_v subseteq G_v such that
            sum_v (phi(v)/8-|H_v|)_+ = o(S_j),
          and every center-edge incidence (v,e), e={x,v,u} in H_v, satisfies simultaneously:
          
          (1) e retains its selected D+Y common-anchor certificate at v;
          (2) e is source-clean and terminal-single at both terminals;
          (3) phi(e)<min{phi(v),phi(u)};
          (4) vu is not a forest edge, so its fundamental cycle C_e lies entirely in J_j;
          (5) e is minimum-rank on C_e; in particular its two cycle-neighbor hyperedges have rank at least phi(e), and e has the canonical additional blocker contact on maximum terminal witnesses for those two neighbors.
          
          Consequently
            sum_v |H_v| >= S_j/8-o(S_j),
          and the union of the H_v contains at least
            (1/16-o(1))S_j
          distinct underlying hyperedges.
          
          Thus the full local one-eighth lens-free selected strict-gap mass can be retained while adding a canonical clean-U11 fundamental-cycle certificate.

        • [1000936] Lens-free selected cycle chords yield theta, outer intersection, or two late gates
            STATEMENT
            Retain the lens-free family H_v from 6f2f8b7f1053. Fix a center-edge incidence
              (v,e),  e={x,v,u} in H_v,
            and write r=phi(e). Let f,g be the two hyperedges whose terminal-pair edges are adjacent to e on its clean-U11 fundamental cycle C_e. Then
              phi(f),phi(g)>=r.
            
            Choose canonical maximum source rails
              R_e,R_f,R_g
            ending at the unique entrances of e,f,g, of lengths
              r-1, phi(f)-1, phi(g)-1.
            
            At least one of the following holds:
            
            (1) |V(R_e) intersect V(R_f)|>=2;
            (2) |V(R_e) intersect V(R_g)|>=2;
            (3) V(R_f) intersect V(R_g) is nonempty;
            (4) both adjacent intersections are unique aligned joints, the outer rails R_f,R_g are disjoint, and their gate indices t_f,t_g on R_e satisfy
                min{t_f,t_g} >= ceil((r-1)/2).
            
            Moreover e still carries, at the selected center v, its common-anchor switching certificate from 6f2f8b7f1053. Hence in residual case (4) the same source rail R_e simultaneously has two late fundamental-cycle gates and belongs to a whole-chord selected state whose certificate anchor precursor contains both x and u.

          • [1000434] The selected-terminal cycle-neighbor rail cannot pierce a certificate-anchor lens
              STATEMENT
              Retain residual case (4) of d0a41dede20a for a selected strict-gap chord
                e={x,v,u}
              with source rail R_e and selected certificate anchor precursor A at terminal v. Let f be the fundamental-cycle neighbor of e that shares terminal v, and let R_f be a canonical source rail of f.
              
              Then R_f intersects both R_e and A.
              
              Consequently at least one of the following holds:
              
              (i) |V(R_f) intersect V(R_e)|>=2;
              (ii) |V(R_f) intersect V(A)|>=2;
              (iii) both intersections are unique aligned joints, say
                   V(R_f) intersect V(R_e)={s},
                   V(R_f) intersect V(A)={t},
              and no clean lens between R_e and A has s in the interior of its R_e-side and t in the interior of its A-side.
              
              In particular, after excluding multiple-overlap outcomes, the cycle-neighbor rail cannot pierce any clean certificate-anchor/source-rail lens: its two unique gates must lie outside, on the boundary of, or on the same side of every such lens.

            • [1001158] A long entrance-side replacement region pushes cycle-neighbor gates outside the common-path interval
                STATEMENT
                Retain residual case (4) of d0a41dede20a for a selected strict-gap edge
                  e={x,v,u}
                of edge rank r. Let R_e be its canonical maximum source path, of length r-1, and let A be the selected common-path precursor at terminal v.
                
                Assume e lies in alternative (B) of bbaf9e0b90fc: there is a common vertex z of R_e and A such that the two segments
                  R_e[z,x] and A[z,x]
                are internally vertex-disjoint and have the same length ell.
                
                Let f be either fundamental-cycle neighbor of e, and let R_f be a canonical maximum source path for f. In residual case (4),
                  V(R_f) intersect V(R_e)={s}
                is a unique aligned joint whose index t on R_e satisfies
                  t>=ceil((r-1)/2).
                
                If
                  ell>floor((r-1)/2),
                then at least one of the following holds:
                (1) |V(R_f) intersect V(A)|>=2;
                (2) V(R_f) intersect V(A)={w} and w does not lie in the open A-segment A(z,x).
                
                Consequently, if both fundamental-cycle neighbors meet A uniquely, then for a long entrance-side replacement region both of their unique A-gates lie outside A(z,x).

          • [1001112] Unique source-path intersections label fundamental-cycle neighbors by reciprocal terminals
              STATEMENT
              Let
                e={x,v,u}
              be an ascending nonspecial edge of edge rank r, with unique entrance x and terminals v,u. Let f and g be ascending nonspecial edges such that f is terminal at v, g is terminal at u, and
                phi(f),phi(g)>=r.
              Choose maximum endpoint paths R_e,R_f,R_g ending at the unique entrances of e,f,g respectively, each avoiding the two terminals of its last edge.
              
              Assume
                V(R_e) intersect V(R_f)={s_f},
                V(R_e) intersect V(R_g)={s_g}.
              Then:
              (1) u belongs to V(R_f);
              (2) v belongs to V(R_g).
              
              More precisely, R_f must meet e at u rather than x, and R_g must meet e at v rather than x. Consequently, when f and g are the two fundamental-cycle neighbors of a minimum-edge-rank nonforest chord e, the hard unique-intersection residual has exact reciprocal-terminal labels on the two neighboring source paths.

            • [1000376] A reciprocal fundamental-cycle terminal lies within the aligned-gate distance budget
                STATEMENT
                Retain the hard unique-intersection residual of d0a41dede20a for
                  e={x,v,u}
                of edge rank r, and let f be the fundamental-cycle neighbor of e sharing terminal v. Let R_e,R_f be maximum endpoint paths ending at the unique entrances of e,f. Assume
                  V(R_e) intersect V(R_f)={s},
                and let t be the aligned joint index of s on both paths. Thus R_e has length r-1 and, by f4f2089110b2, u belongs to R_f while x does not.
                
                Let d_f(s,u) denote the number of R_f-edges in the path segment between s and u. Then
                  d_f(s,u) <= t.
                
                Equivalently, the reciprocal terminal u lies within t path edges of the unique aligned gate s on the neighboring maximum source path. The symmetric statement holds for the other fundamental-cycle neighbor at terminal u.

            • [1000910] A unique selected-common-path intersection with the same-terminal cycle neighbor is exactly the reciprocal terminal
                STATEMENT
                Retain the hard unique-intersection residual of d0a41dede20a for
                  e={x,v,u},
                and let f be the fundamental-cycle neighbor of e that shares terminal v. Let R_e and R_f be canonical maximum source paths for e and f. Let A be the selected common-path precursor at terminal v, so both x and u lie on A.
                
                Assume
                  V(R_e) intersect V(R_f)={s}.
                Then u belongs to V(R_f) intersect V(A).
                
                Consequently, if
                  |V(R_f) intersect V(A)|=1,
                then
                  V(R_f) intersect V(A)={u}.
                Moreover u is an internal joint on both maximum endpoint paths R_f and A at the same path index.
                
                Thus, in the unique-intersection branch, the second gate of R_f against the selected common path is canonically labeled by the reciprocal terminal u; it is not an unspecified return vertex.

      • [1000729] Certificate-at-either-terminal sublinear congestion closes 43/48
          STATEMENT
          Assume there is a function g(p)=o(p) with the following property.
          
          For every relevant choice of maximum endpoint paths, let E be any family of distinct ascending nonspecial edges e={x,u,v} such that:
          (1) e is source-clean at its unique entrance x;
          (2) e is terminal-single on the chosen maximum endpoint paths at both terminals u,v;
          (3) phi(e)<min{phi(u),phi(v)};
          (4) e carries a selected common-anchor D+Y switching certificate at at least one of its two terminals, with that certificate terminal retained as part of the data.
          
          Assign every e in E once to a terminal of minimum vertex rank. Suppose that, at every vertex w of rank p, at most g(p) assigned edges occur.
          
          Then no 43/48 near-extremal sequence with S/n_+ tending to infinity exists.
          
          In particular, any o(p) local bound for this certificate-at-either-terminal class is sufficient to force a strict asymptotic improvement below 43/48.

        • [1000688] Selected strict-gap edges split into same-terminal and uphill certificate classes
            STATEMENT
            Retain the strict-gap family Epp from e2dcd798f528. For each edge e with terminal vertices u,v, choose one selected common-anchor D+Y certificate terminal c(e), and assign e to a terminal m(e) of minimum vertex rank.
            
            Then every edge belongs to exactly one of the following two classes after choosing c(e) optimally:
            (S) same-terminal certified: some selected certificate terminal has vertex rank equal to min{phi(u),phi(v)}, so e may be assigned to a minimum-rank terminal at which it carries its selected certificate;
            (H) uphill certified: every selected certificate terminal has vertex rank strictly larger than min{phi(u),phi(v)}.
            
            In class (H), if m(e)=v and c(e)=u, then
              phi(e)<phi(v)<phi(u).
            Thus the certificate orientation is a strict rise in terminal potential away from the counting terminal.
            
            Consequently, for every near-43/48 member, at least half of the Omega(S) distinct strict-gap edges lie in one of the two classes. To contradict 43/48 it is enough to prove an o(p) assigned local bound separately for class (S) and class (H).

          • [1001126] Higher-terminal certificate anchors reintersect the lower-terminal maximum path
              STATEMENT
              Let e={x,v,u} be an ascending nonspecial edge with unique entrance x and terminals v,u. Suppose a selected common-anchor certificate at u supplies a distinct ascending nonspecial anchor h={y,u,w} and a canonical maximum source precursor A ending at y such that A,h is a longest h-path ending at u, A avoids u, and x,v belong to V(A).
              
              Let P_v be any maximum endpoint path ending at v, and let g be its last edge. Then
                |V(A) intersect V(P_v)| >= 2,
              and at least one of the following holds:
              (C) A union P_v contains a linear cycle;
              (E) g belongs to E(A).
              
              If moreover phi(e)<phi(v) and e is terminal-single on P_v, then exactly one of x,u occurs on the precursor of P_v. In the X-type case x lies on P_v, so A and P_v have the explicit two common vertices v,x. In the U-type case u lies on P_v and x does not; since A avoids u, every common vertex of A and P_v besides v is outside V(e).
              
              In particular, every uphill-certified edge assigned to its lower-rank terminal carries a repeated-intersection certificate between the fixed lower-terminal maximum path and the higher-terminal certificate-anchor precursor, sharpened to a linear cycle or containment of the fixed lower-terminal last edge.

          • [1000456] An uphill higher-terminal certificate forces a repeated intersection with the lower terminal path
              STATEMENT
              Let e={x,v,u} be an ascending nonspecial edge with unique entrance x, with v and u terminal at e. Suppose e carries at u a selected common-anchor certificate whose canonical anchor precursor A contains x and v. Let P_v be a maximum endpoint path ending at v, and assume e is terminal-single on P_v. Then |V(P_v) intersect V(A)|>=2. More precisely, if x lies on P_v then {x,v} is contained in V(P_v) intersect V(A); if u lies on P_v (so x does not), then A and P_v have a second common vertex outside e in addition to v.

  • [1000700] Cheap switching states require order at least 127 over 56 times the host potential
      STATEMENT
      Let H be a finite linear 3-graph on n vertices and let v be an active misaligned vertex with p=phi(v). Suppose v is low-defect and its switching-family source-potential mass is within o(p^2) of the generic 185/512 p^2 floor, in the asymptotic regime p->infinity.
      
      Then
        n >= (127/56-o(1))p.
      
      More explicitly, if U_v is the terminal-retained part of a switching family and k=|U_v|, then
        n >= 2p+1+k.
      Hence any estimate k>=(15/56-epsilon)p gives
        n >= (127/56-epsilon)p+1.
      
      Therefore for every fixed epsilon>0, a sequence with
        n <= (127/56-epsilon)p
      cannot realize the locally cheap post-43/48 switching state at a p-center; such a center must instead pay a fixed positive quadratic gain in switching-source potential over the generic 185/512 floor.
