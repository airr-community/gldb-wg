# AIRR Germline Schema
The [schema](schema/receptor_germline_schema.yaml) defines the data elements necessary to describe a receptor germline gene, including the supporting information that was used to infer the gene, and to describe 'germline sets' - collections of genes deemed to be representative of particular species, or human racial types.

Documents created from the schema are, currently:

- A [Germline Description](docs/receptor_germline_gene_data_definitions.md), defining the data elements in human-readable form
- A [Submission Sheet](docs/iarc_submission_sheet.xlsx), used to submit alleles inferred from germline repertoires to IARC for consideration.

*Note*: these documents are currently in draft and under review. The submission form is not in use yet. For current submissions, please refer to IARC for guidance.

##Building the documents##

The documents are built from [templates](templates/) using [scripts](scripts/). Running [make_documents.sh](scripts/make_documents.sh) in the scripts directory from Linux or Windows will recreate them.

Prerequisites:
- Python 3
- PyYAML
- Jinja2
- Jinja2-cli

*Note:* Version 2.9.0 of Jinja (current at the time of writing) seems to break on Windows when used with Jinja2-cli. Until the current version is updated, please install the development version: pip install https://github.com/pallets/jinja/zipball/master .   
