# Near-minimal switcher source mass forces linear terminal retention on both host halves

## Statement

Let v be an active misaligned p-center with switching family
      F_v=X_v disjoint_union U_v.
    Write
      a=|X_v|,  k=|U_v|,  s=a+k,
    and let k_-,k_+ be the numbers of U_v contacts whose first host-path occurrence lies respectively strictly left and strictly right of the midpoint (p-1)/2 of the chosen maximum host path P_v.

Put
      M_v=sum_{f in F_v} phi(x_f),
    where x_f is the unique entrance of f. Then, up to an additive O(p) term,
      M_v >= (p/2)s + s^2/8
             + max{0, [(s-k)(3s-7k)+2(k_--k_+)^2]/16}.      (*)

Consequently, suppose eta_v=o(p), so s=(5/8-o(1))p, and suppose
      M_v <= (p/2)s+s^2/8+o(p^2).
Then
      k >= (3/7-o(1))s
and, more strongly,
      min{k_-,k_+}
      >= ((5-3sqrt(2))/14-o(1)) s.

Hence
      min{k_-,k_+}
      >= [5(5-3sqrt(2))/112-o(1)] p
      = (0.03379...-o(1))p.

Thus every low-defect center that avoids a fixed quadratic source-mass gain carries a fixed linear family of terminal-retained switchers on each side of its maximum host path.

## Body

The generic all-switcher bound a5066873364f gives
      M_v >= (p/2)s+s^2/8-O(p).                         (1)

The clean-retained bound 7e047fd40dd7 gives
      sum_{X_v} phi(x_f) >= (p/2)a+5a^2/16-O(p).       (2)

The left-right refinement e7b1762fb5c8 gives
      sum_{U_v} phi(x_f)
      >= (p/2)k+k^2/8+(k_--k_+)^2/8-O(p).             (3)

Adding (2) and (3), and using a=s-k,
      M_v
      >= (p/2)s+5(s-k)^2/16+k^2/8+(k_--k_+)^2/8-O(p)
      = (p/2)s+s^2/8
        +[(s-k)(3s-7k)+2(k_--k_+)^2]/16-O(p).         (4)
Taking the stronger of (1) and (4) proves (*).

Now assume M_v is within o(p^2) of the generic floor and s=Theta(p). Put
      t=k/s,
      d=(k_--k_+)/s.
From (4),
      (1-t)(3-7t)+2d^2 <= o(1).                        (5)
In particular t>=3/7-o(1). For t>=3/7, (5) gives
      |d| <= sqrt((1-t)(7t-3)/2)+o(1).                (6)

There are at most two midpoint contacts, so
      min{k_-,k_+}
      >= (k-|k_--k_+|)/2-O(1).
Dividing by s and applying (6),
      min{k_-,k_+}/s
      >= (1/2)[t-sqrt((1-t)(7t-3)/2)]-o(1).           (7)

On 3/7<=t<=1, the function on the right has its minimum at
      t_0=(15-2sqrt(2))/21.
Indeed, differentiating the square-root expression gives the equation
      63t^2-90t+31=0,
and the relevant root is t_0. At this point
      sqrt((1-t_0)(7t_0-3)/2)=sqrt(2)/3,
so the minimum value in (7) is
      (5-3sqrt(2))/14.

Finally s=(5/8-o(1))p under eta_v=o(p), yielding
      min{k_-,k_+}
      >= [5(5-3sqrt(2))/112-o(1)]p.
This proves the claim.