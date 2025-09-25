# Emission Spectrum Look-Up Table Generator

## Description
This Python script generates an emission spectrum look-up table based on the absorption and emission spectra of a luminophore. The resulting table can be uploaded directly into **LightTools** for optical simulations.

Because LightTools inherently interprets overlapping absorption and emission regions as *anti-Stokes behavior* in phosphor particles, the script automatically truncates the emission spectrum for wavelengths shorter than the excitation wavelength. This ensures correct handling of the spectral data inside LightTools.

The script also formats the look-up table and adds a **file header** containing the required metadata so the output can be uploaded into LightTools without further editing.

---

## Requirements
- Python 3.7+
- `numpy`, `pandas` (if used by your script)

Install dependencies (example):
    pip install numpy pandas

---

## Usage
1. Add the absorption and emission spectra of the desired luminophore as text files to the folder `spectra`, using the names `absorption.txt` and `emission.txt`.
2. Run the script:
    python remove_overlap.py
   This will create a text file named `emission_adjusted.txt` containing the LightTools-compatible look-up table.
3. In LightTools:
   - Add a particle to a material under **Add Particle > Phosphor**  
   - In the phosphor particle properties, go to **Emission Spectra** and click **Load File**  
   - Upload `emission_adjusted.txt`

---

## Example
An example absorption and emission spectrum is included for the organic luminophore **Lumogen F Red 305**. This dye is commonly used in Luminescent Solar Concentrator (LSC) devices. Because its spectra overlap significantly in the 550–650 nm region, it serves as an excellent example of the truncation technique implemented in this script.

---

## License
MIT License (or choose your preferred license)
