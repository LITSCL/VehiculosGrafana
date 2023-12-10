-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-12-2023 a las 22:48:44
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

--
-- Volcado de datos para la tabla `portacontenedor`
--

INSERT INTO `portacontenedor` (`nombre`, `rpm`, `velocidad`, `temperatura_motor`, `temperatura_ambiente`, `porcentaje_carga`, `horometro`, `latitud`, `longitud`, `fecha`) VALUES
('POR-01', 2797, 28, 73, 20, 57, 13403, -33.5920098, -71.6333286, '2023-09-09 11:37:06'),
('POR-02', 3056, 29, 80, 20, 25, 12956, -33.5920098, -71.6333286, '2023-09-09 11:37:06'),
('POR-01', 1816, 35, 105, 15, 88, 10320, -33.5920098, -71.6328286, '2023-09-09 11:37:07'),
('POR-02', 2446, 17, 63, 17, 33, 9443, -33.5920098, -71.6338286, '2023-09-09 11:37:07');

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

--
-- Volcado de datos para la tabla `tractocamion`
--

INSERT INTO `tractocamion` (`nombre`, `rpm`, `velocidad`, `temperatura_motor`, `temperatura_ambiente`, `porcentaje_carga`, `horometro`, `latitud`, `longitud`, `fecha`) VALUES
('TRA-01', 1100, 9, 70, 23, 51, 12244, -33.5920098, -71.6343286, '2023-09-09 11:37:06'),
('TRA-02', 2971, 24, 83, 18, 65, 12622, -33.5920098, -71.6328286, '2023-09-09 11:37:06'),
('TRA-01', 2793, 25, 77, 18, 70, 7316, -33.5920098, -71.6348286, '2023-09-09 11:37:07'),
('TRA-02', 947, 25, 64, 18, 87, 10815, -33.5920098, -71.6348286, '2023-09-09 11:37:07');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
