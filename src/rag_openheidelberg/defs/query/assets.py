import dagster as dg

@dg.asset(
    deps={"embeddor"},
    group_name="evaluation",
    description="queries a list of questions and stores the answers",
    kinds={"batch"},
    metadata={
        "link_to_docs": dg.MetadataValue.url("https://openheidelberg-obsidian.vercel.app/concepts/general-rag/"),
    }
)
def query():
    pass
