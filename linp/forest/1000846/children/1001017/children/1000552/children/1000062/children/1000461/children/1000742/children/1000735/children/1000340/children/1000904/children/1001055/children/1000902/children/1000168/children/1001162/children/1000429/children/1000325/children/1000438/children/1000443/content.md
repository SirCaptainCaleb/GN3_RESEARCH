# Flat ascending rotation outputs with no endpoint rise land at aligned defect vertices

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, and let a single blocker through v have its unique precursor contact in an interior cell C_i, producing the standard rotation Q with last edge h=g_{i+2} and last vertex w=b_{i+2}. Then at least one of the following holds: (1) phi(h)>p; (2) phi(h)=p and h is special; (3) phi(h)=p and h is nonspecial nonascending; (4) phi(h)=p, h is ascending, and phi(w)>p; (5) phi(h)=p, h is ascending, phi(w)=p, and w is an active aligned vertex with q(w)=phi(w)=p. In case (5), for p>=8 the local defect eta_w of b032348c1a8a satisfies eta_w>=(5p-24)/8.

## Body

By the certified rotation-output decomposition 6205fe95ecf8, phi(h)>=p. If phi(h)>p, we are in (1). Assume phi(h)=p. If h is special, we are in (2). If h is nonspecial nonascending, we are in (3). It remains to consider the case in which h is ascending. The rotated path Q has p edges, last edge h, and last vertex w=b_{i+2}. Since phi(h)=p, Q is a longest h-ending path, so phi(h,w)=p. Thus w is terminal at h. Also phi(w)>=p. If phi(w)>p, this is (4). If phi(w)=p, then h is an ascending nonspecial edge of rank p terminal at w. Therefore the maximum rank q(w) of an ascending nonspecial edge terminal at w satisfies q(w)>=p, while always q(w)<=phi(w)=p. Hence q(w)=phi(w)=p, so w is active aligned, proving (5). Finally b032348c1a8a gives, at every aligned vertex of potential p>=8, eta_w>=beta(p)-ceil((3p-4)/4)>=(5p-24)/8.
