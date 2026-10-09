# Fully rigid bichromatic hub can have every codimension-two projected-root chart bad simultaneously (even n≥8)

# Even full bichromatic-hub rigidity does not force a near-spanning good path in one chosen four-facet bundle

**Theorem (sharp local-packet no-go in all \(n\ge8\)).** For every \(n\ge8\), there is a **valid active NORI coloring** of physical ordered three-faces, a physical vertex \(z\), and a partition of the \(n\) directions into classes \(A,B\) with \(|A|,|B|\ge2\), together with fixed \(a\in A,b\in B\), such that:

1. At **every actual physical ordered three-face through \(z\)**, for every free direction order \((u,v,w)\), the color equals the **middle direction's class**:
\[
\boxed{c(F_z(\{u,v,w\}),(u,v,w))=\mathbf1_{\{v\in B\}}.}
\tag{1}
\]
Consequently \(z\) is a genuine bichromatic hub with **no incident doubly certified middle-square edge**. Every unordered direction pair inside \(A\) is a color-0 certified middle square at \(z\); every pair inside \(B\) is a color-1 certified middle square; every cross pair is uncertified at \(z\). This realizes the COMPLETE local selector of the positive dichotomy, not merely its cap values.
2. Put \(U=[n]\setminus\{a,b\}\) and let \(r=z|_U\). All four **uniform caps** from the positive theorem are present:
\[
c(F(x;\{a,b,i\}),(a,b,i))=1,\qquad
c(F(x;\{a,b,i\}),(b,a,i))=0
\quad(\forall i\in U,\ x|_U=r).
\tag{2}
\]
3. Nevertheless, in EACH of the four parallel \(U\)-facets, **every** full \(U\)-geodesic starting at the one projected root \(r\), regardless of its direction order, has **at least \(n-6\ge2\) ordered-face color changes**. Thus none of these four rooted facet charts contains even a *one-change* spanning path, much less a monochromatic one.

**Construction.** Write \(m=n-2=|U|\ge6\), and choose the physical hub \(z=0^n\). Pick any bipartition \(A\sqcup B=[n]\) with \(|A|,|B|\ge2\) and \(a\in A,b\in B\); write \(q(i)=\mathbf1_{\{i\in B\}}\). We assign the coloring separately on antipodal-reversal orbits of ordered physical faces. For a U-only ordered face (all three free directions belong to U), denote its omitted-coordinate fixed bits by \(t=(F_a,F_b)\in\{00,01,10,11\}\), and the number of its fixed U-coordinate bits equal to 1 by
\[
\rho(F)=\sum_{j\in U\setminus\operatorname{free}(F)}F_j.
\]

- In exterior facet \(t=00\), put
\[
c(F,(u,v,w))=
\begin{cases}
q(v),&\rho(F)=0,\\
\rho(F)\bmod2,&\rho(F)\ge1.
\end{cases}
\tag{3}
\]
Thus the physical faces *through \(z\)* have exactly the middle-selector pattern (1), while all other fixed-U-rank faces have parity color.
- In facet \(t=11\), define all U-only ordered-face values uniquely by the active antipodal-reversal law from the previously assigned \(t=00\) faces:
\[
c(F,\pi)=1\oplus c(\bar F,\operatorname{rev}\pi).
\tag{4}
\]
- In facet \(t=01\), assign \(c(F,\pi)=\rho(F)\bmod2\) on all U-only ordered faces; define \(t=10\) uniquely by (4) from \(t=01\).
- For any face having **at least one omitted direction free**, give its ordered-face color \(q(v)\) if the face passes through \(z=0^n\), and its NORI-required opposite value on the antipodal face through \(\bar z\). On every remaining free antipodal-reversal orbit, assign any arbitrary bit to one representative and its complement to the other.

These prescriptions are mutually compatible. The U-only cases have fixed omitted-coordinate bits, whereas the last case has at least one omitted direction free. The faces through \(z\) are exactly the faces whose fixed exterior coordinates are all zero; their antipodal mates have fixed exterior bits all 1, distinct since \(n\ge8\). Each active ordered-face involution orbit is paired freely and no orbit receives two contradictory prescriptions. Hence this defines a complete valid active NORI coloring satisfying (1).

**Rooted path calculation.** For each \(t\in\{00,01,10,11\}\), consider an arbitrary permutation \(p=(p_1,\ldots,p_m)\) of the \(U\) directions and its full geodesic from the root with U-coordinate bits \(0^m\) and omitted bits \(t\). It has \(L=m-2\) ordered-three-face windows. In window \(s\) (\(1\le s\le L\)), exactly its first \(s-1\) previously traversed U directions are fixed to 1 outside the three free directions, so \(\rho(F_s)=s-1\).

