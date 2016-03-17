from ccdproc import CCDData
from astropy.stats import sigma_clipped_stats
from photutils import daofind



def source_detection(ccd,fwhm=3.0, sigma=3.0, iters=5, threshold=5.0*std):
	"""
	  Returns an astropy table containing the position of sources within the image.

    Parameters
    ----------------

    array : `numpy.ndarray`
        Image array.

    fwhm : float, optional
        Full-width half-max of stars in the image.

    threshold : float, optional.
    	The absolute image value above which to select sources.

    sigma : float, optional.
    	The number of standard deviations to use as the lower and upper clipping limit. 

    iters : int, optional
    	The number of iterations to perform sigma clipping

    Returns
    -----------

    sources
    	an astropy table of the positions of sources in the image.
        


    """
	data = ccd.data    
	mean, median, std = sigma_clipped_stats(data, sigma=sigma, iters=iters)    
	sources = daofind(data - median,fwhm=fwhm, threshold=threshold)
	return sources
