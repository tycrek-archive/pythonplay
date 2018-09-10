# pythonplay
Giving Python the ability to play games.

Major thanks to [@Sentdex](https://github.com/Sentdex) for his [tutorials on playing games with Python](https://pythonprogramming.net/game-frames-open-cv-python-plays-gta-v/). Without him this would never be possible.

## Introduction

Computers get more and more advanced every year. With new developments in artificial intelligence, we can do amazing things, such as curing disease, advancing R&D, and now... playing games. Pythonplay is a tool that let's you train your computer to play your games for you. It isn't practical in any way, as it doesn't learn the *rules* of the game, but hey, it's cool to see in action!

Pythonplay currently supports driving a car in the bestselling game, Grand Theft Auto 5. It is still very early in development, and can only press 3 keys: A, W, and D. No S? *Where we're going, we don't need brakes... yet.*

## Requirements

All of these requirements are specific. Python 3.6.x must be used for compatibility.

> 64-bit Windows 7, 8, 8.1, 10  
Python 3.6.x 64-bit  
[Script Hook V + Native Trainer for GTA V](https://www.gta5-mods.com/tools/script-hook-v)

If you wish to use your GPU for training (no multi-GPU support right now), follow [this guide](https://www.tensorflow.org/install/install_windows) to set up Tensorflow GPU. The GPU method is much more difficult to set up, but is *ridiculously* faster than CPU training. However, if you want to use a pre-trained model, GPU is **not** required.

**Pip requirements**

    tensorflow
    numpy==1.14.5
    pandas
    opencv-python
    pypiwin32
    tflearn

## How to use

Read the scripts for modification instructions. Also read them to change parameters for filenames.

### 1. Collecting training data

1. Set GTAV to be in **windowed mode at 800x600 resolution**. Put it the the top-left corner of your primary monitor.
2. Using the Native Trainer (NT) menu, ensure your player is Invincible, Never Wanted, Cops Ignored. Make sure that you use the same vehicle (colour and model) for all your training and testing! Using NT menu, make the vehicle Invincible, Strong Wheels, Seatbelt.
3. Using the NT Vehicle menu, select a car to use. This will be the car you use for all training and testing. I recommend the Blista. Then use the Random Paint tool in NT to pick a flashy colour. I used a bright green. This makes it easier for the AI to tell the difference between itself and other objects. Also, 3rd person view is optimal.
4. Use the NT menu to set the Time to around 12:00 (mid-day), and make sure time is stopped to keep 12:00. Make the Weather stay the same, and set it to Extra Sunny or Clear.
4. Open up an **administrator** Command Prompt window in the folder with all the scripts.
5. Run the first script with `python 1.collect_data.py`
6. Quickly click back to GTA; when the script starts working, start driving around San Andreas. To collect good data, try to **avoid** corner-cutting, sidewalks, crashing, drifting, and jumps. As annoying as it is, try to follow lanes, evade cars, stay on the correct side of the road.
7. If you want to PAUSE training at any time, press `t` on your keyboard. To resume, press `t` again. If you get stuck while driving and need to fix the car in any way, pause the training so you don't get bad data.
8. Collect at least 200K frames (200 training files).
9. To quit training, press `t` to pause and then in the Command Prompt window, press `CTRL-C` a few times.

### 2. Balancing training data

1. In an administrator Command Prompt window where the scripts are, run `python 2.balance_data.py`
2. Wait until it completes.
3. You can delete your OLD training files if you want, but don't if you want to continue training with more data later on.

### 3. Training our model

*Training the model can take a very long time using a CPU, so tensorflow-gpu is recommended for this step.*

Depending on the system you have and how much data you collected, **this can take anywhere from a few hours to days, even on a GPU.** If you have an NVIDIA GTX or Tesla GPU, **use it.** Keep in mind that if you use a CPU to train, your computer will act ***very*** slow until training finishes, so don't plan on using it for a while. If you use a GPU to train, you can still use your system, but you **cannot** play games during training. Plan training for overnight or during work/school if you have to.

1. In an administrator Command Prompt window where the scripts are, run `python 3.train_model.py`
2. Go play outside. It's nice out. This will take a while.

### 4. Playing the game

1. Use ALL the same settings from Step 1! Same car, weather, time of day, and window size.
2. In an administrator Command Prompt window where the scripts are, run `python 4.test_model.py`
3. Like with collecting, `t` will pause and unpause the script. This is helpful if the AI gets stuck and needs your help to escape.
4. The AI should now be driving around on its own.

## Known issues

- `Error in CuDNN: CUDNN_STATUS_ALLOC_FAILED`: You do not have enough GPU RAM. In script3, make `BATCH_SIZE` smaller. For script 4, [see this Issue](https://github.com/tycrek/pythonplay/issues/1#issue-358746664)
- "My AI only drives straight!": Collect more data and make it good data, read the tips in Step 1.
- "My AI crashes into stuff all the time!": Read the above issue.
- "I'm having trouble installing Tensorflow GPU" or "I'm getting weird tensorflow errors": **GOOGLE IT**. I didn't make Tensorflow and I barely understand the basics, so I can't exactly help you there.
- "My AI just went on a mass genocide!": Um..... run. Hide.

## Roadmap

- [x] Basic driving in GTA V (forwards, left, right)
- [ ] Advanced driving in GTA V (brakes, reverse, lane changes, crash avoidance)
- [ ] More keyboard keys
- [ ] Mouse interaction
- [ ] Official support for more games

## Contribute

Like this and want to help out? Consider [donating to my PayPal](https://paypal.me/jmoore235) so I can keep development going, or submit a Pull Request if you have code suggestions!