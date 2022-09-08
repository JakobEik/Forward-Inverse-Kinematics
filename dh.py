import numpy as np

# The 4 D-H parameters
class DHparam:
    def __init__(self, d, theta, a, alpha):
        self.d = d
        self.theta = theta
        self.a = a
        self.alpha = alpha

    def __str__(self):
        return "d={}, theta={}, a={}, alpha={}".format(self.d, self.theta, self.a, self.alpha)

# Get the change-of-frame matrix corresponding to a set of D-H parameters
def to_matrix(dh):
    c_theta = np.cos(dh.theta)
    s_theta = np.sin(dh.theta)
    c_alpha = np.cos(dh.alpha)
    s_alpha = np.sin(dh.alpha)

    return np.array([
        [   c_theta,    -s_theta*c_alpha,   s_theta*s_alpha,    dh.a*c_theta  ],
        [   s_theta,    c_theta*c_alpha,    -c_theta*s_alpha,   dh.a*s_theta  ],
        [   0,          s_alpha,            c_alpha,            dh.d          ],
        [   0,          0,                  0,                  1               ],
    ])
