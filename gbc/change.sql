BEGIN;
ALTER TABLE core_slide RENAME TO core_slide_tmp;
ALTER TABLE core_tile RENAME TO core_tile_tmp;
ALTER TABLE core_featurette RENAME TO core_featurette_tmp;

CREATE TABLE "core_slide" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(256) NOT NULL,
    "content" text NOT NULL,
    "image" varchar(100) NOT NULL,
    "link" varchar(256),
    "link_text" varchar(64)
)
;
CREATE TABLE "core_tile" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(256) NOT NULL,
    "content" text NOT NULL,
    "image" varchar(100) NOT NULL,
    "link" varchar(256),
    "link_text" varchar(64),
    "image_format" varchar(2) NOT NULL
)
;
CREATE TABLE "core_featurette" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(256) NOT NULL,
    "subtitle" varchar(256) NOT NULL,
    "content" text NOT NULL,
    "image" varchar(100) NOT NULL,
    "link" varchar(256)
)
;

INSERT INTO core_slide(id, title, content, image, link)
SELECT id, title, content, image, link
FROM core_slide_tmp;

INSERT INTO core_tile(id, title, content, image, link, image_format)
SELECT id, title, content, image, link, 'R'
FROM core_tile_tmp;

INSERT INTO core_featurette(id, title, subtitle, content, image, link)
SELECT id, title, subtitle, content, image, link
FROM core_featurette_tmp;

DROP TABLE core_slide_tmp;
DROP TABLE core_tile_tmp;
DROP TABLE core_featurette_tmp;

CREATE TABLE "core_sponsor" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(128) NOT NULL,
    "description" varchar(512),
    "image" varchar(100) NOT NULL,
    "link" varchar(256)
)
;



COMMIT;