CREATE DATABASE Chefgo;

use Chefgo;

create table Recetario(
ID int not null unique auto_increment primary key,
nombre_de_usuario varchar(50) not null,
recetas varchar(200),
ingredientes varchar(200),
paso_a_paso varchar(200),
duracion int
);
