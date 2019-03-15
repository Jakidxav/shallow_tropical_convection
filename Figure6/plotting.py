import matplotlib.ticker as ticker
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.transforms as transform
import matplotlib.cm as cm
import cmocean

def plot_contours_latHeight(vmin, vmax, field, contours, cmap, cbar_label, left, right, 
                            p_list, p_label, lon_list, lon_labels, p_tick_list, z_label, figname, savefig):
    fig = plt.figure(figsize=(300, 75))
    fig, ax = plt.subplots()

    Norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    contourf = plt.contourf(field, contours, cmap=cmap, norm=Norm)
    #plt.contour(contourf, colors='black', linewidth=0.5)

    cbar = fig.colorbar(contourf, orientation='horizontal')
    cbar.set_label(cbar_label)
    plt.gca().invert_yaxis()

    ax.set_title(left, loc='left', weight='semibold', size='medium')
    ax.set_title(right, loc='right', weight='semibold', size='medium')
    ax.set_ylabel(p_label)

    ax.set_xticks(lon_list)
    ax.set_xticklabels(lon_labels)
    ax.set_yticks(p_tick_list)
    ax.set_yticklabels(p_list, fontsize=6)

    ax2 = ax.twinx()
    ax2.set_ylim(20, 0)
    ax2.set_ylabel(z_label)

    plt.gca().invert_yaxis()

    #plt.tight_layout()
    if (savefig == True):
        plt.savefig(figname, format='pdf')
    
    plt.tight_layout()
    plt.show()