# Global antipodal graphic-flat covers and rainbow spanning-forest chambers

# Global antipodal graphic-flat covers and rainbow spanning-forest chambers

The preceding four-sector theorem describes one monochromatic component and its opposite-colored deck image. The following characterization instead controls the **entire partition of the covering graph into monochromatic components at once**. Its hypotheses and conclusions are intrinsic to a graphic matroid, an edge-free involutive automorphism, and the corresponding partition matroid on deck edge orbits. It applies to both the cube and the ordered-pair cover of ordinary boundary 3-tournaments.

Let \(G=(V,E)\) be a finite connected graph with a fixed-point-free involutive automorphism \(\tau\) acting freely on edges, and let \(M=M(G)\) be its graphic cycle matroid. For a partition \(\Pi\) of \(V\) into nonempty parts, define its graphic flat
\[
\boxed{
F_\Pi=\{uv\in E:u,v\text{ lie in the same part of }\Pi\}.
}
\tag{1}
\]
This is a flat of \(M\); its rank is \(r_M(F_\Pi)=|V|-|\Pi|\). The deck image \(\tau F_\Pi\) is the flat for the partition \(\tau\Pi\).

Call a forest \(T\subseteq F_\Pi\) **orbit-rainbow** if it contains at most one element from each two-element edge orbit \(\{e,\tau e\}\). Call it a **spanning forest of \(\Pi\)** if the connected components of \((V,T)\) are precisely the parts of \(\Pi\).

## 1. Global flat-cover characterization

**Theorem 1 (antipodal flat-cover realization).** The partition \(\Pi\) is the partition of all vertices into color-zero connected components of some deck-odd edge coloring \(c:E(G)\to\mathbb F_2\) if and only if both conditions hold:
\[
\boxed{F_\Pi\cup\tau F_\Pi=E(G),}
\tag{2}
\]
and
\[
\boxed{\text{there exists an orbit-rainbow spanning forest }T
\text{ of }\Pi.}
\tag{3}
\]
Equivalently, with \(P_\tau\) the orbit partition matroid on \(E\),
\[
\boxed{
\max\{|T|:T\subseteq F_\Pi,\ 
T\in\mathcal I(M)\cap\mathcal I(P_\tau)\}
=r_M(F_\Pi)=|V|-|\Pi|.
}
\tag{4}
\]

*Proof.* Suppose \(c\) is deck-odd with red component partition \(\Pi\). Choose a spanning forest \(T\) in the red-edge subgraph. Every red edge has both endpoints in the same red component, so it belongs to \(F_\Pi\). The deck image of every blue edge is red and therefore lies in \(F_\Pi\), so every blue edge lies in \(\tau F_\Pi\). Thus \(E=F_\Pi\cup\tau F_\Pi\). The red forest \(T\) is independent in \(M\) and cannot contain both members of a deck edge orbit, since their colors are opposite; it spans all parts of \(\Pi\), proving (3).

Conversely, suppose (2) and (3). For each edge orbit \(\{e,\tau e\}\), at least one member belongs to \(F_\Pi\). If the orbit meets \(T\), declare its unique tree edge red and its mate blue. Otherwise select any member of the orbit lying in \(F_\Pi\) to be red, and its mate blue. These prescriptions are consistent because \(T\) is orbit-rainbow. They define a deck-odd coloring in which **every red edge lies in** \(F_\Pi\) and **every tree edge lies among the red edges**. Therefore no red edge joins two different parts of \(\Pi\), while \(T\) red-connects each part. The red component partition is \(\Pi\). \(\square\)

**Corollary 2 (all-component cut separation).** If \(\Pi\) is realizable, no graph edge simultaneously crosses a part boundary of \(\Pi\) and the corresponding boundary of \(\tau\Pi\). In other words, for every \(e=uv\),
\[
\boxed{
u\not\sim_\Pi v\ \Longrightarrow\ \tau u\sim_\Pi\tau v.
}
\tag{5}
\]
Here \(\sim_\Pi\) means belonging to the same part. For a specified red component \(R\in\Pi\), this implies the disjoint cocycles \(\delta(R)\cap\tau\delta(R)=\varnothing\) of the preceding Subsection.

