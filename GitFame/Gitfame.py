import gitfame
import os

path=os.environ['gitfamepath']
gitfame.main(['--sort=commits', '-wt', path ])