# IronClash - Tareas para HacknPlan

---

## Resumen de duración del proyecto

| Métrica | Valor |
|--------|--------|
| **Duración por sprint** | **2 semanas** (80 h por desarrollador por sprint) |
| **Sprints totales** | 21 |
| **Horas totales estimadas** | ~1 130 h (suma de tareas) |
| **Tiempo total (1 dev, 40 h/semana)** | ~28–30 semanas (**~7 meses**) |
| **Tiempo total (2 devs, front/back en paralelo)** | ~16–20 semanas (**~4–5 meses**) |

El orden de los sprints sigue el **roadmap del GDD**: Fase 1 Core PvE → Fase 2 Progresión → Fase 3 Housing/Tienda/Contenido → Fase 4 PvP y polish → Torneos (fase posterior). Los sprints con menos de 80 h pueden combinarse con el siguiente o usarse como colchón; los que pasan de 80 h pueden dividirse en dos iteraciones o repartirse entre dos personas.

**Orden recomendado de sprints por fase:**

| Fase | Sprints | Contenido |
|------|---------|-----------|
| **Fase 1 - Core MVP PvE** | 1 → 2 → 3 → 4 → 5 → 6 | Setup, movimiento, combate, mapas, personajes, equipamiento |
| **Fase 2 - Progresión** | 7 → 8 → 14 → 19 | Level up, vidas, cofres, pasivas/habilidades de gear |
| **Fase 3 - Social y contenido** | 9 → 10 → 13 → 17 → 18 | Housing core, housing UI, tienda, expansión mapas/quests, amigos y visitar casas |
| **Fase 4 - PvP y cierre** | 11 → 12 → 16 → 20 → 21 | Matchmaking PvP, combate PvP, ranking/ligas, polish, testing |
| **Fase posterior** | 15 | Torneos en vivo |

---

## Sprint 1: Setup y Fundación (Fase 1 - Core)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~52 h
**Objetivo:** Establecer la base del proyecto y autenticación

### Backend
- [ ] **Setup FastAPI Project Structure**
  - Prioridad: Alta
  - Tipo: Task
  - Descripción: Crear estructura de carpetas (Domain, Services, API), configurar dependencias, setup de PostgreSQL y Redis
  - Estimación: 8h

- [ ] **Implementar Sistema de Autenticación (Login/Register)**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Endpoints para registro, login, JWT tokens, validación de sesión
  - Estimación: 12h

- [ ] **Setup Base de Datos - Esquema Inicial**
  - Prioridad: Alta
  - Tipo: Task
  - Descripción: Crear tablas: users, characters, gear, battles, snapshots
  - Estimación: 6h

- [ ] **API Health Check y Logging**
  - Prioridad: Media
  - Tipo: Task
  - Descripción: Endpoint de health check, configuración de logging estructurado
  - Estimación: 4h

### Frontend
- [ ] **Setup Proyecto Godot 4**
  - Prioridad: Alta
  - Tipo: Task
  - Descripción: Configurar proyecto base, estructura de carpetas, escenas principales
  - Estimación: 4h

- [ ] **Pantalla de Login/Registro**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: UI para login y registro, integración con API de auth
  - Estimación: 8h

- [ ] **Sistema de Navegación entre Escenas**
  - Prioridad: Alta
  - Tipo: Task
  - Descripción: SceneManager para transiciones entre Home, Combat, Settings
  - Estimación: 4h

- [ ] **Configuración de Exportación Multiplataforma**
  - Prioridad: Baja
  - Tipo: Task
  - Descripción: Setup de export templates para Android, iOS, PC
  - Estimación: 6h

---

## Sprint 2: Movimiento y Controles (Fase 1 - Core)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~36 h  
**Objetivo:** Sistema de movimiento y controles básicos del personaje

### Frontend
- [ ] **Sistema de Movimiento del Personaje**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Controles de movimiento (WASD/Joystick), física de movimiento, animaciones de caminar/correr
  - Estimación: 8h

- [ ] **Sistema de Cámara que Sigue al Jugador**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Cámara que sigue al personaje, límites de cámara, suavizado
  - Estimación: 6h

