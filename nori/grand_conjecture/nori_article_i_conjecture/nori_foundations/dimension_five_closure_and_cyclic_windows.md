# Dimension-five closure and cyclic windows

**Theorem (dimension five, without symmetry).** Every binary coloring of ordered three-dimensional faces of Q_5 admits an antipodal geodesic for which the three consecutive length-three window colors have at most one change.

**Proof.** Suppose every such geodesic fails. Since there are exactly three windows, its color word necessarily equals 010 or 101. Fix distinct coordinate directions a,b,c,d,e in this order, and vary the starting cube vertex x freely. The color A of the first window (a,b,c) depends only on x_d,x_e. The color C of the third window (c,d,e) depends only on x_a,x_b, whose bits have been toggled before reaching that window. Since every corresponding path fails, A=C for all choices of the four independent bits. Thus both A and C are constant as their respective exterior bits vary. Since each ordered triple appears as the first triple of some coordinate order, the color c(F,(a,b,c)) is independent of which face F has free directions a,b,c. Write it as f(a,b,c).

For every order (a,b,c,d,e), failure now requires f(a,b,c)≠f(b,c,d). Apply this relation to the five cyclic rotations of (a,b,c,d,e). The five binary values f(a,b,c),f(b,c,d),f(c,d,e),f(d,e,a),f(e,a,b) must alternate around an odd cycle, an impossibility. Hence one path succeeds. □

For n=4 there are only two length-three windows, so the one-change requirement is automatic. The general n≥6 case remains open.
