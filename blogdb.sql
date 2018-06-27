-- MySQL dump 10.16  Distrib 10.1.32-MariaDB, for osx10.6 (i386)
--
-- Host: localhost    Database: blogdb
-- ------------------------------------------------------
-- Server version	10.1.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blog`
--

DROP TABLE IF EXISTS `blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `abstract` varchar(200) NOT NULL,
  `content` text NOT NULL,
  `uid` int(10) unsigned DEFAULT NULL,
  `pcount` int(10) unsigned DEFAULT '0',
  `flag` tinyint(3) unsigned DEFAULT '0',
  `cdate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog`
--

LOCK TABLES `blog` WRITE;
/*!40000 ALTER TABLE `blog` DISABLE KEYS */;
INSERT INTO `blog` VALUES (1,'人生苦短 我学python','人生苦短 我学python - abstract','人生苦短 我学python - content',1,100,1,'2018-05-20 10:22:41'),(2,'人生苦短 我学python1','人生苦短 我学python - abstract1','人生苦短 我学python - content1',2,500,1,'2018-05-21 10:22:41'),(3,'人生苦短 我学python2','人生苦短 我学python - abstract2','人生苦短 我学python - content2',3,20,2,'2018-05-22 10:22:41'),(4,'人生苦短 我学python3','人生苦短 我学python - abstract3','人生苦短 我学python - content3',1,850,1,'2018-05-23 10:22:41'),(5,'人生苦短 我学python4','人生苦短 我学python - abstract4','人生苦短 我学python - content4',5,300,1,'2018-05-24 10:22:41'),(6,'人生苦短 我学python5','人生苦短 我学python - abstract5','人生苦短 我学python - content5',1,0,0,'2018-05-22 12:22:41'),(7,'人生苦短 我学python6','人生苦短 我学python - abstract6','人生苦短 我学python - content6',2,130,1,'2018-05-21 10:22:41'),(8,'人生苦短 我学python7','人生苦短 我学python - abstract7','人生苦短 我学python - content7',6,10,1,'2018-05-22 10:22:41'),(9,'人生苦短 我学python8','人生苦短 我学python - abstract8','人生苦短 我学python - content8',1,800,0,'2018-05-23 10:22:41'),(10,'人生苦短 我学python9','人生苦短 我学python - abstract9','人生苦短 我学python - content9',3,80,1,'2018-05-25 10:22:41'),(11,'人生苦短 我学python10','人生苦短 我学python - abstract10','人生苦短 我学python - content10',1,300,1,'2018-05-21 10:22:41'),(12,'人生苦短 我学python11','人生苦短 我学python - abstract11','人生苦短 我学python - content11',2,600,1,'2018-05-20 10:22:41'),(13,'人生苦短 我学python12','人生苦短 我学python - abstract12','人生苦短 我学python - content12',5,400,1,'2018-05-22 10:22:41'),(14,'人生苦短 我学python13','人生苦短 我学python - abstract13','人生苦短 我学python - content13',6,100,2,'2018-05-24 10:22:41'),(15,'人生苦短 我学python14','人生苦短 我学python - abstract14','人生苦短 我学python - content14',1,900,1,'2018-05-25 10:22:41');
/*!40000 ALTER TABLE `blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `cdate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'John','john@163.com','2018-05-16 17:23:32'),(2,'Abby','abby@163.com','2018-05-20 12:20:13'),(3,'Barry','barry@163.com','2018-04-26 15:12:32'),(4,'Lily','lily@163.com','2018-03-16 10:13:22'),(5,'George','george@163.com','2018-05-26 07:20:32'),(6,'Thomas','thomas@163.com','2018-01-02 10:23:12');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-27 12:36:56
