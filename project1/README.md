# ITS Projekt 1

- **Autor:** Peter Urgoš (xurgos00)
- **Datum:** 2022-04-17

## Matice pokrytí artefaktů

| Artifact                                        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
|-------------------------------------------------|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|
| Method add, edit and delete                     | x | x | x | x | x |   |   |   |   |    |    |    |    |    |    |    |    |    |    |    |    |
| Method to Tool relation                         |   |   |   |   | x |   |   |   |   |    |    |    |    |    |    |    |    |    |    |    |    |
| Tool add, edit and delete                       |   |   |   |   |   | x | x | x | x |    |    |    |    |    |    |    |    |    |    |    |    |
| Use case add, edit and delete                   |   |   |   |   |   |   |   |   |   | x  | x  | x  | x  |    |    |    |    |    |    |    |    |
| Visibility of method in published state         |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    | x  |    |    |    |
| Visibility of method private state              |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    | x  |    |    |
| Visibility of method changed to published state |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    | x  |    |
| Visibility of method changed to private state   |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    |    | x  |

## Matice Feature-Test

| Feature file       | 1-5 | 6-9 | 10-17 | 18-21 |
|--------------------|-----|-----|-------|-------|
| method.feature     |  x  |     |       |       |
| tool.feature       |     |  x  |       |       |
| use_case.feature   |     |     |   x   |       |
| visibility.feature |     |     |       |   x   |
