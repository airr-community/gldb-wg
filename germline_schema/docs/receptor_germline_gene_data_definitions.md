# Receptor Germline Gene Definitions

Data Items required to document receptor germline genes, including the information from which it was inferred, and its delineation according to different numbering schemes.

## Germline Set

The germline genes observed in a particular species or type

| Name | Type | Description |
| --- | --- | --- |
| `release_version` | number | Version number of this record, allocated automatically |
| `pub_ids` | list of PubMed ids | Peer-reviewed publications describing this dataset |
| `author` | name | Corresponding author |
| `release_date` | date | Date of this release |
| `lab_name` | string | Department of corresponding author |
| `lab_address` | string | Institutional address of corresponding author |
| `release_description` | string | Brief descriptive notes of the reason for this release and the changes embodied |
| `organism` | string | Binomial designation of subject's species |
| `notes` | string | None |

## Germline Description

The description of a single gene.

| Name | Type | Description |
| --- | --- | --- |
| `sequence` | IUPAC nucleotide notation | nt sequence of the gene. This should cover the full length that is available, including where possible 5' UTR and lead-in for V-gene sequences |
| `codon_frame` | [1, 2, 3] | Codon position of the first sequence symbol. Mandatory for J genes and V genes. Not used for D genes. ('1' means the sequence is in-frame, '2' means that the first bp is missing from the first codon, '3' means that the first 2 bp are missing) |
| `inference class` | ['Genomic and Rearranged', 'Genomic Only', 'Rearranged Only'] | Class of sequence(s) from which this gene was inferred |
| `locus` | ['Heavy', 'Light-Kappa or Light-Lambda for B-cell sequences', 'or Alpha', 'Beta or Gamma for T-cell sequences'] | Gene locus |
| `l_region_start` | integer | Start coordinate of L region |
| `release_version` | number | Version number of this record, allocated automatically |
| `3_prime_d_rs_end` | integer | End coordinate of 3 prime D recombination site (D-genes only) |
| `j_rs_start` | integer | Start coordinate of J recombination site (J-genes only) |
| `release_description` | string | Brief descriptive notes of the reason for this release and the changes embodied |
| `confidence` | ['Red', 'Amber', 'Green'] | Curator's measure of confidence in the inference of this gene, possibly related to its inference class |
| `author` | name | Corresponding author |
| `v_rs_end` | integer | End coordinate of V recombination site (V-genes only) |
| `lab_name` | string | Department of corresponding author |
| `3_prime_d_rs_start` | integer | Start coordinate of 3 prime D recombination site (D-genes only) |
| `functionality` | ['Functional', 'Nonfunctional'] | Functionality |
| `j_rs_end` | integer | End coordinate of J recombination site (J-genes only) |
| `deprecation_reason` | string | If deprecated, the reason for deprecation |
| `status` | ['Active', 'Deprecated', 'Novel'] | Deprecated sequences are those that have been superceded or removed because of errors or uncertainty. Novel sequences are those that have not been fully scrutinised. Others are Active. |
| `pub_ids` | list of PubMed ids | Peer-reviewed publications describing this dataset |
| `genomic_sequences` | string | IDs of 0 or more Genomic_Sequence records |
| `paralogs` | list of strings | Canonical names of 0 or more paralogs |
| `v_rs_start` | integer | Start coordinate of V recombination site (V-genes only) |
| `allele_designation` | string | Allele designation |
| `l_region_end` | integer | End coordinate of L region |
| `5_prime_d_rs_end` | integer | End coordinate of 5 prime D recombination site (D-genes only) |
| `region` | ['V', 'D', 'J', 'C'] | Gene region |
| `5_prime_utr_end` | integer | End coordinate of 5 prime UTR |
| `gene_subgroup` | string | Gene subgroup (family), as identified for this species |
| `5_prime_d_rs_start` | integer | Start coordinate of 5 prime D recombination site (D-genes only) |
| `notes` | string | None |
| `subgroup_designation` | string | Gene designation within this subgroup |
| `alt_names` | strings | Alternative names for this gene |
| `5_prime_utr_start` | integer | Start coordinate of 5 prime UTR |
| `lab_address` | string | Institutional address of corresponding author |
| `observed_sequences` | string | IDs of 0 or more Observed_Sequence records |
| `organism` | string | Binomial designation of subject's species |
| `release_date` | date | Date of this release |
| `gene_name` | string | The canonical name of this gene (i.e., the name which the curators determine should be used by preference) |

### Germline Delineation

The delineation of fields, and the numbering of codons, according to a particular scheme

### V-gene Delineation

