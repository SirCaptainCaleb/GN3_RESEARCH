# Protected replacement and minimum first phase — preserved pre-item development

Sources: Article II §§190,192,193,200. The short-phase qualification below is necessary.

In a minimum coordinate counterexample, let O=(v_1,...,v_m) be a deletion good order with word 0^p1^q and omitted x. Assume p>=r. Replace coordinate v_p by x:
O'=(v_1,...,v_{p-1},x,v_{p+1},...,v_m).
Only the r windows starting at p-r+1,...,p change. All other coordinates retain their relative order, and the entire suffix of old one-colored windows is protected. If B denotes the replacement packet, the word of O' is 0^(p-r),B,1^q.

If B=0^a1^(r-a), 0<=a<r, then O' is a good deletion order with first phase p'=p-r+a<p. If p'=0, it is monochromatic and immediately extends to a good full order by the endpoint argument. If p'>0, it is a strictly shorter first-phase witness with a newly omitted coordinate v_p.

Choose a deletion good order minimizing p over all omitted coordinates and orientations, and normalize its phases to 0 then 1. Reversal oddness exchanges the phase lengths, so both ends participate in this finite minimum. Provided p>=r, a monotone replacement packet containing a one contradicts this minimum. Therefore the packet must be either 0^r or contain an adjacent 10 descent.

This extremal argument requires no iteration and no inherited scan for the newly omitted vertex. It preserves full support at the deletion level and explicitly changes which coordinate is missing.

Scope limitation. The full r-window formula requires p>=r. A general proof must either show that a minimum-first-phase witness has this property or resolve the cases p<r separately. A descent theorem available only for p>=r can stop in a short phase; availability on those states alone does not close arbitrary uniformity.