- [ ] **Input System Multiplataforma**
  - Prioridad: Alta
  - Tipo: Task
  - Descripción: Sistema de input que soporte teclado, mouse, touch y gamepad
  - Estimación: 6h

- [ ] **Animaciones Básicas de Personaje**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Idle, walk, run, animaciones de dirección (izquierda/derecha)
  - Estimación: 8h

### Backend
- [ ] **Validación de Movimiento en Servidor**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Validar posición del jugador, prevenir teleport/cheats, sincronización
  - Estimación: 8h

---

## Sprint 3: Combate Core - Controles Directos (Fase 1 - Core)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~62 h  
**Objetivo:** Sistema de combate con controles directos del jugador (PvE; la sincronización PvP va en Sprint 16)

### Frontend
- [ ] **Sistema de Ataque con Controles**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Botones/teclas para atacar, combo básico, animaciones de ataque
  - Estimación: 10h

- [ ] **Sistema de Dodge Manual**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Botón de dodge, invencibilidad temporal, animación de dodge
  - Estimación: 6h

- [ ] **Sistema de Block Manual**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Botón de block, reducción de daño mientras bloquea, animación
  - Estimación: 6h

- [ ] **Animaciones de Combate**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Animaciones de ataque, recibir daño, crítico, dodge, block
  - Estimación: 12h

- [ ] **Barras de Vida (HP) en UI**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: UI de barras de HP que se actualizan en tiempo real
  - Estimación: 4h

- [ ] **Efectos Visuales de Combate**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Partículas de impacto, críticos, efectos de dodge/block
  - Estimación: 8h

### Backend
- [ ] **Sistema de Stats Base (HP, ATK, DEF, SPD, CRIT, EVA)**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Modelo de stats, cálculo de stats base y con gear
  - Estimación: 6h

- [ ] **Cálculo de Daño en Servidor**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Fórmula de daño: ATK vs DEF, validación de daño aplicado
  - Estimación: 6h

- [ ] **Sistema de Críticos**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Check de CRIT en servidor, multiplicador x1.5, cálculo de probabilidad
  - Estimación: 4h

- [ ] **Validación de Acciones de Combate**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Validar ataques, dodge, block del cliente, prevenir cheats (PvE; PvP en Sprint 16)
  - Estimación: 10h

---

## Sprint 4: Mapas y Exploración (Fase 1 - Core)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~62 h  
**Objetivo:** Sistema de mapas explorables, enemigos PvE y drops (instancia en solitario, sin minimapa)

### Backend
- [ ] **Sistema de Mapas**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Modelo de mapas, zonas, puntos de spawn, límites de mapa
  - Estimación: 6h

- [ ] **API de Mapas**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Endpoints para obtener información de mapas, desbloqueo de zonas
  - Estimación: 4h

- [ ] **Sistema de Enemigos PvE**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Modelo de enemigos, spawn points, IA básica, stats de enemigos
  - Estimación: 8h

- [ ] **Sistema de Drops de Items**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Tablas de loot por enemigo, probabilidades, generación de drops
  - Estimación: 8h

### Frontend
- [ ] **Sistema de Mapas Base**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Cargar y renderizar mapas, colisiones, límites de mapa
  - Estimación: 10h

- [ ] **Sistema de Enemigos en Mapas**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Spawn de enemigos, IA básica (patrullaje, detección de jugador), combate PvE
  - Estimación: 12h

- [ ] **Sistema de Drops Visuales**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Items que aparecen en el suelo al derrotar enemigos, recoger items
  - Estimación: 8h

- [ ] ~~**Minimapa**~~ **No implementar** (GDD: el juego no tendrá minimapa; orientación por diseño de mapa y puntos de interés.)

- [ ] **Sistema de Navegación entre Mapas**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Transiciones entre mapas, puntos de entrada/salida, carga de escenas
  - Estimación: 6h

## Sprint 5: Personajes y Stats (Fase 1 - Core)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~40 h  
**Objetivo:** Sistema de personajes jugables

### Backend
- [ ] **Modelo de Personaje (Character)**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Schema de personaje con stats, nivel, experiencia, gear equipado, posición
  - Estimación: 6h

