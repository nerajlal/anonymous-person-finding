 Server: localhost -  Database: pydb -  Table: pytb1
-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 18, 2023 at 07:07 AM
-- Server version: 5.1.36
-- PHP Version: 5.3.0

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- Database: `pydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `pytb1`
--

CREATE TABLE IF NOT EXISTS `pytb1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `count` int(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=22 ;

--
-- Dumping data for table `pytb1`
--

INSERT INTO `pytb1` (`id`, `count`) VALUES
(21, 13),
(20, 27),
(19, 10),
(18, 3);

