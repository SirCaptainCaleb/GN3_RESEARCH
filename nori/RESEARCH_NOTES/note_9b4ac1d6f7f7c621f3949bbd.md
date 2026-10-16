# Half-root antipodal geodesic theorem for switched three-exception reader stars

- Stable ID: note_9b4ac1d6f7f7c621f3949bbd
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, balanced, three-nonlinear, rootwise, antipodal-transport
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10003_3
- Updated session: session_nori_r10003_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let n=4+2r, r>=1, with directions a,b,c,u and W=P disjoint-union N, |P|=|N|=r. Put chi=(-1)^x_a. Choose ANY odd signed function L of exterior bits with L(bar w)=-L(w), and ANY even bit function k with k(bar w)=k(w). Set signed color rules s_a=L, (s_b,s_c)=(chi,-L) if k=0 and (-L,chi) if k=1, s_u=-chi, s_i=chi for i in P and s_i=-chi for i in N. The rules are independent of their own bits, antipodally odd and balanced. Up to three rules can be nonunary.

THEOREM. A zero full antipodal geodesic starts from root with a-bit t and W-state w if and only if L(w*)=+1, where w*=w xor P if t=0 and w*=w xor N if t=1. Consequently half of all roots are successful, independent of the nonlinear selector k. This closes the entire all-dimensions switched singleton-reader fringe class.

Proof of necessity: all P-directions have signed color chi and must occur while a=0; all N-directions and u have signed color -chi and must occur while a=1. Since a occurs once, at the a-step W must equal w*; hence its edge requires L(w*)=+1.

Proof of sufficiency when t=0: place P before a and N,u after a. If L(w)=-1, then at the starting root chi=+1 and -L=+1, so both b and c are red; traverse them first, then P,a,N,u. If L(w)=+1, traverse first whichever of b,c is assigned signed color chi under k(w), then P,a,N. At the final exterior state bar w, oddness gives L(bar w)=-1 and evenness preserves k, so the other exceptional edge has signed color -L=+1; traverse it, then u. In both cases the a-step is red because L(w*)=+1.

When t=1: place u,N before a, P after a. If L(w)=+1, then at the final exterior state bar w, L=-1 and chi=+1, so both b and c are red; place them after u,N,a,P. If L(w)=-1, first traverse whichever exceptional edge has signed color -L=+1; then u,N,a,P; at bar w oddness gives L=+1 and evenness preserves k, so the other exceptional edge, assigned chi=+1, is red and can be traversed last. All directions are used once, and all used edges have color zero. The root characterization is necessary and sufficient. As L is odd, it is positive on half the exterior states, giving half the roots.

Independent finite audit: all 256 odd L functions and all 256 even k functions on four exterior bits (65,536 Q8 colorings) obey the predicted root count 16 of 32 compressed root states; a separate program checked the rootwise equivalence in full Q8 on randomized functions. The theorem includes balanced three-nonlinear colorings for which every frozen four-face on a,b,c,u lacks a monochromatic full geodesic. Its mechanism is an antipodal endpoint transport, with L reversing and k preserved.
