import matplotlib.ticker as ticker
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.transforms as transform

import cartopy
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.mpl.ticker as cticker

import matplotlib.cm as cm
import cmocean


"""
Plot latitude-height contours, with dual y-axes: pressure and height coordinates.
"""
def plot_contours_latHeight(field, vmin, vmax, contours, cmap, p_list, p_label, p_tick_list, 
			    z_label, lon_list, lon_labels, left, right, figname, savefig):
    
    fig = plt.figure(figsize=(20, 20))
    fig, ax = plt.subplots()

    Norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    contourf = plt.contourf(field, contours, cmap=cmap, norm=Norm)

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

    if (savefig == True):
        plt.savefig(figname, format='pdf', bbox_inches='tight')
    
    plt.tight_layout()
    plt.show()



"""
Plot a global wind field centered on a specific longitude.
"""
def plot_wind(projection, transform, central_lon, x, y, windx, windy, stride, 
	      lon_list, lat_list, left_title_wind, right_title, figure_name_wind, save_fig):
    
    fig = plt.figure(figsize=(14, 14))
    ax = plt.axes(projection=projection)

    q = ax.quiver(x[::stride], y[::stride], windx[::stride, ::stride], windy[::stride, ::stride],
        minshaft=2, pivot='tip', transform=transform)
        
    ax.coastlines()

    ax.set_xticks(lon_list, crs=transform)
    ax.set_xticklabels(lon_list, weight='bold')
    ax.set_yticks(lat_list, crs=transform)
    ax.set_yticklabels(lat_list, weight='bold')
    ax.yaxis.tick_left()
    
    lon_formatter = cticker.LongitudeFormatter()
    lat_formatter = cticker.LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    ax.grid(linewidth=2, color='black', alpha = 0.5)
    
    ax.set_title(left_title_wind, loc='left', weight='semibold', size='medium')
    ax.set_title(right_title, loc='right', weight='semibold', size='medium')

    if(save_fig==True):
        plt.savefig(figure_name_wind, format='pdf', bbox_inches='tight')
            
    plt.tight_layout()
    plt.show()



"""
Plot a global field centered on a specific longitude
"""
def plot_field(projection, transform, central_lon, x, y, field, vmin, vmax, contours, colormap,
               lon_list, lat_list, left_title, right_title, figure_name, save_fig):
    
    fig = plt.figure(figsize=(14, 14))
    ax = plt.axes(projection=projection)


    Norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    plt1 = ax.contourf(x, y, field, contours, transform=transform, cmap=colormap, norm=Norm)
    cbar = fig.colorbar(plt1, orientation='vertical', shrink=0.2)
    
    ax.coastlines()

    ax.set_xticks(lon_list, crs=transform)
    ax.set_xticklabels(lon_list, weight='bold')
    ax.set_yticks(lat_list, crs=transform)
    ax.set_yticklabels(lat_list, weight='bold')
    ax.yaxis.tick_left()
    
    lon_formatter = cticker.LongitudeFormatter()
    lat_formatter = cticker.LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    ax.grid(linewidth=2, color='black', alpha = 0.5)
    
    ax.set_title(left_title, loc='left', weight='semibold', size='medium')
    ax.set_title(right_title, loc='right', weight='semibold', size='medium')

    if(save_fig==True):
        plt.savefig(figure_name, format='pdf', bbox_inches='tight')
            
    plt.tight_layout()
    plt.show()



"""
Plot a global field centered on a specific longitude, with the option of overlaying wind vectors
"""
def plot_field_wind(projection, transform, central_lon, x, y, field, vmin, vmax, contours, colormap, windx, windy, stride,    			    lon_list, lat_list, left_title, left_title_wind, right_title, figure_name, figure_name_wind, wind_vectors, save_fig):

    fig = plt.figure(figsize=(14, 14))
    ax = plt.axes(projection=projection)


    Norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    plt1 = ax.contourf(x, y, field, contours, transform=transform, cmap=colormap, norm=Norm)
    cbar = fig.colorbar(plt1, orientation='vertical', shrink=0.2)
    
    if(wind_vectors==True):
        q = ax.quiver(x[::stride], y[::stride], windx[::stride, ::stride], windy[::stride, ::stride],
             minshaft=2, pivot='tip', transform=transform)
        
    ax.coastlines()

    ax.set_xticks(lon_list, crs=transform)
    ax.set_xticklabels(lon_list, weight='bold')
    ax.set_yticks(lat_list, crs=transform)
    ax.set_yticklabels(lat_list, weight='bold')
    ax.yaxis.tick_left()
    
    lon_formatter = cticker.LongitudeFormatter()
    lat_formatter = cticker.LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    ax.grid(linewidth=2, color='black', alpha = 0.5)
    
    if(wind_vectors==True):
        ax.set_title(left_title_wind, loc='left', weight='semibold', size='medium')
    else:
        ax.set_title(left_title, loc='left', weight='semibold', size='medium')
    
    ax.set_title(right_title, loc='right', weight='semibold', size='medium')

    if(save_fig==True):
        if(wind_vectors==True):
            plt.savefig(figure_name_wind, format='pdf', bbox_inches='tight')
        else:
            plt.savefig(figure_name, format='pdf', bbox_inches='tight')
            
    plt.tight_layout()
    plt.show()



"""
Run a global t-statistic test, plot contours where the t-stat is >= t_critical
for some significance level.
"""
#plotting method
def plot_field_tstat(projection, transform, central_lon, x, y, t_field, critical_t, vmin, vmax, contours, colormap, 
                       lon_list, lat_list, left_title, right_title, figure_name, save_fig):
    
    fig = plt.figure(figsize=(14, 14))
    ax = plt.axes(projection=projection)

    Norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    plt1 = ax.contourf(x, y, t_field, contours, transform=transform, cmap=colormap, norm=Norm)
    cbar = fig.colorbar(plt1, orientation='vertical', shrink=0.2)

    ax.contour(x, y, t_field>=critical_t, transform=transform, colors='k')
    ax.contour(x, y, t_field<=-critical_t, transform=transform, colors='k')
    
    ax.coastlines()

    ax.set_xticks(lon_list, crs=transform)
    ax.set_xticklabels(lon_list, weight='bold')
    ax.set_yticks(lat_list, crs=transform)
    ax.set_yticklabels(lat_list, weight='bold')
    ax.yaxis.tick_left()
    
    lon_formatter = cticker.LongitudeFormatter()
    lat_formatter = cticker.LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)

    ax.set_title(left_title, loc='left', weight='semibold', size='medium')
    ax.set_title(right_title, loc='right', weight='semibold', size='medium')

    if(save_fig==True):
        plt.savefig(figure_name, format='pdf', bbox_inches='tight')
            
    plt.tight_layout()
    plt.show()





