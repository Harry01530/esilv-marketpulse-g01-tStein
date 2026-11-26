# TD10 - Bloomberg Provider

## Travail réalisé

- Création du module bloomberg_provider.py.
- Réutilisation du mapping réalisé au TD09.
- Normalisation des observations Bloomberg.
- Comparaison avec le fichier de référence.
- Réutilisation des fonctions analytics.py.
- Création de build_market_snapshot().
- Intégration du snapshot dans main.py.

## Résultats

- Mode : APPROVED_SAMPLE.
- Observations AAPL : 21.
- Observations SP500 : 21.
- Les 42 observations correspondent à la référence.
- Rendement AAPL : +6.48 %.
- Rendement SP500 : +2.15 %.
- Performance relative : +4.33 points.
- Base 100 AAPL : 106.48.
- Base 100 SP500 : 102.15.

Le snapshot peut être importé et réutilisé pour le dashboard.

La connexion Bloomberg LIVE n'a pas été testée.
