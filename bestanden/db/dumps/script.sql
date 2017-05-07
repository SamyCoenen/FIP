-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Gegenereerd op: 09 feb 2017 om 17:03
-- Serverversie: 5.7.17
-- PHP-versie: 7.0.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fipdb`
--
CREATE DATABASE IF NOT EXISTS `fipdb` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `fipdb`;
-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `api_bike`
--

CREATE TABLE `api_bike` (
  `id` int(11) NOT NULL,
  `model` varchar(100) NOT NULL,
  `electric` tinyint(1) NOT NULL,
  `speed` int(11) NOT NULL,
  `brand_id` int(11) DEFAULT NULL,
  `lease_price` double NOT NULL,
  `image_location` varchar(200) NOT NULL,
  `image_url` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `api_bike`
--

INSERT INTO `api_bike` (`id`, `model`, `electric`, `speed`, `brand_id`, `lease_price`, `image_location`, `image_url`) VALUES
(1, 'Bolero Gentlemen 7V 2017', 0, 0, 1, 23.9, 'afbeeldingen/Batavus_Bolero_Gentlemen_7V_2017', '/33080_dfd0704/image/300x300'),
(2, 'Bolero Ladies 7V 2017', 0, 0, 1, 23.9, 'afbeeldingen/Batavus_Bolero_Ladies_7V_2017', '/33079_dfd0704/image/300x300'),
(3, 'Boulevard 24 Gentlemen 2017', 0, 0, 1, 21.45, 'afbeeldingen/Batavus_Boulevard_24_Gentlemen_2017', '/34446_ddb5c2e/image/300x300'),
(4, 'Boulevard 24 Ladies 2017', 0, 0, 1, 21.45, 'afbeeldingen/Batavus_Boulevard_24_Ladies_2017', '/34445_ddb5c2e/image/300x300'),
(5, 'Boulevard 8 Gentlemen 2017', 0, 0, 1, 19.91, 'afbeeldingen/Batavus_Boulevard_8_Gentlemen_2017', '/34444_ddb5c2e/image/300x300'),
(6, 'Boulevard 8 Ladies 2017', 0, 0, 1, 19.91, 'afbeeldingen/Batavus_Boulevard_8_Ladies_2017', '/34443_ddb5c2e/image/300x300'),
(7, 'Boulevard X-Light Gentlemen 2017', 0, 0, 1, 22.98, 'afbeeldingen/Batavus_Boulevard_X-Light_Gentlemen_2017', '/34448_ddb5c2e/image/300x300'),
(8, 'Boulevard X-Light Ladies 2017', 0, 0, 1, 22.98, 'afbeeldingen/Batavus_Boulevard_X-Light_Ladies_2017', '/34447_ddb5c2e/image/300x300'),
(9, 'Bryte Gentlemen 8V 2017', 0, 0, 1, 30.65, 'afbeeldingen/Batavus_Bryte_Gentlemen_8V_2017', '/33082_dfd0704/image/300x300'),
(10, 'Bryte Ladies 8V 2017', 0, 0, 1, 30.65, 'afbeeldingen/Batavus_Bryte_Ladies_8V_2017', '/33081_dfd0704/image/300x300'),
(11, 'CNCTD E-Go Gentlemen 300Wh 2017', 1, 0, 1, 52.58, 'afbeeldingen/Batavus_CNCTD_E-Go_Gentlemen_300Wh_2017', '/32963_dfd0704/image/300x300'),
(12, 'CNCTD E-Go Gentlemen 400Wh 2017', 1, 0, 1, 52.58, 'afbeeldingen/Batavus_CNCTD_E-Go_Gentlemen_400Wh_2017', '/32964_dfd0704/image/300x300'),
(13, 'CNCTD E-Go Ladies 300Wh 2017', 1, 0, 1, 47.97, 'afbeeldingen/Batavus_CNCTD_E-Go_Ladies_300Wh_2017', '/32961_dfd0704/image/300x300'),
(14, 'CNCTD E-Go Ladies 400Wh 2017', 1, 0, 1, 47.97, 'afbeeldingen/Batavus_CNCTD_E-Go_Ladies_400Wh_2017', '/32962_dfd0704/image/300x300'),
(15, 'Chicane Gentlemen 7V 2017', 0, 0, 1, 23.29, 'afbeeldingen/Batavus_Chicane_Gentlemen_7V_2017', '/33084_dfd0704/image/300x300'),
(16, 'Chicane Ladies 7V 2017', 0, 0, 1, 23.29, 'afbeeldingen/Batavus_Chicane_Ladies_7V_2017', '/33083_dfd0704/image/300x300'),
(17, 'Click Ladies N7 2017', 0, 0, 1, 18.38, 'afbeeldingen/Batavus_Click_Ladies_N7_2017', '/33085_dfd0704/image/300x300'),
(18, 'Click Ladies V7 2017', 0, 0, 1, 16.85, 'afbeeldingen/Batavus_Click_Ladies_V7_2017', '/33086_dfd0704/image/300x300'),
(19, 'Dinsdag Comfort Gentlemen V7 2017', 0, 0, 1, 26.97, 'afbeeldingen/Batavus_Dinsdag_Comfort_Gentlemen_V7_2017', '/33090_dfd0704/image/300x300'),
(20, 'Dinsdag Comfort Ladies V7 2017', 0, 0, 1, 26.97, 'afbeeldingen/Batavus_Dinsdag_Comfort_Ladies_V7_2017', '/33089_dfd0704/image/300x300'),
(21, 'Dinsdag Exclusive Gentlemen N8 2017', 0, 0, 1, 36.79, 'afbeeldingen/Batavus_Dinsdag_Exclusive_Gentlemen_N8_2017', '/33104_dfd0704/image/300x300'),
(22, 'Dinsdag Exclusive Ladies N8 2017', 0, 0, 1, 36.79, 'afbeeldingen/Batavus_Dinsdag_Exclusive_Ladies_N8_2017', '/33103_dfd0704/image/300x300'),
(23, 'Dinsdag Gentlemen V7 2017', 0, 0, 1, 23.9, 'afbeeldingen/Batavus_Dinsdag_Gentlemen_V7_2017', '/33088_dfd0704/image/300x300'),
(24, 'Dinsdag Ladies V7 2017', 0, 0, 1, 23.9, 'afbeeldingen/Batavus_Dinsdag_Ladies_V7_2017', '/33087_dfd0704/image/300x300'),
(25, 'Dinsdag X-Light Gentlemen V7 2017', 0, 0, 1, 27.58, 'afbeeldingen/Batavus_Dinsdag_X-Light_Gentlemen_V7_2017', '/33106_dfd0704/image/300x300'),
(26, 'Dinsdag X-Light Ladies V7 2017', 0, 0, 1, 27.58, 'afbeeldingen/Batavus_Dinsdag_X-Light_Ladies_V7_2017', '/33105_dfd0704/image/300x300'),
(27, 'Diva E-Go Ladies 300Wh 2017', 1, 0, 1, 52.58, 'afbeeldingen/Batavus_Diva_E-Go_Ladies_300Wh_2017', '/32965_dfd0704/image/300x300'),
(28, 'Diva E-Go Ladies 400Wh 2017', 1, 0, 1, 57.18, 'afbeeldingen/Batavus_Diva_E-Go_Ladies_400Wh_2017', '/32966_dfd0704/image/300x300'),
(29, 'Diva Plus Ladies V7 2017', 0, 0, 1, 24.52, 'afbeeldingen/Batavus_Diva_Plus_Ladies_V7_2017', '/33107_dfd0704/image/300x300'),
(30, 'Donna E-Go Ladies 300Wh 2017', 1, 0, 1, 51.04, 'afbeeldingen/Batavus_Donna_E-Go_Ladies_300Wh_2017', '/32967_dfd0704/image/300x300'),
(31, 'Donna E-Go Ladies 400Wh 2017', 1, 0, 1, 55.64, 'afbeeldingen/Batavus_Donna_E-Go_Ladies_400Wh_2017', '/32968_dfd0704/image/300x300'),
(32, 'Donna Plus Ladies 2017', 0, 0, 1, 23.9, 'afbeeldingen/Batavus_Donna_Plus_Ladies_2017', '/33108_dfd0704/image/300x300'),
(33, 'Fuze Comfort Gentlemen 2017', 0, 0, 1, 27.58, 'afbeeldingen/Batavus_Fuze_Comfort_Gentlemen_2017', '/34452_ddb5c2e/image/300x300'),
(34, 'Fuze Comfort Ladies 2017', 0, 0, 1, 27.58, 'afbeeldingen/Batavus_Fuze_Comfort_Ladies_2017', '/34451_ddb5c2e/image/300x300'),
(35, 'Fuze E-Go Active Gentlemen 10V 400Wh 2017', 1, 0, 1, 80.19, 'afbeeldingen/Batavus_Fuze_E-Go_Active_Gentlemen_10V_400Wh_2017', '/32998_dfd0704/image/300x300'),
(36, 'Fuze E-Go Active Ladies 10V 400Wh 2017', 1, 0, 1, 80.19, 'afbeeldingen/Batavus_Fuze_E-Go_Active_Ladies_10V_400Wh_2017', '/32997_dfd0704/image/300x300'),
(37, 'Fuze E-Go Exclusive Gentlemen 20V 300Wh 2017', 1, 0, 1, 78.66, 'afbeeldingen/Batavus_Fuze_E-Go_Exclusive_Gentlemen_20V_300Wh_2017', '/33003_dfd0704/image/300x300'),
(38, 'Fuze E-Go Exclusive Gentlemen 20V 400Wh 2017', 1, 0, 1, 83.26, 'afbeeldingen/Batavus_Fuze_E-Go_Exclusive_Gentlemen_20V_400Wh_2017', '/33004_dfd0704/image/300x300'),
(39, 'Fuze E-Go Exclusive Gentlemen 20V 500Wh 2017', 1, 0, 1, 86.33, 'afbeeldingen/Batavus_Fuze_E-Go_Exclusive_Gentlemen_20V_500Wh_2017', '/33005_dfd0704/image/300x300'),
(40, 'Fuze E-Go Exclusive Gentlemen 20V 600Wh 2017', 1, 0, 1, 89.4, 'afbeeldingen/Batavus_Fuze_E-Go_Exclusive_Gentlemen_20V_600Wh_2017', '/33006_dfd0704/image/300x300'),
(41, 'Fuze E-Go Exclusive Ladies 20V 300Wh 2017', 1, 0, 1, 78.66, 'afbeeldingen/Batavus_Fuze_E-Go_Exclusive_Ladies_20V_300Wh_2017', '/32999_dfd0704/image/300x300'),
(42, 'Fuze E-Go Exclusive Ladies 20V 400Wh 2017', 1, 0, 1, 83.26, 'afbeeldingen/Batavus_Fuze_E-Go_Exclusive_Ladies_20V_400Wh_2017', '/33000_dfd0704/image/300x300'),
(43, 'Fuze E-Go Exclusive Ladies 20V 500Wh 2017', 1, 0, 1, 86.33, 'afbeeldingen/Batavus_Fuze_E-Go_Exclusive_Ladies_20V_500Wh_2017', '/33001_dfd0704/image/300x300'),
(44, 'Fuze E-Go Exclusive Ladies 20V 600Wh 2017', 1, 0, 1, 89.4, 'afbeeldingen/Batavus_Fuze_E-Go_Exclusive_Ladies_20V_600Wh_2017', '/33002_dfd0704/image/300x300'),
(45, 'Fuze Gentlemen 2017', 0, 0, 1, 24.52, 'afbeeldingen/Batavus_Fuze_Gentlemen_2017', '/34450_ddb5c2e/image/300x300'),
(46, 'Fuze Ladies 2017', 0, 0, 1, 24.52, 'afbeeldingen/Batavus_Fuze_Ladies_2017', '/34449_ddb5c2e/image/300x300'),
(47, 'Fuze X-Light Gentlemen 2017', 0, 0, 1, 30.65, 'afbeeldingen/Batavus_Fuze_X-Light_Gentlemen_2017', '/34454_ddb5c2e/image/300x300'),
(48, 'Fuze X-Light Ladies 2017', 0, 0, 1, 30.65, 'afbeeldingen/Batavus_Fuze_X-Light_Ladies_2017', '/34453_ddb5c2e/image/300x300'),
(49, 'Hommage Gentlemen V3 2017', 0, 0, 1, 21.45, 'afbeeldingen/Batavus_Hommage_Gentlemen_V3_2017', '/33110_dfd0704/image/300x300'),
(50, 'Hommage Ladies V3 2017', 0, 0, 1, 21.45, 'afbeeldingen/Batavus_Hommage_Ladies_V3_2017', '/33109_dfd0704/image/300x300'),
(51, 'Mambo Gentlemen 2017', 0, 0, 1, 24.52, 'afbeeldingen/Batavus_Mambo_Gentlemen_2017', '/33112_dfd0704/image/300x300'),
(52, 'Mambo Ladies 2017', 0, 0, 1, 24.52, 'afbeeldingen/Batavus_Mambo_Ladies_2017', '/33111_dfd0704/image/300x300'),
(53, 'Old Dutch Ladies 3V 2017', 0, 0, 1, 16.85, 'afbeeldingen/Batavus_Old_Dutch_Ladies_3V_2017', '/33113_dfd0704/image/300x300'),
(54, 'Old Dutch Plus Ladies 3V 2017', 0, 0, 1, 18.38, 'afbeeldingen/Batavus_Old_Dutch_Plus_Ladies_3V_2017', '/33114_dfd0704/image/300x300'),
(55, 'Quip Gentlemen 3V 2017', 0, 0, 1, 19.91, 'afbeeldingen/Batavus_Quip_Gentlemen_3V_2017', '/33126_dfd0704/image/300x300'),
(56, 'Quip Uni 3V 2017', 0, 0, 1, 19.91, 'afbeeldingen/Batavus_Quip_Uni_3V_2017', '/33125_dfd0704/image/300x300'),
(57, 'Razer Gentlemen 8V 400Wh 2017', 0, 0, 1, 83.26, 'afbeeldingen/Batavus_Razer_Gentlemen_8V_400Wh_2017', '/33008_dfd0704/image/300x300'),
(58, 'Razer Ladies 8V 400Wh 2017', 0, 0, 1, 83.26, 'afbeeldingen/Batavus_Razer_Ladies_8V_400Wh_2017', '/33007_dfd0704/image/300x300'),
(59, 'Stream Gentlemen 7V 500Wh 2017', 0, 0, 1, 80.19, 'afbeeldingen/Batavus_Stream_Gentlemen_7V_500Wh_2017', '/33010_dfd0704/image/300x300'),
(60, 'Stream Ladies 7V 500Wh 2017', 0, 0, 1, 80.19, 'afbeeldingen/Batavus_Stream_Ladies_7V_500Wh_2017', '/33009_dfd0704/image/300x300'),
(61, 'Wayz Comfort Gentlemen 8V 2017', 0, 0, 1, 26.97, 'afbeeldingen/Batavus_Wayz_Comfort_Gentlemen_8V_2017', '/33130_dfd0704/image/300x300'),
(62, 'Wayz Comfort Ladies 8V 2017', 0, 0, 1, 26.97, 'afbeeldingen/Batavus_Wayz_Comfort_Ladies_8V_2017', '/33129_dfd0704/image/300x300'),
(63, 'Wayz E-Go Active Gentlemen 8V 400Wh 2017', 1, 0, 1, 80.19, 'afbeeldingen/Batavus_Wayz_E-Go_Active_Gentlemen_8V_400Wh_2017', '/33026_dfd0704/image/300x300'),
(64, 'Wayz E-Go Active Gentlemen NH380 400Wh 2017', 1, 0, 1, 100.14, 'afbeeldingen/Batavus_Wayz_E-Go_Active_Gentlemen_NH380_400Wh_2017', '/33028_dfd0704/image/300x300'),
(65, 'Wayz E-Go Active Gentlemen NN330 400Wh 2017', 1, 0, 1, 83.26, 'afbeeldingen/Batavus_Wayz_E-Go_Active_Gentlemen_NN330_400Wh_2017', '/33030_dfd0704/image/300x300'),
(66, 'Wayz E-Go Active Ladies 8V 400Wh 2017', 1, 0, 1, 80.19, 'afbeeldingen/Batavus_Wayz_E-Go_Active_Ladies_8V_400Wh_2017', '/33025_dfd0704/image/300x300'),
(67, 'Wayz E-Go Active Ladies NH380 400Wh 2017', 1, 0, 1, 100.14, 'afbeeldingen/Batavus_Wayz_E-Go_Active_Ladies_NH380_400Wh_2017', '/33027_dfd0704/image/300x300'),
(68, 'Wayz E-Go Active Ladies NN330 400Wh 2017', 1, 0, 1, 83.26, 'afbeeldingen/Batavus_Wayz_E-Go_Active_Ladies_NN330_400Wh_2017', '/33029_dfd0704/image/300x300'),
(69, 'Wayz E-Go Comfort Gentlemen 7V 300Wh 2017', 1, 0, 1, 54.11, 'afbeeldingen/Batavus_Wayz_E-Go_Comfort_Gentlemen_7V_300Wh_2017', '/33033_dfd0704/image/300x300'),
(70, 'Wayz E-Go Comfort Gentlemen 7V 400Wh 2017', 1, 0, 1, 58.71, 'afbeeldingen/Batavus_Wayz_E-Go_Comfort_Gentlemen_7V_400Wh_2017', '/33034_dfd0704/image/300x300'),
(71, 'Wayz E-Go Comfort Ladies 7V 300Wh 2017', 1, 0, 1, 54.11, 'afbeeldingen/Batavus_Wayz_E-Go_Comfort_Ladies_7V_300Wh_2017', '/33031_dfd0704/image/300x300'),
(72, 'Wayz E-Go Comfort Ladies 7V 400Wh 2017', 1, 0, 1, 58.71, 'afbeeldingen/Batavus_Wayz_E-Go_Comfort_Ladies_7V_400Wh_2017', '/33032_dfd0704/image/300x300'),
(73, 'Wayz E-Go Control Ltd Uni 8V 300Wh 2017', 1, 0, 1, 80.19, 'afbeeldingen/Batavus_Wayz_E-Go_Control_Ltd_Uni_8V_300Wh_2017', '/33035_dfd0704/image/300x300'),
(74, 'Wayz E-Go Control Ltd Uni 8V 400Wh 2017', 1, 0, 1, 84.79, 'afbeeldingen/Batavus_Wayz_E-Go_Control_Ltd_Uni_8V_400Wh_2017', '/33036_dfd0704/image/300x300'),
(75, 'Wayz E-Go Control Ltd Uni 8V 500Wh 2017', 1, 0, 1, 87.86, 'afbeeldingen/Batavus_Wayz_E-Go_Control_Ltd_Uni_8V_500Wh_2017', '/33037_dfd0704/image/300x300'),
(76, 'Wayz E-Go Control Ltd Uni 8V 600Wh 2017', 1, 0, 1, 90.93, 'afbeeldingen/Batavus_Wayz_E-Go_Control_Ltd_Uni_8V_600Wh_2017', '/33038_dfd0704/image/300x300'),
(77, 'Wayz E-Go Deluxe Gentlemen 7V 300Wh 2017', 1, 0, 1, 58.71, 'afbeeldingen/Batavus_Wayz_E-Go_Deluxe_Gentlemen_7V_300Wh_2017', '/33056_dfd0704/image/300x300'),
(78, 'Wayz E-Go Deluxe Gentlemen 7V 400Wh 2017', 1, 0, 1, 63.32, 'afbeeldingen/Batavus_Wayz_E-Go_Deluxe_Gentlemen_7V_400Wh_2017', '/33057_dfd0704/image/300x300'),
(79, 'Wayz E-Go Deluxe Gentlemen 7V 500Wh 2017', 1, 0, 1, 66.38, 'afbeeldingen/Batavus_Wayz_E-Go_Deluxe_Gentlemen_7V_500Wh_2017', '/33058_dfd0704/image/300x300'),
(80, 'Wayz E-Go Deluxe Ladies 7V 300Wh 2017', 1, 0, 1, 58.71, 'afbeeldingen/Batavus_Wayz_E-Go_Deluxe_Ladies_7V_300Wh_2017', '/33053_dfd0704/image/300x300'),
(81, 'Wayz E-Go Deluxe Ladies 7V 400Wh 2017', 1, 0, 1, 63.32, 'afbeeldingen/Batavus_Wayz_E-Go_Deluxe_Ladies_7V_400Wh_2017', '/33054_dfd0704/image/300x300'),
(82, 'Wayz E-Go Deluxe Ladies 7V 500Wh 2017', 1, 0, 1, 66.38, 'afbeeldingen/Batavus_Wayz_E-Go_Deluxe_Ladies_7V_500Wh_2017', '/33055_dfd0704/image/300x300'),
(83, 'Wayz E-Go Exclusive Ltd Gentlemen 8V 300Wh 2017', 1, 0, 1, 80.19, 'afbeeldingen/Batavus_Wayz_E-Go_Exclusive_Ltd_Gentlemen_8V_300Wh_2017', '/33063_dfd0704/image/300x300'),
(84, 'Wayz E-Go Exclusive Ltd Gentlemen 8V 400Wh 2017', 1, 0, 1, 84.79, 'afbeeldingen/Batavus_Wayz_E-Go_Exclusive_Ltd_Gentlemen_8V_400Wh_2017', '/33064_dfd0704/image/300x300'),
(85, 'Wayz E-Go Exclusive Ltd Gentlemen 8V 500Wh 2017', 1, 0, 1, 87.86, 'afbeeldingen/Batavus_Wayz_E-Go_Exclusive_Ltd_Gentlemen_8V_500Wh_2017', '/33065_dfd0704/image/300x300'),
(86, 'Wayz E-Go Exclusive Ltd Gentlemen 8V 600Wh 2017', 1, 0, 1, 90.93, 'afbeeldingen/Batavus_Wayz_E-Go_Exclusive_Ltd_Gentlemen_8V_600Wh_2017', '/33066_dfd0704/image/300x300'),
(87, 'Wayz E-Go Exclusive Ltd Ladies 8V 300Wh 2017', 1, 0, 1, 80.19, 'afbeeldingen/Batavus_Wayz_E-Go_Exclusive_Ltd_Ladies_8V_300Wh_2017', '/33059_dfd0704/image/300x300'),
(88, 'Wayz E-Go Exclusive Ltd Ladies 8V 400Wh 2017', 1, 0, 1, 84.79, 'afbeeldingen/Batavus_Wayz_E-Go_Exclusive_Ltd_Ladies_8V_400Wh_2017', '/33060_dfd0704/image/300x300'),
(89, 'Wayz E-Go Exclusive Ltd Ladies 8V 500Wh 2017', 1, 0, 1, 87.86, 'afbeeldingen/Batavus_Wayz_E-Go_Exclusive_Ltd_Ladies_8V_500Wh_2017', '/33061_dfd0704/image/300x300'),
(90, 'Wayz E-Go Exclusive Ltd Ladies 8V 600Wh 2017', 1, 0, 1, 90.93, 'afbeeldingen/Batavus_Wayz_E-Go_Exclusive_Ltd_Ladies_8V_600Wh_2017', '/33062_dfd0704/image/300x300'),
(91, 'Wayz Gentlemen 8V 2017', 0, 0, 1, 23.9, 'afbeeldingen/Batavus_Wayz_Gentlemen_8V_2017', '/33128_dfd0704/image/300x300'),
(92, 'Wayz Ladies 8V 2017', 0, 0, 1, 23.9, 'afbeeldingen/Batavus_Wayz_Ladies_8V_2017', '/33127_dfd0704/image/300x300'),
(93, 'Winner Gentlemen 3V 2017', 0, 0, 1, 16.85, 'afbeeldingen/Batavus_Winner_Gentlemen_3V_2017', '/33132_dfd0704/image/300x300'),
(94, 'Winner Ladies 3V 2017', 0, 0, 1, 16.85, 'afbeeldingen/Batavus_Winner_Ladies_3V_2017', '/33131_dfd0704/image/300x300'),
(95, 'X-Posure Gentlemen 3V 2017', 0, 0, 1, 19.91, 'afbeeldingen/Batavus_X-Posure_Gentlemen_3V_2017', '/33134_dfd0704/image/300x300'),
(96, 'X-Posure Ladies 3V 2017', 0, 0, 1, 19.91, 'afbeeldingen/Batavus_X-Posure_Ladies_3V_2017', '/33133_dfd0704/image/300x300'),
(97, 'Zonar Comfort Gentlemen 2017', 0, 0, 1, 27.58, 'afbeeldingen/Batavus_Zonar_Comfort_Gentlemen_2017', '/34458_ddb5c2e/image/300x300'),
(98, 'Zonar Comfort Ladies 2017', 0, 0, 1, 27.58, 'afbeeldingen/Batavus_Zonar_Comfort_Ladies_2017', '/34457_ddb5c2e/image/300x300'),
(99, 'Zonar Gentlemen 2017', 0, 0, 1, 24.52, 'afbeeldingen/Batavus_Zonar_Gentlemen_2017', '/34456_ddb5c2e/image/300x300'),
(100, 'Zonar Ladies 2017', 0, 0, 1, 24.52, 'afbeeldingen/Batavus_Zonar_Ladies_2017', '/34455_ddb5c2e/image/300x300'),
(101, 'Zonar X-Light Gentlemen 2017', 0, 0, 1, 33.72, 'afbeeldingen/Batavus_Zonar_X-Light_Gentlemen_2017', '/34460_ddb5c2e/image/300x300'),
(102, 'Zonar X-Light Ladies 2017', 0, 0, 1, 33.72, 'afbeeldingen/Batavus_Zonar_X-Light_Ladies_2017', '/34459_ddb5c2e/image/300x300'),
(103, 'A-Class   2016', 0, 0, 2, 59.51, 'afbeeldingen/2_A-Class___2016', '/28959_efb63db/image/300x300'),
(104, 'B-Qin   2016', 0, 0, 2, 18.82, 'afbeeldingen/2_B-Qin___2016', '/28951_efb63db/image/300x300'),
(105, 'Bizo 7Even 2016', 0, 0, 2, 52.58, 'afbeeldingen/2_Bizo_7Even_2016', '/28956_efb63db/image/300x300'),
(106, 'Carbon N7 2016', 0, 0, 2, 52.58, 'afbeeldingen/2_Carbon_N7_2016', '/28952_efb63db/image/300x300'),
(107, 'E-Trendy   2016', 0, 0, 2, 49.51, 'afbeeldingen/2_E-Trendy___2016', '/28955_efb63db/image/300x300'),
(108, 'Emotion III 24V 2016', 0, 0, 2, 40.3, 'afbeeldingen/2_Emotion_III_24V_2016', '/28953_efb63db/image/300x300'),
(109, 'Miesty Bello   2016', 0, 0, 2, 53.37, 'afbeeldingen/2_Miesty_Bello___2016', '/28957_efb63db/image/300x300'),
(110, 'Renault 24V 2016', 0, 0, 2, 44.17, 'afbeeldingen/2_Renault_24V_2016', '/28954_efb63db/image/300x300'),
(111, 'Swies 16 2016', 0, 0, 2, 56.44, 'afbeeldingen/2_Swies_16_2016', '/28958_efb63db/image/300x300'),
(112, 'EMR Urban 400Wh heer 8V 2016', 0, 0, 3, 74.08, 'afbeeldingen/Conway_EMR_Urban_400Wh_heer_8V_2016', '/26350_efb63db/image/300x300'),
(113, 'Booster 2017', 0, 0, 4, 30.65, 'afbeeldingen/E-Twow_Booster_2017', '/34207_7236826/image/300x300'),
(114, 'Eco 2017', 0, 0, 4, 24.52, 'afbeeldingen/E-Twow_Eco_2017', '/28165_88fa1c4/image/300x300'),
(115, 'Master  2017', 0, 0, 4, 28.03, 'afbeeldingen/E-Twow_Master__2017', '/34337_8faeb0b/image/300x300'),
(116, 'Anthem 2 GE 2017', 0, 0, 5, 73.61, 'afbeeldingen/Giant_Anthem_2_GE_2017', '/29580_8c5edae/image/300x300'),
(117, 'Anthem 3 2017', 0, 0, 5, 55.2, 'afbeeldingen/Giant_Anthem_3_2017', '/29581_8c5edae/image/300x300'),
(118, 'Anthem Advanced 1 2017', 0, 0, 5, 125.77, 'afbeeldingen/Giant_Anthem_Advanced_1_2017', '/29579_8c5edae/image/300x300'),
(119, 'Anyroad 2 2017', 0, 0, 5, 29.12, 'afbeeldingen/Giant_Anyroad_2_2017', '/29623_8c5edae/image/300x300'),
(120, 'Argento 1 GB GTS 2017', 0, 0, 5, 27.58, 'afbeeldingen/Giant_Argento_1_GB_GTS_2017', '/29575_8c5edae/image/300x300'),
(121, 'Argento 1 GB LDS 2017', 0, 0, 5, 27.58, 'afbeeldingen/Giant_Argento_1_GB_LDS_2017', '/29576_8c5edae/image/300x300'),
(122, 'Argento 2 GB GTS 2017', 0, 0, 5, 24.52, 'afbeeldingen/Giant_Argento_2_GB_GTS_2017', '/29577_8c5edae/image/300x300'),
(123, 'Argento 2 GB LDS 2017', 0, 0, 5, 24.52, 'afbeeldingen/Giant_Argento_2_GB_LDS_2017', '/29578_8c5edae/image/300x300'),
(124, 'Aspiro 0 GTS 2017', 0, 0, 5, 52.13, 'afbeeldingen/Giant_Aspiro_0_GTS_2017', '/29569_8c5edae/image/300x300'),
(125, 'Aspiro 0 LDS 2017', 0, 0, 5, 52.13, 'afbeeldingen/Giant_Aspiro_0_LDS_2017', '/29570_8c5edae/image/300x300'),
(126, 'Aspiro 1 GB GTS 2017', 0, 0, 5, 36.79, 'afbeeldingen/Giant_Aspiro_1_GB_GTS_2017', '/29571_8c5edae/image/300x300'),
(127, 'Aspiro 1 GB LDS 2017', 0, 0, 5, 36.79, 'afbeeldingen/Giant_Aspiro_1_GB_LDS_2017', '/29572_8c5edae/image/300x300'),
(128, 'Aspiro 2 GB GTS 2017', 0, 0, 5, 30.65, 'afbeeldingen/Giant_Aspiro_2_GB_GTS_2017', '/29573_8c5edae/image/300x300'),
(129, 'Aspiro 2 GB LDS 2017', 0, 0, 5, 30.65, 'afbeeldingen/Giant_Aspiro_2_GB_LDS_2017', '/29574_8c5edae/image/300x300'),
(130, 'Chill 2 GTS 2017', 0, 0, 5, 17.46, 'afbeeldingen/Giant_Chill_2_GTS_2017', '/29521_8c5edae/image/300x300'),
(131, 'Chill 2 LDS 2017', 0, 0, 5, 17.46, 'afbeeldingen/Giant_Chill_2_LDS_2017', '/29520_8c5edae/image/300x300'),
(132, 'Dirt E+ 0 25 km/h 2017', 1, 0, 5, 123.15, 'afbeeldingen/Giant_Dirt_E+_0_25_kmh_2017', '/29511_8c5edae/image/300x300'),
(133, 'Dirt E+ 1 25 km/h 2017', 1, 0, 5, 89.4, 'afbeeldingen/Giant_Dirt_E+_1_25_kmh_2017', '/29512_8c5edae/image/300x300'),
(134, 'Dirt E+ 2 25 km/h 2017', 1, 0, 5, 77.12, 'afbeeldingen/Giant_Dirt_E+_2_25_kmh_2017', '/29513_8c5edae/image/300x300'),
(135, 'Ease E 1 DX 2017', 0, 0, 5, 64.85, 'afbeeldingen/Giant_Ease_E_1_DX_2017', '/29506_8c5edae/image/300x300'),
(136, 'Ease E 2 RB 2017', 0, 0, 5, 58.71, 'afbeeldingen/Giant_Ease_E_2_RB_2017', '/29507_8c5edae/image/300x300'),
(137, 'Ease E 3 RB 2017', 0, 0, 5, 52.58, 'afbeeldingen/Giant_Ease_E_3_RB_2017', '/29508_8c5edae/image/300x300'),
(138, 'Elegance E+ 0 2017', 1, 0, 5, 92.46, 'afbeeldingen/Giant_Elegance_E+_0_2017', '/29498_8c5edae/image/300x300'),
(139, 'Elegance E+ 1 DX 2017', 1, 0, 5, 83.26, 'afbeeldingen/Giant_Elegance_E+_1_DX_2017', '/29499_8c5edae/image/300x300'),
(140, 'Elegance E+ 2 2017', 1, 0, 5, 77.12, 'afbeeldingen/Giant_Elegance_E+_2_2017', '/29500_8c5edae/image/300x300'),
(141, 'Escape 1 2017', 0, 0, 5, 19.3, 'afbeeldingen/Giant_Escape_1_2017', '/29626_8c5edae/image/300x300'),
(142, 'Explore E+ 0 25 km/h 2017', 1, 0, 5, 101.67, 'afbeeldingen/Giant_Explore_E+_0_25_kmh_2017', '/29504_8c5edae/image/300x300'),
(143, 'Explore E+ 1 25 km/h 2017', 1, 0, 5, 83.26, 'afbeeldingen/Giant_Explore_E+_1_25_kmh_2017', '/29505_8c5edae/image/300x300'),
(144, 'FastCity/Allure CS 1 2017', 0, 0, 5, 30.65, 'afbeeldingen/Giant_FastCityAllure_CS_1_2017', '/29568_8c5edae/image/300x300'),
(145, 'FastCity/Allure RS 1 2017', 0, 0, 5, 33.72, 'afbeeldingen/Giant_FastCityAllure_RS_1_2017', '/29526_8c5edae/image/300x300'),
(146, 'FastCity/Allure RS 2 2017', 0, 0, 5, 27.58, 'afbeeldingen/Giant_FastCityAllure_RS_2_2017', '/29527_8c5edae/image/300x300'),
(147, 'Fastroad CoMax 1 2017', 0, 0, 5, 49.06, 'afbeeldingen/Giant_Fastroad_CoMax_1_2017', '/29624_8c5edae/image/300x300'),
(148, 'Fastroad SLR 2 2017', 0, 0, 5, 27.58, 'afbeeldingen/Giant_Fastroad_SLR_2_2017', '/29625_8c5edae/image/300x300'),
(149, 'Fathom 29er 0 2017', 0, 0, 5, 45.99, 'afbeeldingen/Giant_Fathom_29er_0_2017', '/29612_8c5edae/image/300x300'),
(150, 'Fathom 29er 1 LTD 2017', 0, 0, 5, 36.79, 'afbeeldingen/Giant_Fathom_29er_1_LTD_2017', '/29613_8c5edae/image/300x300'),
(151, 'Fathom 29er 2 2017', 0, 0, 5, 26.05, 'afbeeldingen/Giant_Fathom_29er_2_2017', '/29615_8c5edae/image/300x300'),
(152, 'Fathom 29er 2 LTD 2017', 0, 0, 5, 30.65, 'afbeeldingen/Giant_Fathom_29er_2_LTD_2017', '/29614_8c5edae/image/300x300'),
(153, 'Full E+ 1 25 km/h 2017', 1, 0, 5, 141.56, 'afbeeldingen/Giant_Full_E+_1_25_kmh_2017', '/29514_8c5edae/image/300x300'),
(154, 'Full E+ 2 25 km/h 2017', 1, 0, 5, 113.94, 'afbeeldingen/Giant_Full_E+_2_25_kmh_2017', '/29515_8c5edae/image/300x300'),
(155, 'Prime E+ 1 2017', 1, 0, 5, 86.33, 'afbeeldingen/Giant_Prime_E+_1_2017', '/29501_8c5edae/image/300x300'),
(156, 'Prime E+ 2 GTS 2017', 1, 0, 5, 83.26, 'afbeeldingen/Giant_Prime_E+_2_GTS_2017', '/29502_8c5edae/image/300x300'),
(157, 'Prime E+ 2 LDS 2017', 1, 0, 5, 83.26, 'afbeeldingen/Giant_Prime_E+_2_LDS_2017', '/29503_8c5edae/image/300x300'),
(158, 'Reign 1.5 LTD 2017', 0, 0, 5, 95.09, 'afbeeldingen/Giant_Reign_1.5_LTD_2017', '/29583_8c5edae/image/300x300'),
(159, 'Reign 2 LTD 2017', 0, 0, 5, 76.68, 'afbeeldingen/Giant_Reign_2_LTD_2017', '/29584_8c5edae/image/300x300'),
(160, 'Revel 29er 1 2017', 0, 0, 5, 21.45, 'afbeeldingen/Giant_Revel_29er_1_2017', '/29618_8c5edae/image/300x300'),
(161, 'Revel 29er 2 2017', 0, 0, 5, 16.85, 'afbeeldingen/Giant_Revel_29er_2_2017', '/29619_8c5edae/image/300x300'),
(162, 'Roam 1 Disc 2017', 0, 0, 5, 21.45, 'afbeeldingen/Giant_Roam_1_Disc_2017', '/29627_8c5edae/image/300x300'),
(163, 'Talon 1 LTD 2017', 0, 0, 5, 24.52, 'afbeeldingen/Giant_Talon_1_LTD_2017', '/29616_8c5edae/image/300x300'),
(164, 'Talon 2 LTD 2017', 0, 0, 5, 21.45, 'afbeeldingen/Giant_Talon_2_LTD_2017', '/29617_8c5edae/image/300x300'),
(165, 'Toughroad SLR 0 2017', 0, 0, 5, 39.86, 'afbeeldingen/Giant_Toughroad_SLR_0_2017', '/29620_8c5edae/image/300x300'),
(166, 'Toughroad SLR 1 2017', 0, 0, 5, 35.26, 'afbeeldingen/Giant_Toughroad_SLR_1_2017', '/29621_8c5edae/image/300x300'),
(167, 'Toughroad SLR 2 2017', 0, 0, 5, 24.52, 'afbeeldingen/Giant_Toughroad_SLR_2_2017', '/29622_8c5edae/image/300x300'),
(168, 'Trance 1.5 LTD 2017', 0, 0, 5, 85.88, 'afbeeldingen/Giant_Trance_1.5_LTD_2017', '/29582_8c5edae/image/300x300'),
(169, 'Triple X 1 GTS 2017', 0, 0, 5, 22.98, 'afbeeldingen/Giant_Triple_X_1_GTS_2017', '/29522_8c5edae/image/300x300'),
(170, 'Triple X 1 LDS 2017', 0, 0, 5, 22.98, 'afbeeldingen/Giant_Triple_X_1_LDS_2017', '/29523_8c5edae/image/300x300'),
(171, 'Triple X 2 GTS 2017', 0, 0, 5, 19.91, 'afbeeldingen/Giant_Triple_X_2_GTS_2017', '/29524_8c5edae/image/300x300'),
(172, 'Triple X 2 LDS 2017', 0, 0, 5, 19.91, 'afbeeldingen/Giant_Triple_X_2_LDS_2017', '/29525_8c5edae/image/300x300'),
(173, 'Triple X E+ 1 GTS 2017', 1, 0, 5, 46.44, 'afbeeldingen/Giant_Triple_X_E+_1_GTS_2017', '/29509_8c5edae/image/300x300'),
(174, 'Triple X E+ 1 LDS 2017', 1, 0, 5, 46.44, 'afbeeldingen/Giant_Triple_X_E+_1_LDS_2017', '/29510_8c5edae/image/300x300'),
(175, 'Ultimo 1 GTS 2017', 0, 0, 5, 26.05, 'afbeeldingen/Giant_Ultimo_1_GTS_2017', '/29517_8c5edae/image/300x300'),
(176, 'Ultimo 1 LDS 2017', 0, 0, 5, 26.05, 'afbeeldingen/Giant_Ultimo_1_LDS_2017', '/29516_8c5edae/image/300x300'),
(177, 'Ultimo 2 GTS 2017', 0, 0, 5, 22.98, 'afbeeldingen/Giant_Ultimo_2_GTS_2017', '/29519_8c5edae/image/300x300'),
(178, 'Ultimo 2 LDS 2017', 0, 0, 5, 22.98, 'afbeeldingen/Giant_Ultimo_2_LDS_2017', '/29518_8c5edae/image/300x300'),
(179, 'XTC Advanced + 1 2017', 0, 0, 5, 92.02, 'afbeeldingen/Giant_XTC_Advanced_+_1_2017', '/29609_8c5edae/image/300x300'),
(180, 'XTC Advanced 1 2017', 0, 0, 5, 98.16, 'afbeeldingen/Giant_XTC_Advanced_1_2017', '/29610_8c5edae/image/300x300'),
(181, 'XTC Advanced 29er 0 2017', 0, 0, 5, 153.11, 'afbeeldingen/Giant_XTC_Advanced_29er_0_2017', '/29585_8c5edae/image/300x300'),
(182, 'XTC Advanced 29er 1.5 LTD 2017', 0, 0, 5, 70.54, 'afbeeldingen/Giant_XTC_Advanced_29er_1.5_LTD_2017', '/29586_8c5edae/image/300x300'),
(183, 'XTC Advanced 29er 2 LTD 2017', 0, 0, 5, 55.2, 'afbeeldingen/Giant_XTC_Advanced_29er_2_LTD_2017', '/29587_8c5edae/image/300x300'),
(184, 'XTC Advanced 29er 3 GE 2017', 0, 0, 5, 45.99, 'afbeeldingen/Giant_XTC_Advanced_29er_3_GE_2017', '/29608_8c5edae/image/300x300'),
(185, 'XTC Advanced 3 2017', 0, 0, 5, 58.27, 'afbeeldingen/Giant_XTC_Advanced_3_2017', '/29611_8c5edae/image/300x300'),
(186, 'G2R Portable + Commuter 2015', 0, 0, 6, 107.81, 'afbeeldingen/Gocycle_G2R_Portable_+_Commuter_2015', '/17624_efb63db/image'),
(187, 'G3 Base Pack + Commuter Pack 2016', 0, 0, 6, 144.63, 'afbeeldingen/Gocycle_G3_Base_Pack_+_Commuter_Pack_2016', '/27028_701ead7/image'),
(188, 'Direct Drive Men N8 13Ah 2016', 0, 0, 7, 61.78, 'afbeeldingen/Jools_Direct_Drive_Men_N8_13Ah_2016', '/32675_54f5652/image/300x300'),
(189, 'Direct Drive Women N8 13Ah 2016', 0, 0, 7, 61.78, 'afbeeldingen/Jools_Direct_Drive_Women_N8_13Ah_2016', '/32674_54f5652/image/300x300'),
(190, 'E\'coHub Men 7sp 36V/13Ah/250W 2016', 0, 0, 7, 40.18, 'afbeeldingen/Jools_E\'coHub_Men_7sp_36V13Ah250W_2016', '/31172_54f5652/image/300x300'),
(191, 'E\'coHub Women 7sp 36V/13Ah/250W  2016', 0, 0, 7, 40.18, 'afbeeldingen/Jools_E\'coHub_Women_7sp_36V13Ah250W__2016', '/31178_54f5652/image/300x300'),
(192, 'Eas\'E Bike Uni 6V 5,8Ah 2016', 0, 0, 7, 34.17, 'afbeeldingen/Jools_Eas\'E_Bike_Uni_6V_5,8Ah_2016', '/32678_54f5652/image/300x300'),
(193, 'Max\'E Drive Men N8 13Ah 2016', 0, 0, 7, 70.99, 'afbeeldingen/Jools_Max\'E_Drive_Men_N8_13Ah_2016', '/32677_54f5652/image/300x300'),
(194, 'Max\'E Drive Women N8 13Ah 2016', 0, 0, 7, 70.99, 'afbeeldingen/Jools_Max\'E_Drive_Women_N8_13Ah_2016', '/32676_54f5652/image/300x300'),
(195, 'Blast 27.5 Acera 2017', 0, 0, 8, 19.91, 'afbeeldingen/Ridley_Blast_27.5_Acera_2017', '/31558_e770aa6/image/300x300'),
(196, 'Blast 27.5 Deore 2017', 0, 0, 8, 24.52, 'afbeeldingen/Ridley_Blast_27.5_Deore_2017', '/31556_e770aa6/image/300x300'),
(197, 'Blast 27.5 SLX-Deore 2017', 0, 0, 8, 28.5, 'afbeeldingen/Ridley_Blast_27.5_SLX-Deore_2017', '/31554_e770aa6/image/300x300'),
(198, 'Blast 29 Acera 2017', 0, 0, 8, 19.91, 'afbeeldingen/Ridley_Blast_29_Acera_2017', '/31557_e770aa6/image/300x300'),
(199, 'Blast 29 Deore 2017', 0, 0, 8, 24.52, 'afbeeldingen/Ridley_Blast_29_Deore_2017', '/31555_e770aa6/image/300x300'),
(200, 'Blast 29 SLX-Deore 2017', 0, 0, 8, 28.5, 'afbeeldingen/Ridley_Blast_29_SLX-Deore_2017', '/31553_e770aa6/image/300x300'),
(201, 'Fenix A 105 Mix 2017', 0, 0, 8, 39.86, 'afbeeldingen/Ridley_Fenix_A_105_Mix_2017', '/31458_e770aa6/image/300x300'),
(202, 'Fenix A Disc 105 Mix 2017', 0, 0, 8, 52.13, 'afbeeldingen/Ridley_Fenix_A_Disc_105_Mix_2017', '/31455_e770aa6/image/300x300'),
(203, 'Fenix A Disc Tiagra 2017', 0, 0, 8, 41.39, 'afbeeldingen/Ridley_Fenix_A_Disc_Tiagra_2017', '/31456_e770aa6/image/300x300'),
(204, 'Fenix A Tiagra 2017', 0, 0, 8, 36.79, 'afbeeldingen/Ridley_Fenix_A_Tiagra_2017', '/31459_e770aa6/image/300x300'),
(205, 'Fenix A Ultegra Mix 2017', 0, 0, 8, 42.93, 'afbeeldingen/Ridley_Fenix_A_Ultegra_Mix_2017', '/31457_e770aa6/image/300x300'),
(206, 'Fenix C 105 Mix 2017', 0, 0, 8, 53.66, 'afbeeldingen/Ridley_Fenix_C_105_Mix_2017', '/31454_e770aa6/image/300x300'),
(207, 'Fenix C Disc 105 Mix 2017', 0, 0, 8, 76.68, 'afbeeldingen/Ridley_Fenix_C_Disc_105_Mix_2017', '/31452_e770aa6/image/300x300'),
(208, 'Fenix C Disc Ultegra 2017', 0, 0, 8, 92.02, 'afbeeldingen/Ridley_Fenix_C_Disc_Ultegra_2017', '/31451_e770aa6/image/300x300'),
(209, 'Fenix C Ultegra Mix 2017', 0, 0, 8, 58.27, 'afbeeldingen/Ridley_Fenix_C_Ultegra_Mix_2017', '/31453_e770aa6/image/300x300'),
(210, 'Fenix SL 105 Mix 2017', 0, 0, 8, 64.4, 'afbeeldingen/Ridley_Fenix_SL_105_Mix_2017', '/31423_e770aa6/image/300x300'),
(211, 'Fenix SL Disc 105 Mix 2017', 0, 0, 8, 85.88, 'afbeeldingen/Ridley_Fenix_SL_Disc_105_Mix_2017', '/31419_e770aa6/image/300x300'),
(212, 'Fenix SL Disc Ultegra 2017', 0, 0, 8, 104.29, 'afbeeldingen/Ridley_Fenix_SL_Disc_Ultegra_2017', '/31418_e770aa6/image/300x300'),
(213, 'Fenix SL Potenza 2017', 0, 0, 8, 82.81, 'afbeeldingen/Ridley_Fenix_SL_Potenza_2017', '/31420_e770aa6/image/300x300'),
(214, 'Fenix SL Ultegra 2017', 0, 0, 8, 79.75, 'afbeeldingen/Ridley_Fenix_SL_Ultegra_2017', '/31421_e770aa6/image/300x300'),
(215, 'Fenix SL Ultegra Mix 2017', 0, 0, 8, 70.54, 'afbeeldingen/Ridley_Fenix_SL_Ultegra_Mix_2017', '/31422_e770aa6/image/300x300'),
(216, 'Helium SLA 105 Mix 2017', 0, 0, 8, 45.99, 'afbeeldingen/Ridley_Helium_SLA_105_Mix_2017', '/31417_e770aa6/image/300x300'),
(217, 'Helium SLA Ultegra 2017', 0, 0, 8, 58.27, 'afbeeldingen/Ridley_Helium_SLA_Ultegra_2017', '/31416_e770aa6/image/300x300'),
(218, 'Ignite A 27.5 SLX-Deore 2017', 0, 0, 8, 33.72, 'afbeeldingen/Ridley_Ignite_A_27.5_SLX-Deore_2017', '/31552_e770aa6/image/300x300'),
(219, 'Ignite A 27.5 SLX-Deore SL 2017', 0, 0, 8, 39.86, 'afbeeldingen/Ridley_Ignite_A_27.5_SLX-Deore_SL_2017', '/31550_e770aa6/image/300x300'),
(220, 'Ignite A 27.5 XT-SLX 2017', 0, 0, 8, 52.13, 'afbeeldingen/Ridley_Ignite_A_27.5_XT-SLX_2017', '/31548_e770aa6/image/300x300'),
(221, 'Ignite A 29 SLX-Deore 2017', 0, 0, 8, 33.72, 'afbeeldingen/Ridley_Ignite_A_29_SLX-Deore_2017', '/31551_e770aa6/image/300x300'),
(222, 'Ignite A 29 SLX-Deore SL 2017', 0, 0, 8, 39.86, 'afbeeldingen/Ridley_Ignite_A_29_SLX-Deore_SL_2017', '/31549_e770aa6/image/300x300'),
(223, 'Ignite A 29 XT-SLX 2017', 0, 0, 8, 52.13, 'afbeeldingen/Ridley_Ignite_A_29_XT-SLX_2017', '/31547_e770aa6/image/300x300'),
(224, 'Ignite C 27.5 GX1 2017', 0, 0, 8, 76.68, 'afbeeldingen/Ridley_Ignite_C_27.5_GX1_2017', '/31479_e770aa6/image/300x300'),
(225, 'Ignite C 27.5 SLX-Deore 2017', 0, 0, 8, 55.2, 'afbeeldingen/Ridley_Ignite_C_27.5_SLX-Deore_2017', '/31483_e770aa6/image/300x300'),
(226, 'Ignite C 27.5 XT-SLX 2017', 0, 0, 8, 61.34, 'afbeeldingen/Ridley_Ignite_C_27.5_XT-SLX_2017', '/31481_e770aa6/image/300x300'),
(227, 'Ignite C 29 GX1 2017', 0, 0, 8, 76.68, 'afbeeldingen/Ridley_Ignite_C_29_GX1_2017', '/31478_e770aa6/image/300x300'),
(228, 'Ignite C 29 SLX-Deore 2017', 0, 0, 8, 55.2, 'afbeeldingen/Ridley_Ignite_C_29_SLX-Deore_2017', '/31482_e770aa6/image/300x300'),
(229, 'Ignite C 29 XT-SLX 2017', 0, 0, 8, 61.34, 'afbeeldingen/Ridley_Ignite_C_29_XT-SLX_2017', '/31480_e770aa6/image/300x300'),
(230, 'Ignite CSL 27.5 XT 2017', 0, 0, 8, 92.02, 'afbeeldingen/Ridley_Ignite_CSL_27.5_XT_2017', '/31477_e770aa6/image/300x300'),
(231, 'Ignite CSL 27.5 XTR 2017', 0, 0, 8, 122.7, 'afbeeldingen/Ridley_Ignite_CSL_27.5_XTR_2017', '/31475_e770aa6/image/300x300'),
(232, 'Ignite CSL 27.5 XX1 Eagle 2017', 0, 0, 8, 184.07, 'afbeeldingen/Ridley_Ignite_CSL_27.5_XX1_Eagle_2017', '/31473_e770aa6/image/300x300'),
(233, 'Ignite CSL 29 XT 2017', 0, 0, 8, 92.02, 'afbeeldingen/Ridley_Ignite_CSL_29_XT_2017', '/31476_e770aa6/image/300x300'),
(234, 'Ignite CSL 29 XTR 2017', 0, 0, 8, 122.7, 'afbeeldingen/Ridley_Ignite_CSL_29_XTR_2017', '/31474_e770aa6/image/300x300'),
(235, 'Ignite CSL 29 XX1 Eagle 2017', 0, 0, 8, 184.07, 'afbeeldingen/Ridley_Ignite_CSL_29_XX1_Eagle_2017', '/31472_e770aa6/image/300x300'),
(236, 'Jane Potenza 2017', 0, 0, 8, 107.36, 'afbeeldingen/Ridley_Jane_Potenza_2017', '/31580_e770aa6/image/300x300'),
(237, 'Jane SL Disc Ultegra 2017', 0, 0, 8, 134.98, 'afbeeldingen/Ridley_Jane_SL_Disc_Ultegra_2017', '/31576_e770aa6/image/300x300'),
(238, 'Jane SL Disc Ultegra Di2 2017', 0, 0, 8, 168.73, 'afbeeldingen/Ridley_Jane_SL_Disc_Ultegra_Di2_2017', '/31575_e770aa6/image/300x300'),
(239, 'Jane SL Potenza 2017', 0, 0, 8, 128.84, 'afbeeldingen/Ridley_Jane_SL_Potenza_2017', '/31578_e770aa6/image/300x300'),
(240, 'Jane SL Ultegra 2017', 0, 0, 8, 121.17, 'afbeeldingen/Ridley_Jane_SL_Ultegra_2017', '/31579_e770aa6/image/300x300'),
(241, 'Jane SL Ultegra Di2 2017', 0, 0, 8, 150.32, 'afbeeldingen/Ridley_Jane_SL_Ultegra_Di2_2017', '/31577_e770aa6/image/300x300'),
(242, 'Jane Ultegra 2017', 0, 0, 8, 101.22, 'afbeeldingen/Ridley_Jane_Ultegra_2017', '/31581_e770aa6/image/300x300'),
(243, 'Jane Ultegra Mix 2017', 0, 0, 8, 85.88, 'afbeeldingen/Ridley_Jane_Ultegra_Mix_2017', '/31582_e770aa6/image/300x300'),
(244, 'Liz A 105 Mix 2017', 0, 0, 8, 39.86, 'afbeeldingen/Ridley_Liz_A_105_Mix_2017', '/31604_e770aa6/image/300x300'),
(245, 'Liz A Sora 2017', 0, 0, 8, 33.72, 'afbeeldingen/Ridley_Liz_A_Sora_2017', '/31606_e770aa6/image/300x300'),
(246, 'Liz A Tiagra 2017', 0, 0, 8, 36.79, 'afbeeldingen/Ridley_Liz_A_Tiagra_2017', '/31605_e770aa6/image/300x300'),
(247, 'Liz C 105 Mix 2017', 0, 0, 8, 53.66, 'afbeeldingen/Ridley_Liz_C_105_Mix_2017', '/31603_e770aa6/image/300x300'),
(248, 'Liz C Ultegra Mix 2017', 0, 0, 8, 58.27, 'afbeeldingen/Ridley_Liz_C_Ultegra_Mix_2017', '/31602_e770aa6/image/300x300'),
(249, 'Liz SL 105 Mix 2017', 0, 0, 8, 64.4, 'afbeeldingen/Ridley_Liz_SL_105_Mix_2017', '/31601_e770aa6/image/300x300'),
(250, 'Liz SL Disc 105 Mix 2017', 0, 0, 8, 85.88, 'afbeeldingen/Ridley_Liz_SL_Disc_105_Mix_2017', '/31597_e770aa6/image/300x300'),
(251, 'Liz SL Disc Ultegra 2017', 0, 0, 8, 104.29, 'afbeeldingen/Ridley_Liz_SL_Disc_Ultegra_2017', '/31596_e770aa6/image/300x300'),
(252, 'Liz SL Disc Ultegra Di2 2017', 0, 0, 8, 134.98, 'afbeeldingen/Ridley_Liz_SL_Disc_Ultegra_Di2_2017', '/31595_e770aa6/image/300x300'),
(253, 'Liz SL Potenza 2017', 0, 0, 8, 82.81, 'afbeeldingen/Ridley_Liz_SL_Potenza_2017', '/31598_e770aa6/image/300x300'),
(254, 'Liz SL Ultegra 2017', 0, 0, 8, 79.75, 'afbeeldingen/Ridley_Liz_SL_Ultegra_2017', '/31599_e770aa6/image/300x300'),
(255, 'Liz SL Ultegra Mix 2017', 0, 0, 8, 70.54, 'afbeeldingen/Ridley_Liz_SL_Ultegra_Mix_2017', '/31600_e770aa6/image/300x300'),
(256, 'Noah Potenza 2017', 0, 0, 8, 107.36, 'afbeeldingen/Ridley_Noah_Potenza_2017', '/31405_e770aa6/image/300x300'),
(257, 'Noah SL Disc Ultegra 2017', 0, 0, 8, 134.98, 'afbeeldingen/Ridley_Noah_SL_Disc_Ultegra_2017', '/31401_e770aa6/image/300x300'),
(258, 'Noah SL Disc Ultegra Di2 2017', 0, 0, 8, 168.73, 'afbeeldingen/Ridley_Noah_SL_Disc_Ultegra_Di2_2017', '/31400_e770aa6/image/300x300'),
(259, 'Noah SL Potenza 2017', 0, 0, 8, 128.84, 'afbeeldingen/Ridley_Noah_SL_Potenza_2017', '/31403_e770aa6/image/300x300'),
(260, 'Noah SL Ultegra 2017', 0, 0, 8, 121.17, 'afbeeldingen/Ridley_Noah_SL_Ultegra_2017', '/31276_e770aa6/image/300x300'),
(261, 'Noah SL Ultegra Di2 2017', 0, 0, 8, 150.32, 'afbeeldingen/Ridley_Noah_SL_Ultegra_Di2_2017', '/31402_e770aa6/image/300x300'),
(262, 'Noah Ultegra 2017', 0, 0, 8, 101.22, 'afbeeldingen/Ridley_Noah_Ultegra_2017', '/31406_e770aa6/image/300x300'),
(263, 'Noah Ultegra Mix 2017', 0, 0, 8, 85.88, 'afbeeldingen/Ridley_Noah_Ultegra_Mix_2017', '/31407_e770aa6/image/300x300'),
(264, 'Tempo X Men Disc 2017', 0, 0, 8, 33.72, 'afbeeldingen/Ridley_Tempo_X_Men_Disc_2017', '/31571_e770aa6/image/300x300'),
(265, 'Tempo X Men V-Brake 2017', 0, 0, 8, 27.58, 'afbeeldingen/Ridley_Tempo_X_Men_V-Brake_2017', '/31573_e770aa6/image/300x300'),
(266, 'Tempo X Women Disc 2017', 0, 0, 8, 33.72, 'afbeeldingen/Ridley_Tempo_X_Women_Disc_2017', '/31572_e770aa6/image/300x300'),
(267, 'Tempo X Women V-Brake 2017', 0, 0, 8, 27.58, 'afbeeldingen/Ridley_Tempo_X_Women_V-Brake_2017', '/31574_e770aa6/image/300x300'),
(268, 'Classic Gentlemen 7sp 2017', 0, 0, 9, 40.18, 'afbeeldingen/Thompson_Classic_Gentlemen_7sp_2017', '/32496_b93683f/image/300x300'),
(269, 'Classic Gentlemen N7 2017', 0, 0, 9, 45.87, 'afbeeldingen/Thompson_Classic_Gentlemen_N7_2017', '/32498_c791d54/image/300x300'),
(270, 'Classic Ladies 7sp 2017', 0, 0, 9, 40.18, 'afbeeldingen/Thompson_Classic_Ladies_7sp_2017', '/32495_e89cc5a/image/300x300'),
(271, 'Classic Ladies N7 2017', 0, 0, 9, 45.87, 'afbeeldingen/Thompson_Classic_Ladies_N7_2017', '/32497_c791d54/image/300x300'),
(272, 'Elegance Gentlemen 7sp 2017', 0, 0, 9, 40.18, 'afbeeldingen/Thompson_Elegance_Gentlemen_7sp_2017', '/34247_7d9616c/image/300x300'),
(273, 'Elegance Ladies 7sp 2017', 0, 0, 9, 40.18, 'afbeeldingen/Thompson_Elegance_Ladies_7sp_2017', '/34246_23863ab/image/300x300'),
(274, 'Expert Disc 24V dame 2015', 0, 0, 9, 24.39, 'afbeeldingen/Thompson_Expert_Disc_24V_dame_2015', '/20241_efb63db/image/300x300'),
(275, 'Expert Disc 24V heer 2015', 0, 0, 9, 24.39, 'afbeeldingen/Thompson_Expert_Disc_24V_heer_2015', '/20242_efb63db/image/300x300'),
(276, 'Expert V-Brake 24V dame 2015', 0, 0, 9, 22.98, 'afbeeldingen/Thompson_Expert_V-Brake_24V_dame_2015', '/20239_efb63db/image/300x300'),
(277, 'Expert V-Brake 24V heer 2015', 0, 0, 9, 22.98, 'afbeeldingen/Thompson_Expert_V-Brake_24V_heer_2015', '/20240_efb63db/image/300x300'),
(278, 'Garda -S Alivio 24V dame 2015', 0, 0, 9, 25.44, 'afbeeldingen/Thompson_Garda_-S_Alivio_24V_dame_2015', '/20243_efb63db/image/300x300'),
(279, 'Garda -S Alivio 24V heer 2015', 0, 0, 9, 25.44, 'afbeeldingen/Thompson_Garda_-S_Alivio_24V_heer_2015', '/20244_efb63db/image/300x300'),
(280, 'Garda -S Deore 27V dame 2015', 0, 0, 9, 29.92, 'afbeeldingen/Thompson_Garda_-S_Deore_27V_dame_2015', '/20245_efb63db/image/300x300'),
(281, 'Garda -S Deore 27V heer 2015', 0, 0, 9, 29.92, 'afbeeldingen/Thompson_Garda_-S_Deore_27V_heer_2015', '/20246_efb63db/image/300x300'),
(282, 'Garda -S Full LX 30V dame 2015', 0, 0, 9, 34.52, 'afbeeldingen/Thompson_Garda_-S_Full_LX_30V_dame_2015', '/20247_efb63db/image/300x300'),
(283, 'Garda -S Full LX 30V heer 2015', 0, 0, 9, 34.52, 'afbeeldingen/Thompson_Garda_-S_Full_LX_30V_heer_2015', '/20248_efb63db/image/300x300'),
(284, 'Garda Cross 27V dame 2015', 0, 0, 9, 24.09, 'afbeeldingen/Thompson_Garda_Cross_27V_dame_2015', '/20237_efb63db/image/300x300'),
(285, 'Garda Cross 27V heer 2015', 0, 0, 9, 24.09, 'afbeeldingen/Thompson_Garda_Cross_27V_heer_2015', '/20238_efb63db/image/300x300'),
(286, 'S8200 Urban 27V dame 2015', 0, 0, 9, 30.53, 'afbeeldingen/Thompson_S8200_Urban_27V_dame_2015', '/20249_efb63db/image/300x300'),
(287, 'S8200 Urban 27V heer 2015', 0, 0, 9, 30.53, 'afbeeldingen/Thompson_S8200_Urban_27V_heer_2015', '/20250_efb63db/image/300x300'),
(288, 'Sport S6200 Equipped 27V dame 2015', 0, 0, 9, 28.38, 'afbeeldingen/Thompson_Sport_S6200_Equipped_27V_dame_2015', '/20251_efb63db/image/300x300'),
(289, 'Sport S6200 Equipped 27V heer 2015', 0, 0, 9, 28.38, 'afbeeldingen/Thompson_Sport_S6200_Equipped_27V_heer_2015', '/20252_efb63db/image/300x300'),
(290, 'Sport S7200 Equipped 27V dame 2015', 0, 0, 9, 30.53, 'afbeeldingen/Thompson_Sport_S7200_Equipped_27V_dame_2015', '/20253_efb63db/image/300x300'),
(291, 'Sport S7200 Equipped 27V heer 2015', 0, 0, 9, 30.53, 'afbeeldingen/Thompson_Sport_S7200_Equipped_27V_heer_2015', '/20254_efb63db/image/300x300'),
(292, 'Sport S8200 Equipped 30V dame 2015', 0, 0, 9, 36.67, 'afbeeldingen/Thompson_Sport_S8200_Equipped_30V_dame_2015', '/20255_efb63db/image/300x300'),
(293, 'Sport S8200 Equipped 30V heer 2015', 0, 0, 9, 36.67, 'afbeeldingen/Thompson_Sport_S8200_Equipped_30V_heer_2015', '/20256_efb63db/image/300x300'),
(294, 'Sport S8200 Equipped Disc 30V dame 2015', 0, 0, 9, 38.35, 'afbeeldingen/Thompson_Sport_S8200_Equipped_Disc_30V_dame_2015', '/20259_efb63db/image/300x300'),
(295, 'Sport S8200 Equipped Disc 30V heer 2015', 0, 0, 9, 38.35, 'afbeeldingen/Thompson_Sport_S8200_Equipped_Disc_30V_heer_2015', '/20260_efb63db/image/300x300'),
(296, 'Sport S8200 Equipped LX 30V dame 2015', 0, 0, 9, 39.86, 'afbeeldingen/Thompson_Sport_S8200_Equipped_LX_30V_dame_2015', '/20257_efb63db/image/300x300'),
(297, 'Sport S8200 Equipped LX 30V heer 2015', 0, 0, 9, 39.86, 'afbeeldingen/Thompson_Sport_S8200_Equipped_LX_30V_heer_2015', '/20258_efb63db/image/300x300'),
(298, 'Voltage Alfine Di2 Bosch Active Line 400W 10V dame 2015', 0, 0, 9, 90.96, 'afbeeldingen/Thompson_Voltage_Alfine_Di2_Bosch_Active_Line_400W_10V_dame_2015', '/20236_efb63db/image/300x300'),
(299, 'Voltage Alfine Di2 Bosch Active Line 400W 10V heer 2015', 0, 0, 9, 90.96, 'afbeeldingen/Thompson_Voltage_Alfine_Di2_Bosch_Active_Line_400W_10V_heer_2015', '/20235_efb63db/image/300x300'),
(300, 'Voltage Inter 8 Bosch Active Line 400W 10V dame 2015', 0, 0, 9, 81.76, 'afbeeldingen/Thompson_Voltage_Inter_8_Bosch_Active_Line_400W_10V_dame_2015', '/20234_efb63db/image/300x300'),
(301, 'Voltage Inter 8 Bosch Active Line 400W 10V heer 2015', 0, 0, 9, 81.76, 'afbeeldingen/Thompson_Voltage_Inter_8_Bosch_Active_Line_400W_10V_heer_2015', '/20233_efb63db/image/300x300'),
(302, 'Family Bosch Active 400Wh rollerbrakes 2017', 0, 0, 10, 122.87, 'afbeeldingen/Urban_Arrow_Family_Bosch_Active_400Wh_rollerbrakes_2017', '/34378_94c039d/image/300x300'),
(303, 'Family Bosch Performance 400Wh disk brakes 2017', 0, 0, 10, 132.08, 'afbeeldingen/Urban_Arrow_Family_Bosch_Performance_400Wh_disk_brakes_2017', '/34379_94c039d/image/300x300'),
(304, 'Family Bosch Performance CX 500Wh disk brakes 2017', 0, 0, 10, 150.49, 'afbeeldingen/Urban_Arrow_Family_Bosch_Performance_CX_500Wh_disk_brakes_2017', '/34380_94c039d/image/300x300'),
(305, 'e-Manufaktur 10.7 400Wh uni 10V 2016', 0, 0, 11, 107.81, 'afbeeldingen/Victoria_e-Manufaktur_10.7_400Wh_uni_10V_2016', '/26359_efb63db/image/300x300'),
(306, 'e-Manufaktur 10.7 400Wh wave 10V 2016', 0, 0, 11, 107.81, 'afbeeldingen/Victoria_e-Manufaktur_10.7_400Wh_wave_10V_2016', '/26360_efb63db/image/300x300'),
(307, 'e-Spezial 10.6 400Wh heer 10V 2016', 0, 0, 11, 98.6, 'afbeeldingen/Victoria_e-Spezial_10.6_400Wh_heer_10V_2016', '/26351_efb63db/image/300x300'),
(308, 'e-Spezial 10.7 400Wh heer 10V 2016', 0, 0, 11, 107.81, 'afbeeldingen/Victoria_e-Spezial_10.7_400Wh_heer_10V_2016', '/26352_efb63db/image/300x300'),
(309, 'e-Spezial 10.7 400Wh trapeze 10V 2016', 0, 0, 11, 107.81, 'afbeeldingen/Victoria_e-Spezial_10.7_400Wh_trapeze_10V_2016', '/26353_efb63db/image/300x300'),
(310, 'e-Trekking 7.8 400Wh heren Nuvinci 2016', 0, 0, 11, 80.19, 'afbeeldingen/Victoria_e-Trekking_7.8_400Wh_heren_Nuvinci_2016', '/26354_efb63db/image/300x300'),
(311, 'e-Trekking 7.8 400Wh trapeze Nuvinci 2016', 0, 0, 11, 80.19, 'afbeeldingen/Victoria_e-Trekking_7.8_400Wh_trapeze_Nuvinci_2016', '/26356_efb63db/image/300x300'),
(312, 'e-Trekking 7.8 400Wh wave Nuvinci 2016', 0, 0, 11, 80.19, 'afbeeldingen/Victoria_e-Trekking_7.8_400Wh_wave_Nuvinci_2016', '/26355_efb63db/image/300x300'),
(313, 'e-Trekking 8.9 400Wh heren 11V 2016', 0, 0, 11, 92.46, 'afbeeldingen/Victoria_e-Trekking_8.9_400Wh_heren_11V_2016', '/26357_efb63db/image/300x300'),
(314, 'e-Trekking 8.9 400Wh trapeze 11V 2016', 0, 0, 11, 92.46, 'afbeeldingen/Victoria_e-Trekking_8.9_400Wh_trapeze_11V_2016', '/26358_efb63db/image/300x300');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `api_bikebrand`
--

CREATE TABLE `api_bikebrand` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `api_bikebrand`
--

INSERT INTO `api_bikebrand` (`id`, `name`) VALUES
(1, 'Batavus'),
(2, 'Bizobike'),
(3, 'Conway'),
(4, 'E-Twow'),
(5, 'Giant'),
(6, 'Gocycle'),
(7, 'Jools'),
(8, 'Ridley'),
(9, 'Thompson'),
(10, 'Urban Arrow'),
(11, 'Victoria');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `api_calculationparameter`
--

CREATE TABLE `api_calculationparameter` (
  `id` int(11) NOT NULL,
  `rsz` double NOT NULL,
  `co2_gasoline` int(11) NOT NULL,
  `co2_diesel` int(11) NOT NULL,
  `tax_decrease_multiplier_werkbonus` double NOT NULL,
  `arbeider_rsz_multiplier` double NOT NULL,
  `bediende_rsz_multiplier` double NOT NULL,
  `bijzondere_bijdrage_sz_high_boundary` double NOT NULL,
  `bijzondere_bijdrage_sz_high_cat_max_value` double NOT NULL,
  `bijzondere_bijdrage_sz_highest_cat_scale1` double NOT NULL,
  `bijzondere_bijdrage_sz_lowest_boundary` double NOT NULL,
  `bijzondere_bijdrage_sz_lowest_boundary_np` double NOT NULL,
  `bijzondere_bijdrage_sz_married_and_income` double NOT NULL,
  `bijzondere_bijdrage_sz_middle_boundary` double NOT NULL,
  `bijzondere_bijdrage_sz_middle_cat_max_value` double NOT NULL,
  `bijzondere_bijdrage_sz_middle_cat_min_value` double NOT NULL,
  `bijzondere_bijdrage_sz_multiplier_high_cat` double NOT NULL,
  `bijzondere_bijdrage_sz_multiplier_middle_cat` double NOT NULL,
  `high_income_base_tax_scale1` double NOT NULL,
  `high_income_base_tax_scale2` double NOT NULL,
  `high_income_boundary` int(11) NOT NULL,
  `high_income_multiplier_of_diff` double NOT NULL,
  `high_income_rent_boundary` int(11) NOT NULL,
  `low_income_boundary` double NOT NULL,
  `pension_rent_multiplier` double NOT NULL,
  `tax_decrease_child1` int(11) NOT NULL,
  `tax_decrease_child2` int(11) NOT NULL,
  `tax_decrease_child3` int(11) NOT NULL,
  `tax_decrease_child4` int(11) NOT NULL,
  `tax_decrease_child5` int(11) NOT NULL,
  `tax_decrease_child6` int(11) NOT NULL,
  `tax_decrease_child7` int(11) NOT NULL,
  `tax_decrease_child8` int(11) NOT NULL,
  `tax_decrease_child8plus_multiplier` int(11) NOT NULL,
  `tax_decrease_family_member` int(11) NOT NULL,
  `tax_decrease_handicapped` int(11) NOT NULL,
  `tax_decrease_low_income` double NOT NULL,
  `tax_decrease_married_partner_low_income` int(11) NOT NULL,
  `tax_decrease_married_partner_low_rent` int(11) NOT NULL,
  `tax_decrease_old_family_member` int(11) NOT NULL,
  `tax_decrease_single` int(11) NOT NULL,
  `tax_decrease_widow_or_unmarried_with_children` int(11) NOT NULL,
  `tax_decrease_work_bonus_arbeider_lowest` double NOT NULL,
  `tax_decrease_work_bonus_arbeider_multiplier_diff` double NOT NULL,
  `tax_decrease_work_bonus_bediende_lowest` double NOT NULL,
  `tax_decrease_work_bonus_bediende_multiplier_diff` double NOT NULL,
  `work_bonus_highest_boundary` double NOT NULL,
  `work_bonus_lowest_boundary` double NOT NULL,
  `max_vaa_car` int(11) NOT NULL,
  `woon_werkverkeer_auto` double NOT NULL,
  `woon_werkverkeer_auto_belast_vrij` int(11) NOT NULL,
  `woon_werkverkeer_fiets` double NOT NULL,
  `percentage_prive_usage_bike` double NOT NULL,
  `hospitalisation_partner` int(11) NOT NULL,
  `hospitalisation_child` int(11) NOT NULL,
  `vaa_smartphone` double NOT NULL,
  `vaa_laptop` int(11) NOT NULL,
  `vaa_internet` int(11) NOT NULL,
  `tech_budget` int(11) NOT NULL,
  `car_cat1_lease` double NOT NULL,
  `car_cat2_lease` double NOT NULL,
  `car_cat3_lease` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `api_calculationparameter`
--

INSERT INTO `api_calculationparameter` (`id`, `rsz`, `co2_gasoline`, `co2_diesel`, `tax_decrease_multiplier_werkbonus`, `arbeider_rsz_multiplier`, `bediende_rsz_multiplier`, `bijzondere_bijdrage_sz_high_boundary`, `bijzondere_bijdrage_sz_high_cat_max_value`, `bijzondere_bijdrage_sz_highest_cat_scale1`, `bijzondere_bijdrage_sz_lowest_boundary`, `bijzondere_bijdrage_sz_lowest_boundary_np`, `bijzondere_bijdrage_sz_married_and_income`, `bijzondere_bijdrage_sz_middle_boundary`, `bijzondere_bijdrage_sz_middle_cat_max_value`, `bijzondere_bijdrage_sz_middle_cat_min_value`, `bijzondere_bijdrage_sz_multiplier_high_cat`, `bijzondere_bijdrage_sz_multiplier_middle_cat`, `high_income_base_tax_scale1`, `high_income_base_tax_scale2`, `high_income_boundary`, `high_income_multiplier_of_diff`, `high_income_rent_boundary`, `low_income_boundary`, `pension_rent_multiplier`, `tax_decrease_child1`, `tax_decrease_child2`, `tax_decrease_child3`, `tax_decrease_child4`, `tax_decrease_child5`, `tax_decrease_child6`, `tax_decrease_child7`, `tax_decrease_child8`, `tax_decrease_child8plus_multiplier`, `tax_decrease_family_member`, `tax_decrease_handicapped`, `tax_decrease_low_income`, `tax_decrease_married_partner_low_income`, `tax_decrease_married_partner_low_rent`, `tax_decrease_old_family_member`, `tax_decrease_single`, `tax_decrease_widow_or_unmarried_with_children`, `tax_decrease_work_bonus_arbeider_lowest`, `tax_decrease_work_bonus_arbeider_multiplier_diff`, `tax_decrease_work_bonus_bediende_lowest`, `tax_decrease_work_bonus_bediende_multiplier_diff`, `work_bonus_highest_boundary`, `work_bonus_lowest_boundary`, `max_vaa_car`, `woon_werkverkeer_auto`, `woon_werkverkeer_auto_belast_vrij`, `woon_werkverkeer_fiets`, `percentage_prive_usage_bike`, `hospitalisation_partner`, `hospitalisation_child`, `vaa_smartphone`, `vaa_laptop`, `vaa_internet`, `tech_budget`, `car_cat1_lease`, `car_cat2_lease`, `car_cat3_lease`) VALUES
(2016, 0.1307, 107, 89, 0.2803, 1.08, 1, 6038.83, 51.64, 60.94, 1945.38, 1095.1, 9.3, 2190.18, 18.6, 9.3, 0.011, 0.076, 3287.26, 2922.79, 7500, 0.535, 130, 2370.74, 0.2, 34, 93, 248, 454, 671, 887, 1104, 1337, 241, 34, 34, 6.46, 108, 216, 70, 24, 34, 209.29, 0.2369, 193.79, 0.2194, 2461.27, 1577.89, 1260, 0.3412, 380, 0.22, 0.2, 175, 68, 12.5, 15, 5, 400, 435, 485, 585);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `api_car`
--

CREATE TABLE `api_car` (
  `id` int(11) NOT NULL,
  `model` varchar(100) NOT NULL,
  `engine_type` varchar(20) NOT NULL,
  `lease_price` double NOT NULL,
  `co2` int(11) NOT NULL,
  `catalog_value` double NOT NULL,
  `registration_year` date NOT NULL,
  `image_url` varchar(200) NOT NULL,
  `brand_id` int(11) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `api_car`
--

INSERT INTO `api_car` (`id`, `model`, `engine_type`, `lease_price`, `co2`, `catalog_value`, `registration_year`, `image_url`, `brand_id`, `category_id`) VALUES
(1, 'A1', 'benzine', 435, 97, 16850, '2017-02-06', 'audi_a1.png', 1, 1),
(2, 'A1', 'diesel', 435, 94, 19300, '2017-02-06', 'audi_a1.png', 1, 1),
(3, 'A3', 'benzine', 485, 104, 22750, '2017-02-06', 'audi_a3.png', 1, 2),
(4, 'A3', 'diesel', 485, 106, 24290, '2017-02-06', 'audi_a3.png', 1, 2),
(5, 'A4', 'benzine', 585, 123, 30675, '2017-02-06', 'audi_a4.png', 1, 3),
(6, 'A4', 'diesel', 585, 99, 33560, '2017-02-06', 'audi_a4.png', 1, 3),
(7, 'Polo 3d', 'diesel', 435, 95, 18750, '2017-02-06', 'volkswagen_polo_3d.png', 2, 1),
(8, 'Polo 3d', 'benzine', 435, 114, 14390, '2017-02-06', 'volkswagen_polo_3d.png', 2, 1),
(9, 'Polo 5d', 'diesel', 435, 95, 19542, '2017-02-06', 'volkswagen_polo.png', 2, 1),
(10, 'Polo 5d', 'benzine', 435, 114, 14926, '2017-02-06', 'volkswagen_polo.png', 2, 1),
(11, 'Golf Variant', 'diesel', 485, 106, 25280, '2017-02-06', 'volkswagen_golf_variant.png', 2, 2),
(12, 'Golf Variant', 'benzine', 485, 112, 24160, '2017-02-06', 'volkswagen_golf_variant.png', 2, 2),
(13, 'Touran', 'diesel', 585, 112, 31300, '2017-02-06', 'volkswagen_touran.png', 2, 3),
(14, 'Touran', 'benzine', 585, 128, 27300, '2017-02-06', 'volkswagen_touran.png', 2, 3),
(15, 'Passat', 'diesel', 585, 105, 30000, '2017-02-06', 'volkswagen_passat.png', 2, 3),
(16, 'Passat', 'benzine', 585, 115, 30200, '2017-02-06', 'volkswagen_passat.png', 2, 3),
(17, 'Passat Variant', 'diesel', 585, 107, 31920, '2017-02-06', 'volkswagen_passat_variant.png', 2, 3),
(18, 'Passat Variant', 'benzine', 585, 119, 32140, '2017-02-06', 'volkswagen_passat_variant.png\r\n', 2, 3),
(19, 'Fabia 5d', 'diesel', 435, 93, 16255, '2017-02-06', 'skoda_fabia.png', 3, 1),
(20, 'Fabia 5d', 'benzine', 435, 106, 12985, '2017-02-06', 'skoda_fabia.png', 3, 1),
(21, 'Fabia Combi', 'diesel', 435, 94, 16865, '2017-02-06', 'skoda_fabia_combi.png', 3, 1),
(22, 'Fabia Combi', 'benzine', 435, 109, 14415, '2017-02-06', 'skoda_fabia_combi.png', 3, 1),
(23, 'Octavia', 'diesel', 485, 106, 22630, '2017-02-06', 'skoda_octavia.png', 3, 2),
(24, 'Octavia', 'benzine', 485, 108, 24455, '2017-02-06', 'skoda_octavia.png', 3, 2),
(25, 'Octavia Combi', 'benzine', 485, 108, 25280, '2017-02-06', 'skoda_octavia_combi.png', 3, 2),
(26, 'Octavia Combi', 'diesel', 485, 106, 23455, '2017-02-06', 'skoda_octavia_combi.png', 3, 2),
(29, 'Superb 5d', 'diesel', 585, 108, 27545, '2017-02-06', 'skoda_superb.png', 3, 3),
(30, 'Superb 5d', 'benzine', 585, 128, 32135, '2017-02-06', 'skoda_superb.png', 3, 3),
(31, 'Superb combi', 'diesel', 585, 109, 28665, '2017-02-06', 'skoda_superb_combi.png', 3, 3),
(32, 'Superb combi', 'benzine', 585, 126, 28005, '2017-02-06', 'skoda_superb_combi.png', 3, 3);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `api_carbrand`
--

CREATE TABLE `api_carbrand` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `api_carbrand`
--

INSERT INTO `api_carbrand` (`id`, `name`) VALUES
(1, 'Audi'),
(2, 'Volkswagen'),
(3, 'Skoda');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `api_carcategory`
--

CREATE TABLE `api_carcategory` (
  `id` int(11) NOT NULL,
  `name` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `api_carcategory`
--

INSERT INTO `api_carcategory` (`id`, `name`) VALUES
(1, 1),
(2, 2),
(3, 3);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `api_taxscale`
--

CREATE TABLE `api_taxscale` (
  `id` int(11) NOT NULL,
  `bruto` int(11) NOT NULL,
  `scale1` float NOT NULL,
  `scale2` float NOT NULL,
  `year` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `api_taxscale`
--

INSERT INTO `api_taxscale` (`id`, `bruto`, `scale1`, `scale2`, `year`) VALUES
(1, 525, 0, 0, 2016),
(2, 540, 0, 0, 2016),
(3, 555, 0, 0, 2016),
(4, 570, 0, 0, 2016),
(5, 585, 0, 0, 2016),
(6, 600, 0, 0, 2016),
(7, 615, 0, 0, 2016),
(8, 630, 0, 0, 2016),
(9, 645, 0, 0, 2016),
(10, 660, 0, 0, 2016),
(11, 675, 0, 0, 2016),
(12, 690, 0, 0, 2016),
(13, 705, 0, 0, 2016),
(14, 720, 0.53, 0, 2016),
(15, 735, 4.1, 0, 2016),
(16, 750, 7.67, 0, 2016),
(17, 765, 11.25, 0, 2016),
(18, 780, 14.82, 0, 2016),
(19, 795, 18.39, 0, 2016),
(20, 810, 21.96, 0, 2016),
(21, 825, 25.53, 0, 2016),
(22, 840, 29.1, 0, 2016),
(23, 855, 32.67, 0, 2016),
(24, 870, 36.24, 0, 2016),
(25, 885, 39.82, 0, 2016),
(26, 900, 43.39, 0, 2016),
(27, 915, 46.96, 0, 2016),
(28, 930, 50.53, 0, 2016),
(29, 945, 54.1, 0, 2016),
(30, 960, 57.67, 0, 2016),
(31, 975, 61.24, 0, 2016),
(32, 990, 64.81, 0, 2016),
(33, 1005, 68.38, 0, 2016),
(34, 1020, 71.96, 0, 2016),
(35, 1035, 75.53, 0, 2016),
(36, 1050, 79.1, 0, 2016),
(37, 1065, 82.67, 0, 2016),
(38, 1080, 86.24, 0, 2016),
(39, 1095, 89.81, 0, 2016),
(40, 1110, 93.38, 0, 2016),
(41, 1125, 96.95, 0, 2016),
(42, 1140, 100.52, 0, 2016),
(43, 1155, 104.1, 0, 2016),
(44, 1170, 107.85, 0, 2016),
(45, 1185, 112.13, 0, 2016),
(46, 1200, 116.42, 0, 2016),
(47, 1215, 120.7, 0, 2016),
(48, 1230, 124.99, 0, 2016),
(49, 1245, 129.27, 0, 2016),
(50, 1260, 133.56, 0, 2016),
(51, 1275, 138.84, 0, 2016),
(52, 1290, 144.55, 1.15, 2016),
(53, 1305, 150.26, 4.72, 2016),
(54, 1320, 155.98, 8.29, 2016),
(55, 1335, 161.69, 11.86, 2016),
(56, 1350, 167.41, 15.43, 2016),
(57, 1365, 173.12, 19, 2016),
(58, 1380, 178.83, 22.58, 2016),
(59, 1395, 184.55, 26.15, 2016),
(60, 1410, 190.26, 29.72, 2016),
(61, 1425, 195.98, 33.29, 2016),
(62, 1440, 201.69, 36.86, 2016),
(63, 1455, 207.4, 40.43, 2016),
(64, 1470, 213.12, 44, 2016),
(65, 1485, 218.83, 47.57, 2016),
(66, 1500, 224.54, 51.14, 2016),
(67, 1515, 230.26, 54.71, 2016),
(68, 1530, 235.97, 58.29, 2016),
(69, 1545, 241.69, 61.86, 2016),
(70, 1560, 247.4, 65.43, 2016),
(71, 1575, 253.11, 69, 2016),
(72, 1590, 258.33, 72.57, 2016),
(73, 1605, 264.54, 76.25, 2016),
(74, 1620, 270.25, 80.32, 2016),
(75, 1635, 275.97, 84.4, 2016),
(76, 1650, 281.68, 88.47, 2016),
(77, 1665, 287.45, 92.58, 2016),
(78, 1680, 293.68, 97.02, 2016),
(79, 1695, 299.91, 101.45, 2016),
(80, 1710, 306.14, 105.89, 2016),
(81, 1725, 312.36, 110.33, 2016),
(82, 1740, 318.59, 115.08, 2016),
(83, 1755, 324.82, 120.61, 2016),
(84, 1770, 331.76, 126.14, 2016),
(85, 1785, 338.77, 131.66, 2016),
(86, 1800, 345.77, 137.19, 2016),
(87, 1815, 352.78, 142.72, 2016),
(88, 1830, 359.78, 148.25, 2016),
(89, 1845, 366.79, 153.77, 2016),
(90, 1860, 373.8, 159.3, 2016),
(91, 1875, 380.8, 164.83, 2016),
(92, 1890, 387.81, 170.35, 2016),
(93, 1905, 394.81, 175.88, 2016),
(94, 1920, 401.82, 181.41, 2016),
(95, 1935, 408.82, 186.93, 2016),
(96, 1950, 415.83, 192.46, 2016),
(97, 1965, 422.84, 197.99, 2016),
(98, 1980, 429.84, 203.51, 2016),
(99, 1995, 436.85, 209.04, 2016),
(100, 2010, 443.85, 214.57, 2016),
(101, 2025, 450.86, 220.09, 2016),
(102, 2040, 457.87, 225.62, 2016),
(103, 2055, 464.87, 231.15, 2016),
(104, 2070, 471.88, 236.67, 2016),
(105, 2085, 478.88, 242.2, 2016),
(106, 2100, 485.89, 247.73, 2016),
(107, 2115, 492.89, 253.25, 2016),
(108, 2130, 499.9, 258.78, 2016),
(109, 2145, 506.91, 264.31, 2016),
(110, 2160, 513.91, 269.83, 2016),
(111, 2175, 520.92, 275.36, 2016),
(112, 2190, 527.92, 280.89, 2016),
(113, 2205, 534.93, 286.42, 2016),
(114, 2220, 541.94, 291.94, 2016),
(115, 2235, 548.94, 297.47, 2016),
(116, 2250, 555.95, 303, 2016),
(117, 2265, 562.95, 308.52, 2016),
(118, 2280, 569.96, 314.05, 2016),
(119, 2295, 576.96, 319.58, 2016),
(120, 2310, 583.97, 325.1, 2016),
(121, 2325, 590.98, 330.63, 2016),
(122, 2340, 597.98, 336.16, 2016),
(123, 2355, 604.99, 341.68, 2016),
(124, 2370, 611.99, 347.21, 2016),
(125, 2385, 619, 352.74, 2016),
(126, 2400, 626.01, 358.59, 2016),
(127, 2415, 633.01, 364.66, 2016),
(128, 2430, 640.02, 370.74, 2016),
(129, 2445, 647.02, 376.81, 2016),
(130, 2460, 654.03, 382.88, 2016),
(131, 2475, 661.03, 388.95, 2016),
(132, 2490, 668.04, 395.02, 2016),
(133, 2505, 675.05, 401.09, 2016),
(134, 2520, 682.05, 407.17, 2016),
(135, 2535, 689.06, 413.24, 2016),
(136, 2550, 696.06, 419.31, 2016),
(137, 2565, 703.07, 425.38, 2016),
(138, 2580, 710.08, 431.45, 2016),
(139, 2595, 717.08, 437.52, 2016),
(140, 2610, 724.09, 443.6, 2016),
(141, 2625, 731.09, 449.67, 2016),
(142, 2640, 738.1, 455.74, 2016),
(143, 2655, 745.1, 461.81, 2016),
(144, 2670, 752.11, 467.88, 2016),
(145, 2685, 759.12, 473.95, 2016),
(146, 2700, 766.12, 480.03, 2016),
(147, 2715, 773.13, 486.1, 2016),
(148, 2730, 780.13, 492.17, 2016),
(149, 2745, 787.14, 498.24, 2016),
(150, 2760, 794.14, 504.31, 2016),
(151, 2775, 801.15, 510.39, 2016),
(152, 2790, 808.16, 516.46, 2016),
(153, 2805, 815.16, 522.53, 2016),
(154, 2820, 822.17, 528.6, 2016),
(155, 2835, 829.17, 534.67, 2016),
(156, 2850, 836.18, 540.74, 2016),
(157, 2865, 843.19, 546.82, 2016),
(158, 2880, 850.19, 552.89, 2016),
(159, 2895, 857.38, 559.12, 2016),
(160, 2910, 864.6, 565.37, 2016),
(161, 2925, 871.82, 571.63, 2016),
(162, 2940, 879.05, 577.89, 2016),
(163, 2955, 886.27, 584.15, 2016),
(164, 2970, 893.49, 590.41, 2016),
(165, 2985, 900.71, 596.67, 2016),
(166, 3000, 907.94, 602.93, 2016),
(167, 3015, 915.16, 609.19, 2016),
(168, 3030, 922.38, 615.45, 2016),
(169, 3045, 929.6, 621.71, 2016),
(170, 3060, 936.83, 627.97, 2016),
(171, 3075, 944.05, 634.23, 2016),
(172, 3090, 951.27, 640.49, 2016),
(173, 3105, 958.49, 646.75, 2016),
(174, 3120, 965.78, 653.01, 2016),
(175, 3135, 972.94, 659.27, 2016),
(176, 3150, 980.16, 665.53, 2016),
(177, 3165, 987.38, 671.79, 2016),
(178, 3180, 994.61, 678.05, 2016),
(179, 3195, 1001.83, 684.31, 2016),
(180, 3210, 1009.05, 690.56, 2016),
(181, 3225, 1016.27, 697.68, 2016),
(182, 3240, 1023.5, 704.9, 2016),
(183, 3255, 1030.72, 712.13, 2016),
(184, 3270, 1037.94, 719.35, 2016),
(185, 3285, 1045.16, 726.57, 2016),
(186, 3300, 1052.39, 733.79, 2016),
(187, 3315, 1059.61, 741.02, 2016),
(188, 3330, 1066.83, 748.24, 2016),
(189, 3345, 1074.05, 755.46, 2016),
(190, 3360, 1081.28, 762.68, 2016),
(191, 3375, 1088.5, 769.91, 2016),
(192, 3390, 1095.72, 777.13, 2016),
(193, 3405, 1102.94, 784.35, 2016),
(194, 3420, 1110.17, 791.57, 2016),
(195, 3435, 1117.39, 798.8, 2016),
(196, 3450, 1124.61, 806.02, 2016),
(197, 3465, 1131.83, 813.24, 2016),
(198, 3480, 1139.06, 820.46, 2016),
(199, 3495, 1146.28, 827.69, 2016),
(200, 3510, 1153.5, 834.91, 2016),
(201, 3525, 1160.72, 842.13, 2016),
(202, 3540, 1168.66, 849.35, 2016),
(203, 3555, 1176.68, 856.58, 2016),
(204, 3570, 1184.71, 863.8, 2016),
(205, 3585, 1192.73, 871.02, 2016),
(206, 3600, 1200.76, 878.24, 2016),
(207, 3615, 1208.78, 885.47, 2016),
(208, 3630, 1216.81, 892.69, 2016),
(209, 3645, 1224.83, 899.91, 2016),
(210, 3660, 1232.86, 907.13, 2016),
(211, 3675, 1240.88, 914.36, 2016),
(212, 3690, 1248.91, 921.58, 2016),
(213, 3705, 1256.93, 928.8, 2016),
(214, 3720, 1264.96, 936.02, 2016),
(215, 3735, 1272.98, 943.25, 2016),
(216, 3750, 1281.01, 950.47, 2016),
(217, 3765, 1289.03, 957.69, 2016),
(218, 3780, 1297.06, 964.91, 2016),
(219, 3795, 1305.08, 972.14, 2016),
(220, 3810, 1313.11, 979.36, 2016),
(221, 3825, 1321.13, 986.58, 2016),
(222, 3840, 1329.16, 993.8, 2016),
(223, 3855, 1337.18, 1001.03, 2016),
(224, 3870, 1345.21, 1008.25, 2016),
(225, 3885, 1353.23, 1015.47, 2016),
(226, 3900, 1361.26, 1022.69, 2016),
(227, 3915, 1369.28, 1029.92, 2016),
(228, 3930, 1377.31, 1037.14, 2016),
(229, 3945, 1385.33, 1044.36, 2016),
(230, 3960, 1393.36, 1051.58, 2016),
(231, 3975, 1401.38, 1058.81, 2016),
(232, 3990, 1409.41, 1066.03, 2016),
(233, 4005, 1417.43, 1073.25, 2016),
(234, 4020, 1425.46, 1080.47, 2016),
(235, 4035, 1433.48, 1087.7, 2016),
(236, 4050, 1441.51, 1094.92, 2016),
(237, 4065, 1449.53, 1102.14, 2016),
(238, 4080, 1457.56, 1109.36, 2016),
(239, 4095, 1465.58, 1116.59, 2016),
(240, 4110, 1473.61, 1123.81, 2016),
(241, 4125, 1481.63, 1131.03, 2016),
(242, 4140, 1489.66, 1138.25, 2016),
(243, 4155, 1497.68, 1145.48, 2016),
(244, 4170, 1505.71, 1152.7, 2016),
(245, 4185, 1513.73, 1159.92, 2016),
(246, 4200, 1521.76, 1167.14, 2016),
(247, 4215, 1529.78, 1174.37, 2016),
(248, 4230, 1537.81, 1181.59, 2016),
(249, 4245, 1545.83, 1188.81, 2016),
(250, 4260, 1553.86, 1196.03, 2016),
(251, 4275, 1561.88, 1203.26, 2016),
(252, 4290, 1569.91, 1210.48, 2016),
(253, 4305, 1577.93, 1217.7, 2016),
(254, 4320, 1585.96, 1224.92, 2016),
(255, 4335, 1593.98, 1232.15, 2016),
(256, 4350, 1602.01, 1239.37, 2016),
(257, 4365, 1610.03, 1246.59, 2016),
(258, 4380, 1618.06, 1253.81, 2016),
(259, 4395, 1626.08, 1261.62, 2016),
(260, 4410, 1634.11, 1269.64, 2016),
(261, 4425, 1642.13, 1277.67, 2016),
(262, 4440, 1650.16, 1285.69, 2016),
(263, 4455, 1658.18, 1293.72, 2016),
(264, 4470, 1666.21, 1301.74, 2016),
(265, 4485, 1674.23, 1309.77, 2016),
(266, 4500, 1682.26, 1317.79, 2016),
(267, 4515, 1690.28, 1325.82, 2016),
(268, 4530, 1698.31, 1333.84, 2016),
(269, 4545, 1706.33, 1341.87, 2016),
(270, 4560, 1714.36, 1349.89, 2016),
(271, 4575, 1722.38, 1357.92, 2016),
(272, 4590, 1730.41, 1365.94, 2016),
(273, 4605, 1738.43, 1373.97, 2016),
(274, 4620, 1746.46, 1381.99, 2016),
(275, 4635, 1754.48, 1390.02, 2016),
(276, 4650, 1762.51, 1398.04, 2016),
(277, 4665, 1770.53, 1406.07, 2016),
(278, 4680, 1778.56, 1414.09, 2016),
(279, 4695, 1786.58, 1422.12, 2016),
(280, 4710, 1794.61, 1430.14, 2016),
(281, 4725, 1802.63, 1438.17, 2016),
(282, 4740, 1810.66, 1446.19, 2016),
(283, 4755, 1818.68, 1454.22, 2016),
(284, 4770, 1826.71, 1462.24, 2016),
(285, 4785, 1834.73, 1470.27, 2016),
(286, 4800, 1842.76, 1478.29, 2016),
(287, 4815, 1850.78, 1486.32, 2016),
(288, 4830, 1858.81, 1494.34, 2016),
(289, 4845, 1866.83, 1502.37, 2016),
(290, 4860, 1874.86, 1510.39, 2016),
(291, 4875, 1882.88, 1518.42, 2016),
(292, 4890, 1890.91, 1526.45, 2016),
(293, 44905, 1898.93, 1534.47, 2016),
(294, 4920, 1906.96, 1542.49, 2016),
(295, 4935, 1914.98, 1550.52, 2016),
(296, 4950, 1923.01, 1558.54, 2016),
(297, 4965, 1931.03, 1566.57, 2016),
(298, 4980, 1939.06, 1574.59, 2016),
(299, 4995, 1947.08, 1582.62, 2016),
(300, 5010, 1955.11, 1590.64, 2016),
(301, 5025, 1963.13, 1598.67, 2016),
(302, 5040, 1971.16, 1606.69, 2016),
(303, 5055, 1979.18, 1614.72, 2016),
(304, 5070, 1987.21, 1622.74, 2016),
(305, 5085, 1995.23, 1630.77, 2016),
(306, 5100, 2003.26, 1638.79, 2016),
(307, 5115, 2011.28, 1646.82, 2016),
(308, 5130, 2019.31, 1654.84, 2016),
(309, 5145, 2027.33, 1662.87, 2016),
(310, 5160, 2035.36, 1670.89, 2016),
(311, 5175, 2043.38, 1678.92, 2016),
(312, 5190, 2051.41, 1686.94, 2016),
(313, 5205, 2059.43, 1694.97, 2016),
(314, 5220, 2067.46, 1702.99, 2016),
(315, 5235, 2075.48, 1711.02, 2016),
(316, 5250, 2083.51, 1719.04, 2016),
(317, 5265, 2091.53, 1727.07, 2016),
(318, 5280, 2099.56, 1735.09, 2016),
(319, 5295, 2107.63, 1743.12, 2016),
(320, 5310, 2115.61, 1751.14, 2016),
(321, 5325, 2123.63, 1759.17, 2016),
(322, 5340, 2131.66, 1767.19, 2016),
(323, 5355, 2139.68, 1775.22, 2016),
(324, 5370, 2147.71, 1783.24, 2016),
(325, 5385, 2155.73, 1791.27, 2016),
(326, 5400, 2163.76, 1799.29, 2016),
(327, 5415, 2171.78, 1807.32, 2016),
(328, 5430, 2179.81, 1815.34, 2016),
(329, 5445, 2187.83, 1823.37, 2016),
(330, 5460, 2195.86, 1831.39, 2016),
(331, 5475, 2203.88, 1839.42, 2016),
(332, 5490, 2211.91, 1847.44, 2016),
(333, 5505, 2219.93, 1855.47, 2016),
(334, 5520, 2227.96, 1863.49, 2016),
(335, 5535, 2235.98, 1871.52, 2016),
(336, 5550, 2244.01, 1879.54, 2016),
(337, 5565, 2252.03, 1887.57, 2016),
(338, 5580, 2260.06, 1895.59, 2016),
(339, 5595, 2268.08, 1903.62, 2016),
(340, 5610, 2276.11, 1911.64, 2016),
(341, 5625, 2284.13, 1919.67, 2016),
(342, 5640, 2292.16, 1927.69, 2016),
(343, 5655, 2300.18, 1935.72, 2016),
(344, 5670, 2308.21, 1943.74, 2016),
(345, 5685, 2316.23, 1951.77, 2016),
(346, 5700, 2324.26, 1959.79, 2016),
(347, 5715, 2332.28, 1967.82, 2016),
(348, 5730, 2340.31, 1975.84, 2016),
(349, 5745, 2348.33, 1983.87, 2016),
(350, 5760, 2356.36, 1991.89, 2016),
(351, 5775, 2364.38, 1999.92, 2016),
(352, 5790, 2372.41, 2007.94, 2016),
(353, 5805, 2380.43, 2015.97, 2016),
(354, 5820, 2388.46, 2023.99, 2016),
(355, 5835, 2396.48, 2032.02, 2016),
(356, 5850, 2404.51, 2040.04, 2016),
(357, 5865, 2412.53, 2048.07, 2016),
(358, 5880, 2420.56, 2056.09, 2016),
(359, 5895, 2428.58, 2064.12, 2016),
(360, 5910, 2436.61, 2072.14, 2016),
(361, 5925, 2444.63, 2080.17, 2016),
(362, 5940, 2452.66, 2088.19, 2016),
(363, 5955, 2460.68, 2096.22, 2016),
(364, 5970, 2468.71, 2104.24, 2016),
(365, 5985, 2476.73, 2112.27, 2016),
(366, 6000, 2484.76, 2120.29, 2016),
(367, 6015, 2492.78, 2128.32, 2016),
(368, 6030, 2500.81, 2136.34, 2016),
(369, 6045, 2508.83, 2144.37, 2016),
(370, 6060, 2516.86, 2152.39, 2016),
(371, 6075, 2524.88, 2160.42, 2016),
(372, 6090, 2532.91, 2168.44, 2016),
(373, 6105, 2540.93, 2176.47, 2016),
(374, 6120, 2548.96, 2184.49, 2016),
(375, 6135, 2556.98, 2192.52, 2016),
(376, 6150, 2565.01, 2200.54, 2016),
(377, 6165, 2573.03, 2208.57, 2016),
(378, 6180, 2581.06, 2216.59, 2016),
(379, 6195, 2589.08, 2224.62, 2016),
(380, 6210, 2597.11, 2232.64, 2016),
(381, 6225, 2605.13, 2240.67, 2016),
(382, 6240, 2613.16, 2248.69, 2016),
(383, 6255, 2621.18, 2256.72, 2016),
(384, 6270, 2629.21, 2264.74, 2016),
(385, 6285, 2637.23, 2272.77, 2016),
(386, 6300, 2645.26, 2280.79, 2016),
(387, 6315, 2653.28, 2288.82, 2016),
(388, 6330, 2661.31, 2296.84, 2016),
(389, 6345, 2669.33, 2304.87, 2016),
(390, 6360, 2677.36, 2312.89, 2016),
(391, 6375, 2685.38, 2320.92, 2016),
(392, 6390, 2693.41, 2328.94, 2016),
(393, 6405, 2701.43, 2336.97, 2016),
(394, 6420, 2709.46, 2344.99, 2016),
(395, 6435, 2717.48, 2353.02, 2016),
(396, 6450, 2725.51, 2361.04, 2016),
(397, 6465, 2733.53, 2369.07, 2016),
(398, 6480, 2741.56, 2377.09, 2016),
(399, 6495, 2749.58, 2385.12, 2016),
(400, 6510, 2757.61, 2393.14, 2016),
(401, 6525, 2765.63, 2401.17, 2016),
(402, 6540, 2773.66, 2409.19, 2016),
(403, 6555, 2781.68, 2417.22, 2016),
(404, 6570, 2789.71, 2425.24, 2016),
(405, 6585, 2797.73, 2433.27, 2016),
(406, 6600, 2805.76, 2441.29, 2016),
(407, 6615, 2813.78, 2449.32, 2016),
(408, 6630, 2821.81, 2457.34, 2016),
(409, 6645, 2829.83, 2465.37, 2016),
(410, 6660, 2837.86, 2473.39, 2016),
(411, 6675, 2845.88, 2481.42, 2016),
(412, 6690, 2853.91, 2489.44, 2016),
(413, 6705, 2861.93, 2497.47, 2016),
(414, 6720, 2869.96, 2505.49, 2016),
(415, 6735, 2877.98, 2513.52, 2016),
(416, 6750, 2886.01, 2521.54, 2016),
(417, 6765, 2894.03, 2529.57, 2016),
(418, 6780, 2902.06, 2537.59, 2016),
(419, 6795, 2910.08, 2545.62, 2016),
(420, 6810, 2918.11, 2553.64, 2016),
(421, 6825, 2926.13, 2561.67, 2016),
(422, 6840, 2934.16, 2569.69, 2016),
(423, 6855, 2942.18, 2577.72, 2016),
(424, 6870, 2950.21, 2585.74, 2016),
(425, 6885, 2958.23, 2593.77, 2016),
(426, 6900, 2966.26, 2601.79, 2016),
(427, 6915, 2974.28, 2609.82, 2016),
(428, 6930, 2982.31, 2617.84, 2016),
(429, 6945, 2990.33, 2625.87, 2016),
(430, 6960, 2998.36, 2633.89, 2016),
(431, 6975, 3006.38, 2641.92, 2016),
(432, 6990, 3014.41, 2649.94, 2016),
(433, 7005, 3022.43, 2657.97, 2016),
(434, 7020, 3030.46, 2665.99, 2016),
(435, 7035, 3038.48, 2674.02, 2016),
(436, 7050, 3046.51, 2682.04, 2016),
(437, 7065, 3054.53, 2690.07, 2016),
(438, 7080, 3062.56, 2698.09, 2016),
(439, 7095, 3070.58, 2706.12, 2016),
(440, 7110, 3078.61, 2714.14, 2016),
(441, 7125, 3086.63, 2722.17, 2016),
(442, 7140, 3094.66, 2730.19, 2016),
(443, 7155, 3102.68, 2738.22, 2016),
(444, 7170, 3110.71, 2746.24, 2016),
(445, 7185, 3118.73, 2754.27, 2016),
(446, 7200, 3126.76, 2762.29, 2016),
(447, 7215, 3134.78, 2770.32, 2016),
(448, 7230, 3142.81, 2778.34, 2016),
(449, 7245, 3150.83, 2786.37, 2016),
(450, 7260, 3158.86, 2794.39, 2016),
(451, 7275, 3166.88, 2802.42, 2016),
(452, 7290, 3174.91, 2810.44, 2016),
(453, 7305, 3182.93, 2818.47, 2016),
(454, 7320, 3190.96, 2826.49, 2016),
(455, 7335, 3198.98, 2834.52, 2016),
(456, 7350, 3207.01, 2842.54, 2016),
(457, 7365, 3215.03, 2850.57, 2016),
(458, 7380, 3223.06, 2858.59, 2016),
(459, 7395, 3231.08, 2866.62, 2016),
(460, 7410, 3239.11, 2874.64, 2016),
(461, 7425, 3247.13, 2882.67, 2016),
(462, 7440, 3255.16, 2890.69, 2016),
(463, 7455, 3263.18, 2898.72, 2016),
(464, 7470, 3271.21, 2906.74, 2016),
(465, 7485, 3279.23, 2914.77, 2016),
(466, 7500, 3287.26, 2922.79, 2016);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `api_tech`
--

CREATE TABLE `api_tech` (
  `id` int(11) NOT NULL,
  `model` varchar(100) NOT NULL,
  `catalog_value` int(11) NOT NULL,
  `brand_id` int(11) DEFAULT NULL,
  `device_type` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `api_techbrand`
--

CREATE TABLE `api_techbrand` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add tech brand', 1, 'add_techbrand'),
(2, 'Can change tech brand', 1, 'change_techbrand'),
(3, 'Can delete tech brand', 1, 'delete_techbrand'),
(4, 'Can add tech', 2, 'add_tech'),
(5, 'Can change tech', 2, 'change_tech'),
(6, 'Can delete tech', 2, 'delete_tech'),
(7, 'Can add calculation parameter', 3, 'add_calculationparameter'),
(8, 'Can change calculation parameter', 3, 'change_calculationparameter'),
(9, 'Can delete calculation parameter', 3, 'delete_calculationparameter'),
(10, 'Can add bike brand', 4, 'add_bikebrand'),
(11, 'Can change bike brand', 4, 'change_bikebrand'),
(12, 'Can delete bike brand', 4, 'delete_bikebrand'),
(13, 'Can add bike', 5, 'add_bike'),
(14, 'Can change bike', 5, 'change_bike'),
(15, 'Can delete bike', 5, 'delete_bike'),
(16, 'Can add car brand', 6, 'add_carbrand'),
(17, 'Can change car brand', 6, 'change_carbrand'),
(18, 'Can delete car brand', 6, 'delete_carbrand'),
(19, 'Can add car', 7, 'add_car'),
(20, 'Can change car', 7, 'change_car'),
(21, 'Can delete car', 7, 'delete_car'),
(22, 'Can add car category', 8, 'add_carcategory'),
(23, 'Can change car category', 8, 'change_carcategory'),
(24, 'Can delete car category', 8, 'delete_carcategory'),
(25, 'Can add log entry', 9, 'add_logentry'),
(26, 'Can change log entry', 9, 'change_logentry'),
(27, 'Can delete log entry', 9, 'delete_logentry'),
(28, 'Can add permission', 10, 'add_permission'),
(29, 'Can change permission', 10, 'change_permission'),
(30, 'Can delete permission', 10, 'delete_permission'),
(31, 'Can add group', 11, 'add_group'),
(32, 'Can change group', 11, 'change_group'),
(33, 'Can delete group', 11, 'delete_group'),
(34, 'Can add user', 12, 'add_user'),
(35, 'Can change user', 12, 'change_user'),
(36, 'Can delete user', 12, 'delete_user'),
(37, 'Can add content type', 13, 'add_contenttype'),
(38, 'Can change content type', 13, 'change_contenttype'),
(39, 'Can delete content type', 13, 'delete_contenttype'),
(40, 'Can add session', 14, 'add_session'),
(41, 'Can change session', 14, 'change_session'),
(42, 'Can delete session', 14, 'delete_session'),
(43, 'Can add tax scale', 15, 'add_taxscale'),
(44, 'Can change tax scale', 15, 'change_taxscale'),
(45, 'Can delete tax scale', 15, 'delete_taxscale');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$30000$hzTnBFCR9LDS$pvC0QhbkwRPWm9qajwpUwUQGGZjOIku1+mpUZz9e7fQ=', NULL, 1, 'admin', '', '', '', 1, 1, '2017-01-18 17:59:52.969386');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(9, 'admin', 'logentry'),
(5, 'api', 'bike'),
(4, 'api', 'bikebrand'),
(3, 'api', 'calculationparameter'),
(7, 'api', 'car'),
(6, 'api', 'carbrand'),
(8, 'api', 'carcategory'),
(15, 'api', 'taxscale'),
(2, 'api', 'tech'),
(1, 'api', 'techbrand'),
(11, 'auth', 'group'),
(10, 'auth', 'permission'),
(12, 'auth', 'user'),
(13, 'contenttypes', 'contenttype'),
(14, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2017-01-12 12:58:09.720041'),
(2, 'auth', '0001_initial', '2017-01-12 12:58:21.379120'),
(3, 'admin', '0001_initial', '2017-01-12 12:58:24.199610'),
(4, 'admin', '0002_logentry_remove_auto_add', '2017-01-12 12:58:24.251665'),
(5, 'api', '0001_initial', '2017-01-12 12:58:25.233371'),
(6, 'api', '0002_auto_20161220_1145', '2017-01-12 12:58:43.929853'),
(7, 'api', '0003_auto_20161220_1516', '2017-01-12 12:58:52.764398'),
(8, 'api', '0004_auto_20161221_1439', '2017-01-12 12:58:59.449764'),
(9, 'api', '0005_tech_device_type', '2017-01-12 12:59:00.362032'),
(10, 'api', '0006_auto_20161221_1511', '2017-01-12 12:59:05.323153'),
(11, 'api', '0007_auto_20170104_1540', '2017-01-12 12:59:07.970238'),
(12, 'api', '0008_auto_20170104_1736', '2017-01-12 12:59:09.544852'),
(13, 'api', '0009_auto_20170104_2006', '2017-01-12 12:59:09.810656'),
(14, 'api', '0010_auto_20170105_1414', '2017-01-12 12:59:41.056100'),
(15, 'api', '0011_auto_20170112_1020', '2017-01-12 12:59:41.649706'),
(16, 'api', '0012_auto_20170112_1041', '2017-01-12 12:59:41.822420'),
(17, 'api', '0013_calculationparameter_max_vaa_car', '2017-01-12 12:59:43.339320'),
(18, 'api', '0014_auto_20170112_1208', '2017-01-12 12:59:51.294723'),
(19, 'contenttypes', '0002_remove_content_type_name', '2017-01-12 12:59:53.882919'),
(20, 'auth', '0002_alter_permission_name_max_length', '2017-01-12 12:59:55.276174'),
(21, 'auth', '0003_alter_user_email_max_length', '2017-01-12 12:59:57.117991'),
(22, 'auth', '0004_alter_user_username_opts', '2017-01-12 12:59:57.177724'),
(23, 'auth', '0005_alter_user_last_login_null', '2017-01-12 12:59:58.099680'),
(24, 'auth', '0006_require_contenttypes_0002', '2017-01-12 12:59:58.128200'),
(25, 'auth', '0007_alter_validators_add_error_messages', '2017-01-12 12:59:58.163225'),
(26, 'auth', '0008_alter_user_username_max_length', '2017-01-12 12:59:59.196149'),
(27, 'sessions', '0001_initial', '2017-01-12 12:59:59.881248'),
(28, 'api', '0002_auto_20170113_0933', '2017-01-13 15:46:58.332075'),
(29, 'api', '0003_calculationparameter_vaa_smartphone', '2017-01-13 15:46:58.999752'),
(30, 'api', '0004_calculationparameter_vaa_laptop', '2017-01-13 15:50:08.548339'),
(31, 'api', '0005_auto_20170113_1654', '2017-01-13 15:54:20.497455'),
(32, 'api', '0006_calculationparameter_vaa_internet', '2017-01-13 16:02:47.416443'),
(33, 'api', '0007_auto_20170118_1547', '2017-01-18 14:47:45.453255'),
(34, 'api', '0008_auto_20170119_1445', '2017-01-19 13:48:04.016659'),
(35, 'api', '0009_auto_20170119_1528', '2017-01-19 14:39:27.522606'),
(36, 'api', '0010_auto_20170120_1345', '2017-01-20 12:45:21.651789'),
(37, 'api', '0011_auto_20170120_1430', '2017-01-20 13:30:29.023548');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `api_bike`
--
ALTER TABLE `api_bike`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_bike_brand_id_f55ec410_fk_api_bikebrand_id` (`brand_id`);

