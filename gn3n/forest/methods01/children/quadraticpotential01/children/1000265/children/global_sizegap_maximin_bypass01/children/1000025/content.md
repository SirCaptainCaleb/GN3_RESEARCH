# Profiles (c+2,c,c) and (c+3,c,c) reduce to three listed globally-longest cases or a smaller longest-path complement

## Statement

Let H be a minimum counterexample and let P|Q|X be any three-cover with |Q|=|X|=c and |P| in {c+2,c+3}. If P is globally longest, then the only possible component profiles are (5,3,3) at order 11, (6,3,3) at order 12, and (7,4,4) at order 15. If P is not globally longest, then every globally longest tight path L has |V(H)-V(L)|<=2c-1, and H-V(L) is non-Hamiltonian with path-cover number two. Thus this profile/complement dichotomy depends only on the displayed component orders, not on how that profile was obtained.

## Body

Let n=|V(H)| and let lambda be the maximum order of a tight path. First suppose |P|=c+2 and P is globally longest. Then n=3c+2 and lambda=c+2. The certified longest-path bound lambda>=ceil((n-1)/2) gives c+2>=ceil((3c+1)/2), hence c<=3. Minimum-counterexample calculus gives n>10, so c=3 and the profile is (5,3,3) at order 11. If |P|=c+3 and P is globally longest, then n=3c+3 and lambda=c+3. Hence c+3>=ceil((3c+2)/2), so c<=4. Again n>10 forces c>=3, leaving (6,3,3) at order 12 and (7,4,4) at order 15.

Now suppose P is not globally longest and let L be any globally longest tight path. Then |L|>=|P|+1, while n=|P|+2c, so |V(H)-V(L)|<=2c-1. The path L is proper, since otherwise H would be Hamiltonian. By minimum-counterexample calculus its complement has path-cover number at most two. The complement cannot be Hamiltonian, since a Hamilton path there together with L would two-cover H. Hence its path-cover number is exactly two.
