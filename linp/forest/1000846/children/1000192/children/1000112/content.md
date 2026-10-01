# Current conjecture, proposal, and numerical-evidence map

## Statement

Index of the live unproved mechanisms, conjectures, computational evidence, and explicit fences currently relevant to improving the general 3-uniform linear-path upper bound.

## Body

AMBIENT REDUCTION. (0) Minimum-degree-first convention 0e6d8b412f43 and minimal-counterexample lemma fc68ffc8e4ea: for the exact 2/3 target, work from the outset under δ(H)>=floor(2ell/3)+1. Counterexamples below this threshold fence only unrestricted statements unless explicitly relevant to peeling.

PRIMARY LIVE CONJECTURES. (1) Global nonspecial-edge path-length inequality 76ef6efb21e7: if H has minimum degree δ, global longest path length L, and any nonspecial edge, then 3δ<=2L+2. This directly implies the dense all-special conjecture. (2) Dense minimum-degree all-special conjecture 020f694f8767: P_ell-free and δ(H)>2ell/3 implies every edge special. (3) Sharp ascending rank conjecture 482155a6ebaf: every ascending nonspecial edge satisfies φ(e)>=δ+1. (4) Minimum-degree local ascending-neighbor conjecture 4e1c498f922a: under the admissible threshold, at most three ascending edges e={x,v,u} at v have φ(u)>=φ(v). (5) Special-edge nullity conjecture 7305b7ec9d2a. (6) Maximum-rank nonspecial degree conjecture 73679d821853.

CURRENT BOUNDARY-ROTATION FRONTIER. (7) Endpoint-specific minimum-degree bound 1956950d4285 and corrected ascending bound b3f79b5fc50d. (8) Boundary q=δ saturated-fan chain e5859985e51b, 29164b69be06, 1dec5f7cee0a, 9e97d863f94d, 69cf1250bc2b, 116f9606cd05, 4eb4f83d2dd8, ee17956ece60, 22422f603de7, a2c7f4bc8f66. (9) Deficiency mobility 5f79968b85de and terminal-safe deficiency bound cfb1c467addb. (10) Short-loss normal forms 18fbfac7b953 and 87a6758ddc73: loss 2 cannot be terminal; loss 1 has only two explicit exceptional fan types. This is the sharp ascending-rank frontier.

NUMERICAL/STRUCTURED EVIDENCE. (11) d9ee4adc37d3: 13,406 systems; no nonspecial edge above δ/(L+1)=2/3; equality witness δ=4,L=5. (12) 8248fc8b6611 and d2fa3947be65: 12-vertex 5-regular P6-free packings are all-special; 500 distinct packings checked. (13) 09b3a90c50a9: 300 matching deletions from cyclic STS(13), minimum degree at least 5, all-special. (14) a3815355f23e and 37868c0561ad: nullity conjecture finite evidence.

IMPORTANT FENCES. (15) 7564e287447b: fixed δ=4 is insufficient; affine-plane boosters preserve ascending nonspecial edges while path length grows. Therefore minimum degree must scale with ell. (16) c3e95f4ce77d: δ=3 family with every edge ascending; it refutes unrestricted terminal/rank statements but lies outside the live admissible threshold. (17) Low-degree fences 830b0775567f, d5e0ab668a51, 783d197895f5, 439b3c1844c8, 61e82a9b70f5, 0c26080c83b0 all have minimum degree 1 and must not be used to reject a statement required only after the minimum-degree reduction. (18) 9db3de41493c: nonspecial incidence columns need not be independent. (19) 39c1795d6a26 and 6bea43f4bc16 are refuted conjectures; do not treat them as live routes.

LITERATURE. (20) 239a873dfa7a: Ma-Hou-Gao 2020 minimum-degree path theorem for general 3-graphs; useful methodology but thresholds are on the wrong kn scale for linear 3-graphs. (21) 1f8a29778c24 remains the general literature index.

New workers should fetch exact objects before relying on details, and should apply the minimum-degree-first convention before testing main-line conjectures.
