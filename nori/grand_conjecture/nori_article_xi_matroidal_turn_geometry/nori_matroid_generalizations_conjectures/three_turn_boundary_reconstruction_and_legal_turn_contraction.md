# Three-turn boundary reconstruction and legal-turn contraction

Let \(n\ge5\). Write \(S_n\) for the ordered-pair double cover of \(L(K_n)\), with vertices \((u,v)\) and undirected edges labelled by triples \(t=(a,b,c)\), corresponding to \((a,b)-(b,c)\), where the three symbols are distinct. Its deck involution reverses ordered pairs and triple labels. Put
\[
H_{\rm full}=L(S_n)/\langle\rho\rangle\cong L^2(K_n).
\]
The covering \(L(S_n)\to H_{\rm full}\) defines the pointed binary dual \(D_{\rm full}\) of the incidence-plus-monodromy matrix of Article XI.

Declare a turn between triple states **legal** if it has a lift of the form
\[
(a,b,c)\;--\;(b,c,d),\qquad
a,b,c,d\text{ pairwise distinct},
\tag{1}
\]
or the reverse traversal. Let \(F\subseteq E(H_{\rm full})\) be its set of legal turns and \(H_{\rm leg}=(V(H_{\rm full}),F)\). This is the quotient of the alternating-port ordered-triple overlap graph from Article XI. Let \(T=E(H_{\rm full})\setminus F\).

