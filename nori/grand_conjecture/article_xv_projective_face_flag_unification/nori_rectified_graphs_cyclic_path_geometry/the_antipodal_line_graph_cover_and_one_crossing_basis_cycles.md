# The antipodal line-graph cover and one-crossing basis cycles

# The antipodal line-graph cover and one-crossing basis cycles

There is a canonical, reference-free topological meaning for the symmetric part of a NORI1 reversal-odd turn connection. The NORI1 conjecture becomes a one-crossing theorem for distinguished nontrivial cycles in a fixed double cover of a graph. All such cycles are full dimension-simple cube geodesics.

Let \(n\ge3\). Write \(H=L(Q_n)\) for the line graph of the \(n\)-cube: vertices of \(H\) are undirected cube edges, and adjacency means sharing a cube vertex. Cube antipodality induces a free graph involution \(\tau\) on \(H\). No vertex of \(H\) is adjacent to its antipodal image. Thus
\[
\boxed{p:H\longrightarrow Y=H/\tau}
\tag{1}
\]
is a connected regular double covering of finite graphs. Denote its nontrivial covering class by \(\omega\in H^1(Y;\mathbb F_2)\).

**Theorem 1 (NORI1 colorings are representatives of a fixed covering class).** For any antipodally odd undirected cube-edge coloring \(c:V(H)\to\mathbb F_2\), define on every quotient-graph edge represented by adjacent \(e,f\in V(H)\)
\[
\boxed{a_c([e,f])=c(e)+c(f).}
\tag{2}
\]
This is well defined under replacing both \(e,f\) by their antipodes, and represents \(\omega\). Conversely every binary one-cochain \(a\) on \(Y\) with \([a]=\omega\) is \(a_c\) for some antipodally odd coloring \(c\), unique up to complementing all edge colors. Thus the space of unrestricted NORI1 colorings modulo global complementation is canonically the set of all cochain representatives of the same nonzero cohomology class \(\omega\).

*Proof.* Replacing \(e,f\) by \(\tau e,\tau f\) complements both colors, preserving (2). Take any closed walk \(\gamma\) in \(Y\), and lift it to a walk \(e_0,e_1,\ldots,e_m\) in \(H\). The sum of (2) along the lift telescopes to \(c(e_0)+c(e_m)\). This is zero if the lift ends at \(e_0\), and one if it ends at \(\tau e_0\). The resulting evaluation on loops is the monodromy homomorphism of the double cover (1), proving \([a_c]=\omega\). Fix one coloring \(c_0\). For every cochain \(a\) in its cohomology class, there exists a zero-cochain \(f:V(Y)\to\mathbb F_2\) with \(a=a_{c_0}+df\). Put \(c(e)=c_0(e)+f(p(e))\). This is antipodally odd and has \(a_c=a\). If two colorings induce the same \(a\), their difference is a locally constant function on connected \(H\), hence a global constant. \(\square\)

**Theorem 2 (full geodesics are distinguished essential cycles).** Let \(P\) be any full antipodal geodesic in \(Q_n\), with undirected edge sequence \(e_1,e_2,\ldots,e_n\) using every dimension once. Its final edge is incident with the antipodal translate \(\tau e_1\) at its last cube vertex. Therefore
\[
\boxed{e_1\to e_2\to\cdots\to e_n\to\tau e_1}
\tag{3}
\]
is a length-\(n\) path in the line graph, projecting to a closed length-\(n\) cycle \(\gamma_P\) in \(Y\). Its vertices represent \(n\) distinct edge dimensions, so the projected cycle is simple. Its lifted endpoint is \(\tau e_1\), hence
\[
\boxed{\langle\omega,[\gamma_P]\rangle=1.}
\tag{4}
\]
The binary edge labels \(a_c\) around \(\gamma_P\) are the \(n-1\) consecutive internal color-change bits of the geodesic, followed by its antipodally twisted closing color-change bit.

*Proof.* Dimension-simplicity implies the edge dimensions are all distinct, so no two vertices of the projected cycle coincide. The last edge ends at \(\bar x\), where \(\tau e_1\) begins, verifying the closing adjacency. The quotient loop lifts from \(e_1\) to \(\tau e_1\), giving (4). Along its first \(n-1\) edges, (2) is the original adjacent color XOR. Along its final edge, (2) is \(c(e_n)+c(\tau e_1)=1+c(e_n)+c(e_1)\). \(\square\)

**Corollary 3 (topological equivalence of NORI1).** The unrestricted NORI1 conjecture is equivalent to the following one-crossing statement:

> Every \(\mathbb F_2\)-valued one-cochain representing the antipodal covering class \(\omega\) on \(Y=L(Q_n)/\tau\) has at least one distinguished cycle \(\gamma_P\) from (3) on which it is nonzero at only one edge.

*Proof.* The cycle (3) traverses all dimension names once, so its \(n\) possible cyclic starting positions correspond to root slides of complete antipodal geodesics. If its sole labeled edge is chosen as the closing edge, every internal adjacent color comparison is zero, making that root-slid geodesic monochromatic. Conversely a monochromatic full geodesic has no internal changes and, by (4), one closing change. Theorem 1 identifies all NORI1 colorings modulo complement with all cochain representatives of \(\omega\). \(\square\)

**Chiral translation.** An orientation bit \(\chi(e,f)\) on each directed line-graph adjacency, with \(\chi(f,e)=1+\chi(e,f)\) and \(\chi(\tau e,\tau f)=\chi(e,f)\), produces the reversal-odd turn connection
\[
B_c(e,f)=a_c([e,f])+\chi(e,f).
\]
The correction \(B_c+\chi\) is independent of the auxiliary orientation and represents the canonical class \(\omega\). Thus local reversal oddness is a choice of *chiral representation of a nontrivial cover class*, rather than an additional restriction on NORI1 colorings.

**Limit and research objective.** An arbitrary graph double cover with a distinguished family of nontrivial cycles need not have a one-crossing member: sparse signed cycles already yield high crossing counts. The essential additional structure in (3) is that these cycles arise from all full dimension-simple geodesics in the rich cubical face-incidence system. Ordinary reversal-odd boundary tournaments also define arbitrary local chiral data, but their analogue of a fixed covering class has not yet been established. Theorem 2 provides a precise topological target for a future shared one-switch theorem without assuming a separate state-graph construction.
