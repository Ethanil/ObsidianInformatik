---
aliases: 
---
# Sequenzkalkülregeln 
$$\begin{align}
&(Ax)& &\frac{}{\Gamma, \varphi \vdash \Delta \varphi} \\
&(0-Ax)& &\frac{}{\Gamma, 0 \vdash \Delta}& &(1-Ax)& &\frac{}{\Gamma \vdash \Delta, 1} \\
&(\neg L)& &\frac{\Gamma \vdash \Delta \varphi}{\Gamma, \neg \varphi \vdash \Delta}& &(\neg R)& &\frac{\Gamma, \varphi \vdash \Delta}{\Gamma \vdash \Delta \neg \varphi}\\
&(\lor L)& &\frac{\Gamma, \varphi \vdash \Delta\  \ \ \ \ \ \Gamma, \psi \vdash \Delta}{\Gamma, \varphi \lor \psi \vdash \Delta}& &(\lor R)& &\frac{\Gamma \vdash \Delta, \varphi \psi}{\Gamma \vdash \Delta, \varphi \lor \psi}\\
&(\land L)& &\frac{\Gamma, \varphi, \psi \vdash \Delta}{\Gamma, \varpi \land \psi \vdash \Delta}& &(\land R)& &\frac{\Gamma \vdash \Delta, \varphi  \ \ \ \ \ \Gamma \vdash \Delta, \psi}{\Gamma \vdash \Delta, \varphi \land \psi}\\
&(\rightarrow L)& &r
\end{align}$$

## Links