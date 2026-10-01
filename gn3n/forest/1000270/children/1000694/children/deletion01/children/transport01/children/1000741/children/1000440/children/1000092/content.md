# Some anchor has half-family incompatibility outside consecutive compatibility runs

## Statement

Let D be a set of m>=7 deletion labels with one chosen deletion cover F_d for each d, and let G be their full-compatibility graph. Assuming the exact Mantel bound e(G)<=floor(m^2/4), some anchor d has degree at most floor(m/2). Hence F_d is incompatible with at least m-1-floor(m/2)=floor((m-1)/2) other chosen covers. Moreover, among the compatible labels N_G(d), every connected component of G[N_G(d)] is a consecutive run on one of the two displayed paths of F_d. Thus relative to one anchor, at least half the family lies outside a union of one-dimensional full-compatibility runs.

## Body

The degree conclusion follows from averaging: if every vertex had degree greater than floor(m/2), the edge count would exceed floor(m^2/4). Choose d with degree at most floor(m/2); then its number of incompatible partners is m-1-deg(d), at least floor((m-1)/2). Apply the anchor-neighborhood run theorem 689b439cc429 to this d: each connected component induced by its compatible partners is exactly a consecutive run on one displayed anchor path. This packages the global density theorem into the geometry needed by defect-window transport: one anchor sees a linear incompatible population surrounding only one-dimensional islands of full compatibility.
