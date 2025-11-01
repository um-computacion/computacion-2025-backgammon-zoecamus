# Automated Reports

## Coverage Report
```text
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
cli/__init__.py                  0      0   100%
core/__init__.py                 0      0   100%
core/board.py                  188     13    93%   140, 234-238, 317, 341, 358, 364, 377, 387, 417
core/checker.py                 66      5    92%   5-6, 67, 77, 107
core/dice.py                    44      0   100%
core/game.py                    35      0   100%
core/player.py                  39      0   100%
excepciones/__init__.py          0      0   100%
excepciones/excepciones.py      33      0   100%
gui/__init__.py                  0      0   100%
test/__init__.py                 0      0   100%
test/test_board.py             251      4    98%   36, 43, 136, 451
test/test_checker.py            68      1    99%   109
test/test_cli.py               240      4    98%   36, 43, 136, 434
test/test_dice.py               89      1    99%   150
test/test_game.py               65      1    98%   85
test/test_player.py             61      1    98%   105
----------------------------------------------------------
TOTAL                         1179     30    97%

```

## Pylint Report
```text
************* Module test.test_cli
test/test_cli.py:188:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:192:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:197:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:200:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:203:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:207:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:210:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:214:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:298:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:303:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:306:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:316:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:318:68: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:327:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:330:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:333:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:344:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:347:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:350:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:361:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:365:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:368:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:379:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:382:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:395:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:398:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:409:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:414:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:423:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:428:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_cli.py:434:0: C0304: Final newline missing (missing-final-newline)
test/test_cli.py:1:0: C0114: Missing module docstring (missing-module-docstring)
test/test_cli.py:4:0: W0611: Unused BearOffNotAllowedError imported from excepciones.excepciones (unused-import)
test/test_cli.py:4:0: W0611: Unused IllegalReentryPointError imported from excepciones.excepciones (unused-import)
test/test_cli.py:4:0: W0611: Unused BlockedPointError imported from excepciones.excepciones (unused-import)
************* Module test.test_checker
test/test_checker.py:8:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:11:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:17:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:22:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:25:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:30:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:33:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:39:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:44:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:49:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:52:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:58:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:63:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:68:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:72:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:77:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:84:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:90:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:97:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:101:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_checker.py:109:0: C0304: Final newline missing (missing-final-newline)
test/test_checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
test/test_checker.py:14:8: C0415: Import outside toplevel (excepciones.excepciones.InvalidColorError) (import-outside-toplevel)
************* Module test.test_player
test/test_player.py:8:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:13:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:18:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:21:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:27:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:31:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:36:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:39:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:42:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:47:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:50:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:55:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:60:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:66:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:71:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:78:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:85:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:89:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:93:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:97:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_player.py:105:0: C0304: Final newline missing (missing-final-newline)
test/test_player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module test.test_game
test/test_game.py:85:0: C0304: Final newline missing (missing-final-newline)
test/test_game.py:1:0: C0114: Missing module docstring (missing-module-docstring)
test/test_game.py:7:0: C0115: Missing class docstring (missing-class-docstring)
test/test_game.py:15:4: C0116: Missing function or method docstring (missing-function-docstring)
test/test_game.py:20:4: C0116: Missing function or method docstring (missing-function-docstring)
test/test_game.py:27:4: C0116: Missing function or method docstring (missing-function-docstring)
test/test_game.py:35:4: C0116: Missing function or method docstring (missing-function-docstring)
test/test_game.py:38:4: C0116: Missing function or method docstring (missing-function-docstring)
test/test_game.py:49:4: C0116: Missing function or method docstring (missing-function-docstring)
test/test_game.py:60:0: C0115: Missing class docstring (missing-class-docstring)
test/test_game.py:61:4: C0116: Missing function or method docstring (missing-function-docstring)
test/test_game.py:70:0: C0115: Missing class docstring (missing-class-docstring)
test/test_game.py:78:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module test.test_dice
test/test_dice.py:8:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:13:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:16:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:21:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:27:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:31:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:35:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:39:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:43:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:47:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:50:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:53:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:57:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:60:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:63:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:67:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:70:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:73:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:79:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:81:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:87:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:89:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:94:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:100:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:103:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:106:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:111:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:114:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:117:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:123:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:126:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:132:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:135:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:139:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:143:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_dice.py:150:0: C0304: Final newline missing (missing-final-newline)
test/test_dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module test.test_board
test/test_board.py:193:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:197:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:202:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:205:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:208:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:214:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:217:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:223:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:229:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:315:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:320:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:323:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:333:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:335:68: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:344:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:347:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:350:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:361:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:364:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:367:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:378:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:382:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:385:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:396:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:399:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:412:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:415:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:426:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:430:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:440:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:444:0: C0303: Trailing whitespace (trailing-whitespace)
test/test_board.py:451:0: C0304: Final newline missing (missing-final-newline)
test/test_board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
test/test_board.py:4:0: W0611: Unused BearOffNotAllowedError imported from excepciones.excepciones (unused-import)
test/test_board.py:4:0: W0611: Unused IllegalReentryPointError imported from excepciones.excepciones (unused-import)
test/test_board.py:4:0: W0611: Unused BlockedPointError imported from excepciones.excepciones (unused-import)
************* Module core.checker
core/checker.py:180:0: C0325: Unnecessary parens after 'not' keyword (superfluous-parens)
core/checker.py:220:0: C0304: Final newline missing (missing-final-newline)
core/checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/checker.py:5:7: W0718: Catching too general exception Exception (broad-exception-caught)
core/checker.py:2:0: W0611: Unused Player imported from core.player (unused-import)
************* Module core.game
core/game.py:109:0: C0304: Final newline missing (missing-final-newline)
core/game.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/game.py:1:0: W0611: Unused Player imported from core.player (unused-import)
core/game.py:2:0: W0611: Unused Board imported from core.board (unused-import)
core/game.py:3:0: W0611: Unused Dice imported from core.dice (unused-import)
************* Module core.board
core/board.py:178:0: C0325: Unnecessary parens after 'not' keyword (superfluous-parens)
core/board.py:253:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:283:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:347:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:353:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:359:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:371:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:374:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:378:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:383:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:447:0: C0304: Final newline missing (missing-final-newline)
core/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/board.py:290:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
core/board.py:286:4: R0911: Too many return statements (9/6) (too-many-return-statements)
core/board.py:321:4: R0912: Too many branches (21/12) (too-many-branches)
core/board.py:321:4: R0915: Too many statements (56/50) (too-many-statements)
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
cli/CLI.py:43:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:48:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:52:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:61:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:64:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:69:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:84:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:86:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:94:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:96:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:97:0: C0301: Line too long (113/100) (line-too-long)
cli/CLI.py:111:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:126:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:129:0: C0301: Line too long (104/100) (line-too-long)
cli/CLI.py:131:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:134:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:166:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:175:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:177:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:182:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:193:0: C0301: Line too long (105/100) (line-too-long)
cli/CLI.py:223:0: C0304: Final newline missing (missing-final-newline)
cli/CLI.py:95:20: W1401: Anomalous backslash in string: '\ '. String constant might be missing an r prefix. (anomalous-backslash-in-string)
cli/CLI.py:1:0: C0114: Missing module docstring (missing-module-docstring)
cli/CLI.py:1:0: C0103: Module name "CLI" doesn't conform to snake_case naming style (invalid-name)
cli/CLI.py:30:0: R0914: Too many local variables (22/15) (too-many-locals)
cli/CLI.py:46:4: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
cli/CLI.py:46:4: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
cli/CLI.py:46:4: R1702: Too many nested blocks (8/5) (too-many-nested-blocks)
cli/CLI.py:174:26: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
cli/CLI.py:46:4: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
cli/CLI.py:30:0: R0912: Too many branches (44/12) (too-many-branches)
cli/CLI.py:30:0: R0915: Too many statements (131/50) (too-many-statements)
cli/CLI.py:6:0: C0411: standard import "os" should be placed before first party imports "core.board.Board", "core.dice.Dice", "core.game.Game", "core.player.Player", "excepciones.excepciones.BackgammonError"  (wrong-import-order)
************* Module gui.PygameUI
gui/PygameUI.py:131:0: C0301: Line too long (106/100) (line-too-long)
gui/PygameUI.py:1:0: C0114: Missing module docstring (missing-module-docstring)
gui/PygameUI.py:1:0: C0103: Module name "PygameUI" doesn't conform to snake_case naming style (invalid-name)
gui/PygameUI.py:57:0: R0902: Too many instance attributes (33/7) (too-many-instance-attributes)
gui/PygameUI.py:61:8: E1101: Module 'pygame' has no 'init' member (no-member)
gui/PygameUI.py:169:4: R0911: Too many return statements (8/6) (too-many-return-statements)
gui/PygameUI.py:169:4: R0912: Too many branches (17/12) (too-many-branches)
gui/PygameUI.py:333:4: R0914: Too many local variables (19/15) (too-many-locals)
gui/PygameUI.py:507:4: R0914: Too many local variables (24/15) (too-many-locals)
gui/PygameUI.py:676:46: R1714: Consider merging these comparisons with 'in' by using 'punto in (-2, self.__punto_seleccionado__)'. Use a set instead if elements are hashable. (consider-using-in)
gui/PygameUI.py:587:4: R0912: Too many branches (39/12) (too-many-branches)
gui/PygameUI.py:587:4: R0915: Too many statements (108/50) (too-many-statements)
gui/PygameUI.py:637:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
gui/PygameUI.py:740:33: E1101: Module 'pygame' has no 'QUIT' member (no-member)
gui/PygameUI.py:742:35: E1101: Module 'pygame' has no 'MOUSEBUTTONDOWN' member (no-member)
gui/PygameUI.py:754:8: E1101: Module 'pygame' has no 'quit' member (no-member)
gui/PygameUI.py:93:4: W0238: Unused private member `BackgammonUI.__mensaje(self)` (unused-private-member)
gui/PygameUI.py:97:4: W0238: Unused private member `BackgammonUI.__color_mensaje(self)` (unused-private-member)
gui/PygameUI.py:57:0: R0903: Too few public methods (1/2) (too-few-public-methods)
gui/PygameUI.py:758:0: C0116: Missing function or method docstring (missing-function-docstring)
gui/PygameUI.py:1:0: R0801: Similar lines in 2 files
==test.test_board:[10:203]
==test.test_cli:[10:198]
class TestBoardBearOffExtra(unittest.TestCase):
    """Tests adicionales para mejorar coverage de bearing off"""

    def setUp(self):
        self.board = Board()
        self.white = Player("White", "white")
        self.black = Player("Black", "black")

    def test_bear_off_with_all_in_home(self):
        """Test bearing off cuando todas las fichas están en casa"""
        board = Board()

        # Detectar atributo interno
        points_attr = "_points" if hasattr(board, "_points") else "points"
        points = list(getattr(board, points_attr))  # convertimos a lista

        # Limpiar puntos del tablero
        for i in range(24):
            if isinstance(points[i], dict):
                points[i].clear()
            else:
                points[i] = {}

        # Reasignar la lista modificada si es posible
        if hasattr(board, "_points"):
            board.__points__ = points
        elif hasattr(board, "points"):
            # algunos Board usan propiedad → no reasignable, pero igual testea lógica de home
            pass

        # Colocar fichas blancas solo en casa (0–5)
        if hasattr(board, "_points"):
            board.__points__[2] = {"color": "white", "count": 15}
        board.__borne_off_white__ = 0 if hasattr(board, "_borne_off_white") else 0

        # Verificar que está en casa
        self.assertTrue(board.in_home(self.white))


    def test_legal_moves_empty_dice(self):
        """Test movimientos legales con dados vacíos"""
        moves = self.board.legal_moves(self.white, [])
        self.assertEqual(moves, [])


class TestBoardEdgeCases(unittest.TestCase):
    """Tests para casos límite adicionales"""

    def setUp(self):
        self.board = Board()
        self.white = Player("White", "white")
        self.black = Player("Black", "black")

    def test_bar_count(self):
        """Test contar fichas en barra"""
        self.assertEqual(self.board.bar_count("white"), 0)
        self.assertEqual(self.board.bar_count("black"), 0)

    def test_borne_off_count(self):
        """Test contar fichas sacadas"""
        self.assertEqual(self.board.borne_off_count("white"), 0)
        self.assertEqual(self.board.borne_off_count("black"), 0)

    def test_home_range_for_white(self):
        """Test rango de casa para blancas"""
        self.assertEqual(list(Board.home_range_for("white")), list(range(0, 6)))

    def test_home_range_for_black(self):
        """Test rango de casa para negras"""
        self.assertEqual(list(Board.home_range_for("black")), list(range(18, 24)))

    def test_total_on_board(self):
        """Test contar fichas en tablero"""
        self.assertEqual(self.board.total_on_board("white"), 15)
        self.assertEqual(self.board.total_on_board("black"), 15)

    def test_points_property_is_tuple(self):
        """Test que points retorna una tupla inmutable"""
        points = self.board.points
        self.assertIsInstance(points, tuple)
        self.assertEqual(len(points), 24)


class TestBoardLegalMovesExtra(unittest.TestCase):
    """Tests adicionales para legal_moves"""

    def setUp(self):
        self.board = Board()
        self.white = Player("White", "white")
        self.black = Player("Black", "black")

    def test_legal_moves_with_single_die(self):
        """Test movimientos con un solo dado"""
        moves = self.board.legal_moves(self.white, [3])
        self.assertIsInstance(moves, list)

    def test_legal_moves_initial_position_black(self):
        """Test movimientos legales para negras desde posición inicial"""
        moves = self.board.legal_moves(self.black, [2, 4])
        self.assertIsInstance(moves, list)
        for move in moves:
            self.assertIsInstance(move, tuple)
            self.assertEqual(len(move), 2)


class TestBoardRenderExtra(unittest.TestCase):
    """Tests adicionales para render"""

    def test_render_contains_all_points(self):
        """Test que render contiene todos los puntos"""
        board = Board()
        rendered = board.render()
        for i in range(24):
            self.assertIn(f"{i:02d}:", rendered)

    def test_render_empty_point(self):
        """Test que render muestra puntos vacíos correctamente"""
        board = Board()
        # Buscar atributo de puntos sin usar doble subrayado
        points_attr = "_points" if hasattr(board, "_points") else "points"
        points = list(getattr(board, points_attr))

        # Modificamos temporalmente
        points[10] = {"color": None, "count": 0}
        if hasattr(board, "_points"):
            board.__points__ = points

        rendered = board.render()
        self.assertIn("10:", rendered)
        self.assertTrue("vacío" in rendered.lower() or "empty" in rendered.lower())


class TestBoardPrivateMethods(unittest.TestCase):
    """Cubre métodos privados de Board y ramas poco usadas."""

    def setUp(self):
        self.board = Board()
        self.white = Player("White", "white")
        self.black = Player("Black", "black")

    def test_calculate_entry_point_white_y_black(self):
        """Cubre __calculate_entry_point__ para ambos colores"""
        b = self.board
        # Blancas
        self.assertEqual(b.__calculate_entry_point__("white", 3), 21)
        # Negras
        self.assertEqual(b.__calculate_entry_point__("black", 3), 2)
        # Valores fuera de rango
        self.assertIsNone(b.__calculate_entry_point__("white", 25))
        self.assertIsNone(b.__calculate_entry_point__("black", 0))

    def test_validate_point_error(self):
        """Cubre __validate_point__ con índice fuera de rango"""
        b = self.board
        with self.assertRaises(Exception):
            b.__validate_point__(-1)
        with self.assertRaises(Exception):
            b.__validate_point__(24)

    def test_is_blocked_for(self):
        """Cubre __is_blocked_for__"""
        b = self.board
        b.__points__[5] = {"color": "black", "count": 2}
        self.assertTrue(b.__is_blocked_for__("white", 5))
        b.__points__[5] = {"color": "white", "count": 1}
        self.assertFalse(b.__is_blocked_for__("white", 5))

    def test_ensure_can_enter_exceptions(self):
        """Cubre __ensure_can_enter__ lanzando IllegalReentryPointError"""
        b = self.board
        b.__points__[3] = {"color": "black", "count": 3}
        with self.assertRaises(Exception):
            b.__ensure_can_enter__("white", 3)

    def test_can_bear_off_from_exact_and_higher_die(self):
        """
        Cubre __can_bear_off_from__ con exacto y dado alto.

        NOTA: Este test está adaptado al comportamiento ACTUAL del código,
        que tiene un BUG en la línea 297. Ver BUG_REPORT.md para más detalles.
        """
        b = self.board

        # Test 1: Exacto (dado justo para salir)
        # Ficha en punto 0, dado 1 -> 0 - 1 = -1 (exacto para white)
        self.assertTrue(b.__can_bear_off_from__(0, 1, "white", -1))

        # Test 2: Dado alto CON fichas en puntos 1-5 (no se puede sacar)
        # Limpiar el tablero
        for i in range(24):
            b.__points__[i] = None

        b.__points__[0] = {"color": "white", "count": 1} (duplicate-code)
gui/PygameUI.py:1:0: R0801: Similar lines in 2 files
==test.test_board:[238:427]
==test.test_cli:[221:410]
        b = self.board
        b.__send_to_bar__("white")
        b.__send_to_bar__("black")
        self.assertEqual(b.bar_count("white"), 1)
        self.assertEqual(b.bar_count("black"), 1)


class TestBoardApplyMoveExtra(unittest.TestCase):
    """Cubre ramas especiales de apply_move"""

    def setUp(self):
        self.board = Board()
        self.white = Player("White", "white")

    def test_invalid_move_format(self):
        """Cubre InvalidMoveError con formato incorrecto"""
        with self.assertRaises(Exception):
            self.board.apply_move(self.white, "movimiento inválido")

    def test_blocked_point_error(self):
        """Cubre BlockedPointError"""
        b = self.board
        b.__points__[5] = {"color": "black", "count": 2}
        b.__points__[4] = {"color": "white", "count": 1}
        with self.assertRaises(Exception):
            b.apply_move(self.white, (4, 5))

    def test_not_your_checker_error(self):
        """Cubre NotYourCheckerError"""
        b = self.board
        b.__points__[3] = {"color": "black", "count": 1}
        with self.assertRaises(Exception):
            b.apply_move(self.white, (3, 4))

    def test_invalid_bearoff_without_home(self):
        """Cubre BearOffNotAllowedError"""
        b = self.board
        with self.assertRaises(Exception):
            b.apply_move(self.white, ("bearoff", 0))

    def test_render_output_contains_vacio_and_colors(self):
        """Cubre render() completamente"""
        b = Board()
        out = b.render()
        self.assertIn("vacío", out)
        self.assertIn("B x", out)
        self.assertIn("W x", out)


class TestBoardCoverageImprovements(unittest.TestCase):
    """Tests adicionales para mejorar coverage de líneas específicas"""

    def setUp(self):
        self.board = Board()
        self.white = Player("White", "white")
        self.black = Player("Black", "black")

    def test_in_home_all_borne_off(self):
        """Cubre la línea 146: todas las fichas sacadas"""
        b = self.board
        # Simular que todas las fichas fueron sacadas
        b.__borne_off_white__ = 15
        self.assertTrue(b.in_home(self.white))

    def test_has_won_returns_true(self):
        """Cubre has_won cuando el jugador ganó"""
        b = self.board
        b.__borne_off_white__ = 15
        self.assertTrue(b.has_won(self.white))

    def test_legal_moves_with_bearoff_possible(self):
        """Cubre líneas 255-258: bearing off en legal_moves"""
        b = Board()
        # Limpiar tablero
        for i in range(24):
            b.__points__[i] = None

        # Poner todas las fichas blancas en casa
        b.__points__[0] = {"color": "white", "count": 15}
        b.__borne_off_white__ = 0
        b.__bar_white__ = 0

        # Obtener movimientos legales con dado 1
        moves = b.legal_moves(self.white, [1])

        # Debe incluir bearing off
        bearoff_moves = [m for m in moves if m[0] == "bearoff"]
        self.assertTrue(len(bearoff_moves) > 0)

    def test_legal_moves_normal_move_in_bounds(self):
        """Cubre líneas 260-263: movimiento normal dentro del tablero"""
        b = Board()
        # Configuración inicial ya tiene movimientos normales posibles
        moves = b.legal_moves(self.white, [1])

        # Debe haber movimientos normales (origen, destino)
        normal_moves = [m for m in moves if isinstance(m, tuple) and
                       isinstance(m[0], int) and isinstance(m[1], int)]
        self.assertTrue(len(normal_moves) > 0)

    def test_apply_move_reentry_capture(self):
        """Cubre líneas 348-352: captura durante reingreso"""
        b = Board()
        # Poner ficha blanca en la barra
        b.__bar_white__ = 1

        # Poner UNA ficha negra en el punto de entrada (24-3=21)
        b.__points__[21] = {"color": "black", "count": 1}

        # Reingresar debería capturar
        b.apply_move(self.white, ("reentry", 21))

        # La ficha negra debe estar en la barra
        self.assertEqual(b.bar_count("black"), 1)
        # La ficha blanca debe estar en el punto 21
        self.assertEqual(b.__points__[21]["color"], "white")

    def test_apply_move_reentry_empty_point(self):
        """Cubre líneas 355-358: reingreso en punto vacío"""
        b = Board()
        # Poner ficha blanca en la barra
        b.__bar_white__ = 1

        # Asegurar que el punto 21 está vacío
        b.__points__[21] = None

        # Reingresar
        b.apply_move(self.white, ("reentry", 21))

        # Debe crear nueva ficha en punto vacío
        self.assertEqual(b.__points__[21]["color"], "white")
        self.assertEqual(b.__points__[21]["count"], 1)

    def test_apply_move_bearoff_last_checker(self):
        """Cubre líneas 380-382: sacar última ficha del punto"""
        b = Board()
        # Limpiar y poner solo una ficha en casa
        for i in range(24):
            b.__points__[i] = None

        b.__points__[0] = {"color": "white", "count": 1}
        b.__borne_off_white__ = 14
        b.__bar_white__ = 0

        # Sacar la ficha
        b.apply_move(self.white, ("bearoff", 0))

        # El punto debe quedar None
        self.assertIsNone(b.__points__[0])

    def test_apply_move_normal_capture(self):
        """Cubre líneas 404-407: captura en movimiento normal"""
        b = Board()
        # Poner ficha blanca
        b.__points__[12] = {"color": "white", "count": 1}
        # Poner UNA ficha negra en destino
        b.__points__[11] = {"color": "black", "count": 1}

        # Mover debería capturar
        b.apply_move(self.white, (12, 11))

        # Ficha negra en la barra
        self.assertEqual(b.bar_count("black"), 1)
        # Ficha blanca en destino
        self.assertEqual(b.__points__[11]["color"], "white")

    def test_apply_move_normal_to_empty(self):
        """Cubre líneas 414-417: movimiento a punto vacío"""
        b = Board()
        # Poner ficha blanca
        b.__points__[12] = {"color": "white", "count": 2}
        # Asegurar destino vacío
        b.__points__[11] = None

        # Mover
        b.apply_move(self.white, (12, 11))

        # Debe crear nueva ficha en punto vacío
        self.assertEqual(b.__points__[11]["color"], "white")
        self.assertEqual(b.__points__[11]["count"], 1)
        self.assertEqual(b.__points__[12]["count"], 1)

    def test_can_bear_off_white_normal_cases(self):
        """Casos adicionales de bearing off para blancas"""
        b = Board()
        for i in range(24):
            b.__points__[i] = None

        # Caso: Ficha en punto 2, dado 3 -> exacto (duplicate-code)
gui/PygameUI.py:1:0: R0801: Similar lines in 2 files
==test.test_board:[230:238]
==test.test_cli:[406:419]
        for i in range(24):
            b.__points__[i] = None
        b.__points__[23] = {"color": "black", "count": 1}
        b.__points__[20] = {"color": "black", "count": 1}  # Más cerca del inicio
        self.assertFalse(b.__can_bear_off_from__(23, 6, "black", 1))

    def test_send_to_bar(self):
        """Cubre __send_to_bar__""" (duplicate-code)
gui/PygameUI.py:1:0: R0801: Similar lines in 2 files
==test.test_board:[199:210]
==test.test_cli:[420:432]
        for i in range(24):
            b.__points__[i] = None

        b.__points__[0] = {"color": "white", "count": 1}
        b.__points__[3] = {"color": "white", "count": 1}  # Ficha en rango 1-5

        # Dado 6 desde punto 0: 0 - 6 = -6 < -1, pero hay fichas en rango 1-5
        self.assertFalse(b.__can_bear_off_from__(0, 6, "white", -1))

        # Test 3: Dado alto SIN fichas en puntos 1-5 (sí se puede sacar)
        # IMPORTANTE: El código actual verifica range(1,6), no range(point_index+1, 6) (duplicate-code)

-----------------------------------
Your code has been rated at 8.37/10


```
