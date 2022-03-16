---
aliases: 
---
# Merkblatt
Äquivalenzrelation:
Reflexiv: $x_1\sim x_1$
Symm: $x_1\sim x_2\Leftrightarrow x_2\sim x_1$
Transitiv: $x_1\sim x_2\land x_2\sim x_3\Rightarrow x_1\sim x_3$

Injektiv:
$\phi(a)=\phi(b)\Rightarrow a=b$
Surjektiv:
Beliebiges Element aus dem Zielbereich nehmen und zeigen, dass wir dies "treffen" können.

Gruppen:
- Assoziativität $a\cdot (b\cdot c)=(a\cdot b)\cdot c$
- $\exists$ genau 1 neutrl. Element
- $\exists$ inv. Element zu jedem Element genau 1
	- optional: Kommutativität $a\cdot b=b\cdot a$(abelsch)

UG-Kriterien:
- $U\neq\emptyset$
- $a\cdot \bar{b}\in U$

(Gruppen-)Homomorphismen
$f(g_1*g_2)=f(g_1)\diamond f(g_2)$
- bijektive Homomorphismen sind Isomorphismen
	- $f(n_g)=n_h$
	- $\overline{f(g)}=f(\overline{g})$
	- $ker(f)=n_h$

Ringe
- $(R,+)$ ist abelsch
- $(R,\cdot)$ ist Assoziativ
- Distributivität von $+\ \&\ \cdot$
- $(R,\cdot)$ hat Einselement->Ring mit 1
- $(R,\cdot)$ ist Kommutativ->kommutativer Ring mit 1

Körper
- kommutativer Ring mit 1 und $(R\backslash\{0\},\cdot)$ ist abelsch

Komplexe Zahlen:
- $|z|=|\overline{z}|=\sqrt{a^2+b^2}$
- $\overline{z}=a-bi$
- $z\cdot \overline{z}=|z|^2$
- $z^{-1}=\frac{\overline{z}}{|z|^2}$

K-Vektorraum
- $(V,+)$ ist abelsch
- Skalarmult. hat n. Element und ist Ass. und Distr.

UVR-Kriterien:
- $V\neq\emptyset$$(0\in V)$
- $\alpha\cdot v,\beta\cdot w\in V\rightarrow \alpha\cdot v+\beta\cdot w\in V$

Norm:
- Definitheit $(||v||\geq 0 \land||v||=0\Leftrightarrow v=0)$
- Homogenität $(||\alpha v||=|\alpha|\cdot||v||)$
- Dreiecksungl $(||v+w||\geq ||v||+||w||)$
- 1er Norm: $\sum |v|$
- 2er Norm: $\sqrt{\sum v^2}$
- $\infty$ Norm: $max(|v_1|,|v_2|...)$

Skalarprodukt
- Definitheit
- Symmetrie
- $(\alpha x+\beta y|z)=\alpha(x|z)+\beta(y|z)$

lineare Abbildung
- $f(\alpha a+\beta b)=\alpha f(a)+\beta f(b)$

Dim. Formel:
$Rang(\phi)+dim(ker(\phi))=dim(V)$

Basiswechsel:
$M^{B'}_{C'}(\phi)=M^C_{C'}(id_W)\cdot M^B_C(\phi)\cdot M^{B'}_C(id_V)$

Eigenwert:
- $det(A-\lambda I)$
- $A-\lambda I=x$

Eigenraum:
- E()

Matrix Definitheit:
- pos/neg definit = alle EW sind pos/neg.
- semidefinit: jeweils mit 0
- infinit: es gibt pos & neg EW

Matrix symmetrisch-> $A=A^T$
Matrix orthogonal-> $AA^T=A^TA=I$ & Spalten sind normiert
$det(A)=det(A^T)$
