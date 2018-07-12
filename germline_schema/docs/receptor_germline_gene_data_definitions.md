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
| `gene_descriptions` | string | list of one or more Gene_Description records |
| `notes` | string | None |

## Germline Description

The description of a single gene.

| Name | Type | Description |
| --- | --- | --- |
| `description_id` | string | Unique identifier of this gene sequence |
| `author` | name | Corresponding author |
| `lab_name` | string | Department of corresponding author |
| `lab_address` | string | Institutional address of corresponding author |
| `release_version` | number | Version number of this record, updated whenever a revised version is published or released |
| `release_description` | string | Brief descriptive notes of the reason for this release and the changes embodied |
| `release_date` | date | Date of this release |
| `pub_ids` | list of PubMed ids | Peer-reviewed publications describing this inference |
| `organism` | string | Binomial designation of subject's species |
| `sequence_name` | string | The canonical name of this sequence (i.e., the name which the curators determine should be used by preference) |
| `alt_names` | strings | Alternative names for this sequence |
| `locus` | ['Heavy', 'Light-Kappa or Light-Lambda for B-cell sequences', 'or Alpha', 'Beta or Gamma for T-cell sequences'] | Gene locus |
| `domain` | ['V', 'C'] | Sequence domain (Variable or Constant) |
| `functionality` | ['Functional', 'Nonfunctional'] | Functionality |
| `inference_type` | ['Genomic and Rearranged', 'Genomic Only', 'Rearranged Only'] | Type of inference(s) from which this gene sequence was inferred (Genomic and Rearranged, Genomic Only, Rearranged Only) |
| `affirmation_level` | [1, 2, 3] | Count of independent studies in which this allele as been affirmed by IARC (1,2,3 or more) |
| `status` | ['Active', 'Deprecated', 'Novel'] | Deprecated sequences are those that have been superceded or removed because of errors or uncertainty. Novel sequences are those that have not been fully scrutinised. Others are Active. |
| `deprecation_reason` | string | If deprecated, the reason for deprecation |
| `gene_subgroup` | string | Gene subgroup (family), as identified for this species |
| `subgroup_designation` | string | Gene designation within this subgroup |
| `allele_designation` | string | Allele designation |
| `sequence` | IUPAC nucleotide notation | nt sequence of the gene. This should cover the full length that is available, including where possible 5' UTR and lead-in for V-gene sequences |
| `coding_seq_imgt` | sequence | nucleotide sequence of the coding region, aligned, in the case of a V-gene, with the IMGT numbering scheme |
| `codon_frame` | [1, 2, 3] | Codon position of the first sequence symbol in coding_seq_imgt. Mandatory for J genes. Not used for V or D genes. ('1' means the sequence is in-frame, '2' means that the first bp is missing from the first codon, '3' means that the first 2 bp are missing) |
| `j_cdr3_end` | integer | In the case of a J-gene, the co-ordinate (in coding_seq_imgt) of the first nucelotide of the conserved PHE or TRP (IMGT codon position 118) |
| `utr_5_prime_start` | integer | Start co-ordinate of 5 prime UTR |
| `utr_5_prime_end` | integer | End co-ordinate of 5 prime UTR |
| `l_region_start` | integer | Start co-ordinate of L region |
| `l_region_end` | integer | End co-ordinate of L region |
| `v_rs_start` | integer | Start co-ordinate of V recombination site (V-genes only) |
| `v_rs_end` | integer | End co-ordinate of V recombination site (V-genes only) |
| `d_rs_3_prime_start` | integer | Start co-ordinate of 3 prime D recombination site (D-genes only) |
| `d_rs_3_prime_end` | integer | End co-ordinate of 3 prime D recombination site (D-genes only) |
| `d_rs_5_prime_start` | integer | Start co-ordinate of 5 prime D recombination site (D-genes only) |
| `d_rs_5_prime_end` | integer | End co-ordinate of 5 prime D recombination site (D-genes only) |
| `j_rs_start` | integer | Start co-ordinate of J recombination site (J-genes only) |
| `j_rs_end` | integer | End co-ordinate of J recombination site (J-genes only) |
| `paralogs` | list of strings | Canonical names of 0 or more paralogs |
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

