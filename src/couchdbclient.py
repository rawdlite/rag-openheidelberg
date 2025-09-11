from config import Config
import couchdb2
import os
from typing import List, Dict, Any, Optional

DEBUG = os.getenv("DEBUG", "0") in ("1", "true", "True")

class Client:
    """
    A simple CouchDB client to interact with a CouchDB database.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the CouchDB client.
        Loads configuration from the Config class.
        """
        self.config = config or Config().get('couchdb')
        couchdb_server = self.config.get('couchdb_server') or "localhost:5984"
        couchdb_username = self.config.get('couchdb_username') or ''
        couchdb_password = self.config.get('couchdb_password') or ''
        database_name = self.config.get('couchdb_db')
        if not database_name:
            raise ValueError("CouchDB database name must be specified in the configuration.")
        server_url = f"https://{couchdb_server}"
        if DEBUG:
            print(f"**couch config**: {self.config}")
        self.server = couchdb2.Server(
            username=couchdb_username,
            password=couchdb_password,
            href=server_url
        )
        self.db = self.server[database_name]

    @staticmethod
    def mango_filter_by_type(doc_type: str) -> dict:
        """
        Return a Mango filter (selector) for documents with a specific doc_type.
        Example usage: db.find(Client.mango_filter_by_typel('pdf'))
        """
        return {"type": {"$eq": doc_type}}
    

    def get_all_docs(self) -> List[Dict[str, Any]]:
        """
        Fetch all documents from the CouchDB database excluding design documents.
        Returns:
            List of all documents in the database
        """
        rows = self.db.view(designname='app', viewname='all_entries', include_docs=True)
        return [row.doc for row in rows if not row.id.startswith('_design/')]
