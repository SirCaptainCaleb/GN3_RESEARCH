# A balance-minimal one-zero-one deletion state is balanced or exposes a positioned four-window

## Statement

Let H be a boundary tournament with path-cover number greater than two, fix a vertex x, and among all two-path covers H-x=P|Q choose one minimizing |P|^2+|Q|^2. Suppose the concatenated ordering P,x,Q has exactly the linear 101 defect pattern. Write p=|P| and q=|Q|. Then either |p-q|<=1, or H contains the blocked-slide Hamiltonian four-path W of defect101_slide_or_fourwindow01, and H-W has the explicit inherited two-path cover supplied there. More precisely, if p>=q+2 then the left balancing slide must block immediately; if q>=p+2 then the symmetric right balancing slide must block immediately.

## Body

Assume p>=q+2. Apply the left alternative of defect101_slide_or_fourwindow01. If the slide blocks, that theorem gives the asserted Hamiltonian four-path W and its inherited complementary two-path cover. If instead the slide succeeds, defect101_finite_transport01 shows that the omitted label remains x and the shifted ordering is the canonical concatenation P'|{x}|Q' of another two-path cover H-x=P'|Q', with |P'|=p-1 and |Q'|=q+1. Hence the fixed-deletion balance changes by (p-1)^2+(q+1)^2-[p^2+q^2]=2(q-p+1)<0, contradicting the minimal choice of P|Q. Thus the slide must block. The case q>=p+2 is symmetric. Therefore, if no blocked-slide four-window occurs, |p-q|<=1. No global three-cover minimality or ambient-order hypothesis is used.