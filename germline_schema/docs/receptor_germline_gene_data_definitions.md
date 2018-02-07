# Receptor Germline Gene Definitions

Data Items required to document receptor germline genes, including the information from which it was inferred, and its delineation according to different numbering schemes.

## Germline Set

The germline genes observed in a particular species or type

| Name | Type | Description |
| --- | --- | --- |
| `author` | name | Corresponding author |
| `lab_name` | string | Department of corresponding author |
| `lab_address` | string | Institutional address of corresponding author |
| `release_version` | number | Version number of this record, allocated automatically |
| `release_description` | string | Brief descriptive notes of the reason for this release and the changes embodied |
| `release_date` | date | Date of this release |
| `pub_ids` | list of PubMed ids | Peer-reviewed publications describing this dataset |
| `organism` | string | Binomial designation of subject's species |
| `notes` | string | None |

## Germline Description

The description of a single gene.

| Name | Type | Description |
| --- | --- | --- |
| `author` | name | Corresponding author |
| `lab_name` | string | Department of corresponding author |
| `lab_address` | string | Institutional address of corresponding author |
| `release_version` | number | Version number of this record, allocated automatically |
| `release_description` | string | Brief descriptive notes of the reason for this release and the changes embodied |
| `release_date` | date | Date of this release |
| `pub_ids` | list of PubMed ids | Peer-reviewed publications describing this dataset |
| `organism` | string | Binomial designation of subject's species |
| `gene_name` | string | The canonical name of this gene (i.e., the name which the curators determine should be used by preference) |
| `alt_names` | strings | Alternative names for this gene |
| `locus` | ['Heavy', 'Light-Kappa or Light-Lambda for B-cell sequences', 'or Alpha', 'Beta or Gamma for T-cell sequences'] | Gene locus |
| `region` | ['V', 'D', 'J', 'C'] | Gene region |
| `functionality` | ['Functional', 'Nonfunctional'] | Functionality |
| `inference class` | ['Genomic and Rearranged', 'Genomic Only', 'Rearranged Only'] | Class of sequence(s) from which this gene was inferred |
| `confidence` | ['Red', 'Amber', 'Green'] | Curator's measure of confidence in the inference of this gene, possibly related to its inference class |
| `status` | ['Active', 'Deprecated', 'Novel'] | Deprecated sequences are those that have been superceded or removed because of errors or uncertainty. Novel sequences are those that have not been fully scrutinised. Others are Active. |
| `deprecation_reason` | string | If deprecated, the reason for deprecation |
| `gene_subgroup` | string | Gene subgroup (family), as identified for this species |
| `subgroup_designation` | string | Gene designation within this subgroup |
| `allele_designation` | string | Allele designation |
| `sequence` | IUPAC nucleotide notation | nt sequence of the gene. This should cover the full length that is available, including where possible 5' UTR and lead-in for V-gene sequences |
| `codon_frame` | [1, 2, 3] | Codon position of the first sequence symbol. Mandatory for J genes and V genes. Not used for D genes. ('1' means the sequence is in-frame, '2' means that the first bp is missing from the first codon, '3' means that the first 2 bp are missing) |
| `5_prime_utr_start` | integer | Start co-ordinate of 5 prime UTR |
| `5_prime_utr_end` | integer | End co-ordinate of 5 prime UTR |
| `l_region_start` | integer | Start co-ordinate of L region |
| `l_region_end` | integer | End co-ordinate of L region |
| `v_rs_start` | integer | Start co-ordinate of V recombination site (V-genes only) |
| `v_rs_end` | integer | End co-ordinate of V recombination site (V-genes only) |
| `3_prime_d_rs_start` | integer | Start co-ordinate of 3 prime D recombination site (D-genes only) |
| `3_prime_d_rs_end` | integer | End co-ordinate of 3 prime D recombination site (D-genes only) |
| `5_prime_d_rs_start` | integer | Start co-ordinate of 5 prime D recombination site (D-genes only) |
| `5_prime_d_rs_end` | integer | End co-ordinate of 5 prime D recombination site (D-genes only) |
| `j_rs_start` | integer | Start co-ordinate of J recombination site (J-genes only) |
| `j_rs_end` | integer | End co-ordinate of J recombination site (J-genes only) |
| `paralogs` | list of strings | Canonical names of 0 or more paralogs |
| `observed_sequences` | string | IDs of 0 or more Observed_Sequence records |
| `genomic_sequences` | string | IDs of 0 or more Genomic_Sequence records |
| `notes` | string | None |

### Germline Delineation

The delineation of fields, and the numbering of codons, according to a particular scheme

### V-gene Delineation

