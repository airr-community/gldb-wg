# Inference Tool Output For Inferred Gene Submissions #

The Inferred Allele Review Committee expects to review a large number of submissions. To help with this work, we would like to understand
the information provided by inference tools as part of each inferred novel allele. 

IARC recognises that tools will vary in the approach and algorithms employed: therefore we indicate here the nature of the information that 
is of value to the Committee, and ask tool providers to say whether or not each item is provided by their tool, and to provide any notes
on the way or form in which it is provided. We also ask tool providers to list any additional information provided by their tool which is 
likely to be helpful.

Please provide information on your tool by completing the tables below. These cover:

- Overview information on the tool
- Information provided by the tool for each inferred allele
- Information provided by the tool on the entire genotype from which inferences were made
- Information on the identity, version and configuration of the tool used to construct the inferences.

## Overview Information ##

| Item | Description | Response |
| --- | --- | --- |
| `tool_name` | Name of the inference tool |                                           |
| `tool_version` | Version of the inference tool for which this information was submitted |                                           |
| `submitter_name` | Name of the person submitting tool information |                                           |
| `submitter_address` | Email address of the person submitting tool information |                                           |

## Information on Each Inferred Allele ##

| Name | Description | Provided by tool? | Comments |
| --- | --- | --- | --- |
| `sequence_id` |  Identifier of the allele, issued by the submitter (need not follow any particular format) |          |                                     |
| `sequences` |  Overall number of sequences assigned to this allele |          |                                     |
| `closest_reference` |  The closest reference gene and allele, as inferred by the tool |          |                                     |
| `closest_host` |  The closest reference gene and allele that is in the subject's inferred genotype, as inferred by the tool |          |                                     |
| `nt_diff` |  Number of nucleotides that differ between this sequence and the closest reference gene and allele |          |                                     |
| `nt_substitutions` |  List of nucleotide substitutions (e.g. G112A) between this sequence and the closest reference gene and allele |          |                                     |
| `aa_diff` |  Number of amino acids that differ between this sequence and the closest reference gene and allele |          |                                     |
| `aa_substitutions` |  List of amino acid substitutions (e.g. A96N) between this sequence and the closest reference gene and allele |          |                                     |
| `unmutated_frequency` |  The proportion of records in the sequence dataset matching this unmutated sequence |          |                                     |
| `unmutated_sequences` |  The number of records in the sequence dataset exactly matching this unmutated sequence |          |                                     |
| `allelic_percentage` |  The percentage at which this allele was observed in the sequence dataset, compared to other alleles |          |                                     |
| `unique_ds` |  Number of unique D sequences found associated with the inferred V sequence |          |                                     |
| `unique_js` |  Number of unique J sequences found associated with the inferred V sequence |          |                                     |
| `unique_cdr3s` |  Number of unique CDR3s found associated with the inferred V sequence |          |                                     |
| `haplotyping_locus` |  Locus (or loci) from which haplotyping was inferred (e.g. IGHJ6) |          |                                     |
| `haplotyping_ratio` |  Ratio (expressed as two percentages) with which the two inferred haplotypes were found (e.g. 60:40) |          |                                     |
| `nt_sequence` |  The consensus sequence provided by the inference tool |          |                                     |
| `phred_score` |  phred string (FASTQ format) for the consensus contig from which this nt sequence was inferred |          |                                     |
| `repository_name` |  Name of the repository in which the sequence has been deposited |          |                                     |
| `repository_id` |  Id or serial number of the sequence within the repository |          |                                     |
| `deposited_version` |  Version number of the sequence within the repository |          |                                     |
| `IARC_tracking` |  Notes from IARC tracking overall progress of this submission, eg additional info requested, when reviewed, etc |          |                                     |
|    | Can the above information be provided by the tool in .csv or similar format? |   |    |
 
## Information on Entire Genotyope Used for Inference ##

| Name | Description | Provided by tool? | Comments |
| --- | --- | --- | --- |
| `sequence_id` | Identifier of the allele (either IMGT, or the name assigned by the submitter to an inferred gene) |          |                                     |
| `subject_id` | Identifier of the subject from which this genotype was inferred (please provide separate genotypes for each subject) |          |                                     |
| `sequences` | Overall number of sequences assigned to this allele |          |                                     |
| `closest_reference` | For inferred alleles, the closest reference gene and allele, based on percent identity |          |                                     |
| `closest_host` | For inferred alleles, the closest reference gene and allele that is in the subject's inferred genotype, based on percent identity |          |                                     |
| `nt_diff` | For inferred alleles, the number of nucleotides that differ between this sequence and the closest reference gene and allele |          |                                     |
| `aa_diff` | For inferred alleles, the number of amino acids that differ between this sequence and the closest reference gene and allele |          |                                     |
| `cigar` | For inferred alleles, the alignment between this sequence and the closest reference gene and allele (CIGAR string) |          |                                     |
| `unmutated_frequency` | The proportion of records in the sequence dataset matching this unmutated sequence |          |                                     |
| `unmutated_sequences` | The number of records in the sequence dataset exactly matching this unmutated sequence |          |                                     |
| `allelic_percentage` | The percentage at which this allele was observed in the sequence dataset, compared to other alleles |          |                                     |
| `unique_ds` | Number of unique D sequences found associated with the inferred V sequence |          |                                     |
| `unique_js` | Number of unique J sequences found associated with the inferred V sequence |          |                                     |
| `unique_cdr3s` | Number of unique CDR3s found associated with the inferred V sequence |          |                                     |
| `haplotyping_locus` | Locus (or loci) from which haplotyping was inferred (e.g. IGHJ6) |          |                                     |
| `haplotyping_ratio` | Ratio (expressed as two percentages) with which the two inferred haplotypes were found (e.g. 60:40) |          |                                     |
| `nt_sequence` | The consensus sequence provided by the inference tool |          |                                     |
|    | Can the above information be provided by the tool in .csv or similar format? |   |    |

## Tool And Settings ##

| Name | Description | Provided by tool? | Comments |
| --- | --- | --- | --- |
| `software_name` | string | Name of the tool used to produce these inferences |
| `software_version` | string | Version number and / or date |
| `reference_germline_set` | string | Name or description of the germline set used by the tool |
| `reference_germline_version` | string | Version number and / or date |
| `software_settings` | dictionary | Dictionary of setting types and values specific to this software tool |
|    | Can the above information be generated automatically by the tool in .csv or similar format? |   |    |