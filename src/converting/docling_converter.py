import datetime
from converting.converter import Converter
from docling.datamodel.base_models import InputFormat, DocumentStream
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import (
    AcceleratorDevice,
    AcceleratorOptions,
    PdfPipelineOptions,
)


class DoclingConverter(Converter):
    
    def __init__(self):
        super().__init__()
        pipeline_options = PdfPipelineOptions()
        pipeline_options.do_ocr = True
        pipeline_options.do_table_structure = True
        pipeline_options.table_structure_options.do_cell_matching = True
        pipeline_options.ocr_options.lang = ["de"]
        pipeline_options.accelerator_options = AcceleratorOptions(
            num_threads=1, device=AcceleratorDevice.AUTO
        )
        self.pipeline_options = pipeline_options
        
        
    def process(self):
        assets = self.get_assets()
        for asset in assets:
            doc = self.transform(asset)
            self.save_asset(doc)
            
    def transform(self, asset: dict) -> dict:
        """_summary_
        convert a pdf to markdown
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
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            source = DocumentStream(name=f"{asset['id']}.pdf", stream=pdf_content)
            doc_converter = DocumentConverter(
                format_options={
                    InputFormat.PDF: PdfFormatOption(pipeline_options=self.pipeline_options)
                }
            )
            try:
                conv_result = doc_converter.convert(source)
            except Exception as e:
                asset['storage']['md'] = {'error': str(e), 'created_at': now}
                return asset
            markdown = conv_result.document.export_to_markdown()
            key = f"{asset['id']}.md"
            
            self.s3_client.save_stream(data=markdown,key=key)
            asset['storage']['md'] = {'path': f"s3://{self.s3_bucket._name}/{key}",
                                      'created_at': now}
            return asset

def main():
    converter = DoclingConverter()
    converter.process()
    
if __name__ == '__main__':
    main()