*Proof.* Equation (2) says every edge is internal to \(\Pi\) or internal to \(\tau\Pi\). The two formulations are equivalent. If an edge leaves \(R\), it crosses \(\Pi\), so its deck image is internal to \(\Pi\), and cannot leave the corresponding deck image component. \(\square\)

This is stronger organizational information than imposing antipodal boundary separation on one red component at a time: it specifies a pair of **graphic-matroid flats that cover all covering edges simultaneously**.

## 2. A global matroid-intersection cut test

**Theorem 3 (refinement-partition criterion).** Given a vertex partition \(\Pi\), the orbit-rainbow forest condition (3) is equivalent to the following inequalities. For every partition \(\mathcal Q\) of \(V\) that refines \(\Pi\),
\[
\boxed{
\#\bigl\{\{e,\tau e\}:
e\in F_\Pi\text{ joins distinct parts of }\mathcal Q\bigr\}
\ge |\mathcal Q|-|\Pi|.
}
\tag{6}
\]
Thus a proposed component partition is realizable precisely when its two antipodal graphic flats cover \(E\) and all inequalities (6) hold.

*Proof.* If an orbit-rainbow spanning forest \(T\) exists, then contracting each part of \(\mathcal Q\) within its containing \(\Pi\)-part requires at least \(|\mathcal Q|-|\Pi|\) forest edges crossing \(\mathcal Q\). Those forest edges belong to different deck orbits, proving (6).

For sufficiency, apply the matroid-intersection min–max theorem to the restrictions of \(M\) and \(P_\tau\) to \(F_\Pi\). For any \(A\subseteq F_\Pi\), let \(\mathcal Q\) be the partition of \(V\) into connected components of \((V,A)\). It refines \(\Pi\), with
\[
r_M(A)=|V|-|\mathcal Q|,\quad
r_M(F_\Pi)=|V|-|\Pi|.
\]
Every edge of \(F_\Pi\) crossing \(\mathcal Q\) lies in \(F_\Pi\setminus A\). Thus (6) gives
\[
r_{P_\tau}(F_\Pi\setminus A)
\ge|\mathcal Q|-|\Pi|
=r_M(F_\Pi)-r_M(A).
\]
This is the matroid-intersection min–max criterion for a common independent subset of \(F_\Pi\) of size \(r_M(F_\Pi)\). Such a common independent set is the required orbit-rainbow spanning forest of \(\Pi\). \(\square\)

## 3. Boolean chambers of compatible colorings

For fixed \(\Pi\) satisfying (2) and any orbit-rainbow spanning forest \(T\) of \(\Pi\), let
\[
\mathcal O_{\rm amb}(\Pi)
=\{\{e,\tau e\}: e,\tau e\in F_\Pi\}
\tag{7}
\]
be the set of **ambiguous edge orbits**, whose two members are both internal to red components. Let \(\mathcal O(T)\) be the edge orbits represented by \(T\).

**Proposition 4 (basis chambers).** The family of all deck-odd colorings in which \(T\) is red and no red edge leaves a part of \(\Pi\) is an affine Boolean cube of dimension
\[
\boxed{
|\mathcal O_{\rm amb}(\Pi)\setminus\mathcal O(T)|.
}
\tag{8}
\]
In every such coloring, each edge in \(F_\Pi\setminus\tau F_\Pi\) is **forced red**, each edge in \(\tau F_\Pi\setminus F_\Pi\) is **forced blue**, and the remaining choices occur independently on the ambiguous orbits not constrained by \(T\). Every compatible coloring with red component partition \(\Pi\) belongs to at least one of these spanning-forest chambers.

*Proof.* For a deck orbit with only one member in \(F_\Pi\), that member must be red so red edges cannot leave the components; the other member is blue. For an orbit with both members in \(F_\Pi\), either orientation is permitted unless the orbit meets \(T\), in which case its tree member is forced red. The choices on distinct unconstrained orbits are independent. Each resulting coloring contains \(T\) and has red edges only in \(F_\Pi\), so its red components are the parts of \(\Pi\). Conversely, any coloring giving \(\Pi\) has a red spanning forest \(T\), belongs to the associated chamber, and meets the stated conditions. \(\square\)

