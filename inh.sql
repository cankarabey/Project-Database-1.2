-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema new_schema1
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema new_schema1
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `new_schema1` ;
USE `new_schema1` ;

-- -----------------------------------------------------
-- Table `new_schema1`.`Students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `new_schema1`.`Students` (
  `FirstName` VARCHAR(45) NULL,
  `LastName` VARCHAR(45) NULL,
  `StudentNumber` INT NOT NULL,
  `Programme` VARCHAR(45) NULL,
  `Address` VARCHAR(45) NULL,
  `DateOfBirth` DATE NOT NULL,
  PRIMARY KEY (`StudentNumber`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `new_schema1`.`Programmes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `new_schema1`.`Programmes` (
  `idProgramme` INT NOT NULL,
  `Degree` VARCHAR(45) NULL,
  `ProgrammeName` VARCHAR(45) NULL,
  `Duration` INT NOT NULL,
  `ProgrammeLocation` VARCHAR(45) NULL,
  `TuitionFee` INT NULL,
  PRIMARY KEY (`idProgramme`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `new_schema1`.`Employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `new_schema1`.`Employees` (
  `idEmployees` INT NOT NULL,
  `FirstName` VARCHAR(45) NULL,
  `LastName` VARCHAR(45) NULL,
  `Title` VARCHAR(45) NULL,
  `Department` VARCHAR(45) NULL,
  `Salary` INT NULL,
  `FromDate` DATE NULL,
  `ToDate` DATE NULL,
  `DateOfBirth` DATE NULL,
  `Address` VARCHAR(45) NULL,
  `Gender` ENUM('F', 'M') NOT NULL,
  PRIMARY KEY (`idEmployees`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
