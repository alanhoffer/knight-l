# Decisiones de Esquema - IronClash

## Resumen de respuestas

1. **Characters:** Nombre elegido por jugador. Sin clases (1 tipo). Stats iniciales fijos. Guardar posición y mapa (todo online).
2. **Gear:** Cada ítem es instancia única. Nivel y rareza propios. Pasivas genéricas (JSON).
3. **Battles:** PvE contra mobs, tiempo real. Guardar mucha info: resultados, recompensas, acciones.
4. **Snapshots:** Estado del combate en puntos del tiempo para validación/replay.
5. **Alcance:** Todo lo necesario para primer mapa PvE con mobs y looting. Incluir Coins (y Gems).
6. **Inventario:** 12 slots máx. por personaje (validación en aplicación).

## Estructura elegida

### Flujo PvE tiempo real
- Jugador entra a mapa → se crea `map_instance`
- Mobs spawnean → `enemy_instances` vinculados al map_instance
- Combate en tiempo real → acciones validadas por servidor
- Al terminar mapa → `battle` con resultados y recompensas
- Drops → se crean `character_gear` y se registran en `battle_loot`

### Tablas
- **users** – ya existe
- **characters** – personajes con stats, posición, mapa actual, coins, gems
- **maps** – mapas disponibles
- **gear_templates** – catálogo de armas/armaduras base
- **character_gear** – inventario (instancias con nivel y rareza)
- **loot_tables** + **loot_table_entries** – qué dropea cada enemigo
- **enemies** – templates de enemigos por mapa
- **map_instances** – sesión activa de jugador en un mapa
- **enemy_instances** – mobs vivos en esa instancia
- **battles** – resultado del run (victoria/derrota, XP, coins, items)
- **battle_loot** – items dropados en cada batalla
- **battle_snapshots** – estado del combate por tick para validación
