import dagster as dg

@dg.asset(
    description="create a collection of document URI",
    kinds={"json"},
    metadata={
        "link_to_docs": dg.MetadataValue.url("https://openheidelberg-obsidian.vercel.app/concepts/general-rag/"),
    }
)
def collector():
    pass
