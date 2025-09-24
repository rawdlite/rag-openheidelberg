from categorizing.categorizer import Categorizer
from pypdf import PdfReader

class PDFParser(Categorizer):
    """Class for parsing and categorizing PDF files"""

    def __init__(self):
        super().__init__()
        
    def process(self):
        assets = self.get_assets()
        for asset in assets:
            doc = self.transform(asset)
            self.save_asset(doc)
            
    def transform(self, asset: dict) -> dict:
        """_summary_
        categorize a pdf
        Args:
            asset (dict): _description_

        Returns:
            dict: _description_
        """
        print(f"Processing asset {asset['_id']}")
        response = self.s3_client.get_pdf(asset)

        if not response.get('status') == 'ok':
            asset['storage']['error'] = response.get('msg')
            return asset
        else:
            pdf_content = response.get('pdf_content')
            reader = PdfReader(pdf_content)
            if reader.metadata:
                asset['metadata'] = {k[1:]: v for k, v in reader.metadata.items() if type(v).__name__ == 'TextStringObject'}
            return asset
        
def main():
    parser = PDFParser()
    parser.process()

if __name__ == '__main__':
    main()