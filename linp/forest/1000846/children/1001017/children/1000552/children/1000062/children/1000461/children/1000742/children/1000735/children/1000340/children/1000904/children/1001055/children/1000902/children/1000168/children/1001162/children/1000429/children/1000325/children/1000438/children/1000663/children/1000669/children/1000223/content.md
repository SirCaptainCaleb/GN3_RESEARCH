# Top centers pay in triangles or simultaneous source mass and lenses

## Statement

Let v be an active misaligned global-top center with phi(v)=L and eta_v=o(L). Use the interior switching cells on a chosen maximum L-edge host path as in 9586a4d2317f. Let s be the number of interior switchers, D the number of doubly occupied cells, and Y the number of paid/nonflat occupied cells.

Then at least one of the following holds:

(T)  D >= (1/16-o(1))L. In particular the host supports at least (1/16-o(1))L distinct switcher triangles.

(SL) D < (1/16-o(1))L, and simultaneously
  sum_{f in F_int} phi(x_f) >= (401/1024-o(1))L^2
and
  Y >= (1/16-o(1))L.
Hence, by 91f6c32ab805, the same host carries at least (1/16-o(1))L distinct top-potential balanced endpoint-lens attachments.

Thus every low-defect global-top center has either a linear switcher-triangle packet, or both a strengthened quadratic source-potential packet and a linear equal-top lens packet.

## Body

By b032348c1a8a, after deleting O(1) boundary contacts,
  s >= (5/8)L-eta_v-O(1)
    = (5/8-o(1))L.                                    (1)

Assume first that
  D >= (1/16-o(1))L.
Every doubly occupied cell gives one distinct switcher triangle by 9586a4d2317f, proving branch (T).

Now assume
  D < (1/16-o(1))L.                                   (2)

Apply the cell-dispersion source-mass theorem 98152151c212:
  sum_{f in F_int}phi(x_f)
  >= (L/2)s + floor((s-D)^2/4).                       (3)
Using (1) and (2),
  s-D >= (5/8-1/16-o(1))L
      = (9/16-o(1))L.
Hence (3) yields
  sum phi(x_f)
  >= (5/16-o(1))L^2 + (1/4)(81/256-o(1))L^2
  = (5/16+81/1024-o(1))L^2
  = (401/1024-o(1))L^2.                              (4)

Independently, the one-eighth payment theorem 9586a4d2317f gives
  D+Y >= (1/8-o(1))L.
Together with (2),
  Y >= (1/16-o(1))L.                                 (5)

At global top, 91f6c32ab805 converts these distinct paid cells into distinct top-potential balanced endpoint-lens attachments on the same host maximum path. This proves branch (SL).
