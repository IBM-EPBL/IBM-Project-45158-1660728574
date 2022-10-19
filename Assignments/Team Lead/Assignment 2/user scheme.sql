DROP TABLE IF EXISTS Users;

CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    EmailId VARCHAR NOT NULL,
    Password VARCHAR NOT NULL
);

INSERT INTO Users (Username, EmailId, Password) VALUES (
    "KK",
    "KK2002@gmail.com",
    "KK@123",
);
