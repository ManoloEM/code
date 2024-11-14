/*
CREATE TABLE directores (
  id INTEGER,
  dni    VARCHAR(512),
  nombre   VARCHAR(512) NOT NULL,
  apellido   VARCHAR(512),
  nacimiento   DATE,
  nacionalidad VARCHAR(512),
  photo  BYTEA,
  PRIMARY KEY(dni)
);

CREATE TABLE peliculas (
  id INTEGER,
  idpelicula   BIGSERIAL,
  titulo     VARCHAR(512) NOT NULL,
  duracionminutos  INTEGER NOT NULL,
  fechalanzamiento DATE,
  trailer    BYTEA,
  sinopsis   TEXT NOT NULL,
  PRIMARY KEY(idpelicula)
);

CREATE TABLE actores (
  id INTEGER,
  dni    VARCHAR(512),
  nombre   VARCHAR(512) NOT NULL,
  apellido   VARCHAR(512),
  nacimiento   DATE,
  nacionalidad VARCHAR(512),
  photo  BYTEA,
  PRIMARY KEY(dni)
);

CREATE TABLE categoria (
  id INTEGER,
  nombre VARCHAR(512),
  PRIMARY KEY(nombre)
);

CREATE TABLE papel (
  id INTEGER,
  personaje    TEXT,
  actores_dni    VARCHAR(512),
  peliculas_idpelicula BIGINT,
  PRIMARY KEY(actores_dni,peliculas_idpelicula)
);

CREATE TABLE usuario (
  id INTEGER,
  username VARCHAR(512),
  password VARCHAR(512) NOT NULL,
  PRIMARY KEY(username)
);

CREATE TABLE resenas (
  id INTEGER,
  comentario     TEXT,
  fecha    DATE,
  nresena    BIGSERIAL,
  nota     INTEGER NOT NULL,
  usuario_username   VARCHAR(512),
  peliculas_idpelicula BIGINT,
  PRIMARY KEY(nresena,usuario_username,peliculas_idpelicula)
);

CREATE TABLE peliculas_categoria (
  id INTEGER,
  peliculas_idpelicula BIGINT,
  categoria_nombre   VARCHAR(512),
  PRIMARY KEY(peliculas_idpelicula,categoria_nombre)
);

CREATE TABLE directores_peliculas (
  id INTEGER,
  directores_dni   VARCHAR(512),
  peliculas_idpelicula BIGINT,
  PRIMARY KEY(directores_dni,peliculas_idpelicula)
);

ALTER TABLE papel ADD CONSTRAINT papel_fk1 FOREIGN KEY (actores_dni) REFERENCES actores(dni);
ALTER TABLE papel ADD CONSTRAINT papel_fk2 FOREIGN KEY (peliculas_idpelicula) REFERENCES peliculas(idpelicula);
ALTER TABLE resenas ADD CONSTRAINT resenas_fk1 FOREIGN KEY (usuario_username) REFERENCES usuario(username);
ALTER TABLE resenas ADD CONSTRAINT resenas_fk2 FOREIGN KEY (peliculas_idpelicula) REFERENCES peliculas(idpelicula);
ALTER TABLE peliculas_categoria ADD CONSTRAINT peliculas_categoria_fk1 FOREIGN KEY (peliculas_idpelicula) REFERENCES peliculas(idpelicula);
ALTER TABLE peliculas_categoria ADD CONSTRAINT peliculas_categoria_fk2 FOREIGN KEY (categoria_nombre) REFERENCES categoria(nombre);
ALTER TABLE directores_peliculas ADD CONSTRAINT directores_peliculas_fk1 FOREIGN KEY (directores_dni) REFERENCES directores(dni);
ALTER TABLE directores_peliculas ADD CONSTRAINT directores_peliculas_fk2 FOREIGN KEY (peliculas_idpelicula) REFERENCES peliculas(idpelicula);
Alter Table resenas add constraint nota check (nota>=0 and nota<=10);
ALTER TABLE peliculas DROP COLUMN foto;

*/


--Añadir datos CATEGORIA
INSERT INTO categoria VALUES ('Action&Adventure');
INSERT INTO categoria VALUES ('Animation');
INSERT INTO categoria VALUES ('ArtHouseAndInternational');
INSERT INTO categoria VALUES ('Classics');
INSERT INTO categoria VALUES ('Comedy');

