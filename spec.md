# SPEC : Tâche initiale — hello_world()

## ID
TASK-001

## DESCRIPTION
Créer une fonction `hello_world()` dans `main.py` à la racine du projet, qui retourne le string `"Hello from Hermes Pipeline"`.

## FICHIER(S) CONCERNÉ(S)
- `main.py`
- `tests/test_main.py`

## ACCEPTANCE CRITERIA
1. `main.py` existe à la racine et contient une fonction `hello_world()` retournant `"Hello from Hermes Pipeline"`
2. `tests/test_main.py` existe et contient un test unitaire qui appelle `hello_world()` et vérifie le retour
3. Le test passe avec `python -m pytest tests/test_main.py -v`

## NOTES
- Pas de dépendances externes requises au-delà de `pytest` (éventuellement déjà dispo)
- Garde le code minimal et clair

## STATUT
- validation: ✅ OK
- push: ❌ ÉCHEC
- retry: 2026-06-09 16:31:40


# SPEC : Tâche additionnelle — add()

## ID
TASK-002

## DESCRIPTION
Ajouter une fonction `add(a, b)` dans `main.py` qui retourne la somme de ses deux arguments. Créer le test unitaire correspondant `test_add()` dans `tests/test_main.py`.

## FICHIER(S) CONCERNÉ(S)
- `main.py`
- `tests/test_main.py`

## ACCEPTANCE CRITERIA
1. `main.py` contient une fonction `add(a, b)` retournant `a + b`.
2. `tests/test_main.py` contient une fonction `test_add()` qui importe `add` depuis `main` et vérifie que `add(2, 3) == 5` (et d'autres cas).
3. Le test passe avec `python -m pytest tests/test_main.py -v`.

## NOTES
- Garde le code simple et typé (facultatif).
- Aucun effet de bord.

## STATUT
- validation: ⏳ EN ATTENTE
## STATUT
- validation: ✅ OK
- pushed: 2026-06-11 10:17:30


# SPEC : Tâche additionnelle — multiply()

## ID
TASK-003

## DESCRIPTION
Ajouter une fonction `multiply(a, b)` dans `main.py` qui retourne le produit de ses deux arguments. Créer le test unitaire correspondant `test_multiply()` dans `tests/test_main.py`.

## FICHIER(S) CONCERNÉ(S)
- `main.py`
- `tests/test_main.py`

## ACCEPTANCE CRITERIA
1. `main.py` contient une fonction `multiply(a, b)` retournant `a * b`.
2. `tests/test_main.py` contient une fonction `test_multiply()` qui importe `multiply` depuis `main` et vérifie que `multiply(3, 4) == 12` (et d'autres cas).
3. Le test passe avec `python -m pytest tests/test_main.py -v`.

## NOTES
- Garde le code simple et typé (facultatif).
- Aucun effet de bord.

## STATUT
- validation: ⏳ EN ATTENTE