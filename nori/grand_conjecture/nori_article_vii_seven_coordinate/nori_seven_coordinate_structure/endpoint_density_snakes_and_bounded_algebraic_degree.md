# Endpoint-density snakes and bounded algebraic degree

# Endpoint-density snakes and bounded-degree physical NORI3

Let V be the n>=3 coordinate directions. Assume a binary coloring c(F,(u,v,w)) of genuine ordered physical three-faces satisfies **separate same-face reversal oddness** c(F,(w,v,u))=1-c(F,(u,v,w)). Combined with ordinary NORI antipodal-reversal oddness, this is exactly the boundary-compatible class with antipodal invariance. Antipodal invariance is not needed in our proof.

## Theorem 1: endpoint-density terminal-pair snake

Call an r-direction-distinct rooted cube geodesic *positive* when all r-2 consecutive ordered-three-face windows have color 1. Paths of length two are positive vacuously. A negative geodesic reverses to a positive one along the **same physical faces** under same-face reversal oddness; thus the maximal positive length L is the maximal monochromatic length.

For each unordered pair e={u,v}, define r(e) as the maximum number of coordinate moves in a positive geodesic ending in either ordered terminal pair uv or vu, over all possible starting roots and endpoints. Choose ONE maximizing orientation u_e,v_e. Let G_e be the set of cube endpoints y at which some positive r(e)-move geodesic ends with those ordered directions. Define the average maximizing-terminal endpoint density
\[
\delta=\binom n2^{-1}\sum_{e\in\binom V2}|G_e|/2^n.
\]
Then
\[
\boxed{\delta\,(n-1)/2\le(L-1)^2.}\tag{1}
\]
In particular, if a coloring has a longest monochromatic geodesic of order o(sqrt(n)), then its globally maximizing terminal-pair paths occupy o(1) of endpoint fibers **on average**, for every choice of maximizing orientations.

**Proof.** Orient each unordered coordinate pair e from u_e to v_e. For any cube endpoint y, retain only those arcs e for which y is in G_e. Averaging shows that some y retains at least delta*binom(n,2) arcs, and hence at that y some coordinate v has at least delta*(n-1)/2 incoming arcs. Group these incoming arcs u->v by their GLOBAL terminal maximum r(e)=r, defining U_r.

For u,w in U_r, both their chosen maximal positive geodesics (one ending uv and the other wv) can be realized at the SAME endpoint y. Consider the **single physical face** F_y whose free directions are {u,v,w}, and whose other exterior bits are those at y. Extending the uv path by w creates F_y with free-direction ordering (u,v,w); extending the wv path by u creates EXACTLY THE SAME physical F_y with reversed ordering (w,v,u). By same-face reversal oddness, precisely one of these extensions has color 1. Thus comparisons u->w iff c(F_y,(u,v,w))=1 form an ordinary tournament on U_r.

Choose u of outdegree at least (|U_r|-1)/2 in this tournament, and a positive maximal r-move path ending uv at y. Every outneighbor w MUST already occur among the first r-2 directions of this path; otherwise appending w produces an (r+1)-move positive geodesic ending in pair (v,w) at endpoint y XOR e_w, contradicting the GLOBAL maximum r({v,w})=r. Hence (|U_r|-1)/2<=r-2, or |U_r|<=2r-3. Summing from r=2 to L yields delta*(n-1)/2 <= sum_{r=2}^L(2r-3)=(L-1)^2. Every extension and comparison takes place on actual physical faces; no root or face identification is omitted. QED.

The same observation gives the classical Devine--Milans sqrt(n) snake theorem when colors are direction-only: each maximizing terminal sequence then works at EVERY cube endpoint and delta=1.

## Lemma: root multiplicity for low-degree Boolean equations

If f_1,...,f_t are Boolean polynomial functions on F_2^n of algebraic normal form degree <=d and have one simultaneous root with f_i=1 for all i, then they have at least 2^{max(n-dt,0)} such roots.

