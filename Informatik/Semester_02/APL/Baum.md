---
aliases: 
---
$\newcommand{\f}[1]{\mathcal{#1}}\newcommand{\F}[1]{\mathfrak{#1}}\newcommand{\b}[1]{\mathbb{#1}}$
# Baum 
Ein Baum besteht aus einer Knotenmenge $V$, Kantenrelation $E\subseteq V \times V$ und einer Wurzel $\lambda \in V$
```ad-example
title:Beispiel
collapse:
![[Baum 26.04.2022 16-52-12.excalidraw]]
$V=\{0,1,2,3,4,5,6\}$
$E=\{(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)\}$
$\lambda=0$
``` 
## Endlich verzweigt
Ein Baum heißt endlich verzweigt, wenn für jeden Knoten $u \in V$ die direkte Nachfolgermenge $E[u]:=\{v \in V:(u,v)\in E\}$ endlich ist.