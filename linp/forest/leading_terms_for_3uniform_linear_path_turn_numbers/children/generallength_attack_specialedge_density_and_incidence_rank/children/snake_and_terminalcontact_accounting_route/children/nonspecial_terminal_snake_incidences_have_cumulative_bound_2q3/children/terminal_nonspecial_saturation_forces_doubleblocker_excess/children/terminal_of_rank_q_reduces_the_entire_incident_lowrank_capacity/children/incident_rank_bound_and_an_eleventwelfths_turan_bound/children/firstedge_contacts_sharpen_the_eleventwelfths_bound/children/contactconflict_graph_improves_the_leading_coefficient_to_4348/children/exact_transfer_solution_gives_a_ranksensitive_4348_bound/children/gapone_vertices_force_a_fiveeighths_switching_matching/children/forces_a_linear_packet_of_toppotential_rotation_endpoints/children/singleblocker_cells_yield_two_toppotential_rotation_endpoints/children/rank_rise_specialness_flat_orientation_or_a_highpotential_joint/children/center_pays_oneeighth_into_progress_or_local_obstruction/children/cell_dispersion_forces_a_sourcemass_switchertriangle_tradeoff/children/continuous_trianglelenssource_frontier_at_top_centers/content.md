# Continuous triangle-lens-source frontier at top centers

## Statement

Let v be an active misaligned global-top center with phi(v)=L. Use the interior switching-cell notation on a chosen maximum L-edge host path. Let s be the number of interior switchers, D the number of doubly occupied cells, Y the number of paid/nonflat occupied cells, and
  M_v=sum_{f in F_int} phi(x_f)
the total entrance-potential mass of the interior switchers.

Then, up to the absolute O(1) boundary loss already present in the switching theorem,
  s >= (5/8)L-eta_v-O(1),
  D+Y >= (1/8)L-eta_v-O(1),
and
  M_v >= (L/2)s + floor((s-D)^2/4).

Consequently, if eta_v=o(L) and d_v=D/L, then
  Y/L >= max(0,1/8-d_v)-o(1)
and
  M_v/L^2 >= 5/16 + (5/8-d_v)^2/4 - o(1)
whenever d_v<=5/8+o(1).

Thus a low-defect top center lies on a three-currency frontier: increasing switcher-triangle density D is the only way to reduce the cell-dispersion source mass, while until D reaches L/8 it simultaneously reduces but does not eliminate the forced paid-lens/output packet Y.

## Body

The lower bound on s is the dense-switching conclusion of b032348c1a8a after deleting O(1) boundary contacts:
  s >= (5/8)L-eta_v-O(1).                              (1)

The one-eighth paid-cell theorem 9586a4d2317f gives
  D+Y >= s-ceil((L-3)/2),
and substitution of (1) yields
  D+Y >= (1/8)L-eta_v-O(1).                            (2)

The cell-dispersion theorem 98152151c212 gives exactly
  M_v >= (L/2)s + floor((s-D)^2/4).                    (3)

Now assume eta_v=o(L), divide (2) by L, and put d_v=D/L:
  Y/L >= 1/8-d_v-o(1).
Since Y>=0, this is the displayed max form.

For the source mass, (3) is increasing in s whenever s>=D, which holds because every doubly occupied cell contains two switchers. Using s>=(5/8-o(1))L,
  M_v/L^2
  >= 5/16 + (1/4)(5/8-d_v-o(1))^2-o(1)
  = 5/16 + (5/8-d_v)^2/4-o(1).

No additional case split is used. The three quantities D,Y,M_v therefore obey one continuous local tradeoff curve.