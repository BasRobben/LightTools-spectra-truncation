import pandas as pd

# Read data
data_abs = pd.read_csv('spectra/absorption.txt', delim_whitespace=True, header=None, names=['wavelength', 'absorption'])
data_ems = pd.read_csv('spectra/emission.txt', delim_whitespace=True, header=None, names=['wavelength', 'emission'])

# Create a new DataFrame with emission wavelengths as rows
emission_df = pd.DataFrame({'wavelength': data_ems['wavelength']})

# Track excitation wavelengths for columns
excitation_wls = []

for i in range(data_abs.shape[0]):
    excitation_wl = int(data_abs.at[i, 'wavelength'])  # Use integer for column names
    
    if data_abs.at[i, 'absorption'] > 0:
        excitation_wls.append(str(excitation_wl))  # Store excitation wavelength as a string
    
        # Copy emission spectrum
        adjusted_emission = data_ems['emission'].copy()
        
        # Find indices where emission wavelength <= excitation wavelength
        mask = data_ems['wavelength'] <= excitation_wl
        
        # Set emission values before and including excitation wavelength to zero
        adjusted_emission[mask] = 0.0
        
        # Add column for this excitation wavelength
        emission_df[str(excitation_wl)] = adjusted_emission

# Formatting the output file with the required structure
with open("emission_adjusted.txt", "w") as f:
    f.write("dfat version 1.0\n")
    f.write("dataname: Emission Spectra\n")
    f.write("DATAPAIRS: wv inten\n")
    f.write(f"DATASETS: {len(excitation_wls)}\n")
    
    # Write header with excitation wavelengths
    f.write("\t" + "\t".join(excitation_wls) + "\n")

    # Write emission data
    for i in range(emission_df.shape[0]):
        row_values = [f"{emission_df.at[i, 'wavelength']:.0f}"]  # First column: emission wavelength
        row_values += [f"{emission_df.at[i, wl]:.10f}" for wl in excitation_wls]  # Columns for each excitation wavelength
        f.write("\t".join(row_values) + "\n")