| Name | Type | Description |
| --- | --- | --- |
| `gene_name` | name | Canonical name of the gene to which this delineation applies |
| `gene_release_version` | integer | Version of the Gene Description to which this delineation applies |
| `delineation_scheme` | string | e.g. Kabat, IMGT, Chothia |
| `v_start` | integer | Co-ordinate of first V nucleotide in Gene Description 'sequence' field |
| `v_end` | integer | End co-ordinate of the V segment in Gene Description 'sequence' field |
| `fwr1_start` | integer | FWR1 start co-ordinate in Gene Description 'sequence' field |
| `fwr1_end` | integer | FWR1 end co-ordinate in Gene Description 'sequence' field |
| `cdr1_start` | integer | CDR1 start co-ordinate in Gene Description 'sequence' field |
| `cdr1_end` | integer | CDR1 end co-ordinate in Gene Description 'sequence' field |
| `fwr2_start` | integer | FWR2 start co-ordinate in Gene Description 'sequence' field |
| `fwr2_end` | integer | FWR2 end co-ordinate in Gene Description 'sequence' field |
| `cdr2_start` | integer | CDR2 start co-ordinate in Gene Description 'sequence' field |
| `cdr2_end` | integer | CDR2 end co-ordinate in Gene Description 'sequence' field |
| `fwr3_start` | integer | FWR3 start co-ordinate in Gene Description 'sequence' field |
| `fwr3_end` | integer | FWR3 end co-ordinate in Gene Description 'sequence' field |
| `cdr3_start` | integer | CDR3 start co-ordinate in Gene Description 'sequence' field |
| `alignment` | list of integers | one number for each codon in the fields v_start to cdr3_start indicating the number of that codon according to the numbering of the delineation scheme |

### D-gene Delineation

| Name | Type | Description |
| --- | --- | --- |
| `gene_name` | name | Canonical name of the gene to which this delineation applies |
| `gene_release_version` | integer | Version of the Gene Description to which this delineation applies |
| `delineation_scheme` | string | e.g. Kabat, IMGT, Chothia |
| `d_start` | integer | Co-ordinate of first D nucleotide in Gene Description 'sequence' field |
| `d_end` | integer | End co-ordinate of the D segment in Gene Description 'sequence' field |

### J-gene Delineation

| Name | Type | Description |
| --- | --- | --- |
| `gene_name` | name | Canonical name of the gene to which this delineation applies |
| `gene_release_version` | integer | Version of the Gene Description to which this delineation applies |
| `delineation_scheme` | string | e.g. Kabat, IMGT, Chothia |
| `j_start` | integer | Co-ordinate of first D nucleotide in Gene Description 'sequence' field |
| `j_end` | integer | End co-ordinate of the D segment in Gene Description 'sequence' field |
| `cdr3_end` | integer | End co-ordinate of the CDR3 in Gene Description 'sequence' field |


## Supporting Sequences

Sequences, either observed in repertoires or genomic in origin, leading to the inference of a gene.


### Observed Sequence

| Name | Type | Description |
| --- | --- | --- |
| `sequence_id` | string | IARC unique reference for this sequence observation |
| `sequence` | nucleotide sequence | Sequence of interest described in this record |
| `derivation` | ['DNA', 'mRNA'] | Material from which the sequence was derived |
| `observation_type` | string | e.g. direct sequencing, inference from repertoire |
| `notes` | text | Notes added by IARC |
| `repository_name` | string | Name of the repository in which the sequence has been deposited |
| `repository_id` | string | Id or serial number of the sequence within the repository |
| `deposited_version` | string | Version number of the sequence within the repository |
| `seq_start` | integer | Start co-ordinate of the sequence of interest described in this record, within the sequence deposited |
| `seq_end` | integer | End co-ordinate of the sequence of interest described in this record, within the sequence deposited |

### Genomic Sequence

| Name | Type | Description |
| --- | --- | --- |
| `sequence_id` | string | IARC unique reference for this sequence observation |
| `sequence` | nucleotide sequence | Sequence of interest described in this record (typically this will include gene and propoter region) |
| `notes` | text | Notes added by IARC |
| `assembly_id` | string | Ensembl identifier of the genome in which this gene was inferred, including build ID (e.g. GRCh38) |
| `patch_no` | string | Genome assembly patch number in which this gene was inferred (e.g. p7) |
| `gff_seqid` | string | Germline sequence (from the genome) of a window including the gene and preferably also the promoter region |
| `gff_start` | integer | Genomic co-ordinates of the start of the sequence of interest described in this record, in Ensemble GFF version 3 |
| `gff_end` | integer | Genomic co-ordinates of the end of the sequence of interest described in this record, in Ensemble GFF version 3 |
| `gff_strand` | ['+', '-'] | None |

