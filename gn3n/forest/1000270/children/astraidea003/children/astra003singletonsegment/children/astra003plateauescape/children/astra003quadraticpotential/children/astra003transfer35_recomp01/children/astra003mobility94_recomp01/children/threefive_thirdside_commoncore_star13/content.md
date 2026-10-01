# Every trapped three-five-five state has a reachable third-side common-core star

## Statement

Let H be a boundary tournament on thirteen vertices and let T|F|R be a spanning 3|5|5 cover lying in a trapped Astra-003 component consisting of 3|5|5 states. For every two distinct vertices u,v in T there exists r in R such that, with C=R-{r}, all three five-sets C union {r}=R, C union {u}, and C union {v} are Hamiltonian. Moreover the covers T|F|R, (T-{u}+{r})|F|(C union {u}), and (T-{v}+{r})|F|(C union {v}) lie in the same component and form a neutral support triangle with F fixed. Consequently, for suitable Hamilton paths on the three five-sets, at least one of the following occurs: (1) two of the paths disagree in relative order on C; (2) C together with two of {r,u,v} is Hamiltonian; (3) there is a Hamiltonian four-set inside C union {r,u,v}; (4) a tight triple on two roots and one core vertex reverses a displayed root-core edge.

## Body

Fix distinct u,v in T. The coordinate-wise exchange argument in astra003mobility94_recomp01 is side-specific: for each x in T, applying four-of-six to R union {x} gives at least three vertices r in R for which replacing x by r on the three-side and replacing r by x on R is a legal 3|5 repartition, leaving F unchanged. Let R_u,R_v be these two subsets of R. Each has order at least three, while |R|=5, so R_u intersect R_v is nonempty. Choose r in the intersection and put C=R-{r}. Then C union {u} and C union {v} are Hamiltonian by the two legal exchanges, while C union {r}=R is Hamiltonian by the original cover. Thus the three displayed covers lie in the same trapped component and all have profile 3|5|5.

Apply the certified theorem three_fourcore_extensions_sync01 to the common four-core C and roots r,u,v, choosing Hamilton paths on the three Hamiltonian five-extensions. Its four alternatives are exactly the four conclusions in the statement. The provenance is retained: C is obtained from one displayed five-side by deleting the single exchange label r, u and v are prescribed original three-side labels, and the two modified five-extensions arise by one legal neutral move from the original state.
