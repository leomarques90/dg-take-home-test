FROM mysql

ADD scripts/create_tables.sql /docker-entrypoint-initdb.d