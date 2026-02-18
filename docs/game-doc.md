# Game Design Document (GDD) - IronClash

## 1. Resumen General
**Título Provisional:** IronClash  
**Género:** 2D Action RPG / Hack and Slash  
**Plataformas:** PC, Android, iOS (Cross-platform). **NO Web.**  
**Modelo:** Free-to-Play con Monetización Premium (No Pay-to-Win).  
**Modo:** Single Player (PvE) y Multiplayer (PvP en Tiempo Real).  
**Cuenta:** Una cuenta por usuario, multi-device. **Varios personajes por cuenta** permitidos; cada personaje tiene **inventario, progresión y recursos separados** (no comparten Coins, Gems ni items). **Sistema de amigos** incluido.

### Concepto Principal
Un juego de acción donde el jugador controla directamente a un guerrero, explorando mapas para farmear items y enfrentándose a otros jugadores en combates PvP con controles en tiempo real. El jugador gestiona su equipamiento, mejora sus stats y personaliza su experiencia a través de un sistema de Housing donde guarda sus pertenencias y personaliza su espacio.

---

## 2. Mecánicas de Juego (Gameplay)

### 2.1 Sistema de Combate

**Tipo:** Combate en **tiempo real** (acción continua). **No es por turnos.**  
Aplica tanto a **PvP** (jugador vs jugador) como a **PvE** (jugador vs IA): ambos jugadores o el jugador y los enemigos actúan al mismo tiempo en la misma arena.

*   **Flujo de combate:**
    *   Los participantes se mueven, atacan, esquivan y usan habilidades de forma **continua y simultánea**.
    *   No hay fases de "tu turno" / "turno del rival": todo ocurre en tiempo real.
    *   El jugador controla en todo momento movimiento y acciones mediante teclas/botones (mover, atacar, esquivar, bloquear, habilidades).

*   **Mecánicas en tiempo real:**
    *   **Movimiento:** El jugador mueve al personaje en la arena en cualquier dirección (SPD afecta velocidad).
    *   **Ataque:** Botón/tecla para atacar; el daño se aplica al instante según ATK y DEF del objetivo. Sin cola de turnos.
    *   **Crítico:** Probabilidad (stat CRIT) de que un golpe cause daño aumentado (x1.5) en el momento del impacto.
    *   **Dodge (Evasión):** Acción manual (ej. botón de esquivar) y/o chance automática (stat EVA) de evitar el 100% del daño entrante en tiempo real.
    *   **Block (Bloqueo):** Acción manual (mantener bloqueo) y/o chance automática según stats de reducir el daño recibido (40–70%) cuando llega el golpe.
    *   **Habilidades activas:** Las armas/equipo otorgan habilidades que el jugador activa con un botón; se ejecutan en tiempo real (cooldowns/recursos según diseño).
    *   **Pasivas de arma:** Efectos (ej. Stun, doble golpe) que se aplican en tiempo real por RNG o condiciones durante el combate.

*   **Validación en servidor:** El servidor valida posición, ataques y daño en tiempo real para evitar trampas; el combate sigue siendo acción continua, no por turnos.

### 2.2 Sistema de Mapas y Exploración
*   **Tipo de mapas:** **Instancias en solitario.** Cada jugador entra solo a su instancia del mapa (no hay otros jugadores en la misma zona). **Todo online:** la partida y los datos se validan en servidor para evitar hacks y manipulación de datos.
*   **Perspectiva y tamaño:** Juego **2D plano**. Tamaño de mapa **mediano a grande** por zona.
*   **Farmeo de items:**
    *   Los enemigos PvE dropean items al ser derrotados.
    *   Diferentes mapas tienen diferentes tipos de loot y niveles de dificultad.
    *   Items pueden incluir: armas, armaduras, consumibles, recursos.
*   **Quests por mapa:** En cada mapa hay misiones/objetivos, por ejemplo: farmear X cantidad de enemigos o matar X boss. Completar quests otorga recompensas.
*   **Muerte en PvE:** Sí existe. La penalización por muerte (respawn, pérdida de items, etc.) está **por definir**.
*   **Navegación:**
    *   El jugador controla el movimiento del personaje en los mapas.
    *   **No hay minimapa.** Orientación por el propio diseño del mapa y puntos de interés.
    *   Puntos de interés marcados (NPCs, tiendas, entradas a otros mapas).

