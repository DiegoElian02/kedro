from kedro.pipeline import Pipeline, node
from .nodes.nodes import process_dates_and_ids, split_datasets, average_duration, count_trips, final_stats

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=process_dates_and_ids,
            inputs="rawdata",
            outputs="processed_data",
            name="process_dates_and_ids_node"
        ),
        node(
            func=split_datasets,
            inputs="processed_data",
            outputs=["dataset1", "dataset2"],
            name="split_datasets_node"
        ),
        node(
            func=average_duration,
            inputs="dataset1",
            outputs="dataset1_processed",
            name="average_duration_node"
        ),
        node(
            func=count_trips,
            inputs="dataset2",
            outputs="dataset2_processed",
            name="count_trips_node"
        ),
        node(
            func=final_stats,
            inputs=["dataset1_processed", "dataset2_processed"],
            outputs="final_stats",
            name="final_stats_node"
        )
    ])
