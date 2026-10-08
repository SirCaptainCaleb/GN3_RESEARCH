# Two-sided endpoint deletion forces a single interior run

## Development

Statement:
Let n>=5 and let P be an antipodal n-geodesic, with ordered-three-face color word w_1...w_{n-2}. Suppose the (n-1)-geodesics obtained by deleting respectively the first and last move each have at most one color change. If P itself has at least two changes, its word is exactly 0 1^{n-4} 0 or 1 0^{n-4} 1. No antipodal coloring hypothesis is required.

Proof:
Put d_i=w_i XOR w_{i+1} for 1<=i<=n-3. Deleting the last move retains the prefix w_1...w_{n-3}, so sum_{i=1}^{n-4} d_i<=1. Deleting the first move retains suffix w_2...w_{n-2}, so sum_{i=2}^{n-3}d_i<=1. Since sum_{i=1}^{n-3}d_i>=2, any interior d_i=1 would already exhaust both inequalities and force the total to equal 1. Thus the interior d_i vanish, and the total condition forces d_1=d_{n-3}=1. Precisely the asserted two word patterns occur.
