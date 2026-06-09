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
