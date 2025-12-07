-- Create airflow role if not exists
DO
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'airflow') THEN
        CREATE ROLE airflow LOGIN PASSWORD 'airflow';
    END IF;
END
$$;

-- Create airflow_db (this must NOT be inside DO)
CREATE DATABASE airflow_db OWNER airflow;


