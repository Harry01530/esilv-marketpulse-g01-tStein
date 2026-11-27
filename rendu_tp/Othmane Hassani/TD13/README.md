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
