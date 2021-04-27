import yaml

with open('germline_schema.yaml') as fi:
    schema = yaml.load(fi)

with open('germline_schema_tables.tsv', 'w', newline='') as fo:
    for ob_name, ob in schema['definitions'].items():
        fo.write('\n\n%s - %s\n' % (ob_name, ob['description']))
        fo.write('Field\tType\tRequired\tDescription\n')

        for field, props in ob['properties'].items():
            fo.write('%s\t%s\t%s\t%s\n' % (
                field,
                props['type'],
                'Y' if field in ob['required'] else '',
                props['description'] if 'description' in props else ''
            ))