- [ ] **API CRUD de Personajes**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Endpoints para crear, leer, actualizar personajes del usuario
  - Estimación: 8h

- [ ] **Sistema de Experiencia y Nivel**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Ganar XP en combates PvE/PvP, cálculo de nivel up, guardar progreso
  - Estimación: 6h

### Frontend
- [ ] **Visualización de Personaje en Housing**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Sprite del personaje con animaciones idle/walking en casa
  - Estimación: 8h

- [ ] **Panel de Stats del Personaje**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: UI que muestra HP, ATK, DEF, SPD, CRIT, EVA del personaje
  - Estimación: 6h

- [ ] **Interacción con Personaje en Housing**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Al hacer click, abrir menú con stats, equipamiento, inventario
  - Estimación: 6h

---

## Sprint 6: Equipamiento Básico (Fase 1 - Core)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~52 h  
**Objetivo:** Sistema de gear funcional

### Backend
- [ ] **Modelo de Gear (Weapon/Armor)**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Schema de gear con stats, rareza, tipo (arma/armadura)
  - Estimación: 6h

- [ ] **Sistema de Rarezas**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Común, Poco Común, Raro, Épico, Legendario con colores
  - Estimación: 4h

- [ ] **API de Equipamiento**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Endpoints para equipar/desequipar gear, obtener inventario
  - Estimación: 8h

- [ ] **Aplicación de Stats de Gear**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Sumar stats del gear a stats base del personaje en combate
  - Estimación: 4h

### Frontend
- [ ] **UI de Inventario**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Panel que muestra gear disponible, filtros por tipo/rareza
  - Estimación: 10h

- [ ] **UI de Equipamiento**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Slots de arma/armadura, drag & drop para equipar
  - Estimación: 8h

- [ ] **Visualización de Gear en Personaje**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Mostrar arma/armadura visualmente en el sprite del personaje
  - Estimación: 12h

---

## Sprint 7: Progresión y Level Up (Fase 2 - Progresión)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~34 h  
**Objetivo:** Sistema de mejoras roguelike

### Backend
- [ ] **Sistema de Level Up con Elección**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Al subir nivel, generar 3 opciones aleatorias de mejoras
  - Estimación: 8h

- [ ] **Tipos de Mejoras**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Buff de stats, nueva arma, nueva armadura (con probabilidades)
  - Estimación: 6h

- [ ] **API de Selección de Mejora**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Endpoint para que jugador seleccione una de las 3 mejoras
  - Estimación: 4h

### Frontend
- [ ] **Pantalla de Level Up**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: UI que muestra 3 opciones de mejoras, selección del jugador
  - Estimación: 10h

- [ ] **Animación de Level Up**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Efecto visual cuando el personaje sube de nivel
  - Estimación: 6h

---

## Sprint 8: Sistema de Vidas (Fase 2 - Progresión)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~32 h  
**Objetivo:** Energía por personaje

### Backend
- [ ] **Modelo de Vidas por Personaje**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Cada personaje tiene vidas (max 5), timestamp de última regeneración
  - Estimación: 6h

- [ ] **Sistema de Regeneración de Vidas**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Regenerar 1 vida cada 25 minutos, calcular tiempo restante
  - Estimación: 8h

- [ ] **Consumo de Vidas en Combate**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Ganar -1 vida, perder -2 vidas, validar antes de iniciar combate
  - Estimación: 4h

- [ ] **API de Recarga de Vidas con Gems**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Endpoint para recargar todas las vidas pagando Gems
  - Estimación: 4h

### Frontend
- [ ] **UI de Vidas del Personaje**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Indicador visual de vidas restantes, timer de regeneración
  - Estimación: 6h

- [ ] **Validación de Vidas antes de Combate**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Mostrar error si no hay vidas suficientes, opción de recargar
  - Estimación: 4h

---

## Sprint 9: Housing Core - Grid, Placement y Almacenamiento (Fase 3 - Social)
**Duración aproximada:** 2–2,5 semanas · **Horas estimadas:** ~90 h (considerar repartir en 2 iteraciones)  
**Objetivo:** Sistema base de colocación de muebles y almacenamiento de items