--Añadir datos PELICULAS
INSERT INTO peliculas (titulo, duracionminutos, fechalanzamiento, trailer, sinopsis)
VALUES 
  (1,'El Despertar de la Sombra', 120, '2010-05-20', 'https://youtu.be/Z8pcmKXXLaw?si=_T78oelFzXFPAuNR', 'Un oscuro poder amenaza con sumir al mundo en la oscuridad. Un héroe se levanta para enfrentar la sombra y salvar a la humanidad.'),--ABAJO
  (2,'Amanecer Rojo', 110, '2011-09-15', 'https://www.youtube.com/embed/_R7MnPE78w8', 'En un mundo distópico, un grupo de rebeldes lucha por la libertad contra una ocupación militar implacable.'),
  (3,'Mundos Paralelos', 150, '2012-11-10', 'https://www.youtube.com/embed/JQio2EiG8tg', 'Una aventura épica que sigue a un grupo de exploradores a través de portales dimensionales hacia realidades desconocidas.'),
  (4,'El Último Guerrero', 130, '2013-08-20', 'https://www.youtube.com/embed/D9nYphBKgiE', 'Un guerrero solitario emprende un viaje peligroso para enfrentarse al mal y restaurar el equilibrio en el reino.'),
  (5,'Límites Inquebrantables', 145, '2014-06-18', 'https://www.youtube.com/embed/0M1DpuU7QPo', 'Enfrentados a desafíos imposibles, un grupo de amigos descubre la fuerza de la amistad y la determinación.'),
  (6,'Sombras del Pasado', 125, '2015-03-12', 'https://www.youtube.com/embed/euWryM36TFE', 'Un misterioso visitante del pasado trae consigo secretos oscuros que amenazan con cambiar el curso de la historia.'),
  (7,'El Último Aliento', 140, '2016-09-28', 'https://www.youtube.com/embed/sISAfE0VANo', 'En un futuro apocalíptico, un grupo de sobrevivientes lucha contra criaturas mutantes mientras buscan un lugar seguro.'),
  (8,'Código de Honor', 115, '2017-11-05', 'https://www.youtube.com/embed/JtpdJXK5Bnk', 'Un agente secreto deshonrado busca redención al desentrañar una conspiración mortal dentro de su propia agencia.'),
  (9,'El Misterio del Tiempo Perdido', 155, '2018-07-10', 'https://www.youtube.com/embed/JO_hkTozuMw', 'Un reloj misterioso tiene el poder de manipular el tiempo. Un científico y un aventurero deben detener su uso malévolo.'),
  (10,'Aventura en el Horizonte', 135, '2019-04-22', 'https://www.youtube.com/embed/YZY8f5S-0XA', 'Exploradores intrépidos se embarcan en una misión para descubrir tierras inexploradas y enfrentar desafíos desconocidos.'),
  (11,'El Último Susurro', 120, '2020-02-14', 'https://www.youtube.com/embed/Xw5GxqHV-6Q', 'Un romance apasionado entre dos almas destinadas a estar juntas, a pesar de las adversidades que amenazan con separarlas.'),
  (12,'El Misterio del Océano', 170, '2021-10-30', 'https://www.youtube.com/embed/EBSZu-GnPxQ', 'Un equipo de científicos marinos descubre criaturas desconocidas y antiguos secretos mientras exploran las profundidades del océano.'),
  (13,'Cazadores de Sueños', 125, '2022-05-07', 'https://www.youtube.com/embed/TSneA_1c-Hk', 'En un mundo de fantasía, un grupo de héroes se embarca en una misión para encontrar los artefactos mágicos que salvarán su reino.'),
  (14,'Almas Perdidas', 140, '2023-03-18', 'https://www.youtube.com/embed/v1ewFsu5e18', 'En un pueblo misterioso, los habitantes guardan oscuros secretos. Un forastero llega para descubrir la verdad y liberar almas atrapadas.'),
  (15,'La Última Frontera', 150, '2014-08-25', 'https://www.youtube.com/embed/jvV911DdmBI', 'En una colonia espacial, los colonos deben enfrentarse a peligros alienígenas mientras luchan por establecer una nueva vida en un planeta lejano.'),
  (16,'El Poder del Tiempo', 130, '2015-12-12', 'https://www.youtube.com/embed/MMVc80XH7xk', 'Un reloj antiguo concede a su poseedor el poder de viajar en el tiempo. Pero con el poder viene la responsabilidad y las consecuencias.'),
  (17,'Sombra en el Desierto', 160, '2016-06-08', 'https://www.youtube.com/embed/kPlOT8PzCpY', 'En medio del desierto, un arqueólogo descubre una antigua civilización perdida y desentraña un complot oscuro que amenaza con resurgir.'),
  (18,'El Último Baile', 125, '2017-03-02', 'https://www.youtube.com/embed/DjhCTEmdXB0', 'Una historia conmovedora sobre un bailarín que enfrenta desafíos personales y profesionales mientras busca la realización de su pasión.'),
  (19,'La Rebelión de las Máquinas', 135, '2018-09-20', 'https://www.youtube.com/embed/wdcG-gKsA40', 'En un futuro dominado por la inteligencia artificial, la humanidad se rebela contra las máquinas que buscan controlar sus destinos.'),
  (20,'La Ciudad de las Sombras', 145, '2019-12-05', 'https://www.youtube.com/embed/Xcqw9Mt0Wgc', 'Un detective sumergido en un mundo de crímenes oscuros y corrupción lucha por la justicia en una ciudad atrapada en la oscuridad.'),
  (21,'El Círculo de la Vida', 165, '2020-11-18', 'https://www.youtube.com/embed/V5KkgQo3Cb0', 'Un épico viaje que sigue las vidas entrelazadas de diferentes personas a lo largo de generaciones y continentes.'),
  (22,'Inframundo', 155, '2021-06-30', 'https://www.youtube.com/embed/aa0ZI_opvV8', 'Una historia de ciencia ficción que explora un mundo subterráneo habitado por criaturas misteriosas y tecnología avanzada.'),
  (23,'El Juego de los Dioses', 145, '2022-02-14', 'https://www.youtube.com/embed/ZBGpTd2FtwQ', 'En un mundo donde los dioses juegan con la realidad, un héroe se levanta para desafiarlos y cambiar el destino de la humanidad.'),
  (24,'Rebelión en el Cielo', 170, '2023-08-10', 'https://www.youtube.com/embed/POTwrIKMp6A', 'En un futuro distópico donde las ciudades flotan en el cielo, una rebelión se desata para derrocar a un régimen opresivo y restaurar la libertad.');