**Theorem 1 (three-turn reconstruction).** Every omitted turn \(e\in T\) has a lifted representative joining two triple states \(t,t'\) that can be joined by a legal-turn path of length at most three in the ordered-triple graph. The projected path \(P_e\subseteq F\) can be chosen such that \(P_e\cup\{e\}\) is a simple cycle of \(H_{\rm full}\) with trivial covering monodromy. In particular,
\[
\boxed{\forall X\in Z(D_{\rm full}),\quad
\mathbf1_X(e)=\sum_{f\in P_e}\mathbf1_X(f)\pmod2,\qquad |P_e|\le3.}
\tag{2}
\]
Equivalently, every \(e\in T\) belongs to a cocircuit \(Y_e\) of \(D_{\rm full}\) avoiding the port and satisfying
\[
\boxed{Y_e\cap T=\{e\},\qquad |Y_e|\le4.}\tag{3}
\]
The bound three in (2) is attained by the forbidden return turns.

*Proof.* Fix the ordered-pair state \((u,v)\) at which the lifted omitted turn meets. Its incident triple states are of two types,
\[
I_w=(w,u,v),\qquad O_z=(u,v,z),
\quad w,z\notin\{u,v\}.
\]
The legal turns at this state are \(I_w--O_z\) with \(w\ne z\). Every omitted turn falls into one of the following cases.

If \(e=I_wI_{w'}\), with \(w\ne w'\), choose \(z\notin\{u,v,w,w'\}\). Then
\(I_w--O_z--I_{w'}\) is a legal two-turn path.

If \(e=O_zO_{z'}\), choose \(w\notin\{u,v,z,z'\}\). Then
\(O_z--I_w--O_{z'}\) is a legal two-turn path.

If \(e=I_wO_w\), choose distinct \(x,y\notin\{u,v,w\}\). Then
\[
I_w--O_x--I_y--O_w
\tag{4}
\]
is a legal three-turn path. These choices exist for \(n\ge5\). In each case the displayed triple states belong to different reversal orbits, so their projections together with \(e\) form a simple cycle. The lifted path followed by the reversed omitted turn closes on the original sheet, hence that cycle has monodromy zero. Its edge set is therefore a non-port circuit of the incidence-plus-monodromy matroid, equivalently a non-port cocircuit of \(D_{\rm full}\). Binary cycle–cocircuit orthogonality yields (2) and (3). \(\square\)

**Theorem 2 (faithful minor and cycle-space isomorphism).** The pointed legal-turn lift matroid \(D_{\rm leg}\) satisfies
\[
\boxed{D_{\rm leg}=D_{\rm full}/T.}\tag{5}
\]
Moreover, restriction to the surviving elements is a linear isomorphism
\[
\boxed{\pi:Z(D_{\rm full})\xrightarrow{\sim}Z(D_{\rm leg}),
\quad X\longmapsto X\cap(F\cup\{p\}).}\tag{6}
\]
In particular, port-containing cycles are in bijection, and the full boundary-tournament coloring modulo global complementation is recoverable from legal-turn data alone. This contraction does **not** preserve port cogirth: in the established range \(n\ge6\), the full-turn pointed matroid has \(g_p=4\), whereas the alternating-port legal-turn pointed matroid has \(g_p=7\).

*Proof.* Restricting the incidence-plus-monodromy matrix for \(H_{\rm full}\) to columns \(F\cup\{p\}\) gives the corresponding matrix for \(H_{\rm leg}\). Matroid duality exchanges this restriction with contraction, proving (5). Projection of binary cycle spaces under contraction is surjective. It is injective by (2): if a cycle restricts to zero on \(F\cup\{p\}\), (2) forces every omitted coordinate to vanish. Thus (6) holds. The differing port cogirth values are the independently proved four-element star cocircuits in the full double-line-graph model and seven-element reversal cocircuits in the alternating-port triple-state model. \(\square\)

For clarity, the vertex sets of \(H_{\rm full}\) and \(H_{\rm leg}\) both have size \(n\binom{n-1}{2}\), while
\[
|E(H_{\rm full})|=\binom n2\binom{2(n-2)}2,\quad
|F|=\frac{n(n-1)(n-2)(n-3)}2,\quad
|T|=\frac{n(n-1)(n-2)^2}2.
\tag{7}
\]
All \(|T|\) omitted coordinates are recoverable using at most three coordinates each, as in Theorem 1.

**Corollary 3 (common bounded-reconstruction axiom).** More generally, let a two-sheeted turn cover be given, and distinguish a spanning legal-turn subgraph \(H'\subseteq H\). Suppose for each excluded turn \(e\) there is a cycle \(C_e\subseteq H\) of trivial covering monodromy, containing \(e\), with \(C_e\setminus\{e\}\subseteq E(H')\) and \(|C_e|\le L+1\). Then contraction onto the legal-turn pointed matroid induces a linear isomorphism of the binary cycle spaces, with every omitted coordinate recoverable by a parity expression of length at most \(L\). The cube has no omitted turns (\(L=0\)); ordinary boundary 3-tournaments satisfy this axiom with \(L=3\).

*Proof.* Each \(C_e\) is a non-port cocircuit of the pointed dual. Orthogonality expresses the deleted coordinate as the parity sum of the remaining coordinates of \(C_e\). These identities establish injectivity of restriction; surjectivity follows from contraction. \(\square\)

The theorem supplies an intrinsic matroidal compatibility requirement missing from arbitrary signed-cover proposals: **legal-turn contraction with bounded non-port cocircuit certificates**. It preserves all color information, but does not by itself prove any long monochromatic resource-simple path. In particular, small port cogirth of the full-turn matroid cannot substitute for the distinguished long port cocircuits of the legal-turn model.

**Sharpness.** For an omitted return turn joining triples (w,u,v) and (u,v,w), the first state has legal neighbors (u,v,x) and (x,w,u), while the second has legal neighbors (v,w,y) and (y,u,v), with x,y outside {u,v,w}. These neighbor sets are disjoint, and the endpoints are not legally adjacent. Their legal-turn distance is three, so the reconstruction bound cannot be reduced to two.

**Theorem 5 (local-port diameter principle).** Let \(\widetilde G\to G\) be a connected regular two-sheeted graph cover with edge-free deck action. At every cover vertex \(v\), let \(A_v\) be a graph on the incident cover edges; an edge of \(A_v\) indicates that the corresponding turn is permitted. Assume the collection \(\{A_v\}\) is equivariant under the deck involution and that each \(A_v\) is connected of diameter at most \(L\). Let \(H_{\rm all}=L(G)\), let \(H_{\rm perm}\) retain only permitted turns, and define their pointed binary line-cover duals \(D_{\rm all}\) and \(D_{\rm perm}\). Then
\[
\boxed{D_{\rm perm}=D_{\rm all}/(E(H_{\rm all})\setminus E(H_{\rm perm})),}
\]
and restriction is a binary linear isomorphism \(Z(D_{\rm all})\cong Z(D_{\rm perm})\). Every omitted turn \(e\) has a non-port cocircuit certificate containing \(e\), containing no other omitted turns, and having at most \(L+1\) elements.

*Proof.* An omitted turn is an incident-edge pair \(s,t\) at some lifted vertex \(v\). Choose a shortest path \(s=s_0,s_1,\ldots,s_k=t\) in the local permitted-turn graph \(A_v\), where \(k\le L\). The path together with the omitted turn is a simple cycle of the full line graph, since the incident edge states are distinct. Its projection remains simple: two distinct edges incident at \(v\) cannot be deck translates, as the translates are incident at the distinct vertex \(\tau v\), and a deck-invariant cover edge is excluded. The projected cycle has monodromy zero because its lift closes. It therefore provides the required non-port cocircuit of \(D_{\rm all}\). Orthogonality reconstructs the omitted coordinate as a parity sum over the \(k\) permitted turns. The matrix for the permitted-turn dual is the restriction of the full primal matrix to permitted columns together with the port. Duality proves the contraction identity, and these reconstruction relations make its binary cycle-space projection injective, hence an isomorphism. \(\square\)

The local graph for cube turns is \(K_n\): every pair of incident coordinate edges is a permitted turn, so no turn is omitted. At an ordered-pair state \((u,v)\) in the boundary cover, the incident triples split into \(r=n-2\) incoming and \(r\) outgoing states, indexed by the remaining symbols. Permitted turns form
\[
\boxed{A_{(u,v)}=K_{r,r}\setminus\{\text{the }r\text{ matched pairs}\}.}
\]
For \(r\ge3\), this graph has diameter three: vertices on the same side have a common neighbor, unmatched opposite vertices are adjacent, and matched opposite vertices have a three-edge path but no shorter path. Thus Theorem 1 is an instance of Theorem 5 with \(L=3\).

**Consequence for generalization.** A common intrinsic hypothesis worth retaining is *bounded-diameter deck-equivariant local-port completion*. It guarantees that the colored pointed matroid can be reduced to permitted turns without information loss. It does not guarantee a long independent-resource path; that stronger selector still requires compatible global path exchange and the auxiliary resource constraints.

**Theorem 6 (quantitative port-cocircuit transport).** Under the hypotheses of Theorem 5, let \(X\in Z(D_{\rm all})\) contain the port, and let \(Y=C\cup\{p\}\) be any port cocircuit of \(D_{\rm all}\). Write \(r=|C|\), let \(t=|C\cap(E(H_{\rm all})\setminus E(H_{\rm perm}))|\), and let
\[
w_X(C)=|C\cap X|.
\]
There exists a port cocircuit \(Y'=C'\cup\{p\}\) of \(D_{\rm perm}\) such that
\[
\boxed{|C'|\le r+(L-1)t,\qquad
|C'\cap \pi(X)|\le w_X(C)+Lt.}\tag{9}
\]
Equivalently, the port intersection satisfies
\[
\boxed{|\pi(X)\cap Y'|\le |X\cap Y|+Lt.}\tag{10}
\]

*Proof.* For each forbidden turn \(e\in C\), take the permitted path \(P_e\) of length at most \(L\) obtained in Theorem 5, with the closed walk \(e+P_e\) of monodromy zero. In the binary cycle space of the graph \(H_{\rm all}\) set
\[
Z=C\mathbin{\triangle}
\mathop{\triangle}_{e\in C\setminus E(H_{\rm perm})}
(\{e\}\mathbin{\triangle}P_e).
\]
All forbidden edges cancel, so \(Z\) is an Eulerian subgraph of \(H_{\rm perm}\). Since the added cycles have zero monodromy and \(C\) has monodromy one, \(Z\) also has monodromy one. Decompose \(Z\) into edge-disjoint simple cycles. An odd number of these have nonzero monodromy, so choose any such cycle \(C'\). It is a legal-turn port cocircuit after adjoining \(p\). The count of edges in \(Z\) is at most \(r-t+Lt\), which bounds \(|C'|\). Likewise
\[
w_X(Z)\le w_X(C\cap E(H_{\rm perm}))
+\sum_{e\text{ forbidden in }C}w_X(P_e)
\le w_X(C)+Lt,
\]
and the chosen constituent satisfies \(w_X(C')\le w_X(Z)\). This proves (9) and (10). \(\square\)

For boundary tournaments, \(L=3\), hence each forbidden full turn costs at most two additional edges and three additional turn disagreements when a cocircuit is transferred into the alternating-port matroid. The estimate alone does not ensure forward orientation, resource simplicity, or long witness length. It instead isolates an actionable obstruction to lifting matroidal intersection bounds: the **forbidden-turn count of the chosen cocircuit**.

**Corollary 7 (parity-improved transport).** The turn-weight estimate in Theorem 6 can be strengthened to
\[
\boxed{|C'\cap\pi(X)|\le w_X(C)+2\lfloor L/2\rfloor\,t,}
\qquad
\boxed{|\pi(X)\cap Y'|\le |X\cap Y|+2\lfloor L/2\rfloor\,t.}
\tag{11}
\]
In particular, the boundary legal-turn contraction with \(L=3\) incurs at most **two**, rather than three, additional color changes per omitted turn of the original cocircuit.

*Proof.* The reconstruction cycle \(\{e\}\cup P_e\) has monodromy zero, so it meets every port-containing binary cycle evenly. Therefore
\[
w_X(P_e)\equiv\mathbf1_X(e)\pmod2.
\]
Because \(w_X(P_e)\le |P_e|\le L\) and \(\mathbf1_X(e)\in\{0,1\}\), the increase
\[
w_X(P_e)-\mathbf1_X(e)
\]
is an even integer no larger than \(2\lfloor L/2\rfloor\). In the proof of Theorem 6, sum these increases over the \(t\) replaced edges before selecting an odd-monodromy cycle constituent. \(\square\)
