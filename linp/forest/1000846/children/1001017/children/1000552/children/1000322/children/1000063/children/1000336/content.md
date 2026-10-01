# Sharp minimum-degree lower bound conjecture for ascending edges

## Statement

Let H be a finite linear 3-graph with minimum degree δ. If e is an ascending nonspecial edge, then φ(e)>=δ+1.

## Body

The proved endpoint-specific bound gives only φ(e)>=ceil((δ+3)/2). The stronger δ+1 bound is suggested by Pósa-style rotations of a maximum entrance path. A private exact check of 5,219 randomly generated small positive-minimum-degree linear triple systems found no ascending edge with φ(e)<=δ; the smallest observed margin was φ(e)-δ=1. The affine-plane booster family 7564e287447b calibrates the proposed constant sharply: for L=2 it has δ=4 and the distinguished ascending edge has φ(e)=5=δ+1. The intended proof mechanism is to fix a maximum path ending at the unique entrance x, of length φ(e)-1, and iteratively rotate around single blockers at the opposite endpoint. Single blockers should create new opposite endpoints, while double blockers consume two units of the finite path-vertex budget. The conjecture asks for the rotation closure to recover the factor two lost in the elementary blocker count.
