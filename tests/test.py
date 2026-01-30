import os
from pathlib import Path
import subprocess
import shutil, sys
#Check if the user has installed plotxvg first
if shutil.which("plotxvg") == None:
   sys.exit("Please install plotxvg first")

plotxvg_cmd = "plotxvg"

outputdir = Path("plotxvg_tests-output")
outputdir.mkdir(parents=True, exist_ok=True)

#Define examples of using the flags in a list of dictionaries
examples = [
    {
        "name":"default",
        "description":"This plot is created without flags. Default setting is to make a scatterplot.",
        "inputfile":"gmx_files/rmsd_calpha.xvg",
        "cmd":f"{plotxvg_cmd} -f gmx_files/rmsd_calpha.xvg -save {outputdir}/00default.pdf -noshow"
    }
]

#There are multiple ways ad combinations of using the flags. Here they are added more efficiently in a for-loop
all_examples = [
    ("only_lines", "Using lines", "gmx_files/potential_energy.xvg", "-ls solid"),
    ("markers_5datasets", "One file containing five datasets, without any flags added (will thus be plotted using markers).", "other_files/ammonium#chloride.xvg", ""),
    ("lines_4datasets", "User-defined lines", "gmx_files/gyrate.xvg", "-ls dotted solid dashed dashdot"),
    ("mk_and_ls", "Both markers and linetyles combined in the same plot. Note how markers and lines can be used separately and combined", "other_files/ammonium#chloride.xvg", "-ls solid dashed solid None None -mk None None x + ."),
    ("move_legendbox", "Moving the legendbox to the right. Can also be done along the y-axis.", "other_files/ammonium#chloride.xvg", "-legend_x 0.68"),

    ("two_panels", "Using the panels flag, along with -notitles. Also note -sharelabel, which removes axis labels except for the first column and the last row.\n\tSuitable if all subplots shares the same axis labels.", "gmx_files/rmsd_calpha.xvg gmx_files/rmsd_sidechain.xvg", "-panels -sharelabel -notitles -ls solid "),
    ("mult_panels", "Panels that shows differently expressed data, such as two with lines and two with markers.\n\tFont- line- or marker-sizing are dynamic based on the number of subplot columns, but specified at will, by \n\tfor example adding -mksize 20 -mkwidth 4 in a subplot of two columns.", "gmx_files/rmsd_calpha.xvg gmx_files/temp_press.xvg gmx_files/gyrate.xvg gmx_files/potential_energy.xvg", "-ls solid solid solid solid dotted dashdot dashed solid -mk None None None o + x ^ None -panels -tfs 40 -axfs 35 -mksize 20 -mkwidth 4"),

    ("colors","A custom choice of colors. Colors defined by the user will be applied to the datasets in order. \n\tIf there are more datasets than color inputs, default colors will be used.", "gmx_files/intra_energies.xvg", "-colors green purple red"),

    ("equalaxes", "Demonstrates the equal axes flag. This flag makes the plot square with equally large axes, suitable for correlation plots.\n\tAlso note the possibility to plot panels side-by-side by adding side to the panels flag.", "act_files/COULOMB-PC-elec.xvg act_files/COULOMB-PC+GS-elec.xvg", "-dslegends 'PC-elec' 'PC+GS-elec' -eqax -sharelabel -panels side "),
    ("squarefig","Demonstrates the square figure flag. This flag simply makes the saved figure square.", "gmx_files/rmsd_calpha.xvg gmx_files/temp_press.xvg gmx_files/gyrate.xvg gmx_files/potential_energy.xvg", "-ls solid solid solid solid dotted dashdot dashed solid -mk None None None o + x ^ None -panels -mksize 20 -mkwidth 4 -sqfig"),

    ("stats","Shows statistics (RMSD, R\u00b2). If R\u00b2 is close to 1 more digits are added.\n\tCaution for strange plotting behaviours if the legend is too long or the font is large!", "act_files/COULOMB-PC-elec.xvg act_files/COULOMB-PC-allelec.xvg act_files/COULOMB-PC+GS-elec.xvg act_files/COULOMB-PC+GS-allelec.xvg", "-dslegends PC-elec PC-allelec PC+GS-elec PC+GS-allelec -axfs 38 -lfs 19 -panels -sharelabel -sqfig -stats"),
    ("res", "Plots the residual of the data, meaning x is substracted from y for all data sets.\n\tStatistics are based on original train and test values and will not be affected by the residual flag.", "act_files/COULOMB-PC-elec.xvg act_files/COULOMB-PC-allelec.xvg act_files/COULOMB-PC+GS-elec.xvg act_files/COULOMB-PC+GS-allelec.xvg", "-dslegends PC-elec PC-allelec PC+GS-elec PC+GS-allelec -axfs 38 -lfs 19 -panels -sharelabel -sqfig -stats -res"),

    ("bar", "Histogram with one dataset", "gmx_files/rmsf_residues.xvg", "-bar"),
    ("threebars", "Histogram with three datasets", "other_files/rmsf_res_66-76.xvg other_files/rmsf_res_66-76x1.2.xvg other_files/rmsf_res_66-76x0.8.xvg", "-bar"),

    ("std_plot", "A xvg file containing standard deviations is automatically incorporated as errorbars.", "gmx_files/resarea.xvg", "-ls dotted -mk o"),

    ("font","Change the font for all texts. Here it is changed to 'Tahoma'.", "gmx_files/rmsd_backbone.xvg", "-font Tahoma"),

    ("Alot_of_panels", "This demonstrates the dynamics of the program showing that multiple files can be plotted simultaneously with scaled font and marker sizes. Linestyles and markers can be specified for every dataset but can also be generated automatically typing only one input for ls and mk.", "gmx_files/eigenval.xvg gmx_files/gyrate.xvg gmx_files/potential_energy.xvg gmx_files/resarea.xvg gmx_files/rmsd_backbone.xvg gmx_files/rmsd_sidechain.xvg gmx_files/rmsf_residues.xvg gmx_files/sasa_total.xvg gmx_files/intra_energies.xvg", "-mk o -ls solid -panels"),

    ("openMMfile", "This shows the support for OpenMM csv files. -colx takes one argument while -coly can take multiple (Use strings).", "other_files/openmm.csv", "-colx 2 -coly 7 -ls solid"),

    ("heatmap", "Heatmap of two normal distributions with gibbs free energy calculated by plotxvg.", "other_files/test_normaldist.xvg", "-heatmap -gibbs -cmap inferno"),
    ("contour_kde", "Showcasing the use of matplotlib's contourf and contour and calculation of PDF using kde.", "gmx_files/2dproj_PC1_PC2.xvg", "-contour -kde -showdots"),

    ("fig1_article", "The exact run for reproducing Fig.1 in the article.", "gmx_files/rmsd_calpha.xvg gmx_files/temp_press.xvg", "--linestyle solid None solid --marker None . o -panels top --allfontsizes 6"),
    ("fig2_article", "The exact run for reproducing Fig.2 in the article.", "act_files/COULOMB-PC-elec.xvg act_files/COULOMB-PC+GS-elec.xvg", "-dslegends 'PC-elec' 'PC-elec' 'PC+GS-elec' 'PC+GS-elec' --legendfontsize 18 --equalaxes -panels side -sharelabel -stats"),
    ("fig3_article", "The exact run for reproducing Fig.3 in the article.", "other_files/SL_posteriors.dat", "-heatmap -cmap rainbow --allfontsizes 12"),
    ("fig4_article", "The exact run for reproducing Fig.4 in the article.", "gmx_files/2dproj_PC1_PC2.xvg", "-contour -kde -gibbs -showdots --allfontsizes 12"),

]
setcount = 1
for name, desc, inp, flags in all_examples:
    examples.append({
        "name": name,
        "description": desc,
        "inputfile": inp,
        "cmd": f"{plotxvg_cmd} -f {inp} {flags} -save {outputdir}/{setcount:02d}{name}.pdf -noshow" #adding noshow flag so that matplotlib doesn't open every single plot during run
    })
    setcount += 1

# Run plotxvg with all the examples
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
    with open(outputdir/f"{setcount:02d}{ex['name']}_command.txt", "w") as f:
        f.write("Description:\n\t" + ex["description"] + "\n")
        f.write("File(s) used:\n\t" + ex["inputfile"] + "\n")
        f.write("Command:\n\t" + cmd + "\n")
    setcount += 1
print("Done.")