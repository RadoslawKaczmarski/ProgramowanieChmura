# ProgramowanieChmura

## Zadnie Docker - Wykres:

### Instrukcja

1. Link do pobrania repozytorium:
```
https://github.com/RadoslawKaczmarski/ProgramowanieChmura.git
```



2. Aby przenisć się do pobranego repozytorium:
```
cd ProgramowanieChmura
```


3. Zadanie znajduje się w bramchu Wykres:
```
git checkout Wykres
```

4. Nastepnie musimy zbudować 'image':
```
docker build -t wykres:v1.0 . 
```

5. Uruchamiamy kontener wraz z '/bin/bash'
```
docker run --rm -it -p 5000:5000 wykres:v1.0 /bin/bash
```

6. Korzystamy z linku [Localhost:5000](http://127.0.0.1:5000/plot/a:2.0/b:5.0/c:8.0/xmin:-6/xmax:6/ymin:0/ymax:24)

Mamy możliwosć modyfiakcji zmiennych:
* a - zmienna typu float np. 3.5
* b - zmienna typu float np. 3.5
* c - zmienna typu float np. 3.5
* xmin - zmienna typu integer np. 3
* xmax - zmienna typu integer np. 3
* ymin - zmienna typu integer np. 3
* ymax - zmienna typu integer np. 3

7. Aby zastopować działanie kontenera: 
```
ctrl + c
```

8. Aby usunać 'image':
```
docker image rm wykres:v1.0
```
