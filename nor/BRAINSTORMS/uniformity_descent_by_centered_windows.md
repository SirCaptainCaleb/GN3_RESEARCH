# Uniformity descent by centered windows

Investigate whether higher-arity NOR implies lower-arity NOR. Throughout, N_k means coloring ordered k-tuples of consecutive cube vertices; k is tuple arity.


### Centered-subtuple descent with tuple-arity indexing

Throughout this note, (N_k) means the NOR conjecture for colored ordered (k)-tuples of consecutive cube vertices.

If (k-j=2s), every ordered (k)-tuple
[
(X_0,ldots,X_{k-1})
]
contains the canonical centered ordered (j)-tuple
[
(X_s,ldots,X_{s+j-1}).
]

Hence every (N_j)-coloring (chi_j) induces a candidate (N_k)-coloring by
[
chi_k(X_0,ldots,X_{k-1})
=
chi_j(X_s,ldots,X_{s+j-1}).
]
Complement-plus-reversal preserves this centered subtuple.

Along an antipodal geodesic, the induced (k)-tuple color word is the (j)-tuple color word with (s) entries deleted from each end. Thus a proof of (N_k) gives a lower-arity geodesic whose (N_j) word is one-change after deleting those boundary entries.

The unresolved issue is to absorb the boundary defects. In particular, (N_{j+2}) naturally projects to (N_j) after deleting one color at each end.

This note uses **tuple arity only**. If a translation-invariant reduction writes a coordinate label (h(v_1,ldots,v_r)), then (r=j-1) for an (N_j) coloring.
