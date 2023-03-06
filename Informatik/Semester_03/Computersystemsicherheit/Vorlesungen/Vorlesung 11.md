---
aliases: 
---
# Vorlesung 11 
## Phishing/Spearphishing
## Browser-Security
- HTTPS über TLS
- Es gibt Zertifikate
## Broken Access Control
## SQL-Injection
- `' OR '1' = '1`
- `' AND False UNION ALL SELECT 'tabellenspalte1', 'tabellenspalte2'...`
- auf `'` achten oder `#` am Ende
### Gegenmaßnahmen
- Parametrisierte Abfragen
- leaste privilege Verbindungen
## XSS
- Persistent(z.B. Gästebuch)
- Reflected(z.B. Ein Link)
- `<script>alert("message");</script>`
## Links