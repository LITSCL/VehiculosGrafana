-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-12-2023 a las 22:47:20
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dbvehiculosgrafana`
--
CREATE DATABASE IF NOT EXISTS `dbvehiculosgrafana` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `dbvehiculosgrafana`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `portacontenedor`
--

CREATE TABLE `portacontenedor` (
  `nombre` varchar(45) NOT NULL,
  `rpm` int(11) NOT NULL,
  `velocidad` int(11) NOT NULL,
  `temperatura_motor` int(11) NOT NULL,
  `temperatura_ambiente` int(11) NOT NULL,
  `porcentaje_carga` int(11) NOT NULL,
  `horometro` int(11) NOT NULL,
  `latitud` double NOT NULL,
  `longitud` double NOT NULL,
  `fecha` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tractocamion`
--

CREATE TABLE `tractocamion` (
  `nombre` varchar(45) NOT NULL,
  `rpm` int(11) NOT NULL,
  `velocidad` int(11) NOT NULL,
  `temperatura_motor` int(11) NOT NULL,
  `temperatura_ambiente` int(11) NOT NULL,
  `porcentaje_carga` int(11) NOT NULL,
  `horometro` int(11) NOT NULL,
  `latitud` double NOT NULL,
  `longitud` double NOT NULL,
  `fecha` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
