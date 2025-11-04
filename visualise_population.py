import pandas as pd
import matplotlib.pyplot as plt
import zipfile

# ✅ Path to your dataset (must be in the same folder as this script)
zip_path = "API_SP.POP.TOTL_DS2_en_csv_v2_130083.zip"

# --- STEP 1: Automatically find the main data CSV inside the ZIP ---
with zipfile.ZipFile(zip_path, 'r') as z:
    # Print all file names inside the ZIP (for debugging)
    print("Files inside ZIP:", z.namelist())

    # Select the main CSV (ignore metadata files)
    csv_files = [name for name in z.namelist() if name.endswith('.csv')]
    main_csv = [f for f in csv_files if "Metadata" not in f][0]

    # Read the main CSV
    with z.open(main_csv) as f:
        df = pd.read_csv(f, skiprows=4)

# --- STEP 2: Choose year ---
year = '2020'

# --- STEP 3: Define region names ---
regions = [
    'Africa Eastern and Southern', 'Africa Western and Central', 'East Asia & Pacific',
    'Europe & Central Asia', 'Latin America & Caribbean', 'Middle East & North Africa',
    'North America', 'South Asia', 'Sub-Saharan Africa', 'World'
]

# --- STEP 4: Filter and prepare data ---
df_regions = df[df['Country Name'].isin(regions)][['Country Name', year]].dropna()
df_regions[year] = df_regions[year] / 1e9  # convert to billions
df_regions = df_regions.sort_values(by=year, ascending=False)

# --- STEP 5: Plot (VERTICAL bar chart) ---
plt.figure(figsize=(10,6))
bars = plt.bar(df_regions['Country Name'], df_regions[year], color='royalblue')

# Add labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.05,
             f'{height:.2f}B', ha='center', va='bottom', fontsize=9)

# --- STEP 6: Customize ---
plt.title(f'Total Population by Region in {year} (in Billions)', fontsize=13)
plt.xlabel('Region')
plt.ylabel('Total Population (Billions)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# --- STEP 7: Show graph ---
plt.show()
