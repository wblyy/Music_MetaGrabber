SET SESSION storage_engine = "InnoDB"; 
ALTER DATABASE CHARACTER SET "utf8";

CREATE TABLE meta(
    id INT NOT NULL AUTO_INCREMENT,
    song varchar(50) NOT NULL,
    artist VARCHAR(50) NOT NULL,
    artist_img varchar(250),
    album_name varchar(50),
    album_img   varchar(250),
    album_release    DATETIME,
    company varchar(50),

    UNIQUE (song, artist),
    PRIMARY KEY (id)
);

