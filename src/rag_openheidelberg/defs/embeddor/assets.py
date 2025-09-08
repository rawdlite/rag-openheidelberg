import dagster as dg

@dg.asset(
    deps={"vectorizer"},
    description="embeds vectors",
    kinds={"various", "frameworks"},
    metadata={
        "link_to_docs": dg.MetadataValue.url("https://openheidelberg-obsidian.vercel.app/concepts/general-rag/"),
    }
)
def embeddor():
    pass
