# Audit a full ten barrier deletion exposes one additional crossing window — preserved pre-item development

## Composition

(none yet)

## Development

Audit of the claimed canonical deletion shadow for a fully-curved 10 barrier.

Let a longer coordinate order contain consecutive coordinates
(...,u,v,w,z,r,...)
with the fully-curved transition
alpha(u,v,w)=1,
alpha(v,w,z)=0.
Full curvature indeed gives
alpha(u,v,z)=0,
alpha(u,w,z)=1.

Deleting the third coordinate w does collapse the two displayed barrier windows (u,v,w),(v,w,z) to the target-zero window (u,v,z). However this is NOT the entire changed packet in a ternary sliding-window order.

The next old window
(w,z,r)
also disappears, and the deletion creates the new crossing window
(v,z,r).
Thus deletion of w changes at least the local packet
alpha(u,v,w), alpha(v,w,z), alpha(w,z,r)
into
alpha(u,v,z), alpha(v,z,r).

The full-curvature data on {u,v,w,z} determine only the first new bit alpha(u,v,z)=0. They give no value for alpha(v,z,r).

Indeed coboundary flatness on {v,w,z,r} gives
alpha(v,z,r)
=
alpha(v,w,z) xor alpha(v,w,r) xor alpha(w,z,r),
so even when the two consecutive old windows alpha(v,w,z), alpha(w,z,r) are both target-zero, the new crossing bit is the independent off-face alpha(v,w,r).

Therefore a fully-curved 10 barrier does NOT by itself have a target-compatible one-coordinate deletion shadow in a longer order.

Applied to the long stopped splice of root 135, a terminal barrier in the bounded prefix does identify a locally favorable interior deletion, but one additional crossing bit on the suffix side must be retained and checked. The omission-exchange problem of root 136 is consequently premature unless that crossing bit is controlled by the specific prefix provenance.

Safe corrected statement: deleting the third barrier coordinate removes the 10 transition itself and leaves at most one newly exposed suffix-side defect immediately beyond the collapsed packet. If the new crossing bit has the target color, the desired two-omission shadow is target-compatible; otherwise the deletion exports a single defect one step outward, which should be handled by a threshold-band or protected-replacement argument.

This audit does not challenge the exact three-barrier prefix extraction of root 135. It only corrects the claimed automatic target compatibility after deleting the third vertex of a terminal full barrier.
