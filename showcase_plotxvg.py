import os
from pathlib import Path
import subprocess


viewxvg_cmd = "python plotxvg"

outputdir = Path("plotXVG_output")
outputdir.mkdir(parents=True, exist_ok=True)

#Define examples of using the flags in a list of dictionaries
examples = [
    {
        "name":"default",
        "description":"This plot is created without flags. Default setting is to make a scatterplot.",
        "inputfile":"gmx_xvgfiles/2dproj_PC1_PC2.xvg",
        "cmd":f"{viewxvg_cmd} -f gmx_xvgfiles/2dproj_PC1_PC2.xvg -save {outputdir}/00default.pdf -noshow"
    }
]

#There are multiple ways ad combinations of using the flags. Here they are added more efficiently in a for-loop
all_examples = [
    ("only_lines", "Using lines", "gmx_xvgfiles/potential_energy.xvg", "-ls solid"),
    ("markers_5datasets", "One file containing five datasets, without any flags added (will thus be plotted using markers).", "modified_xvgfiles/ammonium#chloride.xvg", ""),
    ("lines_4datasets", "User-defined lines", "gmx_xvgfiles/gyrate.xvg", "-ls dotted solid dashed dashdot"),
    ("mk_and_ls", "Both markers and linetyles combined in the same plot. Note how markers and lines can be used separately and combined", "modified_xvgfiles/ammonium#chloride.xvg", "-ls solid dashed solid None None -mk None None x + ."),

    ("two_panels", "Using the panels flag", "gmx_xvgfiles/rmsd_calpha.xvg gmx_xvgfiles/rmsd_sidechain.xvg", "-panels -ls solid "),
    ("mult_panels", "Panels that shows differently expressed data, such as two with lines and two with markers.\nFont- line- or marker-sizing are dynamic based on the number of subplot columns, but specified at will, by \nfor example adding -mksize 20 -mkwidth 4 in a subplot of two columns.", "gmx_xvgfiles/rmsd_calpha.xvg gmx_xvgfiles/temp_press.xvg gmx_xvgfiles/gyrate.xvg gmx_xvgfiles/2dproj_PC1_PC2.xvg", "-panels -ls solid solid solid solid dotted dashdot dashed None -mk None None None o + x ^ + -tfs 40 -alfs 35 -mksize 20 -mkwidth 4"),

    ("colors","A custom choice of colors. Colors defined by the user will be applied to the datasets in order. \nIf there are more datasets than color inputs, default colors will be used.", "gmx_xvgfiles/intra_energies.xvg", "-colors green purple red"),

    ("equalaxes", "Demonstrates the equal axes flag. This flag makes the plot square with equally large axes.\nAlso note the possibility to create user-defined titles.", "act_xvgfiles/COULOMB-PC-allelec.xvg", "-title 'Coulomb energies from ACT training' -dslegends 'PC-allelec' -eqax"),
    ("squarefig","Demonstrates the square figure flag. This flag simply makes the saved figure square.", "gmx_xvgfiles/rmsd_calpha.xvg gmx_xvgfiles/temp_press.xvg gmx_xvgfiles/gyrate.xvg gmx_xvgfiles/2dproj_PC1_PC2.xvg", "-panels -ls solid solid solid solid dotted dashdot dashed None -mk None None None o + x ^ + -mksize 20 -mkwidth 4 -sqfig"),

    ("stats","Shows statistics (RMSD, R\u00b2). If R\u00b2 is close to 1 more digits are added.\nAlso note -sharelabel, which removes axis labels except for the first column and the last row. Suitable if all subplots shares the same axis labels.", "act_xvgfiles/COULOMB-PC-elec.xvg act_xvgfiles/COULOMB-PC-allelec.xvg act_xvgfiles/COULOMB-PC+GS-elec.xvg act_xvgfiles/COULOMB-PC+GS-allelec.xvg", "-dslegends PC-elec PC-allelec PC+GS-elec PC+GS-allelec -alfs 38 -lfs 19 -panels -sharelabel -sqfig -stats"),
    ("res", "Plots the residual of the data, meaning x is substracted from y for all data sets.\nStatistics are based on original train and test values and will not be affected by the residual flag.", "act_xvgfiles/COULOMB-PC-elec.xvg act_xvgfiles/COULOMB-PC-allelec.xvg act_xvgfiles/COULOMB-PC+GS-elec.xvg act_xvgfiles/COULOMB-PC+GS-allelec.xvg", "-dslegends PC-elec PC-allelec PC+GS-elec PC+GS-allelec -alfs 38 -lfs 19 -panels -sharelabel -sqfig -stats -res"),

    ("bar", "Histogram with one dataset", "gmx_xvgfiles/rmsf_residues.xvg", "-bar"),
    ("threebars", "Histogram with three datasets", "modified_xvgfiles/rmsf_res_66-76.xvg modified_xvgfiles/rmsf_res_66-76x1.2.xvg modified_xvgfiles/rmsf_res_66-76x0.8.xvg", "-bar"),

    ("font","Change the font for all texts.", "gmx_xvgfiles/2dproj_PC1_PC2.xvg", "-font Tahoma"),

    ("Alot_of_panels", "This demonstrates the dynamics of the program showing that even twelve files can be plotted simultaneously.", "gmx_xvgfiles/eigenval.xvg gmx_xvgfiles/gyrate.xvg gmx_xvgfiles/potential_energy.xvg gmx_xvgfiles/2dproj_PC1_PC2.xvg gmx_xvgfiles/resarea.xvg gmx_xvgfiles/rmsd_backbone.xvg gmx_xvgfiles/rmsd_calpha.xvg gmx_xvgfiles/rmsd_sidechain.xvg gmx_xvgfiles/rmsf_residues.xvg gmx_xvgfiles/sasa_total.xvg gmx_xvgfiles/temp_press.xvg gmx_xvgfiles/intra_energies.xvg", "-mk x None None None None None '*' None None None None None o None None None o x ^ -ls None solid dashed dashdot solid solid None solid dashed solid solid solid None solid solid solid solid solid solid -panels")


]
setcount = 1
for name, desc, inp, flags in all_examples:
    examples.append({
        "name": name,
        "description": desc,
        "inputfile": inp,
        "cmd": f"{viewxvg_cmd} -f {inp} {flags} -save {outputdir}/0{setcount}{name}.pdf -noshow" #adding noshow flag so that matplotlib doesn't open every single plot during run
    })
    setcount += 1

# Run viewxvg with all the examples
setcount = 0
for ex in examples:
    print(f"Generating {ex['name']}")
    cmd = ex["cmd"]
    
    # Run command
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run {cmd}:\n{e}")
        continue

    # Save command text
    with open(outputdir/f"0{setcount}{ex['name']}_command.txt", "w") as f:
        f.write("Description:\n" + ex["description"] + "\n")
        f.write("File(s) used:\n" + ex["inputfile"] + "\n")
        f.write("Command:\n" + cmd + "\n")
    setcount += 1
print("Done.")