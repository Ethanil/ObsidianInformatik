Der Gradient ist die Kombination aus der äußeren und der inneren Kante, welche jeweils durch [[Dilatation]] gefolgt von [[Mengendifferenz]] bzw [[Erosion]] gefolgt von [[Mengendifferenz]] entstanden sind:
$$\begin{align*}
\beta_{o}(A) = (A \oplus b)-A&&\text{Äußere Kante}\\
\beta_{i}(A) = A - (A \ominus b)&&\text{Innere Kante}\\
Gradient(A) = \beta_{o} + \beta_{i} = (A \oplus b) - (A \ominus b)
\end{align*}$$