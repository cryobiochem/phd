import pickle, inspect, re
import pyeq3
import numpy, scipy

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from mpl_toolkits.mplot3d import  Axes3D
from matplotlib import cm # to colormap 3D surfaces from blue to red
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import ttk as ttk
from tkinter import messagebox as tk_mbox
import tkinter.scrolledtext as tk_stxt
import XYscrolledtext as xy_stxt


textboxWidth = 60 # units are characters
textboxHeight = 12 # units are characters

graphWidth = 800 # units are pixels
graphHeight = 600 # units are pixels

# 3D contour plot lines
numberOfContourLines = 10

# this is used in several reports
def DataArrayStatisticsReport(parent, titleString, tempdata):
    scrolledText = tk_stxt.ScrolledText(parent, width=textboxWidth, height=textboxHeight, wrap=tk.NONE)
    scrolledText.insert(tk.END, titleString + '\n\n')
    
    # must at least have max and min
    minData = min(tempdata)
    maxData = max(tempdata)
    
    if maxData == minData:
        scrolledText.insert(tk.END, 'All data has the same value,\n')
        scrolledText.insert(tk.END, "value = %-.16E\n" % (minData))
        scrolledText.insert(tk.END, 'statistics cannot be calculated.')
    else:
        scrolledText.insert(tk.END, "max = %-.16E\n" % (maxData))
        scrolledText.insert(tk.END, "min = %-.16E\n" % (minData))
        
        try:
            temp = scipy.mean(tempdata)
            scrolledText.insert(tk.END, "mean = %-.16E\n" % (temp))
        except:
            scrolledText.insert(tk.END, "mean gave error in calculation\n")

        try:
            temp = scipy.stats.sem(tempdata)
            scrolledText.insert(tk.END, "standard error of mean = %-.16E\n" % (temp))
        except:
            scrolledText.insert(tk.END, "standard error of mean gave error in calculation\n")

        try:
            temp = scipy.median(tempdata)
            scrolledText.insert(tk.END, "median = %-.16E\n" % (temp))
        except:
            scrolledText.insert(tk.END, "median gave error in calculation\n")

        try:
            temp = scipy.var(tempdata)
            scrolledText.insert(tk.END, "variance = %-.16E\n" % (temp))
        except:
            scrolledText.insert(tk.END, "variance gave error in calculation\n")

        try:
            temp = scipy.std(tempdata)
            scrolledText.insert(tk.END, "std. deviation = %-.16E\n" % (temp))
        except:
            scrolledText.insert(tk.END, "std. deviation gave error in calculation\n")

        try:
            temp = scipy.stats.skew(tempdata)
            scrolledText.insert(tk.END, "skew = %-.16E\n" % (temp))
        except:
            scrolledText.insert(tk.END, "skew gave error in calculation\n")

        try:
            temp = scipy.stats.kurtosis(tempdata)
            scrolledText.insert(tk.END, "kurtosis = %-.16E\n" % (temp))
        except:
            scrolledText.insert(tk.END, "kurtosis gave error in calculation\n")
            
    return scrolledText
    

