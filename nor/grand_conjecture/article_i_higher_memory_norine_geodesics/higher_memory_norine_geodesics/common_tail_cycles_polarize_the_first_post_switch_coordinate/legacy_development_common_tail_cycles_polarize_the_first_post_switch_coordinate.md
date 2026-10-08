# Audit: tail truncation does not propagate switch polarization — preserved pre-item development

## Development

## Audit

The earlier version claimed that a common-tail deletion 3-cycle with tail word sigma^p(1-sigma)^q forces polarization at the first post-switch coordinate by truncating the final run to length one.

That argument is invalid when q>1. After truncation, the resulting coordinate set is a proper subset of the ambient minimum counterexample. Endpoint blocking and the assertion that every cyclic cut is bad apply to the full ambient counterexample, not automatically to the truncated restriction.

Therefore no first-post-switch polarization is established for q>1.

The q=1 case is different because no truncation occurs. It is valid and is proved independently on the full ground set in the audit/repair subsection and in the corrected singleton-final-run theorem.

This subsection is retained as a guardrail: any tail-shortening argument must explicitly preserve the full ambient vertex set or supply a separate reattachment theorem.