### Backend
- [ ] **Modelo de Furniture**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Schema de muebles con tipo (floor/wall), posición, tamaño
  - Estimación: 6h

- [ ] **Sistema de Almacenamiento en Housing**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Schema de cofres/contenedores, items guardados, capacidad de almacenamiento
  - Estimación: 8h

- [ ] **API de Housing**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Endpoints para guardar/cargar layout de casa, colocar/quitar muebles
  - Estimación: 8h

- [ ] **API de Almacenamiento**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Endpoints para guardar/retirar items de cofres, gestión de inventario de casa
  - Estimación: 8h

### Frontend
- [ ] **Sistema de Grid 2D**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Grid invisible para colocar muebles, validación de posición
  - Estimación: 8h

- [ ] **Sistema de Capas (Floor/Wall)**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Separar muebles de suelo y pared, validar tipo al colocar
  - Estimación: 6h

- [ ] **Drag & Drop de Muebles**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Arrastrar muebles desde inventario y soltarlos en grid
  - Estimación: 10h

- [ ] **Física de Muebles (Gravedad)**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Muebles de suelo caen con gravedad, animación de deploy
  - Estimación: 8h

- [ ] **Persistencia de Layout**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Guardar posición de muebles, cargar al iniciar sesión
  - Estimación: 6h

- [ ] **Sistema de Cofres y Contenedores**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Colocar cofres en casa, abrir/cerrar, visualizar contenido
  - Estimación: 8h

- [ ] **UI de Almacenamiento**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Panel para guardar/retirar items de cofres, organización de inventario
  - Estimación: 10h

---

## Sprint 10: Housing UI/UX (Fase 3 - Social)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~36 h  
**Objetivo:** Mejorar experiencia de usuario en housing

### Frontend
- [ ] **Inventario de Muebles**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Panel inferior con grid de muebles disponibles, filtros
  - Estimación: 8h

- [ ] **Modo Edición de Casa**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Botón para activar/desactivar modo edición, mostrar grid
  - Estimación: 4h

- [ ] **Feedback Visual de Selección**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Efecto "pop" al seleccionar mueble, highlight visual
  - Estimación: 6h

- [ ] **Animación de Colocación**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Animación de asentamiento al soltar mueble (rebote/polvo)
  - Estimación: 6h

- [ ] **Personalización de Texturas (Pared/Suelo)**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Items consumibles para cambiar textura de fondo y suelo
  - Estimación: 10h

- [ ] **Botón Abrir/Cerrar Inventario**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Toggle para mostrar/ocultar panel de inventario
  - Estimación: 2h

---

## Sprint 11: PvP en Tiempo Real - Matchmaking (Fase 4 - PvP)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~80 h (incl. sincronización de combate PvP)  
**Objetivo:** Sistema de búsqueda de rivales y sincronización de combate PvP en tiempo real

### Backend
- [ ] **Sistema de Matchmaking PvP**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Algoritmo de matchmaking por nivel/stats, cola de búsqueda, emparejamiento
  - Estimación: 12h

- [ ] **API de Matchmaking**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Endpoints para buscar partida, cancelar búsqueda, refresh pagando Coins
  - Estimación: 6h

- [ ] **Sistema de Arenas de Combate**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Diferentes mapas de PvP, selección de arena, spawn points
  - Estimación: 6h

- [ ] **Sistema de Ranking Base**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Rating inicial, cálculo de puntos al ganar/perder, guardar historial
  - Estimación: 8h

- [ ] **WebSocket para PvP en Tiempo Real**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Conexión WebSocket para sincronización de combate PvP, mensajes en tiempo real
  - Estimación: 10h

- [ ] **Sincronización de Combate PvP**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Sincronizar acciones entre jugadores en tiempo real, lag compensation (tras Sprint 3 combate PvE)
  - Estimación: 12h

### Frontend
- [ ] **Pantalla de Búsqueda de Partida**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: UI para buscar partida PvP, mostrar estado de búsqueda, cancelar
  - Estimación: 8h

- [ ] **Conexión WebSocket Cliente PvP**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Cliente WebSocket en Godot para PvP, sincronización de acciones
  - Estimación: 10h

