python CreateMarkdownDoc.py ../schema/receptor_germline_schema.yaml ../docs/receptor_germline_gene_data_definitions.md ../templates receptor_germline_gene_data_template.j2
python CreateMarkdownDoc.py ../schema/receptor_germline_schema.yaml ../docs/inference_tool_data.md ../templates inference_tool_data.j2
python CreateSubmissionSheet.py ../schema/receptor_germline_schema.yaml ../docs/iarc_submission_sheet.xlsx ../templates/iarc_submission_template.xlsx
python CreateSubmissionSheet.py ../schema/receptor_germline_schema.yaml ../docs/inferred_sequence_documentation_sheet.xlsx ../templates/inferred_sequence_documentation_template.xlsx
