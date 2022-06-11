CREATE DATABASE exobieres;
use exobieres;
CREATE TABLE bieres (
	num_biere integer NOT NULL AUTO_INCREMENT,
	nom_biere VARCHAR(30),marque VARCHAR(50),
	CONSTRAINT PRIMARY KEY (num_biere))
	ENGINE=InnoDB;
CREATE TABLE bars (
	num_bar integer NOT NULL AUTO_INCREMENT,
	nom_bar VARCHAR(30),
	adresse VARCHAR(50),
	licence VARCHAR(50),
	CONSTRAINT PRIMARY KEY (num_bar))
	ENGINE=InnoDB;
CREATE TABLE tarifs (
	num_bar		integer NOT NULL,
	num_biere	integer NOT NULL,
	prix		REAL,
	CONSTRAINT PRIMARY KEY (num_bar,num_biere),
	CONSTRAINT FOREIGN KEY (num_bar) REFERENCES bars (num_bar),
	CONSTRAINT FOREIGN KEY (num_biere) REFERENCES bieres (num_biere)
	)
	ENGINE=InnoDB;
CREATE TABLE clients (
	num_client integer NOT NULL AUTO_INCREMENT,
	nom_client VARCHAR(30),
	adresse VARCHAR(50),
	telephone CHAR(16),
	CONSTRAINT PRIMARY KEY (num_client))
	ENGINE=InnoDB;
CREATE TABLE aimer (
	num_client integer NOT NULL,
	num_biere integer NOT NULL,
	CONSTRAINT PRIMARY KEY (num_client,num_biere),
	CONSTRAINT FOREIGN KEY (num_client) REFERENCES clients (num_client),
	CONSTRAINT FOREIGN KEY (num_biere) REFERENCES bieres (num_biere)
	)
	ENGINE=InnoDB;
CREATE TABLE frequenter (
	num_client integer NOT NULL,
	num_bar integer NOT NULL,
	CONSTRAINT PRIMARY KEY (num_client,num_bar),
	CONSTRAINT FOREIGN KEY (num_client) REFERENCES clients (num_client),
	CONSTRAINT FOREIGN KEY (num_bar) REFERENCES bars (num_bar)
	)
	ENGINE=InnoDB;

insert into bieres values(null,'Coors','Adolph Coors');
insert into bieres values(null,'Coors Lite','Adolph Coors');
insert into bieres values(null,'Miller','Miller Brewing');
insert into bieres values(null,'Miller Lite','Miller Brewing');
insert into bieres values(null,'MGD','Miller Brewing');
insert into bieres values(null,'Bud','Anheuser-Busch');
insert into bieres values(null,'Bud Lite','Anheuser-Busch');
insert into bieres values(null,'Michelob','Anheuser-Busch');
insert into bieres values(null,'Anchor Steam','Anchor Brewing');

insert into bars values(null,'Joe''s','123 Any Street','B7462A');
insert into bars values(null,'Sue','456 My Way','C5473S');
insert into bars values(null,'Carole','12541 rue du truc','B7462A');
insert into bars values(null,'Patrick','127 avenue du machin','C5473S');
insert into bars values(null,'Sally','1 route du bidule','B7462A');
insert into bars values(null,'Paul','568 grande avenue','C5473S');
insert into bars values(null,'Jack','2 impasse de la chose','B7462A');
insert into bars values(null,'Averell','Lieu dit','C5473S');

