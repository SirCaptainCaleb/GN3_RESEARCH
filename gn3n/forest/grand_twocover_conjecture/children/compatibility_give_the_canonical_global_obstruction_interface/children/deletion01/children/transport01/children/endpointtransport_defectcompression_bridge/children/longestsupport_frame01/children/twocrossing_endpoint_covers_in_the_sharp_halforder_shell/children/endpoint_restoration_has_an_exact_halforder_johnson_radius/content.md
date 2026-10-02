# Crosswise endpoint restoration has an exact half-order Johnson radius

## Statement

In the sharp half-order shell, a crosswise two-crossing endpoint deletion cover with one remainder block of order r yields restored D=1 states at Johnson distances r+1 and lambda-r from the original deficient support. Hence one lies within ceil(lambda/2); for lambda=6 this is radius three.

## Body

Let B=Q-{q0}. Cutting the two crossings gives nonempty B-blocks B1,B2 and X-blocks X1,X2, with each deletion-cover component Ci supported on Bi union Xi. Both Ci have order lambda. If |B1|=r, then |B2|=lambda-1-r, |X1|=lambda-r, and |X2|=r+1. Restoring q0 to either component gives D=1 states. Their deficient supports differ from X by B1 union {q0} and B2 union {q0}, so their Johnson distances from X are r+1 and lambda-r. Therefore the nearer restored support has distance min(r+1,lambda-r)<=ceil(lambda/2). This specializes to radius three when lambda=6. The block-size identities alone therefore do not yield a lambda-uniform bounded radius; any such improvement must use additional ordered/orientation information.