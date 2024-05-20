"""Project pipelines."""
from __future__ import annotations
from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from multicripto.pipelines.pipeline import create_pipeline as data_processing_pipeline


# def register_pipelines() -> dict[str, Pipeline]:
#     """Register the project's pipelines.

#     Returns:
#         A mapping from pipeline names to ``Pipeline`` objects.
#     """
#     pipelines = find_pipelines()
#     pipelines["__default__"] = sum(pipelines.values())
#     return pipelines

def register_pipelines():
    return {
        "__default__": data_processing_pipeline(),
        "dp": data_processing_pipeline(),
    }
