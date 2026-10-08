# One-left A3 directed cycles have no long circuit

## Composition

Within one A3 block, size-one protected provenance imposes incompatible face-bit relations on consecutive directed endpoint roots. Therefore no directed physical cycle of length three or four can consist entirely of one-left A3 protected edges. The only size-one circuit is the opposite-edge two-cycle, already resolved by the boundary-safe one-left splice. Any unresolved protected A3 circuit must use two-left cut traces.

## Development

In one A3 block write the flat face bits as A=abc, B=abd, C=acd, D=bcd. For a canonical protected edge a to b whose cut trace in the block has size one, the two possible inserted-coordinate positions force the face pattern to be 1001 or 0110. Hence B=1-A. For a consecutive distinct edge b to c with the same size-one provenance, the two possibilities force 0011 or 1100. Hence B=A. These relations are incompatible. Thus a directed physical cycle of length three or four cannot consist entirely of size-one protected A3 edges. Only the opposite-edge two-cycle can remain, and the boundary-safe one-left splice already resolves that case. Therefore any unresolved protected A3 circuit must use the two-left cut trace.
