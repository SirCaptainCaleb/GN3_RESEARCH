# Separation is valid on the minimum-first layer but does not yet control terminal band roots

## Metadata

- ID: the_separation_potential_is_valid_on_the_minimum_first_johnson_layer
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 72
- Row version: 2
- Development version: 2
- Composition version: 1
- Composition stale: False

## Composition

On the fixed minimum-first p-layer, Gordan separation is rigorous: either the canonical roots positively depend or a functional w yields a cut potential Phi strictly decreasing along every forced canonical Johnson successor. A Phi-minimal realized cut therefore has a missing successor. This does not directly control terminal threshold-band roots, which may lie far from the p-cut. The missing interface is canonical-to-terminal provenance, repaired for terminal states by their own graded central cuts rather than by pretending they stay in the original layer.

## Development

Let p be the globally minimum possible FIRST-phase length and restrict to normalized witnesses with displayed word 0^p1^q. Their canonical switch-insertion roots cross the physical first-p cut, so the finite alternative applies on one Johnson layer.

Either there is a positive dependence among chosen canonical roots, or there is a functional w with w(rho)>0 for every chosen canonical root. In the separating case the cut potential
Phi(L)=sum_{u in L} w_u
strictly decreases along each forced canonical Johnson successor L^+=L-{a}+{c}. Hence a Phi-minimal realized p-cut has an unrealized forced successor.

This is rigorous and needs no antipodal symmetry.

However it does NOT yet combine directly with threshold-band maximization. Threshold-band combing may transport an exported mismatch far away from the original normalized switch. A terminal fully-curved band barrier then produces a physical slide root whose four supporting coordinates may all lie on one side of the original p-cut. Such a terminal root need not be one of the canonical cut-crossing roots controlled by w, and it need not define a Johnson successor of the Phi-minimal cut.

Therefore the lexicographic pair (Phi,-B) is not yet a single well-founded potential on one common root class.

The corrected separating frontier has two stages:

1. Canonical stage: at a Phi-minimal minimum-first witness, every chosen canonical root points toward an unrealized lower-Phi Johnson neighbor.

2. Transport stage: flat threshold-band repairs can comb local defects outward, but if they terminate at a fully-curved barrier one must still prove a provenance bridge connecting that barrier back to a canonical cut-crossing root, or attach a legitimate local cut and work in a graded cut space.

A closure theorem must therefore show one of:
- terminal barrier transport preserves/recovers the original canonical root and cut;
- a terminal barrier can be pulled back through the flat combing path to realize the missing canonical neighbor;
- or the graded local-cut roots themselves force a positive dependence incompatible with the separator.

The separation theorem is valid; the missing theorem is the canonical-to-terminal provenance bridge.
