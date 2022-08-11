CREATE TABLE IF NOT EXISTS `test_db`.`open_weather_raw_data`(
    `reference_date` TIMESTAMP NOT NULL,
	`data` JSON NOT NULL,
    `loaded_at` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
	PRIMARY KEY(`reference_date`)
);

CREATE TABLE IF NOT EXISTS `test_db`.`max_temperature`(
    `date` VARCHAR(7) NOT NULL,
	`location` VARCHAR(255) NOT NULL,
    `max_temperature` DECIMAL(5,2),
	PRIMARY KEY(`date`,`location`)
);

CREATE TABLE IF NOT EXISTS `test_db`.`temperature_metrics`(
    `date` DATE NOT NULL,
    `sum_temperature` DECIMAL(5,2),
    `min_temperature` DECIMAL(5,2),
    `avg_temperature` DECIMAL(5,2),
    `location_min_temperature` VARCHAR(255),
    `location_max_temperature` VARCHAR(255),
	PRIMARY KEY(`date`)
);