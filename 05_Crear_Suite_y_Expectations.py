import great_expectations as gx

context = gx.get_context(mode="file")

suite_name = "Suite_DS_Taxi_nyc_taxi_data"
suite = context.suites.add(gx.ExpectationSuite(name=suite_name))

suite.add_expectation(
    gx.expectations.ExpectColumnMaxToBeBetween(
        column="passenger_count", min_value=1, max_value=6
    )
)

suite.add_expectation(
    gx.expectations.ExpectColumnPairValuesAToBeGreaterThanB(
        column_A="dropoff_time", column_B="pickup_time", or_equal=False
    )
)