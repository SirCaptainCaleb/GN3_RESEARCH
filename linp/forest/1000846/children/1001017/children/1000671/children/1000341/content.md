# P-scale rotation-closure via deletable blocker endpoints

## Statement

Let H be a finite linear 3-graph and let P be a globally longest p-edge path. Conjecturally, the rotation component of P satisfies a Pósa-type p-scale expansion principle: if reachable terminal vertices repeatedly have degree above p, then repeated length-preserving rotations force either many distinct reachable terminal pairs or many distinct original private path vertices that are absent from some reachable maximum path. In particular, persistent failure of such closure should force terminal degree back to p+O(1), rather than the 2p scale of fixed-path contact counting.

## Body

The fixed-path contact method naturally exposes about 2p path vertices. The rotation route instead treats each path step as one exchange location.

The certified two-contact rotation a51a7f9cff95 and high-terminal-degree single-blocker expansion d71d4dd81a24 suggest the natural local threshold is degree p. The conjectural ingredient is closure across multiple maximum paths. Double contacts should be treated as paired blockers. A rotation replaces one old private path vertex by one new vertex; if a double blocker used the deleted private vertex, that edge loses one path contact relative to the rotated path and becomes a latent singleton exchange once its surviving contact becomes terminal in a reachable state. Because off-terminal contact pairs are disjoint by linearity, different deleted blocker endpoints expose different latent exchanges.

Track both reachable terminal pairs R(P) and the set D(P) of original private vertices omitted by at least one reachable maximum path. Seek a quantitative inequality showing that sustained degree excess over p forces growth of R(P) and/or D(P), while small closure forces degree loss.

Near-term targets: (1) exact one-step inequality from d(v)-p to distinct exchange locations; (2) characterize which doubles lose a contact under a legal rotation; (3) prove a monotone or amortized distinct-deletion statement; (4) convert to a Pósa-style boundary inequality for reachable terminal pairs.

The point is architectural: any useful theorem should genuinely exploit several reachable maximum paths. A bound provable on one fixed path alone risks returning to the old 2p-capacity ceiling.
