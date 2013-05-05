BEGIN;

ALTER TABLE core_slide ADD COLUMN 'order' integer NOT NULL default 99;

ALTER TABLE core_featurette ADD COLUMN 'order' integer NOT NULL default 99;


ALTER TABLE core_tile ADD COLUMN 'order' integer NOT NULL default 99;

ALTER TABLE core_sponsor ADD COLUMN 'order' integer NOT NULL default 99;

COMMIT;