- [ ] **Arenas de Combate PvP**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Cargar mapas de PvP, spawn de jugadores, límites de arena
  - Estimación: 8h

---

## Sprint 12: PvP en Tiempo Real - Combate y Recompensas (Fase 4 - PvP)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~40 h  
**Objetivo:** Completar flujo de PvP en tiempo real

### Backend
- [ ] **Sistema de Recompensas de Combate PvP**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Generar recompensas (Coins, items) según resultado y ranking del oponente
  - Estimación: 8h

- [ ] **Actualización de Ranking Post-Combate**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Calcular nuevo rating según resultado, guardar historial de combates
  - Estimación: 6h

- [ ] **Sistema de Detección de Desconexión**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Manejar desconexiones durante PvP, penalizaciones, reconexión
  - Estimación: 8h

### Frontend
- [ ] **Combate PvP en Tiempo Real**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Sincronizar acciones con oponente, mostrar resultado, recompensas
  - Estimación: 12h

- [ ] **Pantalla de Resultado de Combate PvP**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: UI que muestra resultado, ranking actualizado, recompensas
  - Estimación: 6h

---

## Sprint 13: Tienda y Economía (Fase 3 - Social)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~56 h  
**Objetivo:** Sistema de compras y monedas

### Backend
- [ ] **Sistema de Monedas (Coins/Gems)**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Modelo de wallet, transacciones, validación de balance
  - Estimación: 6h

- [ ] **API de Tienda**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Endpoints para listar items, comprar con Coins/Gems
  - Estimación: 8h

- [ ] **Sistema de Compras In-App (Gems)**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Integración con store (Google Play/App Store), validación de recibos
  - Estimación: 12h

- [ ] **Catálogo de Muebles**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Items de tienda con precios, rarezas, disponibilidad
  - Estimación: 6h

### Frontend
- [ ] **Pantalla de Tienda**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: UI de tienda con categorías, filtros, preview de items
  - Estimación: 10h

- [ ] **Sistema de Wallet UI**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Mostrar balance de Coins/Gems en header, animaciones al ganar/gastar
  - Estimación: 6h

- [ ] **Flujo de Compra**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Confirmación de compra, validación de balance, feedback visual
  - Estimación: 8h

---

## Sprint 14: Cofres y Loot Boxes (Fase 2 - Progresión)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~48 h  
**Objetivo:** Sistema de recompensas time-gated

### Backend
- [ ] **Modelo de Cofres**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Schema de cofres con tiempo de apertura, contenido, rareza
  - Estimación: 6h

- [ ] **Sistema de Slots de Cofres**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Máximo 5 cofres por personaje, validación de slots disponibles
  - Estimación: 4h

- [ ] **Sistema de Apertura de Cofres**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Timer countdown, apertura automática, generar contenido aleatorio
  - Estimación: 8h

- [ ] **Sistema Pity**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Garantizar rareza alta después de X aperturas sin suerte
  - Estimación: 6h

- [ ] **API de Cofres**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Endpoints para obtener cofres, abrir instantáneamente con Gems
  - Estimación: 6h

### Frontend
- [ ] **UI de Cofres**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Panel que muestra cofres activos, timer, rareza visual
  - Estimación: 10h

- [ ] **Animación de Apertura de Cofre**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Efecto visual al abrir cofre, revelar contenido con animación
  - Estimación: 8h

---

## Sprint 15: Torneos en Vivo (Fase posterior - después del MVP)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~78 h  
**Objetivo:** Sistema de torneos con WebSockets

### Backend
- [ ] **Setup WebSockets Server**
  - Prioridad: Alta
  - Tipo: Task
  - Descripción: Configurar servidor WebSocket con FastAPI, manejo de conexiones
  - Estimación: 8h

- [ ] **Sistema de Brackets**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Generar brackets de 32/64 jugadores, emparejamientos, eliminación directa
  - Estimación: 12h

- [ ] **Matchmaking Estricto para Torneos**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Solo jugadores de nivel/liga similar, sin bots
  - Estimación: 6h

