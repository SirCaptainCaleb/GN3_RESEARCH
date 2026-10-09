# Three exterior sensitivities force dimension-six closure

Statement:
For an antipodally odd ordered-three-face coloring of Q_6, if there is an ordered coordinate triple (a,b,c) whose color is sensitive to each of the three fixed exterior coordinates d,e,f (sensitivity may occur at different exterior-bit assignments), then a good antipodal geodesic exists. Equivalently, in every counterexample each ordered triple has exterior Boolean-sensitivity support of size at most two. If a triple has sensitivity to two exterior coordinates, every orientation of its complementary free triple is face-independent.

Proof:
Assume every six-direction geodesic has at least two changes. Apply the antipodal endpoint-collapse theorem to sensitivity of (a,b,c) in d. There is K_d with c(def)=c(dfe)=K_d and c(fed)=c(efd)=1−K_d, all face-independent. Sensitivity in e yields K_e with c(edf)=c(efd)=K_e and c(fde)=c(dfe)=1−K_e; the overlap forces K_e=1−K_d, and the two conclusions together fix all six orientations of free set {d,e,f}. Consequently c(fde)=K_d while c(fed)=1−K_d. Sensitivity in f, however, would force c(fde)=c(fed) by the same endpoint-collapse theorem. Contradiction. The same argument applies under any relabeling and reversal; the witnesses to three sensitivities need not share the same outside-bit assignment.
