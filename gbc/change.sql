BEGIN;
/** Språkstöd **/
ALTER TABLE core_slide RENAME TO core_slide_tmp;
ALTER TABLE core_tile RENAME TO core_tile_tmp;
ALTER TABLE core_featurette RENAME TO core_featurette_tmp;
ALTER TABLE core_sponsor RENAME TO core_sponsor_tmp;

CREATE TABLE "core_slide" (
    "id" integer NOT NULL PRIMARY KEY,
    "title_sv" varchar(256) NOT NULL,
    "title_en" varchar(256),
    "content_sv" text NOT NULL,
    "content_en" text,
    "image" varchar(100) NOT NULL,
    "link" varchar(256),
    "link_text_sv" varchar(64),
    "link_text_en" varchar(64)
)
;
CREATE TABLE "core_tile" (
    "id" integer NOT NULL PRIMARY KEY,
    "title_sv" varchar(256) NOT NULL,
    "title_en" varchar(256),
    "content_sv" text NOT NULL,
    "content_en" text,
    "image" varchar(100) NOT NULL,
    "link" varchar(256),
    "link_file" varchar(100),
    "link_text_sv" varchar(64),
    "link_text_en" varchar(64),
    "image_format" varchar(2) NOT NULL
)
;
CREATE TABLE "core_featurette" (
    "id" integer NOT NULL PRIMARY KEY,
    "title_sv" varchar(256) NOT NULL,
    "title_en" varchar(256),
    "subtitle_sv" varchar(256) NOT NULL,
    "subtitle_en" varchar(256),
    "content_sv" text NOT NULL,
    "content_en" text,
    "image" varchar(100) NOT NULL,
    "link" varchar(256)
)
;

CREATE TABLE "core_sponsor" (
    "id" integer NOT NULL PRIMARY KEY,
    "title_sv" varchar(128) NOT NULL,
    "title_en" varchar(128),
    "description_sv" varchar(512),
    "description_en" varchar(512),
    "image" varchar(100) NOT NULL,
    "link" varchar(256)
)
;
INSERT INTO core_slide(id, title_sv, content_sv, image, link, link_text_sv)
SELECT id, title, content, image, link, link_text
FROM core_slide_tmp;

INSERT INTO core_tile(id, title_sv, content_sv, image, link, image_format, link_text_sv)
SELECT id, title, content, image, link, 'R', link_text
FROM core_tile_tmp;

INSERT INTO core_featurette(id, title_sv, subtitle_sv, content_sv, image, link)
SELECT id, title, subtitle, content, image, link
FROM core_featurette_tmp;

/* Conversion for sponsors missing. */

DROP TABLE core_slide_tmp;
DROP TABLE core_tile_tmp;
DROP TABLE core_featurette_tmp;
DROP TABLE core_sponsor_tmp;

COMMIT;