--
-- Indexen voor tabel `api_bikebrand`
--
ALTER TABLE `api_bikebrand`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `api_calculationparameter`
--
ALTER TABLE `api_calculationparameter`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `api_car`
--
ALTER TABLE `api_car`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_car_category_id_985df86c_fk_api_carcategory_id` (`category_id`),
  ADD KEY `api_car_brand_id_4e152f9c_fk_api_carbrand_id` (`brand_id`);

--
-- Indexen voor tabel `api_carbrand`
--
ALTER TABLE `api_carbrand`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `api_carcategory`
--
ALTER TABLE `api_carcategory`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `api_taxscale`
--
ALTER TABLE `api_taxscale`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `api_tech`
--
ALTER TABLE `api_tech`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_tech_brand_id_43983dce_fk_api_techbrand_id` (`brand_id`);

--
-- Indexen voor tabel `api_techbrand`
--
ALTER TABLE `api_techbrand`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexen voor tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`);

--
-- Indexen voor tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexen voor tabel `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexen voor tabel `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexen voor tabel `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`);

--
-- Indexen voor tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexen voor tabel `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexen voor tabel `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_de54fa62` (`expire_date`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `api_bike`
--
ALTER TABLE `api_bike`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=315;
--
-- AUTO_INCREMENT voor een tabel `api_bikebrand`
--
ALTER TABLE `api_bikebrand`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT voor een tabel `api_calculationparameter`
--
ALTER TABLE `api_calculationparameter`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2017;
--
-- AUTO_INCREMENT voor een tabel `api_car`
--
ALTER TABLE `api_car`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
--
-- AUTO_INCREMENT voor een tabel `api_carbrand`
--
ALTER TABLE `api_carbrand`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT voor een tabel `api_carcategory`
--
ALTER TABLE `api_carcategory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT voor een tabel `api_taxscale`
--
ALTER TABLE `api_taxscale`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=467;
--
-- AUTO_INCREMENT voor een tabel `api_tech`
--
ALTER TABLE `api_tech`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT voor een tabel `api_techbrand`
--
ALTER TABLE `api_techbrand`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT voor een tabel `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT voor een tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT voor een tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;
--
-- AUTO_INCREMENT voor een tabel `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT voor een tabel `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT voor een tabel `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT voor een tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT voor een tabel `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT voor een tabel `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;
--
-- Beperkingen voor geëxporteerde tabellen
--

--
-- Beperkingen voor tabel `api_bike`
--
ALTER TABLE `api_bike`
  ADD CONSTRAINT `api_bike_brand_id_f55ec410_fk_api_bikebrand_id` FOREIGN KEY (`brand_id`) REFERENCES `api_bikebrand` (`id`);

--
-- Beperkingen voor tabel `api_car`
--
ALTER TABLE `api_car`
  ADD CONSTRAINT `api_car_brand_id_4e152f9c_fk_api_carbrand_id` FOREIGN KEY (`brand_id`) REFERENCES `api_carbrand` (`id`),
  ADD CONSTRAINT `api_car_category_id_985df86c_fk_api_carcategory_id` FOREIGN KEY (`category_id`) REFERENCES `api_carcategory` (`id`);

--
-- Beperkingen voor tabel `api_tech`
--
ALTER TABLE `api_tech`
  ADD CONSTRAINT `api_tech_brand_id_43983dce_fk_api_techbrand_id` FOREIGN KEY (`brand_id`) REFERENCES `api_techbrand` (`id`);

--
-- Beperkingen voor tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Beperkingen voor tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Beperkingen voor tabel `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Beperkingen voor tabel `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Beperkingen voor tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

