<p align="center"\>
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/a-highly-detailed--minimalist--and-abstract-repres%20(1).png"/>
</p\>
---

# 📄 Python - Pagination (Gestion des Grands Datasets)

---

## 📝 Description du Projet

Ce projet se concentre sur l'implémentation de différentes stratégies de **pagination** pour gérer l'accès à de grands ensembles de données via une API. L'objectif est de fournir des mécanismes efficaces pour découper un *dataset* (ici, un fichier CSV de noms de bébés populaires) en morceaux gérables, en respectant les standards de conception d'API modernes.

Le projet couvre trois approches clés : la pagination simple par index, l'enrichissement par métadonnées **Hypermedia (HATEOAS)**, et la complexité cruciale de la **résilience à la suppression de données**.

---

## 🎯 Objectifs d'Apprentissage

À la fin de ce projet, vous devez être capable d'expliquer et d'implémenter :

* **Pagination Simple (Page/Taille) :** Comment calculer le `start_index` et le `end_index` à partir des paramètres `page` et `page_size`.
* **Hypermedia as the Engine of Application State (HATEOAS) :** Comment enrichir la réponse de l'API avec des métadonnées (liens vers les pages précédente/suivante, nombre total de pages) pour faciliter la navigation du client.
* **Résilience à la Suppression :** Comment concevoir une pagination qui reste **stable et cohérente** même si les enregistrements sont supprimés du *dataset* pendant que le client navigue entre les pages.

---

## 💻 Contenu de l'Exercice

Le projet est basé sur l'exploitation du fichier `Popular_Baby_Names.csv` et la création d'une classe `Server` pour encapsuler la logique de pagination.

| Fichier | Concept Clé | Objectif |
| :--- | :--- | :--- |
| `0-simple_helper_function.py` | **Calcul des Index** | Implémenter la fonction `index_range(page, page_size)` qui retourne un tuple `(start_index, end_index)` (Pagination 1-indexée). |
| `1-simple_pagination.py` | **Extraction Simple** | Utiliser `index_range` pour implémenter une méthode `get_page` qui retourne la page de données demandée. |
| `2-hypermedia_pagination.py` | **Métadonnées HATEOAS** | Implémenter une méthode `get_hyper` qui retourne le *dataset* paginé, enrichi de métadonnées telles que `page_size`, `page`, `next_page`, `prev_page`, `total_pages`, etc. |
| `3-del_resilient_pagination.py` | **Résilience à la Suppression** | Implémenter une méthode de pagination qui ne dépend plus de l'index de la ligne dans la liste, mais d'un identifiant stable, pour éviter de sauter des enregistrements lors de suppressions concurrentes. |

---

## ⚙️ Prérequis

* **Fichier de Données :** `Popular_Baby_Names.csv`.
* **Interpréteur :** Python 3.9 (ou supérieur).
* **Style de Code :** `pycodestyle` (version 2.5.\*).
* **Type Hinting :** Toutes les fonctions doivent être entièrement **type-annotated**.
* **Exécution :** Les fichiers doivent commencer par `#!/usr/bin/env python3` et être exécutables.

---

## 👤 Auteur

[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School