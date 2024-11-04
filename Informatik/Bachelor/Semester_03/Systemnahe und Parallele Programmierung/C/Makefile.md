---
aliases: Makefiles
---
# Makefile 
Makefiles verwalten den build process (zum Beispiel für [[gcc]]).
Sie beinhalten die Beschreibung wie man das Programm aufbaut.
````ad-example
title:Beispiel
collapse:
```make
all: hello

hello: helloc.
	gcc hello.c -o hello
```
````

## CMake
CMake automatisiert die generation der [[Makefile|Makefiles]].
Man erstellt eine `CMake.txt` die beispielsweise wie folgt aussieht
```cmake
cmake_minimum_required(VERSION 3.11)
project(my_test_project)

set(CMAKE_BUILD_TYPE Release) #Debug

add_executable(my_test_project)
	"source/main.cpp"
)
```
## Links