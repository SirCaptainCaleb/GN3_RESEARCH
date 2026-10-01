# Strict ordered-shadow growth forces near-unit parent-rank growth

## Statement

Let z_0z_1,...,z_{t-1}z_t be a strictly increasing path in the ordered shadow Z, with labels lambda_i and parent ascending hyperedges E_i of ranks q_i. Write epsilon_i=q_i-lambda_i in {0,1}, so epsilon_i=1 exactly when the chosen auxiliary edge is entrance-terminal and epsilon_i=0 exactly when it is terminal-terminal. Then q_{i+1}-q_i >= 1+epsilon_{i+1}-epsilon_i. In particular parent ranks are nondecreasing; equality q_{i+1}=q_i can occur only when epsilon_i=1 and epsilon_{i+1}=0, i.e. only across an entrance-terminal step followed by a terminal-terminal step. More generally q_j-q_i >= (j-i)+epsilon_j-epsilon_i >= j-i-1.

## Body

Since lambda_i=q_i-epsilon_i and strict integrality gives lambda_{i+1}>=lambda_i+1, we have q_{i+1}-epsilon_{i+1}>=q_i-epsilon_i+1, hence q_{i+1}-q_i>=1+epsilon_{i+1}-epsilon_i. Because epsilon values lie in {0,1}, the right side is always nonnegative. Equality of parent ranks requires 1+epsilon_{i+1}-epsilon_i=0, forcing epsilon_i=1 and epsilon_{i+1}=0. Summing from i to j-1 gives q_j-q_i >= (j-i)+epsilon_j-epsilon_i, and the final lower bound follows.