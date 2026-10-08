# Central two-layer normal form for arbitrary nonlinear radial NORI

CENTRAL TWO-LAYER NORMAL FORM FOR ORDERED-FACE HAMMING-RADIAL NORI.

Let n>=4. An ordered-three-face coloring is Hamming-radial when its value depends only on its ordered free triple pi and the number K of exterior coordinates equal to 1: c(F,pi)=g_pi(K), where 0<=K<=m=n-3. The NORI oddness condition is EXACTLY
 g_rev(pi)(m-t)=1+g_pi(t)
for every ordered triple pi and every t, where + is mod 2.

ODD DIMENSIONS. If m=2k, define a(pi)=g_pi(k). The NORI identity at t=k yields a(rev pi)=1+a(pi), so a is a reversal-odd coordinate-only coloring. For every fixed coordinate order p there exists a starting root with K_i=k for EVERY consecutive window; indeed impose x_(i+3)=1-x_i, which makes K constant, and select the three free initial chain bits to obtain K1=k. Consequently any one-change order for a yields a one-change NORI geodesic for c. This is an unconditional dimension-preserving reduction from Hamming-radial odd-dimensional NORI to coordinate-only reversal-odd NOR. The latter is also a subclass (take g_pi constant), so the universal conjectures for the two classes are equivalent in each odd dimension.

EVEN DIMENSIONS. Write m=2k+1 and define for each ordered triple pi two bits
 a(pi)=g_pi(k), epsilon(pi)=g_pi(k)+g_pi(k+1).
The NORI identity is EQUIVALENT ON THE TWO CENTRAL LAYERS to
 epsilon(rev pi)=epsilon(pi),
 a(rev pi)=1+a(pi)+epsilon(pi).
Thus switch flags epsilon are reversal-even. At epsilon=0 the lower central color a is reversal-odd; at epsilon=1 it is reversal-even.

Let pi_i=(p_i,p_(i+1),p_(i+2)) be the consecutive triples of a coordinate order p. Constant-central starts K_i=k exist, yielding color word a(pi_i). By the arbitrary-seam jump theorem, for every j=1,...,n-3 there are exactly 2 or 4 roots realizing K_i=k on windows i<=j and K_i=k+1 on windows i>j. At these roots the complete color word is EXACTLY
 W_i(p,j)=a(pi_i)+epsilon(pi_i)*1_(i>j).
The complementary roots realize the downward central jump and produce
 Wdown_i(p,j)=a(pi_i)+epsilon(pi_i)*1_(i<=j).
These formulas depend only on the two central layers, and remain true when the profiles g_pi(t) are nonlinear and completely unrelated away from those layers.

ALL-SWITCHER COROLLARY. If epsilon(pi)=1 for every ordered triple, then a is reversal-even. For every order whose a-word has r>=1 changes, choose any one of those change seams j: W(p,j) has exactly r-1 changes. In particular, existence of an a-order with at most two changes implies a one-change NORI geodesic; existence of an a-order with exactly one change implies a monochromatic NORI geodesic. Here the profile g_pi may vary ARBITRARILY with pi, subject only to its NORI pair identities and the central switch flag. This strictly enlarges the common additive Hamming-function family h(pi)+f(K).

MIXED-FLAG CERTIFICATE. More generally, for arbitrary epsilon, if there exist p and j for which the explicit word W(p,j) or Wdown(p,j) has at most one adjacent change, the arbitrary Hamming-radial NORI coloring admits the desired geodesic. This reduces the central-witness construction to a finite two-bit reversal-constrained ordered-triple problem. It is a sufficient certificate, not a proof that a good p,j always exists. In particular the all-zero flags include the open reversal-odd coordinate-only NOR case, and arbitrary face-position dependence is beyond the radial hypothesis.

CONSTANT-LAYER START JUSTIFICATION. Let L1,L2,L3 be the lengths of exterior index chains (4,7,...),(5,8,...),(6,9,...), summing to m. In an alternating chain of length L, its number of ones is either floor(L/2) or ceil(L/2). If m even, exactly zero or two chain lengths are odd, so k=m/2 is attainable. If m odd, exactly one or three lengths are odd, so floor(m/2) is attainable. This proves the constant-central start claim for both parity cases.
