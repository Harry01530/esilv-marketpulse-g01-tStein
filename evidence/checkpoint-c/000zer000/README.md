# Checkpoint C - Integration and Release

## Student

- Name: Othmane Hassani
- GitHub: @000zer000

## Contribution

- Branch: feature/final-integration
- Commit: c2c5223
- Pull Request: #22
- Review requested from Stein1605.
- Merged by Stein1605.
- No formal review recorded on PR #22.

## Work completed

- Tested the Bloomberg sample provider.
- Validated the terminal report and Dash dashboard.
- Tested the project from a fresh clone.
- Updated the project documentation.
- Removed temporary files.

## Reproducibility

- Tested commit: 6bb3331
- Python: 3.12.14
- Fresh virtual environment.

Commands:

    python -m pip install -r requirements.txt
    python -m pip check
    python src/main.py
    python src/dashboard.py

## Results

- Provider: Bloomberg stage
- Access mode: APPROVED_SAMPLE
- AAPL: +6.48%
- SP500: +2.15%
- Relative performance: +4.33 percentage points

## Advanced contribution

- CI/CD pipeline implemented in PR #24.
- Ruff, Pytest, Docker and GitHub Actions.
- Automatic Docker publication to GHCR.
- Published image downloaded and tested successfully.

## Evidence

- 01_final_market_data.png
- 02_dash_dashboard.png
- 03_final_pull_request.png
- 04_reproducible_run.png
- 05_advanced_deployment.png