| Name | Type | Description |
| --- | --- | --- |
| `fwr3_end` | integer | FWR3 end coordinate in Gene Description 'sequence' field |
| `v_start` | integer | Coordinate of first V nucleotide in Gene Description 'sequence' field |
| `fwr1_end` | integer | FWR1 end coordinate in Gene Description 'sequence' field |
| `cdr1_start` | integer | CDR1 start coordinate in Gene Description 'sequence' field |
| `alignment` | list of integers | one number for each codon in the fields v_start to cdr3_start indicating the number of that codon according to the numbering of the delineation scheme |
| `fwr2_end` | integer | FWR2 end coordinate in Gene Description 'sequence' field |
| `delineation_scheme` | string | e.g. Kabat, IMGT, Chothia |
| `v_end` | integer | End coordinate of the V segment in Gene Description 'sequence' field |
| `cdr1_end` | integer | CDR1 end coordinate in Gene Description 'sequence' field |
| `fwr2_start` | integer | FWR2 start coordinate in Gene Description 'sequence' field |
| `gene_release_version` | integer | Version of the Gene Description to which this delineation applies |
| `fwr3_start` | integer | FWR3 start coordinate in Gene Description 'sequence' field |
| `fwr1_start` | integer | FWR1 start coordinate in Gene Description 'sequence' field |
| `cdr2_start` | integer | CDR2 start coordinate in Gene Description 'sequence' field |
| `cdr2_end` | integer | CDR2 end coordinate in Gene Description 'sequence' field |
| `cdr3_start` | integer | CDR3 start coordinate in Gene Description 'sequence' field |
| `gene_name` | name | Canonical name of the gene to which this delineation applies |

### D-gene Delineation

| Name | Type | Description |
| --- | --- | --- |
| `gene_release_version` | integer | Version of the Gene Description to which this delineation applies |
| `gene_name` | name | Canonical name of the gene to which this delineation applies |
| `delineation_scheme` | string | e.g. Kabat, IMGT, Chothia |
| `d_start` | integer | Coordinate of first D nucleotide in Gene Description 'sequence' field |
| `d_end` | integer | End coordinate of the D segment in Gene Description 'sequence' field |

### J-gene Delineation

| Name | Type | Description |
| --- | --- | --- |
| `gene_release_version` | integer | Version of the Gene Description to which this delineation applies |
| `j_end` | integer | End coordinate of the D segment in Gene Description 'sequence' field |
| `delineation_scheme` | string | e.g. Kabat, IMGT, Chothia |
| `cdr3_end` | integer | End coordinate of the CDR3 in Gene Description 'sequence' field |
| `j_start` | integer | Coordinate of first D nucleotide in Gene Description 'sequence' field |
| `gene_name` | name | Canonical name of the gene to which this delineation applies |


## Supporting Sequences

Sequences, either observed in repertoires or genomic in origin, leading to the inference of a gene.


### Observed Sequence

| Name | Type | Description |
| --- | --- | --- |
| `repository_name` | string | Name of the repository in which the sequence has been deposited |
| `derivation` | ['DNA', 'mRNA'] | Material from which the sequence was derived |
| `sequence` | nucleotide sequence | Sequence of interest described in this record |
| `notes` | text | Notes added by IARC |
| `deposited_version` | string | Version number of the sequence within the repository |
| `seq_start` | integer | Start coordinate of the sequence of interest described in this record, within the sequence deposited |
| `seq_end` | integer | End coordinate of the sequence of interest described in this record, within the sequence deposited |
| `sequence_id` | string | IARC unique reference for this sequence observation |
| `repository_id` | string | Id or serial number of the sequence within the repository |
| `observation_type` | string | e.g. direct sequencing, inference from repertoire |

### Genomic Sequence

| Name | Type | Description |
| --- | --- | --- |
| `patch_no` | string | Genome assembly patch number in which this gene was inferred (e.g. p7) |
| `assembly_id` | string | Ensembl identifier of the genome in which this gene was inferred, including build ID (e.g. GRCh38) |
| `notes` | text | Notes added by IARC |
| `gff_start` | integer | Genomic co-ordinates of the start of the sequence of interest described in this record, in Ensemble GFF version 3 |
| `sequence` | nucleotide sequence | Sequence of interest described in this record (typically this will include gene and propoter region) |
| `gff_seqid` | string | Germline sequence (from the genome) of a window including the gene and preferably also the promoter region |
| `sequence_id` | string | IARC unique reference for this sequence observation |
| `gff_end` | integer | Genomic co-ordinates of the end of the sequence of interest described in this record, in Ensemble GFF version 3 |
| `gff_strand` | ['+', '-'] | None |


