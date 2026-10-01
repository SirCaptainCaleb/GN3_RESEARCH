# Terminal-tail blocking pushes the flat terminal lens into the late high-rail zone

## Statement

In the minimal one-low high-rail lens state of 039d9d9cd8fd, on each high source rail Q_i of length q the low terminal u_0 lies in one of the final q-2 path edges, and every foreign high terminal u_j lying on Q_i lies in one of the final q-1 path edges. In particular the balanced terminal-terminal lens endpoints and the exterior high-terminal chord contacts are all excluded from the extreme early part of the high source rails.

## Body

Append the high edge e_i to its q-edge source rail Q_i and choose the common assigned terminal v as the last vertex. This is a longest path ending in e_i at v. Apply the certified terminal tail-blocker lemma c0798e59ef02 first with e=e_0, the low rank-q nonspecial edge terminal at v, and f=e_i of rank q+1. It forces the unique e_0 contact u_0 on Q_i into one of the q-2 edges immediately preceding e_i in the relevant suffix. Next apply the same lemma with e=e_j, j distinct from i, where e_j has rank q+1 and is terminal at v, and f=e_i. It forces the unique foreign contact of e_j on Q_i, equal to u_j in every reciprocal-terminal pair, into one of the q-1 edges immediately preceding e_i. These are exactly the stated late-zone localizations.