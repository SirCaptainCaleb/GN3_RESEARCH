# A good shore order with compatible far ports has a fully ported canonical zero path

## Composition

With compatible far ports and all cited path endpoint edges defined, the three canonical cuts guarantee at least one fully ported zero path among six candidates. Short or degenerate paths require separate treatment, and the conclusion does not guarantee two fully ported paths belonging to one cut.

## Development

Let O=(a_1,...,a_k) have ternary word 0^p1^q. Write t_i=1 when a_i->a_{i+1} in the fixed shore tournament. For cuts j=p,p+1,p+2, the prefix zero path P_j has first port t_1 and last port t_{j-1}; the reversed-suffix zero path Q_j has first port 1-t_{k-1} and last port 1-t_{j+1}. Assume the far ports are compatible: t_1=1 and t_{k-1}=0. If none of P_p,P_{p+1},P_{p+2} were fully ported, then t_{p-1}=t_p=t_{p+1}=0. If none of Q_p,Q_{p+1},Q_{p+2} were fully ported, then t_{p+1}=t_{p+2}=t_{p+3}=1. These conclusions contradict at t_{p+1}. Hence at least one of the six canonical zero paths has both endpoint edges forward.

Elevation audit: the indexed port argument assumes all cited endpoint edges exist and each candidate path has enough vertices to have two exposed ordered pairs. Short phases and degenerate paths require separate treatment. Even one fully ported canonical path does not establish that both paths of one cut are fully ported.
