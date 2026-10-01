# An order-preserving inherited-class shortcut forces two reciprocal support crossings

## Statement

Let R=(r_1,...,r_m) be one component of a displayed path cover J, and let T=P|Q be a path cover on the same vertex set. Assume that within each T-component the R-vertices occur in the inherited relative order. If T contains an ordinary edge r_i r_j with j>=i+2, then at least two ordinary edges of the displayed path R have endpoints in different T-components.

## Body

Because r_i and r_j are consecutive in one T-component while their inherited indices satisfy j>=i+2, every intermediate vertex r_{i+1},...,r_{j-1} lies in the other T-component: if some intermediate r_k lay in the same T-component, inherited relative-order preservation would force it to occur strictly between r_i and r_j there, contradicting that r_i r_j is an ordinary T-edge. Hence the component-label sequence along r_i,r_{i+1},...,r_j starts with the component containing r_i, takes the other label on every intermediate vertex, and returns to the original label at r_j. Therefore the inherited edge r_i r_{i+1} crosses the T support partition, and so does r_{j-1}r_j. These are distinct because j>=i+2.
