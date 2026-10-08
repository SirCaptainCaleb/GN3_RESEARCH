# Terminal-root four-paths are not forced by an unoriented endpoint theorem

## Composition

(none yet)

## Development

## An oriented terminal-root strengthening needs additional hypotheses

The correction in [[correction_seven_set_endpoint_absorption_needs_oriented_endpoints]] identifies the missing endpoint orientation. Under bare boundary-tournament hypotheses, the proposed universal terminal-root strengthening is false.

Let \(A\) be any boundary tournament and adjoin \(x\). For all distinct \(u,v\in A\), prescribe
\[
h(u,v,x)=0,\qquad h(x,v,u)=1.
\]
Choose the triples with \(x\) in the middle arbitrarily subject to boundary antisymmetry. These rules define a valid extension: they prescribe complementary values exactly on boundary-reversal pairs.

No tight path with at least three vertices can end at \(x\), because its final triple would be \((u,v,x)\), which is non-tight. Thus for a seven-set \(A\cup\{x\}\), with \(|A|=6\), there is no Hamiltonian four-side whose order ends at \(x\). The unoriented prescribed-endpoint theorem can only use \(x\) as an initial endpoint in this example.

This construction does not refute rooted surgery under the actual protected-witness/interface hypotheses. It shows that one cannot repair [[rooted_corridor_absorption_reduces_to_a_bounded_three_hook_residue]] by merely strengthening the quoted seven-set endpoint theorem for all boundary tournaments.

A valid rooted-interface lemma must either exploit additional relations forced by the selected witness and the frozen corridor, allow an orientation-adaptive repartition, or allow movement of the interface. Counting three unoriented path-neighbors does not guarantee even one terminal-root four-path.

The elementary concatenation criterion remains valid whenever a terminal-root path is actually available: if \(K=(k_1,k_2,t,x)\), \(T=(x,y,z,\ldots)\), and \(h(t,x,y)=1\), then \(K\) concatenated with \(T-\{x\}\) is tight. The missing step is producing \(K\) in that orientation under the relevant interface assumptions.
