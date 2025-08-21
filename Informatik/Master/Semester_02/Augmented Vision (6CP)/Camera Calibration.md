---
aliases: 
---
Mapping 3D Points into 2D: $\pi(P;\color{yellow}R,t$$,\color{green}C$$)\rightarrow p$
## $\color{yellow} \text{Extrinsic parameters } R, t$
Rotation and Translation
### World to Camera
#### Homogeneous coordinates:
$$P_{C}= R \cdot P_{W}+ t \Rightarrow P_{C} = \begin{pmatrix}
R & t \\ 0 & 1
\end{pmatrix} \cdot P_{W}$$
### Camera to World
$$P_{W}=R^{T}\cdot P_{C} - R^{T}\cdot t$$
#### Homogenous coordinates
$$P_{W} = \begin{pmatrix}
R & t \\ 0 & 1
\end{pmatrix}^{-1}\cdot R_{C}$$
## $\color{green}\text{Intrinsic parameter }C$
### Pinhole camera model
![[Pasted image 20250821155119.png]]
$\pi(P;\color{yellow} R,t$$,\color{green}C$$) = \color{green}K$$\cdot\color{yellow}\frac{1}{Z}\cdot \begin{bmatrix}R & t\end{bmatrix}$$\cdot P$
## Links