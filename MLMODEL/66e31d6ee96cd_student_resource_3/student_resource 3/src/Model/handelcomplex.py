def parse_complex_value(text, entity_name):
    # Example: "10 kilogram to 15 kilogram"
    pattern = r'(\d+\.?\d*)\s*(\w+)\s*to\s*(\d+\.?\d*)\s*(\w+)'
    match = re.search(pattern, text.lower())
    if match:
        min_value, min_unit, max_value, max_unit = match.groups()
        if min_unit == max_unit and min_unit in entity_unit_map.get(entity_name, {}):
            return (float(min_value), min_unit), (float(max_value), max_unit)
    return None, None

def process_complex_values(df):
    for index, row in df.iterrows():
        text = row['extracted_text']
        value_range = parse_complex_value(text, row['entity_name'])
        if value_range:
            min_value, max_value = value_range
            df.at[index, 'min_value'] = min_value[0]
            df.at[index, 'max_value'] = max_value[0]
            df.at[index, 'unit'] = min_value[1]
    return df
