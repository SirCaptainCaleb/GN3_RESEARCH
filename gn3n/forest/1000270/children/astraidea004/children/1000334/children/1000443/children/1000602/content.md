# Positional lag is a bounded omission-insertion prefix balance

## Statement

Let A=(a_0,...,a_{lambda-1}) be a globally longest tight path and let C be a tight path of order lambda-d whose common vertices with A occur in the same relative order. Suppose no reversed-edge witness from the positional-lag theorem occurs at a surviving vertex a_i. Let M_i be the number of vertices a_h with h<i that do not lie on C, and let E_i be the number of vertices of C outside A that occur before a_i on C. Then i-p_i=M_i-E_i, where p_i is the position of a_i on C, and therefore 0<=M_i-E_i<=d. Thus every order-preserving comparison path of deficit d has a bounded prefix balance between omissions from A and exterior insertions; for d=1 the balance at every surviving A-vertex lies in {0,1}.

## Body

Among a_0,...,a_{i-1}, exactly i-M_i occur on C. Because the common A-vertices occur in the same relative order, all of those and no later A-vertex occur before a_i on C. The remaining vertices before a_i are precisely the E_i vertices of C outside A. Hence p_i=(i-M_i)+E_i, so i-p_i=M_i-E_i. The certified positional-lag theorem 8f2c6a91d4e7 gives i-d<=p_i<=i whenever no reversed-edge witness occurs, and substitution yields 0<=M_i-E_i<=d. This recasts the order-preserving branch as a bounded-height prefix-balance process rather than a local insertion-sign pattern.
