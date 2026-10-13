# Intrinsic color profiles and rigidity of the ordered-pair overlap graph

- Stable ID: note_nori_xiii_intrinsic_color_profile_rigidity
- Author: Article XIII independent investigation
- Primary home: article:nori_article_xiii_binary_involutive_rainbow_paths
- Labels: rigidity, color-incidence, minimum-strengthening, boundary-tournaments
- Lifecycle: active
- Epistemic status: open
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7442_3
- Updated session: session_nori_r7442_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Intrinsic color profiles and a rigidity warning for minimum strengthenings

**Definition.** Let \((G,\lambda)\) have an ordinary color palette \(C\) with \(n=|C|\ge4\). Assume every vertex \(x\) has one *missing color* \(m(x)\), one *repeated color* \(r(x)\) occurring \(n-2\) times, and one incident edge of each of the remaining \(n-2\) colors. Thus \(m(x)\ne r(x)\). All these data are recovered solely from the ordinary edge coloring.

**Rigidity theorem.** Suppose additionally:
(i) the map \(x\mapsto(m(x),r(x))\) is injective;
(ii) every edge \(xy\) of ordinary color \(c\) has color multiplicity one at precisely one endpoint \(x\) and multiplicity \(n-2\) at the other endpoint \(y\);
(iii) on that edge the missing color at the repeated endpoint equals the repeated color at the single-incidence endpoint: \(m(y)=r(x)\).
Then \((G,\lambda)\) is color-preservingly isomorphic to the undirected ordered-pair overlap graph \(D_n\), with vertex set \(\{(a,b):a,b\in C,\ a\ne b\}\) and one edge of color \(c\) between \((a,b)\) and \((b,c)\) whenever \(a,b,c\) are distinct.

**Proof.** Identify a vertex \(x\) with its pair \((m(x),r(x))=(a,b)\). Each \(c\notin\{a,b\}\) occurs once at \(x\), so there is an edge of color \(c\) with unique-incidence endpoint \(x\). The other endpoint \(y\) has repeated color \(c\) by (ii), and missing color \(b\) by (iii). Hence its intrinsic profile is \((b,c)\). This uniquely determines \(y\) by (i). Thus every directed ordered-pair move \((a,b)\to(b,c)\) with three distinct colors occurs in \(G\).

The graph of such directed moves on ordered pairs of distinct elements of \(C\) is strongly connected for \(n\ge4\). One way to see this is that to reach any target \((d,e)\) from \((a,b)\) with \(b\ne d\), choose an index \(c\) outside \(\{a,b,d,e\}\), if available, and follow \((a,b),(b,c),(c,d),(d,e)\); the remaining cases can be reached by inserting a directed three- or four-cycle through distinct colors. Equivalently, this is the nonbacktracking directed-edge graph of a complete graph, well known to be strongly connected for \(n\ge4\). Therefore, since \(G\) contains at least one vertex and is closed under every such move, all \(n(n-1)\) ordered pairs occur as vertex profiles. Injectivity gives one vertex for each pair. All incident unique-color edges are the stated overlap edges, and repeated-color multiplicities are exhausted by their incoming counterparts. Thus \(G=D_n\).

If an involutive vertex automorphism \(\tau\) additionally satisfies \(m(\tau x)=r(x)\) and \(r(\tau x)=m(x)\), it is necessarily the ordered-pair reversal \(\tau(a,b)=(b,a)\). An arbitrary binary edge labeling reversed by this \(\tau\) is precisely the unrestricted reversal-odd boundary 3-tournament labeling. \(\square\)

**What this establishes, and what it does not.** Profile recoverability (injectivity) is a simple intrinsic feature absent from the two-sheet parity-cover obstructions: each such cover has two vertices with the same \((m,r)\). The edge-incidence identity \(m(y)=r(x)\) is another intrinsic feature of the boundary graph. However, imposing the entire local multiplicity template together with these two requirements recovers the boundary graph itself, so this package is too restrictive to count as a minimal unification of NORI1 and boundary tournaments. In the cube the ordinary edge coloring is proper and no repeated or missing color exists at a vertex. A useful common hypothesis must abstract a weaker part of this incidence compatibility while allowing the proper-color case. No positive linear one-switch bound is claimed.
