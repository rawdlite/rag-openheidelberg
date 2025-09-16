import io
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
        response = self.s3_client.get_pdf(asset)

        if not response.get('status') == 'ok':
            asset['storage']['error'] = response.get('msg')
            return asset
        else:
            pdf_content = response.get('pdf_content')
            source = DocumentStream(name=asset['id'], stream=pdf_content)
            doc_converter = DocumentConverter(
                format_options={
                    InputFormat.PDF: PdfFormatOption(pipeline_options=self.pipeline_options)
                }
            )
            conv_result = doc_converter.convert(source)
            markdown = conv_result.document.export_to_markdown()
            self.s3.save_stream(data=markdown,key=asset['id'].replace('.pdf','.md') )