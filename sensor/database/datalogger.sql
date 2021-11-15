-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Nov 12, 2021 at 08:40 PM
-- Server version: 10.5.4-MariaDB
-- PHP Version: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `datalogger`
--
CREATE DATABASE IF NOT EXISTS `datalogger` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `datalogger`;

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
CREATE TABLE IF NOT EXISTS `log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_time` datetime NOT NULL,
  `sensor_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `sensor_value` float NOT NULL,
  `remark` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `log`
--

INSERT INTO `log` (`id`, `date_time`, `sensor_name`, `sensor_value`, `remark`) VALUES
(1, '2021-11-12 20:18:38', 'test', 10, 'manually added in DB'),
(2, '2021-11-12 20:31:37', 'test', 12, 'Manually added in the DB'),
(3, '2021-11-12 00:00:00', 'test', 50, 'From python'),
(4, '2021-11-12 00:00:00', 'test', 50, 'From python'),
(5, '2021-11-12 00:00:00', 'test', 50, 'From python'),
(6, '2021-11-12 00:00:00', 'test', 50, 'From python'),
(7, '2021-11-12 00:00:00', 'test', 50, 'From python'),
(8, '2021-11-12 00:00:00', 'test', 50, 'From python'),
(9, '2021-11-12 00:00:00', 'test', 50, 'From python'),
(10, '2021-11-12 00:00:00', 'test', 50, 'From python'),
(11, '2021-11-12 00:00:00', 'test', 50, 'From python');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
