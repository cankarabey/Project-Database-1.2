-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: inh
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `CourseName` varchar(45) NOT NULL,
  `Programme` int NOT NULL,
  `Description` varchar(200) DEFAULT NULL,
  `LECTURER` int NOT NULL,
  `ECTS` int NOT NULL,
  PRIMARY KEY (`CourseName`),
  KEY `idEmployees_idx` (`LECTURER`),
  KEY `idProgramme_idx` (`Programme`),
  CONSTRAINT `idEmployees` FOREIGN KEY (`LECTURER`) REFERENCES `employees` (`idEmployees`),
  CONSTRAINT `Programme` FOREIGN KEY (`Programme`) REFERENCES `programmes` (`idProgramme`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES ('Economics 1',32483,'moneys',3213213,4),('History 2',32483,'past',111111,5),('Mathematics 1',123321,'+-=',222222,5),('Mechanics 1',123321,'???',222222,5),('Sociology 1',32483,'An informative desc',3213213,5),('Thermodynamics 1',123321,'intro',222222,5);
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `idEmployees` int NOT NULL,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `Title` varchar(45) NOT NULL,
  `Department` varchar(45) NOT NULL,
  `Salary` int DEFAULT NULL,
  `FromDate` date NOT NULL,
  `ToDate` date DEFAULT NULL,
  `DateOfBirth` date NOT NULL,
  `Address` varchar(45) NOT NULL,
  `PostalCode` varchar(45) NOT NULL,
  `City` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Gender` enum('F','M') NOT NULL,
  `Counselor` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idEmployees`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (111111,'Joe','Biden','Dr.','Social Sciences',60000,'1998-08-09',NULL,'1954-04-20','This Street 81','234KA','Amsterdam','joe@uni.edu','M',NULL),(123211,'Janis','Joplin','Dr.','Sciences',60000,'1998-08-09','2000-09-09','1930-04-20','A Street 81','1231KA','Delft','janis@uni.edu','F',NULL),(222222,'Rick','Sanchez','Dr.','Sciences',55000,'1998-08-09',NULL,'1974-04-20','Other Street 81','234JA','Delft','ricky@uni.edu','M',NULL),(3213213,'Amy','Whinehouse','Dr.','Social Sciences',55000,'1998-08-09',NULL,'1954-04-20','That Street 81','92183JS','Amsterdam','amy@uni.edu','F',NULL);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exams`
--

DROP TABLE IF EXISTS `exams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exams` (
  `Course` varchar(45) NOT NULL,
  `idExam` int NOT NULL,
  `Room` varchar(45) NOT NULL,
  `Resit` enum('Y','N') DEFAULT NULL,
  `Date` date NOT NULL,
  `Time` varchar(45) NOT NULL,
  PRIMARY KEY (`idExam`),
  KEY `CourseName` (`Course`),
  CONSTRAINT `CourseName` FOREIGN KEY (`Course`) REFERENCES `courses` (`CourseName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exams`
--

LOCK TABLES `exams` WRITE;
/*!40000 ALTER TABLE `exams` DISABLE KEYS */;
INSERT INTO `exams` VALUES ('Mechanics 1',98909,'A243','Y','2018-08-13','12:00'),('Thermodynamics 1',98966,'A243','Y','2018-08-14','12:00'),('Sociology 1',312194,'A243','Y','2018-08-09','12:00'),('Economics 1',312313,'A244','Y','2018-08-10','12:00'),('History 2',321231,'A245','Y','2018-08-11','12:00'),('Mathematics 1',434533,'A246','Y','2018-08-12','12:00');
/*!40000 ALTER TABLE `exams` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `programmes`
--

DROP TABLE IF EXISTS `programmes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `programmes` (
  `idProgramme` int NOT NULL,
  `Degree` varchar(45) NOT NULL,
  `ProgrammeName` varchar(45) NOT NULL,
  `Description` varchar(200) NOT NULL,
  `Language` varchar(45) NOT NULL,
  `Duration` int NOT NULL,
  `ProgrammeLocation` varchar(45) NOT NULL,
  `TuitionFee` int DEFAULT NULL,
  PRIMARY KEY (`idProgramme`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `programmes`
--

LOCK TABLES `programmes` WRITE;
/*!40000 ALTER TABLE `programmes` DISABLE KEYS */;
INSERT INTO `programmes` VALUES (32483,'Bachelor','Political Science','All things politics.','English',4,'Amsterdam',2081),(123321,'Bachelor','Physics','particle fast','Dutch',4,'Delft',2081);
/*!40000 ALTER TABLE `programmes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `results`
--

DROP TABLE IF EXISTS `results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `results` (
  `Exam` varchar(45) NOT NULL,
  `ExamID` int NOT NULL,
  `STUDENT` int NOT NULL,
  `Grade` int NOT NULL,
  `PASSED` enum('Y','N') NOT NULL,
  PRIMARY KEY (`Exam`),
  KEY `StudentNummer_idx` (`STUDENT`),
  KEY `idExam` (`ExamID`),
  CONSTRAINT `idExam` FOREIGN KEY (`ExamID`) REFERENCES `exams` (`idExam`),
  CONSTRAINT `StudentNummer` FOREIGN KEY (`STUDENT`) REFERENCES `students` (`StudentNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `results`
--

LOCK TABLES `results` WRITE;
/*!40000 ALTER TABLE `results` DISABLE KEYS */;
INSERT INTO `results` VALUES ('Mathematics 1',434533,225532,70,'Y'),('Socialogy 1',312194,223432,60,'Y');
/*!40000 ALTER TABLE `results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `StudentNumber` int NOT NULL,
  `Programme` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  `DateOfBirth` date NOT NULL,
  `PostalCode` varchar(45) NOT NULL,
  `City` varchar(45) NOT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Counselor` int DEFAULT NULL,
  `StartYear` date NOT NULL,
  `Gender` enum('M','F') NOT NULL,
  `ProgrammeID` int NOT NULL,
  PRIMARY KEY (`StudentNumber`),
  KEY `idProgramme_idx` (`ProgrammeID`),
  CONSTRAINT `idProgramme` FOREIGN KEY (`ProgrammeID`) REFERENCES `programmes` (`idProgramme`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES ('Hans','Gutenberg',123123,'Physics','Other Street 32','1998-08-09','2342JA','Delft','hans@mail.com',NULL,'2018-08-09','M',123321),('Joe','Exotic',123333,'Political Science','Tiger Street 32','1998-08-09','87249AJ','Rotterdam','joex@mail.com',NULL,'2018-08-09','M',32483),('Max','Musterman',223432,'Political Science','Musterstrasse 32','1998-08-09','1234AB','Musterstadt','max@mail.com',NULL,'2018-08-09','M',32483),('Maria','Navarro',223842,'Political Science','This Street 12','1999-04-02','0238AJ','Rotterdam','maria32@mail.com',NULL,'2018-08-09','F',32483),('Julie','McJulieson',225532,'Physics','O Street 32','1998-08-09','831HA','Delft','julie@mail.com',NULL,'2018-08-09','F',123321),('Emma','Goldman',321231,'Physics','That Street 32','1998-08-09','10238JA','Delft','emma@mail.com',NULL,'2018-08-09','F',123321);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-20 11:32:27
