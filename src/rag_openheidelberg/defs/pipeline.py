import dagster as dg


@dg.asset
def pipeline(context: dg.AssetExecutionContext) -> dg.MaterializeResult: ...
