from config import Config
import couchdb2
import os
from typing import List, Dict, Any, Optional

DEBUG = os.getenv("DEBUG", "0") in ("1", "true", "True")
VIEWS = {"views": {
            "all_entries": {
                "map": '''function (doc) {
                    if (!doc._id.startsWith('_design/')) { 
                        emit(doc.id, doc); 
                        }}'''
            },
            'not_run': {
                "map": '''function (doc) {
                    if (
                        doc._id &&
                        doc._id.indexOf("_design") !== 0 && // exclude design docs
                        doc.retrieval &&
                        doc.retrieval.last_run === null
                    ) {
                    emit(doc._id, null);
                    }
                }'''
            },
            'not_converted': {
                "map": '''function (doc) {
                    var noMD =
                        doc.storage &&
                        doc.storage.pdf && 
                        typeof doc.storage.md === "undefined";
                    var mdEmptyPath =
                        doc.storage &&
                        doc.storage.md &&
                        (
                            doc.storage.md.path === "" ||
                            doc.storage.md.path === null ||
                            typeof doc.storage.md.path === "undefined"
                        );

                    if (noMD || mdEmptyPath) {
                        emit(doc._id, null);
                    }}'''
            }
        }
}

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
        return self.db.view(designname='app', viewname='all_entries', include_docs=True)
    
    def get_all_unrun_docs(self,limit: int = None,skip: int = None) -> List[Dict[str, Any]]:
        """
        Fetch all documents from couchdb that are not run yet
        """
        return self.db.view(designname='app', viewname='not_run', include_docs=True, limit=limit, skip=skip)
    
    def get_all_unconverted_docs(self, limit: int = None, skip: int = None) -> List[Dict[str, Any]]:
        """
        Fetch all documents not converted

        Args:
            limit (int, optional): _description_. Defaults to None.
            skip (int, optional): _description_. Defaults to None.

        Returns:
            List[Dict[str, Any]]: _description_
        """
        return self.db.view(designname='app', viewname='not_converted', include_docs=True, limit=limit, skip=skip)

    def create_views(self):
        self.db.put_design('app', VIEWS)