- [ ] **Sistema de Rating Competitivo**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Ganar/pierde rating en torneos, cálculo ELO-like
  - Estimación: 8h

- [ ] **Gestión de Estado de Torneo**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Estados (inscripción, en curso, finalizado), sincronización en tiempo real
  - Estimación: 10h

### Frontend
- [ ] **UI de Torneos**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Pantalla de torneos activos, inscripción, visualización de brackets
  - Estimación: 12h

- [ ] **Conexión WebSocket Cliente**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Cliente WebSocket en Godot, manejo de mensajes, reconexión
  - Estimación: 10h

- [ ] **Visualización de Brackets en Tiempo Real**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Actualizar brackets según avanza el torneo, destacar jugador actual
  - Estimación: 12h

---

## Sprint 16: Ranking y Ligas (Fase 4 - PvP)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~46 h  
**Objetivo:** Sistema competitivo completo

### Backend
- [ ] **Sistema de Ligas**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Bronce, Plata, Oro, Platino, Diamante, Master con thresholds
  - Estimación: 8h

- [ ] **API de Ranking**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Endpoints para obtener top players, ranking por liga, historial personal
  - Estimación: 8h

- [ ] **Recompensas de Temporada**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Recompensas al final de temporada según liga alcanzada
  - Estimación: 6h

### Frontend
- [ ] **Pantalla de Ranking**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Leaderboard global, filtros por liga, búsqueda de jugadores
  - Estimación: 10h

- [ ] **UI de Liga Actual**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Mostrar liga del jugador, progreso hacia siguiente liga, iconos
  - Estimación: 6h

- [ ] **Historial de Combates**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Lista de combates recientes, resultados, ver replay
  - Estimación: 8h

---

## Sprint 17: Expansión de Mapas y Farmeo (Fase 3 - Contenido)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~48 h  
**Objetivo:** Más contenido de mapas, quests y mejoras en farmeo

### Backend
- [ ] **Sistema de Múltiples Mapas**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: Diferentes zonas con diferentes niveles, tipos de enemigos, tablas de loot
  - Estimación: 8h

- [ ] **Sistema de Bosses**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Bosses en mapas, stats mejorados, mejores drops, mecánicas especiales
  - Estimación: 10h

- [ ] **Sistema de Objetivos en Mapas**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Misiones/objetivos en mapas, recompensas por completar
  - Estimación: 6h

### Frontend
- [ ] **Selección de Mapas**
  - Prioridad: Alta
  - Tipo: Feature
  - Descripción: UI para seleccionar mapa, mostrar información, requisitos de nivel
  - Estimación: 8h

- [ ] **Sistema de Bosses Visual**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Sprites y animaciones de bosses, barras de vida especiales, efectos
  - Estimación: 10h

- [ ] **Sistema de Objetivos UI**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Panel de objetivos en UI, progreso, recompensas
  - Estimación: 6h

---

## Sprint 18: Social - Amigos y Visitar Casas (Fase 3 - Social)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~28 h  
**Objetivo:** Funcionalidad social básica (amigos, visitar casas)

### Backend
- [ ] **API de Visitas**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Endpoints para obtener casas de amigos, casas aleatorias, validación de permisos
  - Estimación: 6h

- [ ] **Sistema de Amigos**
  - Prioridad: Baja
  - Tipo: Feature
  - Descripción: Agregar/eliminar amigos, lista de amigos, notificaciones
  - Estimación: 8h

### Frontend
- [ ] **Pantalla de Visitar Casa**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Cargar layout de casa ajena, modo solo lectura, botón volver
  - Estimación: 8h

- [ ] **Lista de Casas Disponibles**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: UI para buscar/explorar casas de otros jugadores
  - Estimación: 6h

---

## Sprint 19: Pasivas de Arma y Habilidades (Fase 2 - Progresión)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~26 h  
**Objetivo:** Efectos especiales de gear

### Backend
- [ ] **Sistema de Pasivas**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Modelo de pasivas (Stun, Doble ataque), activación por RNG
  - Estimación: 10h

- [ ] **Aplicación de Pasivas en Combate**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Check de activación, aplicar efecto, incluir en replay
  - Estimación: 8h

