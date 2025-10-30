import unittest
from unittest.mock import patch, MagicMock, call
from io import StringIO

from cli.CLI import mostrar_encabezado, mostrar_menu, mostrar_tablero, main
from core.board import Board
from excepciones.excepciones import NotYourCheckerError


class TestMostrarEncabezado(unittest.TestCase):
    """Tests para la función mostrar_encabezado."""
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_mostrar_encabezado_imprime_titulo(self, mock_stdout):
        """Verifica que mostrar_encabezado() imprime el título correctamente."""
        mostrar_encabezado()
        output = mock_stdout.getvalue()
        
        self.assertIn("===================================", output)
        self.assertIn("BACKGAMMON", output)
        self.assertEqual(output.count("==================================="), 2)


class TestMostrarMenu(unittest.TestCase):
    """Tests para la función mostrar_menu."""
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_mostrar_menu_imprime_opciones(self, mock_stdout):
        """Verifica que mostrar_menu() imprime todas las opciones."""
        mostrar_menu()
        output = mock_stdout.getvalue()
        
        self.assertIn("Opciones:", output)
        self.assertIn("1. Tirar los dados", output)
        self.assertIn("2. Realizar movimiento", output)
        self.assertIn("3. Salir del juego", output)


class TestMostrarTablero(unittest.TestCase):
    """Tests para la función mostrar_tablero."""
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_mostrar_tablero_con_render_normal(self, mock_stdout):
        """Verifica que mostrar_tablero() usa render() cuando no hay render_pretty()."""
        board = Board()
        mostrar_tablero(board)
        output = mock_stdout.getvalue()
        
        self.assertIn("Tablero actual:", output)
        # Debería contener algunas líneas del tablero
        self.assertIn("00:", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_mostrar_tablero_con_render_pretty(self, mock_stdout):
        """Verifica que mostrar_tablero() usa render_pretty() si existe."""
        board = MagicMock()
        board.render_pretty = MagicMock(return_value="Tablero bonito")
        board.render = MagicMock(return_value="Tablero normal")
        
        mostrar_tablero(board)
        output = mock_stdout.getvalue()
        
        self.assertIn("Tablero actual:", output)
        self.assertIn("Tablero bonito", output)
        board.render_pretty.assert_called_once()
        board.render.assert_not_called()
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_mostrar_tablero_sin_render_pretty(self, mock_stdout):
        """Verifica que mostrar_tablero() usa render() cuando no existe render_pretty()."""
        board = MagicMock()
        board.render = MagicMock(return_value="Tablero normal")
        # No tiene render_pretty
        delattr(board, 'render_pretty') if hasattr(board, 'render_pretty') else None
        
        mostrar_tablero(board)
        output = mock_stdout.getvalue()
        
        self.assertIn("Tablero actual:", output)
        self.assertIn("Tablero normal", output)
        board.render.assert_called_once()


class TestMainSalirInmediato(unittest.TestCase):
    """Tests para main() cuando el usuario elige salir inmediatamente."""
    
    @patch('builtins.input', side_effect=['3'])  # Elige opción 3 (salir)
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_salir_inmediato(self, mock_stdout, mock_input):
        """Verifica que main() permite salir inmediatamente con opción 3."""
        main()
        output = mock_stdout.getvalue()
        
        self.assertIn("Saliendo del juego", output)
        self.assertIn("Gracias por jugar", output)


class TestMainTirarDados(unittest.TestCase):
    """Tests para main() cuando el usuario tira los dados."""
    
    @patch('builtins.input', side_effect=['1', '', '', '3']) 
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_tirar_dados(self, mock_stdout, mock_input):
        """Verifica que main() permite tirar los dados correctamente."""
        main()
        output = mock_stdout.getvalue()
        
        self.assertIn("Tirada de dados:", output)


class TestMainRealizarMovimiento(unittest.TestCase):
    """Tests para main() cuando el usuario realiza un movimiento."""
    
    @patch('builtins.input', side_effect=['2', '12', '10', '', '3'])  
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_movimiento_exitoso(self, mock_stdout, mock_input):
        """Verifica que main() procesa un movimiento exitoso."""
        main()
        output = mock_stdout.getvalue()
        
        self.assertIn("Desde punto", output)
        self.assertIn("hasta punto", output)


class TestMainOpcionInvalida(unittest.TestCase):
    """Tests para main() cuando el usuario elige una opción inválida."""
    
    @patch('builtins.input', side_effect=['99', '' ,'3'])  # Opción inválida, luego salir
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_opcion_invalida(self, mock_stdout, mock_input):
        """Verifica que main() maneja opciones inválidas correctamente."""
        main()
        output = mock_stdout.getvalue()
        
        self.assertIn("Opción inválida", output)
        self.assertIn("Intentá nuevamente", output)


class TestMainMovimientoConError(unittest.TestCase):
    """Tests para main() cuando hay errores en los movimientos."""
    
    @patch('builtins.input', side_effect=['2', 'abc', '', '3'])  # Opción 2, entrada inválida, salir
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_movimiento_valor_invalido(self, mock_stdout, mock_input):
        """Verifica que main() maneja ValueError al ingresar datos no numéricos."""
        main()
        output = mock_stdout.getvalue()
        
        self.assertIn("Ingresá números válidos", output)
    
    @patch('cli.CLI.Board')
    @patch('builtins.input', side_effect=['2', '0', '10', '', '3'])  # Intenta mover ficha que no es suya
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_movimiento_error_backgammon(self, mock_stdout, mock_input, MockBoard):
        """Verifica que main() maneja errores de BackgammonError."""
        # Configurar el mock del tablero para lanzar error
        mock_board_instance = MagicMock()
        mock_board_instance.apply_move.side_effect = NotYourCheckerError("No es tu ficha")
        mock_board_instance.render.return_value = "Tablero"
        MockBoard.return_value = mock_board_instance
        
        main()
        output = mock_stdout.getvalue()
        
        self.assertIn("Error:", output)


class TestMainGanador(unittest.TestCase):
    """Tests para main() cuando hay un ganador."""
    
    @patch('cli.CLI.Game')
    @patch('builtins.input', side_effect=['1', ''])  # Tira dados una vez
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_con_ganador(self, mock_stdout, mock_input, MockGame):
        """Verifica que main() detecta y anuncia al ganador."""
        # Configurar el mock del juego para simular victoria
        mock_game_instance = MagicMock()
        mock_winner = MagicMock()
        mock_winner.name = "Jugador 1"
        
        # Primero winner es None, luego tiene valor
        mock_game_instance.winner = None
        mock_game_instance.current_player = MagicMock(name="Jugador 1", color="white")
        mock_game_instance.roll_dice.return_value = [3, 5]
        
        # En la segunda iteración del while, hay ganador
        def side_effect_winner(*args, **kwargs):
            mock_game_instance.winner = mock_winner
        
        mock_game_instance.roll_dice.side_effect = side_effect_winner
        MockGame.return_value = mock_game_instance
        
        main()
        output = mock_stdout.getvalue()
        
        self.assertIn("ha ganado la partida", output)


class TestMainIntegracion(unittest.TestCase):
    """Tests de integración para main()."""
    
    @patch('builtins.input', side_effect=['1', '', '', '2', '12', '10', '', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_flujo_completo(self, mock_stdout, mock_input):
        """Verifica un flujo completo: tirar dados, mover, salir."""
        main()
        output = mock_stdout.getvalue()
        
        # Verifica que se ejecutaron todas las acciones
        self.assertIn("BACKGAMMON", output)
        self.assertIn("Tirada de dados:", output)
        self.assertIn("Saliendo del juego", output)


if __name__ == "__main__":
    unittest.main()