# Universal fixed-hole states have a half-order support cap — preserved pre-item development

## Composition

(none yet)

## Development

Assume H has no two-cover and fix a vertex x in the universal branch of the fixed-hole Ky Fan theorem: every balanced bipartition of H-x has Hamiltonian sides, while adjoining x to either side is non-Hamiltonian. Let n=|V(H)| and r=floor((n-1)/2). Then every Hamiltonian support containing x has order at most r. Indeed, if a Hamiltonian path containing x had order at least r+1, a contiguous subpath of order r+1 containing x would exist. Removing x from that subpath gives a balanced-side-sized set R of non-hole vertices (size r when n is odd, and size r when n is even as well); the universal blocker property says H[R union {x}] is non-Hamiltonian, contradiction.

In particular, if n=2r+2 is even and x,y are two vertices both in the universal branch, use the universal balanced-partition theorem for hole x. Choose an r|(r+1) partition of V(H)-{x} with y on the (r+1)-side. That side is Hamiltonian and contains y, contradicting the support-size bound for y. Hence for even n at most one vertex can lie in the universal fixed-hole branch; every other vertex must admit an x-sparse unanimity face.

If n=2r+1 is odd and x,y are both universal, then for every partition V(H)-{x,y}=R sqcup S with |R|=r-1 and |S|=r, the three sets R union {x}, R union {y}, and S are Hamiltonian, while R union {x,y} is non-Hamiltonian (otherwise it together with S would two-cover H). Thus the odd-order two-universal residue is a universal pair-critical family: every (r-1)-set R accepts x and y separately but never simultaneously.
