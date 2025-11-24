<p align="center"\>
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/python%20n%C3%A9eon%20carte%20%C3%A9l%C3%A9ctronique.png"\>
</p\>

-----

# 🚀 Python - Async (Programmation Asynchrone et Concurrence)

-----

## 📝 Description du Projet

Ce projet est une exploration approfondie du module standard **`asyncio`** de Python, qui permet l'écriture de code concurrent utilisant le modèle de **boucle d'événements (event loop)** et la syntaxe **`async`/`await`**.

L'objectif est de comprendre et d'implémenter l'exécution de plusieurs fonctions (coroutines) de manière concurrente, non pas via le *multithreading* ou le *multiprocessing* (parallélisme réel), mais via l'**asynchronisme** (concurrence simulée), ce qui est idéal pour les tâches bloquantes liées aux E/S (réseau, disque, attente).

Ce projet couvre les concepts de base des **coroutines**, des **tâches (`asyncio.Task`)** et des outils pour mesurer l'efficacité de la concurrence.

-----

## 🎯 Objectifs d'Apprentissage

À la fin de ce projet, vous devez être capable d'expliquer et d'utiliser :

  * **Coroutines :** La syntaxe **`async def`** pour définir une coroutine et le mot-clé **`await`** pour suspendre son exécution en attendant un résultat.
  * **Boucle d'Événements :** Comment utiliser **`asyncio.run()`** pour exécuter le point d'entrée d'une application asynchrone.
  * **Concurrence :** Lancement et exécution concurrentielle de multiples coroutines en utilisant **`asyncio.gather()`** ou des techniques similaires.
  * **Tâches (`Tasks`) :** La création et la gestion des objets **`asyncio.Task`** qui encapsulent l'exécution des coroutines.
  * **Performance :** Mesure du temps d'exécution total et comparaison avec un modèle séquentiel (implicitement).

-----

## 💻 Contenu de l'Exercice

Chaque tâche est un script Python utilisant le module `asyncio` pour gérer des opérations d'attente (simulées via `asyncio.sleep`) avec un délai aléatoire.

| Fichier | Concept Clé | Fonction `asyncio` Utilisée |
| :--- | :--- | :--- |
| `0-basic_async_syntax.py` | **Coroutines de base** (`async/await`) | `asyncio.sleep`, `random.uniform` |
| `1-concurrent_coroutines.py` | **Concurrence** et liste de résultats | `asyncio.create_task`, `asyncio.gather` |
| `2-measure_runtime.py` | **Mesure de performance** (temps total/moyen) | `time.time()`, `asyncio.run` |
| `3-tasks.py` | **Création explicite de Tâche** (Fonction vs Coroutine) | `asyncio.create_task` |
| `4-tasks.py` | **Exécution concurrente de Tâches** | `asyncio.create_task`, `asyncio.gather` |

-----

## ⚙️ Prérequis

  * **Interpréteur :** Python 3.9 (ou supérieur).
  * **Système :** Ubuntu 20.04 LTS.
  * **Style de Code :** `pycodestyle` (version 2.5.x).
  * **Type Hinting :** Toutes les fonctions et coroutines doivent être entièrement **type-annotated** (incluant les retours `async`).
  * **Documentation :** Tous les modules et fonctions doivent avoir une **docstring détaillée**.
  * **Exécution :** Les fichiers doivent commencer par `#!/usr/bin/env python3` et être exécutables.

-----

## 🚀 Exécution

Les scripts sont conçus pour être exécutés via la boucle d'événements `asyncio.run()`.

```bash
# Exemple d'exécution pour la Tâche 0
#!/usr/bin/env python3
./0-main.py
```

### Exemple de Concurrence

La tâche `1-concurrent_coroutines.py` illustre un point **crucial** : l'utilisation de `asyncio.gather` permet de démarrer plusieurs appels `wait_random` simultanément. Puisque les coroutines sont lancées et suspendent leur exécution de manière non-bloquante, les résultats finaux doivent être collectés dans l'ordre où ils se terminent (même si la liste finale doit être triée).

-----

## 👤 Auteur

**Mathieu**

[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School

-----

## 📜 Licence

Ce projet est distribué sous la **Licence MIT**.
