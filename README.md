# pyrename

Very simple file renamer in Python.

Usage:
```
./pyrename <file-matcher> <new-name-pattern> [-d]
```

Regex patterns use Python substitution (capture groups can be referenced using \1, \2, \3, etc.), `-d` performs a dry-run.