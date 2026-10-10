# Maximal good paths and snake exchanges

# Maximal geodesics, endpoint blockers, and snake exchanges

Let c be a binary coloring of physical ordered three-faces of Q_n satisfying c(bar F,rev pi)=1-c(F,pi). A direction-distinct k-edge path from x is a geodesic; its k-2 consecutive ordered-face colors are its window word. Call the path good when this word has at most one change. We establish the extremal consequences of a hypothetical failure of full antipodal good-path closure, then compare maximal monochromatic snakes.

## Longest good paths have two oppositely colored end walls

Assume no full good path exists. Let P=(p_1,...,p_k) from x to y maximize k among good paths over all cube roots and direction orders. We have k<n. For k>=4 write its window word q^s r^t, with positive s,t and q≠r, and put T=[n]\S, S={p_j}. Such a two-phase description is necessary: if P were monochromatic, appending any d in T would introduce one window and still produce a good path, contradicting maximality.

Set a=p_(k-1), b=p_k, alpha=p_1, beta=p_2. For every d in T,
c(F_y({a,b,d});(a,b,d))=q,
c(F_x({d,alpha,beta});(d,alpha,beta))=r.
Indeed the appended color must differ from the final r, while the prepended color must differ from the first q. Prepending uses starting root x xor d, so its remaining windows are literally the original faces of P. Thus extension at either end produces precisely two color changes, q^s r^t q or r q^s r^t. Antipodal reversal makes the corresponding incoming windows at bar y color r and those at bar x color q. This is a two-ended physical blocker theorem for all globally longest good paths.

## Monochromatic endpoint snakes

Independently let P=(u_1,...,u_(k-2),a,b) be a globally longest q-monochromatic path with k<n and used set S; write T=[n]\S and m=|T|. Every unused d has terminal cap c(F_y({a,b,d});(a,b,d))=1-q. Antipodal reversal supplies a q-monochromatic three-edge path (d,b,a) ending at bar y, with starting root h xor d, where h=bar y xor {a,b}. Consequently the m first-level roots form a physical cube star. For every pair d,e in T there are two actual four-edge paths (d,e,b,a) and (e,d,b,a) rooted at h xor {d,e}. Their last ordered three-face windows already have color q. Their respective first windows have colors c(F_h({b,d,e});(d,e,b)) and c(F_h({b,d,e});(e,d,b)). This gives an exact Johnson J(m,2) configuration of potential merging roots: the roots are indexed by unordered two-subsets, with distance two corresponding to Johnson adjacency. The first-window bits may be assigned independently in legal reversal-odd physical colorings, so the geometry alone forces no monochromatic merge.

For any A subseteq T, let r_A=h xor A. A q-monochromatic incoming path with direction order consisting of A followed by (b,a) witnesses that A is in the incoming snake family. The family contains every singleton and is accessible by deleting the first direction of a witness; it is not automatically a downward-closed family. Reversing antipodally identifies these witnesses with (1-q)-monochromatic paths from y beginning (a,b). The distinguished top root is r_T=x xor {a,b}. This is the only rank at which the root agrees with the translated original path in the standard complementary reversed-two-tail extraction.

## A conditional row-merging theorem

Suppose the q-monochromatic P above is globally longest of its color, k>=4, and |T|>=2. Put v=u_(k-2), w=u_(k-3), t=y xor {a,b}, and let alpha be the color of the genuine (w,v,b) seam after replacing the last pair (a,b) by b. For d in T let beta_d color the corresponding (v,b,d) seam. If alpha=beta_d=q, then for each e in T\{d} the path (u_1,...,u_(k-2),b,d,e) has all preceding windows q and final window gamma_de=c(F_t({b,d,e});(b,d,e)). Its length k+1 contradicts maximality if gamma_de=q; hence gamma_de=1-q. Antipodal reversal gives c(F_h({b,d,e});(e,d,b))=q. Together with the forced q-colored terminal (d,b,a) window, the actual four-edge path (e,d,b,a) from h xor {d,e} to bar y is monochromatic q. One admissible seam direction therefore certifies m-1 complete merge branches.

If instead alpha=q and every beta_d=1-q, consider the remaining seam (v,b,a). When it has color q, swapping the final two directions gives another q-monochromatic k-edge path with the same endpoints. When it has color 1-q, the shortened monochromatic prefix ending in b has a blocked terminal fan including a and all unused directions. This supplies a precise exchange alternative; maximality of the shortened prefix is an additional condition for iteration.

## Locality of adjacent direction exchanges

Swapping consecutive directions p_i,p_(i+1) preserves the root, endpoint and support. The prefix vertices coincide through step i-1 and from step i+1 onward, so every physical ordered three-face window beginning outside [i-2,i+1] stays identical. Thus only four consecutive window colors and their boundary comparisons require recertification. Conversely, there exist legal reversal-odd colorings in every n>=5 for which every insertion of a single missing direction into a specified near-spanning good word is bad. Any successful maximal-path argument must therefore prove progress using a family of genuine reroutings or a compatible complementary-support witness.

The open global step is a terminating exchange or equivariant incidence theorem for these physically rooted path families. The endpoint blocker laws, Johnson roots, and adjacent swaps provide exact inputs to such a theorem; none individually implies a full one-switch antipodal geodesic.

**All-dimensional obstruction to strict swap descent.** For every \(n\ge7\), a position-independent reversal-odd coloring can give the identity order and all \(n-1\) adjacent-swap neighbors the *same fully alternating* \(n-2\)-window word, while the odd-labels-then-even-labels order is monochromatic. The proof assigns alternating bits to ordered triples in the radius-one permutohedron ball, using the sum of the three labels to identify each window index; reversal consistency follows from the at-most-one-inversion property, and the monochromatic comparison order uses only triples whose numerical span is at least four. See the complete theorem and proof in *Maximal geodesic blockers and snake exchanges*. Since colors ignore roots, even arbitrary root changes accompanying one swap cannot ensure a strict defect decrease. A viable variational proof needs neutral sequences or a genuinely global potential.