For \(t=00\), (3) gives
\[
w_1=q(p_2),\qquad w_s=(s-1)\bmod2\quad(2\le s\le L).
\]
The suffix \(w_2,\ldots,w_L\) strictly alternates, hence already contributes \(L-2=m-4=n-6\ge2\) color changes, independent of \(p\).

For \(t=11\), the active antipodal relation (4) sends a window of U-exterior rank \(s-1\) to a \(t=00\) face of exterior rank \(m-3-(s-1)\). For \(1\le s\le L-1=m-3\), the latter rank is positive, so (3) implies
\[
w_s=1\oplus\bigl(m-3-(s-1)\bmod2\bigr),\qquad 1\le s\le L-1.
\]
These first \(L-1\) bits strictly alternate, contributing \(L-2=n-6\) changes regardless of the last bit.

For \(t=01\), all L window colors are \(w_s=(s-1)\bmod2\), with \(L-1=m-3=n-5\) changes. Its antipodal paired \(t=10\) facet has the same alternating property by (4), again giving \(n-5\) changes.

Thus all four root/facet charts are bad, even while \(z\) realizes the complete genuine bichromatic mixed-selector field and its uniform caps. \(\square\)

**Scope and exact lesson.** This is NOT a counterexample to the full NORI conjecture: good full \(n\)-geodesics may start at other physical roots, and a different mixed omitted pair at \(z\) may admit monochromatic near-spanning cores. It refutes only the overstrong proposed intermediate assertion that *one fixed bichromatic hub plus one fixed cross-class omitted pair must yield a near-spanning zero/one-change path in its four parallel projected-root facets*. Any valid topological fixed-point route must exploit the **simultaneous incidence across many cross omitted pairs** (at least \(2(n-3)\) available at each locally separate bichromatic hub), or couple **different hubs and different projected roots** through genuine witness slides. Local labels in one four-facet chart alone do not force the desired complement collision.

## Stronger simultaneous-all-omitted-pairs countermodel (even dimensions)

**Theorem 2 (a fully rigid hub whose *every* codimension-two projected-root chart is bad).** In every EVEN dimension \(n\ge8\), there is a particularly simple valid active NORI coloring and a genuinely bichromatic, locally unique-colored hub \(z\) with the full middle-selector rule (1), such that **for EVERY unordered pair** of omitted directions \(\{a,b\}\subset[n]\), not only cross-class pairs, and for **all four** parallel \(U=[n]\setminus\{a,b\}\) facets based at the projected root \(z|_U\), **every** full \(U\)-geodesic has at least \(n-6\ge2\) ordered-face color changes.

**Construction.** Fix any bipartition \([n]=A\sqcup B\) with \(|A|,|B|\ge2\), put \(q(v)=\mathbf1_{\{v\in B\}}\), and take \(z=0^n\). For every physical three-face \(F\), write \(\rho(F)\) for the TOTAL number of exterior fixed coordinates assigned 1, so \(0\le\rho(F)\le n-3\). Give the ordered free triple \((u,v,w)\) the color
\[
\boxed{
c(F,(u,v,w))=
\begin{cases}
q(v),&\rho(F)=0,\\
\rho(F)\bmod2,&1\le\rho(F)\le n-4,\\
1\oplus q(v),&\rho(F)=n-3.
\end{cases}}
\tag{6}
\]
Because \(n\) is even, \(n-3\) is odd. Under face antipodality, \(\rho(\bar F)=n-3-\rho(F)\); reversing the free order keeps the same middle coordinate \(v\). Both interior parity values and the boundary values therefore complement exactly, so (6) obeys the ACTIVE NORI antipodal-reversal law on **all** ordered faces.

Every physical ordered face through \(z=0^n\) has \(\rho=0\), hence color \(q(v)\); thus **the complete mixed-selector field and local unique-color bichromatic hub** are realized at \(z\). Every monochromatic centered four-edge connector at \(z\) has both middle directions in the same class, and within each class every middle pair is certified in its unique class color. There are no doubly certified incident middle-square edges at \(z\).

Now fix *arbitrary* omitted \(a,b\), let \(U\) be the other \(m=n-2\ge6\) directions, and choose any of the four starting assignments \(t\in\{0,1\}^2\) on the omitted directions, with **all U-coordinates zero**. Along any full \(U\)-permutation-geodesic with \(L=m-2=n-4\) ordered windows, in window \(s\) the total exterior 1-count is
\[
\rho(F_s)=|t|+(s-1).
\tag{7}
\]
This is independent of the permutation because the \(s-1\) previously traversed U-directions are exactly the U-exterior coordinates set to 1; every untraversed U-exterior coordinate is 0.

