# Corrected four-block one-detour antipodal path bound and Q11 obstruction

- Stable ID: note_article_xi_one_detour_monochromatic_path_20261012
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_xi_matroidal_turn_geometry
- Labels: rigorous, geodesicity-obstruction, matroid-duality
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6379_4
- Updated session: session_nori_r6379_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

**Corrected rigorous note.** A monochromatic antipodal path of length \(n+2\) need not begin with its repeated coordinate. Let its direction word be
\[
D\,i\,A\,i\,B\,i\,C,
\]
where the words \(D,A,B,C\) use pairwise disjoint subsets of the other \(n-1\) coordinates; \(A,B\) are nonempty, \(D,C\) may be empty. Put \(d=|D|,a=|A|,b=|B|,h=|C|\), so \(d+a+b+h=n-1\).

**Four-block replacement bound.** Every antipodally odd edge coloring \(c\) admitting this monochromatic antipodal path satisfies
\[
\boxed{\mu(c)\le\min\{U_A,U_B,2\lfloor(d+h)/2\rfloor\},}\tag{1}
\]
where
\[
U_A=\begin{cases}2\lfloor a/2\rfloor,&d=0,\\2\lceil a/2\rceil,&d>0,\end{cases}
\quad
U_B=\begin{cases}2\lfloor b/2\rfloor,&h=0,\\2\lceil b/2\rceil,&h>0.\end{cases}
\tag{2}
\]
The bound is dimension-independent and makes no assumptions on other edge colors.

**Proof.** View \(Q_n\) as two \(i\)-layers of \(Q_{n-1}\). The projection of the path follows a geodesic direction order \(D,A,B,C\). The original path uses layer zero for \(D,B\), layer one for \(A,C\), and three known monochromatic \(i\)-crossings. Build three antipodal geodesics in projected order \(D,A,B,C\), each using one of those original \(i\)-crossings:

- Cross after \(D\), starting in layer zero: only \(B\) is moved to its other layer; all other edges are known monochromatic.
- Cross after \(D,A,B\), starting in layer zero: only \(A\) is moved; the other edges are monochromatic.
- Cross after \(D,A\), starting in layer one: only \(D,C\) are moved, as two terminal blocks; the other edges are monochromatic.

An unknown block of \(k\) edges flanked by known zero edges yields at most \(2\lceil k/2\rceil\) switches. If it is terminal, its contribution is at most \(k\); two terminal blocks of sizes \(d,h\) give at most \(d+h\) switches. In an antipodally odd coloring, the cyclic root-rotation argument turns any odd switch count \(k\) into at most \(k-1\). This improves all terminal bounds to the even integers in (1)--(2).

**Dimension-eleven necessary shape.** For a hypothetical coloring of \(Q_{11}\) with \(\mu(c)>2\), if it has a monochromatic antipodal path of length \(13=n+2\), the four blocks necessarily satisfy
\[
\boxed{a=b=3,\quad d+h=4,\quad d,h\ge1.}\tag{3}
\]
Thus \((d,a,b,h)\) must be one of \((1,3,3,3),(2,3,3,2),(3,3,3,1)\). This follows by testing the necessary inequalities \(U_A,U_B,2\lfloor(d+h)/2\rfloor\ge4\) under \(d+a+b+h=10\). The same bound forces \(n\ge11\) whenever \(\mu(c)>2\) and a monochromatic antipodal path of length \(n+2\) exists.

**Relation to Article XI.** Wu--Yang (arXiv:2607.19276) proves existence of some monochromatic antipodal path, without controlling its length. A shortest weight-one monodromy turn cycle, after stationary contractions, yields a monochromatic antipodal path with length \(n+2q\). The present lemma constrains the first non-geodesic excess layer \(q=1\); no assumption that its path starts with direction \(i\) is permitted.

This note corrects an earlier discarded three-block argument that omitted the initial word \(D\). Do not cite the discarded dimension-eleven exclusion. The all-dimensional two-switch conjecture remains open.
