CREATE TABLE Space(
    ID int NOT NULL AUTO_INCREMENT,
    Space_name varchar(255) NOT NULL DEFAULT 'None',
    region varchar(255) NOT NULL DEFAULT '翠亨',
    link varchar(255) NULL DEFAULT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE Register(
    Start_time TIME NOT NULL,
    Space_id int NOT NULL,
    usable bool NOT NULL DEFAULT TRUE,
    user_id int NULL DEFAULT NULL,
    user_phone int NULL DEFAULT NULL,
    user_dormnumber int NULL DEFAULT NULL,
    change_pwd varchar(255) NULL DEFAULT NULL,
    PRIMARY KEY (Space_id, Start_time),
    FOREIGN KEY (Space_id) REFERENCES Space(ID)
);