# Paired-start exact criterion for NORI1 as a unification toy model

- Stable ID: note_antipodal_paired_start_nori1_toy_unification_probe
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_ix_unification
- Labels: approach, proved, toy_model
- Lifecycle: active
- Epistemic status: proved
- Current version: 6
- Retention: current and at most one previous snapshot
- Created session: session_nori_r4593_2
- Updated session: session_nori_r6202_2
- Disposition: none
- Successor: none

## Related references

- subsection:antipodal_multifacet_bridge_and_seven_coordinate_universality, exact version 2
- note:note_joint_realizability_selection_for_nori1_and_boundary_tournaments

## Research note

# NORI1-only mathematical toy: precise paired-start criterion

Mathematical status: precise proof from subsection composition v2, not a theorem about boundary tournaments and not a common unification theorem. Its relevance is the **joint realizability at one root** mechanism. A future worker may use this as a toy model only after specifying a single structural axiom with realized underlying witnesses that simultaneously specializes to arbitrary antipodally odd NORI1 colorings and unrestricted ordinary boundary tournaments; the two-extra-window seam obstruction must be addressed explicitly. This is a NORI1 toy model for finding a compatible-root selection principle that can extend naturally to valid ordered-triple paths.\n\n## Antipodal paired-start criterion: the precise rooted strengthening

Write \(A_{k+1}\) for the assertion that every antipodally odd coloring of *underlying undirected* edges of \(Q_{k+1}\) has a monochromatic full antipodal geodesic. For an arbitrary underlying (not necessarily antipodal) binary edge coloring \(d\) of \(Q_k\), define
\[
G(d)=\{u\in Q_k:\text{some full antipodal geodesic starting at }u
\text{ has }d\text{-word }0^a1^{k-a}\text{ for }0\le a\le k\}.
\]
Both constant words are included. Let \(\tau u=\bar u\).

**Theorem (precise antipodal paired-start reduction).** For every \(k\ge1\),
\[
\boxed{A_{k+1}\quad\Longleftrightarrow\quad
  \text{for every arbitrary underlying edge coloring }d\text{ of }Q_k,
  \ G(d)\cap\tau G(d)\ne\varnothing.}
\tag{11}
\]
Equivalently, every such \(d\) has *one* starting vertex \(u\) from which there are full antipodal geodesics of each weakly monotone type, one with color word \(0^a1^{k-a}\) and one with color word \(1^b0^{k-b}\), with possibly different coordinate orders.

**Proof.** Fix \(d\), and let \(g:Q_k\to\mathbb F_2\) be an arbitrary *antipodally odd* vertex function, \(g(\bar u)=1\oplus g(u)\). Make a underlying-edge coloring \(c\) on \(Q_k\times Q_{\{s\}}\), writing the last coordinate as \(z\in\{0,1\}\), by
\[
c_i(u,0)=d_i(u),\qquad
c_i(u,1)=1\oplus d_i(\bar u)\quad (i\in[k]),
\qquad c_s(u,z)=g(u).
\tag{12}
\]
Here \(d_i(u)\) is invariant under flipping \(u_i\). Thus every edge in (12) is underlying, and \(c\) is antipodally odd. Moreover, *every* legal antipodally odd underlying-edge coloring of \(Q_{k+1}\) has precisely this form, once the last direction \(s\) is chosen: its lower-facet restriction supplies \(d\), and its \(s\)-edges supply \(g\).

We claim that \(c\) has a full geodesic of color \(0\) precisely when
\[
G(d)\cap g^{-1}(0)\ne\varnothing. \tag{13}
\]
For the forward construction, choose \(u\in G(d)\) with \(g(u)=0\), and a \(d\)-geodesic
\(R:u\xrightarrow{U}v\xrightarrow{V}\bar u\) with the edges in \(U\) colored \(0\), those in \(V\) colored \(1\). (Either list may be empty.) In \(Q_{k+1}\), start at \((v,0)\), traverse \(U\) in reverse along the lower facet from \((v,0)\) to \((u,0)\), cross the \(s\)-edge of color \(g(u)=0\), and traverse the *reverse of the \(Q_k\)-antipodal image of \(V\)* along the upper facet, from \((u,1)\) to \((\bar v,1)\). The upper edges have color \(1\oplus1=0\) by (12). Every coordinate appears once; the endpoints are antipodal, and every edge has color \(0\).

Conversely, take a full all-zero \(c\)-geodesic and reverse its traversal, if needed, so the unique \(s\)-edge crosses from \(z=0\) to \(z=1\), at some \(u\) with \(g(u)=0\). Let \(U\) and \(V\) be the ordered lists of the ordinary \(k\) directions before and after that crossing. Reversing the lower \(U\)-prefix gives a \(d\)-zero path from \(u\) to the original lower starting point. Applying \(Q_k\)-antipodality to the upper \(V\)-suffix, then reversing it, gives a \(d\)-one path from that point to \(\bar u\). Their concatenation is a valid full \(k\)-coordinate geodesic, with word \(0^{|U|}1^{|V|}\). This proves (13).

For any set \(S\subseteq Q_k\), the condition \(S\cap g^{-1}(0)\ne\varnothing\) for *every* antipodally odd function \(g\) is equivalent to \(S\cap\tau S\ne\varnothing\): if \(S\) contains an antipodal pair, precisely one of its two members has \(g=0\); if it contains no such pair, independently set \(g=1\) on all members of \(S\) and extend antipodally to the remaining pairs. Applying this with \(S=G(d)\), (13), and the normal form (12) proves (11). Finally, reversing a full geodesic changes a \(0^a1^{k-a}\) word starting at \(\bar u\) into a \(1^{k-a}0^a\) word starting at \(u\), establishing the same-root formulation. \(\square\)

**precise gap and certificate principle.** The 2-cp assertion \(B_k\) ensures only that \(G(d)\ne\varnothing\); the full unrestricted NORI1 assertion one dimension higher requires an *antipodally paired* pair of successful starts. Any underlying \(d\) for which \(G(d)\cap\tau G(d)=\varnothing\) would give an explicit counterexample to \(A_{k+1}\): choose an odd \(g\) equal to \(1\) on \(G(d)\) and use (12). Conversely, any failure of \(A_{k+1}\) yields a lower-facet \(d\) with this property. The reduction therefore retains every nonlinear NORI1 coloring and identifies the missing root-compatibility mechanism precisely. It is a dimension-by-dimension refinement of the established Leader–Long bridge perspective; it is not a proof of \(A_{k+1}\), nor a transfer theorem for ordinary boundary 3-tournaments.
