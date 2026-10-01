# At a trapped quadratic minimum a linear one-zero-one defect state is balanced or exposes a positioned four-window

## Statement

Let H be a boundary tournament with path-cover number greater than two. Let C=P|{x}|Q be a spanning three-cover that minimizes quadratic potential within its connected pairwise-repartition component, and suppose the concatenated ordering P,x,Q has exactly the linear 101 defect pattern. Write p=|P| and q=|Q|. Then either |p-q|<=1, or H contains the blocked-slide Hamiltonian four-path W of defect101_slide_or_fourwindow01, and H-W has the explicit inherited two-path cover supplied there. More precisely, if p>=q+2 then the left balancing slide must block immediately; if q>=p+2 then the symmetric right balancing slide must block immediately.

## Body

Assume p>=q+2. Apply the left alternative of defect101_slide_or_fourwindow01 to the displayed 101 ordering. If the slide blocks, that theorem gives the asserted Hamiltonian four-path W together with its explicit inherited complementary two-path cover, so we are done. Suppose instead the slide succeeds. By the bookkeeping in defect101_finite_transport01, the middle omitted label remains x and the shifted 101 ordering is the canonical concatenation P'|{x}|Q' of another deletion two-cover H-x=P'|Q', with |P'|=p-1 and |Q'|=q+1. Therefore C'=P'|{x}|Q' is obtained from C by one legal pairwise repartition of the displayed pair P|Q, so it lies in the same pairwise-repartition component. Its quadratic-potential change is
[(p-1)^2+1+(q+1)^2]-[p^2+1+q^2]=2(q-p+1),
which is strictly negative because p>=q+2. This contradicts the assumed componentwise Phi-minimality of C. Hence the left slide cannot succeed and must block. The case q>=p+2 is identical using the symmetric right slide. Consequently, if neither blocked-slide four-window occurs, neither inequality p>=q+2 nor q>=p+2 is possible, so |p-q|<=1.