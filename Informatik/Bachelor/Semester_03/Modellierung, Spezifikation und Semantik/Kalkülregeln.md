---
aliases: 
---
# Kalkülregeln 
$$\begin{align}
&\text{rNum}\frac{}{<n, \sigma > \Downarrow n}\\ \\
&\text{rVar}\frac{}{< X, \sigma > \Downarrow n}n = \sigma(X) \\ \\
&\text{r}\oplus \frac{<aexpr_{1},\sigma>\Downarrow n_{1}\ \ \ <aexpr_{2},\sigma> \Downarrow n_{2}}{<(aexpr_{1} \oplus aexpr_{2}),\sigma > \Downarrow n}n = n_{1} + n_{2} \\ \\
&\text{r}\ominus \frac{<aexpr_{1},\sigma>\Downarrow n_{1}\ \ \ <aexpr_{2},\sigma> \Downarrow n_{2}}{<(aexpr_{1} \ominus aexpr_{2}),\sigma > \Downarrow n}n = n_{1} - n_{2} \\ \\
&\text{r}\odot \frac{<aexpr_{1},\sigma>\Downarrow n_{1}\ \ \ <aexpr_{2},\sigma> \Downarrow n_{2}}{<(aexpr_{1} \odot aexpr_{2}),\sigma > \Downarrow n}n = n_{1} \cdot n_{2} \\ \\
\\
&\text{rtrue}\frac{}{< true, \sigma> \Downarrow true}\\ \\
&\text{rfalse}\frac{}{< false, \sigma> \Downarrow false}\\ \\
&\text{reqt}\frac{<aexpr_{1}, \sigma> \Downarrow n_{1}\ \ \ <aexpr_{2},\sigma> \Downarrow n_{2}}{<(aexpr_{1}\ eq\ aexpr_{2}),\sigma > \Downarrow true}n_{1} = n_{2}\\ \\ 
&\text{reqf}\frac{<aexpr_{1}, \sigma> \Downarrow n_{1}\ \ \ <aexpr_{2},\sigma> \Downarrow n_{2}}{<(aexpr_{1}\ eq\ aexpr_{2}),\sigma > \Downarrow false}\neg n_{1} = n_{2}\\ \\ 
&\text{rleqt}\frac{<aexpr_{1}, \sigma> \Downarrow n_{1}\ \ \ <aexpr_{2},\sigma> \Downarrow n_{2}}{<(aexpr_{1}\ leq\ aexpr_{2}),\sigma > \Downarrow true}n_{1} \leq n_{2}\\ \\ 
&\text{rleqf}\frac{<aexpr_{1}, \sigma> \Downarrow n_{1}\ \ \ <aexpr_{2},\sigma> \Downarrow n_{2}}{<(aexpr_{1}\ leq\ aexpr_{2}),\sigma > \Downarrow false}n_{1} > n_{2}\\ \\ 
\\
&\text{rnott}\frac{< bexpr, \sigma > \Downarrow false}{<not\ bexpr, \sigma> \Downarrow true}\\ \\
&\text{rnotf}\frac{< bexpr, \sigma > \Downarrow true}{<not\ bexpr, \sigma> \Downarrow false}\\ \\
&\text{randf1}\frac{< bexpr_{1}, \sigma > \Downarrow false}{<(bexpr_{1}\ and\ bexpr_{2}), \sigma> \Downarrow false}\\ \\
&\text{randf2}\frac{< bexpr_{2}, \sigma > \Downarrow false}{<(bexpr_{1}\ and\ bexpr_{2}), \sigma> \Downarrow false}\\ \\
&\text{randt}\frac{< bexpr_{1}, \sigma > \Downarrow true\ \ \ < bexpr_{2}, \sigma > \Downarrow true}{<(bexpr_{1}\ and\ bexpr_{2}), \sigma> \Downarrow true}\\ \\
&\text{rort1}\frac{< bexpr_{1}, \sigma > \Downarrow true}{<(bexpr_{1}\ or\ bexpr_{2}), \sigma> \Downarrow true}\\ \\
&\text{rort2}\frac{< bexpr_{2}, \sigma > \Downarrow true}{<(bexpr_{1}\ or\ bexpr_{2}), \sigma> \Downarrow true}\\ \\
&\text{rorf}\frac{< bexpr_{1}, \sigma > \Downarrow false\ \ \ < bexpr_{2}, \sigma > \Downarrow false}{<(bexpr_{1}\ or\ bexpr_{2}), \sigma> \Downarrow false}\\ \\
\\
&\text{rsk}\frac{}{<skip, \sigma> \rightarrow \sigma} \\ \\
&\text{r}\frac{<aexpr, \sigma> \Downarrow n}{<X := aexpr, \sigma > \rightarrow \sigma'}\sigma' = \sigma[X\textbackslash n]\\ \\
&\text{r;}\frac{<c_{1}, \sigma> \rightarrow \sigma''\ \ \ <c_{2},\sigma''>\rightarrow \sigma'}{<c_{1};c_{2},\sigma> \rightarrow \sigma'}\\ \\
&\text{rift}\frac{<bexpr, \sigma> \Downarrow true \ \ \ <c_{1},\sigma> \rightarrow \sigma'}{<if\ bexpr\ then\ c_{1}\ else\ c_{2}\ fi,\sigma>\rightarrow \sigma'}\\ \\
&\text{riff}\frac{<bexpr, \sigma> \Downarrow false \ \ \ <c_{2},\sigma> \rightarrow \sigma'}{<if\ bexpr\ then\ c_{1}\ else\ c_{2}\ fi,\sigma>\rightarrow \sigma'}\\ \\
&\text{rwhf}\frac{<bexpr, \sigma> \Downarrow false}{<while\ bexpr\ do\ c\ od,\sigma>\rightarrow \sigma'}\\ \\
&\text{rwhf}\frac{<bexpr, \sigma> \Downarrow true \ \ \ <c,\sigma> \rightarrow \sigma''\ \ \ <while\ bexpr\ do\ c\ od,\sigma''> \rightarrow \sigma'}{<while\ bexpr\ do\ c\ od,\sigma>\rightarrow \sigma'}\\ \\
\end{align}$$

## Links