# """
#     Default hyperparameters for Cartpole-v0
# """
# # General hyperparameters
# env_name           = 'CartPole-v0'
# render             = False
# gamma              = 0.99       # discount factor
# maxiter            = 3000      # number of learning iterations
# min_trans_per_iter = 1024       # minimum number of transition steps per iteration (if an episode ends before min_trans_per_iter is reached, a new one starts)
#
# # TRPO specific hyperparameters
# kl_bound           = 0.001
# ent_bound          = 0.0005
# cg_damping         = 1e-1       # conjugate gradient damping (for the diagonal entries)
#
# # Policy network parameters
# pi_sizes           = [64, 64]
# pi_activations     = ['tanh', 'tanh']
# pi_layer_types     = ['dense', 'dense']
# pi_lr              = 1e-4
# pi_batch_size      = 64
#
# # Value network parameters
# v_sizes             = [64, 64, 1]
# v_activations       = ['tanh', 'tanh', None]
# v_layer_types       = ['dense', 'dense', 'dense']
# v_lr                = 1e-4
# v_batch_sizes       = 64
# v_epochs            = 20
# lambda_trace       = 0.95       # coefficient for generalized advantage

"""
    Default hyperparameters for Rock-v0
"""
# General hyperparameters
env_name           = 'Rock-v0'
render             = True
gamma              = 0.99       # discount factor
maxiter            = 600      # number of learning iterations
min_trans_per_iter = 5000       # minimum number of transition steps per iteration (if an episode ends before min_trans_per_iter is reached, a new one starts)

# TRPO specific hyperparameters
kl_bound           = 0.01
ent_bound          = 0.01
cg_damping         = 1e-1       # conjugate gradient damping (for the diagonal entries)

# Policy network parameters
pi_sizes           = [32, 32]
pi_activations     = ['tanh', 'tanh']
pi_layer_types     = ['dense', 'dense']
pi_lr              = 1e-4
pi_batch_size      = 64

# Value network parameters
v_sizes             = [64, 64, 1]
v_activations       = ['tanh', 'tanh', None]
v_layer_types       = ['dense', 'dense', 'dense']
v_lr                = 1e-4
v_batch_sizes       = 64
v_epochs            = 20
lambda_trace       = 0.95       # coefficient for generalized advantage
