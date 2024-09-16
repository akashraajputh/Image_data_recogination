import re

def parse_entity_value(text, entity_name):
    # Extract value and unit from text using regex
    pattern = r'(\d+\.?\d*)\s*(\w+)'
    match = re.search(pattern, text.lower())
    if match:
        value, unit = match.groups()
        value = float(value)
        # Standardize units based on entity_name
        if unit in entity_unit_map.get(entity_name, {}):
            return value, unit
    return None, None

def standardize_data(df):
    standardized_data = []
    for _, row in df.iterrows():
        entity_name = row['entity_name']
        text = row['extracted_text']
        value, unit = parse_entity_value(text, entity_name)
        standardized_data.append({
            'index': row['index'],
            'entity_name': entity_name,
            'value': value,
            'unit': unit
        })
    return pd.DataFrame(standardized_data)
