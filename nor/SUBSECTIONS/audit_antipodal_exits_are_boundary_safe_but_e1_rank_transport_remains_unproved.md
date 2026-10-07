# Audit: antipodal exits are boundary safe but E1 rank transport remains unproved

## Metadata

- ID: audit_antipodal_exits_are_boundary_safe_but_e1_rank_transport_remains_unproved
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 32
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Audit: antipodal braid exits are boundary-safe, but later E=1 rank transport is not yet justified

This note separates the valid protected-exit results from the later singleton-defect transport claims.

### Valid direct antipodal exits

In the exact d=e=3 flat antipodal backtrack, subsection 20 gives two canonical protected exits from the caged braid cell.

If the left scan bit s=0, omitting b yields a genuine one-change deletion witness with the same outside order and threshold shifted two windows right.

If the right scan bit t=1, omitting c yields a genuine one-change deletion witness with the same outside order and threshold shifted one window right.

Because exact backtracking already forces q-p>=3, both shifts are strict phase-imbalance improvements under the protected phase-transfer trichotomy; their equality profiles cannot occur here.

In the residual caged state s=1,t=0, subsection 26 correctly proves that the two braid exits preserve the entire outside order on their protected sides. Subsection 19 correctly shows that each exit either closes NOR or exposes a transverse protected 10-descent root. The residual left and right roots avoid the inert exchange coordinates x,y, and subsection 8 shows that their quotient classes are nonzero and cooriented modulo <e_x-e_y>. Thus the antipodal root-pair zero has a genuine local codimension-one/root improvement.

### Unsupported later step

Subsections 24, 25, 28, and 30 subsequently use an asserted one-rank E=1 singleton-defect transport through a constant-color phase.

The only explicit local transport theorem found for that step is Article II subsection 177. But subsection 179 audits it: after the local swap, the next outer ternary window is reversed and changes color. The four-window packet is 0,1,0,0 -> 0,0,1,1, not a single defect shifted one rank. Therefore subsection 177 is only an internal five-set statement; it does not preserve the E=1 locus or the full outside-order threshold state.

No later boundary-preserving theorem has yet been identified that repairs this exported outer defect while proving the same monotone rank transport.

Consequently the reductions in §§24/25/28/30 to a t=1 full-flat blocker, and the m>=3 outward-rank potential, should be treated as unproved until such a boundary-safe transport lemma is supplied.

### Audited flat frontier

The g=1 A2 branch is eliminated by the protected q-minus-four witness plus phase-imbalance descent and the equality-case contradiction.

For the exact antipodal backtrack:
1. nonresidual scan states give genuine deletion-witness exits with strict phase-imbalance improvement;
2. the sole caged state s=1,t=0 has two genuine outside-order-preserving exits;
3. each residual exit either closes or gives a transverse protected root nonzero in the quotient by the inert root line;
4. those quotient roots are cooriented, so the antipodal local zero admits a zero-free local quotient fill.

The remaining combinatorial obligation is NOT currently a t=1 full-flat packet. It is to turn one of the two residual protected exits into a boundary-preserving threshold improvement, or otherwise prove a global protected-root carrier/extraction theorem in which the local quotient improvement is well-founded.

## Frontier

- Development version when composed: None
- Development version now: 1
