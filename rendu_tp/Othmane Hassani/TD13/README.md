# TD13 - CI/CD

## Integration continue (CI)

- Verification de la qualite du code avec Ruff.
- Execution de 5 tests unitaires avec Pytest.
- Construction automatique de l'image Docker.

## Livraison continue (CD)

- Publication automatique sur GitHub Container Registry.
- Publication uniquement sur main si la CI reussit.
- Utilisation de GitHub Actions.

## Resultats

- Ruff : All checks passed.
- Pytest : 5 passed.
- Docker build : Success.
- Docker publication : Success.
- Telechargement et execution de l'image GHCR : Success.

## Contribution personnelle

- Creation du Dockerfile.
- Creation des tests unitaires.
- Configuration de Ruff et Pytest.
- Creation du workflow CI/CD.
- Pull Request #24.

## Validation

Le dashboard fonctionne dans un conteneur Docker.
Le pipeline complet a ete valide sur main.

PR : https://github.com/Harry01530/esilv-marketpulse-g01-tStein/pull/24

Pipeline : https://github.com/Harry01530/esilv-marketpulse-g01-tStein/actions/runs/45967100985

## Tests unitaires

Les 5 tests sont dans tests/test_analytics.py :

- test_index_by_date
- test_align_series
- test_period_return
- test_relative_performance
- test_base_100

## Versionnement

- Tag manuel : v1.0.0 (commit 5b54ad2).
- Tag automatique : v1.0.1 (commit a2f9afd).

## Bonus

- Utilisation de commits conventionnels : feat, fix, docs.
- Creation du script Shell scripts/create_tag.sh.
- Detection du dernier tag de version.
- Incrementation automatique du numero PATCH.
- Validation locale avec --dry-run.
- Creation automatique du tag apres la reussite du CI/CD sur main.

## Validation du bonus

- Les trois jobs GitHub Actions ont reussi.
- Le tag v1.0.1 a ete cree automatiquement.
- Les deux tags sont presents sur GitHub.

PR : https://github.com/Harry01530/esilv-marketpulse-g01-tStein/pull/28

Pipeline : https://github.com/Harry01530/esilv-marketpulse-g01-tStein/actions/runs/45979719478

## Captures supplementaires

- capture_automatic_tag.png
- capture_versions.png
