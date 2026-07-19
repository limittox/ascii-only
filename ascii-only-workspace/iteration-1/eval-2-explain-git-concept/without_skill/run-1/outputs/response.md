Both integrate changes from one branch into another, but differently:

**git merge** combines two branches by creating a new "merge commit" that ties their histories together. Both branches' histories are preserved exactly as they happened.

```
A---B---C  main
     \   \
      D---E---M   (M = merge commit)
```

**git rebase** replays your branch's commits on top of the other branch, rewriting them as new commits. The result is a straight-line history with no merge commit.

```
A---B---C  main
         \
          D'---E'   (rewritten copies of D and E)
```

**Trade-offs:**
- Merge: preserves true history, safe for shared branches, but history gets noisy with merge commits.
- Rebase: clean linear history, but rewrites commits — never rebase commits that others have already pulled.

Common workflow: rebase your local feature branch onto `main` to keep it clean, then merge it into `main` when done.
