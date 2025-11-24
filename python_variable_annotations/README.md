<p align="center"\>
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/HTML%20Advanced%20Structure.png"\>
</p\>

-----

# 🐍 Python - Variable Annotations (Annotations de Type)

-----

## 📝 Description du Projet

Ce projet est dédié à la maîtrise des **annotations de type (Type Annotations)** introduites par Python 3, notamment à partir de la version 3.5 (via la PEP 484). L'objectif est de rendre le code Python plus lisible, maintenable et **auto-documenté** en spécifiant explicitement les types attendus pour les arguments des fonctions, leurs valeurs de retour, ainsi que les variables.

Bien que Python reste un langage à **typage dynamique** (les annotations ne sont pas appliquées au *runtime*), ce projet met l'accent sur l'utilisation d'outils externes comme **`mypy`** pour la vérification statique du type, un standard dans le développement Python à grande échelle.

-----

## 🎯 Objectifs d'Apprentissage

À la fin de ce projet, vous devez être capable d'expliquer :

  * **Annotations de Type :** Comment annoter les signatures de fonctions et les variables.
  * **Types Simples :** Annotation des types primitifs (`int`, `float`, `str`, `bool`).
  * **Types Complexes :** Utilisation du module `typing` pour annoter les structures de données (ex: `List[float]`, `Union[int, float]`, `Tuple[str, float]`).
  * **Fonctions et Type Hinting :** Comment annoter les **fonctions de haut niveau** (fonctions qui retournent d'autres fonctions) à l'aide de `typing.Callable`.
  * **Duck Typing vs. Type Checking :** La philosophie du *duck typing* de Python et comment les annotations de type permettent d'ajouter une couche de sécurité et de clarté pour l'analyse statique (`mypy`).

-----

## 💻 Contenu de l'Exercice

Chaque tâche est un fichier Python contenant une fonction ou des variables annotées, allant des types simples aux types complexes et génériques.

| Fichier | Concept Clé | Type(s) Annoté(s) |
| :--- | :--- | :--- |
| `0-add.py` | Annotations de base (float) | `float`, `float` -\> `float` |
| `1-concat.py` | Annotations de base (str) | `str`, `str` -\> `str` |
| `2-floor.py` | Conversion de type et retour | `float` -\> `int` (via `math.floor`) |
| `3-to_str.py` | Représentation en chaîne | `float` -\> `str` |
| `4-define_variables.py` | Annotation de variables de module | `int`, `float`, `bool`, `str` |
| `5-sum_list.py` | **Types Complexes :** Liste homogène | `List[float]` -\> `float` |
| `6-sum_mixed_list.py` | **Types Complexes :** Liste hétérogène | `List[Union[int, float]]` -\> `float` |
| `7-to_kv.py` | **Types Complexes :** Tuple | `str`, `Union[int, float]` -\> `Tuple[str, float]` |
| `8-make_multiplier.py` | **Types Complexes :** Fonction retournée | `float` -\> `Callable[[float], float]` |
| `9-element_length.py` | **Types Génériques :** Duck Typing | `Iterable[Sequence]` -\> `List[Tuple[Sequence, int]]` |

-----

### 🌟 Tâches Avancées (Advanced)

Ces tâches introduisent des concepts plus complexes du module `typing` pour gérer la flexibilité et la rigueur du *type checking*.

| Fichier | Concept Clé | Annotations Avancées |
| :--- | :--- | :--- |
| `100-safe_first_element.py` | **Duck Typing** et flexibilité d'entrée | `Sequence[Any]` -\> `Optional[Any]` |
| `101-safely_get_value.py` | **Généricité** et dépendance de type | Utilisation de `TypeVar` (ou `~T`) pour garantir que le type du `default` correspond au type de retour potentiel, ainsi que `Mapping`. |
| `102-type_checking.py` | **Vérification Statique (`mypy`)** | Utilisation de `mypy` pour corriger les incohérences de type, notamment le mélange de `Tuple` et `List` dans les annotations et la conversion implicite d'arguments (`3.0` vs `int`). |

-----
## ⚙️ Prérequis

  * **Interpréteur :** Python 3.9 (ou supérieur).
  * **Système :** Ubuntu 20.04 LTS.
  * **Style de Code :** `pycodestyle` (version 2.5.).
  * **Documentation :** Tous les modules, classes et fonctions doivent avoir une **docstring détaillée** (documentation).
  * **Fichiers :** Doivent commencer par `#!/usr/bin/env python3` et être exécutables.
  * **Outil de Vérification :** Bien que non requis directement, l'outil **`mypy`** est l'outil standard pour valider ces annotations.

### 💡 Note Technique

L'attribut spécial `__annotations__` affiché dans les exemples de tests montre que Python stocke les annotations comme des métadonnées sur les fonctions, ce qui est utilisé par des outils comme `mypy`.

-----

## 🚀 Exécution

Les scripts s'exécutent comme des modules Python classiques.

```bash
# Exemple d'exécution pour la Tâche 5
#!/usr/bin/env python3
./5-main.py
```

### Exemple de Vérification Statique (Hors Tâches)

Pour vérifier la validité de vos annotations à l'aide de `mypy` (l'outil de vérification de type statique le plus courant) :

```bash
# Nécessite l'installation de mypy : pip install mypy
mypy 5-sum_list.py
# Succès si aucune erreur de type n'est trouvée.
```

-----

## ✒️ Auteur

**Mathieu**

[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School

-----

## 📜 Licence

Ce projet est publié sous la **Licence MIT**.

-----

## 🙏 Remerciements

Ce projet a été développé sous la direction et le contenu pédagogique de **Holberton School**.