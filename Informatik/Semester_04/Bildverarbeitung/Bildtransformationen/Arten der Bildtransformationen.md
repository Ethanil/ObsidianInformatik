vEs gibt grob 2 Arten der Bildtransformation, die unitäre und die parametrische Bildtransformationen. Wir verwenden diese Transformationen um dann in diesem anderen Raum die Bilder mathematisch zu manipulieren und danach wieder in den normalen Bildraum zu überführen.
## Unitäre Bildtransformationen
Bei einer unitären Bildtransformation wird die Bildinformation in einer Spalten- und Zeilentransformation kodiert.
Jeder unitäre Bildtransformation lässt sich als Matrix von Matrizen beschreiben.
[[Fourier Transformation]]
[[Cosinus Transformation]]
[[Walsh-Hadamard Transformation]]
[[Wavelet(Haar) Transformation]]
## Parametrische Bildtransformationen
Bei einer parametrischen Bildtransformation stellen wir die Bildinformation anhand von veränderten Ortsraumparametern dar z.B. $f[m,n]\mapsto f[r,\varTheta]$. Diese Transformation ist nicht zwingend orthogonale und damit idR nicht invertierbar. Diese Transformation hilft uns bestimmte Informationen einfacher abzulesen.
[[Hough Transformation]]
[[Radon Transformation]]

## Anwendungsgebiete
Wir verwenden die Bildtransformation unter anderem um eine Dimensionsreduktion (bspw. bei Kompression) oder eine Dekorrelation (um herauszufinden welche Teile des Bildes zusammengehören und welche nicht) durchzuführen.
Speziell betrachten wir Bildfilterung, Bildkompression und Bildmerkmale für Mustererkennung & Klassifikation