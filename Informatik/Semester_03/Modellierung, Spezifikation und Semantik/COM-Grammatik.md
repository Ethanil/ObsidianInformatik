---
aliases: 
---
# COM-Grammatik
## aexpr
```ad-abstract
title: aexpr
aexpr ::= 
n | X | (aexpr $\oplus$ aexpr ) | (aexpr $\ominus$ aexpr ) | (aexpr $\odot$ aexpr)
```

## bexpr
```ad-abstract
title: bexpr
bexpr ::= 
true | false | (aexpr eq aexpr) | (aexpr leq aexpr) | not bexpr | (bexpr and bexpr) | bexpr or bexpr
```
## c
```ad-abstract
title:c
c::=
*skip* | X:= aexpr | c; c | *if* bexpr *then* c *else* c *fi* | *while* bexpr *do* c *od*
```
## Links