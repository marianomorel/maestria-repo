-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 24, 2022 at 05:10 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `casa_paez`
--

-- --------------------------------------------------------

--
-- Table structure for table `categorias`
--

CREATE TABLE `categorias` (
  `cat_id` int(10) NOT NULL,
  `cat_name` varchar(64) NOT NULL,
  `cat_desc` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `categorias`
--

INSERT INTO `categorias` (`cat_id`, `cat_name`, `cat_desc`) VALUES
(1, 'Verduras', 'Verduras en general'),
(2, 'Frutas', 'Frutas de estación'),
(3, 'Verduras de hoja', 'Lechuga, acelga, etc.');

-- --------------------------------------------------------

--
-- Table structure for table `productos`
--

CREATE TABLE `productos` (
  `pro_id` int(10) NOT NULL,
  `pro_cat_id` int(10) DEFAULT NULL,
  `pro_sub_id` int(10) DEFAULT NULL,
  `pro_ven_id` int(10) DEFAULT NULL,
  `pro_descrip` varchar(256) NOT NULL,
  `pro_buy_value` float(10,2) DEFAULT NULL,
  `pro_buy_date` date DEFAULT NULL,
  `pro_margin1` float(5,2) DEFAULT NULL,
  `pro_sale_value1` float(10,2) DEFAULT NULL,
  `pro_margin2` float(5,2) DEFAULT NULL,
  `pro_sale_value2` float(10,2) DEFAULT NULL,
  `pro_margin3` float(5,2) DEFAULT NULL,
  `pro_sale_value3` float(10,2) DEFAULT NULL,
  `pro_update_date` date DEFAULT NULL,
  `pro_stock` int(12) DEFAULT NULL,
  `pro_codigo` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `productos`
--

INSERT INTO `productos` (`pro_id`, `pro_cat_id`, `pro_sub_id`, `pro_ven_id`, `pro_descrip`, `pro_buy_value`, `pro_buy_date`, `pro_margin1`, `pro_sale_value1`, `pro_margin2`, `pro_sale_value2`, `pro_margin3`, `pro_sale_value3`, `pro_update_date`, `pro_stock`, `pro_codigo`) VALUES
(1, 1, 1, 2, 'Tomate Platense', 120.00, '2022-06-28', 12.00, 134.40, 44.00, 172.80, 55.00, 186.00, '2022-06-28', 40, '1001'),
(2, 1, 1, 3, 'Papa negra', 60.00, '2022-06-28', 12.00, 67.20, 15.00, 69.00, 33.00, 79.80, '2022-06-28', 50, '1002'),
(3, 3, 1, 2, 'Lechuga', 250.00, '2022-06-28', 33.00, 332.50, 44.00, 360.00, 55.00, 387.50, '2022-06-28', 10, '234'),
(4, 3, 1, 3, 'Acelga (atado grande)', 300.00, '2022-06-28', 12.00, 336.00, 20.00, 360.00, 33.00, 399.00, '2022-06-28', 50, '101010'),
(5, 1, 1, 2, 'Tomate Perita', 150.00, '2022-06-28', 12.00, 168.00, 44.00, 216.00, 55.00, 232.50, '2022-06-28', 10, '10013'),
(6, 1, 2, 2, 'Papa blanca grande', 89.00, '2022-06-28', 12.00, 99.68, 22.00, 108.58, 34.00, 119.26, '2022-06-28', 120, '10015'),
(7, 2, 1, 1, 'Manzanas verdes', 376.32, '2022-06-28', 12.00, 421.48, 20.00, 451.58, 33.00, 500.51, '2022-07-07', 120, '10018'),
(8, 2, 1, 1, 'Manzana roja', 526.84, '2021-09-12', 12.00, 590.06, 18.00, 621.67, 22.00, 642.74, '2022-07-07', 40, '10019'),
(9, 1, 2, 2, 'Zapallo de tronco', 55.00, '2021-09-12', 12.00, 61.60, 22.00, 67.10, 32.00, 72.60, '2022-06-28', 121, '10006'),
(10, 1, 1, 2, 'Zapallo Anco', 55.00, '2021-09-12', 12.00, 61.60, 22.00, 67.10, 32.00, 72.60, '2022-06-28', 80, '10032'),
(11, 2, 1, 1, 'Peras', 268.80, '2020-01-09', 12.00, 301.06, 22.00, 327.94, 33.00, 357.50, '2022-07-07', 12, '111222');

-- --------------------------------------------------------

--
-- Table structure for table `proveedores`
--

CREATE TABLE `proveedores` (
  `ven_id` int(10) NOT NULL,
  `ven_name` varchar(64) NOT NULL,
  `ven_desc` varchar(255) NOT NULL,
  `ven_direc` varchar(64) DEFAULT NULL,
  `ven_loca` varchar(64) DEFAULT NULL,
  `ven_telef` varchar(32) DEFAULT NULL,
  `ven_telec` varchar(32) DEFAULT NULL,
  `ven_email` varchar(64) DEFAULT NULL,
  `ven_cbu` varchar(22) DEFAULT NULL,
  `ven_contacto` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `proveedores`
--

INSERT INTO `proveedores` (`ven_id`, `ven_name`, `ven_desc`, `ven_direc`, `ven_loca`, `ven_telef`, `ven_telec`, `ven_email`, `ven_cbu`, `ven_contacto`) VALUES
(1, 'Frutihortícola S.A.', 'Furtas y verduras al por mayor', 'Dominguez 1565', 'La Plata', '', '02396613943', 'frutihortícola@gmail.com', '02343456500012131', 'Juan Perez'),
(2, 'Huerto Martinez', 'Proveedor de Mar Del Plata, flete por El Rápido.', 'Mitre 456', 'Mar Del Plata - BA', '0233-34-3344', '', 'casa.martinez@gmail.com', '0234355550002302', 'Ana Martinez'),
(3, 'Huertas del sur', 'Frutas y verduras en general', 'Av. Indio Pampa 1323', 'Bahia Blanca - BA', '02345-44-5555', '02345-1544-5555', 'huertas.del.sur@gmail.com', '0234540003434823023', 'Natalia Perez');

-- --------------------------------------------------------

--
-- Table structure for table `subcategorias`
--

CREATE TABLE `subcategorias` (
  `sub_id` int(10) NOT NULL,
  `sub_name` varchar(64) NOT NULL,
  `sub_desc` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subcategorias`
--

INSERT INTO `subcategorias` (`sub_id`, `sub_name`, `sub_desc`) VALUES
(1, 'Estacional', 'Frutas y verduras de estación'),
(2, 'Premium', 'Productos exclusivos');

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `usu_name` varchar(32) NOT NULL,
  `usu_pass` varchar(16) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`usu_name`, `usu_pass`) VALUES
('Ariel', '1234');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`cat_id`);

--
-- Indexes for table `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`pro_id`);

--
-- Indexes for table `proveedores`
--
ALTER TABLE `proveedores`
  ADD PRIMARY KEY (`ven_id`);

--
-- Indexes for table `subcategorias`
--
ALTER TABLE `subcategorias`
  ADD PRIMARY KEY (`sub_id`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`usu_name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `categorias`
--
ALTER TABLE `categorias`
  MODIFY `cat_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `productos`
--
ALTER TABLE `productos`
  MODIFY `pro_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `proveedores`
--
ALTER TABLE `proveedores`
  MODIFY `ven_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `subcategorias`
--
ALTER TABLE `subcategorias`
  MODIFY `sub_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