- If \(|t|=0\), its last \(L-1\) window colors (indices \(s=2,\dots,L\)) are the consecutive parity bits \(1,0,1,0,\dots\), contributing already \(L-2=n-6\) changes. The first bit is the boundary middle-selector value \(q(p_2)\).
- If \(|t|=1\), all \(L\) windows have interior exterior rank \(1,\dots,n-4\) and hence alternate; their number of changes is \(L-1=n-5\).
- If \(|t|=2\), its first \(L-1\) window colors are the consecutive parity bits for ranks \(2,\dots,n-4\), contributing \(L-2=n-6\) changes. Its last window has the complementary boundary selector value \(1\oplus q(p_{L+1})\), which cannot remove those existing changes.

Thus **all \(4\binom n2\) projected-root codimension-two charts at this same hub** contain no full \(U\)-geodesic with fewer than \(n-6\) changes. In particular none has a one-change path for \(n\ge8\), despite exact local rigidity and uniform mixed caps for ALL cross-class omission pairs. \(\square\)

**Crucial strengthened conclusion.** Neither a *single* mixed omitted pair nor the ENTIRE family of mixed omitted pairs at one fixed bichromatic hub can supply a universal rank-(n-2) one-change or monochromatic connector theorem. This does NOT disprove NORI; other physical roots and hub-moving geodesics can still yield grand closure. It rules out a large class of stationary one-hub cubical fixed-point schemes. Any closure proof using these certificates must combine **genuine root motion across distinct projected roots**, higher-rank reachability packets, or antipodal global topology, not infer existence of a long good facet core from local hub data alone.


## Constructive full NORI closure for the stress-test coloring: mobile roots defeat all stationary barriers

Despite the exceptionally severe stationary-hub obstructions above, the explicit coloring (6) has a **full MONOCHROMATIC antipodal geodesic along EVERY prescribed direction permutation**, provided the starting root may be chosen to suit that permutation.

Fix an arbitrary full direction order \(p=(p_1,\ldots,p_n)\). Choose the starting cube bits \(x_{p_s}\in\{0,1\}\) by the six-periodic sequence
\[
(x_{p_1},x_{p_2},\ldots)=(0,0,0,1,1,1,0,0,0,1,1,1,\ldots).
\tag{8}
\]
Equivalently \(x_{p_s}=0\) for \(s=1,2,3\) and
\[
x_{p_{s+3}}=1-x_{p_s},\qquad 1\le s\le n-3.
\tag{9}
\]

Let \(\rho_s\) count the 1-bits among the **fixed exterior** coordinates of the \(s\)-th ordered-three-face window of the rooted full antipodal geodesic. Sliding the window by one direction moves coordinate \(p_s\) from free to traversed-and-fixed, contributing \(1-x_{p_s}\), and moves coordinate \(p_{s+3}\) from future-fixed to free, removing its original bit \(x_{p_{s+3}}\). Hence
\[
\rho_{s+1}-\rho_s
=(1-x_{p_s})-x_{p_{s+3}}
=0
\tag{10}
\]
by (9). Thus \(\rho_s\equiv\rho_1\) for all \(n-2\) windows. At the first window, the exterior fixed bits are exactly positions \(p_4,\ldots,p_n\). Positions \(4,5,6\) carry three 1-bits, and positions \(7,8\) carry two 0-bits, since \(n\ge8\). Thus
\[
3\le \rho_1\le n-5<n-3.
\]
All window ranks lie strictly between the two special boundary ranks \(0,n-3\). Consequently **every ordered window is governed by the ordinary parity middle case of coloring (6)** and has the same color \(\rho_1\bmod2\), regardless of its free-direction order.

Therefore every permutation of all \(n\) directions supports at least one full **monochromatic antipodal geodesic** for the stress-test coloring, even though at the special physical hub \(z=0^n\) all \(4\binom n2\) projected-root codimension-two charts have at least \(n-6\ge2\) color changes.

**Strategic conclusion.** This example vividly separates *stationary root restrictions* from global closure. The correct mobile-root coordinate recurrence (9) bypasses every fixed-hub cap obstruction. A topological proof must manufacture an analogous compatible global root choice (potentially via a Borsuk–Ulam/KKM carrier), rather than infer near-spanning success at a rigid physical vertex. The example now comes equipped with an explicit positive full-geodesic certificate and is unequivocally NOT a counterexample to NORI.


**Connection to the existing affine three-chain theorem.** The mobile-root recurrence (9) is the all-ones exterior-coefficient instance of Item \`nori_affine_exterior_three_residue_chain_eight_monochromatic_roots_20261008\`. The present coloring is not globally affine (the rank-0 and rank-(n−3) face-color rules are nonlinear/order-dependent exceptions), but the deliberately chosen roots keep **every** full-path window in the affine interior region, so the existing three-chain mechanism survives intact. This explains structurally why the severe all-omission stationary-root obstructions do not prevent monochromatic full antipodal paths elsewhere. It is a synthesis of the earlier linear forest solution with the new genuine bichromatic-hub stress test, not an independent claim that the all-ones affine theorem has been newly discovered.
