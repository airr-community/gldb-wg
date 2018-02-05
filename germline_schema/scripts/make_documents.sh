jinja2 ../templates/receptor_germline_gene_data_template.j2 ../schema/receptor_germline_schema.yaml >../docs/receptor_germline_gene_data_definitions.md
python CreateSubmissionSheet.py ../schema/receptor_germline_schema.yaml ../docs/iarc_submission_sheet.xlsx ../templates/iarc_submission_template.xlsx
