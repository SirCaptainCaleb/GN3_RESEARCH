# Every minimum counterexample has a spanning order with between two and nine changes — preserved pre-item development

## Every minimum counterexample has a spanning order with between two and nine changes

Assume a minimum ternary counterexample.

Take any bad full coordinate order \(\pi\), with first and last change positions \(p<q\), and outermost root
\[
D(\pi)=e_{v_p}-e_{v_{q+3}}.
\]

By §251, if the active interval is long, freeze the two extreme four-coordinate collars and replace the proper middle coordinate set by a NOR-good order. This preserves the same first and last changes and produces a full-order witness of the same outermost root with at most nine changes. If the active interval is short, the original witness already has at most seven changes.

Therefore the instance contains a spanning full order with at most nine changes.

Since the instance is a counterexample, every full order has at least two changes. Hence
\[
\boxed{2\le \min_\pi \operatorname{chg}(\pi)\le 9.}
\]

Moreover the upper bound can be attained inside a representative that preserves both extreme-change collars of an arbitrarily chosen outermost root.

### Consequence

The grand ternary closure problem no longer requires analysis of unbounded variation. Any minimum counterexample has a minimum-change witness in one of the eight finite variation levels
\[
2,3,\ldots,9.
\]

At level \(2\), §§254,257–260 reduce the problem to the full/full isolated-band regime and its bounded barrier attachments. For levels \(3,\ldots,9\), one may choose a minimum-change witness and normalize each long interior between extreme collars through proper-subinstance good orders without increasing the universal bound.

This finite-variation reduction is structural rather than computational: it follows only from minimum-counterexample induction and the ternary width of the two frozen collars.