**Proof.** The simultaneous-satisfaction indicator P(x)=product_i f_i(x) is a nonzero multilinear Boolean polynomial of degree at most dt (reducing x_i^2=x_i). The classical Reed--Muller minimum-weight lemma asserts that a nonzero degree-at-most-D polynomial on n Boolean variables is nonzero at least 2^{n-D} times when D<=n, and at least once otherwise. An elementary proof writes P(x',x_n)=x_n Q(x')+R(x'). If Q=0 the support is twice the support of nonzero R; if Q!=0, for every x' with Q(x')=1 exactly one of P(x',0),P(x',1) is 1, and deg Q<=D-1. Induction supplies at least 2^{n-1-(D-1)}=2^{n-D} such x'. QED.

## Theorem 2: logarithmic geodesics under arbitrarily dense bounded algebraic degree

Suppose additionally that, for every ordered free triple pi, the color c(F,pi) is a Boolean polynomial of degree at most d in the actual n-3 fixed exterior coordinates of F, with no restriction on WHICH exterior bits appear and no support bound. Then the maximum monochromatic cube geodesic length L satisfies
\[
\boxed{2^{d(L-2)}(L-1)^2\ge(n-1)/2.}\tag{2}
\]
In particular, if d=0 the full sqrt(n) boundary-snake estimate holds; if d>=1 is fixed, then
\[
\boxed{L\ge\big(\log_2n-2\log_2\log_2n-O_d(1)\big)/d.}\tag{3}
\]
Thus arbitrary (possibly dense) affine exterior dependence d=1 forces an (1-o(1))*log_2(n) monochromatic geodesic for EVERY boundary-compatible physical NORI3 coloring. Degree two forces at least (1/2-o(1))*log_2(n). These are lower guarantees only, NOT matching examples; the universal sqrt(n) target remains open.

**Proof.** For every unordered pair e, choose ONE positive maximal r(e)-move direction sequence with the selected terminal orientation, along with one starting cube vertex where it is positive. Keep the direction order FIXED and vary its initial cube vertex x over Q_n. Its r(e)-2 actual physical ordered windows are Boolean functions of x of degree <=d: each exterior face state is x XOR a fixed previously traversed mask, restricted to the face's exterior directions, preserving degree. Their all-positive indicator is nonzero because of the selected successful root, and has degree at most d(r(e)-2). By the lemma, at least 2^{max(n-d(r(e)-2),0)} starting roots make ALL its windows positive. Translating the start x to its endpoint x XOR {all traversed directions} is a bijection. Therefore
\[
|G_e|/2^n\ge2^{-d(r(e)-2)}\ge2^{-d(L-2)}
\]
for EVERY pair e, whence delta>=2^{-d(L-2)}. Substitution in Theorem 1 yields (2). Taking base-two logarithms gives
d(L-2)+2log_2(L-1)>=log_2((n-1)/2),
and (3) follows by bounding the log(L-1) term with 2log log n+O(1), unless L is already greater than 2log n. QED.

## Structural fallout and precise limits

Equation (1) is an all-dimensional physical-root coherence criterion: if globally maximal positive terminal-pair paths have a constant-average density of possible cube endpoints, the Devine--Milans sqrt(n) path bound survives in full physical boundary-compatible NORI3. Failure of such a long-path bound requires significant localization of maximal terminal paths in the endpoint cube, not merely variation of local face colors.

Equation (2) yields a new algebraic-degree obstruction: if an adversarial boundary-compatible family had L=o(log n), its minimal maximum exterior algebraic degree would necessarily diverge. Quantitatively, for L>=3,
\[
d\ge\frac{\log_2((n-1)/2)-2\log_2(L-1)}{L-2}.
\]
This is logically independent of the existing near-linear **essential exterior support** barrier: a degree-1 Boolean function can depend essentially on n-3 exterior variables. The earlier sparse-support results give stronger polynomial paths if few variables are influential, whereas (2) gives nontrivial logarithmic paths when nearly all exterior variables participate but algebraic degree is bounded.

The result uses same-face reversal oddness essentially. It does not establish a universal logarithmic bound for unrestricted NORI3, nor a universal sqrt(n) bound for all boundary-compatible physical NORI3; a counterexample to the latter might already have degree one unless some further argument excludes it. The theorem provides a rigorous quantitative target for such an argument.

**Attribution:** The original complete boundary-tournament square-root terminal-pair count is due to Devine--Milans (supplied Scrapbook). The Boolean minimum-weight lemma is the classical Reed--Muller fact. The new mathematics is the endpoint-density lift to actual cube faces and its root-multiplicity transfer to globally supported low-degree exterior colorings.

**Checks:** Direct exhaustive evaluation of randomly generated legal affine boundary-compatible physical colorings in dimensions n=4,5,6 verified the endpoint-density inequality and the root-multiplicity claim, using actual physical exterior-bit evaluation. The proofs do not depend on these computations.

## Corollary: cube-translation symmetry and global coefficient rank restore square-root paths

Let H be a subgroup of the F_2^n translation group acting on Q_n. Suppose c(F+h,pi)=c(F,pi) for EVERY actual physical ordered face and h in H. Translating a globally maximizing positive terminal-path witness for any unordered pair e by all h in H preserves its positive colors and terminal order, while producing |H| DISTINCT ending cube vertices. Consequently the maximizing-endpoint density obeys delta>=|H|/2^n. The endpoint-density theorem gives
\[
\boxed{L\ge1+\sqrt{|H|(n-1)/2^{n+1}}.}
\]
If H has codimension at most t, this becomes
\[
\boxed{L\ge1+\sqrt{(n-1)/2^{t+1}}.}
\]
The coloring may be nonlinear and dependent on all exterior bits, provided its action under H is precisely invariant.

For a boundary-compatible affine physical coloring, express each ordered three-face color as b_pi+<A_pi,z(F)> with the coefficient vector A_pi extended by zero on the three free directions. If the linear span of ALL A_pi over every free triple and order has dimension t, take H=(span{A_pi})^perp. Every h in H preserves all physical face colors under translation, since <A_pi,h>=0. Thus the bound above applies: bounded GLOBAL exterior coefficient rank forces Omega(sqrt n) geodesics, even if individual coefficient vectors are dense and there is no bounded common coordinate support. This is a distinct condition from the support-size hypothesis; the general affine-degree-one guarantee remains logarithmic when the global coefficient rank is unbounded.

Proof uses exactly the same physical-fiber translation for every window, not just the abstract ordered direction triples. It does not settle square-root paths for arbitrary affine or nonlinear boundary-compatible colorings.
