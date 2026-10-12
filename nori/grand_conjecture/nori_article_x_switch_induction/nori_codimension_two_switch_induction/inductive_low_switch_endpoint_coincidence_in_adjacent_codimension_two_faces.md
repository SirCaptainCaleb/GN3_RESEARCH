# Inductive low-switch endpoint coincidence in adjacent codimension-two faces

# Inductive low-switch endpoint coincidence in adjacent codimension-two faces

## Objective

Let \(c:E(Q_n)\to\{0,1\}\) satisfy \(c(\bar e)=1-c(e)\). Let \(\sigma(P)\) count the switches on a geodesic \(P\), and put
\[
\mu(c)=\min\{\sigma(P):P\text{ is a long geodesic in }Q_n\}.
\]
A long geodesic in a face traverses all of that face's free coordinate directions. The proposed program aims to prove \(\mu(c)\le 2\) in every dimension by induction.

Fix exterior directions \(a,b\), an \((n-2)\)-face \(F\), and its adjacent face \(F^a\). Seek long low-switch geodesics \(P\subset F\), \(Q\subset F^a\) terminating at *corresponding vertices* \(x,x^a\). The required structural advance is to **produce corresponding endpoints**; the final step follows from Article VIII.

## Proven gluing input

Theorem 10 in Article VIII (*Penultimate-Length Extension and Parallel-Face Endpoint Exclusion*) gives, if \(P,Q\) have respectively \(r,s\) switches,
\[
\mu(c)\le \max\{r,2\lceil s/2\rceil\}.
\]
By interchanging the faces,
\[
\mu(c)\le \min\left\{\max(r,2\lceil s/2\rceil),\max(s,2\lceil r/2\rceil)\right\}. \tag{X.1}
\]
Thus two long geodesics with at most two switches in adjacent codimension-two faces and corresponding terminal vertices force \(\mu(c)\le 2\). The terminal-square proof is preserved in Article VIII.

## Induction problem

**Candidate inductive step.** Starting with a single antipodally odd coloring of \(Q_n\), find adjacent codimension-two faces \(F,F^a\) carrying long geodesics of at most two switches with corresponding terminal vertices. Combining this assertion with (X.1) establishes the global two-switch bound.

Induction requires care: the restriction of an antipodally odd coloring to an individual face can be an arbitrary edge coloring and need not inherit antipodal oddness relative to that face. A successful induction should therefore strengthen the maintained hypothesis or work simultaneously with a family of parallel face restrictions. One may organize potential long-path endpoints by their minimum switch count and seek a corresponding pair through a geometric or topological intersection argument.

The endpoint-alignment claim is an open research target. No assertion about independently colored arbitrary faces is assumed here. The principal task is to exploit the coupled constraints inherited from the common ambient antipodally odd coloring.

## Status

**Established:** the dimension-independent parallel-face switch bound (X.1), with proof in Article VIII. **Open:** a mechanism furnishing low-switch long geodesics terminating at corresponding vertices in adjacent codimension-two faces. This is the proposed route to the universal estimate \(\mu(c)\le2\).
