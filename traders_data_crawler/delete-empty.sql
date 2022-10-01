USE `tradersdb`;
DELETE FROM `info` WHERE `info_id` IN ( SELECT `info_id` FROM ( SELECT `info`.`info_id` FROM `info` LEFT JOIN `data` ON `info`.`info_id` = `data`.`data_id` WHERE `data`.`data_id` IS NULL ) AS a );
DELETE FROM `info` WHERE `info_name` IS NULL;
DELETE FROM `data` WHERE `data_pair` LIKE 'LUNA-OLD/USDT';
