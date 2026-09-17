# Why order-eleven PORT rigidity does not lift directly to k=6

**Workspace:** D17
**State:** limitation
**Key:** `middle-layer-k6-port-fence`

**Summary:** Exact k=6 computational fences show that full six-set Hamiltonicity with no P7 can still support multiple ports at one five-core, including a fully uniform rigid K4 packet. This blocks direct padding or naive lifting of R957.

### 27. R957 local port rigidity does not lift to k=6

The accepted seven-vertex theorem R957 is genuinely special to k=5. There is an exact eight-vertex boundary tournament G on V={0,1,2,3,4,5,6,7} with all of the following properties simultaneously:

1. every one of the C(8,6)=28 six-subsets supports a Hamilton tight P6;
2. G contains no tight P7;
3. the five-core R={0,1,2,3,4} has several physical ports across its Hamilton endpoint completions. In particular completion 5 realizes ports 0,1,4, completion 6 realizes ports 0,1,4, and completion 7 realizes ports 0,1.

Thus the natural k=6 analogue of R957, namely ``every six-set Hamiltonian plus no P7 forces unique ports on every five-core', is false. In particular no proof of the general uniform-middle-layer theorem may obtain port uniqueness merely by restricting to a bounded (k+2)-vertex subsystem around one (k-1)-core.

Exact certificate. Enumerate the 168 complete-reversal pairs of ordered triples on 0,...,7 by scanning all ordered triples lexicographically and taking the first-seen representative of each pair (a,b,c)~(c,b,a). Bit 1 means this canonical representative is tight and bit 0 means its reversal is tight. The assignment is

000000110111100011100000010000111111011011000000111110001100000111110100111011111011101110110100000110011011110010000111000101001000100000010111011111001100110011100111

Independent exhaustive verification over all ordered tuples gives exactly zero P7s and at least one Hamilton P6 on every six-subset. On the displayed core R, the Hamilton endpoint-pair sets are:

R+5: {(0,3),(0,5),(1,3),(1,5),(4,5)}, so completion 5 has ports {0,1,4};
R+6: {(0,1),(0,3),(0,6),(1,6),(4,6)}, so completion 6 has ports {0,1,4};
R+7: {(0,7),(1,7)}, so completion 7 has ports {0,1}.

The model is a local fence, not a 13-vertex uniform-residue counterexample. It shows only that the R957 mechanism does not scale by bounded local port uniqueness.

A related k=6 diagnostic shows the general R929 exceptional rigid nucleus is also genuinely live locally. With common four-core M={0,1,2,3} and exterior labels 4,5,6,7, the five rigid supports indexed by K4-e edges 45,46,47,56,57 can coexist with no P7. An exact SAT instance with 408 variables and 44645 clauses is satisfiable; one model already has 23 of 28 six-subsets Hamiltonian. This does NOT decide the fully uniform K4-e packet, but it rules out any bare-nucleus generalization of the k=5 rigid-triangle argument.

The scalable information that remains is therefore circuit-valued. Accepted R929 still forces every missing chord of a minimum rigid Hall bicycle into switch/new-core geometry except the K4-e nucleus, and every PORT-SWITCH still yields two genuinely different inherited Hamilton orders on one (k-1)-core with named completion labels and named physical ports. The next parent theorem must consume those data through the factor-critical Hall circuit or another global uniform-layer synchronization; generic R435 output and bounded local port-rigidity are insufficient.

Status: the eight-vertex counterexample and its exhaustive checks are exact. The bare K4-e statement is an exact satisfiable diagnostic. No claim is made about the unresolved fully uniform k=6 K4-e packet or about order 13 itself.

#### Stronger k=6 fence: a fully uniform complete rigid K4 also survives

The preceding K4-e diagnostic can be strengthened all the way to the complete rigid K4 without losing local uniformity. There exists an exact boundary tournament on the same eight vertices with common core M={0,1,2,3} and exterior set U={4,5,6,7} such that:

* every one of the 28 six-subsets is Hamiltonian;
* there is no tight P7;
* for every pair u,v in U, EVERY Hamilton P6 on M+{u,v} has endpoint set exactly {u,v}.

After normalizing one actual order on M+{4,5} to (4,0,1,2,3,5), a lazy exact SAT construction reaches full uniformity after forcing only the supports that fail in successive models. Independent direct enumeration of the resulting 168-turn assignment verifies zero P7s, all 28 Hamilton six-sets, and the rigid endpoint pairs on all six U-edges. The canonical 168-bit turn assignment is

111110000000000101110111101100110111001000100111110000010100000000000000011111000000111001010000111101011111000111101010111000111000101000000111111000011011011101100110

The numbers of Hamilton orders on the six rigid supports are respectively 2,1,2,1,1,1 for edges 45,46,47,56,57,67; their endpoint-pair sets are exactly the corresponding exterior pairs.

This proves that even ``full local uniformity + complete rigid K4' is not a k=6 contradiction. Consequently the general R929 K4-e exception cannot be removed by a theorem confined to the natural eight-vertex packet. Any scalable consumer must use vertices outside M union U, or the whole Hall circuit / global uniform layer.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