def CoefficientAndFitStatistics(parent, equation):
    scrolledText = tk_stxt.ScrolledText(parent, width=80, height=25, wrap=tk.NONE)
    if equation.upperCoefficientBounds or equation.lowerCoefficientBounds:
        scrolledText.insert(tk.END, 'This model has coefficient bounds. Parameter statistics may\n')
        scrolledText.insert(tk.END, 'not be valid for parameter values at or near the bounds.\n')
        scrolledText.insert(tk.END, '\n')
    
    scrolledText.insert(tk.END, 'Degress of freedom error ' + str(equation.df_e) + '\n')
    scrolledText.insert(tk.END, 'Degress of freedom regression ' + str(equation.df_r) + '\n')
    
    if equation.rmse == None:
        scrolledText.insert(tk.END, 'Root Mean Squared Error (RMSE): n/a\n')
    else:
        scrolledText.insert(tk.END, 'Root Mean Squared Error (RMSE): ' + str(equation.rmse) + '\n')
    
    if equation.r2 == None:
        scrolledText.insert(tk.END, 'R-squared: n/a\n')
    else:
        scrolledText.insert(tk.END, 'R-squared: ' + str(equation.r2) + '\n')
    
    if equation.r2adj == None:
        scrolledText.insert(tk.END, 'R-squared adjusted: n/a\n')
    else:
        scrolledText.insert(tk.END, 'R-squared adjusted: ' + str(equation.r2adj) + '\n')
    
    if equation.Fstat == None:
        scrolledText.insert(tk.END, 'Model F-statistic: n/a\n')
    else:
        scrolledText.insert(tk.END, 'Model F-statistic: ' + str(equation.Fstat) + '\n')
    
    if equation.Fpv == None:
        scrolledText.insert(tk.END, 'Model F-statistic p-value: n/a\n')
    else:
        scrolledText.insert(tk.END, 'Model F-statistic p-value: ' + str(equation.Fpv) + '\n')
    
    if equation.ll == None:
        scrolledText.insert(tk.END, 'Model log-likelihood: n/a\n')
    else:
        scrolledText.insert(tk.END, 'Model log-likelihood: ' + str(equation.ll) + '\n')
    
    if equation.aic == None:
        scrolledText.insert(tk.END, 'Model AIC: n/a\n')
    else:
        scrolledText.insert(tk.END, 'Model AIC: ' + str(equation.aic) + '\n')
    
    if equation.bic == None:
        scrolledText.insert(tk.END, 'Model BIC: n/a\n')
    else:
        scrolledText.insert(tk.END, 'Model BIC: ' + str(equation.bic) + '\n')
    
    
    scrolledText.insert(tk.END, '\n')
    scrolledText.insert(tk.END, "Individual Parameter Statistics:\n")
    for i in range(len(equation.solvedCoefficients)):
        if type(equation.tstat_beta) == type(None):
            tstat = 'n/a'
        else:
            tstat = '%-.5E' %  (equation.tstat_beta[i])
    
        if type(equation.pstat_beta) == type(None):
            pstat = 'n/a'
        else:
            pstat = '%-.5E' %  ( equation.pstat_beta[i])
    
        if type(equation.sd_beta) != type(None):
            scrolledText.insert(tk.END, "Coefficient %s = %-.16E, std error: %-.5E\n" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i], equation.sd_beta[i]))
        else:
            scrolledText.insert(tk.END, "Coefficient %s = %-.16E, std error: n/a\n" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i]))
        scrolledText.insert(tk.END, "          t-stat: %s, p-stat: %s, 95 percent confidence intervals: [%-.5E, %-.5E]\n" % (tstat,  pstat, equation.ci[i][0], equation.ci[i][1]))
            
    scrolledText.insert(tk.END, '\n')
    scrolledText.insert(tk.END, "Coefficient Covariance Matrix:\n")
    for i in  equation.cov_beta:
        scrolledText.insert(tk.END, str(i) + '\n')
        
    return scrolledText


def CoefficientListing(parent, equation):
    scrolledText = tk_stxt.ScrolledText(parent, width=textboxWidth, height=textboxHeight, wrap=tk.NONE)
    cd = equation.GetCoefficientDesignators()
    for i in range(len(equation.solvedCoefficients)):
        scrolledText.insert(tk.END, "%s = %-.16E\n" % (cd[i], equation.solvedCoefficients[i]))

    return scrolledText


def SourceCodeReport(parent, equation, lanuageNameString):
    scrolledText = tk_stxt.ScrolledText(parent, width=textboxWidth, height=textboxHeight, wrap=tk.NONE)    
    code = eval('pyeq3.outputSourceCodeService().GetOutputSourceCode' + lanuageNameString + '(equation)')
    scrolledText.insert(tk.END, code)
    
    return scrolledText


