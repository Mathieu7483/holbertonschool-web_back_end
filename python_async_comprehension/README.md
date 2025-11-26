<p align="center"\>
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/python%20n%C3%A9eon%20carte%20%C3%A9l%C3%A9ctronique.png"\>
</p\>

-----

# ✨ Python - Async Comprehension (Générateurs et Compréhensions Asynchrones)

-----

## 📝 Description du Projet

Ce projet se concentre sur l'application des concepts de programmation asynchrone de Python (**`asyncio`**) aux structures de données et aux itérateurs. L'objectif est de maîtriser les **Générateurs Asynchrones** (utilisant `async for` et `yield`) et les **Compréhensions Asynchrones** (`[await f(i) for i in async_iter]`).

Ceci représente une approche moderne et élégante pour gérer des flux de données qui impliquent des opérations **asynchrones et bloquantes** (simulées ici par des attentes) de manière performante et lisible.

-----

## 🎯 Objectifs d'Apprentissage

À la fin de ce projet, vous devez être capable d'expliquer et d'implémenter :

  * **Générateur Asynchrone :** Comment créer un itérable capable de suspendre et reprendre son exécution pendant les cycles d'itération (`async for`).
  * **Compréhensions Asynchrones :** L'utilisation idiomatique des constructions de listes et de générateurs dans un contexte `async`/`await` (introduit par la **PEP 530**).
  * **Type Hinting :** Comment annoter correctement les générateurs et les fonctions asynchrones.
  * **Concurrence Réelle :** Mesurer le temps d'exécution de tâches asynchrones parallèles pour en valider l'efficacité.

-----

## 💻 Contenu de l'Exercice

Ce projet se compose de fonctions et coroutines utilisant des fonctionnalités avancées de Python 3.9 pour la concurrence.

| Fichier | Concept Clé | Implémentation |
| :--- | :--- | :--- |
| `0-async_generator.py` | **Générateur Asynchrone** | Utilise `async def` et `yield` avec `asyncio.sleep` pour produire des valeurs de manière asynchrone. |
| `1-async_comprehension.py` | **Compréhension Asynchrone** | Utilise une *async list comprehension* sur le générateur de la Tâche 0 pour collecter des données de manière concise. |
| `2-measure_runtime.py` | **Exécution Parallèle** et Mesure | Mesure le temps d'exécution de l'appel à la compréhension asynchrone lancé quatre fois en parallèle, démontrant le gain de temps de la concurrence. |

-----

## ⚙️ Prérequis

  * **Interpréteur :** Python 3.9 (ou supérieur).
  * **Style de Code :** `pycodestyle` (version 2.5.x).
  * **Type Hinting :** Toutes les fonctions et coroutines doivent être entièrement **type-annotated**.
  * **Documentation :** Tous les modules et fonctions doivent avoir une **docstring détaillée**.
  * **Exécution :** Les fichiers doivent commencer par `#!/usr/bin/env python3` et être exécutables.

-----

## 🚀 Exécution

Les scripts sont exécutés à l'aide de la boucle d'événements `asyncio.run()`, assurant l'exécution correcte des coroutines et des générateurs asynchrones.

```bash
# Exemple d'exécution de la Tâche 2 (Mesure du temps)
#!/usr/bin/env python3
./2-main.py
```

-----

## ✒️ Auteur

[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School