insert into tarifs select (select num_bar from bars where nom_bar='Joe''s'),(select num_biere from bieres where nom_biere='Coors'),2;
insert into tarifs select (select num_bar from bars where nom_bar='Joe''s'),(select num_biere from bieres where nom_biere='Bud'),2;
insert into tarifs select (select num_bar from bars where nom_bar='Joe''s'),(select num_biere from bieres where nom_biere='Bud Lite'),2;
insert into tarifs select (select num_bar from bars where nom_bar='Joe''s'),(select num_biere from bieres where nom_biere='Michelob'),2;
insert into tarifs select (select num_bar from bars where nom_bar='Joe''s'),(select num_biere from bieres where nom_biere='Anchor Steam'),3;
insert into tarifs select (select num_bar from bars where nom_bar='Sue'),(select num_biere from bieres where nom_biere='Coors'),4;
insert into tarifs select (select num_bar from bars where nom_bar='Sue'),(select num_biere from bieres where nom_biere='Miller'),3;
insert into tarifs select (select num_bar from bars where nom_bar='Carole'),(select num_biere from bieres where nom_biere='Coors'),1;
insert into tarifs select (select num_bar from bars where nom_bar='Carole'),(select num_biere from bieres where nom_biere='Bud'),6;
insert into tarifs select (select num_bar from bars where nom_bar='Carole'),(select num_biere from bieres where nom_biere='Bud Lite'),3;
insert into tarifs select (select num_bar from bars where nom_bar='Carole'),(select num_biere from bieres where nom_biere='Michelob'),4;
insert into tarifs select (select num_bar from bars where nom_bar='Carole'),(select num_biere from bieres where nom_biere='Anchor Steam'),2;
insert into tarifs select (select num_bar from bars where nom_bar='Patrick'),(select num_biere from bieres where nom_biere='Coors'),3;
insert into tarifs select (select num_bar from bars where nom_bar='Patrick'),(select num_biere from bieres where nom_biere='Bud'),4;
insert into tarifs select (select num_bar from bars where nom_bar='Patrick'),(select num_biere from bieres where nom_biere='Bud Lite'),2;
insert into tarifs select (select num_bar from bars where nom_bar='Patrick'),(select num_biere from bieres where nom_biere='Michelob'),6;
insert into tarifs select (select num_bar from bars where nom_bar='Patrick'),(select num_biere from bieres where nom_biere='Anchor Steam'),5;
insert into tarifs select (select num_bar from bars where nom_bar='Patrick'),(select num_biere from bieres where nom_biere='Miller'),4;
insert into tarifs select (select num_bar from bars where nom_bar='Sally'),(select num_biere from bieres where nom_biere='Coors'),2;
insert into tarifs select (select num_bar from bars where nom_bar='Sally'),(select num_biere from bieres where nom_biere='Bud'),3;
insert into tarifs select (select num_bar from bars where nom_bar='Sally'),(select num_biere from bieres where nom_biere='Bud Lite'),4;
insert into tarifs select (select num_bar from bars where nom_bar='Sally'),(select num_biere from bieres where nom_biere='Michelob'),6;
insert into tarifs select (select num_bar from bars where nom_bar='Sally'),(select num_biere from bieres where nom_biere='Anchor Steam'),4;
insert into tarifs select (select num_bar from bars where nom_bar='Sally'),(select num_biere from bieres where nom_biere='Miller'),2;
insert into tarifs select (select num_bar from bars where nom_bar='Paul'),(select num_biere from bieres where nom_biere='Bud Lite'),6;
insert into tarifs select (select num_bar from bars where nom_bar='Paul'),(select num_biere from bieres where nom_biere='Michelob'),5;
insert into tarifs select (select num_bar from bars where nom_bar='Paul'),(select num_biere from bieres where nom_biere='Anchor Steam'),4;
insert into tarifs select (select num_bar from bars where nom_bar='Paul'),(select num_biere from bieres where nom_biere='Miller'),3;
insert into tarifs select (select num_bar from bars where nom_bar='Jack'),(select num_biere from bieres where nom_biere='Coors'),4;
insert into tarifs select (select num_bar from bars where nom_bar='Jack'),(select num_biere from bieres where nom_biere='Bud'),5;
insert into tarifs select (select num_bar from bars where nom_bar='Jack'),(select num_biere from bieres where nom_biere='Bud Lite'),6;
insert into tarifs select (select num_bar from bars where nom_bar='Averell'),(select num_biere from bieres where nom_biere='Coors'),5;
insert into tarifs select (select num_bar from bars where nom_bar='Averell'),(select num_biere from bieres where nom_biere='Miller'),4;

