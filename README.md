# General RAG
This project provides a configurable and adaptable pipeline to preprocess, embed, query, and evaluate Retrieval-Augmented Generation (RAG) systems.

Its primary goal is to support members of the OpenHeidelberg AI team in experimenting with and evaluating different aspects of RAG. The pipeline is modular, allowing team members to work on individual components without interfering with other parts of the system.

## Setup

### Clone the repository:

```bash
git clone <repo-url>
cd <repo-name>
```

### Install dependencies using uv:

```bash
uv sync
```

### Start the development environment:

```bash
dg dev
```

## Configuration
The pipeline is designed to generalize across different retrieval scenarios. Configuration is managed through a config.toml file, which can be placed in one of the following locations (checked in order):

1. $RAG_CONFIG

2. ~/.config/rag-openheidelberg/config.toml

3. $DAGSTER_HOME/configs/rag-openheidelberg/config.toml

4. /etc/rag-openheidelberg/config.toml

5. /usr/local/etc/rag-openheidelberg/config.toml

This allows for flexible setup depending on user preferences and environment requirements.