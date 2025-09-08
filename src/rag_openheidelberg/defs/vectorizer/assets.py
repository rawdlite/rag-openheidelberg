import dagster as dg

@dg.asset(
    deps={"tokenizer"},
    description="vectorize tokens",
    kinds={"various"},
    metadata={
        "link_to_docs": dg.MetadataValue.url("https://openheidelberg-obsidian.vercel.app/concepts/general-rag/"),
    }
)
def vectorizer():
    pass