**Corollary 5 (a forced-edge geodesic certificate).** In the antipodal cube, suppose a realizable partition \(\Pi\) has a monochromatic antipodal geodesic using only edges from the forced-red set \(F_\Pi\setminus\tau F_\Pi\). Then **every** deck-odd coloring with red component partition \(\Pi\) satisfies NORI1.

*Proof.* The edges of such a geodesic are red by Proposition 4 for every compatible coloring, so the path is a monochromatic full antipodal geodesic. \(\square\)

The certificate is sufficient, not asserted to hold in every realizable partition. In particular, when \(F_\Pi=E\), the forced-red set is empty, and the certificate does not apply.

## 4. Relationship to both canonical pointed matroids

In the cube, the graphic matroid is \(M(Q_n)\) and \(\tau\) is coordinate complementation. In the ordinary boundary-tournament covering, use \(M(S(K_n))\), whose edge states are reversal-paired ordered triples. Both have the same full component-partition characterization (2), (4) and the refinement cut test (6).

This theorem coordinates *all* monochromatic components across the two sheets of their regular covering, beyond the Eulerian zero-turn contact graph and the local four-sector pair for a single component. It also exposes the coloring choices not fixed by component connectivity as independent ambiguous edge-orbit variables. Nevertheless, it does not alone prove the deterministic spanning-path targets. In the cube, geodesicity must still be certified by a red resource-simple antipodal path in at least one component; in the boundary model, the original-vertex graphic-resource independence and forward ordered-pair coherence remain additional requirements. The global flat-cover constraints give an intrinsic common class within which a future geodesic or one-turn selector theorem must operate.

## 5. Global cycle-rank conservation

The flat-cover theorem gives a common partition-based representation; regularity imposes an additional **global graphic-matroid nullity budget** that cannot be detected inside a single component.

**Theorem 6 (fixed red cycle-rank budget).** Let \(G\) be a finite \(d\)-regular graph on \(N\) vertices with a free vertex-and-edge involution \(\tau\), and let \(c\) be any deck-odd edge coloring. Let \(\Pi_c\) be its partition into color-zero connected components, including isolated vertices, with \(\kappa=|\Pi_c|\). Then the nullity of its color-zero edge set in the graphic matroid \(M(G)\) is
\[
\boxed{
\dim Z(G_{\rm red})
=|E_{\rm red}|-r_M(E_{\rm red})
=\frac{(d-4)N}{4}+\kappa.
}
\tag{9}
\]
In particular,
\[
\boxed{
\sum_{R\in\Pi_c}
\left(|E_{\rm red}(R)|-|R|+1\right)
=\frac{(d-4)N}{4}+\kappa.
}
\tag{10}
\]

*Proof.* The covering graph has \(dN/2\) edges. Since every antipodal edge orbit consists of one red and one blue edge, \(|E_{\rm red}|=dN/4\), independently of the coloring. The graphic rank of the red subgraph is \(N-\kappa\), because its connected components are the parts of \(\Pi_c\), including isolated vertices. Subtracting rank from edge count proves (9); summing the component cyclomatic numbers proves (10). \(\square\)

**Corollary 7 (the two canonical budgets).** For an antipodally odd edge coloring of \(Q_n\), whose \(2^n\) vertices have degree \(n\),
\[
\boxed{\dim Z((Q_n)_{\rm red})=(n-4)2^{n-2}+\kappa.}
\tag{11}
\]
For an ordinary reversal-odd boundary coloring on the ordered-pair covering graph \(S(K_n)\), which has \(N=n(n-1)\) vertices and degree \(d=2(n-2)\),
\[
\boxed{
\dim Z((S(K_n))_{\rm red})
=\frac{n(n-1)(n-4)}2+\kappa.
}
\tag{12}
\]

The budget is global: it does **not** assert that every self-antipodal red component contains a red circuit. Research-note constructions in Q4–Q6 exhibit self-antipodal components that are trees, including one with a two-unit geodesicity defect. Such tree components contribute zero to (10), forcing the total cycle-rank budget to reside elsewhere. This is a rigorous indication that a successful matroid closure argument may need to compare distinct monochromatic components and their graphic cycles through the shared antipodal flat-cover constraints, rather than optimizing only one port-loop component.
