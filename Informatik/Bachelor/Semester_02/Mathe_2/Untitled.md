$$\begin{cases}
y'(t)=12t^{2}e^{-y(t)}-e^{-y(t)}, t \geq \frac{1}{2} \\
y(\frac{1}{2})=0
\end{cases}$$
$$\begin{align}
y'(t)&=12t^{2}e^{-y(t)}-e^{-y(t)}\\
\Leftrightarrow y'(t)&=e^{-y(t)}(12t^{2}-1)\\
\text{Trennung der Variablen:}\\
y'(t)&=g(t)h(y(t))\\
g(b)&=12b^{2}-1\\
h(t)&=e^{-t}\\
G(t)&=\int^{t}_{\frac{1}{2}}12b^{2}-1 dt = [4b^{3}-b]^{t}_{\frac{1}{2}} = 4t^{3}-t- (4\cdot\frac{1}{8}- \frac{1}{2})=4t^{3}-t \\
H(x)&=\int^{x}_{0} \frac{1}{e^{-t}} dt =\int^{x}_{0}e^{t} dt =e^{x}-1 \\
x&=e^{H^{-1}(x)}-1\\
\Leftrightarrow H^{-1}(x)&=\ln(x+1) \\
y(t)&=H^{-1}(G(t)) \\
\Rightarrow y(t)&=ln(4t^{3}-t+1)
\end{align}$$
$$\begin{align}
\text{Probe:}\\
y(\frac{1}{2})=\ln(4\cdot \frac{1}{2}^{3}-\frac{1}{2}+1)&=\ln(1)=0 \checkmark \\
(\ln(4t^{3}-t+1))'=\frac{1}{4t^{3}-t+1}\cdot(12t^{2}-1) = \frac{1}{e^{\ln(4t^{3}-t+1)}}\cdot(12t^{2}-1)&=\frac{1}{e^{y(t)}}\cdot(12t^{2}-1)=e^{-y(t)}\cdot(12t^{2}-1)\checkmark
\end{align}$$