### 2.3 Stats y Personajes
*   **Stats base:**
    *   `HP`: Vida.
    *   `ATK`: Daño base.
    *   `DEF`: Reducción de daño.
    *   `SPD`: Velocidad de movimiento y ataque.
    *   `CRIT`: Probabilidad de golpe crítico.
    *   `EVA`: Probabilidad de evasión.
*   **Valores iniciales:** Al inicio del proyecto, **valores fijos** para reducir trabajo. A largo plazo se plantea **generación aleatoria** de stats iniciales.
*   **Progresión (Level Up):**
    *   Al subir de nivel, el jugador elige **1 de 3 mejoras aleatorias** (estilo Roguelike).
    *   Opciones posibles: Buff de stats, Nueva arma, Nueva armadura. Las opciones **pueden repetirse** (ej. dos armas y un buff), excepto que las **skills se repiten menos**.
    *   Si los stats base mejoran automáticamente al subir de nivel: **por definir** (al principio no).
*   **Nivel máximo:** Hay tope por **etapa del juego**. Se empieza con un **nivel máximo bajo** porque al principio solo habrá **1 mapa**; el nivel máximo y los mapas se irán expandiendo con el contenido.

### 2.4 Equipamiento (Gear)
*   **Slots equipados:** 1 Arma, 1 Armadura (máximo).
*   **Inventario:** **12 slots máximo** al principio. El jugador puede llevar varios items pero solo equipar 1 arma y 1 armadura a la vez.
*   **Rarezas:** Común (Gris), Poco Común (Verde), Raro (Azul), Épico (Violeta), Legendario (Dorado).
*   **Nivel de objeto:** Las armas y armaduras tienen **nivel**; a mayor nivel, **mejores stats**. Los equipos **se pueden mejorar** (subir nivel o rareza) en lugar de solo reemplazarlos.
*   **Sets:** **No hay bonus** por llevar piezas del mismo set.
*   **Mecánica de armas:** Otorgan stats, **habilidades activas** y **pasivas**. El jugador usa las activas en combate; las pasivas se aplican por RNG o condiciones.
*   **Mecánica de armaduras:** Igual que las armas: stats, **habilidades activas** y **pasivas** (activas y pasivas tanto en armas como en armaduras).

---

## 3. Modos de Juego

### 3.1 PvP en Tiempo Real (Modo Principal)
*   **Funcionamiento:** El jugador se enfrenta a otros jugadores en tiempo real con controles directos.
*   **Matchmaking:**
    *   El jugador puede buscar partidas rápidas o desafiar a jugadores específicos.
    *   Sistema de matchmaking por nivel/stats para balancear encuentros.
    *   Puede refrescar la búsqueda pagando **Coins**.
*   **Arenas de Combate:**
    *   Mapas específicos para PvP donde los jugadores se enfrentan.
    *   Diferentes arenas con diferentes layouts y mecánicas.
*   **Coste:** Sistema de Vidas (opcional).
    *   Ganar: -1 Vida.
    *   Perder: -2 Vidas.
*   **Ranking:** Sistema de Ligas (Bronce a Master).
    *   Ganar sube ranking, perder lo baja.
    *   Recompensas según liga y victorias.

### 3.2 PvE - Mapas y Farmeo
*   **Funcionamiento:** El jugador explora mapas en instancia propia, derrota enemigos controlados por IA y farmea items. **Sin límite de energía:** se puede jugar PvE de forma ilimitada.
*   **Tipos de mapas:**
    *   Mapas de nivel bajo/medio/alto. **Dificultad seleccionable** en (o por) mapa (ej. Normal / Difícil) con impacto en loot y desafío.
    *   Mapas especiales con bosses y mejores recompensas.
    *   Mapas temáticos con diferentes tipos de enemigos y loot.
*   **Sistema de drops:**
    *   **Cada enemigo tiene una tabla de loot definida** con ítems y **probabilidades** concretas.
    *   **Los bosses tienen su propia tabla de loot** (normalmente con mejor probabilidad de ítems raros).
