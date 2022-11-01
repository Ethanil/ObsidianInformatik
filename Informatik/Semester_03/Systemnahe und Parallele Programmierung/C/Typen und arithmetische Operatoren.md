---
aliases: 
---
# Typen und arithmetische Operatoren 

## Variable
In C ist eine Variable ein Name für eine Speicherstelle.
### Deklaration
Variablen müssen deklariert werden, bevor sie verwendet werden und sind typisiert.
### Namensgebung
Variablennamen dürfen nicht mit einer Zahl beginnen und dürfen:
- Großbuchstaben
- Kleinbuchstaben
- Zahlen
- _
enthalten.
## Primitive Typen
| Type     | Beschreibung                                        | Größe             |
| -------- | --------------------------------------------------- | ----------------- |
| `int`    | Integer, Größe ist abhängig vom ausführenden System | meistens `32`-bit |
| `char`   | Ein einzelner byte                                  | 8 bit             |
| `float`  | Floating point number                               | 32 bit            |
| `double` | Double-precision floating point number              | 64 bit            |

| Modifier | Beschreibung                                          | Verwendbar für    |
| -------- | ----------------------------------------------------- | ----------------- |
| unsigned | Immer positiv oder 0                                  | `int` oder `char` |
| long     | Mindestens so lang wie `int`                          | `int`             |
| short    | Mindestnes 16-bit groß, maximal so groß wie ein `int` | `int`                  |

## Konstanten
| Beispiel      | Typ      |
| ------------- | -------- |
| 3343          | `int`    |
| 3L            | `long`   |
| 's'           | `char`   |
| 3.0f          | `float`  |
| 27.0          | `double` |
| "some string" | A string         |

## Special Characters
| Character | Beschreibung   |
| --------- | -------------- |
| `\n`      | newline        |
| `\t`      | horizontal tab |
| `\v`      | vertical tab   |
| `\\`      | backslash      |
| `\b`      | Backspace      |
| `\'`      | single quote   |
| `\"`      | double quote               |

## Operator Präzedenz
- `()`
- `++, --`
- `*, \`
- `+, -`
- `=, +=, -=, *=, \=`

## static Variable
static variable behalten ihren Wert zwischen aufrufen. Wenn wir also bspw. eine `counter` variable in einer Funktion haben, die zählt wie oft die Funktion schon aufgerufen wurde und jedes mal in der Funktion damit um 1 erhöht wird, ist sie beim ersten Aufruf 1, danach 2, dann 3 usw.
## Links