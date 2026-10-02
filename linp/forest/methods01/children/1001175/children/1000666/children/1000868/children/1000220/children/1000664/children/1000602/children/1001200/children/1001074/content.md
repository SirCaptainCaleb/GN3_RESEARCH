# Lens-free flat terminal cycles have no lengths six, seven, or nine

## Statement

In the entrance-rail lens-free flat gap-one terminal-cycle setting of 315871ed0c8b, the cycle length c is not 6, 7, or 9. Together with 14bb137811b4, it is therefore not 5,6,7, or9.

## Body

Write
  V(R_j) intersect V(R_{j+3})={t_{j+2}}
for the unique distance-three intersections supplied by 8777d2ccd614.

If c=6, applying this once with j=i and once with j=i+3 gives
  V(R_i) intersect V(R_{i+3})={t_{i+2}}
and
  V(R_{i+3}) intersect V(R_i)={t_{i+5}}.
Thus t_{i+2}=t_{i+5}, impossible because these are distinct terminal vertices of the linear cycle.

Suppose c=7. Consider R_i,R_{i+1},R_{i+4}. Their three pairwise intersections are unique:
  V(R_i) intersect V(R_{i+1})={y_i}
by 960a5153b900,
  V(R_{i+1}) intersect V(R_{i+4})={t_{i+3}}
by 8777d2ccd614, and, since (i+4)+3=i modulo 7,
  V(R_{i+4}) intersect V(R_i)={t_{i+6}}
by the same lemma. By 8e3ab4a34ced the three unique intersections must coincide. This would give t_{i+3}=t_{i+6}, again impossible for distinct cycle terminals.

Suppose c=9. The three rails R_i,R_{i+3},R_{i+6} are pairwise at cyclic distance three, and 8777d2ccd614 gives the unique intersections
  {t_{i+2}}, {t_{i+5}}, {t_{i+8}},
respectively. By 8e3ab4a34ced these three vertices must coincide, contradicting the distinctness of the cycle terminals.

Hence c is none of 6,7,9. The exclusion c=5 was proved in 14bb137811b4.