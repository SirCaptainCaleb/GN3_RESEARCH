# Actual good-window complex has a connected (Z2)^2 temporal-antipodal covering, with a mixed-cup criterion for grand closure

# Genuine good-window carrier has a connected four-sheeted temporal/antipodal voltage cover

Assume n≥5 and an active NORI coloring of actual physical ordered three-faces, with c(bar F,rev pi)=1-c(F,pi). Let W=W_good(c) be the finite simplicial complex whose vertices are ACTUAL ordered physical 3-face windows and whose simplices are finite window sets jointly contained in ONE actual at-most-one-switch geodesic. The antipodal physical reversal tau acts freely simplicially. Let Y=W/tau.

For any edge uv in W set beta(uv)=d_1(m(F_u),m(F_v)) mod 2, with physical face centers m. By the proved intrinsic distance theorem nori_good_window_set_complex_metric_parity_extension_and_full_span_edge_20261009, any simplex has a common actual good path and d_1 between two windows equals their INTEGER window-position separation on that path. Consequently beta is a genuine tau-invariant 1-cocycle: on each triangle at positions i<j<k the sum of the three edge distances equals (j-i)+(k-j)+(k-i)=0 mod2. Let beta_bar be its descended class in H^1(Y;F2). Write w for the first Stiefel–Whitney class of the actual two-fold cover W→Y.

**Theorem 1 (connected physical window-shift graph).** The 1-skeleton of W is connected, independently of the coloring. Indeed the actual ordered-window SHIFT graph H has one edge for each legal pair of overlapping ordered windows along a 4-edge path; every such path is admitted because it has only two color windows and at most one change. For each coordinate direction i, the induced window-shift graph H_i consisting of ordered windows whose free triple contains i and shift edges having i as one of the two middle directions is CONNECTED by the proved coordinate-retaining shift-graph lemma (Item nori_certified_square_complex_connected_antipodal_one_class_20261008). Any H_i and H_j share windows whose free triple contains both i,j; all windows belong to some H_i. Hence H, and therefore W, is connected.

**Theorem 2 (two independent literal holonomies).** The two degree-one cohomology classes beta_bar and w are LINEARLY INDEPENDENT in H^1(Y;F2). More concretely, the covering associated with the character pair
  pi1(Y) → F2×F2,
  [gamma] → ( <beta_bar,gamma>, <w,gamma> )
is SURJECTIVE. There exists a connected regular 4-sheeted cover of Y with deck group Z2×Z2, with a literal path/window lift model given below.

**Proof.** Fix any physical cube vertex z and any five distinct directions p0,...,p4 in cyclic order. Let u_i denote the ACTUAL oriented 3-face through z with free order (p_i,p_(i+1),p_(i+2)), indices mod5. Every consecutive pair (u_i,u_(i+1)) is realized on one genuine 4-edge geodesic and is thus an edge of W regardless of its two colors. These five edges form a LITERAL CLOSED PENTAGON in W. Each edge has physical-window center distance 1, so beta evaluates to 5=1 mod2 on that closed pentagon. This pentagon is a closed LIFT in W, hence its image in Y has w-voltage zero. It therefore witnesses the character pair (beta_bar,w)=(1,0).

Because the connected W is a free antipodal double cover of Y, some edge path P within W joins any chosen window u to tau u. Its image in Y is a loop with w-voltage 1 (lift changes sheets) and beta_bar-voltage epsilon∈F2, depending on P. Together the two loop voltages (1,0) and (epsilon,1) generate all of F2×F2. Thus the joint character pair is surjective and the classes are independent. \(\square\)

**Theorem 3 (explicit path-certified four-sheeted cover).** Form the beta-parity double cover of W as follows. Its vertices are ordered pairs (u,t) with u an ACTUAL physical window of W and t∈F2. Over any simplex σ={u_0,...,u_k} of W, include precisely its two lifted simplices with labels
  t(u_i)=h+beta(u_0,u_i) for some h∈F2.
The cocycle equation makes the lifting independent of the choice of base vertex u_0 and compatible on common faces. The beta-double cover is CONNECTED because W is connected and the literal pentagon has odd beta-voltage. Physical reversal lifts by
  tilde_tau(u,t)=(tau u,t),
while parity-deck change is
  kappa(u,t)=(u,t+1).
These commuting free involutions generate four deck transformations, giving a CONNECTED REGULAR cover
  (beta-cover of W) → Y
with deck group {1,kappa,tilde_tau,kappa tilde_tau}≅(Z2)^2, over each quotient-window vertex exactly four lifted windows. Every cell is the lift of a simplex already certified by ONE actual good geodesic: there are no invented geodesics or simplex fillings.

**Theorem 4 (three genuine nonzero one-classes and a conditional maximum-distance cup-product extraction).** Let alpha be the descended 1-cocycle with edge value
  alpha(uv)=beta(uv)+c(u)+c(v) mod2,
so on consecutive-window edges it is precisely the monochromatic-shift indicator. The cohomology identity from the good-window theorem gives [alpha_bar]=[beta_bar]+w. Since beta_bar and w are independent, the three classes w,beta_bar,alpha_bar are ALL NONZERO and distinct.

For r=3, if ANY homogeneous polynomial P(w,beta_bar) of total cohomological degree n−3 has NONZERO evaluation in H^(n−3)(Y;F2) — for example w^(n−3), beta_bar·w^(n−4), beta_bar^2·w^(n−5), or alpha_bar^(n−3) — then an actual full n-edge NORI geodesic with at most ONE change MUST exist.

**Proof of conditional extraction.** Under hypothetical grand failure every simplex of W comes from an actual admissible path with at most n−1 edges, hence at most n−3 windows and dimension at most n−4. Because the quotient by free simplicial tau has the same dimension, H^(n−3)(Y;F2)=0. Thus nonzero total-degree-(n−3) cup product forces an n−3-dimensional simplex in W, certified by at least n−2 distinct physical windows on ONE actual good geodesic. Since a direction-distinct path with n edges has at most n−2 windows, this certificate must be a FULL good antipodal geodesic. \(\square\)

**Why this is useful, and exact remaining gap.** The temporal/window-index parity and physical antipodal sheet-flip are two genuinely INDEPENDENT topological monodromies, present for EVERY coloring, with an explicit faithful fourfold lift. This does not by itself prove a NONZERO PRODUCT of degree two or higher: a wedge of two circles also has independent H^1 classes with all degree-two cup products zero. The new, mathematically precise topology-first closure target is to show that actual root/order/witness-incidence cells force ONE high-degree MIXED PRODUCT in the good-window complex quotient. Unlike a pure fixed-root Borsuk–Ulam index, such a product could simultaneously detect rooted progression and physical antipodal transport. The physical five-window Möbius band from Item nori_physical_five_window_mobius_band_pairwise_nonhelly_good_window_complex_20261008 realizes the beta-loop geometrically, while the global window-shift connectivity supplies the w-loop. Demonstrating nontrivial higher-dimensional cup products between these loops is the remaining global compatibility theorem, not yet established.
