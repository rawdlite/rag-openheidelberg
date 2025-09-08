import dagster as dg

@dg.asset(
    deps={"converter"},
    description="extract and store metadata",
    kinds={"optional"},
    metadata={
        "link_to_docs": dg.MetadataValue.url("https://openheidelberg-obsidian.vercel.app/concepts/general-rag/"),
    }
)
def categorizer():
    pass
