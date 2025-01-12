import great_expectations as gx

context = gx.get_context(mode="file")

data_source_name = "DS Taxi"
data_asset_name = "nyc_taxi_data"
batch_definition_name = "FULL_TABLE"
batch_definition = (
    context.data_sources.get(data_source_name)
    .get_asset(data_asset_name)
    .get_batch_definition(batch_definition_name)
)

batch = batch_definition.get_batch()

expectation = gx.expectations.ExpectColumnMaxToBeBetween(
    column="passenger_count", min_value=1, max_value=6
)

validation_results = batch.validate(expectation)

print(validation_results)