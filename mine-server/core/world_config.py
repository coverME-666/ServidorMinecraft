class WorldConfig:
    def __init__(
        self,
        nombre,
        modo_juego,
        dificultad,
        tipo_mundo,
        semilla=None,
        generar_estructuras=True,
        trucos=False,
        cofre_bonificacion=False,
        mostrar_coordenadas=True,
        ciclo_dia_noche=True,
        clima=True,
        fuego_propaga=True,
        saqueo_tnt=True,
        regeneracion_salud=True,
        mobs_hostiles=True,
        mantener_inventario=False,
        dificultad_fija=False,
        limite_jugadores=20,
        distancia_renderizado=10,
        online_mode=True,
        personalizacion_avanzada=None
    ):
        self.nombre = nombre
        self.modo_juego = modo_juego
        self.dificultad = dificultad
        self.tipo_mundo = tipo_mundo
        self.semilla = semilla
        self.generar_estructuras = generar_estructuras
        self.trucos = trucos
        self.cofre_bonificacion = cofre_bonificacion
        self.mostrar_coordenadas = mostrar_coordenadas
        self.ciclo_dia_noche = ciclo_dia_noche
        self.clima = clima
        self.fuego_propaga = fuego_propaga
        self.saqueo_tnt = saqueo_tnt
        self.regeneracion_salud = regeneracion_salud
        self.mobs_hostiles = mobs_hostiles
        self.mantener_inventario = mantener_inventario
        self.dificultad_fija = dificultad_fija
        self.limite_jugadores = limite_jugadores
        self.distancia_renderizado = distancia_renderizado
        self.online_mode = online_mode
        self.personalizacion_avanzada = personalizacion_avanzada or {}

    def to_properties(self):
        props = {
            "level-name": self.nombre,
            "level-seed": self.semilla or "",
            "gamemode": self.modo_juego,
            "difficulty": self.dificultad,
            "level-type": self.tipo_mundo,
            "generate-structures": "true" if self.generar_estructuras else "false",
            "allow-cheats": "true" if self.trucos else "false",
            "bonus-chest": "true" if self.cofre_bonificacion else "false",
            "max-players": str(self.limite_jugadores),
            "view-distance": str(self.distancia_renderizado),
            "online-mode": "true" if self.online_mode else "false",
        }
        props.update(self.personalizacion_avanzada)
        return props

    def to_gamerules(self):
        return {
            "showCoordinates": "true" if self.mostrar_coordenadas else "false",
            "doDaylightCycle": "true" if self.ciclo_dia_noche else "false",
            "doWeatherCycle": "true" if self.clima else "false",
            "doFireTick": "true" if self.fuego_propaga else "false",
            "mobGriefing": "true" if self.saqueo_tnt else "false",
            "naturalRegeneration": "true" if self.regeneracion_salud else "false",
            "doMobSpawning": "true" if self.mobs_hostiles else "false",
            "keepInventory": "true" if self.mantener_inventario else "false",
            "difficultyLocked": "true" if self.dificultad_fija else "false",
        }