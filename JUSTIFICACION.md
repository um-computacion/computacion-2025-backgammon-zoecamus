## Justificación de las clases elegidas

- **Player:**  
  Representa a cada jugador.  
  **Responsabilidad:** encapsular nombre, color y dirección de movimiento.  
  **Motivo:** evita duplicar lógica de jugador y facilita alternancia de turnos.

- **Dice:**  
  Modela los dados de seis caras.  
  **Responsabilidad:** generar tiradas válidas y manejar casos especiales (dobles).  
  **Motivo:** desacoplar la generación aleatoria de la lógica del juego.

- **Board:**  
  Representa los 24 puntos del tablero y el estado de las fichas.  
  **Responsabilidad:** manejar la distribución inicial, las reglas de movimiento, capturas, reingresos y bearing off.  
  **Motivo:** centralizar la lógica de validación y estado del juego.

- **Game:**  
  Orquesta la partida.  
  **Responsabilidad:** controlar turnos, invocar tiradas de dados, delegar movimientos al tablero y detectar fin del juego.  
  **Motivo:** aplicar separación entre la interfaz (CLI o GUI) y la lógica interna.

- **Excepciones personalizadas:**  
  Cada módulo define errores propios (ej. `InvalidMoveError`, `BlockedPointError`, `NotYourCheckerError`).  
  **Motivo:** mejorar la trazabilidad de errores y simplificar los tests.

---

## Justificación de atributos principales

| Clase | Atributo | Motivo |
|-------|-----------|--------|
| `Player` | `__name`, `__color`, `__direction` | Encapsulan información única e inmutable del jugador. |
| `Dice` | `__values`, `__used` | Mantienen control de tiradas y dados disponibles. |
| `Board` | `__points__`, `__bar`, `__borne_off` | Representan el estado completo del tablero según las reglas del juego. |
| `Game` | `__current_player`, `__winner`, `__last_roll` | Facilitan el control de flujo de la partida. |

---

## Decisiones de diseño relevantes

- **Encapsulamiento fuerte:** todos los atributos usan doble subrayado (`__attr`) para evitar acceso externo directo.
- **Inicialización estandarizada:** el método `_initial_points()` del `Board` replica la disposición clásica de fichas del Backgammon real.
- **Testing aislado:** uso de `unittest` y `MagicMock` para probar la clase `Game` sin depender de `Board` ni `Dice` reales.
- **Separación entre lógica y presentación:** el motor del juego (`core/`) no depende de `CLI` ni `pygame_ui`, permitiendo reutilización del mismo backend.

---

## Excepciones y manejo de errores

Jerarquía definida en `excepciones/excepciones.py`:

| Módulo | Excepciones | Motivo |
|--------|--------------|--------|
| **Player** | `InvalidColorError`, `InvalidDirectionError` | Validan entrada de jugador. |
| **Dice** | `InvalidDiceSidesError`, `InvalidDiceOverrideError` | Evitan estados inválidos. |
| **Board** | `InvalidMoveError`, `BlockedPointError`, `OutOfBoundsPointError`, `NotYourCheckerError`, `BearOffNotAllowedError` | Garantizan que las reglas se cumplan. |
| **Game** | `InvalidTurnError` | Controla coherencia del flujo de turnos. |

**Justificación:** usar excepciones específicas mejora la depuración, claridad y cobertura en los tests.

---

## Estrategias de testing y cobertura

- Framework: `unittest`  
- Se cubren:
  - Inicialización y atributos de todas las clases principales.  
  - Casos de uso válidos y excepciones.  
  - Flujos de juego (`Game.make_move`, `Board.apply_move`).  
  - Lógica de dados (`Dice.roll`, `Dice.use_die`).  
  - Validación de encapsulamiento (`__attr`).

- Uso de **Coverage.py** para medir líneas ejecutadas.  
  Meta de cobertura: **≥ 90 %** (actualmente en optimización).

---

## Cumplimiento de principios SOLID

| Principio | Aplicación |
|------------|-------------|
| **S (Single Responsibility)** | Cada clase tiene una única función clara. |
| **O (Open/Closed)** | Métodos listos para extensión sin modificar base. |
| **L (Liskov Substitution)** | Las instancias de `Player`, `Board`, `Dice` se intercambian sin romper dependencias. |
| **I (Interface Segregation)** | La lógica del juego (`Game`) no obliga a implementar métodos innecesarios. |
| **D (Dependency Inversion)** | `Game` depende de abstracciones (métodos públicos), no de implementaciones concretas. |

