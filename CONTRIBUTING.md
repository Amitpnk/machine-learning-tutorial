# Contributing Guide

## For Students

### Submitting Lab Work

1. Fork this repository to your GitHub account
2. Create a branch: `git checkout -b lab/week-<N>-<your-name>`
3. Complete the notebook inside `modules/<module>/lab/`
4. Push your branch and open a Pull Request against `main`

### Lab Notebook Rules

- Do not modify anything outside the `# YOUR CODE HERE` sections
- Restart kernel and run all cells before submitting (`Kernel → Restart & Run All`)
- All cells must execute without errors
- Keep outputs visible — do not clear cell outputs before submitting

### Getting Help

- Open a GitHub Issue with the label `question`
- Tag the relevant module: e.g., `module-05-classification`

---

## For Instructors / Contributors

### Branch Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Student-facing code — no solutions |
| `solutions` | All lab solutions merged |
| `youtube/drafts` | WIP notebooks being polished for upload |
| `dev` | Active development for upcoming modules |

### Adding a New Notebook

1. Branch off `dev`
2. Add your notebook under `modules/<module>/notebooks/`
3. Add a corresponding lab starter under `modules/<module>/lab/`
4. Add the solution to `modules/<module>/solutions/` (commit on `solutions` branch)
5. Update the module's `README.md` with the new notebook entry
6. Update `youtube/episode_guide.md` if it maps to a video

### Notebook Quality Checklist

- [ ] Restart & Run All — zero errors
- [ ] No hardcoded absolute paths
- [ ] Datasets loaded via `datasets/download_datasets.py` or relative path
- [ ] All imports at the top cell
- [ ] Markdown cells explain each section
- [ ] Final cell prints/displays a result (not just silently runs)

### Commit Message Convention

```
feat(module-05): add SVM kernel comparison notebook
fix(module-03): fix broken Kaggle download link
docs(youtube): add episode 12 description
lab(module-08): add MLP from scratch starter
```
