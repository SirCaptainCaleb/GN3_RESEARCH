# Near-minimum average potential forces simultaneous near-saturation of special and nonspecial incidence capacities

## Statement

Let H satisfy the hypotheses of ce94930a22e0, and write rho=m/n. Suppose
  (1/n)sum_v phi(v)=rho+5/6+epsilon
with epsilon>=0.

Let
  Delta_ns = sum_v(2phi(v)-3)-2(m-s),
the slack in the cumulative nonspecial-terminal capacity, and
  Delta_sn = sum_v(2phi(v)-1)-(2m+s),
the slack in the total snake-indegree capacity.

Then
  (1/2)Delta_ns + Delta_sn = 3epsilon n.

Also
  (2/3-epsilon)n <= s <= (2/3+2epsilon)n.

In particular, epsilon=0 iff Delta_ns=Delta_sn=0, and then s=2n/3. More generally, if epsilon=o(1), then both capacity systems have total slack o(n), so all but o(n) vertices have locally near-saturated terminal/snake budgets in the averaged sense.

## Body

Put S=sum_v phi(v)=(rho+5/6+epsilon)n and m=rho n.

By definition,
Delta_ns
 = 2S-3n-2m+2s
 = 2(rho+5/6+epsilon)n-3n-2rho n+2s
 = 2s-(4/3)n+2epsilon n.                              (1)

Similarly,
Delta_sn
 = 2S-n-2m-s
 = 2(rho+5/6+epsilon)n-n-2rho n-s
 = (2/3)n+2epsilon n-s.                               (2)

Therefore
(1/2)Delta_ns+Delta_sn
 = [s-(2/3)n+epsilon n]+[(2/3)n+2epsilon n-s]
 = 3epsilon n.

Since both slacks are nonnegative, (1) and (2) give respectively
  s >= (2/3-epsilon)n
and
  s <= (2/3+2epsilon)n.

If epsilon=0 then the weighted sum of two nonnegative slacks is zero, so both vanish and s=2n/3. The final near-saturation statement is immediate from the exact weighted slack identity.
