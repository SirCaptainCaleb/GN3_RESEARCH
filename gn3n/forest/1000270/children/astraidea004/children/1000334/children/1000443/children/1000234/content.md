# Positional lag is exactly the omission-minus-insertion prefix balance

## Statement

Let A=(a_0,...,a_{lambda-1}) be a globally longest tight path and C a tight path of order lambda-d whose common vertices with A occur in the same relative order. Assume no ordered-A-edge reversing witness from 8f2c6a91d4e7 occurs at the common vertices. If a_i occurs at position p_i of C, let M_i be the number of vertices of A-C among a_0,...,a_{i-1}, and let E_i be the number of vertices of C-A occurring before a_i in C. Then i-p_i=M_i-E_i, and hence 0<=M_i-E_i<=d. In particular, at every surviving A-vertex, the number of exterior C-vertices already inserted never exceeds the number of omitted A-vertices already passed, and the excess of omissions is at most d.

## Body

Before a_i there are i vertices of A. Exactly M_i of them are omitted from C, so i-M_i common A-vertices precede a_i in C. In addition E_i exterior vertices of C-A precede a_i. Therefore p_i=(i-M_i)+E_i and i-p_i=M_i-E_i. The certified positional-lag theorem gives i-d<=p_i<=i in the absence of a reversing witness, which is exactly 0<=M_i-E_i<=d. Thus the displacement profile is a bounded prefix-balance process: an omitted A-vertex increases the balance and an exterior C-vertex decreases it, with the balance constrained to the strip [0,d] whenever a common A-vertex is encountered. For d=1 this balance is binary, recovering the one-transition behavior on consecutive surviving runs.