insert into clients values(null,'Bill','1 avenue ZZZZ','831-459-1812');
insert into clients values(null,'Kelly','2 rue RRRRR','650-856-2002');
insert into clients values(null,'Fred','3 GGGGGG','831-426-1956');
insert into clients values(null,'Francis','4 FFFFFFFF','831-459-1812');
insert into clients values(null,'François','5 DDDDDDDD','650-856-2002');
insert into clients values(null,'Sylvie','6 SSSSSSSSS','831-426-1956');
insert into clients values(null,'John','1234 sssssssss','831-426-1956');

insert into aimer select (select num_client from clients where nom_client='Bill'),(select num_biere from bieres where nom_biere='Miller');
insert into aimer select (select num_client from clients where nom_client='Bill'),(select num_biere from bieres where nom_biere='Michelob');
insert into aimer select (select num_client from clients where nom_client='Kelly'),(select num_biere from bieres where nom_biere='Anchor Steam');
insert into aimer select (select num_client from clients where nom_client='Fred'),(select num_biere from bieres where nom_biere='MGD');
insert into aimer select (select num_client from clients where nom_client='Fred'),(select num_biere from bieres where nom_biere='Bud Lite');
insert into aimer select (select num_client from clients where nom_client='Francis'),(select num_biere from bieres where nom_biere='Michelob');
insert into aimer select (select num_client from clients where nom_client='Francis'),(select num_biere from bieres where nom_biere='Anchor Steam');
insert into aimer select (select num_client from clients where nom_client='Francis'),(select num_biere from bieres where nom_biere='Miller');
insert into aimer select (select num_client from clients where nom_client='François'),(select num_biere from bieres where nom_biere='Coors');
insert into aimer select (select num_client from clients where nom_client='Sylvie'),(select num_biere from bieres where nom_biere='Coors');
insert into aimer select (select num_client from clients where nom_client='Sylvie'),(select num_biere from bieres where nom_biere='Bud');
insert into aimer select (select num_client from clients where nom_client='Sylvie'),(select num_biere from bieres where nom_biere='Bud Lite');
insert into aimer select (select num_client from clients where nom_client='John'),(select num_biere from bieres where nom_biere='Michelob');
insert into aimer select (select num_client from clients where nom_client='John'),(select num_biere from bieres where nom_biere='Anchor Steam');

insert into frequenter select (select num_client from clients where nom_client='Bill'),(select num_bar from bars where nom_bar='Joe''s');
insert into frequenter select (select num_client from clients where nom_client='Bill'),(select num_bar from bars where nom_bar='Sue');
insert into frequenter select (select num_client from clients where nom_client='Kelly'),(select num_bar from bars where nom_bar='Joe''s');
insert into frequenter select (select num_client from clients where nom_client='Fred'),(select num_bar from bars where nom_bar='Carole');
insert into frequenter select (select num_client from clients where nom_client='Fred'),(select num_bar from bars where nom_bar='Patrick');
insert into frequenter select (select num_client from clients where nom_client='Francis'),(select num_bar from bars where nom_bar='Sally');
insert into frequenter select (select num_client from clients where nom_client='Francis'),(select num_bar from bars where nom_bar='Paul');
insert into frequenter select (select num_client from clients where nom_client='Sylvie'),(select num_bar from bars where nom_bar='Jack');
insert into frequenter select (select num_client from clients where nom_client='Sylvie'),(select num_bar from bars where nom_bar='Patrick');
insert into frequenter select (select num_client from clients where nom_client='John'),(select num_bar from bars where nom_bar='Averell');
insert into frequenter select (select num_client from clients where nom_client='John'),(select num_bar from bars where nom_bar='Paul');
