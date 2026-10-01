# A nonspecial terminal of rank q reduces the entire incident low-rank capacity

## Statement

Let H be a finite linear 3-graph and let h be a nonspecial edge of rank q≥2 with v terminal at h. Put J_q(v)={f∈E(H): v∈f and φ(f)≤q}. Then |J_q(v)|≤2q-3. For q=3 the stronger bound |J_3(v)|≤2 holds; for q=2, J_2(v)={h}. The counted edges need not be nonspecial or terminal at v. In particular, if q=φ(v), then d_D^-(v)≤2φ(v)-3.

## Body

Choose a longest q-edge path P=(g_1,...,g_q) with g_q=h and last vertex v. Since h is nonspecial and v is terminal at h, the unique entrance x=g_{q-1}∩h differs from v.

If q=2, any edge f≠h through v gives the two-edge path (f,h), entering h through v. This contradicts the unique entrance of h. Thus there is no such f, and J_2(v)={h}.

Assume q≥3 and put W=V(P)\h, so |W|=2q-2. Every f∈J_q(v)\{h} meets W: otherwise f meets P only at v, and appending f gives a path of length q+1 ending in f, contrary to φ(f)≤q. The contact sets (f\{v})∩W are pairwise disjoint, because all the edges contain v.

For q≥4 put C=g_{q-2}\g_{q-3}. This consists of the two possible last vertices of the prefix (g_1,...,g_{q-2}) and lies in W. We claim every f∈J_q(v)\{h} has a contact in W\C. Otherwise all its contacts with W lie in C. Since C is contained in the single edge g_{q-2}, linearity allows only one such contact, say w. Then
(g_1,...,g_{q-2},f,h)
is a q-edge linear path ending in h through v: f meets the prefix only at w, h is disjoint from that prefix, and f∩h={v}. This contradicts the unique entrance of h. The claim follows. Choosing a contact in W\C for each f gives an injection, so
|J_q(v)|-1≤|W\C|=2q-4.

For q=3 use C=g_1 instead. All three vertices of g_1 belong to W. If f had contacts only in C, linearity would again leave a single contact, and (g_1,f,h) would be a three-edge path entering h through v. Thus all f≠h meet W\g_1, a set of size one, giving |J_3(v)|≤2.

Finally, when q=φ(v), every snake-incoming edge at v has rank at most q and belongs to J_q(v). This proves the last assertion.

The proof counts all low-rank incident edges. This distinction is essential: the two forbidden contact vertices cannot be occupied by a singly contacting special edge either, since it is the nonspeciality of the fixed last edge h that supplies the contradiction.