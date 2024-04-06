-- Création de la base de données
CREATE DATABASE IF NOT EXISTS ismdb;
USE ismdb;

-- Création de la table 'valises'
CREATE TABLE IF NOT EXISTS valises (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    marque VARCHAR(255) NOT NULL,
    prix VARCHAR(255) NOT NULL,
    lien VARCHAR(255) NOT NULL,
    image_url VARCHAR(255) NOT NULL
);