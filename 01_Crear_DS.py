import great_expectations as gx

context = gx.get_context(mode="file") # Definimos que se utilizará la metadata almacenada en el filesystem

datasource_name = "DS Taxi"
my_connection_string = "postgresql+psycopg2://readonly:gxpassword@sample-data-gx-cloud.cwbweqtoi6rb.us-east-1.rds.amazonaws.com/gx_demo_database"

data_source = context.data_sources.add_postgres(
    name=datasource_name, connection_string=my_connection_string
)

print(context.data_sources.get(datasource_name))