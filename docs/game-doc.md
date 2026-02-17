# Game Design Document (GDD) - IronClash

## 1. Resumen General
**Título Provisional:** IronClash  
**Género:** 2D Action RPG / Hack and Slash  
**Plataformas:** PC, Android, iOS (Cross-platform). **NO Web.**  
**Modelo:** Free-to-Play con Monetización Premium (No Pay-to-Win).  
**Modo:** Single Player (PvE) y Multiplayer (PvP en Tiempo Real).  
**Cuenta:** Single Account, Multi-device.

### Concepto Principal
Un juego de acción donde el jugador controla directamente a un guerrero, explorando mapas para farmear items y enfrentándose a otros jugadores en combates PvP con controles en tiempo real. El jugador gestiona su equipamiento, mejora sus stats y personaliza su experiencia a través de un sistema de Housing donde guarda sus pertenencias y personaliza su espacio.

---

## 2. Mecánicas de Juego (Gameplay)

### 2.1 Sistema de Combate
*   **Tipo:** Acción en tiempo real con controles directos del jugador.
*   **Controles:** El jugador mueve al personaje y ejecuta ataques manualmente.
*   **Mecánicas de Combate:**
    *   **Ataque:** El jugador presiona botones/teclas para atacar. Daño basado en ATK y mitigado por DEF del enemigo.
    *   **Crítico:** Chance de daño aumentado (x1.5) basado en stat CRIT.
    *   **Dodge (Evasión):** El jugador puede esquivar manualmente o tiene chance automática de evitar el 100% del daño según stat EVA.
    *   **Block (Bloqueo):** El jugador puede bloquear manualmente o tiene chance automática de reducir el daño recibido (40-70%) según stats.
    *   **Habilidades:** Diferentes armas y equipamiento otorgan habilidades especiales activables.
    *   **Pasivas de Arma:** Efectos especiales (ej. Stun, Doble ataque) activados por RNG o condiciones.
*   **Validación Servidor:** El servidor valida las acciones del jugador para prevenir trampas, pero el combate es en tiempo real.

### 2.2 Sistema de Mapas y Exploración
*   **Mapas:** Diferentes zonas explorables donde el jugador puede moverse libremente.
*   **Farmeo de Items:**
    *   Los enemigos PvE en mapas dropean items al ser derrotados.
    *   Diferentes mapas tienen diferentes tipos de loot y niveles de dificultad.
    *   Items pueden incluir: armas, armaduras, consumibles, recursos.
*   **Navegación:**
    *   El jugador controla el movimiento del personaje en los mapas.
    *   Sistema de minimapa para orientación.
    *   Puntos de interés marcados (NPCs, tiendas, entradas a otros mapas).

### 2.3 Stats y Personajes
*   **Stats Base:**
    *   `HP`: Vida.
    *   `ATK`: Daño base.
    *   `DEF`: Reducción de daño.
    *   `SPD`: Velocidad de movimiento y ataque.
    *   `CRIT`: Probabilidad de golpe crítico.
    *   `EVA`: Probabilidad de evasión.
*   **Progresión (Level Up):**
    *   Al subir de nivel, el jugador elige **1 de 3 mejoras aleatorias** (Roguelike style).
    *   Opciones posibles: Buff de Stats, Nueva Arma, Nueva Armadura.

### 2.4 Equipamiento (Gear)
*   **Slots:** 1 Arma, 1 Armadura (Máximo).
*   **Rarezas:** Común (Gris), Poco Común (Verde), Raro (Azul), Épico (Violeta), Legendario (Dorado).
*   **Mecánica:** Las armas y armaduras otorgan stats planos y pasivas. Las armas pueden otorgar habilidades activas que el jugador puede usar en combate.
*   **Inventario:** El jugador puede llevar múltiples items en su inventario, pero solo puede equipar 1 arma y 1 armadura a la vez.

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
*   **Funcionamiento:** El jugador explora mapas, derrota enemigos controlados por IA y farmea items.
*   **Tipos de Mapas:**
    *   Mapas de nivel bajo/medio/alto con diferentes dificultades.
    *   Mapas especiales con bosses y mejores recompensas.
    *   Mapas temáticos con diferentes tipos de enemigos y loot.
*   **Sistema de Drops:**
    *   Enemigos dropean items aleatorios al ser derrotados.
    *   Diferentes enemigos tienen diferentes tablas de loot.
    *   Bosses tienen mayor probabilidad de dropear items raros.
