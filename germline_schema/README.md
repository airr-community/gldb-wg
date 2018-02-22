# AIRR Germline Data Formats

The AIRR Germline Database Working Group is defining data and formats that will support:

- The submission and review of new receptor germline genes and alleles that have been inferred from germline repertoires
- The definition and curation of germline sets - i.e., collections of genes deemed to be representative of particular species, or human racial types.

The required data elements are defined in a [schema](schema/receptor_germline_schema.yaml). The schema is used to create the following documents:

- A [Submission Sheet](docs/iarc_submission_sheet.xlsx), used to submit alleles inferred from germline repertoires to IARC for consideration.
- [Guidelines for Inference Tool Developers](docs/inference_tool_data.md) that are intended to facilitate the provision of information that will support submissions, in a convenient format.
- A [Germline Description](docs/receptor_germline_gene_data_definitions.md), defining the data elements underlying the definition of a germline gene and a germline set, in human-readable form

*Note*: these documents are currently in draft and under review. The submission form is not in use yet. For current submissions, please refer to IARC for guidance.

## Building the documents

The documents are built from [templates](templates/) using [scripts](scripts/). Running [make_documents.sh](scripts/make_documents.sh) in the scripts directory from Linux or Windows will recreate them.

Prerequisites:
- Python 3
- PyYAML
- Jinja2
- Jinja2-cli

*Note:* Version 2.9.0 of Jinja (current at the time of writing) seems to break on Windows when used with Jinja2-cli. Until the current version is updated, please install the development version: pip install https://github.com/pallets/jinja/zipball/master .   
