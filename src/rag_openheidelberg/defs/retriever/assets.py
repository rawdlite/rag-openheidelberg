import dagster as dg

@dg.asset(
    deps={"collector"},
    description="retrieve documents from a collection of document URI",
    kinds={"S3"},
    metadata={
        "link_to_docs": dg.MetadataValue.url("https://openheidelberg-obsidian.vercel.app/concepts/general-rag/"),
    }
)
def retriever():
    pass
