<p align="center"\>
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/fait-moi-une-image-de-page-de-garde-pour-un-projet.png"\>
</p\>

# NodeJS Basics

## 📝 Description

Ce projet pose les bases de l'utilisation de **Node.js** dans un environnement backend. L'objectif est de s'affranchir du navigateur pour exécuter du JavaScript côté serveur. Le projet couvre la manipulation du système de fichiers (synchrone et asynchrone), l'utilisation de l'API `process`, la création de serveurs HTTP natifs, et l'introduction au framework **Express**. Une attention particulière est portée à l'organisation du code et à l'utilisation d'ES6 via Babel.

## 🛠️ Contenu de l'exercice

Le projet est découpé en plusieurs modules progressifs :

| Fichier / Répertoire   | Fonction / Objectif                                                   |
| ---------------------- | --------------------------------------------------------------------- |
| `0-console.js`         | Fonction `displayMessage` pour imprimer dans `STDOUT`.                |
| `1-stdin.js`           | Script interactif utilisant `process.stdin` et `process.stdout`.      |
| `2-read_file.js`       | Lecture synchrone d'un fichier CSV et traitement de données.          |
| `3-read_file_async.js` | Lecture asynchrone (Promesses) d'un fichier CSV.                      |
| `4-http.js`            | Création d'un serveur HTTP simple avec le module `http` de Node.      |
| `5-http.js`            | Serveur HTTP complexe gérant des routes et des accès aux données CSV. |
| `6-http_express.js`    | Création d'un serveur basique avec le framework **Express**.          |
| `7-http_express.js`    | Serveur Express avancé avec gestion de routes dynamiques.             |
| `8-full_server/`       | Structure complète d'un serveur Express (Controllers, Routes, Utils). |
| `database.csv`         | Base de données d'exemple contenant les informations des étudiants.   |

## 🏗️ Prérequis

L'environnement de développement doit strictement respecter les versions suivantes (standard Holberton) :

- **Système d'exploitation :** Ubuntu 20.04 LTS
- **Node.js :** version 20.x.x
- **npm :** version 9.x.x
- **Éditeurs autorisés :** vi, vim, emacs, VS Code

[Image d'une architecture client-serveur Node.js]

## 🚀 Installation et Exécution

### 1. Installation des dépendances

Une fois le dépôt cloné, installez les modules nécessaires (Babel, Jest, ESLint, Express, etc.) :

```bash
npm install

```

### 2. Exécution d'un script

Pour les fichiers de base (ex: tâche 0) :

```bash
node 0-main.js

```

Pour les serveurs nécessitant une transpilation ES6 en temps réel (via `nodemon` et `babel-node`) :

```bash
npm run dev

```

### 3. Tests et Qualité

Le projet utilise **Mocha** pour les tests unitaires et **ESLint** pour le respect des standards de code.

- **Lancer les tests :** `npm run test`
- **Vérifier le lint :** `npm run lint`
- **Test complet (Lint + Mocha) :** `npm run full-test`

## 👤 Auteur

**Mathieu**

[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School

## ⚖️ Licence

Ce projet est sous licence **MIT**.

## 🙏 Remerciements

- **Holberton School** pour le curriculum et les ressources pédagogiques.
- **Johann Kerbrat** pour la conception de l'exercice.
