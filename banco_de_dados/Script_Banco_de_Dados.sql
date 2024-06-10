CREATE SCHEMA IF NOT EXISTS defaultdb DEFAULT CHARACTER SET utf8 ;
USE defaultdb ;

DROP TABLE IF EXISTS Grupo CASCADE ;
CREATE TABLE Grupo (
  idGrupo INT NOT NULL AUTO_INCREMENT,
  nome_grupo VARCHAR(45) NOT NULL UNIQUE,
  codigo_grupo VARCHAR(10) NOT NULL UNIQUE,
  PRIMARY KEY (idGrupo))
ENGINE = InnoDB;

DROP TABLE IF EXISTS Aluno CASCADE ;
CREATE TABLE Aluno (
  idAluno INT NOT NULL AUTO_INCREMENT,
  usuario_aluno VARCHAR(45) NOT NULL UNIQUE,
  senha_aluno VARCHAR(45) NOT NULL,
  idGrupo INT NULL,
  maior_pontuacao_aluno INT NOT NULL DEFAULT 0,
  PRIMARY KEY (idAluno),
FOREIGN KEY (idGrupo) REFERENCES Grupo (idGrupo) ON DELETE NO ACTION ON UPDATE NO ACTION)
ENGINE = InnoDB;

DROP TABLE IF EXISTS Professor CASCADE ;
CREATE TABLE Professor (
  idProfessor INT NOT NULL AUTO_INCREMENT,
  usuario_professor VARCHAR(45) NOT NULL UNIQUE,
  senha_professor VARCHAR(45) NOT NULL,
  idGrupo INT NULL,
  maior_pontuacao_professor INT NULL DEFAULT 0,
  PRIMARY KEY (idProfessor),
  FOREIGN KEY (idGrupo) REFERENCES Grupo (idGrupo) ON DELETE NO ACTION ON UPDATE NO ACTION)
ENGINE = InnoDB;

DROP TABLE IF EXISTS Administrador CASCADE ;
CREATE TABLE Administrador (
  idAdministrador INT NOT NULL AUTO_INCREMENT,
  usuario_administrador VARCHAR(45) NOT NULL UNIQUE,
  senha_administrador VARCHAR(45) NOT NULL,
  PRIMARY KEY (idAdministrador))
ENGINE = InnoDB;

DROP TABLE IF EXISTS Pergunta CASCADE ;
CREATE TABLE Pergunta (
  idPergunta INT NOT NULL AUTO_INCREMENT,
  texto_enunciado VARCHAR(700) NOT NULL,
  PRIMARY KEY (idPergunta))
ENGINE = InnoDB;

DROP TABLE IF EXISTS Alternativa CASCADE ;
CREATE TABLE Alternativa (
  idAlternativa INT NOT NULL AUTO_INCREMENT,
  alternativa VARCHAR(300) NOT NULL,
  PRIMARY KEY (idAlternativa))
ENGINE = InnoDB;

DROP TABLE IF EXISTS Tentativa CASCADE ;
CREATE TABLE Tentativa (
  idTentativa INT NOT NULL AUTO_INCREMENT,
  numero_tentativas INT NOT NULL DEFAULT 0,
  numero_acertos INT NOT NULL DEFAULT 0,
  PRIMARY KEY (idTentativa))
ENGINE = InnoDB;

DROP TABLE IF EXISTS Pergunta_Alternativas CASCADE ;
CREATE TABLE Pergunta_Alternativas (
  idPerguntaAlternativas INT NOT NULL,
  idGrupo INT NOT NULL,
  idPergunta INT NOT NULL,
  idAlternativa INT NOT NULL,
  idTentativa INT NOT NULL,
  alternativa_correta TINYINT NOT NULL,
  PRIMARY KEY (idPerguntaAlternativas, idGrupo, idPergunta, idAlternativa),
FOREIGN KEY (idGrupo) REFERENCES Grupo (idGrupo) ON DELETE NO ACTION ON UPDATE NO ACTION,
FOREIGN KEY (idPergunta) REFERENCES Pergunta (idPergunta) ON DELETE NO ACTION ON UPDATE NO ACTION,
FOREIGN KEY (idAlternativa) REFERENCES Alternativa (idAlternativa) ON DELETE NO ACTION ON UPDATE NO ACTION,
FOREIGN KEY (idTentativa) REFERENCES Tentativa (idTentativa) ON DELETE NO ACTION ON UPDATE NO ACTION)
ENGINE = InnoDB;








