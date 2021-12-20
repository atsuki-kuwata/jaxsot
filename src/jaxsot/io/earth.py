import healpy as hp
import numpy as np
def binarymap(nside=16,show=False):
    """Load a binary map of Earth

    Args:
       nside: nside in Healpix
       show: if True, display a map 

    returns:
       binary map in healpix   
     

    """
    # test map
    mmap=(hp.read_map("../data/mockalbedo"+str(nside)+".fits"))

    mask=(mmap>0.0)
    mmap[mask]=1.0
    mmap=np.asarray(mmap)
    if show:
        import matplotlib.pyplot as plt
        hp.mollview(mmap, title="Cloud-subtracted Earth",flip="geo",cmap=plt.cm.bone,min=0,max=1)
        hp.graticule(color="white")
        plt.show()

    return mmap

if __name__=="__main__":
    mmap=binarymap(nside=16,show=True)
    print(len(mmap[mmap==1.0]))
