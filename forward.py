import sys, os
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

from utils import gif_save, natural_key, make_manifold, manifold, make_sphere

if __name__ == '__main__':
    n = 10 # number of iterations in plotting
    b = 1 # domain bound
    k = 20 # number of points
    X, Y, Z = make_manifold(b, k)

    # choose starting points
    m = 25
    z = 2*np.random.rand(m, 3) - 1
    for i in range(m):
        z[i, 2] = manifold(z[i,0], z[i,1])

    # colors
    colors = ['Blues', 'Greens', 'Oranges', 'Purples', 'Reds', 'Brwnyl', 'Burg', 'Mint']
    c = np.random.randint(0, len(colors), size=(m))

    # make folder to save each image (then save folder contents into gif)
    os.makedirs('imgs', exist_ok=True)

    # plotting
    a_track = [1]
    for i in range(1, n):
        # TODO: this is noise schedule, make general class to compare other methods 
        # important: setting the beta term
        beta = 1e-4 + (i-1)*(0.1 - 1e-4)/(n-2)
        a = (1 - beta) * a_track[-1]
        a_track.append(a)
        
        data = [go.Surface(x=X, y=Y, z=Z, colorscale='Greys')]

        # plot sphere
        for j in range(m):
            (xs, ys, zs) = make_sphere(np.sqrt(a_track[-1]) * z[j], np.sqrt(1 - a_track[-1]))
            data.append(go.Surface(x=xs, y=ys, z=zs, colorscale=colors[c[j]]))
            spot = np.random.randint(len(colors))
        fig = go.Figure(data=data)
        fig.update_layout( autosize=False, width=800, height=800,)
        fig.write_image('imgs/img_{}.png'.format(i))

    gif_save('imgs', '../example')
    sys.exit()