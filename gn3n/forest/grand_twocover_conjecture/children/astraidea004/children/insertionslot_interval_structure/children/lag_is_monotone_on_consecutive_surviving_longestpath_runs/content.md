# Positional lag is monotone on consecutive surviving longest-path runs

## Statement

Let A=(a_0,...,a_{lambda-1}) be a globally longest tight path and let C be a tight path of order lambda-d whose common vertices with A occur in the same relative order. Let a_i,a_{i+1},...,a_j be consecutive vertices of A that all lie on C, and suppose the reversed-edge alternative of 8f2c6a91d4e7 does not occur at these vertices. If a_t occurs at position p_t of C and delta_t=t-p_t, then 0<=delta_t<=d and delta_{t+1}<=delta_t for i<=t<j. In particular, when d=1 the displacement profile on the run has the form 1,...,1,0,...,0, with at most one transition.

## Body

The certified positional-lag theorem 8f2c6a91d4e7 gives t-d<=p_t<=t, hence 0<=delta_t<=d. Since the common A-vertices occur in the same relative order and a_t,a_{t+1} are both present, their positions satisfy p_{t+1}>=p_t+1. Therefore delta_{t+1}=t+1-p_{t+1}<=t-p_t=delta_t. Thus the displacement is nonincreasing along every consecutive surviving A-run. For d=1 its values lie in {0,1}, so there can be at most one change, necessarily from 1 to 0. This supplies one-dimensional interval structure from global longest-path maximality even though local failed-insertion signs may alternate arbitrarily.