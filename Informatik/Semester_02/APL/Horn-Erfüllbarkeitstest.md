---
aliases: 
---
# Horn-Erfüllbarkeitstest 
Wir verwenden eine [[Hornklauseln|Hornklauselmenge]] $H$ und definieren folgende Mengen:
- $H^{-}\subseteq H:$ negative Klauseln in $H$
- $H_{0}:= H \backslash H^-:$ nicht negative Klauseln

1. Schritt: Berechne minmale Interpetation $\mathfrak{I}_0 \vDash H_{0}$.
2. Schritt: Prüfe, ob $\mathfrak{I}_{0}\vDash H^-$.

```ad-abstract
title:Beweis
collapse:
Sei $H$ erfüllbar mit $\mathfrak{I}$, also $\mathfrak{I}\vDash H$. Dann erfüllt $\mathfrak{I}$ auch $H_0$. $\mathfrak{I}$ muss also alle Variablen wahr machen, die auch $\mathfrak{I}_0$ wahr macht. Da $\mathfrak{I}\vDash H^-$, erfüllt $\mathfrak{I}_0$ auch alle (negativen) Klauseln in $H^-$, also folgt $\mathfrak{I}_{0}\vDash H$
```

