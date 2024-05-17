CREATE TABLE IF NOT EXISTS `Categoria` (
	`id` integer primary key NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Proveedor` (
	`id` integer primary key NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL,
	`correo` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Producto` (
	`id` integer primary key NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL,
	`cantidad` INTEGER NOT NULL,
	`categoria_id` INTEGER NOT NULL,
	`proveedor_id` INTEGER NOT NULL,
FOREIGN KEY(`categoria_id`) REFERENCES `Categoria`(`id`),
FOREIGN KEY(`proveedor_id`) REFERENCES `Proveedor`(`id`)
);


FOREIGN KEY(`categoria_id`) REFERENCES `Categoria`(`id`)
FOREIGN KEY(`proveedor_id`) REFERENCES `Proveedor`(`id`)