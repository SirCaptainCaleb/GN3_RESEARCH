# A well-founded potential orientation of a finite move component must have a sink

## Statement

Let G be a finite graph of three-cover states, and orient every legal move u-v from u to v only when a globally defined scalar or lexicographically well-founded potential satisfies F(v)<F(u). Then the resulting orientation has a sink: any vertex minimizing F has no outgoing edge. Therefore the no-sink orientation brainstorm cannot simultaneously orient moves by a genuine globally well-founded potential and prove that every trapped finite component has no sink. A viable cyclic orientation would have to abandon global potential monotonicity, while a viable potential proof must instead characterize and exclude its sinks.

## Body

The proposed route combines two incompatible mechanisms: global well-founded descent and sinklessness. On a finite state set, choose a state of minimum potential. Every outgoing oriented move would have to lower the potential further, impossible. Equivalently, a potential-induced orientation is acyclic and every finite acyclic digraph has a sink. Thus 'prove no sink, infer directed cycle, then contradict strict potential change around the cycle' cannot be implemented with one globally monotone potential. The route can be repaired only by changing its central mechanism: either use a non-potential local orientation and separately forbid cycles, or keep the potential and attack the structure of minimal states.
