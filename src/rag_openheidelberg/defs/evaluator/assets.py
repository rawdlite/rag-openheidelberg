import dagster as dg

@dg.asset(
    deps={"query"},
    group_name="evaluation",
    description="compares a list of given answers to provided answers",
    kinds={"cosine"},
    metadata={
        "link_to_docs": dg.MetadataValue.url("https://openheidelberg-obsidian.vercel.app/concepts/general-rag/"),
    }
)
def evaluator():
    pass
