# Corrected cube dictionary: unordered pole-crossing and ordered windows — preserved pre-item development

## Composition

(none yet)

## Development

### Corrected cube dictionary: unordered pole-crossing versus ordered windows

Let \(Q_V\) be the Boolean cube on \(V\). An antipodal cube geodesic
\[
G=(X_0,X_1,\ldots,X_n),\qquad X_n=V\setminus X_0,
\]
has length \(n=|V|\), hence flips each coordinate exactly once. Write
\[
X_{i-1}\triangle X_i=\{v_i\}.
\]
Then \((v_1,\ldots,v_n)\) is a spanning order of the boundary tournament. This observation does not require \(G\) to run from \(\varnothing\) to \(V\), nor does it require Boolean rank to be monotone.

There are two distinct cube representations and they should not be conflated.

#### 1. Unordered / bare-cube representation

If local colored objects are treated without traversal order, Boolean rank is the only ambient mechanism available to orient a local piece. Consequently a general antipodal geodesic cannot be read this way: its ranks may rise and fall repeatedly.

There is, however, an exact restricted situation in which the bare-cube picture again encodes the two path pieces. Mark each edge of \(G\) by \(+\) when it increases \(|X|\) and by \(-\) when it decreases \(|X|\). If this sign word has at most one change, then the geodesic necessarily passes through a Boolean pole.

Indeed, if the sign word is \(+^*-^*\), all coordinates outside \(X_0\) are added before any coordinate of \(X_0\) is removed, so the unique turning vertex is \(V\). If the sign word is \(-^*+^*\), the turning vertex is \(\varnothing\). Thus
\[
\boxed{\text{at most one rank-direction inversion}
\iff
\text{the antipodal geodesic passes through a Boolean pole}.}
\]

The two arms then use complementary coordinate sets. In the \(+^*-^*\) case the incoming arm orders \(V\setminus X_0\), while the outgoing arm orders \(X_0\); in the \(-^*+^*\) case the roles are reversed. Therefore, whenever the unordered local coloring is constant on each of the two arms with the two colors interpreted by boundary reversal, the two monochromatic geodesic components encode two disjoint tight paths whose supports partition \(V\). This is the natural bare-cube two-cover picture.

The restriction is essential: once a geodesic has two or more rank-direction inversions, no single Boolean-pole orientation canonically reads all local pieces, and local XOR or collision normalizations may change from window to window. Such corrections do not preserve the GN3 status word in general.

#### 2. Ordered 4-tuple representation

The ordered formulation has no such restriction. For every ordered four consecutive vertices
\[
(X_i,X_{i+1},X_{i+2},X_{i+3})
\]
of a cube geodesic, define its three coordinate directions by
\[
X_i\triangle X_{i+1}=\{u\},\qquad
X_{i+1}\triangle X_{i+2}=\{v\},\qquad
X_{i+2}\triangle X_{i+3}=\{w\}.
\]
Because the ambient path is geodesic, \(u,v,w\) are distinct. Attach the GN3 color
\[
C(X_i,X_{i+1},X_{i+2},X_{i+3})=h(u,v,w).
\]

Hence every antipodal geodesic, regardless of its starting vertex or rank profile, has ordered-window color word
\[
h(v_1,v_2,v_3),\,
h(v_2,v_3,v_4),\,
\ldots,\,
h(v_{n-2},v_{n-1},v_n),
\]
which is exactly the GN3 status word of the spanning order \((v_1,\ldots,v_n)\).

Thus
\[
\boxed{\text{every antipodal cube geodesic represents a spanning GN3 order}}
\]
in the ordered-window model. The distinguished bottom-up geodesics
\[
\varnothing\to V
\]
are only one complete slice of this representation, not the full family.

Reversing the ordered four-tuple sends \((u,v,w)\) to \((w,v,u)\), so boundary antisymmetry gives
\[
C(X_{i+3},X_{i+2},X_{i+1},X_i)=1-C(X_i,X_{i+1},X_{i+2},X_{i+3}).
\]
Cube complementation alone preserves the ordered direction triple, while complement-plus-reversal complements the color.

This corrects the earlier distinguished-pole intuition: varying antipodal endpoints do not create extraneous geodesics. Every antipodal geodesic already encodes a legitimate spanning order. What the memory-lift construction adds is an ordinary edge-colored lifted graph, not the first exact geodesic representation of spanning orders.

#### Consequence for the Norine analogy

There are therefore two different transfer targets.

- A bare/unordered cube-coloring argument can directly recover a two-cover from a suitably two-component antipodal geodesic only when its Boolean-rank direction has at most one inversion; the turning point is then automatically a pole and the two arms are the two path supports.
- An ordered-window argument may use an arbitrary antipodal geodesic. Its flip sequence is a spanning order, and the ordered four-tuple colors reproduce the GN3 status word without normalization.

Any topological argument that ranges over arbitrary antipodal endpoints should therefore be judged against the ordered-window model before it is dismissed as failing a distinguished-pole requirement.
