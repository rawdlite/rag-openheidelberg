import dagster as dg

@dg.asset(
    deps={"retriever"},
    description="convert documents to requirerd format, extract metadata",
    kinds={"markdown","docling"},
    metadata={
        "link_to_docs": dg.MetadataValue.url("https://openheidelberg-obsidian.vercel.app/concepts/general-rag/"),
    }
)
def converter():
    pass
