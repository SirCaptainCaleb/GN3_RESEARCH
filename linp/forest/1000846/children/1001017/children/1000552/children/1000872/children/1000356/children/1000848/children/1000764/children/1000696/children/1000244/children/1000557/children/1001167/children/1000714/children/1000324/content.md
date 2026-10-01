# The one-low odd-central all-single state reduces to one terminal-low pattern

## Statement

Let q>=4 and p=2q-3. In the setting of a3a8412d2499, assume exactly one of four assigned charged all-single edges has rank q. Then the following hold.

(1) The low contact C=g_{q-2}∩g_{q-1} cannot be a visible entrance.

(2) The slot E=g_{q-1}∩g_q is unoccupied.

Consequently the sole surviving one-low/three-high all-single pattern is:
- the rank-q edge f_C has C as its opposite-terminal witness and its unique entrance off P;
- the three rank-(q+1) high contacts occupy exactly A,B,D.

## Body

By a3a8412d2499 the low witness is C.

First suppose C is the visible entrance of the rank-q edge. Then phi(C)=q-1. Since C=g_{q-2}∩g_{q-1} is a clean joint entrance, eac2e3da3eea forbids every other single contact whose first-contact cell is q-3; in particular A=g_{q-3}∩g_{q-2} is unavailable. Thus the three high contacts must occupy B,D,E.

But E cannot be a visible high entrance, because a clean entrance at E=g_{q-1}∩g_q would, by eac2e3da3eea, forbid the occupied C-contact. Therefore the E-edge h_E is terminal-only.

Write f_C for the rank-q low edge. Consider the reversed suffix
  g_p,g_{p-1},...,g_q,h_E,f_C.
There are p-q+1=q-2 inherited suffix edges, hence q edges total. The suffix meets h_E only at E, h_E∩f_C={v}, and f_C has no suffix contact because its sole P-contact C lies in g_{q-2}∪g_{q-1}, which are omitted. Thus the sequence is linear and ends in f_C through v. Since f_C is nonspecial of rank q and its unique entrance is C, this is a longest f_C-path through a wrong entrance, contradiction. Hence C cannot be the low entrance.

Now C is terminal-only for f_C, so the unique entrance of f_C is absent from P. If E were occupied, exactly the same argument applies: E cannot be a visible entrance because its clean-joint hole would forbid the occupied C-contact, so h_E is terminal-only, and the reversed suffix followed by h_E,f_C is again a q-edge path ending in f_C through terminal v rather than its absent unique entrance. Contradiction.

Therefore E is unoccupied. Since four contacts occupy four of A,...,E and C is the low contact, the three high contacts are exactly A,B,D.