---
aliases: 
---
# Pumping Lemma
Sei $L\subseteq \Sigma^*$ regulär, dann exisitert $n\in\mathbb{N}$ derart, dass sich jedes $x\in L$ mit $|x|\geq n$ zerlegen lässt in $x=uvw, v\neq \epsilon, |uv|\leq n$ und für alle $m\in \mathbb{N}$
$$u\cdot v^m\cdot w=u\cdot\underbrace{v\cdot v\cdot \dotso\cdot v}_{m\text{ mal}}\cdot u\in L$$

## Beweis per Pumping Lemma:
Sei $L$ regulär, dann muss gelten:
Sei $n\in\mathbb{N}$ gegeben.
Setze das Wort spezifisch fest abhängig von n.
Sei Zerlegung $x=uvw$ mit $v\neq \epsilon, |uv|\leq n$ gegeben.
Pumpe das Wort mittels $m$ auf/ab und beweise so, dass das neue Wort nicht mehr in $L$ ist $\Rightarrow L$ ist nicht regulär.

### Beispiel
$L=a^kb^k$
Sei $L=a^kb^k$ regulär, dann muss gelten:
Sei $n\in\mathbb{N}$ gegeben.
Setzte $w=a^nb^n$.
Sei Zerlegung $x=uvw$ mit $v\neq \epsilon, |uv|\leq n$ gegeben.
Da $|uv|\leq n$ besteht sowohl $u$, als auch $v$ nur aus $a$'s. Wenn wir nun also $m=0$ wählen, dann entfernen wir mindestens ein $a$ ohne ein $b$ zu entfernen und somit ist das Wort nicht mehr in $L$, da $|a|\neq|b|$.