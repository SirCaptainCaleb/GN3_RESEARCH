# Generalize the P4 special-edge lemma to dense cores

## Statement

Try to prove the dense-core all-special conjecture by generalizing the source P4 special-edge mechanism: a nonspecial edge together with minimum degree >2ell/3 should force enough distinct path attachments to create an alternative longest-path entrance label, hence make the edge special or create P_ell.

## Body

The source linear_paths.tex contains a P4-specific lemma: if a vertex z has at least r incoming snake incidences, then every incoming edge at z is special. Its proof fixes a longest path ending at a candidate edge and uses many alternative incident edges plus linearity/pigeonhole to force a second terminal realization. For general ell and r=3, fix a nonspecial edge e={u,x,y}, where u is its unique longest-path entrance label, and a longest path P ending in e through u. Because x and y are valid terminal vertices, every edge through x or y that would otherwise extend P must attach back into P; linearity makes attachment witnesses within each star distinct. The proposed argument is to exploit delta(H)>2ell/3 to show the combined attachment pattern cannot remain compatible with unique entrance through u: either a detour creates P_ell, or two attachment patterns produce a longest induced path ending e through x or y. The ell=6, delta=4 equality witness shows any counting must use the strict excess above 2ell/3 and cannot prove the same statement at equality. Missing obligation: derive a rigorous attachment/rotation inequality with the sharp 2ell/3 threshold.
