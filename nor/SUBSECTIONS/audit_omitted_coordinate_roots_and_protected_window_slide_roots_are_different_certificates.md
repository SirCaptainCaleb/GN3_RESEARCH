# Audit: omitted-coordinate roots and protected window-slide roots are different certificates

## Metadata

- ID: audit_omitted_coordinate_roots_and_protected_window_slide_roots_are_different_certificates
- Parent Section: directed_nor_union_closed_bridge
- Position: 225
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Audit of the proposed antipodal-root desingularization. The current project uses two distinct root assignments which must not be conflated. In §§197 and 204, the protected topological certificate attached to a noninert replacement bridge B is the sum of window-slide roots e_{a_i}-e_{c_i}, where a_i is the physical coordinate dropped and c_i the coordinate entering as two consecutive r-windows crossing the replacement position slide by one. Every such bridge window contains the inserted coordinate x, and the replaced coordinate y is absent from the bridge. Hence these level-1 roots involve neighboring core coordinates; they are not the omitted-coordinate exchange root e_x-e_y. By contrast, §207 assigns e_x-e_y to the change of omitted coordinate in the flat replacement dynamics. That is a different bookkeeping root. Therefore the antipodal two-cycle x->y->x in §207 is not automatically an antipodal pair in the §197 Radon/root map. Subsection 224 incorrectly assumed that identification when calling rho=e_x-e_y a level-1 protected root zero. Its local geometric observation about breaking a pair of opposite vectors through an independent third vector is valid abstractly, but it has not yet been connected to the actual §197 root certificate. Likewise §220's suggestion that the flat antipodal/A2 cycles are exactly the minimal Radon zeros requires an additional dictionary theorem between omitted-coordinate exchange roots and protected window-slide roots. Until such a dictionary is proved, the modified-triangulation program should keep these root systems separate.

## Frontier

- Development version when composed: None
- Development version now: 1