def AbsoluteErrorGraph(parent, equation):
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    canvas = FigureCanvasTkAgg(f, master=parent)
    axes = f.add_subplot(111)
    dep_data = equation.dataCache.allDataCacheDictionary['DependentData']
    abs_error = equation.modelAbsoluteError
    axes.plot(dep_data, abs_error, 'D')
    
    if equation.GetDimensionality() == 2: # used for labels only
        axes.set_title('Absolute Error vs. X Data')
        axes.set_xlabel('X Data')
    else:
        axes.set_title('Absolute Error vs. Z Data')
        axes.set_xlabel('Z Data')
        
    axes.set_ylabel(" Absolute Error") # Y axis label is always absolute error

    canvas.draw()
    plt.close('all') # clean up after using pyplot or else thaere can be memory and process problems
    
    return [canvas.get_tk_widget(), f]


def PercentErrorGraph(parent, equation):
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    canvas = FigureCanvasTkAgg(f, master=parent)
    axes = f.add_subplot(111)
    dep_data = equation.dataCache.allDataCacheDictionary['DependentData']
    per_error = equation.modelPercentError
    axes.plot(dep_data, per_error, 'D')
    
    if equation.GetDimensionality() == 2: # used for labels only
        axes.set_title('Percent Error vs. X Data')
        axes.set_xlabel('X Data')
    else:
        axes.set_title('Percent Error vs. Z Data')
        axes.set_xlabel('Z Data')
        
    axes.set_ylabel(" Percent Error") # Y axis label is always percent error

    canvas.draw()
    plt.close('all') # clean up after using pyplot or else thaere can be memory and process problems
    return [canvas.get_tk_widget(), f]


def AbsoluteErrorHistogram(parent, equation):
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    canvas = FigureCanvasTkAgg(f, master=parent)
    axes = f.add_subplot(111)
    abs_error = equation.modelAbsoluteError
    bincount = len(abs_error)//2 # integer division
    if bincount < 5:
        bincount = 5
    if bincount > 25:
        bincount = 25
    n, bins, patches = axes.hist(abs_error, bincount, rwidth=0.8)
    
    # some axis space at the top of the graph
    ylim = axes.get_ylim()
    if ylim[1] == max(n):
        axes.set_ylim(0.0, ylim[1] + 1)

    axes.set_title('Absolute Error Histogram') # add a title
    axes.set_xlabel('Absolute Error') # X axis data label
    axes.set_ylabel(" Frequency") # Y axis label is frequency

    canvas.draw()
    plt.close('all') # clean up after using pyplot or else thaere can be memory and process problems
    return [canvas.get_tk_widget(), f]


def PercentErrorHistogram(parent, equation):
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    canvas = FigureCanvasTkAgg(f, master=parent)
    axes = f.add_subplot(111)
    per_error = equation.modelPercentError
    bincount = len(per_error)//2 # integer division
    if bincount < 5:
        bincount = 5
    if bincount > 25:
        bincount = 25
    n, bins, patches = axes.hist(per_error, bincount, rwidth=0.8)
    
    # some axis space at the top of the graph
    ylim = axes.get_ylim()
    if ylim[1] == max(n):
        axes.set_ylim(0.0, ylim[1] + 1)

    axes.set_title('Percent Error Histogram') # add a title
    axes.set_xlabel('Percent Error') # X axis data label
    axes.set_ylabel(" Frequency") # Y axis label is frequency

    canvas.draw()
    plt.close('all') # clean up after using pyplot or else thaere can be memory and process problems
    return [canvas.get_tk_widget(), f]


