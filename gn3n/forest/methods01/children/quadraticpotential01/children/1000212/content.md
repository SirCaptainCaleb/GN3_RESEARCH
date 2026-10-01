# Adjacent-gap quadratic minima are equitable or maximin-tight staircases

## Statement

Let F be a nonempty family of triples of positive integers with common sum n, let (p,q,c) in F with p>=q>=c minimize p^2+q^2+c^2 over F, and assume p-q<=1 and q-c<=1. Let rho be the maximum minimum coordinate among triples in F. Then either p-c<=1, in which case the profile is equitable and rho=floor(n/3), or (p,q,c)=(c+2,c+1,c), in which case n=3(c+1) and rho=c=floor(n/3)-1. Applied to spanning three-covers, an adjacent-gap global quadratic minimum is therefore either equitable or a maximin-tight staircase.

## Body

If p-c<=1 then the displayed profile itself has minimum coordinate floor(n/3), while no triple with sum n can have minimum coordinate larger than floor(n/3). Hence rho=floor(n/3). Now suppose p-c=2. The adjacent-gap assumptions force p=c+2 and q=c+1, so n=3c+3. The displayed triple gives rho>=c. If rho>=c+1, some triple in F has all three coordinates at least c+1; since their sum is 3c+3, it must be (c+1,c+1,c+1). But its sum of squares is 3(c+1)^2, whereas the staircase has (c+2)^2+(c+1)^2+c^2=3(c+1)^2+2, contradicting quadratic minimality. Therefore rho=c=floor(n/3)-1.
