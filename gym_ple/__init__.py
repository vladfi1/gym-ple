from gym.envs.registration import registry, register, make, spec
from gym_ple.ple_env import PLEEnv
# Pygame
# ----------------------------------------

def registerPLE(game, **kwargs):
    kwargs_ = dict(
      game_name = game,
      display_screen = False,
    )
    kwargs_.update(**kwargs)
    register(
        id='ple/{}-v0'.format(game),
        entry_point='gym_ple:PLEEnv',
        kwargs=kwargs_,
        tags={'wrapper_config.TimeLimit.max_episode_steps': 10000, 'ple': True},
        nondeterministic=False,
    )

for game in ['Catcher', 'MonsterKong', 'FlappyBird', 'PixelCopter', 'PuckWorld', 'RaycastMaze', 'Snake', 'WaterWorld']:
    registerPLE(game)

for game in ['Pong']:
    registerPLE(game+'NV', game_name=game, visual=False)
