class Tablas():
    def __init__(self):
        self.tablaJugadores = """
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME CHAR(80) UNIQUE,
        PASSWD CHAR(80),
        CONT INTEGER
        """
        self.tablaCategorias = """
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CATEGORIA INTEGER NOT NULL UNIQUE
        """
        self.tablaPremios = """
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PREMIO INTEGER NOT NULL UNIQUE,
        ID_CATEGORIA INTEGER NOT NULL, 
        FOREIGN KEY(ID_CATEGORIA) REFERENCES categorias(ID)
        """

        self.tablaPreguntas = """
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PREGUNTA TEXT NOT NULL UNIQUE,
        ID_CATEGORIA INTEGER NOT NULL, 
        FOREIGN KEY(ID_CATEGORIA) REFERENCES categorias(ID)
        """

        self.tablaOpciones = """
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        OPCION TEXT NOT NULL UNIQUE,
        ID_PREGUNTA INTEGER NOT NULL,
        FOREIGN KEY(ID_PREGUNTA) REFERENCES preguntas(ID)
        """

        self.tablaRespuestas = """
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        RESPUESTA TEXT NOT NULL UNIQUE, 
        ID_PREGUNTA INTEGER NOT NULL,
        FOREIGN KEY(ID_PREGUNTA) REFERENCES preguntas(ID)
        """

        self.tablaRondas = """
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_JUGADOR INTEGER NOT NULL REFERENCES jugadores(ID),
        ID_PREGUNTA INTEGER NOT NULL REFERENCES preguntas(ID),
        ID_PREMIO INTEGER NOT NULL REFERENCES premios(ID),
        CONT INTEGER NOT NULL
        """

        self.lengPlayer ="null, ?, ?, ?"
        self.playerAdmin = [('admin', 'admin', 0)]

        self.lengCategorie = "null, ?"
        self.categories =[(1,), (2,), (3,), (4,), (5,)]

        self.lengReward = "null, ?, ?"
        self.reward =[(5,1),(15,2),(30,3),(100,4),(350,5)]

        self.lengQuestion = "null, ?, ?"
        self.question = [
                        ('El sol es:', 1),
                        ('??Cu??ntos d??as tiene un a??o bisiesto?\r\n', 1),
                        ('??Cu??l es la capital de Colombia?', 1),
                        ('??Cu??l es el primer d??a de la semana ?', 1),
                        ('??Qui??n es Shakira?\r\n', 1),
                        ('Un kilometro es:\r\n', 2),
                        ('Benedicto XVI fue:\r\n', 2),
                        ('Para f(x) = 3x+5, con x = 5 \r\n', 2),
                        ('??Qu?? es NaCl?\r\n', 2),
                        ('XL es:\r\n', 2),
                        ('??Cu??l es el r??o m??s caudaloso del mundo ?\r\n', 3),
                        ('??Qu?? pa??s est?? entre Per?? y Colombia?\r\n', 3),
                        ('??Qu?? se celebra el 20 de Julio? \r\n', 3),
                        ('??C??mo se llama la l??nea vertical imaginaria que divide el mundo en dos mitades?\r\n', 3),
                        ('??Cu??ntos departamentos tiene Colombia? \r\n', 3),
                        ('??Cu??l fue el sistema operativo para desktop m??s usado en 2020?\r\n', 4),
                        ('??Qu?? fil??sofo cre?? ???El mito de la caverna????\r\n', 4),
                        ('??En qu?? mes el Sol est?? m??s cerca de la Tierra?\r\n', 4),
                        ('??En qu?? ciudad vive el mago de Oz?\r\n', 4),
                        ('??Qui??n era el emperador de Roma cuando muri?? Jes??s de Nazaret?\r\n', 4),
                        ('??C??mo se llama el caballo de Don Quijote de la Mancha?\r\n', 5),
                        ('??Qu?? poeta escribi?? el poema ???Oda a Afrodita????\r\n', 5),
                        ('??C??mo se llama la reacci??n qu??mica que ocurre en el n??cleo del sol ?\r\n', 5),
                        ('??Qu?? edad tiene la Tierra?\r\n', 5),
                        ('La constante de la gravitaci??n es:\r\n', 5)
                        ]
    
        self.lengOption = "null, ?, ?"
        self.Options = [
                        ('El dios del fuego', 1),
                        ('Un planeta', 1),
                        ('Una estrella', 1),
                        ('Un cometa', 1),
                        ('Uno m??s de lo normal', 2),
                        ('365', 2),
                        ('Uno menos de lo normal', 2),
                        ('300', 2),
                        ('Sucre', 3),
                        ('Medell??n', 3),
                        ('Cundinamarca', 3),
                        ('Bogot??', 3),
                        ('Domingo', 4),
                        ('Enero', 4),
                        ('Lunes', 4),
                        ('S??bado', 4),
                        ('La expresidente de Argentina', 5),
                        ('La reina de belleza de Cartagena', 5),
                        ('Una cantante Colombiana', 5),
                        ('La campeona de nataci??n de los juegos Ol??mpicos 2021', 5),
                        ('Una unidad de medida de longitud', 6),
                        ('Una medida de ??rea', 6),
                        ('Una medida de volumen', 6),
                        ('Una pelicula Cubana', 6),
                        ('Un rey del imperio Romano', 7),
                        ('Un papa de la iglesia cat??lica', 7),
                        ('El libertador de francia', 7),
                        ('Un matem??tico Aleman', 7),
                        ('f(x) = 13', 8),
                        ('f(x) = y', 8),
                        ('f(x) = 28', 8),
                        ('f(x) = 20', 8),
                        ('Sal de cocina', 9),
                        ('Una empresa de la NASA', 9),
                        ('Una formula de la f??sica', 9),
                        ('La formula quimica del agua', 9),
                        ('Una talla de ropa', 10),
                        ('Un n??mero romano', 10),
                        ('Todas las anteriores', 10),
                        ('Ninguna de las anteriores', 10),
                        ('El r??o Nilo', 11),
                        ('El r??o de la Plata', 11),
                        ('El r??o de los 7 colores', 11),
                        ('El r??o Amazonas', 11),
                        ('Ecuador', 12),
                        ('Panam??', 12),
                        ('Brasil', 12),
                        ('Venezuela', 12),
                        ('El grito de independencia', 13),
                        ('La independencia de Colombia', 13),
                        ('La batalla de Boyac??', 13),
                        ('La liberaci??n de los esclavos', 13),
                        ('La generariz', 14),
                        ('Linea Ecuatorial', 14),
                        ('El eje de las Ordenadas', 14),
                        ('El meridiano de Greenwich', 14),
                        ( '50', 15),
                        ('27', 15),
                        ('32', 15),
                        ('No tiene departamentos', 15),
                        ('MacOS', 16),
                        ('Windows', 16),
                        ('Android', 16),
                        ('Linux', 16),
                        ('Plat??n', 17),
                        ('Euclides', 17),
                        ('Pitagoras', 17),
                        ('Kepler', 17),
                        ('Junio', 18),
                        ('Agosto', 18),
                        ('Noviembre', 18),
                        ('Diciembre', 18),
                        ('En el pa??s de las Maravillas', 19),
                        ('Escocia', 19),
                        ('Macondo', 19),
                        ('Esmeralda', 19),
                        ('Pilatos', 20),
                        ('Tiberio', 20),
                        ('Alejandro Magno', 20),
                        ('Ner??n', 20),
                        ('Marengo', 21),
                        ('Palomo', 21),
                        ('Rocinante', 21),
                        ('Pegasus', 21),
                        ('Salvador Dal??', 22),
                        ('Omero', 22),
                        ('Socrates', 22),
                        ('Safo de Mitilene', 22),
                        ('Fusi??n nuclear', 23),
                        ('Fisi??n nuclear', 23),
                        ('Radiacci??n nuclear', 23),
                        ('Divisi??n nuclear', 23),
                        ('2022 a??os', 24),
                        ('250 millones de a??os', 24),
                        ('4.543  millones de a??os', 24),
                        ('115 a??os luz', 24),
                        ('6.667x10^-11', 25),
                        ('9.8', 25),
                        ('6.02x10^23', 25),
                        ('3.1416', 25)
                        ]

        self.lengAnswer = "null, ?, ?"
        self.answers = [
                        ('Una estrella', 1),
                        ('Uno m??s de lo normal ', 2),
                        ('Bogot??', 3),
                        ('Lunes', 4),
                        ('Una cantante Colombiana', 5),
                        ('Una unidad de medida de longitud', 6),
                        ('Un papa de la iglesia cat??lica', 7),
                        ('f(x) = 20', 8),
                        ('Sal de cocina', 9),
                        ('Todas las anteriores', 10),
                        ('El r??o Amazonas', 11),
                        ('Ecuador', 12),
                        ('El grito de independencia', 13),
                        ('El meridiano de Greenwich', 14),
                        ('32', 15),
                        ('Windows', 16),
                        ('Plat??n', 17),
                        ('Diciembre', 18),
                        ('Esmeralda', 19),
                        ('Toberio', 20),
                        ('Rocinante', 21),
                        ('Safo de Mitilene', 22),
                        ('Fusi??n nuclear', 23),
                        ('4.543  millones de a??os', 24),
                        ('6.667x10^-11', 25)
                      ]


if __name__=="__main__":
    pass