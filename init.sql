CREATE TABLE IF NOT EXISTS "user"
(
    username text,
    country text
);

INSERT INTO "user" (username, country)
	VALUES ('Bob', 'UK');
INSERT INTO "user" (username, country)
	VALUES ('Jane', 'Germany');
INSERT INTO "user" (username, country)
	VALUES ('Harry', 'US');
