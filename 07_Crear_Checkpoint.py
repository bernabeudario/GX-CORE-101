import great_expectations as gx

context = gx.get_context(mode="file")

validation_name = "Validation_Suite_DS_Taxi_nyc_taxi_data"
validation_definitions = [ context.validation_definitions.get(validation_name)]

action_list = [
    gx.checkpoint.actions.UpdateDataDocsAction(
        name="update_my_site", site_names=["local_site"]
    )
]

checkpoint_name = "Checkpoint_Suite_DS_Taxi_nyc_taxi_data"
checkpoint = gx.Checkpoint(
    name=checkpoint_name,
    validation_definitions=validation_definitions,
    actions=action_list,
    result_format={"result_format": "COMPLETE"},
)

context.checkpoints.add(checkpoint)