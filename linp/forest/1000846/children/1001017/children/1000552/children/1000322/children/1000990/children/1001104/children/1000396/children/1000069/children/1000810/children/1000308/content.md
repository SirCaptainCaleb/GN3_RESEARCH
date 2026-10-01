# Packet deletion has an exact effective-charge formula

## Statement

At exact density, for any vertex set S with charge K(S)=sum_{v in S}k_v and m_i(S) edges meeting S in exactly i vertices, the deficit after deleting S is r(H-S)=2d|S|-K(S)-m_2(S)-2m_3(S). Hence S is deficit-nonincreasing exactly when K(S)+m_2(S)+2m_3(S)>=2d|S|. Shared edges therefore act as packet charge.

## Body

Let H be an exact-density linear triple system:
  |E(H)|=d|V(H)|.
Use the equality charges
  k_v=3d-d_H(v).

Fix S⊆V(H), let s=|S|, and let m_i=m_i(S) denote the number of hyperedges meeting S in exactly i vertices, i=1,2,3.

Degree summation over S gives
  sum_{v∈S}d_H(v)=m_1+2m_2+3m_3.
On the other hand
  sum_{v∈S}d_H(v)=3ds-K(S),
where
  K(S)=sum_{v∈S}k_v.
Hence
  m_1=3ds-K(S)-2m_2-3m_3.

The number of edges deleted with S is
  |N(S)|=m_1+m_2+m_3
        =3ds-K(S)-m_2-2m_3.

Therefore
  |E(H-S)|
   =d|V(H)|-|N(S)|
   =d(|V(H)|-s)
      -[2ds-K(S)-m_2-2m_3].

Thus the deficit of H-S relative to density d is exactly
  r(H-S)=2d|S|-K(S)-m_2(S)-2m_3(S).               (1)

Consequently S is deficit-nonincreasing (indeed H-S still has density at least d) exactly when
  K(S)+m_2(S)+2m_3(S)>=2d|S|.                    (2)

For |S|=1 the shared-edge terms vanish and (2) is the vertex-charge target k_v>=2d. But for larger packets, edges meeting S twice or three times supply extra effective charge. This is precisely the mechanism by which matching/blocker structures can make a packet deletable even when no individual vertex reaches charge 2d.

In the top-two-layer exceptional state of 76c961f0dc48, taking S=T={phi=ell-1}, every ascending source edge from N=L_{ell-2} meets T in exactly two vertices and hence contributes one unit to m_2(T). Every hyperedge internal to T contributes two units to m_3(T). Thus the strong-rainbow matching system is simultaneously a packet-charge contribution in (2).