def ModelScatterConfidenceGraph(parent, equation, scatterplotOnlyFlag):
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    canvas = FigureCanvasTkAgg(f, master=parent)
    axes = f.add_subplot(111)
    y_data = equation.dataCache.allDataCacheDictionary['DependentData']
    x_data = equation.dataCache.allDataCacheDictionary['IndependentData'][0]

    # first the raw data as a scatter plot
    axes.plot(x_data, y_data,  'D')

    if not scatterplotOnlyFlag:
        # create data for the fitted equation plot
        xModel = numpy.linspace(min(x_data), max(x_data))

        tempcache = equation.dataCache # store the data cache
        equation.dataCache = pyeq3.dataCache()
        equation.dataCache.allDataCacheDictionary['IndependentData'] = numpy.array([xModel, xModel])
        equation.dataCache.FindOrCreateAllDataCache(equation)
        yModel = equation.CalculateModelPredictions(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
        equation.dataCache = tempcache # restore the original data cache

        # now the model as a line plot
        axes.plot(xModel, yModel)

        # now calculate confidence intervals
        # http://support.sas.com/documentation/cdl/en/statug/63347/HTML/default/viewer.htm#statug_nlin_sect026.htm
        # http://www.staff.ncl.ac.uk/tom.holderness/software/pythonlinearfit
        mean_x = numpy.mean(x_data)
        n = equation.nobs

        t_value = scipy.stats.t.ppf(0.975, equation.df_e) # (1.0 - (a/2)) is used for two-sided t-test critical value, here a = 0.05

        confs = t_value * numpy.sqrt((equation.sumOfSquaredErrors/equation.df_e)*(1.0/n + (numpy.power((xModel-mean_x),2.0)/
                                                                                           ((numpy.sum(numpy.power(x_data,2.0)))-n*(numpy.power(mean_x,2.0))))))

        # get lower and upper confidence limits based on predicted y and confidence intervals
        upper = yModel + abs(confs)
        lower = yModel - abs(confs)

        # mask off any numbers outside the existing plot limits
        booleanMask = yModel > axes.get_ylim()[0]
        booleanMask &= (yModel < axes.get_ylim()[1])

        # color scheme improves visibility on black background lines or points
        axes.plot(xModel[booleanMask], lower[booleanMask], linestyle='solid', color='white')
        axes.plot(xModel[booleanMask], upper[booleanMask], linestyle='solid', color='white')
        axes.plot(xModel[booleanMask], lower[booleanMask], linestyle='dashed', color='blue')
        axes.plot(xModel[booleanMask], upper[booleanMask], linestyle='dashed', color='blue')

    if not scatterplotOnlyFlag:
        axes.set_title('Model With 95% Confidence Intervals') # add a title
    else:
        axes.set_title('Scatter Plot') # add a title
    axes.set_xlabel('X Data') # X axis data label
    axes.set_ylabel('Y Data') # Y axis data label

    canvas.draw()
    plt.close('all') # clean up after using pyplot or else thaere can be memory and process problems
    return [canvas.get_tk_widget(), f]


def SurfacePlot(parent, equation):
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    canvas = FigureCanvasTkAgg(f, master=parent)
    
    matplotlib.pyplot.grid(True)
    axes = Axes3D(f)
    x_data = equation.dataCache.allDataCacheDictionary['IndependentData'][0]
    y_data = equation.dataCache.allDataCacheDictionary['IndependentData'][1]
    z_data = equation.dataCache.allDataCacheDictionary['DependentData']

            
    xModel = numpy.linspace(min(x_data), max(x_data), 20)
    yModel = numpy.linspace(min(y_data), max(y_data), 20)
    X, Y = numpy.meshgrid(xModel, yModel)

    tempcache = equation.dataCache # store the data cache
    equation.dataCache = pyeq3.dataCache()
    equation.dataCache.allDataCacheDictionary['IndependentData'] = numpy.array([X, Y])
    equation.dataCache.FindOrCreateAllDataCache(equation)
    Z = equation.CalculateModelPredictions(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    equation.dataCache = tempcache# restore the original data cache

    axes.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=1, antialiased=True, alpha=0.75)

    axes.scatter(x_data, y_data, z_data, depthshade=False, color='k')

    axes.set_title('Surface Plot (click-drag with mouse)') # add a title for surface plot
    axes.set_xlabel('X Data') # X axis data label
    axes.set_ylabel('Y Data') # Y axis data label
    axes.set_zlabel('Z Data') # Z axis data label

    canvas.draw()
    plt.close('all') # clean up after using pyplot or else thaere can be memory and process problems
    return [canvas.get_tk_widget(), f]


def ContourPlot(parent, equation):
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    canvas = FigureCanvasTkAgg(f, master=parent)
    axes = f.add_subplot(111)

    x_data = equation.dataCache.allDataCacheDictionary['IndependentData'][0]
    y_data = equation.dataCache.allDataCacheDictionary['IndependentData'][1]
    z_data = equation.dataCache.allDataCacheDictionary['DependentData']

    # filter out huge and minimal numbers for messing up the contour plot
    z_data[z_data > numpy.log(525600)] = numpy.log(525600)
    z_data[z_data < numpy.log(1/60)] = numpy.log(1/60)

    xModel = numpy.linspace(min(x_data), max(x_data), 20)
    yModel = numpy.linspace(min(y_data), max(y_data), 20)
    X, Y = numpy.meshgrid(xModel, yModel)
        
    tempcache = equation.dataCache # store the data cache
    equation.dataCache = pyeq3.dataCache()
    equation.dataCache.allDataCacheDictionary['IndependentData'] = numpy.array([X, Y])
    equation.dataCache.FindOrCreateAllDataCache(equation)
    Z = equation.CalculateModelPredictions(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    equation.dataCache = tempcache # restore the original data cache
        
    #axes.plot(x_data, y_data, '.')

    #axes.set_title('Contour Plot') # add a title for contour plot
    axes.set_xlabel('FucoPol concentration (wt.%)', fontsize=17, fontname='Arial', fontweight='bold') # X axis data label
    axes.set_ylabel('Working temperature (ºC)', fontsize=17, fontname='Arial', fontweight='bold') # Y axis data label
    #axes.set_ylim(-15,-4)

    for label in (axes.get_xticklabels() + axes.get_yticklabels()):
        label.set_fontsize(14)
        label.set_fontname('Arial')
        label.set_fontweight('bold')

    axes.spines["top"].set_linewidth(3)
    axes.spines["left"].set_linewidth(3)
    axes.spines["right"].set_linewidth(3)
    axes.spines["bottom"].set_linewidth(3)

    # Define levels in z-axis where we want lines to appear
    levels = numpy.array(numpy.log([1/60, 1, 60, 1440, 10080, 40320, 525600]))

    # Generate a color mapping of the levels we've specified
    cmap = matplotlib.cm.RdBu_r  # define the colormap
    # extract all colors from the .jet map
    cmaplist = [cmap(i) for i in range(cmap.N)]

    # create the new map
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        'Custom cmap', cmaplist, cmap.N)

    # define the bins and normalize
    #bounds = numpy.linspace(-10, 10000000, 256)
    #norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)


    cpf = matplotlib.pyplot.contourf(X, Y, Z, len(levels), cmap='RdBu_r')

   #cb = matplotlib.colorbar.ColorbarBase(X,Y,Z, cmap=cmap, norm=norm,
   #                               spacing='proportional', ticks=bounds, boundaries=bounds, format='%1i')

    # Set all level lines to black
    line_colors = ['black' for l in cpf.levels]

    CS = matplotlib.pyplot.contour(X, Y, Z, len(levels), colors='k', levels=levels)


    fmt = {}
    strs = ['Second', 'Minute', 'Hour', 'Day', 'Week', 'Month', 'Year']
    for l, s in zip(CS.levels, strs):
        fmt[l] = s


    matplotlib.pyplot.clabel(CS, inline=1, fontsize=12, colors=line_colors, fmt=fmt) # labels for contours
    plt.rcParams["figure.figsize"] = (10,10)
    plt.savefig('contour.tif', dpi=300)
    canvas.draw()
    plt.close('all') # clean up after using pyplot or else thaere can be memory and process problems
    return [canvas.get_tk_widget(), f]


def ScatterPlot(parent, equation):
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    canvas = FigureCanvasTkAgg(f, master=parent)
    
    matplotlib.pyplot.grid(True)
    axes = Axes3D(f)
    x_data = equation.dataCache.allDataCacheDictionary['IndependentData'][0]
    y_data = equation.dataCache.allDataCacheDictionary['IndependentData'][1]
    z_data = equation.dataCache.allDataCacheDictionary['DependentData']
            
    axes.scatter(x_data, y_data, z_data, depthshade=False, color='k')

    axes.set_title('Scatter Plot (click-drag with mouse)')
    axes.set_xlabel('X Data')
    axes.set_ylabel('Y Data')
    axes.set_zlabel('Z Data')

    canvas.draw()
    plt.close('all') # clean up after using pyplot or else thaere can be memory and process problems
    return [canvas.get_tk_widget(), f]


def AllEquationReport(parent, dim):
    xyscrolledText = xy_stxt.XYScrolledText(parent, width=textboxWidth, height=textboxHeight, wrap=tk.NONE)
    xyscrolledText.tag_configure("sup", offset=5) # superscript is +5 pixels
    xyscrolledText.tag_configure("sub", offset=-5) # subscript is -5 pixels
    xyscrolledText.tag_configure("bold", font='-weight bold')
    xyscrolledText.tag_configure("italic", font='-slant italic')
    
    if dim == 2:
        module = pyeq3.Models_2D
    else:
        module = pyeq3.Models_3D
     
    for submodule in inspect.getmembers(module):
        if inspect.ismodule(submodule[1]):
            for equationClass in inspect.getmembers(submodule[1]):
                if inspect.isclass(equationClass[1]):
                    for extendedVersionName in ['Default', 'Offset']:
                        
                        # if the equation *already* has an offset,
                        # do not add an offset version here
                        if (-1 != extendedVersionName.find('Offset')) and (equationClass[1].autoGenerateOffsetForm == False):
                            continue

                        equation = equationClass[1]('SSQABS', extendedVersionName)

                        equationName = equation.GetDisplayName()
                        moduleName = str(dim) + 'D ' + submodule[0]
                        
                        xyscrolledText.insert(tk.END, moduleName, 'bold')
                        xyscrolledText.insert(tk.END, '   ')
                        xyscrolledText.insert(tk.END, equationName, 'italic')
                        xyscrolledText.insert(tk.END, '   ')

                        html = equation.GetDisplayHTML()
                        
                        # html <br> tags become new line characters
                        html = html.replace('<br>', '\n')
                        
                        # display pyeq3's html superscript and subscript tags
                        # tkinter has no native HTML widget, and pyeq3's html os
                        # simple and has no *nested* HTML tags - no recursion needed
                        findIter = re.finditer(r'<su.>|</su.>', html)
                        currentIndex = 0
                        endingIndex = len(html)
                        itemCount = 0
                        for item in findIter:
                            span = item.span()
                            if not itemCount % 2: # text is *not* within HTML tags
                                t = html[currentIndex:span[0]]
                                xyscrolledText.insert(tk.END, t)
                                currentIndex = span[1] # beginning tag
                            else: # text *is* within html tags
                                if html[span[1]-2] == 'b': # subscript tag
                                    tag = 'sub'
                                else: # html superscript tag
                                    tag = 'sup'
                                t = html[currentIndex:span[1]-6]
                                xyscrolledText.insert(tk.END, t, tag)
                                currentIndex = span[1] # ending tag
                            itemCount += 1

                        # any ending text, or if no tags were found
                        if currentIndex < endingIndex:
                            t = html[currentIndex:endingIndex]
                            xyscrolledText.insert(tk.END, t)
                            
                        xyscrolledText.insert(tk.END, '\n')
                        
    return xyscrolledText



if __name__ == "__main__":
    import FittingResultsViewer
    root = tk.Tk()
    interface = FittingResultsViewer.ResultsFrame(root, 'pickledEquationFile')
    interface.pack()
    root.title("Example tkinterFit -  Fitting Results Viewer")
    
    # manually center the application window on the user display
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2) # integer division
    y = (root.winfo_screenheight() // 2) - (height // 2) # integer division
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))        
        
    root.mainloop()