*   **Desbloqueo de mapas:** Los mapas se desbloquean mediante **ítems** y **misiones** (no solo por nivel).
*   **Progresión:** Completar quests y objetivos en mapas otorga recompensas adicionales.

### 3.3 Torneos (Para después)
*   **Prioridad:** Quedan **para una fase posterior** al MVP y contenido base. No forman parte del alcance inicial.
*   **Funcionamiento previsto:** Eventos competitivos en tiempo real mediante WebSockets.
*   **Estructura prevista:** Eliminación directa (brackets 32/64 jugadores). Matchmaking estricto por nivel/liga. Se pierde rating al perder.

---

## 4. Meta-Juego y Economía

### 4.1 Sistema de Housing (Casas & Almacenamiento)
*   **Concepto:** Espacio personal decorable en **Grid 2D** (tamaño en celdas definido; ampliable con Coins/Gems si se desea) donde el jugador guarda sus items y personaliza su hogar.
*   **Perspectiva y capas:** Vista lateral (Side View).
    *   **Capa Suelo (Floor):** Items con gravedad (mesas, sillas, camas, cofres). Los personajes caminan sobre esta capa.
    *   **Capa Pared (Wall):** Items colgados (cuadros, ventanas, estanterías). Fondo visual detrás de los personajes.
    *   **Personalización de Superficies:** Existen items consumibles o reutilizables (Papeles Tapiz, Cerámicas, Alfombras completas) que permiten cambiar la textura, diseño y color del fondo (pared) y del suelo base.
    *   **Restricción de Colocación:** Cada mueble tiene un tipo de anclaje definido (Suelo vs. Pared) que determina dónde se puede soltar en la grilla.
*   **Almacenamiento:**
    *   **Cofres y contenedores:** El jugador coloca cofres en su casa; **cada cofre tiene un número de slots** definido. Se pueden colocar varios cofres.
    *   **Inventario de casa:** Sistema de almacenamiento separado del inventario del personaje.
    *   **Organización:** El jugador organiza sus items en diferentes contenedores según su preferencia.
*   **Personajes:** El guerrero del jugador está visible dentro de la casa (idle/walking).
*   **Interacción (UI/UX):**
    *   **Acceso a Items:** El jugador puede acceder a sus cofres y contenedores para guardar/retirar items.
    *   **Gestión de Equipamiento:** Desde la casa se puede gestionar el equipamiento del personaje.
    *   **Modo Edición:** Botón específico para reorganizar muebles (con inventario inferior drag & drop).
    *   **Feedback Visual (Animaciones):**
        *   **Selección:** Al tocar/arrastrar un mueble, este realiza un efecto de "pop" (escala o brillo) para indicar que está activo.
        *   **Colocación (Drop):** Al soltarlo, reproduce una animación de asentamiento (ej. rebote suave o polvo) para confirmar la acción.
*   **Impacto en Gameplay:** Funcional como sistema de almacenamiento y organización de items. Estético y social.
*   **Funciones:**
    *   Guardar y organizar items en cofres y contenedores.
    *   Colocar muebles y decoraciones respetando capas (catálogo de muebles; algunos por Coins, otros por Gems o eventos).
    *   **Visitar casas de amigos o casas aleatorias** (solo visual/social; sin intercambio de items en visitas si no se define lo contrario).
    *   Acceso rápido al inventario y equipamiento.
*   **Superficies (papel/alfombra):** Los papeles tapiz y alfombras son una **capa aparte** (pared/suelo); no consumen slots de la grilla de muebles.

### 4.2 Economía (Monetización)
**Filosofía:** Pay-to-Fast / Pay-for-Cosmetics. **NO Pay-to-Win.**

*   **Monedas:**
    *   **Coins (moneda blanda):** Se obtienen jugando: completar quests, vender items, recompensas de PvP, recompensa de login diario. Uso: muebles básicos, refrescar rivales en matchmaking, mejoras estándar de equipo. Sin límite diario estricto (o cap opcional para balance).
    *   **Gems (moneda premium):** Principalmente **dinero real**. Opcionalmente, cantidades muy pequeñas por logros únicos (ej. primer boss, tutorial) para que la tienda se sienta alcanzable sin pagar. Uso: cosméticos premium, recargar vidas al instante, abrir cofres al instante, expansiones de inventario/housing.
