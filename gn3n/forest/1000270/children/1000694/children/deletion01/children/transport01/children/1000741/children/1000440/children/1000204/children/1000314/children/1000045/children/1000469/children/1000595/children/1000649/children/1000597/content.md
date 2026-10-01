# Endpoint incidences force incompatible pairs or triangle-free compatibility edges

## Statement

Let H be a minimum counterexample on n vertices. Choose one deletion cover F_d of H-d for every d in V(H), and let G be the resulting full compatibility graph. Assume no anchor-endpoint compatibility triangle occurs, equivalently the endpoint four-kernel frontier of 93109600e88d never occurs. Let I be the number of incompatible unordered pairs of chosen deletion covers, and let Z be the number of compatibility edges of G that lie in no triangle. Then I+(2/3)Z>=n.

## Body

For each anchor d, apply c6b15d82c380. Since the endpoint-triangle frontier is excluded, either at least two of the four displayed endpoint labels are incompatible with d, or at least three are compatibility neighbors of d isolated in G[N_G(d)]. Partition the anchors into A, consisting of those with at least two incompatible endpoint incidences, and B=V(H)-A. Let E_I be the number of directed incidences (d,y) for which y is a displayed endpoint of F_d and F_d,F_y are incompatible. Then E_I>=2|A|. Every incompatible unordered pair contributes at most two directed endpoint incidences, so E_I<=2I and I>=|A|. Similarly let E_Z be the number of directed incidences (d,y) in which y is a displayed endpoint of F_d and is isolated in G[N_G(d)]. Then E_Z>=3|B|. Such an edge dy has no common compatibility neighbor and therefore lies in no triangle. Every triangle-free compatibility edge contributes at most two directed endpoint incidences, so E_Z<=2Z and Z>=3|B|/2. Hence I+(2/3)Z>=|A|+|B|=n.
