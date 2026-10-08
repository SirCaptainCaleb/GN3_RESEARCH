# Audit: late-blocker descent leaves m=0,1,2, not only m=1,2 — preserved pre-item development

## Composition

(none yet)

## Development


Correction to subsection 30.

There m denotes the number of successful one-rank singleton transports completed before the first t=1 full-flat blocker.

The strict estimate itself is correct: after resolving a blocker reached after m transports, every exported mismatch lies at rank at least j+m-2 relative to original defect rank j, so m>=3 gives strict outward progress.

However the list of exceptional short cases omitted m=0.

In the residual antipodal right exit, the relevant residual scan begins

1,0,0,...

on the consecutive old suffix pairs. If the next scan bit is 1, the initial singleton packet is already of full/flat type: the defect is blocked before any successful elementary transport. This is the m=0 case.

Therefore the correct remaining finite short-distance cases are

m in {0,1,2}.

Subsection 30 should be used only for its m>=3 strict-progress conclusion. The m=0,1,2 packets require separate boundary analysis.
