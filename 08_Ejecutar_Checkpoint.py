import great_expectations as gx

context = gx.get_context(mode="file")

checkpoint_name = "Checkpoint_Suite_DS_Taxi_nyc_taxi_data"
checkpoint = context.checkpoints.get(checkpoint_name)

validation_results = checkpoint.run()
print(validation_results)