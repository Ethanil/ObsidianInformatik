System calls sind eine Schnittstelle zwischen einem [[Informatik/Semester_05/Betribessysteme/Prozess|Prozess]] und dem Betriebssystem.

```ad-example
title:Beispiele
collapse:
- hardware-realted services
- Erzeugung und Ausführung von neuen Prozessen (fork und exec)
- Kommunikation mit integralen Kernel-Services wie process-scheduling
```

## Invocation am Beispiel read
1. Ein Userlevel-Prozess ruft die wrapper-funktion `read` auf.
2. Die Wrapper-Funktion platziert den System-Call `0`(read) in das akkumulator-Register `RAX` und die Parameter in die entsprechenden Register
3. Die Wrapper-Funktion called eine trap-funktion um einen software interrupt zu generieren
4. Der Prozessor switched in den kernel mode um den syscall dispatcher auszuführen
5. Der Syscall dispatcher schaut in der syscall tabelle nach welcher syscall handler(hier read) zu der syscall-nummer(hier 0) gehört
6. Der entsprechende Syscall handler bearbeitet den entsprechenden Syscall
7. Die Kontrolle wird an den ausführenden Wrapper zurückgegeben und der Prozessor switched wieder in der user-mode