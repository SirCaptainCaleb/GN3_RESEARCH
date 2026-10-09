# Optimal antipodal window-transport distance and exponential monochromatic connector abundance in each direction

# Optimal-length antipodal window transport and quantitative middle-direction monochromatic connectors

Let n>=5. Fix a coordinate i and an active NORI binary coloring c of ACTUAL PHYSICAL ordered three-faces satisfying c(bar F,reverse pi)=1-c(F,pi). Let H_i be the graph whose vertices are all actual ordered three-face windows containing free direction i. Join two such vertices when they occur as consecutive windows of a genuine four-edge geodesic and i is one of their two middle directions. Every H_i edge has a literal physical four-edge path certificate. Call the edge good when its endpoint face colors agree. Let N_i count distinct good edges in H_i.

**THEOREM 1 (sharp geometric antipodal transport length).** The shortest H_i walk between any window u with ordered triple (a,i,b) and its physical antipodal reversed mate tau(u) is
  L_n = max{6, 2*ceil((n-1)/2)}.
This distance is independent of u and the coloring.

**Proof of lower bound.** Each H_i shift takes i from the middle of the ordered triple to an outer slot, or conversely, so the length L of a walk between middle-i windows is even. Project its ordered triples to an uncolored triple sequence. A two-edge move between middle-i windows can change AT MOST ONE of the two ordered outer coordinates (and may return to the same pair): it has one of the forms
  (a,i,b)--(i,b,h)--(d,i,b)
or
  (a,i,b)--(h,a,i)--(a,i,d),
with four distinct coordinates in each displayed shift. Reversing the two different outer entries (a,b)->(b,a) takes at least THREE such single-slot replacements, hence L>=6.

Further, both original outer letters a and b must at some point be removed from their slots and later introduced into their OPPOSITE slots. Thus at least two of the L elementary shifts reintroduce one of {a,b} rather than a previously unseen outsider. Each elementary shift introduces at most one new direction. There are n-3 outsiders k outside {a,i,b}; every one MUST occur free in some intermediate window, because otherwise its fixed physical bit cannot change between u and tau(u). Therefore n-3 <= L-2, or L>=n-1. With evenness, L>=max{6,2ceil((n-1)/2)}.

**Proof of matching upper bound: explicit direction-triple sequence.** Put m=n-3 and enumerate the outsiders k1,...,km. All adjacent ordered triples below are related by a genuine four-distinct-direction shift with i in its overlapping middle pair. Therefore each abstract sequence can be realized as an H_i walk on physical ordered windows.

(A) m EVEN and m>=4 (odd n>=7). Start T0=(a,i,b). For j=1,...,m-2 set
  Tj=(i,b,kj) for j odd; Tj=(kj,i,b) for j even.
The last such triple is (k_(m-2),i,b). Finish with the FOUR shifts
  (k_(m-1),k_(m-2),i),
  (k_(m-2),i,a),
  (i,a,km),
  (b,i,a).
This visits ALL m outsider directions in L=m+2=n-1 shifts.

(B) m ODD and m>=5 (even n>=8). Start with the TWO shifts
  (a,i,b) -> (i,b,k1) -> (a,i,b).
Then introduce k2,...,k_(m-2), one per shift, alternating
  (i,b,kj) for EVEN j, and (kj,i,b) for ODD j.
The final alternating triple is (k_(m-2),i,b). Append the same four-shift tail as in (A). The resulting length is L=2+(m-3)+4=m+3=n.

(C) n=5 or 6. Choose outsiders k1,k2, and let k3 be the third outsider when n=6, or k3=k1 when n=5. The SIX-shift sequence is
  (a,i,b), (i,b,k1), (k2,i,b),
  (k1,k2,i), (k2,i,a), (i,a,k3), (b,i,a).
For n=5, using k1 again in the penultimate triple is legal since the adjacent triples use four distinct directions.

**Physical realization.** Start with the prescribed actual window u, whose exterior bits are fixed. The direction sequences begin with (a,i,b), end with (b,i,a), and every outsider k appears as a FREE direction at least once. Assign each outsider's common fixed bits to the starting values before its first free occurrence, and to the COMPLEMENTARY starting values after its last free occurrence. Any intermediate fixed intervals can be assigned consistently, changing a bit only while that direction is free. For the endpoint directions a,i,b, which are free in BOTH endpoint windows, assign any consistent intermediate fixed values. Each consecutive ordered triple then corresponds to two actual PHYSICAL faces with identical fixed bits outside their union, so it admits a genuine four-edge connector. The terminal actual window has precisely the complementary exterior fixed bits and reversed ordered triple, hence is tau(u). This realizes the asserted length. Combining with the lower bound proves sharpness. QED.

**THEOREM 2 (quantitative NORI connector supply, both middle orientations).** Define
 E0=2^(n-2)(n-1)(n-2)(n-3)
and L_n as above. In H_i, edges divide into two equal orbits E_L,E_R according as i occurs FIRST or SECOND among the two overlapping middle coordinates of their uniquely directed four-word. EACH orbit contains exactly E0 edges. If K_L,K_R count its genuine good edges, then
 K_L=K_R >= ceil(E0/L_n).
Consequently
  BOX: N_i=K_L+K_R >= 2*ceil(2^(n-2)*(n-1)*(n-2)*(n-3)/max{6,2ceil((n-1)/2)}).
In particular the fraction of good edges in EACH orientation class is at least 1/L_n, asymptotically of order 1/n.

**Proof.** Translation of physical cube bits and arbitrary permutation of coordinate names fixing i act transitively on EACH of E_L,E_R and commute with tau. To count an orbit, choose the ordered other three directions in (n-1)(n-2)(n-3) ways, all n-4 exterior fixed bits in 2^(n-4) ways, and the separate two endpoint-face exterior bits in 4 ways. Thus |E_L|=|E_R|=E0. Antipodal reversal tau takes a genuine shift with four-word (a,b,c,d) to one with word (d,c,b,a), exchanges the two i-middle orientations, and complements both colors. Therefore it bijects good edges of E_L with good edges of E_R: K_L=K_R=:K.

Choose a shortest geometric antipodal walk P from u to tau u of length L_n. The endpoint colors differ by the active NORI oddness. Since L_n is even, the number of equal-color consecutive-window edges on P is ODD and is at least one. For every cube translation and coordinate permutation g fixing i, gP is still an even walk between gv and tau(gv), so it too has >=1 good edge. Average over all these symmetries. Every one of the L_n edges of P is distributed uniformly over the appropriate orbit, whose good-edge density is K/E0. Hence
 1<=E_g[# good edges of gP]=L_n*K/E0.
So K>=ceil(E0/L_n), as claimed. QED.

**Examples.** n=5: L5=6, E0=192, so at least 32 distinct equal-color connector edges of EACH middle orientation, N_i>=64. n=6: L6=6, E0=960, giving N_i>=320. For all n the theorem counts genuine physical ordered-face/window certificates, with their unique four-direction geodesic incidence; no SAT computation or abstract unphysical labels are used.

**Scope and exact gap.** This strengthens the earlier 4n-6 and 2n-2 transport walks and their connector-count bounds. It is a sharp theorem about the underlying uncolored H_i antipodal distance, and a rigorous quantitatively large supply of physical monochromatic four-edge connectors in every direction. Different witnesses may have incompatible roots, terminal two-direction memories, and colors. Averaging alone cannot force their concatenation into complementary same-root reversed-two-tail reachability. Consequently grand NORI remains open. The targeted missing statement is a GLOBAL lifting/gluing theorem for the certified window-shift graph that retains these exact path memories and enforces one-switch full antipodal closure.
