# One change and the width-one inversion relaxation

## Composition


NOR asks for a genuine one-change word \(0^*1^*\) or \(1^*0^*\). Article VII used a weaker nearby condition: with \(p\) the first \(0\) and \(q\) the last \(1\), \(q\le p+1\). This permits only a width-one mixed seam. It is not equivalent to one change, but it is a useful intermediate target because its failure has bounded local witnesses.


## Development


For a binary word \(w=\epsilon_1\cdots\epsilon_m\), a genuine one-change word is of the form
\[
0^*1^*\quad\text{or}\quad 1^*0^*.
\]
This is the target appearing in NOR.

Article VII repeatedly used a nearby but weaker condition. Fix the orientation \(1\to0\), let \(p\) be the first \(0\), and let \(q\) be the last \(1\). The inequality
\[
q\le p+1
\]
allows a width-one mixed seam: a \(0\) may be followed by a later \(1\), but only at adjacent status positions.

This relaxation should not be identified with NOR's one-change condition. It is nevertheless useful because it converts a global inversion condition into a finite local-witness problem and may serve as an intermediate target in ordered-tuple arguments.

The same construction can be applied after color complementation to the opposite orientation.