### Frontend
- [ ] **Visualización de Pasivas**
  - Prioridad: Media
  - Tipo: Feature
  - Descripción: Mostrar pasivas en tooltip de gear, efectos visuales en combate
  - Estimación: 8h

---

## Sprint 20: Polish y Optimización (Fase 4 - Live)
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~54 h  
**Objetivo:** Mejoras de UX y rendimiento

### Backend
- [ ] **Optimización de Queries**
  - Prioridad: Media
  - Tipo: Technical Debt
  - Descripción: Revisar queries lentas, agregar índices, optimizar joins
  - Estimación: 8h

- [ ] **Caché con Redis**
  - Prioridad: Media
  - Tipo: Task
  - Descripción: Cachear datos frecuentes (rankings, snapshots), invalidación
  - Estimación: 6h

- [ ] **Rate Limiting**
  - Prioridad: Media
  - Tipo: Task
  - Descripción: Limitar requests por usuario, prevenir abuse
  - Estimación: 4h

### Frontend
- [ ] **Optimización de Rendimiento**
  - Prioridad: Media
  - Tipo: Technical Debt
  - Descripción: Optimizar sprites, reducir draw calls, pooling de objetos
  - Estimación: 10h

- [ ] **Mejoras de UI/UX**
  - Prioridad: Media
  - Tipo: Task
  - Descripción: Ajustar tamaños, espaciados, feedback visual, tooltips
  - Estimación: 12h

- [ ] **Sistema de Sonidos**
  - Prioridad: Baja
  - Tipo: Feature
  - Descripción: SFX de combate, UI, música de fondo, ajustes de volumen
  - Estimación: 8h

- [ ] **Animaciones de Transición**
  - Prioridad: Baja
  - Tipo: Feature
  - Descripción: Fade in/out entre escenas, transiciones suaves
  - Estimación: 6h

---

## Sprint 21: Testing y Bug Fixes
**Duración aproximada:** 2 semanas · **Horas estimadas:** ~34 h (+ tiempo variable para bugs)  
**Objetivo:** Estabilidad y calidad

### General
- [ ] **Testing de Combate**
  - Prioridad: Alta
  - Tipo: Task
  - Descripción: Validar cálculos de daño, críticos, dodge, block en todos los casos
  - Estimación: 12h

- [ ] **Testing de Integración**
  - Prioridad: Alta
  - Tipo: Task
  - Descripción: Probar flujos completos: login → combate → recompensas → housing
  - Estimación: 10h

- [ ] **Testing Multiplataforma**
  - Prioridad: Alta
  - Tipo: Task
  - Descripción: Probar en Android, iOS, PC, validar controles y UI
  - Estimación: 12h

- [ ] **Fix de Bugs Críticos**
  - Prioridad: Alta
  - Tipo: Bug
  - Descripción: Resolver bugs encontrados durante testing
  - Estimación: Variable

---

## Notas para HacknPlan

### Prioridades Sugeridas:
- **Alta**: Core gameplay, sistemas críticos
- **Media**: Features importantes pero no bloqueantes
- **Baja**: Nice-to-have, polish

### Tipos de Tarea:
- **Feature**: Nueva funcionalidad
- **Bug**: Corrección de errores
- **Task**: Trabajo técnico/infraestructura
- **Technical Debt**: Mejoras de código existente

### Estimaciones:
- Todas las estimaciones están en horas
- Ajustar según velocidad del equipo
- Sprint sugerido: 2 semanas (80 horas por desarrollador)

### Dependencias:
- Sprint 1 debe completarse antes de cualquier otro
- Sprint 2-3 deben completarse antes de Sprint 4 (mapas necesitan movimiento y combate)
- Sprint 4 debe completarse antes de Sprint 5 (personajes en mapas)
- Sprint 5-6 deben completarse antes de Sprint 7 (progresión necesita personajes y gear)
- Sprint 9 debe completarse antes de Sprint 10 (housing core antes de UI)
- Sprint 11-12 deben completarse antes de Sprint 13 (PvP antes de tienda)
- Sprint 15 debe completarse antes de Sprint 16 (torneos antes de ranking)
