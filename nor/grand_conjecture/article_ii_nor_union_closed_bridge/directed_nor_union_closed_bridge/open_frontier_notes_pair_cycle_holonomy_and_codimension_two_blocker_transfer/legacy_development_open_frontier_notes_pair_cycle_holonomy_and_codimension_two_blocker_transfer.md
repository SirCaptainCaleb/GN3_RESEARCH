# Open frontier notes: pair-cycle holonomy and codimension-two blocker transfer — preserved pre-item development

Open research notes / adversarial frontier after the latest audits.

1. Pair-cycle holonomy for a pure three-circuit.
For a whole-front pure-orientation circuit U={a,b,c} attached to a sigma-monochromatic path P=(f_1,...,f_m), the tau-pair cycle on U is rigorously pinned at both endpoint pivots f_1 and f_m. Interior propagation is NOT proved. Therefore the correct adversarial picture is a loop of pair-tournament states along the pivots f_j: the state starts at a fixed directed 3-cycle and must return to the same cycle at the rear, but may wander through other tournaments in between. A promising closure route is to study the first excursion and first return. Any successful argument must preserve all consumed prefix/suffix coordinates; the earlier edge-flip propagation proof failed exactly by dropping f_1. One should seek a full-support surgery showing that the first excursion forces either a one-change spanning weave, a forced cyclic-wrap color, or a smaller front obstruction.

2. Codimension-two insertion strategy in the pure sector.
For a one-change carrier O, a single exterior vertex can realize the unique perfect blocking scan and defeat every one-vertex insertion. However two exterior vertices cannot both realize that same perfect blocking scan: identical scans force their mutual pair-color to be constant along O, and consecutive pair insertion at the switch yields a one-change extension. Thus in any codimension-two situation at least one omitted vertex must fail to be a perfect blocker. A possible induction is to choose a one-change carrier on V\{x,y} extremally, insert the non-perfect blocker in a gap minimizing disturbance, and then analyze whether the remaining vertex can become a perfect blocker relative to the enlarged carrier. If every such step merely transfers blocker status between x and y, the transfer itself should define a finite-state walk; parity or first-return may force a simultaneous-blocker state, which is impossible.

3. Exact flat-sector switching-class target.
When delta alpha=0, arbitrary coordinate orders are exactly directed Hamilton paths after a suitable vertex switching of the representing tournament. Hence the exact flat-sector problem is not a theorem about one fixed tournament but about the entire switching class: find some switched representative with a directed Hamilton path whose distance-two shortcut word has at most one change. Adversarially, a flat-sector counterexample must defeat this in every switched representative. This suggests using switching-class invariants rather than ordinary tournament condensation.

4. Pure-sector minimum obstruction size.
Two-element fixed-tail support circuits are impossible by alternation, so the smallest genuine pure-orientation support obstruction has size at least three. Consequently insertion-sliding in the pure sector cannot terminate at a shifted two-circuit; a failed internal transition must instead produce the centered-triangle/backward-blocker alternative (or the protected-front wedge at the first transition). This may make repeated insertion sliding more rigid in the pure sector than in the full reversal-odd setting.

5. Caution on curvature tubes.
The previously proposed full-curvature tube and explicit five-step weave depend on unproved pair-cycle persistence and must remain conditional. The safe endpoint facts are: one-step singleton propagation from the original front, and the same pair cycle at the rear pivot. Any future 'tube' argument should explicitly label which fibers are proved fully curved and which are conjectural.

These are working directions, not closure claims.
