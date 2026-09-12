# Unfragmented excess geometry

**Workspace:** D1
**State:** established
**Key:** `excess-f0`

**Summary:** When both X dimers remain contiguous, endpoint polarity and monotone Q contact order reduce all excess to repeated Q-cell use; sigma counts exactly those duplications.

Assume both X cells G_3,G_4 are contiguous T-blocks, but allow sigma>0. The fixed endpoint signs plus R518 force G_4 to be initial on its T-rail and G_3 terminal unless a labelled P4 already occurs. Outside the explicit R435 outputs, Q contacts on each rail are strictly increasing. Since each G_i for i=0,1,2 is a contiguous interval of Q, a given Q cell can occur at most once on each rail. Each X cell contributes exactly one T-block. Therefore any excess over the five baseline blocks comes only from a Q cell appearing on both rails. If k of the three Q source cells are represented on both rails, B=5+k and sigma=B-5=k. Thus sigma is exactly the number of doubled Q cells and lies in {0,1,2,3}; R862 gives t_G=3+sigma. This is R870. The conclusion is geometric: it records which physical Q cells are duplicated and retains the endcap roles. It is not merely the f=0 numerical specialization of R901.
