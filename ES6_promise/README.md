Bonjour Mathieu,

Le projet sur les **Promesses ES6** est la suite logique de votre apprentissage sur les classes et la manipulation de données. C'est un concept **fondamental** pour gérer le code **asynchrone** en JavaScript, remplaçant les *callbacks* complexes et conduisant à des applications plus robustes.

Voici un `README.md` détaillé qui met l'accent sur le modèle et la gestion des états des Promesses.

-----

# 🤝 ES6 Promises (Gestion du Code Asynchrone)

-----

## 📝 Description du Projet

Ce dépôt est consacré à la maîtrise des **Promesses (Promises)** en JavaScript, introduites par ES6. Les Promesses sont des objets qui représentent l'achèvement (ou l'échec) futur d'une opération asynchrone, permettant d'organiser les opérations séquentielles de manière beaucoup plus propre que les *callbacks* imbriqués (*callback hell*).

Le projet explore les différents états d'une Promesse, les méthodes pour gérer leur résolution (`.then()`), leur rejet (`.catch()`), et les outils modernes pour la composition de Promesses (comme `Promise.all()`, `Promise.race()`, l'opérateur `await` et les fonctions `async`).

-----

## 🎯 Objectifs d'Apprentissage

À la fin de ce projet, vous devez être capable d'expliquer et d'utiliser :

  * **Cycle de Vie des Promesses :** Compréhension des trois états d'une Promesse : `pending` (en attente), `resolved` (réussie), et `rejected` (échouée).
  * **Consommation de Promesses :** Utilisation des chaînes de méthodes **`.then()`** et **`.catch()`** pour traiter les résultats ou les erreurs.
  * **Composition de Promesses :** Utilisation des méthodes statiques de l'objet `Promise` (`Promise.all()`, `Promise.race()`, `Promise.resolve()`, `Promise.reject()`) pour gérer plusieurs opérations asynchrones simultanément.
  * **Async/Await :** Utilisation de la syntaxe **`async`** et de l'opérateur **`await`** pour écrire du code asynchrone qui ressemble à du code synchrone, améliorant grandement la lisibilité.
  * **Gestion des Erreurs :** Utilisation des blocs **`try...catch`** dans le contexte `async/await` pour une gestion robuste des erreurs.

-----

## 💻 Contenu de l'Exercice

Ce projet propose des tâches allant de la simple création de Promesses à la gestion d'erreurs complexes et la composition asynchrone.

| Fichier | Concept Clé |
| :--- | :--- |
| `0-promise.js` | Création d'une simple instance de **`Promise`**. |
| `1-promise.js` | Résolution (`resolve`) et Rejet (`reject`) conditionnels. |
| `2-catch.js` | Utilisation de la méthode **`.catch()`** pour gérer les rejets. |
| `3-all.js` | Utilisation de **`Promise.all()`** pour gérer plusieurs promesses réussies en parallèle. |
| `4-user-promise.js` | Raccourcis pour la résolution immédiate : **`Promise.resolve()`**. |
| `5-photo-reject.js` | Raccourcis pour le rejet immédiat : **`Promise.reject()`**. |
| `6-final-user.js` | Gestion d'un ensemble de promesses, y compris les échecs, pour retourner un état final. |
| `7-guerilla.js` | Utilisation de **`Promise.race()`** (Load Balancer) pour obtenir le résultat le plus rapide. |
| `8-try.js` | Implémentation de la gestion des exceptions synchrones au sein d'une Promesse. |
| `9-try.js` | Utilisation de la structure **`try...catch`** avec des fonctions *callback* pour intercepter les erreurs. |

-----

## 🛠️ Configuration et Dépendances

Le projet est basé sur l'environnement Node.js moderne.

### ⚙️ Prérequis

  * **Environnement d'Exécution :** Node.js **20.x.x** et npm **9.x.x**.
  * **Fichier Utilitaire :** Le fichier `utils.js` est fourni pour simuler les appels asynchrones (`uploadPhoto`, `createUser`).
  * **Tests :** **Jest Testing Framework**.
  * **Linting :** **ESLint**.

### 🛠️ Installation

1.  **Clonage du Dépôt :**

    ```bash
    git clone https://github.com/votre-utilisateur/holbertonschool-web_back_end.git
    cd holbertonschool-web_back_end/ES6_promise
    ```

2.  **Installation des Dépendances (Jest, Babel, ESLint) :**

    ```bash
    npm install
    ```

3.  **Tests et Linting :**

      * Exécutez l'ensemble des tests et la vérification de style :
        ```bash
        npm run full-test
        ```

-----

-----

## ✒️ Auteur

**Mathieu**

[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School