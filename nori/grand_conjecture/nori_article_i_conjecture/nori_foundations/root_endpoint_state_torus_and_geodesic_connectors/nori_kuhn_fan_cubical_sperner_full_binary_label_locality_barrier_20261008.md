# Cubical Sperner forces all binary labels under one-bit locality; boundary-alone counterexample

# Cubical Sperner with 0–1 vector labels: a direct all-labels theorem and sharp local-regularity barrier

Research question: can existing fixed-point lemmas force COMPLEMENTARY n-bit labels rather than merely coordinatewise balance?

**Published direct theorem.** The cubical Sperner theorem with the neighborhood property, associated with Kuhn/Ky Fan, states: triangulation not required; let [0,M]^n be subdivided into unit n-cubes, label grid vertices lambda(v) in {0,1}^n, with
(i) lambda_i(v)=0 whenever v_i=0;
(ii) lambda_i(v)=1 whenever v_i=M;
(iii) if u,v are adjacent grid vertices, d_H(lambda(u),lambda(v))<=1.
Then some unit cell has ALL 2^n labels on its 2^n corners. Thus it has many complementary bit-string pairs. Source: Oleg Musin "Sperner type lemma for quadrangulations", arXiv:1406.5082, introduction attributes fully labeled cubes under neighborhood property to Ky Fan; L. Wolsey, "Cubical sperner lemmas as applications of generalized complementary pivoting", JCTA 23 (1977), 78–87; the detailed special formulation is also reviewed in the cubic variants of Sperner's lemma.

**Theorem (the 1-bit neighbor condition cannot simply be deleted).** For EVERY n>=2 there is a labeling of the 2^n small unit n-cubes subdividing [0,2]^n that obeys BOTH face-boundary rules (i),(ii), but NO small cube has all 2^n labels.

Construction. For every grid point t in {0,1,2}^n other than m=(1,...,1) set lambda_i(t)=1 iff t_i=2. Set lambda(m)=1^n. Boundary rules are immediate, because m lies on neither outer boundary face. Every cell C other than the "upper" cell [1,2]^n has at least one coordinate i in its low interval [0,1]. In C, only the central vertex m has label_i=1; every other corner has label_i=0. But a fully labeled cell would have 2^(n-1)>=2 different corner labels with ith bit one, impossible. The upper cell has all natural labels except 0^n, because its lower corner m has been relabeled 1^n, so it is not fully labeled. The local condition fails dramatically: neighboring vertices m and (0,1,...,1) have labels 1^n and 0^n, differing in n bits. This is a dimension-independent counterexample to the INCORRECT idea that boundary-face rules alone yield a fully labeled cell.

**NORI gap.** A target-bit or support-bit label selected from an actual reachable-target set need not satisfy (i) or (ii); the coloring's antipodal oddness instead relates REACHABILITY SETS by root complementation and color swap. Nor does any present result show that moving to an adjacent root/repair state changes a selected n-bit target by at most one coordinate. Cubical Sperner is thus unusually strong IF a geodesic-compatible, 1-Hamming-Lipschitz target selector with the correct face boundary rule can be constructed. Furthermore, a cell containing complementary labels is not automatically a connector certificate: one must show that its paired label vertices correspond to antipodal roots and a shared ACTUAL target, or to complementary used supports at one root, with jointly valid geodesics. An arbitrary bit-string label coincidence in a cell does not ensure these root constraints.

**Secondary routes.** Poincare–Miranda and cubical KKM prove a joint coordinate sign crossing, whose discretization without the neighborhood rule normally supplies only zero in convex hull / a neutral cell. Cubical Sperner with its neighborhood rule is the clearest currently established n-bit-label theorem that genuinely forces full opposite label pairs in dimension n.
