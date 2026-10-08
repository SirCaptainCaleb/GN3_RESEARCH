# Protection forces a minimum-hole boundary reservoir to be uniformly blocked

## Composition

(none yet)

## Development

## Protection and a minimum deletion set force a hole reservoir to be blocked

Let X be a minimum two-cover deletion set of H and let H-X=P|Q, with
\[
P=(z,z_1,z_2,z_3,\ldots)
\]
a tight path of order at least four. Let B subset X with |B|>=2. Suppose a protected face F has B as a free ordered-partition block whose last two positions are the first two positions of a selected left span-two window, followed by the fixed labels z,z_1,z_2,z_3. All other relevant blocks may be held fixed.

**Theorem.** For all distinct u,v in B,
\[
h(v,z,z_1)=1,\qquad h(u,v,z)=0.
\]
Thus the selected left word is 011 in every chamber, and the terminal-pair absence relation on B is empty.

**Proof.** The status immediately after the selected window is h(z_1,z_2,z_3)=1; its third status is h(z,z_1,z_2)=1. The inward span-two word starting one position later is therefore
\[
h(v,z,z_1),1,1.
\]
Protection excludes 011 there, so h(v,z,z_1)=1. Every v in B can occupy the last position of that free block, giving this identity uniformly.

If h(u,v,z)=1 for some ordered pair, then
\[
(u,v,z,z_1,z_2,z_3,\ldots)
\]
is a tight Hamilton order on V(P) union {u,v}. Together with the untouched Q it would two-cover H-(X-{u,v}) using |X|-2 deletions, contradicting minimality of X. Hence h(u,v,z)=0 for every ordered pair. ∎

**Corollary.** If |B|>=3, some chamber has a strictly farther left positive span-two occurrence. Indeed, put any three distinct block labels in its final three positions and choose their order with internal status 0 by boundary antisymmetry. The next status is h(u,v,z)=0 and the following one is h(v,z,z_1)=1. The outward start one position before the selected window has word 001. Therefore a no-farther-witness reservoir of this type has order at most two.

The mirror statement applies at the corresponding reversed right boundary.

## Consequence for carrier loops

A four-label terminal-pair cycle cannot lie wholly in a minimum deletion reservoir facing a fixed tight component of order at least four under these protection hypotheses. The same-face absence graph is empty before any topological argument is needed.

This explains why the carrier-loop branch and the blocked minimum-hole branch cannot be identified merely because both expose small supports. A surviving loop must involve labels outside that uniform minimum-hole reservoir, lose the fixed long tight boundary, or use a different face geometry. The Hamiltonian-five-support theorem supplies their common local object, but a global handoff must track these roles explicitly.

No minimum-counterexample assumption or disturbance argument is used; only minimality of the chosen deletion set, protection, and boundary antisymmetry.