--Añadir datos DIRECTORES *FALTAN FOTOS
INSERT INTO directores (dni, nombre, apellido, nacimiento, nacionalidad, photo)
VALUES 
  (1,'12345678A', 'John', 'Smith', '1970-03-15', 'Estadounidense', 'https://upload.wikimedia.org/wikipedia/commons/8/84/Humphrey_Bogart_1940.jpg'),
  (2,'98765432B', 'Maria', 'Garcia', '1982-06-22', 'Española', 'https://upload.wikimedia.org/wikipedia/commons/8/84/Humphrey_Bogart_1940.jpg'),--ABAJO
  (3,'45678901C', 'Hiroshi', 'Tanaka', '1975-12-10', 'Japonesa', 'https://upload.wikimedia.org/wikipedia/commons/8/8f/MKr25425_Steven_Spielberg_%28Berlinale_2023%29.jpg'),
  (4,'23456789D', 'Sophie', 'Dubois', '1968-08-05', 'Francesa', 'https://upload.wikimedia.org/wikipedia/commons/f/fe/James_Cameron_by_Gage_Skidmore.jpg'),
  (5,'87654321E', 'Rajesh', 'Patel', '1972-05-20', 'India', 'https://upload.wikimedia.org/wikipedia/commons/f/f1/Joe_Russo_%26_Anthony_Russo_by_Gage_Skidmore.jpg'),
  (6,'34567890F', 'Elena', 'Popescu', '1978-04-03', 'Rumana', 'https://upload.wikimedia.org/wikipedia/commons/4/4a/Peter_Jackson_SDCC_2014.jpg'),
  (7,'56789012G', 'Luca', 'Rossi', '1966-11-18', 'Italiana', 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Michael.bay.png'),
  (8,'78901234H', 'Katja', 'Schmidt', '1976-09-25', 'Alemana', 'https://upload.wikimedia.org/wikipedia/commons/5/5b/David_Yates_by_Gage_Skidmore.jpg'),
  (9,'89012345I', 'Chen', 'Li', '1969-07-08', 'China', 'https://upload.wikimedia.org/wikipedia/commons/9/95/Christopher_Nolan_Cannes_2018.jpg'),
  (10,'01234567J', 'Yuki', 'Sato', '1973-02-14', 'Japonesa', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Edward_G._Robinson_1948.jpg/150px-Edward_G._Robinson_1948.jpg'),
  (11,'23456789K', 'Luis', 'Fernandez', '1970-10-30', 'Mexicana', 'https://upload.wikimedia.org/wikipedia/commons/4/4e/J._J._Abrams_by_Gage_Skidmore.jpg');

--Añadir datos ACTORES *FALTAN FOTOS
INSERT INTO actores (dni, nombre, apellido, nacimiento, nacionalidad, photo)
VALUES 
  (1,'11111111A', 'Emma', 'Johnson', '2000-08-15', 'Estadounidense', NULL),
  (2,'22222222B', 'Miguel', 'Lopez', '1995-06-22', 'Española', NULL),
  (3,'33333333C', 'Aya', 'Takahashi', '1988-12-10', 'Japonesa', NULL),
  (4,'44444444D', 'Claire', 'Dupont', '1993-04-05', 'Francesa', NULL),
  (5,'55555555E', 'Rahul', 'Kumar', '1987-05-20', 'India', NULL),
  (6,'66666666F', 'Irina', 'Popova', '1990-03-03', 'Rusa', NULL),
  (7,'77777777G', 'Giorgio', 'Marini', '1992-09-18', 'Italiana', NULL), --ABAJO
  (8,'88888888H', 'Sophie', 'Müller', '1986-07-25', 'Alemana', 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Jack_Nicholson_2001.jpg'),
  (9,'99999999I', 'Wei', 'Chen', '1991-01-08', 'China', 'https://upload.wikimedia.org/wikipedia/commons/a/a9/Tom_Hanks_TIFF_2019.jpg'),
  (10,'10101010J', 'Satoshi', 'Yamamoto', '1989-12-14', 'Japonesa', 'https://upload.wikimedia.org/wikipedia/commons/3/33/Tom_Cruise_by_Gage_Skidmore_2.jpg'),
  (11,'12121212K', 'Ana', 'Gutierrez', '1998-10-30', 'Mexicana', 'https://upload.wikimedia.org/wikipedia/commons/4/46/Leonardo_Dicaprio_Cannes_2019.jpg'),
  (12,'13131313L', 'Lucas', 'Silva', '2002-05-01', 'Brasileña', 'https://upload.wikimedia.org/wikipedia/commons/9/95/Mel_Gibson_Cannes_2016_2.jpg'),
  (13,'14141414M', 'Elena', 'Gomez', '1999-11-28', 'Española', 'https://upload.wikimedia.org/wikipedia/commons/c/c4/Bruce_Willis_by_Gage_Skidmore_3.jpg'),
  (14,'15151515N', 'Hiroshi', 'Fujita', '1994-03-17', 'Japonesa', 'https://upload.wikimedia.org/wikipedia/commons/4/4c/Brad_Pitt_2019_by_Glenn_Francis.jpg'),
  (15,'16161616O', 'Marina', 'Kovač', '1997-07-12', 'Croata', 'https://upload.wikimedia.org/wikipedia/commons/3/33/Reuni%C3%A3o_com_o_ator_norte-americano_Keanu_Reeves_%2846806576944%29_%28cropped%29.jpg'),
  (16,'17171717P', 'Juan', 'Martinez', '1985-08-03', 'Española', 'https://upload.wikimedia.org/wikipedia/commons/a/af/Arnold_Schwarzenegger_by_Gage_Skidmore_4.jpg'),
  (17,'18181818Q', 'Yuki', 'Tanaka', '2001-02-21', 'Japonesa', 'https://upload.wikimedia.org/wikipedia/commons/0/04/Jackie_Chan_Cannes_2012_%28cropped%29.jpg'),
  (18,'19191919R', 'Olga', 'Ivanova', '1996-09-05', 'Rusa', 'https://upload.wikimedia.org/wikipedia/commons/3/34/Harrison_Ford_by_Gage_Skidmore_3.jpg'),
  (19,'20202020S', 'Raj', 'Singh', '1984-06-10', 'India', 'https://upload.wikimedia.org/wikipedia/commons/8/8b/Jim_Carrey_2008.jpg'),
  (20,'21212121T', 'Giulia', 'Moretti', '1993-04-29', 'Italiana', 'https://upload.wikimedia.org/wikipedia/commons/2/21/Johnny_Depp_2020.jpg'),
  (21,'22222222U', 'Felix', 'Schneider', '1990-10-15', 'Alemana', 'https://upload.wikimedia.org/wikipedia/commons/8/81/Cameron_Diaz_WE_2012_Shankbone_4.JPG'),
  (22,'23232323V', 'Li', 'Wei', '2000-07-08', 'China', 'https://upload.wikimedia.org/wikipedia/commons/9/94/Robert_Downey_Jr_2014_Comic_Con_%28cropped%29.jpg'),
  (23,'24242424W', 'Yui', 'Suzuki', '1995-12-14', 'Japonesa', 'https://upload.wikimedia.org/wikipedia/commons/3/33/SYDNEY%2C_AUSTRALIA_-_JANUARY_23_Margot_Robbie_arrives_at_the_Australian_Premiere_of_%27I%2C_Tonya%27_on_January_23%2C_2018_in_Sydney%2C_Australia_%2828074883999%29_%28cropped%29.jpg'),
  (24,'25252525X', 'Carlos', 'Lopez', '1987-11-30', 'Mexicana', 'https://upload.wikimedia.org/wikipedia/commons/4/40/Denzel_Washington_2018.jpg'),
  (25,'26262626Y', 'Larisa', 'Dmitrieva', '1992-05-22', 'Rusa', 'https://upload.wikimedia.org/wikipedia/commons/6/65/Aamir_Khan_at_the_success_bash_of_Secret_Superstar.jpg'),
  (26,'27272727Z', 'Fabio', 'Conti', '1998-02-18', 'Italiana', 'https://upload.wikimedia.org/wikipedia/commons/1/15/Sandra_Bullock_in_July_2013.jpg'),
  (27,'28282828AA', 'Sophia', 'Schulz', '1986-01-27', 'Alemana', 'https://upload.wikimedia.org/wikipedia/commons/a/a6/Julia_Roberts_2011_Shankbone_3.JPG'),
  (28,'29292929BB', 'Wei', 'Zhang', '1991-09-10', 'China', 'https://upload.wikimedia.org/wikipedia/commons/1/11/Dwayne_%22The_Rock%22_Johnson_Visits_the_Pentagon_%2841%29_%28cropped%29.jpg'),
  (29,'30303030CC', 'Yuki', 'Ito', '1994-04-14', 'Japonesa', 'https://upload.wikimedia.org/wikipedia/commons/8/84/Sylvester_Stallone_Cannes_2019.jpg');

--Añadir datos USUARIO 
INSERT INTO usuario (username, password)
VALUES 
  (1,'Manu', '1234'),
  (2,'Juan', '1234'),
  (3,'CineLover', '1234'),
  (4,'Hater98', '1234'),
  (5,'RottenTomatoes', '1234');

--Añadir datos PELICULAS_CATEGORIAS
ALTER TABLE peliculas_categoria ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY;
INSERT INTO peliculas_categoria (id, peliculas_idpelicula, categoria_nombre)
VALUES 
  (DEFAULT, 1, 'Action&Adventure'),
  (DEFAULT, 2, 'Animation'),
  (DEFAULT, 3, 'ArtHouseAndInternational'),
  (DEFAULT, 4, 'Classics'),
  (DEFAULT, 5, 'Comedy'),
  (DEFAULT, 6, 'Action&Adventure'),
  (DEFAULT, 7, 'Animation'),
  (DEFAULT, 8, 'ArtHouseAndInternational'),
  (DEFAULT, 9, 'Classics'),
  (DEFAULT, 10, 'Comedy'),
  (DEFAULT, 11, 'Action&Adventure'),
  (DEFAULT, 12, 'Animation'),
  (DEFAULT, 13, 'ArtHouseAndInternational'),
  (DEFAULT, 14, 'Classics'),
  (DEFAULT, 15, 'Comedy'),
  (DEFAULT, 16, 'Action&Adventure'),
  (DEFAULT, 17, 'Animation'),
  (DEFAULT, 18, 'ArtHouseAndInternational'),
  (DEFAULT, 19, 'Classics'),
  (DEFAULT, 20, 'Comedy'),
  (DEFAULT, 21, 'Action&Adventure'),
  (DEFAULT, 22, 'Animation'),
  (DEFAULT, 23, 'ArtHouseAndInternational'),
  (DEFAULT, 24, 'Classics'),
  (DEFAULT, 2, 'ArtHouseAndInternational'),
  (DEFAULT, 4, 'Comedy'),
  (DEFAULT, 7, 'Classics'),
  (DEFAULT, 9, 'Animation'),
  (DEFAULT, 11, 'Animation'),
  (DEFAULT, 13, 'Classics'),
  (DEFAULT, 15, 'Classics'),
  (DEFAULT, 17, 'Comedy'),
  (DEFAULT, 19, 'Action&Adventure'),
  (DEFAULT, 21, 'Classics');

/*
--Añadir datos RESENAS
INSERT INTO resenas (comentario, fecha, nota, usuario_username, peliculas_idpelicula)
VALUES 
  ('Una película emocionante con un giro inesperado al final. ¡Altamente recomendada!', '2023-01-15', 9, 'Manu', 1),
  ('Increíble animación y personajes entrañables. ¡Perfecta para toda la familia!', '2023-02-20', 8, 'Juan', 2),
  ('Una obra maestra del cine clásico. La cinematografía y la actuación son impresionantes.', '2023-03-10', 10, 'CineLover', 3),
  ('Drama cautivador que te mantendrá en vilo. Actuaciones excepcionales de todo el elenco.', '2023-04-05', 8, 'Hater98', 4),
  ('Acción intensa y una trama emocionante. ¡No puedes apartar la mirada!', '2023-05-12', 9, 'RottenTomatoes', 5),
  ('Una comedia ligera que te hará reír de principio a fin. Perfecta para relajarse.', '2023-06-20', 7, 'Manu', 6),
  ('Un clásico atemporal con una historia cautivadora. ¡No te la puedes perder!', '2023-07-08', 10, 'Juan', 7),
  ('Drama profundo que te hace reflexionar sobre la vida. Actuaciones conmovedoras.', '2023-08-15', 8, 'CineLover', 8),
  ('Emocionante aventura llena de acción. Los efectos visuales son impresionantes.', '2023-09-22', 9, 'Hater98', 9),
  ('Una comedia ingeniosa con un guion brillante. Risas garantizadas.', '2023-10-18', 7, 'RottenTomatoes', 10),
  ('Una historia épica que te sumergirá en un mundo fantástico. Visualmente deslumbrante.', '2023-11-25', 9, 'Manu', 11),
  ('Animación espectacular con una trama conmovedora. Perfecta para todas las edades.', '2023-12-10', 8, 'Juan', 12),
  ('Una obra de arte cinematográfica. La dirección y la música son excepcionales.', '2023-01-05', 10, 'CineLover', 13),
  ('Drama intrigante con giros inesperados. Actuaciones sorprendentes.', '2023-02-12', 8, 'Hater98', 14),
  ('Acción trepidante y efectos visuales asombrosos. Una experiencia cinematográfica única.', '2023-03-20', 9, 'RottenTomatoes', 15),
  ('Comedia encantadora que te sacará más de una carcajada. ¡Altamente entretenida!', '2023-04-08', 7, 'Manu', 16),
  ('Un clásico que sigue siendo relevante hoy. Una joya del cine.', '2023-05-15', 10, 'Juan', 17),
  ('Drama conmovedor que te tocará el corazón. Una historia poderosa.', '2023-06-22', 8, 'CineLover', 18),
  ('Aventura emocionante con efectos visuales impresionantes. ¡Te mantendrá al borde del asiento!', '2023-07-10', 9, 'Hater98', 19),
  ('Comedia inteligente con diálogos ingeniosos. Una delicia para los amantes del humor.', '2023-08-18', 7, 'RottenTomatoes', 20),
  ('Una historia conmovedora que te hará reflexionar. Altamente recomendada.', '2023-09-25', 8, 'Manu', 21),
  ('Animación espectacular y personajes entrañables. Perfecta para toda la familia.', '2023-10-10', 9, 'Juan', 22),
  ('Un drama intenso con actuaciones excepcionales. Te dejará sin aliento.', '2023-11-05', 7, 'CineLover', 23),
  ('Comedia hilarante con giros inesperados. Risas garantizadas.', '2023-12-02', 8, 'Hater98', 24),
  ('Una película decepcionante, la trama no tiene sentido y las actuaciones son malas.', '2023-12-20', 2, 'Hater98', 21),
  ('No entiendo por qué a la gente le gusta esto. Aburrida y sin sentido.', '2024-01-08', 1, 'Hater98', 22),
  ('Un intento fallido de drama. No vale la pena verla.', '2024-02-15', 3, 'Hater98', 23),
  ('Comedia sin gracia y personajes insoportables. Totalmente olvidable.', '2024-03-02', 4, 'Hater98', 24);
*/
--Añadir datos PAPEL
ALTER TABLE papel ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY;
INSERT INTO papel (id, personaje, actores_dni, peliculas_idpelicula)
VALUES
  (DEFAULT, 'Protagonista', '11111111A', 1),
  (DEFAULT, 'Antagonista', '22222222B', 1),
  (DEFAULT, 'Secundario', '33333333C', 1),
  (DEFAULT, 'Amigo del protagonista', '44444444D', 1),
  (DEFAULT, 'Familia del protagonista', '55555555E', 1),

  (DEFAULT, 'Personaje principal', '66666666F', 2),
  (DEFAULT, 'Personaje secundario', '77777777G', 2),
  (DEFAULT, 'Villano', '88888888H', 2),
  (DEFAULT, 'Amigo del héroe', '99999999I', 2),
  (DEFAULT, 'Familia del personaje principal', '10101010J', 2),

  (DEFAULT, 'Detective', '11111111A', 3),
  (DEFAULT, 'Sospechoso', '22222222B', 3),
  (DEFAULT, 'Testigo', '33333333C', 3),
  (DEFAULT, 'Compañero del detective', '44444444D', 3),
  (DEFAULT, 'Víctima', '55555555E', 3),

  (DEFAULT, 'Humorista', '66666666F', 4),
  (DEFAULT, 'Romántico principal', '77777777G', 4),
  (DEFAULT, 'Compañero cómico', '88888888H', 4),
  (DEFAULT, 'Familiar gracioso', '99999999I', 4),
  (DEFAULT, 'Víctima de bromas', '10101010J', 4),

  (DEFAULT, 'Rey/Reina', '11111111A', 5),
  (DEFAULT, 'Príncipe/Princesa', '22222222B', 5),
  (DEFAULT, 'Villano real', '33333333C', 5),
  (DEFAULT, 'Consejero', '44444444D', 5),
  (DEFAULT, 'Sirviente', '55555555E', 5),

  (DEFAULT, 'Aventurero', '66666666F', 6),
  (DEFAULT, 'Explorador', '77777777G', 6),
  (DEFAULT, 'Villano de la jungla', '88888888H', 6),
  (DEFAULT, 'Guía local', '99999999I', 6),
  (DEFAULT, 'Amigo del aventurero', '10101010J', 6),

  (DEFAULT, 'Estudiante destacado', '11111111A', 7),
  (DEFAULT, 'Profesor', '22222222B', 7),
  (DEFAULT, 'Villano académico', '33333333C', 7),
  (DEFAULT, 'Amigo del estudiante', '44444444D', 7),
  (DEFAULT, 'Familiar del estudiante', '55555555E', 7),

  (DEFAULT, 'Médico principal', '66666666F', 8),
  (DEFAULT, 'Paciente', '77777777G', 8),
  (DEFAULT, 'Enfermera', '88888888H', 8),
  (DEFAULT, 'Villano médico', '99999999I', 8),
  (DEFAULT, 'Familiar del paciente', '10101010J', 8),

  (DEFAULT, 'Héroe', '66666666F', 9),
  (DEFAULT, 'Villano principal', '77777777G', 9),
  (DEFAULT, 'Compañero de aventuras', '88888888H', 9),
  (DEFAULT, 'Familiar del héroe', '99999999I', 9),
  (DEFAULT, 'Mentor', '10101010J', 9),

  (DEFAULT, 'Ingeniero espacial', '11111111A', 10),
  (DEFAULT, 'Astronauta', '22222222B', 10),
  (DEFAULT, 'Extraterrestre', '33333333C', 10),
  (DEFAULT, 'Villano intergaláctico', '44444444D', 10),
  (DEFAULT, 'Científico loco', '55555555E', 10),

  (DEFAULT, 'Detective paranormal', '66666666F', 11),
  (DEFAULT, 'Fantasma', '77777777G', 11),
  (DEFAULT, 'Cazafantasmas', '88888888H', 11),
  (DEFAULT, 'Espíritu vengativo', '99999999I', 11),
  (DEFAULT, 'Medium', '10101010J', 11),

  (DEFAULT, 'Héroe de acción', '11111111A', 12),
  (DEFAULT, 'Villano criminal', '22222222B', 12),
  (DEFAULT, 'Inocente acusado', '33333333C', 12),
  (DEFAULT, 'Compañero de la ley', '44444444D', 12),
  (DEFAULT, 'Testigo clave', '55555555E', 12),

  (DEFAULT, 'Pirata', '66666666F', 13),
  (DEFAULT, 'Capitán del barco', '77777777G', 13),
  (DEFAULT, 'Misterioso forastero', '88888888H', 13),
  (DEFAULT, 'Villano de los mares', '99999999I', 13),
  (DEFAULT, 'Isleño nativo', '10101010J', 13),

  (DEFAULT, 'Genio loco', '11111111A', 14),
  (DEFAULT, 'Científico brillante', '22222222B', 14),
  (DEFAULT, 'Asistente', '33333333C', 14),
  (DEFAULT, 'Villano científico', '44444444D', 14),
  (DEFAULT, 'Creador de inventos', '55555555E', 14),

  (DEFAULT, 'Espía', '66666666F', 15),
  (DEFAULT, 'Agente secreto', '77777777G', 15),
  (DEFAULT, 'Villano internacional', '88888888H', 15),
  (DEFAULT, 'Infiltrado', '99999999I', 15),
  (DEFAULT, 'Técnico de gadgets', '10101010J', 15),

  (DEFAULT, 'Chef famoso', '11111111A', 16),
  (DEFAULT, 'Crítico gastronómico', '22222222B', 16),
  (DEFAULT, 'Villano culinario', '33333333C', 16),
  (DEFAULT, 'Camarero', '44444444D', 16),
  (DEFAULT, 'Amante de la comida', '55555555E', 16),

  (DEFAULT, 'Artista bohemio', '66666666F', 17),
  (DEFAULT, 'Crítico de arte', '77777777G', 17),
  (DEFAULT, 'Villano del mundo del arte', '88888888H', 17),
  (DEFAULT, 'Coleccionista de arte', '99999999I', 17),
  (DEFAULT, 'Asistente del artista', '10101010J', 17),

  (DEFAULT, 'Estudiante prodigio', '11111111A', 18),
  (DEFAULT, 'Profesor de música', '22222222B', 18),
  (DEFAULT, 'Villano musical', '33333333C', 18),
  (DEFAULT, 'Amante de la música', '44444444D', 18),
  (DEFAULT, 'Familiar del estudiante', '55555555E', 18),

  (DEFAULT, 'Médico residente', '66666666F', 19),
  (DEFAULT, 'Paciente difícil', '77777777G', 19),
  (DEFAULT, 'Enfermera carismática', '88888888H', 19),
  (DEFAULT, 'Villano médico', '99999999I', 19),
  (DEFAULT, 'Familiar del paciente', '10101010J', 19),

  (DEFAULT, 'Detective astuto', '11111111A', 20),
  (DEFAULT, 'Sospechoso escurridizo', '22222222B', 20),
  (DEFAULT, 'Testigo clave', '33333333C', 20),
  (DEFAULT, 'Compañero del detective', '44444444D', 20),
  (DEFAULT, 'Víctima desconcertante', '55555555E', 20),

  (DEFAULT, 'Conquistador', '66666666F', 21),
  (DEFAULT, 'Princesa cautiva', '77777777G', 21),
  (DEFAULT, 'Villano imperial', '88888888H', 21),
  (DEFAULT, 'Consejero real', '99999999I', 21),
  (DEFAULT, 'Soldado leal', '10101010J', 21),

  (DEFAULT, 'Piloto intrépido', '11111111A', 22),
  (DEFAULT, 'Astronauta valiente', '22222222B', 22),
  (DEFAULT, 'Extraterrestre amistoso', '33333333C', 22),
  (DEFAULT, 'Villano alienígena', '44444444D', 22),
  (DEFAULT, 'Científico espacial', '55555555E', 22),

  (DEFAULT, 'Detective paranormal', '66666666F', 23),
  (DEFAULT, 'Fantasma atormentado', '77777777G', 23),
  (DEFAULT, 'Cazador de fantasmas', '88888888H', 23),
  (DEFAULT, 'Espíritu vengativo', '99999999I', 23),
  (DEFAULT, 'Medium sensitivo', '10101010J', 23),

  (DEFAULT, 'Héroe de acción', '11111111A', 24),
  (DEFAULT, 'Villano maestro del disfraz', '22222222B', 24),
  (DEFAULT, 'Inocente atrapado', '33333333C', 24),
  (DEFAULT, 'Compañero de la ley', '44444444D', 24),
  (DEFAULT, 'Testigo clave', '55555555E', 24),
  
  (DEFAULT, 'Protagonista', '12121212K', 1),
  (DEFAULT, 'Antagonista', '13131313L', 2),
  (DEFAULT, 'Secundario', '14141414M', 3),
  (DEFAULT, 'Amigo del protagonista', '15151515N', 4),
  (DEFAULT, 'Familia del protagonista', '16161616O', 5),
  (DEFAULT, 'Personaje principal', '17171717P', 6),
  (DEFAULT, 'Personaje secundario', '18181818Q', 7),
  (DEFAULT, 'Villano', '19191919R', 8),
  (DEFAULT, 'Amigo del héroe', '20202020S', 9),
  (DEFAULT, 'Familia del personaje principal', '21212121T', 10),
  (DEFAULT, 'Detective', '22222222U', 11),
  (DEFAULT, 'Sospechoso', '23232323V', 12),
  (DEFAULT, 'Testigo', '24242424W', 13),
  (DEFAULT, 'Compañero del detective', '25252525X', 14),
  (DEFAULT, 'Víctima', '26262626Y', 15),
  (DEFAULT, 'Humorista', '27272727Z', 16),
  (DEFAULT, 'Romántico principal', '28282828AA', 17),
  (DEFAULT, 'Compañero cómico', '29292929BB', 18),
  (DEFAULT, 'Familiar gracioso', '30303030CC', 19),
  (DEFAULT, 'Detective paranormal', '12121212K', 20),
  (DEFAULT, 'Fantasma', '13131313L', 21),
  (DEFAULT, 'Cazafantasmas', '14141414M', 22),
  (DEFAULT, 'Espíritu vengativo', '15151515N', 23),
  (DEFAULT, 'Medium', '16161616O', 24);


  --Añadir datos DIRECTORES_PELICULAS
ALTER TABLE directores_peliculas ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY;
INSERT INTO directores_peliculas (id, directores_dni, peliculas_idpelicula)
VALUES
  (DEFAULT, '12345678A', 1),
  (DEFAULT, '12345678A', 2),
  (DEFAULT, '98765432B', 2),
  (DEFAULT, '23456789D', 3),
  (DEFAULT, '45678901C', 4),
  (DEFAULT, '23456789D', 4),
  (DEFAULT, '87654321E', 5),
  (DEFAULT, '34567890F', 6),
  (DEFAULT, '78901234H', 7),
  (DEFAULT, '89012345I', 8),
  (DEFAULT, '01234567J', 9),
  (DEFAULT, '23456789K', 10),
  (DEFAULT, '56789012G', 11),
  (DEFAULT, '01234567J', 11),
  (DEFAULT, '56789012G', 12),
  (DEFAULT, '78901234H', 13),
  (DEFAULT, '89012345I', 14),
  (DEFAULT, '01234567J', 15),
  (DEFAULT, '23456789K', 16),
  (DEFAULT, '56789012G', 17),
  (DEFAULT, '78901234H', 18),
  (DEFAULT, '89012345I', 19),
  (DEFAULT, '01234567J', 20),
  (DEFAULT, '23456789K', 21),
  (DEFAULT, '56789012G', 22),
  (DEFAULT, '78901234H', 23),
  (DEFAULT, '89012345I', 24);




