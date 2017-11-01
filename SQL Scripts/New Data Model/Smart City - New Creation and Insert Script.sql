# Drop old database
DROP DATABASE smartcity_db;

CREATE DATABASE IF NOT EXISTS smartcityv2_db;
USE smartcityv2_db;

CREATE TABLE IF NOT EXISTS user (
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(60) NOT NULL,
email VARCHAR(100) NOT NULL,
password VARCHAR(60) NOT NULL
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS profile (
userId INT NOT NULL, 
userType ENUM('student', 'tourist', 'business'),
FOREIGN KEY(userId) REFERENCES smartcityv2_db.user(id)
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS city (
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100) NOT NULL,
state VARCHAR(10) NOT NULL,
latitude DECIMAL(20, 10) NOT NULL,
longitude DECIMAL(20, 10) NOT NULL
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS locationInfo (
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
cityId INT NOT NULL,
name VARCHAR(100) NOT NULL,
address VARCHAR(500) NOT NULL,
email VARCHAR(100) NOT NULL,
image VARCHAR(500) NOT NULL,
phone VARCHAR(20),
industryType VARCHAR(200),
departments VARCHAR(200),
infoType ENUM(
'college', 'library', 'industry', 'hotel', 'park',
'zoo', 'museum', 'restaurant', 'mall'
),
favourites INT,
FOREIGN KEY(cityId) REFERENCES smartcityv2_db.city(id)
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS review (
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
userId INT NOT NULL,
locationInfoId INT NOT NULL,
rating VARCHAR(1) NOT NULL,
text VARCHAR(100) NOT NULL,
FOREIGN KEY(userId) REFERENCES smartcityv2_db.user(id),
FOREIGN KEY(locationInfoId) REFERENCES smartcityv2_db.city(id)
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

# Inserting dummy data
INSERT INTO user VALUES(
1, 
'test_student', 
'student@sample.com',
'password123'
);

INSERT INTO profile VALUES(
1, 
'student'
);

INSERT INTO city VALUES(
1, 
'Brisbane',
'QLD',
-27.4698,
153.0251
);

INSERT INTO locationInfo VALUES(
1,
1, # Brisbane ID
'QUT',
'2 George St, Brisbane City QLD 4000',
'askqut@qut.edu.au',
'https://www.qut.edu.au/qut-logo-og-200.jpg',
'',
'',
'Business, Creative Industries...etc.',
'college',
0
);

INSERT INTO review VALUES(
1, 
1, # Brisbane ID
1, # QUT ID
5,
'Very nice campus'
);

# 2nd lot of data
INSERT INTO city VALUES(
last_insert_id(),
'Melbourne',
'VIC',
-37.8136,
144.9631
);

INSERT INTO user VALUES(
last_insert_id(),
'tourist1',
'tourist1@example.com',
'password321'
);

INSERT INTO profile VALUES(
last_insert_id(),
'tourist'
);

INSERT INTO locationInfo VALUES(
last_insert_id(),
2, # Melbourne ID
'University of Melbourne',
'Parkville VIC 3010',
'http://melbourneuni.png',
'ask@unm.edu.au',
'0447539222',
'',
'Business, Aviation',
'college',
1
);

INSERT INTO review VALUES(
last_insert_id(), 
2, # Melbourne ID
2, # UNM ID
3,
'Antique campus'
);