*   **Progresión:**
    *   Los mapas se desbloquean según el nivel del jugador.
    *   Completar objetivos en mapas otorga recompensas adicionales.

### 3.3 Torneos (Opcional)
*   **Funcionamiento:** Eventos competitivos en tiempo real mediante WebSockets.
*   **Estructura:** Eliminación directa (Brackets de 32/64 jugadores).
*   **Competitivo:** Se pierde rating/puntos al perder.
*   **Requisitos:** Matchmaking estricto por nivel/liga.

---

## 4. Meta-Juego y Economía

### 4.1 Sistema de Housing (Casas & Almacenamiento)
*   **Concepto:** Espacio personal decorable en Grid 2D donde el jugador guarda sus items y personaliza su hogar.
*   **Perspectiva y Capas:** Vista lateral (Side View).
    *   **Capa Suelo (Floor):** Items con gravedad (mesas, sillas, camas, cofres). Los personajes caminan sobre esta capa.
    *   **Capa Pared (Wall):** Items colgados (cuadros, ventanas, estanterías). Fondo visual detrás de los personajes.
    *   **Personalización de Superficies:** Existen items consumibles o reutilizables (Papeles Tapiz, Cerámicas, Alfombras completas) que permiten cambiar la textura, diseño y color del fondo (pared) y del suelo base.
    *   **Restricción de Colocación:** Cada mueble tiene un tipo de anclaje definido (Suelo vs. Pared) que determina dónde se puede soltar en la grilla.
*   **Almacenamiento:**
    *   **Cofres y Contenedores:** El jugador puede colocar cofres en su casa para guardar items.
    *   **Inventario de Casa:** Sistema de almacenamiento separado del inventario del personaje.
    *   **Organización:** El jugador puede organizar sus items en diferentes contenedores según su preferencia.
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
    *   Colocar muebles y decoraciones respetando capas.
    *   Visitar casas de amigos o aleatorias.
    *   Acceso rápido al inventario y equipamiento.

### 4.2 Economía (Monetización)
**Filosofía:** Pay-to-Fast / Pay-for-Cosmetics. **NO Pay-to-Win.**

*   **Monedas:**
    *   **Coins (Soft Currency):** Se gana jugando. Para comprar muebles básicos, refrescar rivales, mejoras estándar.
    *   **Gems (Hard Currency):** **Solo con dinero real.** Para cosméticos premium, recargar vidas, abrir cofres instantáneamente.
*   **Sistema de Vidas (Energía):**
    *   Cada personaje tiene sus propias vidas (Max 5).
    *   Regeneración por tiempo (ej. 25 min/vida).
    *   Recarga completa pagando Gems.
*   **Cofres (Loot Boxes):**
    *   Ganados en PvP.
    *   Requieren tiempo para abrirse (Time-gated).
    *   Slots limitados (5 por personaje).
    *   Contienen: Gear, Coins.
    *   Sistema **Pity**: Garantiza rareza alta tras X aperturas sin suerte.

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
*   **Validación en Tiempo Real:** El servidor verifica las acciones del cliente en tiempo real durante combates PvP y PvE.
*   **Sincronización:** Sistema de sincronización para mantener consistencia entre clientes en PvP.
*   **Seguridad:** Validación de recibos de pago, prevención de manipulación de stats, anti-cheat por diseño, validación de posición y acciones.

---

## 6. Roadmap de Desarrollo (MVP)

**Fase 1: Core (MVP)**
*   Setup del proyecto (Godot + FastAPI).
*   Sistema de Login/Auth.
*   Combate básico con controles directos (movimiento, ataque, daño).
*   1 Personaje jugable con controles, equipamiento básico.
*   Sistema de mapas básico (1-2 mapas explorables).

**Fase 2: Progresión**
*   Sistema de Level Up y elección de mejoras.
*   Inventario y gestión de Gear.
*   Sistema de Vidas y regeneración.

**Fase 3: Social & PvP**
*   Implementación de Housing (Grid placement, almacenamiento).
*   Sistema de PvP en tiempo real con matchmaking.
*   Tienda básica (Coins/Gems).
*   Sistema de mapas expandido (más zonas, farmeo de items).

**Fase 4: Live & Polish**
*   Torneos via WebSockets.
*   Ranking y Ligas.
*   Ajustes de UI/UX y efectos visuales.
