# ITS Projekt 1

- **Autor:** Peter Urgoš (xurgos00)
- **Datum:** 2022-04-17

## Matice pokrytí artefaktů

| Artifact                                        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
|-------------------------------------------------|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|
| Method add                                      | x | x |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    |    |    |
| Method edit                                     |   |   | x |   | x |   |   |   |   |    |    |    |    |    |    |    |    |    |    |    |    |
| Method delete                                   |   |   |   | x |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    |    |    |
| Method to Tool relation                         |   |   |   |   | x |   |   |   |   |    |    |    |    |    |    |    |    |    |    |    |    |
| Tool add                                        |   |   |   |   |   | x | x |   |   |    |    |    |    |    |    |    |    |    |    |    |    |
| Tool edit                                       |   |   |   |   |   |   |   | x |   |    |    |    |    |    |    |    |    |    |    |    |    |
| Tool delete                                     |   |   |   |   |   |   |   |   | x |    |    |    |    |    |    |    |    |    |    |    |    |
| Use case add                                    |   |   |   |   |   |   |   |   |   | x  | x  |    |    |    |    |    |    |    |    |    |    |
| Use case edit                                   |   |   |   |   |   |   |   |   |   |    |    | x  |    | x  | x  |    |    |    |    |    |    |
| Use case delete                                 |   |   |   |   |   |   |   |   |   |    |    |    | x  |    |    |    |    |    |    |    |    |
| Use case to requirement relation                |   |   |   |   |   |   |   |   |   |    |    |    |    | x  |    |    |    |    |    |    |    |
| Use case to evaluation scenario relation        |   |   |   |   |   |   |   |   |   |    |    |    |    |    | x  |    |    |    |    |    |    |
| Evaluation scenario to requirement relation     |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    | x  |    |    |    |    |    |
| Requirement to test case relation               |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    | x  |    |    |    |    |
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
