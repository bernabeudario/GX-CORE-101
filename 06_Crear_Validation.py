import great_expectations as gx

context = gx.get_context(mode="file")

suite_name = "Suite_DS_Taxi_nyc_taxi_data"
suite = context.suites.get(name=suite_name)

data_source_name = "DS Taxi"
data_asset_name = "nyc_taxi_data"
batch_definition_name = "FULL_TABLE"
batch_definition = (
    context.data_sources.get(data_source_name)
    .get_asset(data_asset_name)
    .get_batch_definition(batch_definition_name)
)

definition_name = "Validation_Suite_DS_Taxi_nyc_taxi_data"
validation_definition = gx.ValidationDefinition(
    data=batch_definition, suite=suite, name=definition_name
)

validation_definition = context.validation_definitions.add(validation_definition)