*   **Sistema de vidas (PvP / uso opcional):**
    *   Cada personaje tiene sus propias vidas (máx. 5).
    *   Regeneración: **1 vida cada 25 minutos** (timer continuo; al gastar una, la siguiente entra en cuenta atrás).
    *   Recarga completa inmediata pagando Gems.
*   **Cofres (loot boxes):**
    *   Se ganan en PvP (y opcionalmente en eventos PvE).
    *   **Time-gated:** requieren tiempo para abrir (ej. 1h común, 4h raro, 12h épico/legendario; valores a balancear).
    *   **5 slots de cofre por personaje** (si hay varios personajes, cada uno tiene sus 5).
    *   Contienen: Gear, Coins.
    *   **Pity:** Tras X aperturas sin cierta rareza, se garantiza un item de esa rareza (ej. cada 10 cofres sin épico = 1 épico garantizado; X a definir en balance).

### 4.3 Publicidad
*   **NO ADS.** Experiencia limpia y premium.

---

## 5. Arquitectura Técnica

### 5.1 Stack Tecnológico
*   **Cliente (Frontend):** Godot 4 (GDScript).
    *   Exportación: Android, iOS, PC.
*   **Backend:** Python (FastAPI).
    *   Arquitectura limpia (Domain, Services, API).
*   **Base de Datos:** PostgreSQL (Persistencia) + Redis (Caché y sesiones torneos).
*   **Comunicaciones:**
    *   REST API: Para la mayoría de acciones (Login, Setup batalla, Housing, Shop).
    *   WebSockets: Exclusivo para Torneos en Vivo.

### 5.2 Lógica de Servidor
*   **Autoritativo:** El servidor valida todas las acciones del jugador (movimiento, ataques, daño) para prevenir trampas.
*   **Validación en tiempo real:** El servidor verifica las acciones del cliente en tiempo real durante combates PvP y PvE. Tick rate y política de interpolación: **por definir** en implementación (ej. 20–30 ticks/s según plataforma).
*   **Sincronización:** Sistema de sincronización para mantener consistencia entre clientes en PvP (cuando se implemente).
*   **Reconexión:** Política por definir (ej. ventana de 30–60 s para reconectar en partida PvP antes de dar por perdida).
*   **Seguridad:** Validación de recibos de pago, prevención de manipulación de stats, anti-cheat por diseño (validación servidor); sin cliente anti-cheat adicional por ahora.
*   **Guardado:** Persistencia en servidor; no hay modo offline. Todo el progreso vive en backend para evitar hacks.

---

## 6. Roadmap de Desarrollo (MVP)

**Enfoque MVP:** **PvE con 1 mapa muy pulido.** El control del personaje, **animaciones y movimientos** deben ser de **muy buena calidad** desde el inicio. El **PvP multijugador** se aborda **después** de tener esa base sólida. Los **torneos** quedan para una fase posterior.

**Fase 1: Core (MVP PvE)**
*   Setup del proyecto (Godot + FastAPI).
*   Sistema de Login/Auth.
*   Combate en tiempo real con controles directos (movimiento, ataque, daño) y **animaciones/movimientos de alta calidad** para el personaje.
*   1 personaje jugable con controles y equipamiento básico.
*   **1 mapa** explorable, **muy pulido** (instancia en solitario, online, quests básicas).

**Fase 2: Progresión**
*   Sistema de Level Up y elección de mejoras (1 de 3 aleatorias).
*   Inventario (12 slots) y gestión de Gear (mejora de equipo, nivel de objeto).
*   Sistema de vidas y regeneración (para cuando exista PvP).

**Fase 3: Social, Housing y contenido**
*   Implementación de Housing (grid, cofres, muebles, visitas).
*   Tienda básica (Coins/Gems).
*   Más mapas, tablas de loot, dificultad seleccionable, desbloqueo por ítems y misiones.
*   Sistema de amigos.

**Fase 4: PvP y polish**
*   **PvP en tiempo real** con matchmaking (arenas, ranking, ligas).
*   Ajustes de UI/UX y efectos visuales.

**Fase posterior: Torneos**
*   Torneos vía WebSockets (brackets, eventos programados).
