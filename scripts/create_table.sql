CREATE TABLE `test_db`.`open_weather_raw_data`(
    `reference_date` TIMESTAMP NOT NULL,
	`data` JSON NOT NULL,
    `loaded_at` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
	PRIMARY KEY(`reference_date`)
);