# Hidden ordered-shadow cycles force a near-doubling rank spread

## Statement

In the obstruction alternative of 1412d7e749b8, suppose the minimal hidden cycle is E_i,...,E_j and has c=j-i+1 edges. Let q_min=q_i and q_max=q_j; these are respectively the minimum and maximum parent ranks on the cycle. Then c<=q_min and q_max-q_min>=c-2. Consequently q_max>=q_min+c-2>=2c-2, so c<=floor((q_max+2)/2).

## Body

By 31a31f25c2bf, the parent ranks along the increasing shadow segment are nondecreasing and q_j-q_i >= (j-i)-1 = c-2. By f2925a904b8e, every nonspecial edge on a c-edge linear cycle has rank at least c, so in particular q_i>=c. Combining gives q_j>=q_i+c-2>=2c-2, and rearranging yields the final bound.