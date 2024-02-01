def ext_type(file_type, action, OUTPUT_DIR, INPUT):
    file_type_lower = file_type.lower()
    if file_type_lower in ('excel', 'xlsx'):
        file_ext = 'xlsx'
    elif file_type_lower == 'csv':
        file_ext = 'csv'
    elif file_type_lower == 'json':
        file_ext = 'json'
    elif file_type_lower == 'txt':
        file_ext = 'txt'
    else:
        raise ValueError(f"File type {file_type_lower} is not supported or misspelled.")
    return file_ext