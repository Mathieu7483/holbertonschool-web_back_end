<p align="center"\>
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/a-highly-detailed--minimalist--and-abstract-repres%20(1).png"/>
</p\>

-----

# 💾 NoSQL - MongoDB (Stockage Document et PyMongo)

-----

## 📝 Description du Projet

Ce projet est une introduction pratique aux bases de données **NoSQL**, en se concentrant spécifiquement sur **MongoDB** et son modèle de **stockage de documents**. L'objectif est de maîtriser les opérations CRUD (Create, Read, Update, Delete) à la fois via le **shell Mongo** et l'interface **Python** à l'aide de la librairie **`PyMongo`**.

Ce travail permet de comprendre les avantages des bases de données orientées documents pour les structures de données flexibles et de savoir comment interroger, modifier et administrer des collections.

-----

## 🎯 Objectifs d'Apprentissage

À la fin de ce projet, vous devez être capable d'expliquer et d'utiliser :

  * **Concepts NoSQL :** La signification de **NoSQL**, sa différence avec les bases **SQL** (transactionnalité **ACID** vs. flexibilité), et les types de stockage NoSQL (document, clé-valeur, graphe, etc.).
  * **MongoDB (Shell) :** Utilisation des commandes de base du shell Mongo pour lister les bases de données, insérer, lire, mettre à jour et supprimer des documents.
  * **Opérations CRUD :** Maîtrise des méthodes `insert`, `find`, `update`, `delete` et `count`.
  * **Agrégation et Requêtes :** Comment effectuer des requêtes avancées et des comptages spécifiques dans les collections.
  * **Python et PyMongo :** Connexion à une instance MongoDB depuis un script Python et implémentation des opérations CRUD de manière programmatique.

-----

## 💻 Contenu de l'Exercice

Le projet alterne entre des scripts du shell Mongo (exécutés directement) et des scripts Python utilisant `PyMongo`.

### 1\. MongoDB Shell Scripts

Les tâches initiales se concentrent sur la syntaxe du shell pour l'administration et la manipulation des données.

| Tâches (0 à 7) | Concepts Clés du Shell Mongo |
| :--- | :--- |
| **Administration** | Lister et créer des bases de données. |
| **CRUD de Base** | `db.collection.insert()`, `db.collection.find()`, `db.collection.update()`, `db.collection.deleteMany()`. |
| **Requêtes** | Filtrage par conditions, comptage (`.count()`). |

### 2\. Python Scripts (`PyMongo`)

Les tâches suivantes implémentent la même logique dans un environnement Python, essentielle pour l'intégration *back-end* (comme dans une API Flask/Django).

| Tâches (8 à 12) | Concepts Clés de PyMongo |
| :--- | :--- |
| **Connexion** | Initialisation du client MongoDB en Python. |
| **CRUD Python** | Implémentation de fonctions Python pour `find()`, `insert()`, `update_one()` (via l'opérateur `$set`). |
| **Agrégation/Statistiques** | Comptage de documents, utilisation de la méthode `aggregate` pour les statistiques de log. |

-----

## ⚙️ Prérequis et Configuration

  * **MongoDB Version :** 4.4.
  * **Environnement :** Ubuntu 20.04 LTS.
  * **Librairies Python :** `python3` (v3.9) et **`PyMongo`** (v4.8.0).
  * **Style de Code :** `pycodestyle` (v2.5.\*).
  * **Fichiers Mongo :** Doivent commencer par `// my comment`.
  * **Fichiers Python :** Doivent commencer par `#!/usr/bin/env python3` et respecter les *docstrings* et l'isolation du code (`if __name__ == "__main__":`).

### ⚠️ Installation (Critique)

L'installation de MongoDB 4.4 sur Ubuntu 22.04 nécessite l'ajout de dépendances (comme `libssl1.1`) et le démarrage du processus `mongod` en arrière-plan avant d'exécuter les scripts ou le shell.

```bash
# Lancement de MongoDB (selon les instructions du projet)
sudo -u mongodb /usr/bin/mongod --config /etc/mongod.conf &
```

-----

## ✒️ Auteur

**Mathieu**

[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School