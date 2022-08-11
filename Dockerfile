FROM mysql

ADD scripts/create_table.sql /docker-entrypoint-initdb.d