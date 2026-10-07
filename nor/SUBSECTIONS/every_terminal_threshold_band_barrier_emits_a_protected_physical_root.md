# Every terminal threshold-band barrier emits a protected physical root

## Metadata

- ID: every_terminal_threshold_band_barrier_emits_a_protected_physical_root
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 41
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

A maximal threshold-compatible band has a canonical barrier certificate. If a nearest boundary mismatch is flat, outward endpoint repair strictly increases the band length B. If no such repair is available, the supporting boundary tetrahedron is fully curved. Its two boundary windows still form an actual color transition; after color complementation/reversal normalize it to 10. Sliding from the first ternary window to the second drops the first boundary coordinate a and enters the fourth d, producing the protected physical root e_a-e_d.

Therefore flat combing and protected-root extraction fit into one dichotomy: enlarge B at a flat boundary, or emit a physical root at a full boundary. Accumulating emitted roots invokes the graphic-matroid alternative: each new root increases root-span rank or closes a signed coordinate circuit. Since rank is bounded, recurrent boundary repair reduces to circuit extraction rather than singleton-defect transport.

This does not yet close NOR: a graphic circuit need not have the positive/sign-compatible orientation required by the antipodal carrier. The remaining local/global interface is to extract a monotone protected bridge from the first compatible signed circuit, beginning with the A2 triangle case.

## Development

## Every terminal threshold-band barrier emits a protected physical root

Work in the coboundary-flat ternary sector with a one-change target and a maximal threshold-compatible interval [L,R] around its cut. Suppose an unresolved boundary remains after all available outward flat repairs. By the threshold-band normal form, its supporting tetrahedron is fully curved.

Consider a left boundary; the right boundary is symmetric. Let four consecutive coordinates be (a,b,c,d), with the boundary windows
alpha(a,b,c)=1-eta,
alpha(b,c,d)=eta,
where eta is the constant target color on this side. Thus the two consecutive windows form an actual transition.

After globally complementing colors if necessary, normalize this transition to
alpha(a,b,c)=1,
alpha(b,c,d)=0.
Sliding the ternary window one step drops a and enters d. Therefore the boundary carries the protected physical descent root
rho = e_a-e_d.

The root is supported entirely on the four-coordinate boundary packet, while every coordinate in the already matched interval and every coordinate beyond the protected outside boundary remains in its established relative order. Full curvature is not needed for the existence of rho; its role is exactly to certify that neither endpoint swap can absorb the transition and enlarge the threshold band.

Hence the threshold-band process has an exact handoff:

1. if the boundary tetrahedron is flat, repair it and strictly increase B;
2. if it is fully curved, retain the boundary transition as a protected physical root.

Now accumulate the roots emitted by successive full barriers. By the graphic-matroid rank lemma, every new root either increases the span rank of the retained physical roots, or closes a signed coordinate circuit relative to a spanning forest. Rank can increase only finitely many times.

Thus repeated Article III repair admits a two-level termination architecture: threshold-band length disposes of all flat mobility, and full-curvature stops feed a finite root-rank/circuit process. The remaining obstruction is no longer recurrent flat transport. It is the extraction of a compatible monotone bridge from the first signed protected-root circuit (with the A2 triangle as the first nontrivial case).

Caveat: an arbitrary graphic circuit is not automatically a positive Radon dependence. This lemma only proves the handoff to the signed-circuit problem; sign compatibility still has to be extracted from the carrier/provenance.
