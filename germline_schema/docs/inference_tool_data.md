# Inference Tool Output To Support Inferred Gene Submissions #

The AIRR Germline Database Working Group believes that the submission and review of inferred alleles would be facilitated by the automated 
provision of supporting information from inference tools. We see benefit in identifying and codifying information that is likely to be of 
value; however we recognise that tools vary in the approach and algorithms employed: therefore not every tool can be expected to provide all 
the identified information, and tools are likely to provide other information in addition to that listed here which would also be helpful
in analysis.

Inference Tool providers are encouraged to:

- Provide as much of the information listed below, in the format specified, as is reasonable, given the capability and approach of their tools
- Provide any additional information that is likely to be helpful to reviewers, in an equivalent format.

The information is structured into three groups, covering information on:

- Each inferred allele
- The entire genotype from which inferences were made
- The identity, version and configuration of the tool used to construct the inferences.

These are covered in more detail below.

## Information on Each Inferred Allele ##

This should be provided in CSV format.

| Name | Type | Description |
| --- | --- | --- |
| `sequence_id` | string | Identifier of the allele, issued by the submitter (need not follow any particular format) |
| `sequences` | integer | Overall number of sequences assigned to this allele |
| `closest_reference` | string | The closest reference gene and allele, based on percent identity |
| `closest_host` | string | The closest reference gene and allele that is in the subject's inferred genotype, based on percent identity |
| `nt_diff` | integer | Number of nucleotides that differ between this sequence and the closest reference gene and allele |
| `aa_diff` | integer | Number of amino acids that differ between this sequence and the closest reference gene and allele |
| `cigar` | string | Alignment between this sequence and the closest reference gene and allele (CIGAR string) |
| `unmutated_frequency` | number | The proportion of records in the sequence dataset matching this unmutated sequence |
| `unmutated_sequences` | integer | The number of records in the sequence dataset exactly matching this unmutated sequence |
| `allelic_percentage` | number | The percentage at which this allele was observed in the sequence dataset, compared to other alleles |
| `unique_ds` | integer | Number of unique D sequences found associated with the inferred V sequence |
| `unique_js` | integer | Number of unique J sequences found associated with the inferred V sequence |
| `unique_cdr3s` | integer | Number of unique CDR3s found associated with the inferred V sequence |
| `haplotyping_locus` | string | Locus (or loci) from which haplotyping was inferred (e.g. IGHJ6) |
| `haplotyping_ratio` | string | Ratio (expressed as two percentages) with which the two inferred haplotypes were found (e.g. 60:40) |
| `nt_sequence` | IUPAC nucleotide notation | The consensus sequence provided by the inference tool |
| `phred_score` | string (phred format) | phred string (FASTQ format) for the consensus contig from which this nt sequence was inferred |
| `repository_name` | string | Name of the repository in which the sequence has been deposited |
| `repository_id` | string | Id or serial number of the sequence within the repository |
| `deposited_version` | string | Version number of the sequence within the repository |
| `IARC_tracking` | list of timestamped strings | Notes from IARC tracking overall progress of this submission, eg additional info requested, when reviewed, etc |
 
## Information on Entire Genotyope Used for Inference ##

This should be provided in CSV format.

| Name | Type | Description |
| --- | --- | --- |
| `sequence_id` | string | Identifier of the allele (either IMGT, or the name assigned by the submitter to an inferred gene) |
| `subject_id` | string | Identifier of the subject from which this genotype was inferred (please provide separate genotypes for each subject) |
| `sequences` | integer | Overall number of sequences assigned to this allele |
| `closest_reference` | string | For inferred alleles, the closest reference gene and allele, based on percent identity |
| `closest_host` | string | For inferred alleles, the closest reference gene and allele that is in the subject's inferred genotype, based on percent identity |
| `nt_diff` | integer | For inferred alleles, the number of nucleotides that differ between this sequence and the closest reference gene and allele |
| `aa_diff` | integer | For inferred alleles, the number of amino acids that differ between this sequence and the closest reference gene and allele |
| `cigar` | string | For inferred alleles, the alignment between this sequence and the closest reference gene and allele (CIGAR string) |
| `unmutated_frequency` | number | The proportion of records in the sequence dataset matching this unmutated sequence |
| `unmutated_sequences` | integer | The number of records in the sequence dataset exactly matching this unmutated sequence |
| `allelic_percentage` | number | The percentage at which this allele was observed in the sequence dataset, compared to other alleles |
| `unique_ds` | integer | Number of unique D sequences found associated with the inferred V sequence |
| `unique_js` | integer | Number of unique J sequences found associated with the inferred V sequence |
| `unique_cdr3s` | integer | Number of unique CDR3s found associated with the inferred V sequence |
| `haplotyping_locus` | string | Locus (or loci) from which haplotyping was inferred (e.g. IGHJ6) |
| `haplotyping_ratio` | string | Ratio (expressed as two percentages) with which the two inferred haplotypes were found (e.g. 60:40) |
| `nt_sequence` | nucleotide sequence | The consensus sequence provided by the inference tool |

## Tool And Settings ##

This should be provided in yaml format (see SoftwareProcessing schema in ../schema/receptor_germline_schema.yaml)

| Name | Type | Description |
| --- | --- | --- |
| `software_name` | string | Name of the tool used to produce these inferences |
| `software_version` | string | Version number and / or date |
| `reference_germline_set` | string | Name or description of the germline set used by the tool |
| `reference_germline_version` | string | Version number and / or date |
| `software_settings` | dictionary | Dictionary of setting types and values specific to this software tool |
