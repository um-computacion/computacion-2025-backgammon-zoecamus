# Automated Reports

## Coverage Report
```text
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
cli/CLI.py                      57      1    98%   85
cli/__init__.py                  0      0   100%
core/__init__.py                 0      0   100%
core/board.py                  182     58    68%   141, 147, 209-211, 258-260, 285, 302-322, 348-368, 372-391, 404, 409-410, 415, 420, 432-435
core/checker.py                 66     11    83%   5-6, 97, 107, 149, 191, 206-210
core/dice.py                    44      1    98%   119
core/game.py                    35      0   100%
core/player.py                  39      2    95%   84, 124
excepciones/__init__.py          0      0   100%
excepciones/excepciones.py      33      0   100%
gui/__init__.py                  0      0   100%
test/__init__.py                 0      0   100%
test/test_board.py             129      1    99%   236
test/test_checker.py            50      3    94%   6-7, 63
test/test_cli.py               130      1    99%   216
test/test_dice.py               57      1    98%   82
test/test_game.py               65      1    98%   85
test/test_player.py             49      1    98%   69
----------------------------------------------------------
TOTAL                          936     81    91%

```

## Pylint Report
```text
************* Module ./tests
./tests:1:0: F0001: No module named ./tests (fatal)
************* Module ./pygame_ui
./pygame_ui:1:0: F0001: No module named ./pygame_ui (fatal)
************* Module core.checker
core/checker.py:180:0: C0325: Unnecessary parens after 'not' keyword (superfluous-parens)
core/checker.py:220:0: C0304: Final newline missing (missing-final-newline)
core/checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/checker.py:5:7: W0718: Catching too general exception Exception (broad-exception-caught)
core/checker.py:208:26: W0212: Access to a protected member __uid of a client class (protected-access)
core/checker.py:209:33: W0212: Access to a protected member __uid of a client class (protected-access)
core/checker.py:216:12: W0212: Access to a protected member __color of a client class (protected-access)
core/checker.py:217:12: W0212: Access to a protected member __owner of a client class (protected-access)
core/checker.py:218:12: W0212: Access to a protected member __point of a client class (protected-access)
core/checker.py:219:12: W0212: Access to a protected member __state of a client class (protected-access)
core/checker.py:2:0: W0611: Unused Player imported from core.player (unused-import)
************* Module core.game
core/game.py:109:0: C0304: Final newline missing (missing-final-newline)
core/game.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/game.py:1:0: W0611: Unused Player imported from core.player (unused-import)
core/game.py:2:0: W0611: Unused Board imported from core.board (unused-import)
core/game.py:3:0: W0611: Unused Dice imported from core.dice (unused-import)
************* Module core.board
core/board.py:19:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:179:0: C0325: Unnecessary parens after 'not' keyword (superfluous-parens)
core/board.py:255:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:286:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:307:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:311:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:321:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:350:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:356:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:362:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:374:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:377:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:381:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:386:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:450:0: C0304: Final newline missing (missing-final-newline)
core/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/board.py:324:4: R0912: Too many branches (21/12) (too-many-branches)
core/board.py:324:4: R0915: Too many statements (56/50) (too-many-statements)
core/board.py:1:0: W0611: Unused Player imported from core.player (unused-import)
************* Module core.player
core/player.py:111:0: C0301: Line too long (120/100) (line-too-long)
core/player.py:127:0: C0304: Final newline missing (missing-final-newline)
core/player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module core.dice
core/dice.py:18:0: C0303: Trailing whitespace (trailing-whitespace)
core/dice.py:108:0: C0303: Trailing whitespace (trailing-whitespace)
core/dice.py:113:0: C0303: Trailing whitespace (trailing-whitespace)
core/dice.py:116:0: C0301: Line too long (104/100) (line-too-long)
core/dice.py:118:0: C0325: Unnecessary parens after 'not' keyword (superfluous-parens)
core/dice.py:121:0: C0303: Trailing whitespace (trailing-whitespace)
core/dice.py:122:0: C0304: Final newline missing (missing-final-newline)
core/dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module cli.CLI
cli/CLI.py:1:0: C0114: Missing module docstring (missing-module-docstring)
cli/CLI.py:1:0: C0103: Module name "CLI" doesn't conform to snake_case naming style (invalid-name)
cli/CLI.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
cli/CLI.py:21:0: C0116: Missing function or method docstring (missing-function-docstring)
cli/CLI.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 0.00/10


```
