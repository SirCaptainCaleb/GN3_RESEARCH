# Audit: local A2 scan constraints do not imply global scan monotonicity — preserved pre-item development


Audit correction.

A previous draft tried to deduce that each residual suffix scan in the recurrent flat A2 configuration is globally of the form 1*0* and that the three drop positions have the same parity.

That deduction is not established.

The existing companion-weave theorem, and the strengthened second companion weave, control only the tested boundary segment of the suffix. They do not by themselves propagate to arbitrary later suffix edges.

What is currently proved is local:
- all three residual scans have the recurrent front value required by the A2 packet;
- at the immediate tested suffix boundary, the strengthened companion weave forces the next two scan bits to be 00 for each residual coordinate;
- pairwise scan differences still satisfy the flat transport identity wherever defined.

To obtain global scan monotonicity one must first prove a recurrence-coverage lemma that transports an equivalent boundary-compatible weave to every later suffix pivot while preserving full support and the required A2 relations.

Therefore any theorem depending on globally single-step residual scans or same-parity drop ranks should be treated as conditional until such propagation is proved.
