.. _GermlineSchema:

Germline Sets
=============

Motivation
==========

Understanding and cataloguing receptor germline genes and allele sequences is critical to the analysis of AIRR data.
While the human set is relatively well understood in outline, although probably still far from complete, that
of other species, even those that are relatively closely studied, is at a much earlier stage. There is an
urgent need to define a standardised format for listing such genes, so that they can be shared between researchers
and easily consumed by software tools.

Receptor Germline Schema
=============================

The receptor germline schema defines the data elements necessary to describe one or more receptor germline
genes, together with supporting evidence. The fundamental object is the ``GeneDescription``, which describes a
single gene or allele, containing the necessary details for the annotation of a rearranged sequence. ``GeneDescription``
also contains fields to delineate the RSS and leader regions of V, D and J genes, should those regions be covered
by the sequence provided.

Evidence supporting the gene or allele can be provided in linked ``GenomicSequence`` and ``RearrangedSequence``
objects. Information represented in these objects will typically be
stored in a repository: either an INSDC repository such as Genbank or SRA, or a lower-tier repository such as
OGRDB.

For V-genes, an IMGT-aligned sequence is provided in ``GeneDescription``. Other delineations can be provided via linked
``GeneDelineationV`` objects.

A ``GermlineSet`` brings together multiple ``GeneDescriptions`` to form a
curated set.

Gene and Allele Naming
======================

The International Union of Immunological Societies allocates gene symbols for receptor genes. ``GeneDescription``
contains a ``gene_symbol`` field, but it is optional, recognising that a symbol may not have been
assigned. Gene symbols are long-lasting, but the underlying sequence may be revised over time. ``GeneDescription``
contains a mandatory ``coding_sequence_identifier``, which will be updated should the sequence change. It is anticipated
that publishers of gene sets will provide mechanisms to issue these identifiers, and to allow researchers to
review change history of ``GeneDescriptions`` and ``GermlineSets``. In the interests of consistency and transparency,
when referring to a gene or allele, the ``gene_symbol`` should be used wherever possible, however
``coding_sequence_identifier`` provides a fallback where a gene symbol has not been assigned.





