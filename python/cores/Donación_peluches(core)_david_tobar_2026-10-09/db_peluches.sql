CREATE DATABASE IF NOT EXISTS donaciones_db;
USE donaciones_db;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR() NOT NULL,
    apellido VARCHAR() NOT NULL,
    email VARCHAR() NOT NULL UNIQUE,
    password VARCHAR() NOT NULL,
);