standardized_df = standardize_data(df)
processed_df = process_complex_values(standardized_df)

# Save or use the processed DataFrame
processed_df.to_csv('/content/processed_data.csv', index=False)