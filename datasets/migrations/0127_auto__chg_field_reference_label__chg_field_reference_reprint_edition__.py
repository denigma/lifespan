# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Reference.label'
        db.alter_column('datasets_reference', 'label', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Reference.reprint_edition'
        db.alter_column('datasets_reference', 'reprint_edition', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Reference.author_address'
        db.alter_column('datasets_reference', 'author_address', self.gf('django.db.models.fields.CharField')(max_length=150, null=True))

        # Changing field 'Reference.notes'
        db.alter_column('datasets_reference', 'notes', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Reference.research_notes'
        db.alter_column('datasets_reference', 'research_notes', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Reference.reviewed_items'
        db.alter_column('datasets_reference', 'reviewed_items', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Reference.caption'
        db.alter_column('datasets_reference', 'caption', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Reference.legal_note'
        db.alter_column('datasets_reference', 'legal_note', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    def backwards(self, orm):

        # Changing field 'Reference.label'
        db.alter_column('datasets_reference', 'label', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Reference.reprint_edition'
        db.alter_column('datasets_reference', 'reprint_edition', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Reference.author_address'
        db.alter_column('datasets_reference', 'author_address', self.gf('django.db.models.fields.CharField')(default='', max_length=150))

        # Changing field 'Reference.notes'
        db.alter_column('datasets_reference', 'notes', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Reference.research_notes'
        db.alter_column('datasets_reference', 'research_notes', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Reference.reviewed_items'
        db.alter_column('datasets_reference', 'reviewed_items', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Reference.caption'
        db.alter_column('datasets_reference', 'caption', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Reference.legal_note'
        db.alter_column('datasets_reference', 'legal_note', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

    models = {
        'datasets.acetylation': {
            'Meta': {'object_name': 'Acetylation'},
            'ensembl_gene': ('django.db.models.fields.CharField', [], {'max_length': '9', 'primary_key': 'True'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'h2ak7': ('django.db.models.fields.FloatField', [], {}),
            'h2bk11': ('django.db.models.fields.FloatField', [], {}),
            'h2bk16': ('django.db.models.fields.FloatField', [], {}),
            'h3k14': ('django.db.models.fields.FloatField', [], {}),
            'h3k18': ('django.db.models.fields.FloatField', [], {}),
            'h3k23': ('django.db.models.fields.FloatField', [], {}),
            'h3k27': ('django.db.models.fields.FloatField', [], {}),
            'h3k9': ('django.db.models.fields.FloatField', [], {}),
            'h4k12': ('django.db.models.fields.FloatField', [], {}),
            'h4k16': ('django.db.models.fields.FloatField', [], {}),
            'h4k8': ('django.db.models.fields.FloatField', [], {}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'datasets.adult_height_association': {
            'Meta': {'object_name': 'Adult_Height_Association'},
            'chr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'effect_allele': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'female_effect': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'female_p': ('django.db.models.fields.FloatField', [], {}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locus_rank': ('django.db.models.fields.IntegerField', [], {}),
            'male_effect': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'male_p': ('django.db.models.fields.FloatField', [], {}),
            'phet_m_vs_f': ('django.db.models.fields.FloatField', [], {}),
            'snp': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'datasets.adultcbdynamic': {
            'Meta': {'object_name': 'AdultCbDynamic'},
            'chr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'end': ('django.db.models.fields.IntegerField', [], {}),
            'gene': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_value': ('django.db.models.fields.FloatField', [], {}),
            'peak': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'seq': ('django.db.models.fields.TextField', [], {}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        },
        'datasets.adultcbstable': {
            'Meta': {'object_name': 'AdultCbStable'},
            'chr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'end': ('django.db.models.fields.IntegerField', [], {}),
            'gene': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_value': ('django.db.models.fields.FloatField', [], {}),
            'peak': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'seq': ('django.db.models.fields.TextField', [], {}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        },
        'datasets.adultheightassociation': {
            'Meta': {'object_name': 'AdultHeightAssociation'},
            'chr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'effect_allele': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'female_effect': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'female_p': ('django.db.models.fields.FloatField', [], {}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locus_rank': ('django.db.models.fields.IntegerField', [], {}),
            'male_effect': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'male_p': ('django.db.models.fields.FloatField', [], {}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phet_m_vs_f': ('django.db.models.fields.FloatField', [], {}),
            'snp': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'datasets.adulthippdynamic': {
            'Meta': {'object_name': 'AdultHippDynamic'},
            'chr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'end': ('django.db.models.fields.IntegerField', [], {}),
            'gene': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_value': ('django.db.models.fields.FloatField', [], {}),
            'peak': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'seq': ('django.db.models.fields.TextField', [], {}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        },
        'datasets.adulthippstable': {
            'Meta': {'object_name': 'AdultHippStable'},
            'chr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'end': ('django.db.models.fields.IntegerField', [], {}),
            'gene': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_value': ('django.db.models.fields.FloatField', [], {}),
            'peak': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'seq': ('django.db.models.fields.TextField', [], {}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        },
        'datasets.author': {
            'Meta': {'object_name': 'Author'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'datasets.bmal1_sites_liver': {
            'Meta': {'object_name': 'BMAL1_Sites_Liver'},
            'biotype': ('django.db.models.fields.CharField', [], {'max_length': '23'}),
            'chromosome': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'conservation': ('django.db.models.fields.FloatField', [], {}),
            'distance': ('django.db.models.fields.IntegerField', [], {}),
            'e1': ('django.db.models.fields.IntegerField', [], {}),
            'e1_e2': ('django.db.models.fields.IntegerField', [], {}),
            'end': ('django.db.models.fields.IntegerField', [], {}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '18'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mrna_phase': ('django.db.models.fields.FloatField', [], {}),
            'mrna_pvalue': ('django.db.models.fields.FloatField', [], {}),
            'start': ('django.db.models.fields.IntegerField', [], {}),
            'zt10': ('django.db.models.fields.IntegerField', [], {}),
            'zt14': ('django.db.models.fields.IntegerField', [], {}),
            'zt18': ('django.db.models.fields.IntegerField', [], {}),
            'zt2': ('django.db.models.fields.IntegerField', [], {}),
            'zt22': ('django.db.models.fields.IntegerField', [], {}),
            'zt6': ('django.db.models.fields.IntegerField', [], {})
        },
        'datasets.cbspecific': {
            'Meta': {'object_name': 'CbSpecific'},
            'chr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'end': ('django.db.models.fields.IntegerField', [], {}),
            'gene': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_value': ('django.db.models.fields.FloatField', [], {}),
            'peak': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'seq': ('django.db.models.fields.TextField', [], {}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        },
        'datasets.change': {
            'Meta': {'object_name': 'Change'},
            'comparision': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '250', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'pmid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'references': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['datasets.Reference']", 'symmetrical': 'False', 'blank': 'True'}),
            'start': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'stop': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'taxid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tissue': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        'datasets.circadiansystemicentrainedfactors': {
            'Meta': {'object_name': 'CircadianSystemicEntrainedFactors'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'datasets.clockmodulator': {
            'Meta': {'object_name': 'ClockModulator'},
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'confirmed_by_bmal1_kockdown': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gene_name': ('django.db.models.fields.CharField', [], {'max_length': '152'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phenotype': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'rna_nucleotide_accession_version': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'datasets.dam_fernandez2011': {
            'Meta': {'object_name': 'DAM_Fernandez2011'},
            'cgi': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'correlation': ('django.db.models.fields.FloatField', [], {}),
            'cpg_site': ('django.db.models.fields.CharField', [], {'max_length': '19'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_value': ('django.db.models.fields.FloatField', [], {})
        },
        'datasets.dr_essential': {
            'Meta': {'object_name': 'DR_Essential'},
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'taxid': ('django.db.models.fields.IntegerField', [], {})
        },
        'datasets.gencc': {
            'Meta': {'object_name': 'GenCC'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '68', 'blank': 'True'}),
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'observation': ('django.db.models.fields.CharField', [], {'max_length': '248', 'blank': 'True'}),
            'peak_actvity': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'peak_mrna': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'peak_protein': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'pubmed_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '37', 'blank': 'True'}),
            'taxid': ('django.db.models.fields.IntegerField', [], {})
        },
        'datasets.gendr': {
            'Meta': {'object_name': 'Gendr'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ensembl_gene_id': ('django.db.models.fields.CharField', [], {'max_length': '18', 'blank': 'True'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'gene_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lifespan': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lifespan.Assay']", 'symmetrical': 'False'}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'observation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pubmed_id': ('django.db.models.fields.CharField', [], {'max_length': '87', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'regimen': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lifespan.Regimen']", 'symmetrical': 'False'}),
            'taxid': ('django.db.models.fields.IntegerField', [], {})
        },
        'datasets.hippspecific': {
            'Meta': {'object_name': 'HippSpecific'},
            'chr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'end': ('django.db.models.fields.IntegerField', [], {}),
            'gene': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_value': ('django.db.models.fields.FloatField', [], {}),
            'peak': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'seq': ('django.db.models.fields.TextField', [], {}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        },
        'datasets.humanbraindnamethylationchanges': {
            'Meta': {'object_name': 'HumanBrainDnaMethylationChanges'},
            'adjusted_r2_estimates_from_stage_i_crblm': ('django.db.models.fields.FloatField', [], {}),
            'adjusted_r2_estimates_from_stage_i_fctx': ('django.db.models.fields.FloatField', [], {}),
            'adjusted_r2_estimates_from_stage_i_pons': ('django.db.models.fields.FloatField', [], {}),
            'adjusted_r2_estimates_from_stage_i_tctx': ('django.db.models.fields.FloatField', [], {}),
            'beta_coefficient_range': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'c_g_count': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'chr': ('django.db.models.fields.IntegerField', [], {}),
            'cpg_count': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'cpg_sequence': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cpg_sequence_2kb': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'distance_to_tss': ('django.db.models.fields.IntegerField', [], {}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'genomic_position_in_bp': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'percentage_c_or_g': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'percentage_cpg': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'ratio': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'stage_i_pvalue_crblm': ('django.db.models.fields.FloatField', [], {}),
            'stage_i_pvalue_fctx': ('django.db.models.fields.FloatField', [], {}),
            'stage_i_pvalue_pons': ('django.db.models.fields.FloatField', [], {}),
            'stage_i_pvalue_tctx': ('django.db.models.fields.FloatField', [], {}),
            'stage_ii_pvalue_crblm': ('django.db.models.fields.FloatField', [], {}),
            'stage_ii_pvalue_fctx': ('django.db.models.fields.FloatField', [], {})
        },
        'datasets.humanbrainmethylationchanges': {
            'Meta': {'object_name': 'HumanBrainMethylationChanges'},
            'adjusted_r2_estimates_from_stage_i_crblm': ('django.db.models.fields.FloatField', [], {}),
            'adjusted_r2_estimates_from_stage_i_fctx': ('django.db.models.fields.FloatField', [], {}),
            'adjusted_r2_estimates_from_stage_i_pons': ('django.db.models.fields.FloatField', [], {}),
            'adjusted_r2_estimates_from_stage_i_tctx': ('django.db.models.fields.FloatField', [], {}),
            'beta_coefficient_range': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'c_g_count': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'chr': ('django.db.models.fields.IntegerField', [], {}),
            'cpg_count': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'cpg_sequence': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cpg_sequence_2kb': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'distance_to_tss': ('django.db.models.fields.IntegerField', [], {}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'genomic_position_in_bp': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'percentage_c_or_g': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'percentage_cpg': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'ratio': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'stage_i_p_value_crblm': ('django.db.models.fields.FloatField', [], {}),
            'stage_i_p_value_fctx': ('django.db.models.fields.FloatField', [], {}),
            'stage_i_p_value_pons': ('django.db.models.fields.FloatField', [], {}),
            'stage_i_p_value_tctx': ('django.db.models.fields.FloatField', [], {}),
            'stage_ii_p_value_crblm': ('django.db.models.fields.FloatField', [], {}),
            'stage_ii_p_value_fctx': ('django.db.models.fields.FloatField', [], {}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'datasets.humangenes': {
            'Meta': {'object_name': 'HumanGenes'},
            'aliases': ('django.db.models.fields.CharField', [], {'max_length': '68', 'blank': 'True'}),
            'band': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'cds_accession': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'cellular_location': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'epd_accession': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'expression': ('django.db.models.fields.CharField', [], {'max_length': '69'}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '94'}),
            'gene_name': ('django.db.models.fields.CharField', [], {'max_length': '131'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'hagrid': ('django.db.models.fields.IntegerField', [], {}),
            'homologene': ('django.db.models.fields.IntegerField', [], {}),
            'homologues': ('django.db.models.fields.TextField', [], {}),
            'hprd': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interactions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'location_end': ('django.db.models.fields.IntegerField', [], {}),
            'location_start': ('django.db.models.fields.IntegerField', [], {}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'observations': ('django.db.models.fields.TextField', [], {}),
            'omim': ('django.db.models.fields.IntegerField', [], {}),
            'orf_accession': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'orientation': ('django.db.models.fields.IntegerField', [], {}),
            'pubmed_ids': ('django.db.models.fields.TextField', [], {}),
            'reference': ('django.db.models.fields.TextField', [], {}),
            'selection_reason': ('django.db.models.fields.CharField', [], {'max_length': '21'}),
            'swiss_prot': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'unigene': ('django.db.models.fields.IntegerField', [], {})
        },
        'datasets.joannegenes': {
            'Meta': {'object_name': 'JoanneGenes'},
            'assoc_gene_name': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'cds_length': ('django.db.models.fields.IntegerField', [], {}),
            'chimp_ensembl_gene_id': ('django.db.models.fields.CharField', [], {'max_length': '19'}),
            'chimp_percentage_id': ('django.db.models.fields.IntegerField', [], {}),
            'dn': ('django.db.models.fields.FloatField', [], {}),
            'dn_ds': ('django.db.models.fields.FloatField', [], {}),
            'ds': ('django.db.models.fields.FloatField', [], {}),
            'ensembl_gene_id': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'human_percentage_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'longevity': ('django.db.models.fields.CharField', [], {'max_length': '18'}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'datasets.k56ac': {
            'Meta': {'object_name': 'K56Ac'},
            'ensembl_gene': ('django.db.models.fields.CharField', [], {'max_length': '9', 'primary_key': 'True'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expression': ('django.db.models.fields.FloatField', [], {}),
            'level': ('django.db.models.fields.FloatField', [], {}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'datasets.murineimprinted': {
            'Meta': {'object_name': 'MurineImprinted'},
            'chromosome': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'chromosome_region': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expressed_parental_allele': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'gene_name': ('django.db.models.fields.CharField', [], {'max_length': '74'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'datasets.newlongevityregulators': {
            'Meta': {'object_name': 'NewLongevityRegulators'},
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phenotype': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'wormbase_id': ('django.db.models.fields.CharField', [], {'max_length': '14'})
        },
        'datasets.newlongevityregulatorscandidates': {
            'Meta': {'object_name': 'NewLongevityRegulatorsCandidates'},
            'ensembl_gene_id': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gene_symbol': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wormbase_id': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'})
        },
        'datasets.oneyrcbspecific': {
            'Meta': {'object_name': 'OneyrCbSpecific'},
            'chr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'end': ('django.db.models.fields.IntegerField', [], {}),
            'gene': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_value': ('django.db.models.fields.FloatField', [], {}),
            'peak': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'seq': ('django.db.models.fields.TextField', [], {}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        },
        'datasets.oneyrhippspecific': {
            'Meta': {'object_name': 'OneyrHippSpecific'},
            'chr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'end': ('django.db.models.fields.IntegerField', [], {}),
            'gene': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_value': ('django.db.models.fields.FloatField', [], {}),
            'peak': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'seq': ('django.db.models.fields.TextField', [], {}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        },
        'datasets.p7cbdynamic': {
            'Meta': {'object_name': 'P7CbDynamic'},
            'chr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'end': ('django.db.models.fields.IntegerField', [], {}),
            'gene': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_value': ('django.db.models.fields.FloatField', [], {}),
            'peak': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'seq': ('django.db.models.fields.TextField', [], {}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        },
        'datasets.p7hippdynamic': {
            'Meta': {'object_name': 'P7HippDynamic'},
            'chr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'end': ('django.db.models.fields.IntegerField', [], {}),
            'gene': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_value': ('django.db.models.fields.FloatField', [], {}),
            'peak': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'seq': ('django.db.models.fields.TextField', [], {}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        },
        'datasets.pokholok': {
            'Meta': {'object_name': 'Pokholok'},
            'chr': ('django.db.models.fields.IntegerField', [], {}),
            'ensembl_gene': ('django.db.models.fields.CharField', [], {'max_length': '19'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'esa1_ypd': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'gcn4_aa': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'gcn5_ypd': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'gg_ypd': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'h3_h2o2': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'h3_ypd': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'h3k14acvsh3_h2o2': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'h3k14acvsh3_ypd': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'h3k14acvswce_ypd': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'h3k36me3vsh3_ypd': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'h3k4me1vsh3_ypd': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'h3k4me2vsh3_ypd': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'h3k4me3vsh3_ypd': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'h3k79me3vsh3_ypd': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'h3k9acvsh3_ypd': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'h4_ypd': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'h4acvsh3_h2o2': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'h4acvsh3_ypd': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'noab_ypd': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'pos': ('django.db.models.fields.IntegerField', [], {})
        },
        'datasets.reference': {
            'Meta': {'object_name': 'Reference'},
            'abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'access_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'accession_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'alternate_journal': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'article_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author_address': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'authors': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'call_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'database_provider': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'doi': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'epub_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'issue': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'legal_note': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_of_database': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'nihmsid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'original_publication': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'pmcid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pmid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'reprint_edition': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'research_notes': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'reviewed_items': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'start_page': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'translated_author': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'type_of_article': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'datasets.signature': {
            'Meta': {'object_name': 'Signature'},
            'age': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'control': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'ctr': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exp': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'experimental': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'fold_change': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'p_value': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'tissue': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        'datasets.survivinginthecold': {
            'Meta': {'object_name': 'SurvivingInTheCold'},
            'embl': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'entrez_gene_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locus_tag': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'mapping': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'protein_accession_number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sgd_id': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'datasets.ultradian': {
            'Meta': {'object_name': 'Ultradian'},
            'component': ('django.db.models.fields.CharField', [], {'max_length': '65', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '243'}),
            'f': ('django.db.models.fields.IntegerField', [], {}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '165', 'blank': 'True'}),
            'gene': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'o': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'orf': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'process': ('django.db.models.fields.CharField', [], {'max_length': '225', 'blank': 'True'})
        },
        'lifespan.assay': {
            'Meta': {'object_name': 'Assay'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'shortcut': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'lifespan.regimen': {
            'Meta': {'object_name': 'Regimen'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'shortcut': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['datasets']