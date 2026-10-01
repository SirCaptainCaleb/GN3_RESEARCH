# Minimum span three has a uniformly bounded cyclic defect certificate with only five run geometries

## Statement

Let H be a boundary tournament with path-cover number greater than two and let pi be a spanning ordering of minimum defect span three. Its cyclic defect graph Gamma has 3 to 6 edges and satisfies nu(Gamma-q)>=2 for every cyclic cut vertex q, with equality for the cut recovering pi. If Gamma is proper, nu(Gamma)=3. Relative to the linear span-three pattern, the only possible proper cyclic run multisets are {1,1,1}, {2,1,1}, {3,1}, {3,2}, and {5}; the only compatible full-cycle case is C5.

## Body

Cutting the cyclic order at q deletes exactly the two possible defect tests incident with q, so the linear defect graph of that rotation is Gamma-q. The defect-line identity gives c(pi_q)=1+nu(Gamma-q). Since H has no two-cover, every cut has nu>=2, while the chosen minimum-span ordering gives equality for one cut. As Gamma-q0 is a path-subgraph with matching number two, it has at most four edges; restoring q0 adds at most two, so |E(Gamma)|<=6. At least three edges are necessary, else deleting an incident vertex leaves matching number at most one. If Gamma is proper, writing its edge-runs r_j gives min_q nu(Gamma-q)=nu(Gamma)-1, hence nu(Gamma)=3. Therefore the run contributions sum to three, a uniformly bounded theorem-level case space. The original span-three ordering has linear defect pattern 101 or 111. Restoring only the two possible wrap edges and requiring deletion of q0 to recover that linear pattern leaves exactly {1,1,1},{2,1,1},{3,1} in the 101 branch and {3,1},{3,2},{5} in the 111 branch. If Gamma is a full cycle, the equality-two cut forces C5 or C6, and only C5 deletes to the required span-three linear pattern.
