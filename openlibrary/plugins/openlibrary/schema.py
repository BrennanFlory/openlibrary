"""OpenLibrary schema."""
from infogami.infobase import dbstore
from infogami import config

def get_schema():
    schema = dbstore.Schema()
    schema.add_table_group('type', '/type/type')
    schema.add_table_group('type', '/type/property')
    schema.add_table_group('type', '/type/backreference')
    schema.add_table_group('user', '/type/user')
    schema.add_table_group('user', '/type/usergroup')
    schema.add_table_group('user', '/type/permission')

    schema.add_table_group('edition', '/type/edition')
    schema.add_table_group('author', '/type/author')
    schema.add_table_group('scan', '/type/scan_location')
    schema.add_table_group('scan', '/type/scan_record')

    schema.add_table_group('work', '/type/work')
    schema.add_table_group('publisher', '/type/publisher')
    schema.add_table_group('subject', '/type/subject')

    if 'upstream' in config.get('features', []):
        schema.add_seq('/type/edition', '/books/OL%dM')
        schema.add_seq('/type/author', '/authors/OL%dA')
    else:
        schema.add_seq('/type/edition', '/b/OL%dM')
        schema.add_seq('/type/author', '/a/OL%dA')

    schema.add_seq('/type/work', '/works/OL%dW')
    schema.add_seq('/type/publisher', '/publishers/OL%dP')
    
    return schema

if __name__ == "__main__":
    print get_schema().sql()
